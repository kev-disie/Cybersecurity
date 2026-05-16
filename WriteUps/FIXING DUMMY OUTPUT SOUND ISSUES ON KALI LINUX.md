

Heyyyyyy!! faahm it's M4ST3RS again with another write up but this time sound issue on specifically on kali linux  
which is the OS I've used for quite some time now  
So lemme quit the yapping and go straight to address the Elephant 🐘in the room

Atleast at some point you clicked the sound icon on the panel and saw something like 

            DUMMY OUTPUT
So yeah this is what will fix right now so right away to the fun part open your terminal and put on your hoodie😅💔

<mark style="background: #BBFABBA6;">Grand Unified Bootloader</mark>
Famously known as GRUB is the   program that takes over from the <mark style="background: #BBFABBA6;">BIOS</mark> during boot time,so basically the boot process takes place as shown below almost in every PC 

![[boot.jpg|371]]
The flow in linux  systems

<mark style="background: #ADCCFFA6;">BIOS/UEFI → GRUB → Linux Kernel → Systemd → Desktop</mark> 
So the GRUB decides:  > which kernel to boot
				 >What Kernel parameters to pass.
				 >Recovery mode options.
				 >Dual boot menus.

To fix our issue we need to modify the this file */etc/default/gru*b 
![[Pasted image 20260511164645.png]]
open the file and you will find the following details

- GRUB_TIMEOUT=5
- GRUB_DEFAULT=0
- GRUB_CMDLINE_LINUX_DEFAULT="quiet"
So after editing the file run the command  *sudo update-grub*
This regenerates the real boot configuration used during startup

So this line <mark style="background: #BBFABBA6;">*GRUB_CMDLINE_LINUX_DEFAULT="quiet"*</mark>  contains the variables kernel boot parameters hence anything inside the " "is passed directly to the Linux Kernel at boot
 <mark style="background: #FFB8EBA6;">"quiet"</mark>  in this case tells the Kernel to hide most of the boot messeges: 
- Loading drivers...
- Initializing ACPI...
- Starting udev...

so we need to modify that line like this : <mark style="background: #FFB86CA6;">GRUB_CMDLINE_LINUX_DEFAULT="quiet snd_intel_dspcfg.dsp_driver=1" </mark>

Now we just added another Kernel parameter which specifically affects Intel Audio Driver behavior 

![[Pasted image 20260511170239.png|621]]

 CTRL + X and then Y to save and exit the file  after that run *sudo update-grub* and <mark style="background: #ABF7F7A6;">reboot</mark> 