#!/bin/bash

while read host
do
    output="$(printf 'HELO example.com\nMAIL FROM:test@example.com\nRCPT TO:test@test.com\nQUIT\n' | nc $host 25 -w 1 2> /dev/null)"
    if ! [[ -z $output ]]
    then
        if ! [[ $output =~ denied ]]
        then
            echo $host
        fi
    fi
done < ${1:-/dev/stdin}

