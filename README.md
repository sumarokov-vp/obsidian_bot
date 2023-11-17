# obsidian_bot

https://yandex.ru/support/disk-desktop-linux/
### Yandex disk for obsidian sync

```bash
wget -O YANDEX-DISK-KEY.GPG http://repo.yandex.ru/yandex-disk/YANDEX-DISK-KEY.GPG
apt-key add YANDEX-DISK-KEY.GPG
echo "deb http://repo.yandex.ru/yandex-disk/deb/ stable main" >> /etc/apt/sources.list.d/yandex-disk.list
apt-get update
apt-get install yandex-disk

# initial setup
yandex-disk setup
vim ~/.config/yandex-disk/config.cfg
```

```config
# ~/.config/yandex-disk/config.cfg
#data directory
dir="~/Yandex.Disk"

#exclude files
exclude-dirs="exclude/dir1,exclude/dir2,path/to/another/exclude/dir"
```

Then you can run service
```bash
yandex-disk start
```

### Using bot

Add note - send message to bot with text. First line will be title, other lines will be content.
/search - search in notes by content

