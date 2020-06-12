# nuttel : Identify your proxyjump SSH tunnels and make a 

Your remote devices make a ssh to a public host (tip: use autossh and a service). Great, you can ssh and port forward via this  jump host. But then how to identify the local ports/tunnels and easily connect? That's what nuttel is for

## Install

Do this on your _local_ and _public_ machine. 

`pip install nuttel 
echo "include remotes" >> ~/.ssh/config`

## Run
nuttel.py --user iot1 --jump yourjumphost.com > ~/.ssh/remotes
cat ~/.ssh/remotes
ssh myremote-jump

Nuttel sshs to your jump host, identifies all local ports that are ssh tunnels, interrogates them and reports back a ready to use config file, which you add to your .ssh/ directory. It specifies the ports and jump hosts required to login to your remove devices. Nuttel will preserve your existing config file, and just update it.

## Options
Put in a cron job to have your remotes at hand:

`0 * * * * /usr/local/bin/tmv-tunnel --user pi --config ~/.ssh/remotes  > ~/.ssh/remotes`
