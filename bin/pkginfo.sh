#!/usr/bin/bash
echo -e "列出系統安裝的程式庫訊息："
#m=`pkgconf --list-all | awk -F ' ' '{print $1}'`
m=`pkgconf --list-package-names`
for pkgs in $m; do
	echo -e "$pkgs;`pkgconf --path $pkgs`;`pkgconf --cflags $pkgs`;`pkgconf --libs $pkgs`"
done

