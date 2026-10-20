# experiment qwen14b pw oracle rerun

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_qwen14b-pw-oracle-rerun_20260521T103658_result.json`
- **Structured JSON:** [`a0f8bd1dfe9d7cb7aa02.json`](../../sessions/a0/a0f8bd1dfe9d7cb7aa02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| Metric | exp-022 (旧 traces) | exp032 (canonical) |
|--------|---------------------|-------------------|
| **Oracle-SICA** | 86.67% (520/600) | **91.17% (547/600)** |
| SC | — | 73.50% (441/600) |
| SICA(self) | — | 71.50% (429/600) |
| Delta (Oracle vs SC) | — | +17.67 pp |
| Z3-gold match rate | — | 97.14% (577/594) |
| Parse errors | — | 6/600 |

Per-subtype Oracle:
- AttNoneg: 98.7% | AttNeg: 91.9% | RelNoneg: 84.2% | RelNeg: 89.3%

Oracle 从 86.67% 升至 91.17%（+4.5pp），表明 exp032 canonical traces 质量更高。完整结果在服务器 `/root/symb_invariant_consensus/results/exp032_qwen14b_pw_oracle/results.json`，artifact 已注册。

---
