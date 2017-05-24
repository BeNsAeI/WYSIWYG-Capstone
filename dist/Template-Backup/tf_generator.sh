#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
	echo "Creating file: $line.template.py"
	if [ ! -f $line.template.py ]; then
		echo "#0#'''<<ARG0>>'''" >> $line.template.py
		echo "Created!"
	fi
done < "$1"
