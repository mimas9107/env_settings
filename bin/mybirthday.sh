#!/usr/bin/env bash

cur_year=$(date +%Y)
#echo -e $cur_year
nowdate_s=$(date +%s)
#echo -e $nowdate_s

mybirthdate=""
thisbirthdate=$cur_year-$mybirthdate
#echo -e $thisbirthdate

thisbirthdate_s=$(date --date=$thisbirthdate +%s)
#echo -e $thisbirthdate_s
deltaday_s=$((thisbirthdate_s - nowdate_s))
deltaday=$((deltaday_s/60/60/24))
echo -e "There are $deltaday days"




