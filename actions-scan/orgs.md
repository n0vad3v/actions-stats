
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 778.87 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 259.62 mins              | 778.87 mins            |
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
+-------------------------------------+---------------+---------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                   | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+---------------------------------+--------------------------+------------------------+
| webp-sh/webp_server_node            | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_go              | 516.15 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 4.7 mins                 | 65.75 mins             |
|                                     |               | CI check on every push          | 1.69 mins                | 13.55 mins             |
|                                     |               | CodeQL                          | 2.21 mins                | 77.18 mins             |
|                                     |               | Integration Tests               | 2.69 mins                | 37.72 mins             |
|                                     |               | Release Binaries                | 2.14 mins                | 12.83 mins             |
|                                     |               | Build and release docker images | 22.08 mins               | 309.12 mins            |
| webp-sh/webp                        | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python          | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java            | 0.0 mins      |                                 |                          |                        |
|                                     |               | No workflow name(why?)          | 0.0 mins                 | 0.0 mins               |
| webp-sh/gowebp                      | 0.0 mins      |                                 |                          |                        |
| webp-sh/go-avif                     | 0.0 mins      |                                 |                          |                        |
| webp-sh/docs.webp.sh                | 0.0 mins      |                                 |                          |                        |
| webp-sh/libvips                     | 71.55 mins    |                                 |                          |                        |
|                                     |               | Build and release docker images | 71.55 mins               | 71.55 mins             |
| webp-sh/halo-plugin-webp-cloud      | 1.8 mins      |                                 |                          |                        |
|                                     |               | Build Plugin JAR File           | 1.8 mins                 | 1.8 mins               |
| webp-sh/wordpress-plugin-webp-cloud | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_bench                  | 0.0 mins      |                                 |                          |                        |
| webp-sh/blog-comments               | 0.0 mins      |                                 |                          |                        |
| webp-sh/govips                      | 19.78 mins    |                                 |                          |                        |
|                                     |               | build                           | 6.59 mins                | 19.78 mins             |
+-------------------------------------+---------------+---------------------------------+--------------------------+------------------------+

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
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 107322.08 mins |                                     |                          |                        |
|                                     |                | Release                             | 108.18 mins              | 4651.82 mins           |
|                                     |                | Cancel PR Workflow                  | 0.07 mins                | 22.02 mins             |
|                                     |                | Production                          | 161.88 mins              | 28652.85 mins          |
|                                     |                | Build Tool                          | 25.53 mins               | 51.07 mins             |
|                                     |                | Crowdin Action                      | 3.37 mins                | 235.95 mins            |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 0.41 mins                | 636.2 mins             |
|                                     |                | Bindings Python                     | 39.77 mins               | 46885.38 mins          |
|                                     |                | Dev                                 | 20.39 mins               | 24104.98 mins          |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Cloud                               | 32.01 mins               | 1760.35 mins           |
|                                     |                | PR Assistant                        | 0.16 mins                | 321.47 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 1280.18 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 23.08 mins               | 1177.27 mins           |
|                                     |                | commit-message-check                | 1.75 mins                | 56.1 mins              |
|                                     |                | Unit test coverage                  | 4.51 mins                | 36.05 mins             |
|                                     |                | DevSkim                             | 0.89 mins                | 3.57 mins              |
|                                     |                | GPT refine markdown                 | 0.27 mins                | 6.03 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 1.17 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.0 mins                 | 0.0 mins               |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/weekly                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 357.95 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 11.93 mins               | 357.95 mins            |
| datafuselabs/databend-perf          | 404.15 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 25.03 mins               | 225.27 mins            |
|                                     |                | pages build and deployment          | 0.54 mins                | 2.68 mins              |
|                                     |                | Reload tpch                         | 18.2 mins                | 72.82 mins             |
|                                     |                | Reload hits                         | 12.91 mins               | 64.53 mins             |
|                                     |                | Reload ontime                       | 7.77 mins                | 38.85 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 26.0 mins      |                                     |                          |                        |
|                                     |                | ci                                  | 3.31 mins                | 23.15 mins             |
|                                     |                | Release Charts                      | 0.36 mins                | 1.07 mins              |
|                                     |                | pages build and deployment          | 0.89 mins                | 1.78 mins              |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins       |                                     |                          |                        |
| datafuselabs/jsonb                  | 0.0 mins       |                                     |                          |                        |
|                                     |                | publish                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Rust                                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal-redirect       | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 591.63 mins    |                                     |                          |                        |
|                                     |                | Bindings Node.js                    | 4.73 mins                | 104.08 mins            |
|                                     |                | Bindings Python                     | 2.35 mins                | 56.33 mins             |
|                                     |                | CI                                  | 9.99 mins                | 369.7 mins             |
|                                     |                | PR Assistant                        | 0.2 mins                 | 6.6 mins               |
|                                     |                | Publish                             | 7.02 mins                | 21.05 mins             |
|                                     |                | Release                             | 16.93 mins               | 33.87 mins             |
| datafuselabs/askbend                | 0.0 mins       |                                     |                          |                        |
|                                     |                | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | release                             | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend_fiddle        | 0.0 mins       |                                     |                          |                        |
|                                     |                | Pylint                              | 0.0 mins                 | 0.0 mins               |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+

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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+------------------------------------+---------------+----------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+----------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                              |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                              |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                              |                          |                        |
| pingcap/check                      | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb                       | 5236.23 mins  |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 1.66 mins                | 3.32 mins              |
|                                    |               | BR & Lightning                               | 4.57 mins                | 3164.08 mins           |
|                                    |               | Dumpling                                     | 10.68 mins               | 1548.02 mins           |
|                                    |               | Pessimistic Tests                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                         | 2.87 mins                | 505.33 mins            |
|                                    |               | Leaked Secrets Scan                          | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 131.22 mins   |                                              |                          |                        |
|                                    |               | Unit Test                                    | 6.91 mins                | 131.22 mins            |
| pingcap/kvproto                    | 607.2 mins    |                                              |                          |                        |
|                                    |               | C++ Test                                     | 4.65 mins                | 200.13 mins            |
|                                    |               | Golang Test                                  | 1.45 mins                | 62.27 mins             |
|                                    |               | Rust Test                                    | 8.02 mins                | 344.8 mins             |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3803.4 mins   |                                              |                          |                        |
|                                    |               | Upload media files to Qiniu when they change | 0.62 mins                | 4.97 mins              |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                     | 0.18 mins                | 47.1 mins              |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 53.25 mins             |
|                                    |               | ci                                           | 3.44 mins                | 2998.82 mins           |
|                                    |               | Links                                        | 1.5 mins                 | 5.98 mins              |
|                                    |               | bot                                          | 0.7 mins                 | 15.3 mins              |
|                                    |               | cron                                         | 1.4 mins                 | 30.73 mins             |
|                                    |               | Links (Fail Fast)                            | 0.4 mins                 | 342.87 mins            |
|                                    |               | Prevent Deletion                             | 0.35 mins                | 304.38 mins            |
|                                    |               | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 4345.73 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 4.4 mins                 | 3625.73 mins           |
|                                    |               | Trigger docs site update                     | 0.18 mins                | 45.33 mins             |
|                                    |               | Flush PDF by Version                         | 0.26 mins                | 2.05 mins              |
|                                    |               | Flush All PDF                                | 0.31 mins                | 1.23 mins              |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.39 mins                | 322.08 mins            |
|                                    |               | Links                                        | 1.42 mins                | 5.68 mins              |
|                                    |               | Upload media files to Qiniu when they change | 0.58 mins                | 2.9 mins               |
|                                    |               | Prevent Deletion                             | 0.35 mins                | 290.48 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 50.23 mins             |
| pingcap/tidb-binlog                | 0.0 mins      |                                              |                          |                        |
| pingcap/sqlgram                    | 0.0 mins      |                                              |                          |                        |
| pingcap/mydumper                   | 0.0 mins      |                                              |                          |                        |
| pingcap/blog                       | 0.0 mins      |                                              |                          |                        |
|                                    |               | ci                                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins      |                                              |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins      |                                              |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins      |                                              |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins      |                                              |                          |                        |
| pingcap/blog-cn                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn     | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark                    | 538.45 mins   |                                              |                          |                        |
|                                    |               | TLS test                                     | 14.19 mins               | 113.55 mins            |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | Update changelog manually                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 14.86 mins               | 178.27 mins            |
|                                    |               | Follower Read test                           | 10.17 mins               | 81.35 mins             |
|                                    |               | Close inactive issues                        | 0.25 mins                | 7.47 mins              |
|                                    |               | License checker                              | 1.09 mins                | 18.6 mins              |
|                                    |               | .github/workflows/license-checker-config.yml | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                       | 8.19 mins                | 139.22 mins            |
| pingcap/octopus                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins      |                                              |                          |                        |
| pingcap/jepsen                     | 0.0 mins      |                                              |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins      |                                              |                          |                        |
| pingcap/chaos                      | 0.0 mins      |                                              |                          |                        |
| pingcap/meetup                     | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/mysqlx-driver              | 0.0 mins      |                                              |                          |                        |
| pingcap/campaign                   | 0.0 mins      |                                              |                          |                        |
| pingcap/community                  | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-lightning             | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-ctl                   | 0.0 mins      |                                              |                          |                        |
|                                    |               | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-vision                | 0.0 mins      |                                              |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins      |                                              |                          |                        |
| pingcap/tla-plus                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins      |                                              |                          |                        |
| pingcap/go-ycsb                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | Docker Image CI                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | Publish artifacts to github release          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tispark-test-data          | 0.0 mins      |                                              |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                              |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                              |                          |                        |
|                                    |               | testbuild                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-operator              | 10261.05 mins |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 47.73 mins               | 6586.78 mins           |
|                                    |               | ci                                           | 21.7 mins                | 3667.02 mins           |
|                                    |               | Close stale issues/prs                       | 0.24 mins                | 7.25 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 1545.12 mins  |                                              |                          |                        |
|                                    |               | Pull Request CI                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | License checker                              | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins      |                                              |                          |                        |
| pingcap/parser                     | 0.0 mins      |                                              |                          |                        |
| pingcap/benchmarksql               | 0.0 mins      |                                              |                          |                        |
| pingcap/gofail                     | 0.0 mins      |                                              |                          |                        |
| pingcap/work-reporter              | 0.0 mins      |                                              |                          |                        |
| pingcap/dm                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | Test binlog 999999                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build & Lint                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade via TiUP                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream database switch                     | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins      |                                              |                          |                        |
| pingcap/log                        | 0.0 mins      |                                              |                          |                        |
|                                    |               | Audit License                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | .github/workflows/assign_project.yml         | 0.0 mins                 | 0.0 mins               |
| pingcap/poco                       | 0.0 mins      |                                              |                          |                        |
| pingcap/capnproto                  | 0.0 mins      |                                              |                          |                        |
| pingcap/boost-extra                | 0.0 mins      |                                              |                          |                        |
| pingcap/kdt                        | 0.0 mins      |                                              |                          |                        |
| pingcap/failpoint                  | 0.0 mins      |                                              |                          |                        |
|                                    |               | Build & Test                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins      |                                              |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins      |                                              |                          |                        |
| pingcap/tidiff                     | 0.0 mins      |                                              |                          |                        |
| pingcap/fn                         | 0.0 mins      |                                              |                          |                        |
| pingcap/diag                       | 225.15 mins   |                                              |                          |                        |
|                                    |               | reprotest                                    | 10.23 mins               | 143.18 mins            |
|                                    |               | static-tests                                 | 3.73 mins                | 81.97 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                              |                          |                        |
| pingcap/tiflow                     | 65548.88 mins |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.23 mins                | 99.42 mins             |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 21.28 mins               | 4468.72 mins           |
|                                    |               | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                             | 15.52 mins               | 3260.07 mins           |
|                                    |               | DM Chaos                                     | 13.87 mins               | 2912.47 mins           |
|                                    |               | DM Web UI Lint                               | 1.96 mins                | 3.92 mins              |
|                                    |               | Upstream Database Switch                     | 17.43 mins               | 3661.12 mins           |
|                                    |               | Design Docs Lint                             | 0.35 mins                | 10.88 mins             |
|                                    |               | Upgrade DM via TiUP                          | 200.62 mins              | 42130.13 mins          |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 1183.28 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 26.88 mins               | 1182.57 mins           |
|                                    |               | release                                      | 0.36 mins                | 0.72 mins              |
| pingcap/style-guide                | 0.0 mins      |                                              |                          |                        |
| pingcap/go-tpc                     | 0.0 mins      |                                              |                          |                        |
|                                    |               | release                                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                     | 0.0 mins                 | 0.0 mins               |
| pingcap/kops                       | 0.0 mins      |                                              |                          |                        |
| pingcap/sysutil                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins      |                                              |                          |                        |
| pingcap/discourse-chat-integration | 0.0 mins      |                                              |                          |                        |
| pingcap/discourse_docker           | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-helper                | 0.0 mins      |                                              |                          |                        |
| pingcap/dumpling                   | 0.0 mins      |                                              |                          |                        |
|                                    |               | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tipocket                   | 0.0 mins      |                                              |                          |                        |
|                                    |               | Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build-workflow                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Pre-Check                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Test                                         | 0.0 mins                 | 0.0 mins               |
+------------------------------------+---------------+----------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
