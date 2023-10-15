
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+----------------------------------+---------------+------------------------+--------------------------+------------------------+
| Repo                             | Total Runtime | Workflow Name          | Workflow Average Runtime | Workflow Total Runtime |
+----------------------------------+---------------+------------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless      | 0.0 mins      |                        |                          |                        |
| knatnetwork/g2fs-serverless      | 0.0 mins      |                        |                          |                        |
| knatnetwork/github-runner        | 485.98 mins   |                        |                          |                        |
|                                  |               | Build Runner Image     | 161.99 mins              | 485.98 mins            |
| knatnetwork/github-runner-kms    | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder   | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server    | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/github-runner-kms-rs | 0.0 mins      |                        |                          |                        |
|                                  |               | Build Image            | 0.0 mins                 | 0.0 mins               |
+----------------------------------+---------------+------------------------+--------------------------+------------------------+

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
| webp-sh/webp_server_go              | 331.8 mins    |                                 |                          |                        |
|                                     |               | CI check on every PR            | 4.5 mins                 | 22.52 mins             |
|                                     |               | CI check on every push          | 2.43 mins                | 12.15 mins             |
|                                     |               | CodeQL                          | 2.01 mins                | 28.08 mins             |
|                                     |               | Integration Tests               | 2.93 mins                | 14.65 mins             |
|                                     |               | Release Binaries                | 2.27 mins                | 4.55 mins              |
|                                     |               | Build and release docker images | 35.69 mins               | 249.85 mins            |
| webp-sh/webp                        | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python          | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java            | 0.0 mins      |                                 |                          |                        |
|                                     |               | No workflow name(why?)          | 0.0 mins                 | 0.0 mins               |
| webp-sh/gowebp                      | 0.0 mins      |                                 |                          |                        |
| webp-sh/go-avif                     | 0.0 mins      |                                 |                          |                        |
| webp-sh/docs.webp.sh                | 0.0 mins      |                                 |                          |                        |
| webp-sh/libvips                     | 0.0 mins      |                                 |                          |                        |
|                                     |               | Build and release docker images | 0.0 mins                 | 0.0 mins               |
| webp-sh/halo-plugin-webp-cloud      | 0.0 mins      |                                 |                          |                        |
|                                     |               | Build Plugin JAR File           | 0.0 mins                 | 0.0 mins               |
| webp-sh/wordpress-plugin-webp-cloud | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_bench                  | 0.0 mins      |                                 |                          |                        |
| webp-sh/blog-comments               | 0.0 mins      |                                 |                          |                        |
| webp-sh/govips                      | 0.0 mins      |                                 |                          |                        |
|                                     |               | build                           | 0.0 mins                 | 0.0 mins               |
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
| datafuselabs/databend               | 91043.33 mins |                                     |                          |                        |
|                                     |               | Release                             | 80.92 mins               | 3803.32 mins           |
|                                     |               | Cancel PR Workflow                  | 0.12 mins                | 33.95 mins             |
|                                     |               | Production                          | 99.17 mins               | 21618.22 mins          |
|                                     |               | Crowdin Action                      | 3.21 mins                | 818.8 mins             |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.48 mins                | 826.12 mins            |
|                                     |               | Dev                                 | 21.66 mins               | 31040.07 mins          |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 30.99 mins               | 3347.23 mins           |
|                                     |               | PR Assistant                        | 0.24 mins                | 554.53 mins            |
|                                     |               | Scheduled                           | 3.06 mins                | 863.38 mins            |
|                                     |               | Bindings Python                     | 20.72 mins               | 28010.65 mins          |
|                                     |               | Build Tool                          | 21.18 mins               | 127.07 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 681.0 mins    |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 22.54 mins               | 676.07 mins            |
|                                     |               | commit-message-check                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Unit test coverage                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | DevSkim                             | 0.82 mins                | 4.12 mins              |
|                                     |               | GPT refine markdown                 | 0.26 mins                | 0.52 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.05 mins                | 0.1 mins               |
|                                     |               | .github/workflows/issue-welcome.yml | 0.2 mins                 | 0.2 mins               |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 118.92 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 3.96 mins                | 118.92 mins            |
| datafuselabs/databend-perf          | 815.67 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 47.18 mins               | 613.37 mins            |
|                                     |               | pages build and deployment          | 0.61 mins                | 2.43 mins              |
|                                     |               | Reload tpch                         | 1.7 mins                 | 6.8 mins               |
|                                     |               | Reload hits                         | 9.14 mins                | 155.43 mins            |
|                                     |               | Reload ontime                       | 9.41 mins                | 37.63 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 25.05 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 2.51 mins                | 22.58 mins             |
|                                     |               | Release Charts                      | 0.56 mins                | 1.67 mins              |
|                                     |               | pages build and deployment          | 0.8 mins                 | 0.8 mins               |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-go            | 3.73 mins     |                                     |                          |                        |
|                                     |               | CI                                  | 0.93 mins                | 3.73 mins              |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-py            | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release on Version Change           | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-sqlalchemy    | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-jdbc          | 370.77 mins   |                                     |                          |                        |
|                                     |               | Release Workflow                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | Tests                               | 52.97 mins               | 370.77 mins            |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 16.5 mins     |                                     |                          |                        |
|                                     |               | publish                             | 4.13 mins                | 4.13 mins              |
|                                     |               | Rust                                | 1.37 mins                | 12.37 mins             |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 1480.25 mins  |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 4.46 mins                | 343.63 mins            |
|                                     |               | Bindings Python                     | 4.45 mins                | 195.68 mins            |
|                                     |               | CI                                  | 7.79 mins                | 771.47 mins            |
|                                     |               | PR Assistant                        | 0.23 mins                | 17.82 mins             |
|                                     |               | Publish                             | 10.62 mins               | 63.75 mins             |
|                                     |               | Release                             | 12.56 mins               | 87.9 mins              |
| datafuselabs/askbend                | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
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
| pingcap/tidb                       | 5371.55 mins  |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR & Lightning                               | 5.39 mins                | 3067.43 mins           |
|                                    |               | Dumpling                                     | 10.37 mins               | 2167.02 mins           |
|                                    |               | misc                                         | 2.68 mins                | 136.85 mins            |
|                                    |               | Leaked Secrets Scan                          | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 46.43 mins    |                                              |                          |                        |
|                                    |               | Unit Test                                    | 6.63 mins                | 46.43 mins             |
| pingcap/kvproto                    | 560.22 mins   |                                              |                          |                        |
|                                    |               | C++ Test                                     | 8.7 mins                 | 226.2 mins             |
|                                    |               | Golang Test                                  | 1.43 mins                | 52.77 mins             |
|                                    |               | Rust Test                                    | 7.6 mins                 | 281.25 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3630.43 mins  |                                              |                          |                        |
|                                    |               | Upload media files to Qiniu when they change | 0.52 mins                | 11.0 mins              |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                     | 0.2 mins                 | 43.68 mins             |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 45.77 mins             |
|                                    |               | ci                                           | 3.74 mins                | 2841.02 mins           |
|                                    |               | Links                                        | 1.54 mins                | 6.15 mins              |
|                                    |               | bot                                          | 0.74 mins                | 15.63 mins             |
|                                    |               | cron                                         | 2.47 mins                | 12.33 mins             |
|                                    |               | Links (Fail Fast)                            | 0.46 mins                | 344.67 mins            |
|                                    |               | Prevent Deletion                             | 0.4 mins                 | 310.18 mins            |
|                                    |               | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 3760.02 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 4.39 mins                | 3125.52 mins           |
|                                    |               | Trigger docs site update                     | 0.2 mins                 | 34.98 mins             |
|                                    |               | Flush PDF by Version                         | 0.28 mins                | 1.42 mins              |
|                                    |               | Flush All PDF                                | 0.26 mins                | 1.58 mins              |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.41 mins                | 289.08 mins            |
|                                    |               | Links                                        | 1.31 mins                | 5.25 mins              |
|                                    |               | Upload media files to Qiniu when they change | 0.46 mins                | 3.7 mins               |
|                                    |               | Prevent Deletion                             | 0.37 mins                | 265.13 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 33.35 mins             |
| pingcap/tidb-binlog                | 0.0 mins      |                                              |                          |                        |
| pingcap/sqlgram                    | 0.0 mins      |                                              |                          |                        |
| pingcap/mydumper                   | 0.0 mins      |                                              |                          |                        |
| pingcap/blog                       | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins      |                                              |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins      |                                              |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins      |                                              |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins      |                                              |                          |                        |
| pingcap/blog-cn                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn     | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark                    | 358.18 mins   |                                              |                          |                        |
|                                    |               | TLS test                                     | 14.55 mins               | 87.32 mins             |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 14.93 mins               | 149.33 mins            |
|                                    |               | Follower Read test                           | 11.12 mins               | 66.72 mins             |
|                                    |               | Close inactive issues                        | 0.26 mins                | 7.87 mins              |
|                                    |               | License checker                              | 1.02 mins                | 6.15 mins              |
|                                    |               | verify                                       | 6.8 mins                 | 40.8 mins              |
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
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-vision                | 0.0 mins      |                                              |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins      |                                              |                          |                        |
| pingcap/tla-plus                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins      |                                              |                          |                        |
| pingcap/go-ycsb                    | 4.67 mins     |                                              |                          |                        |
|                                    |               | Docker Image CI                              | 2.08 mins                | 2.08 mins              |
|                                    |               | Publish artifacts to github release          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                           | 2.58 mins                | 2.58 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                              |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                              |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                              |                          |                        |
|                                    |               | testbuild                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-operator              | 6634.4 mins   |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                           | 59.08 mins               | 6617.47 mins           |
|                                    |               | Close stale issues/prs                       | 0.56 mins                | 16.93 mins             |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 1135.8 mins   |                                              |                          |                        |
|                                    |               | Pull Request CI                              | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins      |                                              |                          |                        |
| pingcap/parser                     | 0.0 mins      |                                              |                          |                        |
| pingcap/benchmarksql               | 0.0 mins      |                                              |                          |                        |
| pingcap/gofail                     | 0.0 mins      |                                              |                          |                        |
| pingcap/work-reporter              | 0.0 mins      |                                              |                          |                        |
| pingcap/dm                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
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
| pingcap/diag                       | 174.32 mins   |                                              |                          |                        |
|                                    |               | reprotest                                    | 11.28 mins               | 124.13 mins            |
|                                    |               | static-tests                                 | 3.58 mins                | 50.18 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                              |                          |                        |
| pingcap/tiflow                     | 79473.03 mins |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.23 mins                | 56.03 mins             |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 26.69 mins               | 5605.4 mins            |
|                                    |               | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                             | 16.93 mins               | 3555.67 mins           |
|                                    |               | DM Chaos                                     | 14.99 mins               | 3147.58 mins           |
|                                    |               | DM Web UI Lint                               | 1.19 mins                | 3.57 mins              |
|                                    |               | Upstream Database Switch                     | 20.21 mins               | 4244.07 mins           |
|                                    |               | Design Docs Lint                             | 0.35 mins                | 9.18 mins              |
|                                    |               | Upgrade DM via TiUP                          | 200.63 mins              | 42131.55 mins          |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 779.92 mins   |                                              |                          |                        |
|                                    |               | ci                                           | 20.0 mins                | 779.92 mins            |
|                                    |               | release                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins      |                                              |                          |                        |
| pingcap/go-tpc                     | 12.83 mins    |                                              |                          |                        |
|                                    |               | release                                      | 0.34 mins                | 0.68 mins              |
|                                    |               | workflow                                     | 1.52 mins                | 12.15 mins             |
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
Error: {'total_count': 100, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
