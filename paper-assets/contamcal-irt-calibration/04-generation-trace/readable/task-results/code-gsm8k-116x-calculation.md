# code gsm8k 116x calculation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k-116x-calculation_20260520T005202_result.json`
- **Structured JSON:** [`c57b12ad6ce3e29934c2.json`](../../sessions/c5/c57b12ad6ce3e29934c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**cqa1 s123 GSM8K eval 脚本跑的剂量：`d000` 和 `d100`（仅 2 点）。** 循环为 `for DOSAGE in 000 100`，不包含 d005/d025/d050。

分析文件已创建并注册（`art_20260520_2a45c4`），包含：
- 5 点完整数据表（含 Δ 和累积占比）
- 每个剂量点的线性 vs 实际对比（d005=11.5×, d025=3.4×, d050=1.6×）
- 11.6× 计算过程（6.37/0.5535=11.51）
- d050 < d025 非单调性分析（-0.83pp，待多 seed 确认）
- AUGMENT confound 三重排除论证
- OLMo-2 archetype 对比（+1.74pp vs +11.07pp，6.4× 差异）

---
