# ops s3 backup remote

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s3-backup-remote_20260525T210919_result.json`
- **Structured JSON:** [`ca432e526fe4cfac8ac2.json`](../../sessions/ca/ca432e526fe4cfac8ac2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Tarball 有效（可列出文件）。4.3G 太大不适合做完整 listing。直接给结果报告。

---

## 打包完成报告

| 项目 | 详情 |
|------|------|
| **tarball 路径** | `/root/autodl-tmp/exec-sim-repair-verifier_remote.tar.gz` |
| **tarball 大小** | **4.3 GB** |
| **打包后磁盘剩余** | 34 GB（/root/autodl-tmp 数据盘） |

### 打包内容（项目原始 6.4G）
- **代码文件**: 所有 .py, .sh 脚本（训练/评估/分析）
- **checkpoints**: 全部 LoRA checkpoints（~4.3G，含 cls8b, cwm8b, cwm_rank32 等多个 seed 变体）
- **data/**: 自定义数据集（~1.7G）
- **results/**: 评估结果（~11M）
- **artifacts/**: 产出文件（~4.1M）
- **wandb/**: 本地 wandb 缓存（排除 media 大文件）
- **docs/**: 文档

### 排除内容
- `__pycache__`, `*.pyc`
- `*.venv*`, `.cache`
- `pretrained_models`（公开预训练模型）
- `*.log`（日志文件）
- `wandb/*/files/media`（wandb 大媒体文件）
- **注意**：项目无 `.git` 目录

### SCP 回 BE 的命令
在 BE 上执行：
```bash
scp connect.westd.seetacloud.com:/root/autodl-tmp/exec-sim-repair-verifier_remote.tar.gz /tmp/
```

---
