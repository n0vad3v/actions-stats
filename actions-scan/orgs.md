
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
| knatnetwork/github-runner        | 773.03 mins   |                        |                          |                        |
|                                  |               | Build Runner Image     | 193.26 mins              | 773.03 mins            |
| knatnetwork/github-runner-kms    | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder   | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server    | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/github-runner-kms-rs | 442.28 mins   |                        |                          |                        |
|                                  |               | Build Image            | 73.71 mins               | 442.28 mins            |
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
| webp-sh/webp_server_go              | 365.92 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 4.14 mins                | 37.3 mins              |
|                                     |               | CI check on every push          | 2.43 mins                | 12.15 mins             |
|                                     |               | CodeQL                          | 1.95 mins                | 37.07 mins             |
|                                     |               | Integration Tests               | 2.78 mins                | 25.0 mins              |
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
| datafuselabs/databend               | 80598.95 mins |                                     |                          |                        |
|                                     |               | Release                             | 102.91 mins              | 4630.75 mins           |
|                                     |               | Cancel PR Workflow                  | 0.06 mins                | 16.57 mins             |
|                                     |               | Production                          | 100.46 mins              | 21298.22 mins          |
|                                     |               | Crowdin Action                      | 3.42 mins                | 885.98 mins            |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.43 mins                | 767.5 mins             |
|                                     |               | Dev                                 | 17.99 mins               | 25135.95 mins          |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 31.57 mins               | 3315.07 mins           |
|                                     |               | PR Assistant                        | 0.2 mins                 | 444.48 mins            |
|                                     |               | Push on main                        | 3.04 mins                | 704.75 mins            |
|                                     |               | Bindings Python                     | 21.03 mins               | 23388.95 mins          |
|                                     |               | Build Tool                          | 10.73 mins               | 10.73 mins             |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 679.87 mins   |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 22.55 mins               | 676.38 mins            |
|                                     |               | commit-message-check                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Unit test coverage                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | DevSkim                             | 0.87 mins                | 3.48 mins              |
|                                     |               | GPT refine markdown                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/issue-welcome.yml | 0.0 mins                 | 0.0 mins               |
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
| datafuselabs/opensrv                | 201.72 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 4.92 mins                | 201.72 mins            |
| datafuselabs/databend-perf          | 321.57 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 8.86 mins                | 115.18 mins            |
|                                     |               | pages build and deployment          | 0.56 mins                | 2.82 mins              |
|                                     |               | Reload tpch                         | 9.98 mins                | 39.93 mins             |
|                                     |               | Reload hits                         | 7.43 mins                | 126.27 mins            |
|                                     |               | Reload ontime                       | 9.34 mins                | 37.37 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 11.62 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 5.81 mins                | 11.62 mins             |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-jdbc          | 398.48 mins   |                                     |                          |                        |
|                                     |               | Release Workflow                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | Tests                               | 15.33 mins               | 398.48 mins            |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 9.42 mins     |                                     |                          |                        |
|                                     |               | publish                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Rust                                | 1.57 mins                | 9.42 mins              |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 1467.45 mins  |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 4.69 mins                | 281.55 mins            |
|                                     |               | Bindings Python                     | 3.25 mins                | 159.42 mins            |
|                                     |               | CI                                  | 7.78 mins                | 848.33 mins            |
|                                     |               | PR Assistant                        | 0.4 mins                 | 47.03 mins             |
|                                     |               | Publish                             | 9.59 mins                | 57.52 mins             |
|                                     |               | Release                             | 14.72 mins               | 73.6 mins              |
| datafuselabs/askbend                | 69.78 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 8.72 mins                | 69.78 mins             |
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
+------------------------------------+----------------+----------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime  | Workflow Name                                | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+----------------+----------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins       |                                              |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins       |                                              |                          |                        |
| pingcap/go-themis                  | 0.0 mins       |                                              |                          |                        |
| pingcap/sqllogictest               | 0.0 mins       |                                              |                          |                        |
| pingcap/check                      | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb                       | 5951.2 mins    |                                              |                          |                        |
|                                    |                | BR / Compatibility Test                      | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR & Lightning                               | 5.17 mins                | 3568.52 mins           |
|                                    |                | Dumpling                                     | 10.16 mins               | 2032.63 mins           |
|                                    |                | misc                                         | 2.73 mins                | 349.8 mins             |
|                                    |                | Leaked Secrets Scan                          | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                              |                          |                        |
| pingcap/tipb                       | 62.55 mins     |                                              |                          |                        |
|                                    |                | Unit Test                                    | 6.95 mins                | 62.55 mins             |
| pingcap/kvproto                    | 680.92 mins    |                                              |                          |                        |
|                                    |                | C++ Test                                     | 4.41 mins                | 229.17 mins            |
|                                    |                | Golang Test                                  | 1.31 mins                | 70.5 mins              |
|                                    |                | Rust Test                                    | 7.06 mins                | 381.25 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                              |                          |                        |
| pingcap/docs                       | 4216.63 mins   |                                              |                          |                        |
|                                    |                | Upload media files to Qiniu when they change | 1.04 mins                | 10.4 mins              |
|                                    |                | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                     | 0.2 mins                 | 58.12 mins             |
|                                    |                | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Automatic Rebase                             | 0.04 mins                | 60.35 mins             |
|                                    |                | ci                                           | 3.49 mins                | 3236.43 mins           |
|                                    |                | Links                                        | 1.61 mins                | 6.43 mins              |
|                                    |                | bot                                          | 0.72 mins                | 15.87 mins             |
|                                    |                | cron                                         | 2.09 mins                | 31.38 mins             |
|                                    |                | Links (Fail Fast)                            | 0.46 mins                | 425.93 mins            |
|                                    |                | Prevent Deletion                             | 0.39 mins                | 371.72 mins            |
|                                    |                | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 4703.87 mins   |                                              |                          |                        |
|                                    |                | ci                                           | 3.87 mins                | 3835.08 mins           |
|                                    |                | Trigger docs site update                     | 0.19 mins                | 37.28 mins             |
|                                    |                | Flush PDF by Version                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Flush All PDF                                | 0.25 mins                | 1.48 mins              |
|                                    |                | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Links (Fail Fast)                            | 0.42 mins                | 417.5 mins             |
|                                    |                | Links                                        | 1.93 mins                | 7.73 mins              |
|                                    |                | Upload media files to Qiniu when they change | 0.0 mins                 | 0.0 mins               |
|                                    |                | Prevent Deletion                             | 0.37 mins                | 366.0 mins             |
|                                    |                | Automatic Rebase                             | 0.04 mins                | 38.78 mins             |
| pingcap/tidb-binlog                | 0.0 mins       |                                              |                          |                        |
| pingcap/sqlgram                    | 0.0 mins       |                                              |                          |                        |
| pingcap/mydumper                   | 0.0 mins       |                                              |                          |                        |
| pingcap/blog                       | 0.0 mins       |                                              |                          |                        |
|                                    |                | ci                                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog        | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins       |                                              |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins       |                                              |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins       |                                              |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins       |                                              |                          |                        |
| pingcap/blog-cn                    | 0.0 mins       |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog-cn     | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins       |                                              |                          |                        |
| pingcap/tispark                    | 87.3 mins      |                                              |                          |                        |
|                                    |                | TLS test                                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | Update changelog manually                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                       | 19.91 mins               | 79.63 mins             |
|                                    |                | Follower Read test                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | Close inactive issues                        | 0.26 mins                | 7.67 mins              |
|                                    |                | License checker                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                       | 0.0 mins                 | 0.0 mins               |
| pingcap/octopus                    | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins       |                                              |                          |                        |
| pingcap/jepsen                     | 0.0 mins       |                                              |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins       |                                              |                          |                        |
| pingcap/chaos                      | 0.0 mins       |                                              |                          |                        |
| pingcap/meetup                     | 0.0 mins       |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/mysqlx-driver              | 0.0 mins       |                                              |                          |                        |
| pingcap/campaign                   | 0.0 mins       |                                              |                          |                        |
| pingcap/community                  | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-lightning             | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-ctl                   | 0.0 mins       |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-vision                | 0.0 mins       |                                              |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins       |                                              |                          |                        |
| pingcap/tla-plus                   | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins       |                                              |                          |                        |
| pingcap/go-ycsb                    | 0.0 mins       |                                              |                          |                        |
|                                    |                | Docker Image CI                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | Publish artifacts to github release          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tispark-test-data          | 0.0 mins       |                                              |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                              |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-insight               | 0.0 mins       |                                              |                          |                        |
|                                    |                | testbuild                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | release                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-operator              | 1244.58 mins   |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | ci                                           | 20.46 mins               | 1227.8 mins            |
|                                    |                | Close stale issues/prs                       | 0.56 mins                | 16.78 mins             |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 1100.22 mins   |                                              |                          |                        |
|                                    |                | Pull Request CI                              | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins       |                                              |                          |                        |
| pingcap/parser                     | 0.0 mins       |                                              |                          |                        |
| pingcap/benchmarksql               | 0.0 mins       |                                              |                          |                        |
| pingcap/gofail                     | 0.0 mins       |                                              |                          |                        |
| pingcap/work-reporter              | 0.0 mins       |                                              |                          |                        |
| pingcap/dm                         | 0.0 mins       |                                              |                          |                        |
|                                    |                | Test binlog 999999                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade via TiUP                             | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upstream database switch                     | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins       |                                              |                          |                        |
| pingcap/log                        | 0.0 mins       |                                              |                          |                        |
|                                    |                | Audit License                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 0.0 mins       |                                              |                          |                        |
| pingcap/poco                       | 0.0 mins       |                                              |                          |                        |
| pingcap/capnproto                  | 0.0 mins       |                                              |                          |                        |
| pingcap/boost-extra                | 0.0 mins       |                                              |                          |                        |
| pingcap/kdt                        | 0.0 mins       |                                              |                          |                        |
| pingcap/failpoint                  | 0.0 mins       |                                              |                          |                        |
|                                    |                | Build & Test                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins       |                                              |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins       |                                              |                          |                        |
| pingcap/tidiff                     | 0.0 mins       |                                              |                          |                        |
| pingcap/fn                         | 0.0 mins       |                                              |                          |                        |
| pingcap/diag                       | 213.88 mins    |                                              |                          |                        |
|                                    |                | reprotest                                    | 11.23 mins               | 146.02 mins            |
|                                    |                | static-tests                                 | 3.77 mins                | 67.87 mins             |
| pingcap/sqlsmith                   | 0.0 mins       |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins       |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins       |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins       |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins       |                                              |                          |                        |
| pingcap/tiflow                     | 249130.28 mins |                                              |                          |                        |
|                                    |                | Auto Assign to Bugs and Questions            | 0.24 mins                | 74.2 mins              |
|                                    |                | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                        | 27.2 mins                | 5712.22 mins           |
|                                    |                | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Binlog 999999                             | 16.65 mins               | 3495.48 mins           |
|                                    |                | DM Chaos                                     | 14.57 mins               | 3059.97 mins           |
|                                    |                | DM Web UI Lint                               | 1.19 mins                | 3.57 mins              |
|                                    |                | Upstream Database Switch                     | 18.31 mins               | 3845.38 mins           |
|                                    |                | Design Docs Lint                             | 0.37 mins                | 3.67 mins              |
|                                    |                | Upgrade DM via TiUP                          | 200.61 mins              | 42127.5 mins           |
| pingcap/br                         | 0.0 mins       |                                              |                          |                        |
|                                    |                | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins       |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins       |                                              |                          |                        |
| pingcap/advanced-statefulset       | 944.8 mins     |                                              |                          |                        |
|                                    |                | ci                                           | 19.68 mins               | 944.42 mins            |
|                                    |                | release                                      | 0.38 mins                | 0.38 mins              |
| pingcap/style-guide                | 0.0 mins       |                                              |                          |                        |
| pingcap/go-tpc                     | 12.83 mins     |                                              |                          |                        |
|                                    |                | release                                      | 0.34 mins                | 0.68 mins              |
|                                    |                | workflow                                     | 1.52 mins                | 12.15 mins             |
| pingcap/kops                       | 0.0 mins       |                                              |                          |                        |
| pingcap/sysutil                    | 0.0 mins       |                                              |                          |                        |
|                                    |                | Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins       |                                              |                          |                        |
| pingcap/discourse-chat-integration | 0.0 mins       |                                              |                          |                        |
| pingcap/discourse_docker           | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-helper                | 0.0 mins       |                                              |                          |                        |
| pingcap/dumpling                   | 0.0 mins       |                                              |                          |                        |
|                                    |                | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tipocket                   | 0.0 mins       |                                              |                          |                        |
|                                    |                | Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build-workflow                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pre-Check                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Test                                         | 0.0 mins                 | 0.0 mins               |
+------------------------------------+----------------+----------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
