# VERSION CONTROL

Heyyyy!! Gaiiss,M4ST3RS,here another write-up yeah...
Okay I know it's basic but just because you know it doesn't mean someone starting of knows about it aswell 

I'll keep this straight forward no fluff kinda stuff I'll assume you know what is `git and Github`  

So connecting you github account with git is universal for both `Linux and Windows`
Feel free to copy and paste the commands  __BUT EDIT WHERE NECESSARY

___Setting the correct global identity


Move to the directory you want to initialize git and follow through with the commands as follows

```
		cd ~/Desktop/Everything/Versioncontrol
```

Initialize git in that directory 
```
		git init
```

Configure Identity
This is essential for github to know the author who is committing changes to that repository
```
        git config --global user.name "kev-disie"
        git config --global user.email "disiekelvin@gmail.com"
```


_verify your setup_
```
         git config --global --list
```

_Expected  output

`user.name=kev-disie`
`user.email=disiekelvin@gmail.com`

_Adding the remote url

```
		git remote add origin https://github.com/kev-disie/verisoncontrol.git
```

_Verify_

```
		git remote -v
```

`origin  https://github.com/kev-disie/Versioncontrol.git (fetch)`
`origin  https://github.com/kev-disie/Versioncontrol.git (push)`

_Error:Messege if remot exixts

`error: remote origin already exists.`

_Adding files_

```
		git add .
```

This adds all the files and subfolders in that directory 

_Commiting changes_
```
		git commit -m "This is my first commit"
```

_changing the master branch to main_
```
		git -M branch main
```

_Pushing commits to git hub_
```
		git push -u origin main
```


__2) Now creating a repo using the gh CLI utility

Ensure you navigate to the directory which you will initialize git and create the repo from there.
```
		cd ~/Desktop/Everything/Versioncontrol
```

```
        #Command works only for Linux systems with apt as the package manager
        sudo apt install gh 
```

```
		gh auth login
```

_choose 
`Github.com`
`HTTPS`
`Login with browser`

Your browser opens --- authorize GitHub CLI

_Verify_
```
		gh auth status
```

_Create the repo
```
		gh repo create Versioncontrol --public --source=. --remote=origin --push
```

_Expected output_
`https://github.com/kev-disie/Versioncontrol`

Initialize git in that directory 
```
		git init
```

Configure Identity
This is essential for github to know the author who is committing changes to that repository
```
        git config --global user.name "kev-disie"
        git config --global user.email "disiekelvin@gmail.com"
```

_verify your setup_
```
         git config --global --list
```

_Expected  output

`user.name=kev-disie`
`user.email=disiekelvin@gmail.com`

__NB:WE DO NOT SET A REMOTE URL WHEN USING THE gh UTILITY

So there you go you version control system set-up in less that a miute🙂