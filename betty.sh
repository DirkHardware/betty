#!/bin/bash

FILES=$HOME/.config/autostart/*
for file in $FILES
	do
	presence=`grep 'Betty' -w $file`
	echo "$presence"
	# In order for if statement to work, we have to wrap $presence in double quotes to keep it as one string, otherwise we will get a too many arguments error
	# Ideally we should surround "Betty", the string we are searching for, in wildcards in case it were not a whole word but a substring, tho in this case that
	# is not strictly necessary. 
		if [ "$presence"=*"Betty"* ]
		then
			echo "Betty is present"
		fi
	done
# echo `grep -wl 'Betty' $HOME/.config/autostart/*`

