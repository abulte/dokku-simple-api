# dokku-simple-api

Demonstrates a very simple python + postgres API hosted on dokku.

## Deploy

On dokku server:

```
dokku apps:create simple-api
dokku postgres:create simple-api
dokku postgres:link simple-api simple-api
```

On local copy:

```
git remote add dokku dokku@{host}:simple-api
git push dokku master
```

:rocket: http://simple-api.{host}/api
