I am not familar with SSH but there are a lot of usage of it in anywhere. It is better to get some knowledge about it.

0.
Firstly, how to delete keys fo known hosts.
It sounds strange while I write it at the beginning. It is because I Myself have been confused by this for a whole.
Some bad things of old keys made me can not work normally. *Therefore I think it is a very ###important### thing that we should know.*

Nomally,

`rm -f .ssh/known_hosts`
is good for handling this problem.

Otherwise,

`ssh-keygen -R "hostname"`
should help you.

...
