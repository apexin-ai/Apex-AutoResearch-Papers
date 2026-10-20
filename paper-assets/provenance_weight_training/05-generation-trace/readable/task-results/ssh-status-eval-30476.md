# ssh status eval 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status_eval_30476_20260517T205249_result.json`
- **Structured JSON:** [`dd75e39d80ee5ed69581.json`](../../sessions/dd/dd75e39d80ee5ed69581.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 4 个实验仍在运行，尚未完成。无法执行 eval。**

当前进度（max_steps=6103）：

| exp_id | PID | GPU | step/total | 进度 |
|--------|-----|-----|-----------|------|
| grid_b0_1_seed42 | 34716 | cuda:0 | 1500/6103 | ~25% |
| grid_b0_3_seed123 | 42432 | cuda:1 | 1000/6103 | ~16% |
| rho02_adaptive_tau08_seed42 | 41387 | cuda:2 | 3500/6103 | ~57% |
| batchsize16_nmin8_r2 | 48891 | cuda:3 | 1500/6103 | ~25% |

注意事项：
- 用户提到的名称 "grid_b0_3_seed123_r2" 实际输出目录为 `grid_b0_3_seed123`
- 用户提到的 "batchsize16_nmin8_r3" 实际为 `batchsize16_nmin8_r2`（输出到 `/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2`）

按当前速率估算（实验从约 01:20-03:32 启动，现在 04:53）：
- **rho02_adaptive_tau08_seed42** 可能最先完成（约再需 2.5 小时）
- 其余三个约需 5-8 小时

需要我设定定时检查、等完成后自动跑 eval 吗？

---
