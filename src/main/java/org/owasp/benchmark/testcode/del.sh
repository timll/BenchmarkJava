cat del.txt | while read line ; do
   rm "$line" "${line%.xml}.java"
done
