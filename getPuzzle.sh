echo Which day is it?
read day
URL=https://adventofcode.com/2021/day/$day/input
dirName=./day$day
mkdir -p $dirName
curl $URL --output $dirName/input.txt --cookie ./settings/cookies-adventofcode-com.txt
cp ./boilerplate.py $dirName/day$day.py
