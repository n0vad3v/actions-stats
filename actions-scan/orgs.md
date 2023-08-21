
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
| webp-sh/webp_server_go              | 219.25 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 5.42 mins                | 32.5 mins              |
|                                     |               | CI check on every push          | 2.56 mins                | 10.25 mins             |
|                                     |               | CodeQL                          | 2.04 mins                | 42.83 mins             |
|                                     |               | Integration Tests               | 2.81 mins                | 16.85 mins             |
|                                     |               | Release Binaries                | 2.37 mins                | 4.73 mins              |
|                                     |               | Build and release docker images | 18.68 mins               | 112.08 mins            |
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
| datafuselabs/databend               | 105421.73 mins |                                     |                          |                        |
|                                     |                | Release                             | 112.67 mins              | 5070.02 mins           |
|                                     |                | Cancel PR Workflow                  | 0.07 mins                | 21.82 mins             |
|                                     |                | Production                          | 159.18 mins              | 27857.02 mins          |
|                                     |                | Build Tool                          | 25.53 mins               | 51.07 mins             |
|                                     |                | Crowdin Action                      | 3.32 mins                | 302.05 mins            |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 0.41 mins                | 613.97 mins            |
|                                     |                | Bindings Python                     | 40.59 mins               | 46229.0 mins           |
|                                     |                | Dev                                 | 20.56 mins               | 23479.78 mins          |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Cloud                               | 34.52 mins               | 1484.15 mins           |
|                                     |                | PR Assistant                        | 0.16 mins                | 312.87 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 904.32 mins    |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 23.46 mins               | 868.05 mins            |
|                                     |                | commit-message-check                | 1.93 mins                | 19.32 mins             |
|                                     |                | Unit test coverage                  | 4.31 mins                | 12.93 mins             |
|                                     |                | DevSkim                             | 0.79 mins                | 3.17 mins              |
|                                     |                | GPT refine markdown                 | 0.23 mins                | 0.7 mins               |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 0.15 mins              |
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
| datafuselabs/opensrv                | 372.93 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 12.43 mins               | 372.93 mins            |
| datafuselabs/databend-perf          | 357.77 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 25.54 mins               | 229.88 mins            |
|                                     |                | pages build and deployment          | 0.54 mins                | 3.23 mins              |
|                                     |                | Reload tpch                         | 12.08 mins               | 48.33 mins             |
|                                     |                | Reload hits                         | 9.61 mins                | 48.05 mins             |
|                                     |                | Reload ontime                       | 7.07 mins                | 28.27 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 11.72 mins     |                                     |                          |                        |
|                                     |                | ci                                  | 2.53 mins                | 10.12 mins             |
|                                     |                | Release Charts                      | 0.32 mins                | 0.63 mins              |
|                                     |                | pages build and deployment          | 0.97 mins                | 0.97 mins              |
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
| datafuselabs/bendsql                | 540.1 mins     |                                     |                          |                        |
|                                     |                | Bindings Node.js                    | 4.73 mins                | 104.08 mins            |
|                                     |                | Bindings Python                     | 2.31 mins                | 48.53 mins             |
|                                     |                | CI                                  | 9.9 mins                 | 326.75 mins            |
|                                     |                | PR Assistant                        | 0.2 mins                 | 5.82 mins              |
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
| pingcap/tidb                       | 5704.8 mins   |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 1.66 mins                | 3.32 mins              |
|                                    |               | BR & Lightning                               | 4.19 mins                | 3304.02 mins           |
|                                    |               | Dumpling                                     | 10.52 mins               | 1778.02 mins           |
|                                    |               | Pessimistic Tests                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                         | 2.8 mins                 | 603.97 mins            |
|                                    |               | Leaked Secrets Scan                          | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 131.22 mins   |                                              |                          |                        |
|                                    |               | Unit Test                                    | 6.91 mins                | 131.22 mins            |
| pingcap/kvproto                    | 434.58 mins   |                                              |                          |                        |
|                                    |               | C++ Test                                     | 4.38 mins                | 140.22 mins            |
|                                    |               | Golang Test                                  | 1.4 mins                 | 44.87 mins             |
|                                    |               | Rust Test                                    | 7.8 mins                 | 249.5 mins             |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3436.07 mins  |                                              |                          |                        |
|                                    |               | Upload media files to Qiniu when they change | 0.68 mins                | 4.1 mins               |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                     | 0.18 mins                | 43.5 mins              |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 47.35 mins             |
|                                    |               | ci                                           | 3.47 mins                | 2709.38 mins           |
|                                    |               | Links                                        | 1.9 mins                 | 9.5 mins               |
|                                    |               | bot                                          | 0.68 mins                | 13.63 mins             |
|                                    |               | cron                                         | 1.36 mins                | 25.78 mins             |
|                                    |               | Links (Fail Fast)                            | 0.4 mins                 | 308.1 mins             |
|                                    |               | Prevent Deletion                             | 0.35 mins                | 274.72 mins            |
|                                    |               | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 3877.33 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 4.35 mins                | 3225.48 mins           |
|                                    |               | Trigger docs site update                     | 0.18 mins                | 39.77 mins             |
|                                    |               | Flush PDF by Version                         | 0.26 mins                | 2.05 mins              |
|                                    |               | Flush All PDF                                | 0.29 mins                | 1.45 mins              |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.4 mins                 | 294.23 mins            |
|                                    |               | Links                                        | 1.69 mins                | 8.43 mins              |
|                                    |               | Upload media files to Qiniu when they change | 0.0 mins                 | 0.0 mins               |
|                                    |               | Prevent Deletion                             | 0.35 mins                | 261.92 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 44.0 mins              |
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
| pingcap/tispark                    | 445.75 mins   |                                              |                          |                        |
|                                    |               | TLS test                                     | 13.7 mins                | 82.2 mins              |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | Update changelog manually                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 15.15 mins               | 151.55 mins            |
|                                    |               | Follower Read test                           | 10.64 mins               | 63.87 mins             |
|                                    |               | Close inactive issues                        | 0.25 mins                | 7.47 mins              |
|                                    |               | License checker                              | 1.1 mins                 | 16.47 mins             |
|                                    |               | .github/workflows/license-checker-config.yml | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                       | 8.28 mins                | 124.2 mins             |
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
| pingcap/tidb-operator              | 9360.63 mins  |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 47.78 mins               | 5589.78 mins           |
|                                    |               | ci                                           | 21.14 mins               | 3763.67 mins           |
|                                    |               | Close stale issues/prs                       | 0.24 mins                | 7.18 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 978.65 mins   |                                              |                          |                        |
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
| pingcap/diag                       | 158.33 mins   |                                              |                          |                        |
|                                    |               | reprotest                                    | 10.46 mins               | 94.13 mins             |
|                                    |               | static-tests                                 | 3.78 mins                | 64.2 mins              |
| pingcap/sqlsmith                   | 0.0 mins      |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                              |                          |                        |
| pingcap/tiflow                     | 65377.05 mins |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.23 mins                | 98.6 mins              |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 21.4 mins                | 4494.15 mins           |
|                                    |               | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                             | 15.57 mins               | 3270.38 mins           |
|                                    |               | DM Chaos                                     | 13.93 mins               | 2925.5 mins            |
|                                    |               | DM Web UI Lint                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream Database Switch                     | 16.74 mins               | 3515.9 mins            |
|                                    |               | Design Docs Lint                             | 0.35 mins                | 12.18 mins             |
|                                    |               | Upgrade DM via TiUP                          | 200.62 mins              | 42129.8 mins           |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 569.3 mins    |                                              |                          |                        |
|                                    |               | ci                                           | 17.78 mins               | 568.97 mins            |
|                                    |               | release                                      | 0.33 mins                | 0.33 mins              |
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
    
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
