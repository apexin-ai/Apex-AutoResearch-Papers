# deploy cqa1 pi05 experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-pi05-experiments_20260521T212812_result.json`
- **Structured JSON:** [`78624526ff16baff11e1.json`](../../sessions/78/78624526ff16baff11e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功运行并进入 eval 循环：

| 实验 | GPU | 显存 | Pruning | 状态 |
|------|-----|------|---------|------|
| **A**: `eval_pi05_l2norm_k085_object_seed42` | GPU2 | 10262/24564 MiB | l2norm keep=217/256 | RUNNING |
| **B**: `eval_pi05_random_k03_object_seed43` | GPU3 | 10134/24564 MiB | random keep=76/256 | RUNNING |

部署总结：
- 磁盘 71%（无需清理）
- π0.5 权重从 HuggingFace 下载完成（7.47GB）
- eval 脚本通过 heredoc 传输到 cqa1
- 修复了 `google/paligemma-3b-pt-224` tokenizer 缓存缺失问题
- 两个实验在 tmux session 中运行，日志写入 `logs/` 目录
- 显存 ~10GB/24GB，无 OOM 风险
- Registry 已更新为 RUNNING

---
