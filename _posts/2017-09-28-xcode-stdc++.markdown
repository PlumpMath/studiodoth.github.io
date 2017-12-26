---
title: "Xcode에 bits/stdc++.h 설치하기"
layout: post
date: 2017-09-28 23:04
headerImage: false
projects: false
author: simotion
tags: ["XCode"]
---

stdc++.h를 Xcode의 include 폴더에 넣어주면 된다. 아래 스크립트를 받아서 실행해주자.

{% highlight bash %}
cd /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1
sudo mkdir bits && cd bits
sudo wget https://gist.githubusercontent.com/reza-ryte-club/97c39f35dab0c45a5d924dd9e50c445f/raw/47ecad34033f986b0972cdbf4636e22f838a1313/stdc++.h
{% endhighlight %}