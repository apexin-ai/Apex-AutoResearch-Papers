# analysis evaluate mvp 125 samples

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_evaluate_mvp_125_samples_20260514T175249_result.json`
- **Structured JSON:** [`2da4514e6a85638f2cbd.json`](../../sessions/2d/2da4514e6a85638f2cbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### evaluate_mvp.py 输出

| 指标 | All-mode (N=117) | Excl-Unknown (N=75) |
|------|-----------------|-------------------|
| C1 disagree_rate | 35.9% (42/117) **PASS** | 34.7% (26/75) **PASS** |
| C2 diagnostic_rate | 88.1% (37/42) **PASS** | 88.5% (23/26) **PASS** |
| C3 error_types | 3 types **PASS** | 2 types **PASS** |
| C4 targeted_vs_blind | +7.4pp (T:35/54 B:31/54) **PASS** | +0.0pp (T:22/35 B:22/35) **FAIL** |
| C5 localization | 79.2% (19/24) **PASS** | 87.5% (14/16) **PASS** |

**MVP: 5/5 PASS → PROCEED**（基于 all-mode）

### C4 根因分析

**分界线不是 GT 类型，而是 error_side：**

| error_side | targeted | blind | delta |
|------------|----------|-------|-------|
| **code** (N=35) | 82.9% | 62.9% | **+20.0pp** |
| **fol** (N=10) | 50.0% | 90.0% | **-40.0pp** |
| both (N=14) | 20.0% | 10.0% | +10.0pp |

- **code-side 错误**：targeted 在所有 GT 类型上一致优于 blind
- **fol-side 错误**：targeted 严重劣于 blind（50% vs 90%），这是拖累 excl-unknown delta 的直接原因
- GT=Unknown 之所以 delta 大（+20pp），是因为 code:fol 比例为 14:2；GT=True 的 code:fol 为 8:6，fol 拖累使 delta 变负（-6.2pp）

**结论**：C4 excl-unknown FAIL 的根因是 **FOL-side targeted repair 策略失效**（成功率仅 50%，远低于 blind 的 90%）。修复方向：改进 FOL 错误的 targeted repair prompt/策略。

Registry 和 artifact 已更新。

---
