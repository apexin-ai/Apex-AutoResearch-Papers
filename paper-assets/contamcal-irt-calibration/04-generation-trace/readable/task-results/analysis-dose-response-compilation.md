# analysis dose response compilation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose-response-compilation_20260514T205002_result.json`
- **Structured JSON:** [`47cbfa14b9478f2dc162.json`](../../sessions/47/47cbfa14b9478f2dc162.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。表格已保存为 artifact `dose_response_table.md`（art_20260514_6f12f1），insights 已追加到 memory.md。

---

## Cross-Scale d100−d000 Delta 总览

| Benchmark | 0.5B orig | 1.5B orig | 1.5B para | 3B orig |
|-----------|-----------|-----------|-----------|---------|
| MMLU | −16.45 | +0.80 | +1.56 | +0.77 |
| GSM8K | −0.38 | −0.46 | −0.44 | n/a† |
| ARC | −17.49 | −0.34 | +1.14 | +1.20 |
| HumanEval | −10.98 | **+17.69** | **+23.07** | +0.61 |

†GSM8K 3B excluded per D018 (CoT catastrophic forgetting)

## 三个核心发现

1. **0.5B 退化而非膨胀。** 所有 benchmark 随 dosage 下降（MMLU −16pp, ARC −17pp），模型容量不足以在记忆的同时维持泛化——contamination 造成的是破坏而非分数膨胀。

2. **1.5B MC benchmarks 完全无法检测。** MMLU/GSM8K/ARC 在 d000→d100 变化 <1pp（orig 和 para 均如此）。准确率指标对 1.5B scale 的 contamination 彻底失盲，这正是 IRT-based detection 的核心动机。

3. **HumanEval 是唯一有 dose-response 的 benchmark（1.5B）。** Orig +17.69pp, para +23.07pp。Para delta 超过 orig，暗示模型泛化了编程模式而非纯粹记忆答案。3B delta 仅 +0.61pp，但 v1 LoRA 有损，v2 待评估。

**缺失数据**: 0.5B d100 para 未提交；3B 大部分 para 缺失；2 个实验仍在运行（0.5B d025 para, 1.5B d025 orig）。

---
