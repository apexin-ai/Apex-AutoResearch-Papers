# code plan 018 threshold sensitivity

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_018_threshold_sensitivity_20260521T031126_result.json`
- **Structured JSON:** [`29565c08cc144d938dfc.json`](../../sessions/29/29565c08cc144d938dfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Overall temporal DIF (12,508 items):**

| Threshold | C% (uncorrected) | C% (BH-corrected) |
|-----------|-------------------|--------------------|
| 1.0 | 48.93% | 48.16% |
| 1.5 | 31.32% | 31.30% |
| 2.0 | 18.34% | 18.34% |
| 2.5 | 10.22% | 10.22% |

**关键发现：**
- BH 校正影响极小（56.9% 的 tests 在 BH 下仍显著），因为大 DIF items 的 p-value 本身就很小
- ">15% large DIF" 结论在 threshold ≤ 2.0 下稳健成立；即使在极严格的 2.5 阈值下仍有 10.2% flagged
- Within-family DIF 更高（threshold=1.5 时 50.1% uncorrected / 45.1% BH-corrected）
- 审稿人关于阈值校准的质疑可回应：结论不依赖于 1.5 的具体选择

产出已注册：报告 `art_20260521_1ac690`，脚本 `art_20260521_00bec4`。

---
