# analysis f1 stag conf stratified

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f1-stag-conf-stratified_20260514T191207_result.json`
- **Structured JSON:** [`9f400cb86c59889db222.json`](../../sessions/9f/9f400cb86c59889db222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件已写入服务器并注册 artifact。

**结果摘要：**

### 1. Per-class Breakdown（3 seeds）

| Model | macro_F1 | F1_stag | F1_prog | P_stag | R_stag |
|-------|----------|---------|---------|--------|--------|
| probe_001 (s42) | 0.9055 | 0.8593 | 0.9518 | 0.8969 | 0.8247 |
| probe (s123) | 0.9265 | 0.9022 | 0.9508 | 0.9409 | 0.8666 |
| probe (s456) | 0.9234 | 0.9024 | 0.9444 | 0.8908 | 0.9142 |

woob→p001 test: F1_stag=0.6272 (R_stag=0.48 是瓶颈)。OH 100% FT: F1_stag=0.5439。

### 2. Confidence 分层（probe_001）

| Conf | N | macro_F1 | F1_stag | F1_prog |
|------|---|----------|---------|---------|
| 1 (zero-shot) | 39408 | 0.7327 | 0.6414 | 0.824 |
| 2 (test) | 1780 | 0.9078 | 0.8633 | 0.9522 |
| 3 (test) | 44 | 0.6906 | 0.4444 | 0.9367 |

conf=3 仅 44 windows（4 stag），指标不可靠。conf=1→2 有明显的 F1 阶梯。

### 3. 错误分析

- 131 errors / 1824 test = 7.2% error rate
- **46 FP**（pred stag/actual prog, 35.1%）+ **85 FN**（pred prog/actual stag, 64.9%）
- 错误集中在 conf=2：126/131 errors (96.2%)。conf=3 仅 5 errors（但 error rate 更高 11.4%，受极小样本影响）

---
