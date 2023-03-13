
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 351.18 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 117.06 mins              | 351.18 mins            |
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
| webp-sh/webp_server_go     | 155.98 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.54 mins                | 28.33 mins             |
|                            |               | Release Binaries                | 2.68 mins                | 2.68 mins              |
|                            |               | Build and release docker images | 15.36 mins               | 92.15 mins             |
|                            |               | CodeQL                          | 1.93 mins                | 32.82 mins             |
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
| datafuselabs/databend               | 144346.82 mins |                                     |                          |                        |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 109.43 mins              | 4924.45 mins           |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 86.02 mins               | 23998.27 mins          |
|                                     |                | Build Tool                          | 34.49 mins               | 172.45 mins            |
|                                     |                | Dev Linux                           | 21.38 mins               | 28502.35 mins          |
|                                     |                | Dev MacOS                           | 61.07 mins               | 81403.57 mins          |
|                                     |                | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Benchmark                           | 2.7 mins                 | 4280.87 mins           |
|                                     |                | Benchmark Commentator (trusted)     | 0.09 mins                | 143.22 mins            |
|                                     |                | Release Repository                  | 1.43 mins                | 4.28 mins              |
|                                     |                | Typos Check                         | 1.36 mins                | 917.37 mins            |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 10038.32 mins  |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 55.24 mins               | 8175.45 mins           |
|                                     |                | commit-message-check                | 7.28 mins                | 1244.18 mins           |
|                                     |                | Unit test coverage                  | 8.74 mins                | 375.62 mins            |
|                                     |                | DevSkim                             | 0.92 mins                | 3.67 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.06 mins                | 1.85 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 4.6 mins                 | 55.23 mins             |
|                                     |                | .github/workflows/pages.yaml        | 3.77 mins                | 26.42 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 10.23 mins               | 51.17 mins             |
|                                     |                | pages build and deployment          | 14.96 mins               | 104.73 mins            |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 15.77 mins     |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.82 mins                | 3.28 mins              |
|                                     |                | Typos Check                         | 3.54 mins                | 7.08 mins              |
|                                     |                | pages build and deployment          | 1.35 mins                | 5.4 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 97982.85 mins  |                                     |                          |                        |
|                                     |                | Benchmark                           | 22.76 mins               | 1866.72 mins           |
|                                     |                | Binding NodeJS CI                   | 7.54 mins                | 1364.97 mins           |
|                                     |                | Bindings Python CI                  | 28.05 mins               | 12539.7 mins           |
|                                     |                | CI                                  | 18.9 mins                | 10056.02 mins          |
|                                     |                | Docs                                | 13.42 mins               | 2669.95 mins           |
|                                     |                | Publish                             | 23.73 mins               | 71.18 mins             |
|                                     |                | Service Test Azblob                 | 8.78 mins                | 2703.72 mins           |
|                                     |                | Service Test Azdfs                  | 9.93 mins                | 3058.0 mins            |
|                                     |                | Service Test Dashmap                | 7.59 mins                | 1350.3 mins            |
|                                     |                | Service Test Fs                     | 11.02 mins               | 3305.13 mins           |
|                                     |                | Service Test Ftp                    | 14.01 mins               | 4245.47 mins           |
|                                     |                | Service Test Gcs                    | 9.99 mins                | 3005.87 mins           |
|                                     |                | Service Test Ghac                   | 10.06 mins               | 3026.8 mins            |
|                                     |                | Service Test HDFS                   | 11.14 mins               | 3341.08 mins           |
|                                     |                | Service Test HDFS and WebHDFS       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test HTTP                   | 11.17 mins               | 3352.22 mins           |
|                                     |                | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test IPMFS                  | 9.69 mins                | 2915.6 mins            |
|                                     |                | Service Test Memcached              | 9.03 mins                | 2744.8 mins            |
|                                     |                | Service Test Memory                 | 8.61 mins                | 2582.83 mins           |
|                                     |                | Service Test Moka                   | 9.51 mins                | 2853.3 mins            |
|                                     |                | Service Test Obs                    | 11.65 mins               | 3506.07 mins           |
|                                     |                | Service Test Oss                    | 10.81 mins               | 3263.73 mins           |
|                                     |                | Service Test Redis                  | 9.31 mins                | 2792.55 mins           |
|                                     |                | Service Test RocksDB                | 15.35 mins               | 4697.65 mins           |
|                                     |                | Service Test S3                     | 11.82 mins               | 3581.32 mins           |
|                                     |                | Service Test Sled                   | 8.68 mins                | 2656.53 mins           |
|                                     |                | Service Test WebDAV                 | 17.32 mins               | 5472.37 mins           |
|                                     |                | Service Test WebHDFS                | 10.71 mins               | 3224.83 mins           |
|                                     |                | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 3.49 mins                | 1255.23 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 3.68 mins                | 478.92 mins            |
| datafuselabs/opensrv                | 729.23 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 17.36 mins               | 729.23 mins            |
| datafuselabs/databend-perf          | 1952.15 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 193.64 mins              | 1742.77 mins           |
|                                     |                | pages build and deployment          | 1.03 mins                | 5.15 mins              |
|                                     |                | Reload tpch                         | 16.59 mins               | 66.37 mins             |
|                                     |                | Reload hits                         | 26.56 mins               | 106.25 mins            |
|                                     |                | Reload ontime                       | 7.9 mins                 | 31.62 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 19.38 mins     |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.74 mins                | 8.17 mins              |
|                                     |                | pages build and deployment          | 1.02 mins                | 11.22 mins             |
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
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 3003.98 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 12.57 mins               | 12.57 mins             |
|                                    |               | BR & Lightning                                       | 1.28 mins                | 748.18 mins            |
|                                    |               | Dumpling                                             | 9.45 mins                | 1748.42 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.89 mins                | 494.6 mins             |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 178.05 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.56 mins                | 178.05 mins            |
| pingcap/kvproto                    | 1257.32 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 6.39 mins                | 530.75 mins            |
|                                    |               | Golang Test                                          | 1.77 mins                | 147.32 mins            |
|                                    |               | Rust Test                                            | 6.98 mins                | 579.25 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5480.32 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.52 mins                | 4.7 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 81.65 mins             |
|                                    |               | external-link-check                                  | 2.93 mins                | 17.58 mins             |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 85.7 mins              |
|                                    |               | ci                                                   | 3.77 mins                | 4353.45 mins           |
|                                    |               | Links                                                | 2.89 mins                | 14.43 mins             |
|                                    |               | bot                                                  | 0.79 mins                | 16.68 mins             |
|                                    |               | cron                                                 | 1.31 mins                | 39.35 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.43 mins                | 451.83 mins            |
|                                    |               | Prevent Deletion                                     | 0.36 mins                | 414.93 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5473.62 mins  |                                                      |                          |                        |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                                   | 4.09 mins                | 4507.07 mins           |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 73.38 mins             |
|                                    |               | Flush PDF by Version                                 | 0.28 mins                | 0.55 mins              |
|                                    |               | Flush All PDF                                        | 0.26 mins                | 9.17 mins              |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                                    | 0.4 mins                 | 406.23 mins            |
|                                    |               | Links                                                | 1.6 mins                 | 8.0 mins               |
|                                    |               | Upload media files to Qiniu when they change         | 0.43 mins                | 6.47 mins              |
|                                    |               | Prevent Deletion                                     | 0.34 mins                | 383.65 mins            |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 79.1 mins              |
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
| pingcap/tispark                    | 3283.78 mins  |                                                      |                          |                        |
|                                    |               | TLS test                                             | 13.41 mins               | 750.73 mins            |
|                                    |               | alter-primary-key-false-test                         | 9.22 mins                | 516.38 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 18.02 mins               | 1081.5 mins            |
|                                    |               | Follower Read test                                   | 9.41 mins                | 526.8 mins             |
|                                    |               | Close inactive issues                                | 0.23 mins                | 6.75 mins              |
|                                    |               | License checker                                      | 1.13 mins                | 63.2 mins              |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 6.04 mins                | 338.42 mins            |
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
| pingcap/go-ycsb                    | 43.42 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.67 mins                | 24.0 mins              |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.16 mins                | 19.42 mins             |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 10234.15 mins |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 1066.49 mins             | 2132.98 mins           |
|                                    |               | chaos                                                | 20.86 mins               | 4087.67 mins           |
|                                    |               | ci                                                   | 17.65 mins               | 4006.07 mins           |
|                                    |               | Close stale issues/prs                               | 0.25 mins                | 7.43 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 5075.42 mins  |                                                      |                          |                        |
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
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build & Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins      |                                                      |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidiff                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/fn                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/diag                       | 121.88 mins   |                                                      |                          |                        |
|                                    |               | reprotest                                            | 11.18 mins               | 89.45 mins             |
|                                    |               | static-tests                                         | 3.24 mins                | 32.43 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 51961.25 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 16.01 mins               | 17278.4 mins           |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.54 mins                | 24.83 mins             |
|                                    |               | Upgrade DM via TiUP                                  | 5.33 mins                | 1118.52 mins           |
|                                    |               | DM Chaos                                             | 27.94 mins               | 5867.92 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.27 mins                | 162.0 mins             |
|                                    |               | DM Binlog 999999                                     | 13.97 mins               | 2934.47 mins           |
|                                    |               | Upstream Database Switch                             | 15.56 mins               | 3268.07 mins           |
|                                    |               | CDC Integration Tests                                | 17.83 mins               | 14706.73 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.51 mins                | 4.52 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 31.4 mins                | 6593.58 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
| pingcap/br                         | 10.18 mins    |                                                      |                          |                        |
|                                    |               | compatibility-test                                   | 2.23 mins                | 2.23 mins              |
|                                    |               | build                                                | 7.95 mins                | 7.95 mins              |
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
| pingcap/dumpling                   | 8.17 mins     |                                                      |                          |                        |
|                                    |               | Go                                                   | 8.17 mins                | 8.17 mins              |
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
