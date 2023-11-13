# obsidian_bot

https://hub.docker.com/r/deanar/yandex.disk/

### Obtain OAuth token
(leave default path to Yandex.Disk folder or change it in volumes section too)

```bash
docker-compose run --rm ya.disk yandex-disk setup
```

#Не синхронизировать указанные каталоги.
#exclude-dirs="exclude/dir1,exclude/dir2,path/to/another/exclude/dir"

Then you can run service

```bash
docker-compose up -d
```

