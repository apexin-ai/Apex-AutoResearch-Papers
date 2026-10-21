# ssh fix experiments tex data

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-experiments-tex-data_20260512T224037_result.json`
- **Structured JSON:** [`f1275e79df146c8ccb66.json`](../../sessions/f1/f1275e79df146c8ccb66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已确认。以下是汇报：

---

## 任务 1: all_correct_observed

- **真实值：46**（114 个 problem 中 46 个全对）
- **百分比：40.35%**（46/114）
- 来源：`/home/sonny/exec-sim-repair-verifier/block_corr_results.json`，由 `block_correlation_analysis.py` 产出
- 独立验证：grep 逐行计数 `"all_correct": true` = 46，`"all_correct": false` = 68，合计 114 ✓
- **论文需要修改：是**
  - 48 → **46**
  - 42.1% → **40.4%**（取 40.35% 一位小数四舍五入）
- 无法纯分析重跑（`block_correlation_analysis.py` 需要加载模型做推理），但 JSON 结果和 summary 一致，数据可信

## 任务 2: error complementarity

数据来源：`/home/sonny/exec-sim-repair-verifier/matched_seed_overlap_results.json`，由 `matched_seed_analysis.py` 产出。同时被 `analyze_error_overlap.py` → `error_overlap_analysis.json` 交叉验证（overlap 计数完全一致）。

**CLS 漏检率：**
- CLS-only errors（CLS 错、CWM 对）= 53 例
- 其中 true label = FAIL 的有 40 例（CLS 预测 PASS，实际 FAIL → 漏检）
- 精确值 = 40/53 = **75.47%**
- 论文写 75.5% → **正确**（四舍五入到 1 位小数）

**CWM 误报率：**
- CWM-only errors（CWM 错、CLS 对）= 59 例
- 其中 true label = PASS 的有 49 例（CWM 预测 FAIL，实际 PASS → 误报）
- 精确值 = 49/59 = **83.05%**
- 论文写 83.1% → **正确**（四舍五入到 1 位小数）

**Oracle accuracy：**
- Oracle correct（CLS 对 ∪ CWM 对）= 1713/1890
- 精确值 = **90.63%**
- 论文写 90.63% → **完全匹配**

**计算逻辑：**
- CLS 漏检率 = FN_unique / (FN_unique + FP_unique)，即 CLS 独有错误中"漏掉 FAIL"的比例
- CWM 误报率 = 同理，CWM 独有错误中"把 PASS 判成 FAIL"的比例
- Oracle = CLS correct ∪ CWM correct（任一模型判对即算对）

**分析脚本路径：**
- `/home/sonny/exec-sim-repair-verifier/matched_seed_analysis.py`（主脚本）
- `/home/sonny/exec-sim-repair-verifier/analyze_error_overlap.py`（交叉验证）

**数据差异：无**（三个数值均与论文一致）

---

**总结：论文唯一需要修正的是 §5.6(b) 的 all_correct 数据：48→46，42.1%→40.4%。§5.6(a) 的三个数值均正确。**

---
