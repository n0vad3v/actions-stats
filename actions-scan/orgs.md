
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
| webp-sh/webp_server_go     | 1114.78 mins  |                                 |                          |                        |
|                            |               | CI check on every PR            | 5.24 mins                | 335.5 mins             |
|                            |               | CodeQL                          | 1.92 mins                | 165.13 mins            |
|                            |               | Integration Tests               | 2.3 mins                 | 18.43 mins             |
|                            |               | Release Binaries                | 1.87 mins                | 11.23 mins             |
|                            |               | Build and release docker images | 24.35 mins               | 584.48 mins            |
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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 36531.87 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cancel PR Workflow                  | 0.05 mins                | 11.62 mins             |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 80.48 mins               | 11588.52 mins          |
|                                     |               | Build Tool                          | 23.65 mins               | 70.95 mins             |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Benchmark                           | 5.98 mins                | 1549.37 mins           |
|                                     |               | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.4 mins                 | 503.33 mins            |
|                                     |               | Bindings Python                     | 16.36 mins               | 14807.08 mins          |
|                                     |               | Dev                                 | 18.05 mins               | 4224.08 mins           |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 130.24 mins              | 3776.92 mins           |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 1651.82 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 21.59 mins               | 1511.48 mins           |
|                                     |               | commit-message-check                | 0.84 mins                | 50.43 mins             |
|                                     |               | Unit test coverage                  | 4.62 mins                | 73.97 mins             |
|                                     |               | DevSkim                             | 0.88 mins                | 4.38 mins              |
|                                     |               | GPT refine markdown                 | 0.22 mins                | 7.57 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 2.15 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.2 mins                 | 1.83 mins              |
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
| datafuselabs/opensrv                | 256.7 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 8.56 mins                | 256.7 mins             |
| datafuselabs/databend-perf          | 36583.3 mins  |                                     |                          |                        |
|                                     |               | Perf                                | 2103.96 mins             | 16831.68 mins          |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Reload tpch                         | 1860.28 mins             | 7441.13 mins           |
|                                     |               | Reload hits                         | 1439.17 mins             | 5756.7 mins            |
|                                     |               | Reload ontime                       | 1638.45 mins             | 6553.78 mins           |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 27.62 mins    |                                     |                          |                        |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Rust                                | 2.3 mins                 | 27.62 mins             |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 514.97 mins   |                                     |                          |                        |
|                                     |               | ci                                  | 7.61 mins                | 471.9 mins             |
|                                     |               | publish                             | 4.22 mins                | 12.65 mins             |
|                                     |               | release                             | 15.21 mins               | 30.42 mins             |
| datafuselabs/askbend                | 115.18 mins   |                                     |                          |                        |
|                                     |               | ci                                  | 4.08 mins                | 93.83 mins             |
|                                     |               | release                             | 10.68 mins               | 21.35 mins             |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 100, 'workflow_runs': []}
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
| pingcap/tidb                       | 3849.33 mins   |                                                      |                          |                        |
|                                    |                | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR / Compatibility Test                              | 1.75 mins                | 1.75 mins              |
|                                    |                | BR & Lightning                                       | 0.96 mins                | 811.42 mins            |
|                                    |                | Dumpling                                             | 9.8 mins                 | 2420.83 mins           |
|                                    |                | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | misc                                                 | 2.9 mins                 | 584.97 mins            |
|                                    |                | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tipb                       | 74.32 mins     |                                                      |                          |                        |
|                                    |                | Unit Test                                            | 5.72 mins                | 74.32 mins             |
| pingcap/kvproto                    | 751.82 mins    |                                                      |                          |                        |
|                                    |                | C++ Test                                             | 4.65 mins                | 260.6 mins             |
|                                    |                | Golang Test                                          | 1.37 mins                | 76.83 mins             |
|                                    |                | Rust Test                                            | 7.4 mins                 | 414.38 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/docs                       | 11736.88 mins  |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu when they change         | 0.73 mins                | 5.87 mins              |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 0.18 mins                | 44.8 mins              |
|                                    |                | external-link-check                                  | 1996.53 mins             | 7986.12 mins           |
|                                    |                | Automatic Rebase                                     | 0.04 mins                | 57.3 mins              |
|                                    |                | ci                                                   | 3.37 mins                | 2927.17 mins           |
|                                    |                | Links                                                | 2.51 mins                | 10.05 mins             |
|                                    |                | bot                                                  | 0.7 mins                 | 14.1 mins              |
|                                    |                | cron                                                 | 1.37 mins                | 41.2 mins              |
|                                    |                | Links (Fail Fast)                                    | 0.42 mins                | 342.17 mins            |
|                                    |                | Prevent Deletion                                     | 0.35 mins                | 308.12 mins            |
|                                    |                | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 3810.45 mins   |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu when they change         | 0.46 mins                | 0.92 mins              |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 0.18 mins                | 39.12 mins             |
|                                    |                | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Automatic Rebase                                     | 0.04 mins                | 46.1 mins              |
|                                    |                | ci                                                   | 4.52 mins                | 3215.8 mins            |
|                                    |                | Links                                                | 1.86 mins                | 7.45 mins              |
|                                    |                | Flush All PDF                                        | 0.25 mins                | 1.25 mins              |
|                                    |                | Links (Fail Fast)                                    | 0.39 mins                | 255.97 mins            |
|                                    |                | Prevent Deletion                                     | 0.34 mins                | 243.17 mins            |
|                                    |                | Flush PDF by Version                                 | 0.23 mins                | 0.68 mins              |
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
| pingcap/tispark                    | 1329.97 mins   |                                                      |                          |                        |
|                                    |                | TLS test                                             | 11.47 mins               | 309.57 mins            |
|                                    |                | alter-primary-key-false-test                         | 13.07 mins               | 183.05 mins            |
|                                    |                | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                               | 13.88 mins               | 430.43 mins            |
|                                    |                | Follower Read test                                   | 8.31 mins                | 224.42 mins            |
|                                    |                | Close inactive issues                                | 0.23 mins                | 6.82 mins              |
|                                    |                | License checker                                      | 1.08 mins                | 29.2 mins              |
|                                    |                | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                               | 5.43 mins                | 146.48 mins            |
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
| pingcap/tidb-operator              | 5945.2 mins    |                                                      |                          |                        |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/cd.yml                             | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                                | 21.45 mins               | 2852.57 mins           |
|                                    |                | ci                                                   | 17.43 mins               | 3085.3 mins            |
|                                    |                | Close stale issues/prs                               | 0.24 mins                | 7.33 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 679.0 mins     |                                                      |                          |                        |
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
| pingcap/diag                       | 71.88 mins     |                                                      |                          |                        |
|                                    |                | reprotest                                            | 10.65 mins               | 42.58 mins             |
|                                    |                | static-tests                                         | 3.66 mins                | 29.3 mins              |
| pingcap/sqlsmith                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins       |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins       |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins       |                                                      |                          |                        |
| pingcap/tiflow                     | 271166.12 mins |                                                      |                          |                        |
|                                    |                | Auto Assign to Bugs and Questions                    | 0.24 mins                | 99.95 mins             |
|                                    |                | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                                | 21.6 mins                | 4537.02 mins           |
|                                    |                | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Binlog 999999                                     | 14.77 mins               | 3102.15 mins           |
|                                    |                | DM Chaos                                             | 13.78 mins               | 2892.9 mins            |
|                                    |                | DM Web UI Lint                                       | 1.63 mins                | 4.88 mins              |
|                                    |                | Upstream Database Switch                             | 16.12 mins               | 3384.82 mins           |
|                                    |                | Design Docs Lint                                     | 0.35 mins                | 18.83 mins             |
|                                    |                | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | CDC Integration Tests                                | 22.93 mins               | 14260.22 mins          |
|                                    |                | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade DM via TiUP                                  | 200.62 mins              | 42129.8 mins           |
| pingcap/br                         | 0.0 mins       |                                                      |                          |                        |
|                                    |                | build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | compatibility-test                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins       |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 817.07 mins    |                                                      |                          |                        |
|                                    |                | ci                                                   | 27.24 mins               | 817.07 mins            |
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
