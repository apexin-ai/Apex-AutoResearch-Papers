# fix batch64 num workers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_batch64_num_workers_20260517T080846_result.json`
- **Structured JSON:** [`44c3df7b88307b4b0c67.json`](../../sessions/44/44c3df7b88307b4b0c67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行。总结：

**num_workers=2 训练已成功启动在 cqa1-33015 GPU 1 上。**

速度对比：
| 指标 | num_workers=1 | num_workers=2 | 提升 |
|------|-------------|-------------|------|
| step 0→50 | 738s | 342s | **2.16x** |
| step 50→100 | 729s | 339s | **2.15x** |
| 实际 sps | ~0.068 | ~0.147 | **2.16x** |
| 预计 ETA | 11.6 天 | **~5.4 天** | |

关键数据：
- step 0 (16:18:21) → step 50 (16:24:03) → step 100 (16:29:42)
- GPU 内存：2727 MiB（稳定，未增长）
- 系统内存：953.7GB available（充裕）
- loss 正常下降：1.5052 → 1.3758 → 0.6564
- 显示 sps=0.1 是因为 `%.1f` 格式精度不够，实际 sps ≈ 0.15

注意事项：
- 从 step 0 重新开始（之前 step 267 的 checkpoint 损坏）
- 需要设置 `HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline`
- OOM 风险需持续关注（之前 num_workers=4 在 step 3550 OOM），但目前 GPU 内存稳定

---
