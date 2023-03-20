
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
| webp-sh/webp_server_go     | 236.03 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.68 mins                | 47.88 mins             |
|                            |               | Release Binaries                | 2.68 mins                | 2.68 mins              |
|                            |               | Build and release docker images | 17.3 mins                | 138.37 mins            |
|                            |               | CodeQL                          | 1.96 mins                | 47.1 mins              |
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
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 159135.95 mins |                                     |                          |                        |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 110.03 mins              | 5721.43 mins           |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 89.66 mins               | 25104.77 mins          |
|                                     |                | Build Tool                          | 34.49 mins               | 172.45 mins            |
|                                     |                | Dev Linux                           | 23.38 mins               | 32914.45 mins          |
|                                     |                | Dev MacOS                           | 64.08 mins               | 88821.63 mins          |
|                                     |                | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Benchmark                           | 1.97 mins                | 3485.42 mins           |
|                                     |                | Benchmark (trusted)                 | 0.65 mins                | 1163.43 mins           |
|                                     |                | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 1.45 mins                | 1752.37 mins           |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 4964.05 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 22.26 mins               | 3694.47 mins           |
|                                     |                | commit-message-check                | 4.08 mins                | 735.17 mins            |
|                                     |                | Unit test coverage                  | 8.24 mins                | 362.7 mins             |
|                                     |                | DevSkim                             | 0.94 mins                | 3.77 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.07 mins                | 2.2 mins               |
|                                     |                | .github/workflows/issue-welcome.yml | 0.21 mins                | 1.92 mins              |
|                                     |                | .github/workflows/pages.yaml        | 2.34 mins                | 16.35 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 8.73 mins                | 52.4 mins              |
|                                     |                | pages build and deployment          | 13.58 mins               | 95.08 mins             |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 14.9 mins      |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.98 mins                | 2.95 mins              |
|                                     |                | Typos Check                         | 3.54 mins                | 7.08 mins              |
|                                     |                | pages build and deployment          | 1.62 mins                | 4.87 mins              |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 805.78 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 19.19 mins               | 805.78 mins            |
| datafuselabs/databend-perf          | 1659.32 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 155.63 mins              | 1400.63 mins           |
|                                     |                | pages build and deployment          | 1.05 mins                | 5.23 mins              |
|                                     |                | Reload tpch                         | 16.35 mins               | 65.4 mins              |
|                                     |                | Reload hits                         | 39.6 mins                | 158.42 mins            |
|                                     |                | Reload ontime                       | 7.41 mins                | 29.63 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 17.98 mins     |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.77 mins                | 7.68 mins              |
|                                     |                | pages build and deployment          | 1.03 mins                | 10.3 mins              |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins       |                                     |                          |                        |
| datafuselabs/jsonb                  | 18.62 mins     |                                     |                          |                        |
|                                     |                | Rust                                | 2.07 mins                | 18.62 mins             |
| datafuselabs/opendal-redirect       | 2.17 mins      |                                     |                          |                        |
|                                     |                | CI                                  | 0.72 mins                | 2.17 mins              |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+

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
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 2519.8 mins   |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 12.57 mins               | 12.57 mins             |
|                                    |               | BR & Lightning                                       | 0.98 mins                | 560.37 mins            |
|                                    |               | Dumpling                                             | 9.41 mins                | 1608.92 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.92 mins                | 306.7 mins             |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 201.68 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.45 mins                | 201.68 mins            |
| pingcap/kvproto                    | 1345.75 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 6.3 mins                 | 560.3 mins             |
|                                    |               | Golang Test                                          | 1.78 mins                | 158.22 mins            |
|                                    |               | Rust Test                                            | 7.05 mins                | 627.23 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5183.12 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.69 mins                | 9.0 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 71.02 mins             |
|                                    |               | external-link-check                                  | 9.28 mins                | 27.85 mins             |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 75.53 mins             |
|                                    |               | ci                                                   | 4.09 mins                | 3909.67 mins           |
|                                    |               | Links                                                | 2.47 mins                | 12.33 mins             |
|                                    |               | bot                                                  | 0.81 mins                | 16.98 mins             |
|                                    |               | cron                                                 | 1.33 mins                | 40.0 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.54 mins                | 461.45 mins            |
|                                    |               | Prevent Deletion                                     | 0.58 mins                | 559.28 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5692.78 mins  |                                                      |                          |                        |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                                   | 3.88 mins                | 4651.95 mins           |
|                                    |               | Trigger docs site update                             | 0.22 mins                | 76.07 mins             |
|                                    |               | Flush PDF by Version                                 | 0.26 mins                | 1.05 mins              |
|                                    |               | Flush All PDF                                        | 0.27 mins                | 7.75 mins              |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                                    | 0.43 mins                | 481.6 mins             |
|                                    |               | Links                                                | 1.73 mins                | 8.67 mins              |
|                                    |               | Upload media files to Qiniu when they change         | 0.46 mins                | 7.9 mins               |
|                                    |               | Prevent Deletion                                     | 0.38 mins                | 457.8 mins             |
|                                    |               | Automatic Rebase                                     | 0.0 mins                 | 0.0 mins               |
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
| pingcap/tispark                    | 4332.8 mins   |                                                      |                          |                        |
|                                    |               | TLS test                                             | 13.21 mins               | 977.73 mins            |
|                                    |               | alter-primary-key-false-test                         | 9.22 mins                | 681.97 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 17.73 mins               | 1382.92 mins           |
|                                    |               | Follower Read test                                   | 9.54 mins                | 706.0 mins             |
|                                    |               | Close inactive issues                                | 0.23 mins                | 7.03 mins              |
|                                    |               | License checker                                      | 1.1 mins                 | 85.97 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 6.3 mins                 | 491.18 mins            |
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
| pingcap/go-ycsb                    | 29.25 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.69 mins                | 16.13 mins             |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.19 mins                | 13.12 mins             |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 8087.5 mins   |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 1066.49 mins             | 2132.98 mins           |
|                                    |               | chaos                                                | 20.47 mins               | 3091.02 mins           |
|                                    |               | ci                                                   | 16.51 mins               | 2855.97 mins           |
|                                    |               | Close stale issues/prs                               | 0.25 mins                | 7.53 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 5078.18 mins  |                                                      |                          |                        |
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
| pingcap/tiflow                     | 52883.87 mins |                                                      |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.28 mins                | 163.38 mins            |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 0.74 mins                | 2.22 mins              |
|                                    |               | Dataflow Engine Chaos                                | 30.46 mins               | 6396.38 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                                     | 14.27 mins               | 2997.68 mins           |
|                                    |               | DM Chaos                                             | 27.98 mins               | 5876.15 mins           |
|                                    |               | DM Web UI Lint                                       | 1.51 mins                | 4.52 mins              |
|                                    |               | Upstream Database Switch                             | 15.18 mins               | 3186.88 mins           |
|                                    |               | Design Docs Lint                                     | 0.51 mins                | 29.08 mins             |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CDC Integration Tests                                | 17.72 mins               | 15419.4 mins           |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                                  | 5.4 mins                 | 1133.6 mins            |
| pingcap/br                         | 91.68 mins    |                                                      |                          |                        |
|                                    |               | build                                                | 9.86 mins                | 69.02 mins             |
|                                    |               | compatibility-test                                   | 3.24 mins                | 22.67 mins             |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 1.1 mins      |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.1 mins                 | 1.1 mins               |
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
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
