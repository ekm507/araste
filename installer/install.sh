#!/bin/env bash
function msg() {
 local text="$1"
 local div_width="80"
 printf "%${div_width}s\n" ' ' | tr ' ' -
 printf "%s\n" "$text"
}
function logo() {
  cat <<'EOF'
                                        ██████          
          ████                ██        ██              
    ████                      ██          ██            
    ████    ██    ██  ██  ██  ██    ██    ██            
      ██████████████████████  ██    ██    ██            
                                    ██                  
                                  ██                    
EOF
}
function main(){
  logo
  msg "cloning repo"

# check if directory araste exists
 if [[ -d "/usr/share/araste" ]];then
   msg "directory araste already exists. pulling new version"
   cd /usr/share/araste
   sudo git pull
   msg "araste is updated!"
 else
  sudo git clone https://github.com/ekm507/araste.git /usr/share/araste
  msg "installing executable file"
  sudo cp /usr/share/araste/araste.py /bin/araste
  sudo chmod +x /bin/araste
  msg "araste is installed!"
 fi
}
main
