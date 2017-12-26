---
title: "Google Code Jam 2016 - Round 1A"
layout: post
date: 2017-04-24 21:20
image: https://koppl.in/indigo/assets/images/jekyll-logo-light-solid.png
headerImage: false
projects: false
author: simotion
tags: ["Google Code Jam"]
---

저번글에 이어서..

## Problem A. The Last Word

앞에 붙일지 뒤에 붙일지를 그리디하게 정해주면 됩니다.

{% highlight cpp %}

#include <cstdio>
#include <cstring>
void solve() {
    char ans[1005],inp[1005];
    memset(ans,0,sizeof(ans));
    scanf("%s",&inp);
    int len=strlen(inp);
    ans[0]=inp[0];
    for(int i=1;i<len;i++) {
        char s1[1005],s2[1005];
        strcpy(s1+1,ans);
        strcpy(s2,ans);
        s1[0]=s2[i]=inp[i];
        s2[i+1]=0;
        if(strcmp(s1,s2)<0) strcpy(ans,s2);
        else strcpy(ans,s1);
    }
    printf("%s\n",ans);
}
int main() {
    int n;scanf("%d",&n);
    for(int i=1;i<=n;i++) {
        printf("Case #%d: ",i);
        solve();
    }
}

{% endhighlight %}

## Problem B. Rank and file

모든 행과 열에서 나오는 숫자를 센다면, 가로 세로 한번씩 나와야 하니까 숫자마다 나오는 횟수가 짝수여야 합니다. 한줄이 모자라니까 부족한 숫자는 횟수가 홀수일 것이니 입력에서 주어지는 모든 숫자의 개수를 세고, 홀수번 나온 숫자를 오름차순으로 출력하면 됩니다.

{% highlight cpp %}

#include <cstdio>
#include <cstring>
int cnts[2502],n,tmp,li;
void solve() {
    memset(cnts,0,sizeof(cnts));
    scanf("%d",&li);
    for(int i=1;i<2*li;i++) {
        for(int j=0;j<li;j++) {
            scanf("%d",&tmp);
            cnts[tmp]++;
        }
    }
    for(int i=1;i<2501;i++) if(cnts[i]&&cnts[i]%2) printf("%d ",i);
    printf("\n");
}
int main() {
    scanf("%d",&n);
    for(int i=1;i<=n;i++) {
        printf("Case #%d: ",i);
        solve();
    }
}

{% endhighlight %}

## Problem C. BFFs

한줄요약: max(사이클의 길이가 2인 부분을 포함하는 부분 그래프들의 길이의 합, 사이클의 길이가 3 이상인 부분 그래프들 중 가장 큰 길이)

{% highlight cpp %}

#include <cstdio>
#include <cstring>
#define MAX(A,B) A>B?A:B
int n,bff[1005],plen[1005],ans,ccount,cycle_max;
void track(int loc,int start,bool* vis,int depth) {
    if(bff[bff[loc]]==loc) {
        if(loc==start) {
            ccount++;
        }
        plen[loc]=MAX(plen[loc],depth);
        return;
    }
    if(vis[loc]) {
        if(start==loc) cycle_max=MAX(cycle_max,depth);
        return;
    }
    vis[loc]=true;
    track(bff[loc],start,vis,depth+1);
}
void solve() {
    ans=ccount=cycle_max=0;
    memset(bff,0,sizeof(bff));
    memset(plen,0,sizeof(plen));
    scanf("%d",&n);
    for(int i=1;i<=n;i++) scanf("%d",&bff[i]);
    for(int i=1;i<=n;i++) {
        bool vis[1005];
        memset(vis,0,sizeof(vis));
        track(i,i,vis,0);
    }
    for(int i=1;i<=n;i++) {
        if(i==bff[bff[i]]) {
            ans+=plen[i]+plen[bff[i]];
            plen[i]=plen[bff[i]]=0;
        }
    }
    ans+=ccount;
    printf("%d\n",MAX(ans,cycle_max));
}
int main() {
    int caseCnt;
    scanf("%d",&caseCnt);
    for(int i=1;i<=caseCnt;i++) {
        printf("Case #%d: ",i);
        solve();
    }
}

{% endhighlight%}
