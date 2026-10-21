# ops s3 backup

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s3-backup_20260525T205524_result.json`
- **Structured JSON:** [`4b2e71d0560e6f7d0a82.json`](../../sessions/4b/4b2e71d0560e6f7d0a82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 备份完成

| 项目 | 值 |
|------|-----|
| **Tarball** | `entrainment_gated_ft-final-20260525T205624Z.tar.gz` |
| **大小** | 1496.8 MB (1,569,461,077 bytes) |
| **S3 URI** | `s3://agent-ml-manager-backups-emnlp/manager-backup/backends/entrainment_gated_ft/project-archive/entrainment_gated_ft-final-20260525T205624Z.tar.gz` |
| **上传速率** | 16.0 MB/s (93.5s) |

**注意**：由于 BE 机器无法直连 westb-48145（SSH 密钥认证失败），跳过了 Step 2 的 SCP 步骤，改为从服务器直接上传到 S3。已清理服务器上的临时凭证脚本。

---
