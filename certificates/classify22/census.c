/* Exhaustive connected unlabelled graphs, via vertex extension + canonical labelling.
 * C11, no external libraries. Edges are encoded by columns j=1..n-1,
 * within column i=0..j-1. One representative per isomorphism class.
 * Command: cc -std=c11 -O3 -o /tmp/classify22-census classify22/census.c
 *          /tmp/classify22-census > classify22/census.log
 */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#define MAXN 9
#define CAP (1u<<20)
static uint64_t hash_table[CAP];
static uint64_t *previous, *next;
static size_t count_prev, count_next;
static uint16_t graph[MAXN];
static int colors[MAXN], vertex_order[MAXN], chosen[MAXN], used[MAXN];
static int n_global, edge_bits;
static uint64_t best;

typedef struct {int v, old; int counts[MAXN];} Sig;
static int ncolors_cmp;
static int sigcmp(const void *pa, const void *pb){
    const Sig *a=pa,*b=pb;
    if (a->old != b->old) return a->old-b->old;
    for (int k=0; k<ncolors_cmp; ++k) if(a->counts[k]!=b->counts[k]) return a->counts[k]-b->counts[k];
    return 0;
}
static void refine(void){
    int n=n_global, cnum=0;
    for(int i=0;i<n;i++){
        int d=__builtin_popcount((unsigned)graph[i]);
        colors[i]=d;
    }
    for(int round=0;round<=n+2;round++){
        Sig sig[MAXN];
        ncolors_cmp=n;
        for(int v=0;v<n;v++){
            sig[v].v=v;sig[v].old=colors[v];
            memset(sig[v].counts,0,sizeof(sig[v].counts));
            for(int u=0;u<n;u++) if((graph[v]>>u)&1u) sig[v].counts[colors[u]]++;
        }
        qsort(sig,n,sizeof(Sig),sigcmp);
        int fresh[MAXN], c=0;
        for(int k=0;k<n;k++){
            if(k && sigcmp(&sig[k-1],&sig[k])) c++;
            fresh[sig[k].v]=c;
        }
        int same=1;
        /* Both old and fresh partitions are ordered. Compare class equivalence. */
        for(int u=0;u<n;u++) for(int v=0;v<n;v++)
            if((colors[u]==colors[v]) != (fresh[u]==fresh[v])) same=0;
        memcpy(colors,fresh,n*sizeof(int));
        cnum=c+1;
        if(same) break;
    }
    int idx=0;
    for(int c=0;c<cnum;c++) for(int v=0;v<n;v++)
        if(colors[v]==c) vertex_order[idx++]=c;
    if(idx!=n) {fputs("color partition failure\n",stderr);exit(3);}
}
static void canonical_backtrack(int j, uint64_t prefix){
    if(j==n_global){if(prefix<best)best=prefix;return;}
    int cell=vertex_order[j];
    for(int v=0;v<n_global;v++) if(!used[v] && colors[v]==cell){
        uint64_t col=0;
        for(int i=0;i<j;i++) col=(col<<1)|((graph[v]>>chosen[i])&1u);
        uint64_t p=(prefix<<j)|col;
        int written=j*(j+1)/2;
        if(best!=UINT64_MAX && p>(best>>(edge_bits-written)))continue;
        chosen[j]=v;used[v]=1;
        canonical_backtrack(j+1,p);
        used[v]=0;
    }
}
static uint64_t canonical(void){
    refine();memset(used,0,sizeof(used));best=UINT64_MAX;
    edge_bits=n_global*(n_global-1)/2;
    canonical_backtrack(0,0);
    return best;
}
static void decode(uint64_t code, int n){
    memset(graph,0,sizeof(graph));
    for(int j=n-1;j>=1;j--){
        for(int i=j-1;i>=0;i--){
            int e=(int)(code&1u);code>>=1;
            if(e){graph[i]|=(uint16_t)1u<<j;graph[j]|=(uint16_t)1u<<i;}
        }
    }
}
static uint64_t hash64(uint64_t x){
    x ^= x>>30; x*=UINT64_C(0xbf58476d1ce4e5b9);
    x ^= x>>27; x*=UINT64_C(0x94d049bb133111eb);
    return x^(x>>31);
}
static int insert(uint64_t key){
    uint32_t h=(uint32_t)hash64(key)&(CAP-1);
    for(;;){
        if(hash_table[h]==key)return 0;
        if(hash_table[h]==UINT64_MAX){hash_table[h]=key;return 1;}
        h=(h+1)&(CAP-1);
    }
}
static int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
static uint64_t regular[10], irregular[10], num_two[10], num_three[10], num_four[10], num_more[10];
static int alpha_counts[10][2];
static void equality(int n,uint64_t code){
    int d[MAXN],s[MAXN], num_degrees=0, degree_seen[MAXN+1]={0};
    for(int i=0;i<n;i++)d[i]=__builtin_popcount((unsigned)graph[i]);
    for(int i=0;i<n;i++){
        s[i]=0;for(int j=0;j<n;j++)if((graph[i]>>j)&1u)s[i]+=d[j];
        if(!degree_seen[d[i]]++){num_degrees++;}
    }
    if(num_degrees==1){regular[n]++;return;}
    int hi=0,lo=0;
    for(int i=0;i<n;i++){if(d[i]>d[hi])hi=i;if(d[i]<d[lo])lo=i;}
    int H=(d[hi]-d[lo])*d[hi]*d[lo];
    int K=s[lo]*d[hi]-s[hi]*d[lo];
    if(K<=0 || K>H) return;
    for(int i=0;i<n;i++)if((K*d[i]*d[i]+H*s[i])*d[hi] != (K*d[hi]*d[hi]+H*s[hi])*d[i])return;
    int den=H+K,g=gcd(K,den), anum=K/g,aden=den/g;
    irregular[n]++;
    if(num_degrees==2)num_two[n]++;
    else if(num_degrees==3)num_three[n]++;
    else if(num_degrees==4)num_four[n]++;
    else num_more[n]++;
    if(2*anum==aden)alpha_counts[n][1]++; else alpha_counts[n][0]++;
    printf("W\t%d\t%09llx\t%d/%d\t%d\n",n,(unsigned long long)code,anum,aden,num_degrees);
}
int main(int argc,char **argv){
    int maxn=9;
    if(argc>1){maxn=atoi(argv[1]);if(maxn<2||maxn>9){fprintf(stderr,"maxn must be 2..9\n");return 2;}}
    previous=malloc(CAP*sizeof(uint64_t));next=malloc(CAP*sizeof(uint64_t));
    if(!previous||!next){fputs("allocation failure\n",stderr);return 2;}
    previous[0]=0;count_prev=1;
    printf("# classify22 census v1; connected unlabelled graphs via one-vertex extension\n");
    printf("# W n canonical-column-bit-code alpha distinct-degree-count\n");
    printf("# n=1 connected=1 (isolated, excluded from equation)\n");
    for(int n=2;n<=maxn;n++){
        memset(hash_table,0xff,sizeof(hash_table));count_next=0;
        n_global=n;
        for(size_t g=0;g<count_prev;g++){
            decode(previous[g],n-1);
            uint16_t base[MAXN];memcpy(base,graph,sizeof(base));
            for(int mask=1;mask<(1<<(n-1));mask++){
                memcpy(graph,base,sizeof(base));
                for(int i=0;i<n-1;i++)if(mask&(1<<i)){
                    graph[i]|=(uint16_t)1u<<(n-1);
                    graph[n-1]|=(uint16_t)1u<<i;
                }
                uint64_t code=canonical();
                if(insert(code)){
                    if(count_next>=CAP){fputs("too many graphs\n",stderr);return 3;}
                    next[count_next++]=code;
                    decode(code,n);
                    equality(n,code);
                }
            }
        }
        fprintf(stderr,"n=%d count=%zu regular=%llu irregular=%llu alpha_lt_half=%d alpha_eq_half=%d distinct2=%llu distinct3=%llu distinct4=%llu distinct5plus=%llu\n",n,count_next,(unsigned long long)regular[n],(unsigned long long)irregular[n],alpha_counts[n][0],alpha_counts[n][1],(unsigned long long)num_two[n],(unsigned long long)num_three[n],(unsigned long long)num_four[n],(unsigned long long)num_more[n]);
        printf("# n=%d connected=%zu regular=%llu irregular=%llu alpha_lt_half=%d alpha_eq_half=%d distinct2=%llu distinct3=%llu distinct4=%llu distinct5plus=%llu\n",n,count_next,(unsigned long long)regular[n],(unsigned long long)irregular[n],alpha_counts[n][0],alpha_counts[n][1],(unsigned long long)num_two[n],(unsigned long long)num_three[n],(unsigned long long)num_four[n],(unsigned long long)num_more[n]);
        uint64_t *sw=previous;previous=next;next=sw;count_prev=count_next;
    }
    free(previous);free(next);
    return 0;
}
