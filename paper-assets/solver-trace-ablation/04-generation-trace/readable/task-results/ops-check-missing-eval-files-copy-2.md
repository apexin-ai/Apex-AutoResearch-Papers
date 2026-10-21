# ops check missing eval files

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-missing-eval-files_20260515T151559_result.json`
- **Structured JSON:** [`081b6c01c3c4a57ed804.json`](../../sessions/08/081b6c01c3c4a57ed804.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| # | 目录 | 状态 | eval 文件 |
|---|------|------|-----------|
| 1 | `plan001_exec_only_s42` | **MISSING** | 目录不存在，backup 中也无 |
| 2 | `plan001_exec_only_s43_r4` | **MISSING** | 目录不存在，backup 中也无（训练 log 存在于 `/root/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log`，但 checkpoint 已被清理） |
| 3 | `plan009_sft_baseline_s42_1000` | **EXISTS** | `/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json` (195KB) + `classify_h7_results.json` |
| 4 | `plan009_sft_baseline_s43_1000` | **EXISTS** | `/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json` (192KB) + `classify_h7_results.json` |
| 5 | `plan009_sft_baseline_s44_1000` | **EXISTS** | `/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/eval_sta_results.json` (196KB) + `classify_h7_results.json` |
| 6 | `plan013_random_reward_s42_r4` | **MISSING** | 目录不存在，backup 中也无（训练 log 存在于 `/root/runs/solver-trace-ablation/plan013-random-reward-s42-r4.log`，但 checkpoint 已被清理） |
| 7 | `plan018_additive_random_b01_s42_1000_r3` | **EXISTS** | `/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3/eval_results.json` (207KB) — 注意文件名是 `eval_results.json` 而非 `eval_sta_results.json`，可能需要用 eval_sta.py 重新评估 |

**需补扫的 eval JSON 完整路径（4 个 EXISTS）：**
- `/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json`
- `/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json`
- `/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/eval_sta_results.json`
- `/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3/eval_results.json` (⚠️ 非 eval_sta 格式)

**3 个 MISSING 的 checkpoint 已被清理，需重训才能获得 eval 数据。**

---
