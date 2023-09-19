# :book: 0x05. 0x03. Queuing System in JS.
## :page_with_curl: Topics Covered.
This project involves how to use Redis and implementing Kue as a queue system. The learning objectives include;
1. Running a Redis server.
2. Using a Redis client for basic operations and with Node JS.
3. Storing hash values in Redis.
4. Dealing with async operations.
5. Building a basic Express app interacting with a Redis server.
6. Building a basic Express app interacting with a Redis server and queue.

# :computer: Tasks.
<!---->
## [0. Install a redis instance](1-redis_op.js)
### :page_with_curl: Task requirements.
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/download/](/rltoken/v6VB9ZwmVfppL0OmzbmVWQ "https://redis.io/download/")):
```
    $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    $ tar xzf redis-6.0.10.tar.gz
    $ cd redis-6.0.10
    $ make
```

* Start Redis in the background with `src/redis-server`
```
    $ src/redis-server &
```

* Make sure that the server is working with a ping `src/redis-cli ping`
```
    PONG
```

* Using the Redis client again, set the value `School` for the key `Holberton`
```
    127.0.0.1:[Port]> set Holberton School
    OK
    127.0.0.1:[Port]> get Holberton
    "School"
```

* Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)
```
    $ kill [PID_OF_Redis_Server]
```

Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

Requirements:

* Running `get Holberton` in the client, should return `School`

**Repo:**

* GitHub repository: `alx-backend`
* Directory: `0x03-queuing_system_in_js`
* File: `README.md, dump.rdb`

### :wrench: Task setup.
```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make

# Start Redis.
cd /root/redis-6.0.10
src/redis-server &

# ping redis server.
src/redis-cli ping

# Enter Redis client.
redis-cli

# Kill redis server
redis-cli shutdown # or using process id

ps aux | grep redis-server
kill <PID>
```

### :heavy_check_mark: Solution
> [:point_right: README.md](README.md), [dump.rdb](dump.rdb)
<!---->

<!---->
## [1. Node Redis Client](0-redis_client.js)
### :page_with_curl: Task requirements.
Install [node_redis](/rltoken/mRftfl67BrNvl-RM5JQfUA "node_redis") using npm

Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

* It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly
* It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work

**Requirements:**

* To import the library, you need to use the keyword `import`
```
    bob@dylan:~$ ps ax | grep redis-server
     2070 pts/1    S+     0:00 grep --color=auto redis-server
    bob@dylan:~$ 
    bob@dylan:~$ npm run dev 0-redis_client.js 
    
    > queuing_system_in_js@1.0.0 dev /root
    > nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"
    
    [nodemon] 2.0.4
    [nodemon] to restart at any time, enter `rs`
    [nodemon] watching path(s): *.*
    [nodemon] watching extensions: js,mjs,json
    [nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
    Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
    Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
    Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
    ^C
    bob@dylan:~$ 
    bob@dylan:~$ ./src/redis-server > /dev/null 2>&1 &
    [1] 2073
    bob@dylan:~$ ps ax | grep redis-server
     2073 pts/0    Sl     0:00 ./src/redis-server *:6379
     2078 pts/1    S+     0:00 grep --color=auto redis-server
    bob@dylan:~$
    bob@dylan:~$ npm run dev 0-redis_client.js 
    
    > queuing_system_in_js@1.0.0 dev /root
    > nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"
    
    [nodemon] 2.0.4
    [nodemon] to restart at any time, enter `rs`
    [nodemon] watching path(s): *.*
    [nodemon] watching extensions: js,mjs,json
    [nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
    Redis client connected to the server
    ^C
    bob@dylan:~$
```
