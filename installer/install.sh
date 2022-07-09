#!/bin/env bash

function msg() {
 local text="$1"
 local div_width="80"
 printf "%${div_width}s\n" ' ' | tr ' ' -
 printf "%s\n" "$text"
}
function main(){
 if ! [[ -d "$HOME/.local/bin" ]];then
   mkdir $HOME/.local/bin
 fi
 msg "cloning repo"
 sudo git clone https://github.com/ekm507/araste.git /usr/share/araste
 msg "installing binary file"
 sudo cp /home/sameet/Repos/araste/araste.py /bin/araste
 sudo chmod +x /bin/araste
}
main
