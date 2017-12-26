---
title: "XRDP에서 VS Code 실행하기"
layout: post
date: 2017-08-07 00:03
image: https://koppl.in/indigo/assets/images/jekyll-logo-light-solid.png
headerImage: false
projects: false
author: simotion
tags: ["Linux", "VS Code"]
---

Ubuntu 16.04.3에 XRDP를 깔아서 이것저것 해보는데 VS Code가 계속 튕기는 문제가 있었다. XRDP를 처음 사용하는거라 설정이 꼬인줄 알았는데, 찾아보니 [VS Code의 문제](https://github.com/Microsoft/vscode/issues/3451) (정확히는 [Electron의 문제](https://github.com/electron/electron/issues/2256))였다. XRDP를 사용하려면 MATE나 Xfce같은 환경이 필요한데, 마침 이 환경에서 문제가 발생한다고 한다....

{% highlight bash %}
cd /usr/lib/x86_64-linux-gnu
# 라이브러리 파일 백업
sudo cp libxcb.so.1 libxcb.so.1.bak
sudo cp libxcb.so.1.1.0 libxcb.so.1.1.0.bak
# libxcb.so 파일들을 편집해준다.
sudo sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' libxcb.so.1
sudo sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' libxcb.so.1.1.0
# 이 파일들을 /usr/share/code에도 복사해준다.
sudo cp libxcb.so.1 /usr/share/code/libxcb.so.1
sudo cp libxcb.so.1.1.0 /usr/share/code/libxcb.so.1.1.0
{% endhighlight %}
이렇게 하고 재접속하면 VS Code를 정상적으로 사용할 수 있다.