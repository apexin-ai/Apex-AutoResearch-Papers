# check math500 progress v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_math500_progress_v2_20260518T031350_result.json`
- **Structured JSON:** [`3fc83783267102294eef.json`](../../sessions/3f/3fc83783267102294eef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| exp_id | server:gpu | pid alive | progress | accuracy (if done) | est_completion |
|--------|-----------|-----------|----------|-------------------|----------------|
| eval_math500_grpo_standard_20 | westd:cuda1 | Yes (17h48m) | **unknown** (no log file, stdout→pipe) | — | unknown* |
| eval_math500_grpo_rasp_20_v3 | westd:cuda3 | Yes (12h28m) | **371/500** (74%) | 0.2486 @350 | ~4h (~15:15 UTC) |
| eval_math500_grpo_unpruned | westd:cuda2 | Yes (4h05m) | **251/500** (50%) | 0.7040 @250 | ~4h (~15:15 UTC) |
| eval_math500_sft_cka_only_20_v2 | westd:cuda0 | Yes (34min) | **17/500** (3.4%) | — | ~15h (~02:00 UTC May 19) |
| eval_math500_grpo_cka_only_20 | westb:cuda1 | Yes (33min) | **10/500** (2%) | — | ~20-24h (very early, pace uncertain) |

**关键发现：**

1. **grpo_standard_20** — 进程活了 17h48m 但无可访问的日志（stdout 输出到 pipe，可能在 tmux 里）。按 rasp 的速度推算它应该早完成了，但结果文件不存在，进程仍在运行（状态 Rl）。**建议 attach tmux 查看实际进度，可能有问题。**

2. **grpo_rasp_20_v3** — acc@350 = **24.86%**，异常偏低。正常运行中，还剩约 129 个样本。

3. **grpo_unpruned** — acc@250 = **70.40%**，进度正常。

4. **sft_cka_only_20_v2** 和 **grpo_cka_only_20** — 刚启动约 30 分钟，进度极早期，预计 15-24 小时完成。

---
