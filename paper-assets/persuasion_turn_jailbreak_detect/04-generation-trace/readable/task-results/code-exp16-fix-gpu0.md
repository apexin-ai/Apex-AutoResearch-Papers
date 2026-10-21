# code exp16 fix gpu0

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-fix-gpu0_20260519T202759_result.json`
- **Structured JSON:** [`c40ba1eb8a3614e42e60.json`](../../sessions/c4/c40ba1eb8a3614e42e60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并在运行。

**汇报**：

| 项目 | 状态 |
|------|------|
| 模型缓存 | DeBERTa-v3-base 离线缓存完整，`TRANSFORMERS_OFFLINE=1` 验证通过 |
| vanilla checkpoints | **3 个 seeds 全部已完成**（42/123/456 均有 12M best.pt），已跳过 |
| 恢复脚本 | `scripts/run_exp16_gpu0_recovery.sh` — 仅跑 MLM 3 seeds（42→123→456），每个 seed 跑 Stage 1 DAPT + Stage 2 GRU classifier，设置了 `TRANSFORMERS_OFFLINE=1` + `CUDA_VISIBLE_DEVICES=0` |
| tmux session | `exp16_gpu0_recovery` 运行中 |
| GPU 0 | 82% utilization, 20.6GB/97.9GB 已占用，MLM seed 42 Stage 1 正在训练 |
| 预估总时长 | ~3.75 小时（3 seeds × ~75min） |
| 日志 | `logs/exp16_gpu0_recovery.log` |

---
