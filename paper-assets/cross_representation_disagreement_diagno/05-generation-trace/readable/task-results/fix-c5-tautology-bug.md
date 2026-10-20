# fix c5 tautology bug

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c5_tautology_bug_20260515T065117_result.json`
- **Structured JSON:** [`25d438f1f07528bac210.json`](../../sessions/25/25d438f1f07528bac210.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。两处 bug 都已修正（`compute_metrics` 第 95 行 + `bootstrap_ci` 第 178 行）。

### 修复结果

**修改**：`dis.get("error_side")` → `s.get("stability", {}).get("predicted_error_side")`
- `predicted` 现在来自 stability 分析（不依赖 GT）
- `actual` 仍由 GT 派生（作为 ground truth 标签）

### C1-C5 评估结果

| 指标 | All (N=204) | Excl Unknown (N=135) |
|------|-------------|---------------------|
| C1 disagree_rate | 0.4216 (86/204) | 0.3852 (52/135) |
| C2 diagnostic_rate | 0.8721 (75/86) | 0.8462 (44/52) |
| C3 error_types | 4 types | 3 types |
| C4 targeted_delta | +0.0465 | -0.0192 |
| **C5 localization_acc** | **0.5303 (35/66)** | **0.6579 (25/38)** |

**C5 Bootstrap 95% CI**：
- All: 0.5297 [0.4098, 0.6508]
- Excl-Unknown: 0.6572 [0.5000, 0.8056]

C5 从同义反复的 100% 降到合理的 53%/66%，bootstrap CI 也正常了。

---
