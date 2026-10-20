# ops westd urgent fix and harvest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_urgent_fix_and_harvest_20260518T181340_result.json`
- **Structured JSON:** [`602d9ebe97c540e05cd3.json`](../../sessions/60/602d9ebe97c540e05cd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 任务 1：cuda:2 SFT CKA-only MATH-500 重启

- cuda:2 原本无残留进程（0MiB），直接可用
- **已启动** eval_math500_sft_cka_only_20_v4_restart，PID 21013，tmux session `sft_cka_eval_v4`
- Registry: 旧条目 `eval_math500_sft_cka_only_20_v4` 标记 DONE/failed，新条目 `eval_math500_sft_cka_only_20_v4_restart` 状态 RUNNING

## 任务 2：Dense MATH-500 收割 + RASP GRPO 启动

- **Dense 结果**: accuracy=**0.736** (368/500), stderr=0.0197, natural_eos_pct=75.2%
- 日志确认 500/500 完成（02:09:52 写入结果）
- Registry `eval_math500_dense_unpruned` 已更新为 DONE/success
- cuda:3 空闲，RASP checkpoint 找到：`/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair/`
- **已启动** RASP GRPO MATH-500 eval，PID 21100，tmux session `rasp_grpo_eval`
- Registry `eval_math500_grpo_rasp_20_fair` 状态 RUNNING

## 任务 3：E2 CKA-only Extended reward=1.00 验证

**结论：reward=1.00 是误报，不是真实值。**

训练仍在运行（193/300, 64%）。从日志中提取的 reward 趋势（每 10 步汇报一次 `rewards/reward_fn/mean`）：

| Step | reward_mean |
|------|-------------|
| 110  | 0.3206 |
| 120  | 0.2562 |
| 130  | (截断) |
| 170  | 0.2669 |
| 180  | 0.3406 |
| 190  | 0.2338 |

- Step 181 没有单独的日志行（每 10 步汇报一次）
- **step 180 的 batch mean reward 只有 0.3406，step 190 回落到 0.2338**
- 表格中显示的个别 sample reward 是 0.00 和 -0.50
- reward 在 0.23~0.34 区间波动，无任何"顿悟"迹象
- 之前看到的 reward=1.00 极大可能是某个**单条 sample 的 reward**（表格中某行），而非 batch 均值

---

**当前 GPU 分配 (westd-29022):**
- cuda:0: E2 CKA-only Extended GRPO (193/300, running)
- cuda:1: Standard GRPO fair MATH-500 eval (running)
- cuda:2: SFT CKA-only MATH-500 eval (刚启动)
- cuda:3: RASP GRPO fair MATH-500 eval (刚启动)

---
