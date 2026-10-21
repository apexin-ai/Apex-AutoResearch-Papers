# exp pilot final read

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pilot_final_read_20260520T235925_result.json`
- **Structured JSON:** [`2c18bb29f40bc4b3124c.json`](../../sessions/2c/2c18bb29f40bc4b3124c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pilot 推理全部完成。** 汇总：

| 指标 | 值 |
|------|-----|
| 总记录数 | 20,000 |
| Overall accuracy | 61.6% |
| 字段完整性 | All 15 present |
| 磁盘占用 | 13MB |

**Per-GPU:**
- gpu0: 5000 records, acc=60.5%, avg_lat=174.4ms
- gpu1: 5000 records, acc=62.2%, avg_lat=184.7ms
- gpu2: 5000 records, acc=62.7%, avg_lat=183.1ms
- gpu3: 5000 records, acc=61.0%, avg_lat=181.5ms

**条件覆盖:**
- Precision: float32 only — 100 conditions（20,000 / 200 items）
- Temperature: T=0.0 only — 100 conditions

注意：当前 pilot 只跑了 **float32 + T=0.0** 这一个精度×温度组合。如果设计上 pilot 只测这个组合的 100 个 seed/prompt/ordering 条件，这是符合预期的。如果原计划包含多精度/多温度，需要检查配置。

---
