
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 166.38 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 166.38 mins              | 166.38 mins            |
| knatnetwork/github-runner-kms  | 0.0 mins      |                    |                          |                        |
|                                |               | Build Image        | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder | 0.0 mins      |                    |                          |                        |
|                                |               | Build Image        | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server  | 0.0 mins      |                    |                          |                        |
|                                |               | Build Image        | 0.0 mins                 | 0.0 mins               |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>webp-sh</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| Repo                       | Total Runtime | Workflow Name                   | Workflow Average Runtime | Workflow Total Runtime |
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| webp-sh/webp_server_node   | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_go     | 220.82 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.73 mins                | 29.8 mins              |
|                            |               | CodeQL                          | 2.03 mins                | 38.55 mins             |
|                            |               | Release Binaries                | 5.37 mins                | 10.73 mins             |
|                            |               | Build and release docker images | 17.72 mins               | 141.73 mins            |
| webp-sh/webp               | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java   | 0.0 mins      |                                 |                          |                        |
|                            |               | No workflow name(why?)          | 0.0 mins                 | 0.0 mins               |
| webp-sh/fiber              | 0.0 mins      |                                 |                          |                        |
| webp-sh/gowebp             | 0.0 mins      |                                 |                          |                        |
| webp-sh/go-avif            | 0.0 mins      |                                 |                          |                        |
| webp-sh/docs.webp.sh       | 0.0 mins      |                                 |                          |                        |
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>datafuselabs</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 174355.6 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 118.23 mins              | 6502.52 mins           |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 86.3 mins                | 25114.47 mins          |
|                                     |               | Build Tool                          | 38.49 mins               | 76.98 mins             |
|                                     |               | Dev Linux                           | 22.89 mins               | 37784.82 mins          |
|                                     |               | Dev MacOS                           | 64.52 mins               | 98141.62 mins          |
|                                     |               | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Benchmark                           | 1.29 mins                | 2441.58 mins           |
|                                     |               | Benchmark (trusted)                 | 1.11 mins                | 2106.83 mins           |
|                                     |               | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 1.17 mins                | 2186.78 mins           |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 4967.65 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 23.39 mins               | 3789.38 mins           |
|                                     |               | commit-message-check                | 3.93 mins                | 676.28 mins            |
|                                     |               | Unit test coverage                  | 6.96 mins                | 334.08 mins            |
|                                     |               | DevSkim                             | 0.93 mins                | 3.72 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.07 mins                | 3.15 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.45 mins                | 4.92 mins              |
|                                     |               | .github/workflows/pages.yaml        | 1.22 mins                | 8.52 mins              |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 11.86 mins               | 47.43 mins             |
|                                     |               | pages build and deployment          | 14.31 mins               | 100.17 mins            |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 8.18 mins     |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.45 mins                | 0.45 mins              |
|                                     |               | Typos Check                         | 3.54 mins                | 7.08 mins              |
|                                     |               | pages build and deployment          | 0.65 mins                | 0.65 mins              |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 743.85 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 19.57 mins               | 743.85 mins            |
| datafuselabs/databend-perf          | 1136.55 mins  |                                     |                          |                        |
|                                     |               | Perf                                | 84.73 mins               | 762.55 mins            |
|                                     |               | pages build and deployment          | 0.62 mins                | 3.08 mins              |
|                                     |               | Reload tpch                         | 16.48 mins               | 65.9 mins              |
|                                     |               | Reload hits                         | 53.41 mins               | 267.05 mins            |
|                                     |               | Reload ontime                       | 7.59 mins                | 37.97 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 6.55 mins     |                                     |                          |                        |
|                                     |               | Release Charts                      | 0.43 mins                | 2.98 mins              |
|                                     |               | pages build and deployment          | 0.89 mins                | 3.57 mins              |
| datafuselabs/sqlparser-rs           | 0.0 mins      |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 18.62 mins    |                                     |                          |                        |
|                                     |               | Rust                                | 2.07 mins                | 18.62 mins             |
| datafuselabs/opendal-redirect       | 2.17 mins     |                                     |                          |                        |
|                                     |               | CI                                  | 0.72 mins                | 2.17 mins              |
| datafuselabs/databend-client        | 586.03 mins   |                                     |                          |                        |
|                                     |               | ci                                  | 8.2 mins                 | 573.97 mins            |
|                                     |               | publish                             | 4.02 mins                | 12.07 mins             |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'message': 'Server Error'}
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 2849.47 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 15.97 mins               | 63.88 mins             |
|                                    |               | BR & Lightning                                       | 1.05 mins                | 721.18 mins            |
|                                    |               | Dumpling                                             | 9.27 mins                | 1733.12 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.91 mins                | 300.03 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 230.8 mins    |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.77 mins                | 230.8 mins             |
| pingcap/kvproto                    | 1357.43 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 4.15 mins                | 435.97 mins            |
|                                    |               | Golang Test                                          | 1.43 mins                | 150.1 mins             |
|                                    |               | Rust Test                                            | 7.35 mins                | 771.37 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5908.98 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.71 mins                | 7.1 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.2 mins                 | 70.13 mins             |
|                                    |               | external-link-check                                  | 7.12 mins                | 28.5 mins              |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 19.48 mins             |
|                                    |               | ci                                                   | 4.1 mins                 | 4424.32 mins           |
|                                    |               | Links                                                | 3.13 mins                | 12.53 mins             |
|                                    |               | bot                                                  | 0.82 mins                | 18.08 mins             |
|                                    |               | cron                                                 | 1.44 mins                | 43.2 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.62 mins                | 605.93 mins            |
|                                    |               | Prevent Deletion                                     | 0.62 mins                | 679.7 mins             |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 6006.52 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.47 mins                | 5.22 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.23 mins                | 71.73 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                                   | 3.94 mins                | 4922.18 mins           |
|                                    |               | Links                                                | 1.22 mins                | 4.88 mins              |
|                                    |               | Flush All PDF                                        | 0.25 mins                | 1.97 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.45 mins                | 518.73 mins            |
|                                    |               | Prevent Deletion                                     | 0.38 mins                | 480.52 mins            |
|                                    |               | Flush PDF by Version                                 | 0.26 mins                | 1.28 mins              |
| pingcap/tidb-binlog                | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqlgram                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/mydumper                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/blog                       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
|                                    |               | Merge Schedule                                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | links                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins      |                                                      |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins      |                                                      |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/blog-cn                    | 0.47 mins     |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn             | 0.47 mins                | 0.47 mins              |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark                    | 4124.12 mins  |                                                      |                          |                        |
|                                    |               | TLS test                                             | 13.6 mins                | 924.5 mins             |
|                                    |               | alter-primary-key-false-test                         | 9.25 mins                | 628.77 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 18.19 mins               | 1309.9 mins            |
|                                    |               | Follower Read test                                   | 9.59 mins                | 651.78 mins            |
|                                    |               | Close inactive issues                                | 0.24 mins                | 7.28 mins              |
|                                    |               | License checker                                      | 1.11 mins                | 84.23 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 6.81 mins                | 517.65 mins            |
| pingcap/octopus                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/grpc                       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | PR AutoFix                                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/jepsen                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins      |                                                      |                          |                        |
| pingcap/chaos                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/meetup                     | 0.0 mins      |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/mysqlx-driver              | 0.0 mins      |                                                      |                          |                        |
| pingcap/campaign                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/community                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lightning             | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-ctl                   | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-vision                | 0.0 mins      |                                                      |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins      |                                                      |                          |                        |
| pingcap/tla-plus                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-ycsb                    | 14.43 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.59 mins                | 7.78 mins              |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.22 mins                | 6.65 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 7088.42 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 1066.49 mins             | 2132.98 mins           |
|                                    |               | chaos                                                | 23.07 mins               | 2653.6 mins            |
|                                    |               | ci                                                   | 17.12 mins               | 2293.93 mins           |
|                                    |               | Close stale issues/prs                               | 0.26 mins                | 7.9 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 4160.48 mins  |                                                      |                          |                        |
|                                    |               | Pull Request CI                                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins      |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/benchmarksql               | 0.0 mins      |                                                      |                          |                        |
| pingcap/gofail                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/work-reporter              | 0.0 mins      |                                                      |                          |                        |
| pingcap/dm                         | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Test binlog 999999                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build & Lint                                         | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade via TiUP                                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream database switch                             | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins      |                                                      |                          |                        |
| pingcap/log                        | 8.72 mins     |                                                      |                          |                        |
|                                    |               | Audit License                                        | 0.99 mins                | 5.97 mins              |
|                                    |               | Unit Test                                            | 0.46 mins                | 2.75 mins              |
| pingcap/tiflash                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | .github/workflows/assign_project.yml                 | 0.0 mins                 | 0.0 mins               |
| pingcap/poco                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/capnproto                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/boost-extra                | 0.0 mins      |                                                      |                          |                        |
| pingcap/kdt                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/failpoint                  | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build & Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins      |                                                      |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidiff                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/fn                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/diag                       | 64.83 mins    |                                                      |                          |                        |
|                                    |               | reprotest                                            | 11.72 mins               | 46.9 mins              |
|                                    |               | static-tests                                         | 3.59 mins                | 17.93 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 43787.8 mins  |                                                      |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.26 mins                | 170.28 mins            |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 30.54 mins               | 6412.58 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                                     | 14.43 mins               | 3029.33 mins           |
|                                    |               | DM Chaos                                             | 27.91 mins               | 5860.97 mins           |
|                                    |               | DM Web UI Lint                                       | 1.51 mins                | 4.52 mins              |
|                                    |               | Upstream Database Switch                             | 16.02 mins               | 3364.6 mins            |
|                                    |               | Design Docs Lint                                     | 0.41 mins                | 22.73 mins             |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CDC Integration Tests                                | 18.18 mins               | 16106.47 mins          |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                                  | 5.5 mins                 | 1154.57 mins           |
| pingcap/br                         | 91.68 mins    |                                                      |                          |                        |
|                                    |               | build                                                | 9.86 mins                | 69.02 mins             |
|                                    |               | compatibility-test                                   | 3.24 mins                | 22.67 mins             |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 2.23 mins     |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.12 mins                | 2.23 mins              |
| pingcap/kops                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/sysutil                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Test                                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins      |                                                      |                          |                        |
|                                    |               | (experimental) Ember CLI tests (core)                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Linting                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | Tests                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse-chat-integration | 0.0 mins      |                                                      |                          |                        |
| pingcap/discourse_docker           | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-helper                | 0.0 mins      |                                                      |                          |                        |
| pingcap/dumpling                   | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
