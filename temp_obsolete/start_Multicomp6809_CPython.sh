#!/bin/bash

(
    set -x
    python2 DragonPy_CLI.py --verbosity=50 --cfg=Multicomp6809 --display_cycle
)
echo
read -n1 -p "Start bash? [y,n]" doit
echo
case $doit in
    y|Y)
        bash -i
        exit 0
        ;;
    n|N)
        echo "bye bye"
        ;;
    *)
        echo "input, don't know, bye."
        ;;
esac