# code ot7b layer16 verification

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ot7b_layer16_verification_20260517T084857_result.json`
- **Structured JSON:** [`809d5063af78b6fbc2b8.json`](../../sessions/80/809d5063af78b6fbc2b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果摘要：

**Layer 16 (W=3) 全面优于 Layer 0 (W=3)**：

| 指标 | Layer 0 | Layer 16 | 改善 |
|------|---------|----------|------|
| bal_acc | 0.672 | **0.688** | +1.6 pp |
| precision | 0.357 | **0.466** | +10.9 pp |
| pre_cp_fpr | 0.188 | **0.100** | -8.8 pp |
| Bonferroni pass | 2/3 | **3/3** | +1 |

Layer 16 bootstrap 三个指标全部 p=0.000，均通过 Bonferroni 校正（Layer 0 的 precision p=0.056 未通过）。

报告已保存至 `artifacts/ot7b_layer16_verification/report.md`，建议论文中 OT-7B 全部替换为 Layer 16 结果。

---
