# ops d025 completion d100 gsm8k

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d025_completion_d100_gsm8k_20260516T232944_result.json`
- **Structured JSON:** [`3706f6be07598061b70b.json`](../../sessions/37/3706f6be07598061b70b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个任务都无法按原计划提交：**

**Task A (d025 → cuda:2)**：cuda:2 已被 PID 888570 占用，正在跑 `d025 MMLU s4`（正好是任务 A 的一部分）。按 C001 不能重复提交。

**Task B (d100 GSM8K → cuda:0)**：d100 GSM8K 信号已完整存在：
- `signal_s4_selfcritique_gsm8k.json` — 1319 items (完整)
- `signals_merged_gsm8k.json` — 1319 items (完整)
- s1、s2 也都在

无需重复计算。

**另外注意**：`--benchmark` 参数只接受单个值（不能 `--benchmark mmlu gsm8k`），需要分开跑。

---

**建议替代方案**：cuda:0 空闲，可以先提交 d025 GSM8K（s4 全部 + merge）到 cuda:0，与 cuda:2 上正在跑的 d025 MMLU s4 并行。等 MMLU s4 完成后再跑 MMLU merge。

需要我提交 d025 GSM8K 到 cuda:0 吗？

---
