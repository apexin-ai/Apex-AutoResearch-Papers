# backup execute final backup

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_backup_execute-final-backup_20260525T211320_result.json`
- **Structured JSON:** [`48091ea43b114c8f61c3.json`](../../sessions/48/48091ea43b114c8f61c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

上传成功。Step 6 汇报：

---

## S3 备份完成

### (a) 各 tarball 文件名 + 大小

| 文件 | 大小 |
|------|------|
| `schema_semantic_constrained_ie_be_local.tar.gz` | 3.0G |
| `schema_semantic_constrained_ie_westd-16980.tar.gz` | 94M |
| `schema_semantic_constrained_ie_westd-21461.tar.gz` | 2.2G |

### (b) 最终 tarball

- 路径：`/home/ubuntu/s3_staging/schema_semantic_constrained_ie-final-20260525T215124Z.tar.gz`
- 大小：5.2G (5,506,461,787 bytes)

### (c) S3 URI

```
s3://agent-ml-manager-backups-emnlp/manager-backup/backends/schema_semantic_constrained_ie/project-archive/schema_semantic_constrained_ie-final-20260525T215124Z.tar.gz
```

### (d) 上传速率

119.3 MB/s，耗时 44.0s

### (e) 备份内容清单

| 服务器 | 包含目录 |
|--------|---------|
| **BE local** | `projects/schema_semantic_constrained_ie/`（代码、artifacts、checkpoints、data、compiler、figures、docs、paper 等） |
| **westd-16980** | `schema_semantic_constrained_ie/`（代码、outputs、logs、data） |
| **westd-21461** | `schema_semantic_constrained_ie/`（代码、checkpoints/qwen3_8b_lora_wikievents 1.2G、checkpoints/llama_lora_docred 1.2G、outputs、logs）+ `autodl-tmp/schema_outputs/` |

### (f) 每台服务器数据总大小

| 服务器 | 原始大小 | 压缩后 |
|--------|---------|--------|
| BE local | 3.8G | 3.0G |
| westd-16980 | 693M | 94M |
| westd-21461 | 2.75G（代码 2.6G + outputs 145M）| 2.2G |
| **合计** | **~7.2G** | **5.2G** |

---
