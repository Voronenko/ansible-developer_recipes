1. Dotfiles
2. tooling from ansible-developer-recipes
3. Get browser settings
4. Register IDEA
5. Generate or restore keypairs for host
6. Prevent parallel OS partition from mounting, if any. Configure shared partition, if any.
7. Ensure you have installed node with nvm and ruby with chruby
8. Configure VPN if any - pritunl, fortigate, built-in
9. Initialize ide settings from dotfiles, install SourceCodePro
10. Install powermanagement if on notebook
11. Recover messaging accounts



If you are on notebook with NVIDIA


Detect what you have  
ubuntu-drivers devices

if yes, 

1. Follow advise for driver
sudo apt install nvidia-390

2. Blacklist built-in driver

sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
cat /etc/modprobe.d/blacklist-nvidia-nouveau.conf
sudo update-initramfs -u
sudo reboot

3. (Not confirmed)
add in  /etc/default/grub 

acpi_rev_override=1

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_rev_override=1"

sudo update-grub2

sudo reboot 0

4. Install nvidia-prime

sudo apt-get install nvidia-prime


5. If card is not needed for a while

sudo prime-select intel
sudo reboot 0

if GPU is needed

sudo prime-select nvidia
sudo reboot 0



On success your discharge rate should be < 10W w/o wifi

In NVidia is powered on - ~ 15W.

$powertop
The battery reports a discharge rate of 17.0 W

