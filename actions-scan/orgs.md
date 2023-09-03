
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+----------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                             | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+----------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless      | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless      | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner        | 554.98 mins   |                    |                          |                        |
|                                  |               | Build Runner Image | 277.49 mins              | 554.98 mins            |
| knatnetwork/github-runner-kms    | 0.0 mins      |                    |                          |                        |
|                                  |               | Build Image        | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder   | 0.0 mins      |                    |                          |                        |
|                                  |               | Build Image        | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server    | 0.0 mins      |                    |                          |                        |
|                                  |               | Build Image        | 0.0 mins                 | 0.0 mins               |
| knatnetwork/github-runner-kms-rs | 217.38 mins   |                    |                          |                        |
|                                  |               | Build Image        | 72.46 mins               | 217.38 mins            |
+----------------------------------+---------------+--------------------+--------------------------+------------------------+

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
| webp-sh/webp_server_go              | 157.17 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 5.33 mins                | 26.65 mins             |
|                                     |               | CI check on every push          | 2.57 mins                | 7.72 mins              |
|                                     |               | CodeQL                          | 1.73 mins                | 20.78 mins             |
|                                     |               | Integration Tests               | 2.69 mins                | 13.45 mins             |
|                                     |               | Release Binaries                | 2.37 mins                | 4.73 mins              |
|                                     |               | Build and release docker images | 16.77 mins               | 83.83 mins             |
| webp-sh/webp                        | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python          | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java            | 0.0 mins      |                                 |                          |                        |
|                                     |               | No workflow name(why?)          | 0.0 mins                 | 0.0 mins               |
| webp-sh/gowebp                      | 0.0 mins      |                                 |                          |                        |
| webp-sh/go-avif                     | 0.0 mins      |                                 |                          |                        |
| webp-sh/docs.webp.sh                | 0.0 mins      |                                 |                          |                        |
| webp-sh/libvips                     | 71.55 mins    |                                 |                          |                        |
|                                     |               | Build and release docker images | 71.55 mins               | 71.55 mins             |
| webp-sh/halo-plugin-webp-cloud      | 0.0 mins      |                                 |                          |                        |
|                                     |               | Build Plugin JAR File           | 0.0 mins                 | 0.0 mins               |
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
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 80074.77 mins |                                     |                          |                        |
|                                     |               | Release                             | 94.11 mins               | 4517.22 mins           |
|                                     |               | Cancel PR Workflow                  | 0.07 mins                | 20.73 mins             |
|                                     |               | Production                          | 105.47 mins              | 17613.2 mins           |
|                                     |               | Build Tool                          | 25.53 mins               | 51.07 mins             |
|                                     |               | Crowdin Action                      | 3.32 mins                | 640.05 mins            |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.41 mins                | 564.43 mins            |
|                                     |               | Bindings Python                     | 31.18 mins               | 32705.22 mins          |
|                                     |               | Dev                                 | 20.84 mins               | 21856.13 mins          |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 31.16 mins               | 1775.93 mins           |
|                                     |               | PR Assistant                        | 0.16 mins                | 294.08 mins            |
|                                     |               | Scheduled                           | 3.34 mins                | 36.7 mins              |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 729.53 mins   |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 24.18 mins               | 725.35 mins            |
|                                     |               | commit-message-check                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Unit test coverage                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | DevSkim                             | 0.84 mins                | 4.18 mins              |
|                                     |               | GPT refine markdown                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/issue-welcome.yml | 0.0 mins                 | 0.0 mins               |
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
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 299.52 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 9.98 mins                | 299.52 mins            |
| datafuselabs/databend-perf          | 148.62 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 10.65 mins               | 85.23 mins             |
|                                     |               | pages build and deployment          | 0.53 mins                | 3.18 mins              |
|                                     |               | Reload tpch                         | 6.91 mins                | 27.65 mins             |
|                                     |               | Reload hits                         | 3.95 mins                | 19.75 mins             |
|                                     |               | Reload ontime                       | 3.2 mins                 | 12.8 mins              |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 24.63 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 2.17 mins                | 21.68 mins             |
|                                     |               | Release Charts                      | 0.36 mins                | 1.07 mins              |
|                                     |               | pages build and deployment          | 0.94 mins                | 1.88 mins              |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-jdbc          | 404.37 mins   |                                     |                          |                        |
|                                     |               | Release Workflow                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | Tests                               | 13.48 mins               | 404.37 mins            |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 19.12 mins    |                                     |                          |                        |
|                                     |               | publish                             | 2.24 mins                | 4.48 mins              |
|                                     |               | Rust                                | 1.13 mins                | 14.63 mins             |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 1158.1 mins   |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 7.04 mins                | 288.65 mins            |
|                                     |               | Bindings Python                     | 2.9 mins                 | 63.88 mins             |
|                                     |               | CI                                  | 10.08 mins               | 584.87 mins            |
|                                     |               | PR Assistant                        | 0.53 mins                | 28.52 mins             |
|                                     |               | Publish                             | 7.98 mins                | 47.9 mins              |
|                                     |               | Release                             | 28.86 mins               | 144.28 mins            |
| datafuselabs/askbend                | 14.3 mins     |                                     |                          |                        |
|                                     |               | ci                                  | 7.15 mins                | 14.3 mins              |
|                                     |               | release                             | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend_fiddle        | 0.0 mins      |                                     |                          |                        |
|                                     |               | Pylint                              | 0.0 mins                 | 0.0 mins               |
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
| pingcap/tidb                       | 5340.33 mins  |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 1.47 mins                | 1.47 mins              |
|                                    |               | BR & Lightning                               | 4.25 mins                | 3343.5 mins            |
|                                    |               | Dumpling                                     | 10.38 mins               | 1432.87 mins           |
|                                    |               | Pessimistic Tests                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                         | 2.76 mins                | 546.82 mins            |
|                                    |               | Leaked Secrets Scan                          | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 15.5 mins     |                                              |                          |                        |
|                                    |               | Unit Test                                    | 7.75 mins                | 15.5 mins              |
| pingcap/kvproto                    | 441.58 mins   |                                              |                          |                        |
|                                    |               | C++ Test                                     | 4.4 mins                 | 140.92 mins            |
|                                    |               | Golang Test                                  | 1.33 mins                | 45.07 mins             |
|                                    |               | Rust Test                                    | 7.52 mins                | 255.6 mins             |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3456.52 mins  |                                              |                          |                        |
|                                    |               | Upload media files to Qiniu when they change | 1.15 mins                | 10.33 mins             |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                     | 0.18 mins                | 43.77 mins             |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 49.43 mins             |
|                                    |               | ci                                           | 3.52 mins                | 2706.8 mins            |
|                                    |               | Links                                        | 2.28 mins                | 9.12 mins              |
|                                    |               | bot                                          | 0.71 mins                | 14.9 mins              |
|                                    |               | cron                                         | 1.18 mins                | 14.1 mins              |
|                                    |               | Links (Fail Fast)                            | 0.43 mins                | 327.0 mins             |
|                                    |               | Prevent Deletion                             | 0.36 mins                | 281.07 mins            |
|                                    |               | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 3503.12 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 4.52 mins                | 2914.38 mins           |
|                                    |               | Trigger docs site update                     | 0.18 mins                | 43.22 mins             |
|                                    |               | Flush PDF by Version                         | 0.23 mins                | 0.93 mins              |
|                                    |               | Flush All PDF                                | 0.23 mins                | 1.38 mins              |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.4 mins                 | 257.97 mins            |
|                                    |               | Links                                        | 2.9 mins                 | 11.62 mins             |
|                                    |               | Upload media files to Qiniu when they change | 0.43 mins                | 1.72 mins              |
|                                    |               | Prevent Deletion                             | 0.35 mins                | 227.47 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 44.43 mins             |
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
| pingcap/tispark                    | 241.43 mins   |                                              |                          |                        |
|                                    |               | TLS test                                     | 7.96 mins                | 31.85 mins             |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | Update changelog manually                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 14.08 mins               | 112.67 mins            |
|                                    |               | Follower Read test                           | 8.38 mins                | 33.52 mins             |
|                                    |               | Close inactive issues                        | 0.23 mins                | 6.85 mins              |
|                                    |               | License checker                              | 0.93 mins                | 5.55 mins              |
|                                    |               | .github/workflows/license-checker-config.yml | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                       | 8.5 mins                 | 51.0 mins              |
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
| pingcap/tidb-operator              | 4875.6 mins   |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 49.71 mins               | 1889.1 mins            |
|                                    |               | ci                                           | 22.92 mins               | 2979.13 mins           |
|                                    |               | Close stale issues/prs                       | 0.25 mins                | 7.37 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 577.37 mins   |                                              |                          |                        |
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
| pingcap/diag                       | 143.55 mins   |                                              |                          |                        |
|                                    |               | reprotest                                    | 10.41 mins               | 83.27 mins             |
|                                    |               | static-tests                                 | 4.02 mins                | 60.28 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                              |                          |                        |
| pingcap/tiflow                     | 64427.63 mins |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.23 mins                | 84.12 mins             |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 21.77 mins               | 4572.15 mins           |
|                                    |               | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                             | 15.76 mins               | 3309.23 mins           |
|                                    |               | DM Chaos                                     | 13.9 mins                | 2918.1 mins            |
|                                    |               | DM Web UI Lint                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream Database Switch                     | 17.55 mins               | 3685.27 mins           |
|                                    |               | Design Docs Lint                             | 0.35 mins                | 22.37 mins             |
|                                    |               | Upgrade DM via TiUP                          | 200.62 mins              | 42129.68 mins          |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 577.52 mins   |                                              |                          |                        |
|                                    |               | ci                                           | 17.49 mins               | 577.13 mins            |
|                                    |               | release                                      | 0.38 mins                | 0.38 mins              |
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
