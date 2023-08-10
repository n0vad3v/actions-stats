
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 483.95 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 241.97 mins              | 483.95 mins            |
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
| webp-sh/webp_server_go              | 706.53 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 4.42 mins                | 114.87 mins            |
|                                     |               | CI check on every push          | 1.69 mins                | 15.17 mins             |
|                                     |               | CodeQL                          | 2.38 mins                | 114.13 mins            |
|                                     |               | Integration Tests               | 2.68 mins                | 69.58 mins             |
|                                     |               | Release Binaries                | 2.17 mins                | 15.2 mins              |
|                                     |               | Build and release docker images | 23.6 mins                | 377.58 mins            |
| webp-sh/webp                        | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python          | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java            | 0.0 mins      |                                 |                          |                        |
|                                     |               | No workflow name(why?)          | 0.0 mins                 | 0.0 mins               |
| webp-sh/gowebp                      | 0.0 mins      |                                 |                          |                        |
| webp-sh/go-avif                     | 0.0 mins      |                                 |                          |                        |
| webp-sh/docs.webp.sh                | 0.0 mins      |                                 |                          |                        |
| webp-sh/libvips                     | 71.55 mins    |                                 |                          |                        |
|                                     |               | Build and release docker images | 71.55 mins               | 71.55 mins             |
| webp-sh/halo-plugin-webp-cloud      | 2.48 mins     |                                 |                          |                        |
|                                     |               | Build Plugin JAR File           | 1.24 mins                | 2.48 mins              |
| webp-sh/wordpress-plugin-webp-cloud | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_bench                  | 0.0 mins      |                                 |                          |                        |
| webp-sh/blog-comments               | 0.0 mins      |                                 |                          |                        |
| webp-sh/govips                      | 9.02 mins     |                                 |                          |                        |
|                                     |               | build                           | 9.02 mins                | 9.02 mins              |
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
| datafuselabs/databend               | 114720.75 mins |                                     |                          |                        |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 106.84 mins              | 4273.68 mins           |
|                                     |                | Cancel PR Workflow                  | 0.07 mins                | 23.25 mins             |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 174.54 mins              | 32638.23 mins          |
|                                     |                | Build Tool                          | 23.4 mins                | 23.4 mins              |
|                                     |                | Crowdin Action                      | 4.43 mins                | 57.6 mins              |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 0.41 mins                | 662.5 mins             |
|                                     |                | Bindings Python                     | 41.56 mins               | 50500.28 mins          |
|                                     |                | Dev                                 | 19.83 mins               | 24152.37 mins          |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Cloud                               | 26.42 mins               | 2060.82 mins           |
|                                     |                | PR Assistant                        | 0.17 mins                | 328.62 mins            |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 1596.07 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 22.93 mins               | 1467.47 mins           |
|                                     |                | commit-message-check                | 1.41 mins                | 70.28 mins             |
|                                     |                | Unit test coverage                  | 4.51 mins                | 45.08 mins             |
|                                     |                | DevSkim                             | 0.88 mins                | 3.53 mins              |
|                                     |                | GPT refine markdown                 | 0.26 mins                | 7.88 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 1.58 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.23 mins                | 0.23 mins              |
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
| datafuselabs/opensrv                | 378.33 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 12.61 mins               | 378.33 mins            |
| datafuselabs/databend-perf          | 457.83 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 29.1 mins                | 261.93 mins            |
|                                     |                | pages build and deployment          | 0.53 mins                | 3.72 mins              |
|                                     |                | Reload tpch                         | 18.02 mins               | 72.08 mins             |
|                                     |                | Reload hits                         | 14.96 mins               | 74.82 mins             |
|                                     |                | Reload ontime                       | 9.06 mins                | 45.28 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 14.28 mins     |                                     |                          |                        |
|                                     |                | ci                                  | 4.34 mins                | 13.03 mins             |
|                                     |                | Release Charts                      | 0.43 mins                | 0.43 mins              |
|                                     |                | pages build and deployment          | 0.82 mins                | 0.82 mins              |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins       |                                     |                          |                        |
| datafuselabs/jsonb                  | 3.07 mins      |                                     |                          |                        |
|                                     |                | publish                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Rust                                | 0.77 mins                | 3.07 mins              |
| datafuselabs/opendal-redirect       | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 2054.25 mins   |                                     |                          |                        |
|                                     |                | Bindings Node.js                    | 11.49 mins               | 907.48 mins            |
|                                     |                | Bindings Python                     | 2.2 mins                 | 59.42 mins             |
|                                     |                | CI                                  | 7.78 mins                | 824.73 mins            |
|                                     |                | PR Assistant                        | 0.2 mins                 | 17.52 mins             |
|                                     |                | Publish                             | 5.71 mins                | 45.67 mins             |
|                                     |                | Release                             | 22.16 mins               | 199.43 mins            |
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
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 4569.32 mins  |                                                      |                          |                        |
|                                    |               | BR / Compatibility Test                              | 1.85 mins                | 1.85 mins              |
|                                    |               | BR & Lightning                                       | 4.55 mins                | 2884.08 mins           |
|                                    |               | Dumpling                                             | 10.64 mins               | 1340.28 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.91 mins                | 342.87 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 131.22 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 6.91 mins                | 131.22 mins            |
| pingcap/kvproto                    | 747.35 mins   |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 4.57 mins                | 255.92 mins            |
|                                    |               | Golang Test                                          | 1.42 mins                | 79.28 mins             |
|                                    |               | Rust Test                                            | 7.36 mins                | 412.15 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 3978.28 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.6 mins                 | 5.42 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.18 mins                | 49.72 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 56.82 mins             |
|                                    |               | ci                                                   | 3.41 mins                | 3131.58 mins           |
|                                    |               | Links                                                | 1.7 mins                 | 6.8 mins               |
|                                    |               | bot                                                  | 0.7 mins                 | 15.42 mins             |
|                                    |               | cron                                                 | 1.4 mins                 | 36.38 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.39 mins                | 358.75 mins            |
|                                    |               | Prevent Deletion                                     | 0.34 mins                | 317.4 mins             |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 4705.18 mins  |                                                      |                          |                        |
|                                    |               | ci                                                   | 4.4 mins                 | 3927.23 mins           |
|                                    |               | Trigger docs site update                             | 0.18 mins                | 48.4 mins              |
|                                    |               | Flush PDF by Version                                 | 0.25 mins                | 2.03 mins              |
|                                    |               | Flush All PDF                                        | 0.31 mins                | 1.25 mins              |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                                    | 0.39 mins                | 347.85 mins            |
|                                    |               | Links                                                | 1.59 mins                | 7.97 mins              |
|                                    |               | Upload media files to Qiniu when they change         | 0.58 mins                | 2.9 mins               |
|                                    |               | Prevent Deletion                                     | 0.35 mins                | 311.92 mins            |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 55.63 mins             |
| pingcap/tidb-binlog                | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqlgram                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/mydumper                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/blog                       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins      |                                                      |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins      |                                                      |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/blog-cn                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn             | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark                    | 535.33 mins   |                                                      |                          |                        |
|                                    |               | TLS test                                             | 14.19 mins               | 113.55 mins            |
|                                    |               | alter-primary-key-false-test                         | 0.0 mins                 | 0.0 mins               |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 14.58 mins               | 175.02 mins            |
|                                    |               | Follower Read test                                   | 10.17 mins               | 81.35 mins             |
|                                    |               | Close inactive issues                                | 0.25 mins                | 7.6 mins               |
|                                    |               | License checker                                      | 1.09 mins                | 18.6 mins              |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 8.19 mins                | 139.22 mins            |
| pingcap/octopus                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins      |                                                      |                          |                        |
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
| pingcap/go-ycsb                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 10264.08 mins |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 43.83 mins               | 6135.63 mins           |
|                                    |               | ci                                                   | 22.89 mins               | 4121.07 mins           |
|                                    |               | Close stale issues/prs                               | 0.25 mins                | 7.38 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 1310.57 mins  |                                                      |                          |                        |
|                                    |               | Pull Request CI                                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins      |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins      |                                                      |                          |                        |
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
| pingcap/log                        | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Audit License                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Unit Test                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | .github/workflows/assign_project.yml                 | 0.0 mins                 | 0.0 mins               |
| pingcap/poco                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/capnproto                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/boost-extra                | 0.0 mins      |                                                      |                          |                        |
| pingcap/kdt                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/failpoint                  | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Build & Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins      |                                                      |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidiff                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/fn                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/diag                       | 149.4 mins    |                                                      |                          |                        |
|                                    |               | reprotest                                            | 10.05 mins               | 100.52 mins            |
|                                    |               | static-tests                                         | 3.49 mins                | 48.88 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 63733.25 mins |                                                      |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.24 mins                | 92.97 mins             |
|                                    |               | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 21.32 mins               | 4476.98 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                                     | 15.28 mins               | 3209.78 mins           |
|                                    |               | DM Chaos                                             | 14.08 mins               | 2956.2 mins            |
|                                    |               | DM Web UI Lint                                       | 2.04 mins                | 6.12 mins              |
|                                    |               | Upstream Database Switch                             | 17.18 mins               | 3608.43 mins           |
|                                    |               | Design Docs Lint                                     | 0.36 mins                | 10.82 mins             |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                                  | 200.62 mins              | 42129.9 mins           |
| pingcap/br                         | 0.0 mins      |                                                      |                          |                        |
|                                    |               | build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 1836.7 mins   |                                                      |                          |                        |
|                                    |               | ci                                                   | 23.52 mins               | 1834.88 mins           |
|                                    |               | release                                              | 0.36 mins                | 1.82 mins              |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 0.0 mins      |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 0.0 mins                 | 0.0 mins               |
| pingcap/kops                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/sysutil                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Test                                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/discourse-chat-integration | 0.0 mins      |                                                      |                          |                        |
| pingcap/discourse_docker           | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-helper                | 0.0 mins      |                                                      |                          |                        |
| pingcap/dumpling                   | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tipocket                   | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build-workflow                                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | Pre-Check                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Test                                                 | 0.0 mins                 | 0.0 mins               |
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
