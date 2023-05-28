
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 0.0 mins      |                    |                          |                        |
|                                |               | Build Runner Image | 0.0 mins                 | 0.0 mins               |
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
| webp-sh/webp_server_go     | 894.97 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 5.25 mins                | 330.82 mins            |
|                            |               | CodeQL                          | 1.87 mins                | 149.73 mins            |
|                            |               | Release Binaries                | 1.76 mins                | 8.8 mins               |
|                            |               | Build and release docker images | 22.53 mins               | 405.62 mins            |
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
| datafuselabs/databend               | 50064.52 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 145.95 mins              | 5400.23 mins           |
|                                     |               | Cancel PR Workflow                  | 0.07 mins                | 12.58 mins             |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 75.76 mins               | 12500.08 mins          |
|                                     |               | Build Tool                          | 23.81 mins               | 190.48 mins            |
|                                     |               | Dev Linux                           | 19.84 mins               | 21032.3 mins           |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Benchmark                           | 4.71 mins                | 1818.43 mins           |
|                                     |               | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.39 mins                | 554.5 mins             |
|                                     |               | Bindings Python                     | 16.08 mins               | 8555.9 mins            |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 3132.28 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 22.15 mins               | 2791.1 mins            |
|                                     |               | commit-message-check                | 1.02 mins                | 138.95 mins            |
|                                     |               | Unit test coverage                  | 4.83 mins                | 183.35 mins            |
|                                     |               | DevSkim                             | 0.9 mins                 | 4.48 mins              |
|                                     |               | GPT refine markdown                 | 0.22 mins                | 7.5 mins               |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 3.58 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.21 mins                | 3.32 mins              |
|                                     |               | .github/workflows/pages.yaml        | 0.0 mins                 | 0.0 mins               |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/weekly                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 219.17 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 7.31 mins                | 219.17 mins            |
| datafuselabs/databend-perf          | 34487.92 mins |                                     |                          |                        |
|                                     |               | Perf                                | 1841.94 mins             | 14735.55 mins          |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Reload tpch                         | 1860.14 mins             | 7440.57 mins           |
|                                     |               | Reload hits                         | 1439.39 mins             | 5757.55 mins           |
|                                     |               | Reload ontime                       | 1638.56 mins             | 6554.25 mins           |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 66.98 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 2.7 mins                 | 62.2 mins              |
|                                     |               | Release Charts                      | 0.39 mins                | 1.55 mins              |
|                                     |               | pages build and deployment          | 0.81 mins                | 3.23 mins              |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 10.03 mins    |                                     |                          |                        |
|                                     |               | Rust                                | 1.67 mins                | 10.03 mins             |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 454.13 mins   |                                     |                          |                        |
|                                     |               | ci                                  | 5.46 mins                | 327.73 mins            |
|                                     |               | publish                             | 4.05 mins                | 28.37 mins             |
|                                     |               | release                             | 16.34 mins               | 98.03 mins             |
| datafuselabs/askbend                | 38.83 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 3.88 mins                | 38.83 mins             |
|                                     |               | release                             | 0.0 mins                 | 0.0 mins               |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime  | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins       |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins       |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb                       | 4053.85 mins   |                                                      |                          |                        |
|                                    |                | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR / Compatibility Test                              | 1.75 mins                | 1.75 mins              |
|                                    |                | BR & Lightning                                       | 1.09 mins                | 804.03 mins            |
|                                    |                | Dumpling                                             | 9.67 mins                | 2861.85 mins           |
|                                    |                | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | misc                                                 | 2.89 mins                | 355.85 mins            |
|                                    |                | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tipb                       | 101.63 mins    |                                                      |                          |                        |
|                                    |                | Unit Test                                            | 5.65 mins                | 101.63 mins            |
| pingcap/kvproto                    | 705.37 mins    |                                                      |                          |                        |
|                                    |                | C++ Test                                             | 4.63 mins                | 245.45 mins            |
|                                    |                | Golang Test                                          | 1.33 mins                | 70.28 mins             |
|                                    |                | Rust Test                                            | 7.35 mins                | 389.63 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/docs                       | 15416.73 mins  |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu when they change         | 0.42 mins                | 1.27 mins              |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 0.24 mins                | 65.1 mins              |
|                                    |                | external-link-check                                  | 1965.92 mins             | 11795.53 mins          |
|                                    |                | Automatic Rebase                                     | 0.08 mins                | 108.4 mins             |
|                                    |                | ci                                                   | 3.46 mins                | 2730.12 mins           |
|                                    |                | Links                                                | 3.31 mins                | 13.23 mins             |
|                                    |                | bot                                                  | 0.7 mins                 | 14.02 mins             |
|                                    |                | cron                                                 | 1.34 mins                | 40.2 mins              |
|                                    |                | Links (Fail Fast)                                    | 0.46 mins                | 336.2 mins             |
|                                    |                | Prevent Deletion                                     | 0.39 mins                | 312.67 mins            |
|                                    |                | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 3627.48 mins   |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu when they change         | 0.46 mins                | 0.92 mins              |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 0.18 mins                | 39.27 mins             |
|                                    |                | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Automatic Rebase                                     | 0.05 mins                | 47.37 mins             |
|                                    |                | ci                                                   | 4.44 mins                | 3045.25 mins           |
|                                    |                | Links                                                | 2.18 mins                | 8.73 mins              |
|                                    |                | Flush All PDF                                        | 0.25 mins                | 1.23 mins              |
|                                    |                | Links (Fail Fast)                                    | 0.39 mins                | 241.97 mins            |
|                                    |                | Prevent Deletion                                     | 0.35 mins                | 242.37 mins            |
|                                    |                | Flush PDF by Version                                 | 0.19 mins                | 0.38 mins              |
| pingcap/tidb-binlog                | 0.0 mins       |                                                      |                          |                        |
| pingcap/sqlgram                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/mydumper                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/blog                       | 0.0 mins       |                                                      |                          |                        |
|                                    |                | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Links                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
|                                    |                | Merge Schedule                                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | links                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins       |                                                      |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins       |                                                      |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/blog-cn                    | 0.0 mins       |                                                      |                          |                        |
|                                    |                | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog-cn             | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins       |                                                      |                          |                        |
| pingcap/tispark                    | 1261.98 mins   |                                                      |                          |                        |
|                                    |                | TLS test                                             | 11.86 mins               | 272.87 mins            |
|                                    |                | alter-primary-key-false-test                         | 11.57 mins               | 231.38 mins            |
|                                    |                | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                               | 14.25 mins               | 384.7 mins             |
|                                    |                | Follower Read test                                   | 8.7 mins                 | 200.02 mins            |
|                                    |                | Close inactive issues                                | 0.23 mins                | 7.0 mins               |
|                                    |                | License checker                                      | 1.05 mins                | 26.28 mins             |
|                                    |                | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                               | 5.59 mins                | 139.73 mins            |
| pingcap/octopus                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/grpc                       | 0.0 mins       |                                                      |                          |                        |
|                                    |                | PR AutoFix                                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/jepsen                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins       |                                                      |                          |                        |
| pingcap/chaos                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/meetup                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/mysqlx-driver              | 0.0 mins       |                                                      |                          |                        |
| pingcap/campaign                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/community                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-lightning             | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-ctl                   | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-vision                | 0.0 mins       |                                                      |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins       |                                                      |                          |                        |
| pingcap/tla-plus                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-ycsb                    | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Docker Image CI                                      | 0.0 mins                 | 0.0 mins               |
|                                    |                | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tispark-test-data          | 0.0 mins       |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins       |                                                      |                          |                        |
|                                    |                | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-operator              | 4741.48 mins   |                                                      |                          |                        |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/cd.yml                             | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                                | 21.79 mins               | 2484.33 mins           |
|                                    |                | ci                                                   | 16.66 mins               | 2249.67 mins           |
|                                    |                | Close stale issues/prs                               | 0.25 mins                | 7.48 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 1481.47 mins   |                                                      |                          |                        |
|                                    |                | Pull Request CI                                      | 0.0 mins                 | 0.0 mins               |
|                                    |                | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins       |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/benchmarksql               | 0.0 mins       |                                                      |                          |                        |
| pingcap/gofail                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/work-reporter              | 0.0 mins       |                                                      |                          |                        |
| pingcap/dm                         | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Test binlog 999999                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build & Lint                                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade via TiUP                                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upstream database switch                             | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins       |                                                      |                          |                        |
| pingcap/log                        | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Audit License                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Unit Test                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 0.0 mins       |                                                      |                          |                        |
|                                    |                | .github/workflows/assign_project.yml                 | 0.0 mins                 | 0.0 mins               |
| pingcap/poco                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/capnproto                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/boost-extra                | 0.0 mins       |                                                      |                          |                        |
| pingcap/kdt                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/failpoint                  | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build & Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins       |                                                      |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidiff                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/fn                         | 0.0 mins       |                                                      |                          |                        |
| pingcap/diag                       | 120.87 mins    |                                                      |                          |                        |
|                                    |                | reprotest                                            | 11.07 mins               | 77.5 mins              |
|                                    |                | static-tests                                         | 3.61 mins                | 43.37 mins             |
| pingcap/sqlsmith                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins       |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins       |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins       |                                                      |                          |                        |
| pingcap/tiflow                     | 268220.82 mins |                                                      |                          |                        |
|                                    |                | Auto Assign to Bugs and Questions                    | 0.23 mins                | 97.3 mins              |
|                                    |                | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                                | 21.59 mins               | 4533.18 mins           |
|                                    |                | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Binlog 999999                                     | 14.81 mins               | 3109.43 mins           |
|                                    |                | DM Chaos                                             | 13.94 mins               | 2926.38 mins           |
|                                    |                | DM Web UI Lint                                       | 1.5 mins                 | 3.0 mins               |
|                                    |                | Upstream Database Switch                             | 16.2 mins                | 3402.27 mins           |
|                                    |                | Design Docs Lint                                     | 0.35 mins                | 22.68 mins             |
|                                    |                | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | CDC Integration Tests                                | 20.74 mins               | 12546.98 mins          |
|                                    |                | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade DM via TiUP                                  | 200.62 mins              | 42129.45 mins          |
| pingcap/br                         | 0.0 mins       |                                                      |                          |                        |
|                                    |                | build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | compatibility-test                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins       |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 455.73 mins    |                                                      |                          |                        |
|                                    |                | ci                                                   | 15.19 mins               | 455.73 mins            |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-tpc                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | workflow                                             | 0.0 mins                 | 0.0 mins               |
| pingcap/kops                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/sysutil                    | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Test                                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins       |                                                      |                          |                        |
|                                    |                | (experimental) Ember CLI tests (core)                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Linting                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | Tests                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse-chat-integration | 0.0 mins       |                                                      |                          |                        |
| pingcap/discourse_docker           | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-helper                | 0.0 mins       |                                                      |                          |                        |
| pingcap/dumpling                   | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
