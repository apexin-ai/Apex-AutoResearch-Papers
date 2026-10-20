# eval exp 001 eval 3B d000 s42 a32

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp_001_eval_3B_d000_s42_a32_20260516T003804_result.json`
- **Structured JSON:** [`35206504ee7035c561ae.json`](../../sessions/35/35206504ee7035c561ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:4 被占用，无法提交 eval。** PID 662616 是一个 compute_signals 进程（d100_a32_s123 mmlu），已运行 23 分钟，在 cuda:4 上。

---

### 汇报

**1. v8 signals 完成情况**

**d025_s123:**

| Benchmark | s1_embedding | s2_minkpp | s4_selfcritique | signals_merged |
|-----------|:---:|:---:|:---:|:---:|
| mmlu | ✓ | ✓ | ✗ | ✗ |
| gsm8k | ✓ | ✓ | ✓ | ✓ |
| arc_challenge | ✓ | ✓ | ✓ | ✓ |

**d100_a32_s123:**

| Benchmark | s1_embedding | s2_minkpp | s4_selfcritique | signals_merged |
|-----------|:---:|:---:|:---:|:---:|
| mmlu | ✓ | ✓ | ✗ (v8 死在 6%) | ✗ |
| gsm8k | ✗ | ✗ | ✗ | ✗ |
| arc_challenge | ✗ | ✗ | ✗ | ✗ |

**2. v8 缺失项**
- d025_s123: 缺 mmlu 的 s4_selfcritique + signals_merged
- d100_a32_s123: 缺 mmlu 的 s4+merged，gsm8k 和 arc_challenge 全部缺失

**3. d000_s42 eval 未提交**
- 原因：cuda:4 当前被 PID 662616 占用（compute_signals d100_a32_s123 mmlu，已运行 ~24min）
- Checkpoint alpha=32 已确认，等 cuda:4 空闲后可立即提交

需要等 PID 662616 完成（或决定是否 kill 它）后再提交 eval。

---
