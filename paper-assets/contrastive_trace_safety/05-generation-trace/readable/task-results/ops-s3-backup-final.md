# ops s3 backup final

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s3-backup-final_20260525T210641_result.json`
- **Structured JSON:** [`54b619b49a9f70f882fe.json`](../../sessions/54/54b619b49a9f70f882fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**Step 5: 备份汇报**

**(a) Tarball**
- 路径: `/home/ubuntu/contrastive_trace_safety-final.tar.gz`（已上传后清理）
- 大小: **7.15 GB**

**(b) S3 URI**
```
s3://agent-ml-manager-backups-emnlp/manager-backup/backends/contrastive_trace_safety/manual-backup/2026/05/25/contrastive_trace_safety-final.tar.gz
```

**(c) 备份内容清单**

| 部分 | 路径 | 内容 |
|------|------|------|
| **Server** (`cts_final/server/`) | `contrastive_trace_safety_archive/` | `code/`（源码）、`data/`（数据集/trace）、`results/`（实验结果）、`paper/`（论文相关） |
| **Local** (`cts_final/local/project/`) | 完整 BE 项目目录 | `.git/`（完整 git 历史）、`docs/paper/`（LaTeX 论文）、`artifacts/`（58 个子目录）、`checkpoints/`、实验配置（`experiment_plan.yaml`、`decisions.yaml`、`dream_registry.yaml`）、`memory.md`、`ROADMAP.md`、`.claude/` 等 |

---
