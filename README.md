
<p align="center">
<img src="docs/content/assets/img/traefik.logo.png" alt="Traefik" title="Traefik" />
</p>

[![Build Status SemaphoreCI](https://semaphoreci.com/api/v1/containous/traefik/branches/master/shields_badge.svg)](https://semaphoreci.com/containous/traefik)
[![Docs](https://img.shields.io/badge/docs-current-brightgreen.svg)](https://doc.traefik.io/traefik)
[![Go Report Card](https://goreportcard.com/badge/traefik/traefik)](https://goreportcard.com/report/traefik/traefik)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/traefik/traefik/blob/master/LICENSE.md)
[![Join the community support forum at https://community.traefik.io/](https://img.shields.io/badge/style-register-green.svg?style=social&label=Discourse)](https://community.traefik.io/)
[![Twitter](https://img.shields.io/twitter/follow/traefik.svg?style=social)](https://twitter.com/intent/follow?screen_name=traefik)


Traefik (pronounced _traffic_) is a modern HTTP reverse proxy and load balancer that makes deploying microservices easy.
Traefik integrates with your existing infrastructure components ([Docker](https://www.docker.com/), [Swarm mode](https://docs.docker.com/engine/swarm/), [Kubernetes](https://kubernetes.io), [Marathon](https://mesosphere.github.io/marathon/), [Consul](https://www.consul.io/), [Etcd](https://coreos.com/etcd/), [Rancher](https://rancher.com), [Amazon ECS](https://aws.amazon.com/ecs), ...) and configures itself automatically and dynamically.
Pointing Traefik at your orchestrator should be the _only_ configuration step you need.

---

. **[Overview](#overview)** .
**[Features](#features)** .
**[Supported backends](#supported-backends)** .
**[Quickstart](#quickstart)** .
**[Web UI](#web-ui)** .
**[Documentation](#documentation)** .

. **[Support](#support)** .
**[Release cycle](#release-cycle)** .
**[Contributing](#contributing)** .
**[Maintainers](#maintainers)** .
**[Credits](#credits)** .

---

:warning: Please be aware that the old configurations for Traefik v1.x are NOT compatible with the v2.x config as of now. If you're running v2, please ensure you are using a [v2 configuration](https://doc.traefik.io/traefik/).

## Overview

Imagine that you have deployed a bunch of microservices with the help of an orchestrator (like Swarm or Kubernetes) or a service registry (like etcd or consul).
Now you want users to access these microservices, and you need a reverse proxy.

Traditional reverse-proxies require that you configure _each_ route that will connect paths and subdomains to _each_ microservice. 
In an environment where you add, remove, kill, upgrade, or scale your services _many_ times a day, the task of keeping the routes up to date becomes tedious. 

**This is when Traefik can help you!**

Traefik listens to your service registry/orchestrator API and instantly generates the routes so your microservices are connected to the outside world -- without further intervention from your part. 

**Run Traefik and let it do the work for you!** 
_(But if you'd rather configure some of your routes manually, Traefik supports that too!)_

![Architecture](docs/content/assets/img/traefik-architecture.png)

## Features

- Continuously updates its configuration (No restarts!)
- Supports multiple load balancing algorithms
- Provides HTTPS to your microservices by leveraging [Let's Encrypt](https://letsencrypt.org)  (wildcard certificates support)
- Circuit breakers, retry
- See the magic through its clean web UI
- Websocket, HTTP/2, GRPC ready
- Provides metrics (Rest, Prometheus, Datadog, Statsd, InfluxDB)
- Keeps access logs (JSON, CLF)
- Fast
- Exposes a Rest API
- Packaged as a single binary file (made with :heart: with go) and available as an [official](https://hub.docker.com/r/_/traefik/) docker image


## Supported Backends

- [Docker](https://doc.traefik.io/traefik/providers/docker/) / [Swarm mode](https://doc.traefik.io/traefik/providers/docker/)
- [Kubernetes](https://doc.traefik.io/traefik/providers/kubernetes-crd/)
- [Marathon](https://doc.traefik.io/traefik/providers/marathon/)
- [Rancher](https://doc.traefik.io/traefik/providers/rancher/) (Metadata)
- [File](https://doc.traefik.io/traefik/providers/file/)

## Quickstart

To get your hands on Traefik, you can use the [5-Minute Quickstart](https://doc.traefik.io/traefik/getting-started/quick-start/) in our documentation (you will need Docker).

## Web UI

You can access the simple HTML frontend of Traefik.

![Web UI Providers](docs/content/assets/img/webui-dashboard.png)

## Documentation

You can find the complete documentation of Traefik v2 at [https://doc.traefik.io/traefik/](https://doc.traefik.io/traefik/).

A collection of contributions around Traefik can be found at [https://awesome.traefik.io](https://awesome.traefik.io).

## Support

To get community support, you can:
- join the Traefik community forum: [![Join the chat at https://community.traefik.io/](https://img.shields.io/badge/style-register-green.svg?style=social&label=Discourse)](https://community.traefik.io/)

If you need commercial support, please contact [Traefik.io](https://traefik.io) by mail: <mailto:support@traefik.io>.

## Download

- Grab the latest binary from the [releases](https://github.com/traefik/traefik/releases) page and run it with the [sample configuration file](https://raw.githubusercontent.com/traefik/traefik/master/traefik.sample.toml):

```shell
./traefik --configFile=traefik.toml
```

- Or use the official tiny Docker image and run it with the [sample configuration file](https://raw.githubusercontent.com/traefik/traefik/master/traefik.sample.toml):

```shell
docker run -d -p 8080:8080 -p 80:80 -v $PWD/traefik.toml:/etc/traefik/traefik.toml traefik
```

- Or get the sources:

```shell
git clone https://github.com/traefik/traefik
```

## Introductory Videos

You can find high level and deep dive videos on [videos.traefik.io](https://videos.traefik.io).

## Maintainers

We are strongly promoting a philosophy of openness and sharing, and firmly standing against the elitist closed approach. Being part of the core team should be accessible to anyone who is motivated and want to be part of that journey!
This [document](docs/content/contributing/maintainers-guidelines.md) describes how to be part of the core team as well as various responsibilities and guidelines for Traefik maintainers.
You can also find more information on our process to review pull requests and manage issues [in this document](docs/content/contributing/maintainers.md).


## Contributing

If you'd like to contribute to the project, refer to the [contributing documentation](CONTRIBUTING.md).

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md).
By participating in this project, you agree to abide by its terms.

## Release Cycle

- We usually release 3/4 new versions (e.g. 1.1.0, 1.2.0, 1.3.0) per year.
- Release Candidates are available before the release (e.g. 1.1.0-rc1, 1.1.0-rc2, 1.1.0-rc3, 1.1.0-rc4, before 1.1.0).
- Bug-fixes (e.g. 1.1.1, 1.1.2, 1.2.1, 1.2.3) are released as needed (no additional features are delivered in those versions, bug-fixes only).

Each version is supported until the next one is released (e.g. 1.1.x will be supported until 1.2.0 is out).

We use [Semantic Versioning](https://semver.org/).

## Mailing Lists

- General announcements, new releases: mail at news+subscribe@traefik.io or on [the online viewer](https://groups.google.com/a/traefik.io/forum/#!forum/news).
- Security announcements: mail at security+subscribe@traefik.io or on [the online viewer](https://groups.google.com/a/traefik.io/forum/#!forum/security).

## Credits

Kudos to [Peka](http://peka.byethost11.com/photoblog/) for his awesome work on the gopher's logo!.

The gopher's logo of Traefik is licensed under the Creative Commons 3.0 Attributions license.

The gopher's logo of Traefik was inspired by the gopher stickers made by [Takuya Ueda](https://twitter.com/tenntenn).
The original Go gopher was designed by [Renee French](https://reneefrench.blogspot.com/).

## 反向代理 demo
```go
package main

import (
"log"
"net/http"
"net/http/httputil"
"net/url"
)

func main() {
    // 创建一个反向代理对象
    targetUrl, err := url.Parse("https://www.example.com")
    if err != nil {
    panic(err)
    }
    proxy := httputil.NewSingleHostReverseProxy(targetUrl)

    // 创建一个 HTTP 服务器
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        // 设置请求头，以便后端服务器能够正确处理 HTTPS 请求
        r.Host = targetUrl.Host
        r.URL.Scheme = targetUrl.Scheme
        r.URL.Host = targetUrl.Host

        // 反向代理请求到后端服务器
        proxy.ServeHTTP(w, r)
    })

    // 启动 HTTP 服务器
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

以上代码中，我们首先创建了一个反向代理对象，并将其配置为代理到 https://www.example.com。然后，我们创建了一个 HTTP 服务器，并将所有请求都转发给反向代理对象进行处理。在处理每个请求时，我们设置了请求头，以便后端服务器能够正确处理 HTTPS 请求。最后，我们启动了 HTTP 服务器，并监听在本地的 8080 端口上。

这样，当我们访问 http://localhost:8080 时，HTTP 服务器会将请求转发给 https://www.example.com，并将后端服务器的响应返回给客户端。注意，在实际使用中，我们需要将 https://www.example.com 替换为真实的 HTTPS 服务地址。


## 变更记录
1. service.proxy: buildProxy
2. ref commit log


## 启动方式-cmd
```shell
./traefik --configfile=sample.toml
```

## 启动方式-idea
```shell
go build github.com/traefik/traefik/v2/cmd/traefik
程序参数配置 --configfile=sample.toml
```

## 启动方式-docker
```shell
docker run --rm  -p 8099:8099 -v sample.toml:/etc/traefik/traefik.toml harbor.jkservice.org/df/traefik:fr0718
```

## 测试说明
1. 启动tests/http-config服务，访问地址：`http://localhost:8000`
2. 启动proxy-service服务，访问地址：`http://localhost:8099`
3. 提供动态配置接口
    ```toml
    [providers.http]
      endpoint = "http://localhost:8000/api/config/yaml"
      pollInterval = "5s"
    ```
    - 动态配置来自于tests/http-config服务，返回yaml配置。
4. 动态配置中使用forward-auth对请求进行权限判断
    ```yaml
      middlewares:
        my-app:
          forwardAuth:
            address: http://localhost:8000/api/auth/token
            trustForwardHeader: true
            authResponseHeadersRegex: ^X-
            authResponseHeaders:
              - "jk-xxxx"
              - "jk-Header"
    
    ```
    - 请求被拦截到接口`http://localhost:8000/api/auth/token`
    - 根据authResponseHeadersRegex，authResponseHeaders配置设置header
5. 访问测试
    ```shell
      curl --location 'http://localhost:8099/api/authtest/test'
    ```
   打印日志信息
    ```text
    ============token===================//auth认证接口打印日志
    ('host', 'localhost:8000')//auth认证服务可以获取到目标服务host
    ('user-agent', 'PostmanRuntime/7.36.0')
    ('accept', '*/*')
    ('accept-encoding', 'gzip, deflate, br')
    ('postman-token', '56362e19-85a0-45f4-98ab-e180786b015b')
    ('x-forwarded-for', '::1')
    ('x-forwarded-host', 'localhost:8099')
    ('x-forwarded-method', 'GET')
    ('x-forwarded-port', '8099')
    ('x-forwarded-proto', 'http')
    ('x-forwarded-server', 'Gavin-MacBook-Pro.local')
    ('x-forwarded-uri', '/api/authtest/test') //auth认证服务可以获取到访问的url
    ('x-real-ip', '::1')
    
    ============test===================//最终目标服务接口打印日志
    ('host', 'localhost:8000')
    ('user-agent', 'PostmanRuntime/7.36.0')
    ('accept', '*/*')
    ('accept-encoding', 'gzip, deflate, br')
    ('jk-header', 'ffffff') //为auth认证接口返回的数据
    ('jk-xxxx', 'xxxx') //为auth认证接口返回的数据
    ('postman-token', '56362e19-85a0-45f4-98ab-e180786b015b')
    ('x-custom-header', 'Some custom value') //为auth认证接口返回的数据
    ('x-forwarded-for', '::1')
    ```
