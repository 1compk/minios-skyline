echo "Nala Update..."
#sudo nala update

echo "Nala Install..."
#sudo nala install binutils debootstrap squashfs-tools xz-utils lz4 zstd xorriso mtools rsync grub-efi-amd64-bin grub-pc-bin -y

echo "Start Building..."
./minios-cmd -d trixie -a amd64 -de xfce -pv standard -c zstd -l en_US -tz "Asia/Bangkok"