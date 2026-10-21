# code mvp a oracle sim

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-a-oracle-sim_20260511T182340_result.json`
- **Structured JSON:** [`1a5f1c1fa85fedcd5347.json`](../../sessions/1a/1a5f1c1fa85fedcd5347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MVP-A Oracle 模拟完成。

**结果：PASS**

| 指标 | Block-correlated | I.I.D. |
|------|-----------------|--------|
| 70-85% mean advantage | **36.2%** | 18.5% |
| min advantage | 33.5% | 14.0% |
| max advantage | 37.5% | 21.4% |
| Pass (≥5%) | **YES** | YES |

产出文件（服务器 `home-1x5090:/home/sonny/exec-sim-repair-verifier/`）：
- `mvp_a_oracle_sim.py` — 模拟脚本
- `mvp_a_results.json` — 完整结果数据
- `mvp_a_curves.pdf` — 可视化（resolve rate 曲线 + advantage 曲线）

Registry 已更新为 DONE/success，metrics 和 notes 已写入。

---
