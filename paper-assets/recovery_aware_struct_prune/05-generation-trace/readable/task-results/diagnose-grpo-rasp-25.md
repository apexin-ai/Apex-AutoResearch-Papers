# diagnose grpo rasp 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_rasp_25_20260516T170358_result.json`
- **Structured JSON:** [`cacafa0d5f6c6799d122.json`](../../sessions/ca/cacafa0d5f6c6799d122.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

**grpo_rasp_25 没有失败，是 Cron 误判。** 实验 100/100 步正常完成（57 分钟），模型和 checkpoint 均完整保存。Cron 在进程正常退出后 ~7 分钟轮询时发现无存活进程，错误标记为 failed。

已完成的修复：
- Registry `conclusion` 已从 `failed` 改为 `success`
- `failure_reason` 已更新为 FALSE POSITIVE 说明
- `wandb_run_id` 已补充 (`bc4ojqie`)
- 诊断报告已注册为 artifact (`art_20260516_baffc3`)

值得注意：step 100 的 `frac_reward_zero_std=0.875`、`reward=0.009` 表明虽然训练跑完了，但模型出现了严重的 reward collapse——这与 RASP 25% 的研究假设一致，后续需定量分析。

---
