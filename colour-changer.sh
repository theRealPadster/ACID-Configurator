#!/bin/bash

#find-and-replace from $oldcolour to the new colour, $acidcolour

sed -i "s|$oldcolour|$acidcolour|g" $HOME/.themes/ACID/gnome-shell/gnome-shell.css  $HOME/.themes/ACID/gnome-shell/assets/*
