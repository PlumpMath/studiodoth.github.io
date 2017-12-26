---
title: "Google Code Jam 2016 - Qualification Round"
layout: post
date: 2017-04-22 18:33
image: https://koppl.in/indigo/assets/images/jekyll-logo-light-solid.png
headerImage: false
projects: false
author: simotion
tags: ["Google Code Jam"]
---

신청기간을 지나버려서 올해 신청은 못했고.. 어차피 시험기간이라 못한다고 합리화를 하며 작년 문제를 풀어보았습니다.

(작성중)

## Problem A. Counting Sheep

노가다 뛰면 됩니다.

0이 아니라면 모든 자릿수가 표현 가능합니다.
굳이 증명을 하자면, n에 대해 $$gcd(n,10)=1$$라면 $$n,2n,...,10n$$은 $$mod\:10$$에 대해 완전잉여계이므로 모든 자릿수가 등장합니다.
$$gcd(n,10)\neq1$$이라면, n에 적당한 $$2^a5^b$$를 곱해 $$n=10^kn'\:(gcd(n',10)=1)$$ 꼴로 만들 수 있는데, $$n'$$에서 전자의 경우가 되므로 증명이 완료됩니다.


{% highlight cpp %}
#include <cstdio>
int check,n,val,tmp;
bool addCheck(int n) {
    while(n) {
        check|=(1<<(n%10));
        n/=10;
    }
    return !(check==((1<<10)-1));
}
int main() {
    scanf("%d",&n);
    for(int i=1;i<=n;i++) {
        check=tmp=0;
        printf("Case #%d: ",i);
        scanf("%d",&val);
        if(val==0) {
            printf("INSOMNIA\n");
            continue;
        }
        do{tmp+=val;} while(addCheck(tmp));
        printf("%d\n",tmp);
    }
}
{% endhighlight %}

## Problem B. Revenge of the Pancakes

마찬가지로 간단한 문제입니다.

팬케익의 방향이 주어졌을때, 방향끼리 묶어보면 XOXOXO.. 또는 OXOXOX..가 됩니다. n개의 묶음이 있다고 합시다. 첫 번째 묶음을 뒤집으면 두 번째 묶음과 방향이 같아집니다. 다시 첫 번쨰 묶음과 두 번째 묶음을 뒤집으면 1~3번째 묶음의 방향이 같아지고, 이 과정을 n-1번 반복하면 모든 묶음(=팬케익)의 방향이 같아지게 됩니다. 여기서 팬케익들의 방향이 X라면 한번 더 뒤집어주고 나면 모든 방향이 O로 되면서 최소 횟수로 팬케익들이 방향을 모두 맞춰줄 수 있습니다.

이를 구현하려면 몇번 방향이 바뀌는지만 세어주면 됩니다. 마지막 팬케익의 방향을 보고 X라면 (방향 바뀌는 횟수+1)이, 아니면 (방향 바뀌는 횟수)가 최소 횟수가 되겠죠.

{% highlight cpp %}
#include <cstdio>
int n,tmp,j;
char s[101];
int main() {
    scanf("%d",&n);
    for(int i=1;i<=n;i++) {
        tmp=0;
        printf("Case #%d: ",i);
        scanf("%s",&s);
        for(j=1;s[j];j++) if(s[j]!=s[j-1]) tmp++;
        if(s[j-1]=='-') tmp++;
        printf("%d\n",tmp);
    }
}
{% endhighlight %}

## Problem C. Coin Jam

Base가 홀수일 경우, Base의 거듭제곱도 항상 홀수이므로 1이 짝수개 있으면 짝수가 되어 항상 2로 나누어 떨어집니다.
Base가 2일때 $$2^k\equiv (-1)^k (mod 3)$$이므로 짝수 지수에 위치한 1의 개수와 홀수 지수에 위치한 1의 개수가 같으면 3으로 나누어 떨어집니다. Base가 4일때는 5, Base가 6일때는 7,..로 같은 과정을 반복해서 Base가 짝수일 경우 짝수 지수에 위치한 1의 개수와 홀수 지수에 위치한 1의 개수가 같으면 충분하다는 것을 알 수 있습니다. 그런데 짝수 지수에 위치한 1의 개수와 홀수 지수에 위치한 1의 개수가 같으면 총 개수는 짝수이므로, Base가 홀수인 경우까지 모두 포함하게 됩니다.

따라서 짝수 지수에 위치한 1의 개수와 홀수 지수에 위치한 1의 개수가 같게 해주면 항상 Jamcoin이 됨을 알 수 있습니다.

{% highlight cpp %}

#include <cstdio>
#include <cmath>
char k[1001];
int n,j,cnt;
void s(int loc, int oc, int ec) {
    if(cnt>=j) return;
    if(loc==n-1) {
        if(n%2) oc++;
        else ec++;
        if(oc==ec) {
            cnt++;
            printf("%s ",k);
            for(int base=2;base<11;base++) {
                printf("%d ",base%2?2:(base+1));
            }
            printf("\n");
        }
        return;
    }
    k[loc]='0';
    s(loc+1,oc,ec);
    k[loc]='1';
    s(loc+1,oc+(loc%2?0:1),ec+(loc%2?1:0));
}
int main() {
    scanf("%*d %d %d",&n,&j);
    printf("Case #1:\n");
    k[0]=k[n-1]='1';
    s(1,1,0);
}

{% endhighlight %}
