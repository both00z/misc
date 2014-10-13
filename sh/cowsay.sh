#!/bin/bash
function wtimes
{
	for ((i=0; i<$1; i++))
	do
		echo -n "$2"
	done
}
text=""
len=0
for arg in "$@"
do
	newlen=${#arg}
	if [ "$text" == "" ]
	then
		text="$arg"
	else
		text="$text-$arg"
	fi
	if [ "$newlen" -gt "$len" ]
	then
		len=$newlen
	fi
done
echo 
echo -n ' -'
wtimes $len '-'
echo '-'
IFS="-"
for arg in $text
do
	echo -n "< $arg"
	let "x= $len-${#arg}"
	wtimes $x " "
	echo " >"
done
echo -n ' -'
wtimes $len '-'
echo '-'
let "r= $len/2 + 3"
wtimes $r " "
echo '\  ^__^'
wtimes $r " "
echo ' \ (oo)\_______'
wtimes $r " "
echo '   (__)\       )\/\'
wtimes $r " "
echo '       ||----w |'
wtimes $r " "
echo '       ||     ||'
