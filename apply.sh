#!/bin/bash

#(re)set GNOME-Shell theme to ACID
#gsettings set org.gnome.shell.extensions.user-theme name "ACID"

# Set the schemadir, from Satyajit Sahoo
glibschemas="/usr/share/glib-2.0/schemas"
extensiondir="$HOME/.local/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/schemas"
schemafile="org.gnome.shell.extensions.user-theme.gschema.xml"
if [[ -f "$extensiondir/$schemafile" && -f "$extensiondir/gschemas.compiled" ]]; then
	schemadir="$extensiondir"
elif [[ -f "$glibschemas/$schemafile" && -f "$glibschemas/gschemas.compiled" ]]; then
	schemadir="$glibschemas"
else
	return 1
fi

gsettings --schemadir "$schemadir" set org.gnome.shell.extensions.user-theme name 'ACID'

gnome-shell --replace &

unset glibschemas
unset extensiondir
unset schemafile

#clear variables
#unset colour
#unset bool
