#!/bin/bash
mkdir lake
cd lake
for x in midnight 2am 3.14am 4am 6am 8am 10am noon 2pm 4pm 6pm 8pm 10pm; do
    mkdir $x; cd $x;
    for f in header_tile.jpg footer_tile.jpg header_bg.jpg; do
        wget -c http://www.google.com/ig/images/skins/teahouse/$x/$f
    done
    cd ..
done
mkdir 314am
mv 3.14am/* 314am
rm -rf 3.14am
cd ..

mkdir field
cd field
for x in midnight 2am 314am 4am 6am 8am 10am noon 2pm 4pm 6pm 8pm 10pm; do
    mkdir $x; cd $x;
    for f in footer_bg_rside.jpg headertile_bg.jpg canvastile_bg.jpg header_bg.jpg footertile_bg_rside.jpg; do
        wget -c https://ssl.gstatic.com/ui/v1/icons/mail/themes/teahouse/$x/$f
    done
    cd ..
done
cp noon/canvastile_bg.jpg noon/footertile_bg_rside.jpg noon/header_bg.jpg noon/headertile_bg.jpg 2pm
cp 8am/canvastile_bg.jpg 8am/header_bg.jpg 8am/headertile_bg.jpg 10am
cd ..

