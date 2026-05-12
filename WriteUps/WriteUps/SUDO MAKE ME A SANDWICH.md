
![[Pasted image 20260511061314.png|471]]

Heyyyyyy! It’s M4ST3RS or just Kev,well never mind after all who care’s 🤷‍♂️ 
Other wise guys lets go through this easy challenge on #Picogym #picoctf currently having a new look and feel Cylab Security Academy ===> [https://cylabacademy.org/]

![[new look.png|592]]


Being my first ever write up I’ll go straight to the challenge which was tagged easy but not in that sense even for a rookie like me 😅  
Yah so in this challenge we are introduced by the info 

			can you read the flag?I think you can!  
  
  To get the flag we access the lab environment using  ssh and the specific port provided to you as shown below and enter the password given on the site to access the lab.

![[Pasted image 20260511062117.png|671]]

After accessing the lab we use the _ls_  command  to list down  the  directories and files we are provided with as shown below

![[Screenshot_2026-05-11_04-42-49.png]]

Yap!! 
You guessed right I also tried it out and it didn't work 🤦‍♂️ so yeah form the image above trying to read the flag.txt file directly will not work but there is another way around.

So I decided to check for the permissions I have on this lab and what I can  do to get [SUDO]permissions.

![[sudo.png]]

From the snippet we can see a a file  [/bin/emacs] which we can use to get [root]  Privileges 
So we run the command [sudo /bin/emacs] then [ALT + X] and type [shell] on the emacs interface to get root access
![[shell.png|573]]

After typing [shell ]the terminal will split then we can [ls] and [cat flag.txt] to get our flag in the form 
[picoCTF{.....}]

![[flag.png]]

On the right terminal we can see our flag [picoCTF{ju57_5ud0_17_4c6f730f}]
So yeah there you go 🥳🥳

