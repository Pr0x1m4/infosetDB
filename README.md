# InfosetDB

InfosetDB is a robust, flexible and lightweight database API written in python and designed for time series data.

## Install

InfosetDB uses `redis` for caching and `celery` for async tasks, so they need to be installed before `InfosetDB`, after they've been installed, clone and run install script.

```bash
λ git clone https://github.com/PalisadoesFoundation/infoset-ng
λ cd infoset-ng
λ pip install -r requirements.txt
λ python docker/api.py

* Running on http://0.0.0.0:6000/ (Press CTRL+C to quit)
```
### Redis
After starting infoset server, start local redis server.
```bash
λ redis-server
[28550] 01 Aug 19:29:28 # Warning: no config file specified, using the default config. In order to specify a config file use 'redis-server /path/to/redis.conf'
[28550] 01 Aug 19:29:28 * Server started, Redis version 2.2.12
[28550] 01 Aug 19:29:28 * The server is now ready to accept connections on port 6379
```
### Celery

After installing celery and starting redis, open a new terminal and launch the celery worker.

```bash
λ cd infoset-ng
λ celery worker -A infoset.api.post.celery --loglevel=info

 -------------- celery@localhost.localdomain v4.0.2 (latentcall)
---- **** ----- 
--- * ***  * -- Linux-4.9.34-1-lts-x86_64-with-arch 2017-07-29 17:06:12
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         infoset:0x7f4670d6afd0
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     redis://localhost:6379/0
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
 
```

## Collecting Data

InfosetDB by itself <b>does not</b> collect data, to begin collecting data on your local machine, simply install and run [collectr](https://github.com/PalisadoesFoundation/collectr.git).


For more information check out the docs at [http://infoset-ng.readthedocs.io/en/latest/]() 


