# ops eval 3B d000 v2 para check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-3B-d000-v2-para-check_20260515T011404_result.json`
- **Structured JSON:** [`ddea99b689835a7d7b20.json`](../../sessions/dd/ddea99b689835a7d7b20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中已被清除或过期）。

**总结：**

`exp_001_eval_3B_d000_v2_para_aligned_v2` 已完成，结果成功。

- **输出目录**: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2/`
- **文件**: eval_results.json (900KB), item_responses.json (1MB), correctness_matrix.json (48KB)
- **Metrics**:
  - mmlu_para: 0.6468 (4266/6596)
  - gsm8k_para: 0.2895 (66/228)
  - arc_challenge_para: 0.8121 (566/697)
  - humaneval_para: 0.0385 pass@1 (1/26)
- **Registry**: status=DONE, conclusion=success, metrics 已记录

注：该实验之前被 cron 误标为 failed（"Process and tmux session died silently"），实际进程在之后完成并输出了完整结果。

---
