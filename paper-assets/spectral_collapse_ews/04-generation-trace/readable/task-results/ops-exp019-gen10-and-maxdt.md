# ops exp019 gen10 and maxdt

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp019-gen10-and-maxdt_20260524T022814_result.json`
- **Structured JSON:** [`4dd5a3f3c6012e9c1672.json`](../../sessions/4d/4dd5a3f3c6012e9c1672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**1. Seed44 SLV 轨迹 (gen_0 → gen_10):**

| Gen | SLV |
|-----|-----|
| 0 | 2366.6829 |
| 1 | 2369.4258 |
| 2 | 2361.1064 |
| 3 | 2365.5503 |
| 4 | 2377.0579 |
| 5 | 2395.6187 |
| 6 | 2411.7842 |
| 7 | 2424.3687 |
| 8 | 2436.0762 |
| 9 | 2451.2527 |
| 10 | 2466.1516 |

**2. 3-seed mean maxΔ_t:**
- Raw: **3.8105**
- Normalized: **0.001610**

**3. 与旧值对比:**
- 旧 2-seed normalized: 0.0017
- 新 3-seed normalized: 0.0016
- 差异: 0.000090（下降约 5.3%）

maxΔ_t 略微下降但量级不变，seed44 加入后信号稳定。

**4. JSON 已保存:** `artifacts/exp_019/full_metrics.json`

---
