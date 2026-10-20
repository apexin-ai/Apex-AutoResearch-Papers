# run c1 format regen

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_c1_format_regen_20260517T072625_result.json`
- **Structured JSON:** [`a90adbad52004bb39ec5.json`](../../sessions/a9/a90adbad52004bb39ec5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常：
- Gen 0 的 checkpoint 已恢复（跳过了重新生成）
- 正在 GPU 0 上进行 ArmoRM scoring
- 输出目录正确指向 `outputs_lora_k4_curated/`
- seed=42, K=4, 2000 prompts, 3 generations

**提交结果：**
- PID: 552767
- tmux session: `c1-regen-lora-k4-curated`
- 日志: `~/runs/collapse_aware_reward_rebalancing/c1-regen-lora-k4-curated.log`
- 预计完成时间: 约 3-4 小时（gen_0 跳过生成步，gen_1/gen_2 各约 1-1.5h）
- Watcher 已由 submit_training_job 自动设置（tmux session 有 timeout_hours=8 的自动监控）

---
