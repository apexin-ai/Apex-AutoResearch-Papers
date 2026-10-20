# run fullft lr2e5 probe

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_fullft_lr2e5_probe_20260516T204005_result.json`
- **Structured JSON:** [`4dd5130a1e0f588c1ff2.json`](../../sessions/4d/4dd5130a1e0f588c1ff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认启动正常：

- **cuda:1** 已占用 ~21GB 显存（模型已加载，正在生成/评估）
- 日志显示 dataset 从离线缓存加载成功
- PID 523811 运行中

**配置总结**：
- `LR = 2e-5` (4x from 5e-6)
- `EPOCHS = 3` (from 2)
- `USE_LORA = False`, `BATCH_SIZE=1`, `GRAD_ACCUM=8`
- `K=4`, `NUM_PROMPTS=2000`, `3 generations`
- 输出目录: `outputs_fullft_lr2e5/`
- 实验 ID: `carr_fullft_lr2e5_probe_01`
- 日志: `~/runs/collapse_aware_reward_rebalancing/carr_fullft_lr2e5_probe_01.log`

---
