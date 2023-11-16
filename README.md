# obsidian_bot

https://hub.docker.com/r/deanar/yandex.disk/

### Yandex disk: Obtain OAuth token
(leave default path to Yandex.Disk folder or change it in volumes section too)
```bash
docker-compose run --rm ya.disk yandex-disk setup
```

Disable auto sync for folders
```config
exclude-dirs="exclude/dir1,exclude/dir2,path/to/another/exclude/dir"
```

Then you can run service
```bash
docker-compose up -d
```

### Using bot

Add note - send message to bot with text. First line will be title, other lines will be content.
/search - search in notes by content

