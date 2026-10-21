# ops s3 backup archive

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s3-backup-archive_20260525T205549_result.json`
- **Structured JSON:** [`09a6f9d8f7d5b41c5b2b.json`](../../sessions/09/09a6f9d8f7d5b41c5b2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

备份完成。以下是最终汇报：

---

## 备份结果

### (a) Tarball
- **路径**: `/root/autodl-tmp/exec-sim-repair-verifier-final-20260525T205829Z.tar.gz`（远程服务器）
- **大小**: 5.9 GB (6,279,884,689 bytes)

### (b) S3 URI
```
s3://agent-ml-manager-backups-emnlp/manager-backup/backends/exec-sim-repair-verifier/project-archive/exec-sim-repair-verifier-final-20260525T205829Z.tar.gz
```

### (c) 上传速率
- **16.4 MB/s**，耗时 364.6s（从远程服务器直接上传 S3，跳过 SCP 中转）

### (d) 备份内容清单

| 目录 | 大小 | 内容 |
|------|------|------|
| **code/** | 148 MB | 项目全部代码（含 data/）：训练/评测脚本（train_*.py, eval_*.py, build_*.py）、数据集文件（JSONL）、结果 JSON |
| **checkpoints/** | 6.7 GB | 42 个训练 run 的 best LoRA adapter（DeepSeek/Qwen3 4B/8B/14B × cls/cwm/traj × 多 seed）+ 7 个 14B func-level checkpoint |
| **results/** | 1.3 GB | eval_results/（77 个评测目录）、experiment_results/（22 组）、logs/、scripts/、runs/、batch test 日志、结果 JSON |
| **data/** | 279 MB | project_data（训练/测试 JSONL）、data_dryrun、swebench_full_s123_snapshot |
| **paper/** | 168 KB | figures（figure2 PDF/PNG）、artifacts（regression results）、plot 和 regression 脚本 |

### 排除项
- 公开模型 (models/ 109GB, .hf_cache 23GB)
- 中间 checkpoint（只保留 best/）
- miniconda3、__pycache__、venv
- 已清理远程 S3 凭证文件

---
