# diagnose eval gsm8k grpo alpha4 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_grpo_alpha4_20_20260521T213035_result.json`
- **Structured JSON:** [`1dadad25788319aba449.json`](../../sessions/1d/1dadad25788319aba449.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论**：774/1319 (58.7%) 完成后 timeout (EXIT_CODE=124)。

**根因**：周期性生成卡顿。正常 ~2-3s/sample，但 ~1.73% 的 samples 无 EOS token，导致单 sample 生成耗时 5-6 分钟（sample 714 和 756 各卡 ~350s）。这些 stall 把平均速度从 ~2.5s 拉到 ~9s/sample，2h timeout 不够跑完。

**可抢救数据**：无 results.json（脚本只在全部完成后写文件）。但 log 中 750/1319 处 acc=**0.6293** (62.93%)，accuracy 趋势稳定，最终值预计 ~62-63%。

**重跑方案**：
- 加 `--max_new_tokens 2048` 防止单 sample 卡顿（与 MATH-500 _v2 修复一致）
- timeout_hours 设 3h（加了 max_new_tokens 后预计 ~1.5h 完成）
- 加 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`

---
