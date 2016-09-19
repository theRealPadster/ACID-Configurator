#!/bin/bash

# Replaces any 6-digit hex codes in the theme with their corresponding rgb codes.
# This is so the colourizer's find and replace doesn't rewrite any essential colours.
# Also, Inkscape resets the rgb to 6 digit hex when editing, so this fixes it.

sed -i "s|#afafaf|rgb(175,175,175)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#bebebe|rgb(190,190,190)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#bfbfbf|rgb(191,191,191)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#cdcdcd|rgb(205,205,205)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#c4c4c4|rgb(196,196,196)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#e6e6e6|rgb(230,230,230)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#e8e8e8|rgb(232,232,232)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#f9f9f9|rgb(249,249,249)|g" $HOME/.themes/ACID/gnome-shell/assets/*

sed -i "s|#000000|rgb(0,0,0)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#131313|rgb(19,19,19)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#131c1b|rgb(19,28,27)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#2c3733|rgb(44,55,51)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#212121|rgb(33,33,33)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#232323|rgb(35,35,35)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#3b3b3b|rgb(59,59,59)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#323232|rgb(50,50,50)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#333333|rgb(51,51,51)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#343434|rgb(52,52,52)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#373737|rgb(55,55,55)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#4d4d4d|rgb(77,77,77)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#4e4e4e|rgb(78,78,78)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#404040|rgb(64,64,64)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#414141|rgb(65,65,65)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#424242|rgb(66,66,66)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#464646|rgb(70,70,70)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#5c5c5c|rgb(92,92,92)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#595959|rgb(89,89,89)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#6e6e6e|rgb(110,110,110)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#606060|rgb(96,96,96)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#646464|rgb(100,100,100)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#666666|rgb(102,102,102)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#888888|rgb(136,136,136)|g" $HOME/.themes/ACID/gnome-shell/assets/*
sed -i "s|#969696|rgb(150,150,150)|g" $HOME/.themes/ACID/gnome-shell/assets/*
