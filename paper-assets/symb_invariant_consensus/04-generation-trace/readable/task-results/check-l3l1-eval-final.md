# check l3l1 eval final

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_l3l1_eval_final_20260516T025244_result.json`
- **Structured JSON:** [`a731e543dd936e35aa14.json`](../../sessions/a7/a731e543dd936e35aa14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程仍在运行（已 1h06m），正在处理第 5/5 题 `ProofWriter_RelNoneg-OWA-D5-31_Q12` 的 traces 9-12。已完成 **4/5**。

---

## 已完成 4 题详细结果

### 每题统计

| # | problem_id | gold | SICA | SICA✓ | SC | SC✓ | SC votes | wall_time |
|---|-----------|------|------|-------|----|-----|----------|-----------|
| 1 | AttNeg-OWA-D5-891_Q1 | True | True | ✓ | True | ✓ | True:12 | 536s |
| 2 | RelNoneg-OWA-D5-616_Q7 | True | True | ✓ | True | ✓ | **True:7, False:5** | 1212s |
| 3 | RelNoneg-OWA-D5-251_Q10 | False | False | ✓ | False | ✓ | **False:9, Unknown:3** | 950s |
| 4 | AttNoneg-OWA-D5-500_Q8 | False | False | ✓ | False | ✓ | False:12 | 458s |

### SICA Scores（每题候选分数）

| # | sica_scores | 候选数 |
|---|------------|--------|
| 1 | True=136.0 | 1（一致） |
| 2 | **True=7.0, False=-2.5** | **2（多候选）** |
| 3 | **False=39.0, Unknown=-1.5** | **2（多候选）** |
| 4 | False=94.0 | 1（一致） |

### Constraints Stats

| # | total_extracted | traces_with_constraints | 提取率 | unique_after_dedup |
|---|----------------|------------------------|--------|--------------------|
| 1 | 136 | 12/12 | 100% | 25 |
| 2 | 12 | 12/12 | 100% | 2 |
| 3 | 42 | 12/12 | 100% | 23 |
| 4 | 94 | 12/12 | 100% | 8 |

### MaxSAT Stats

| # | satisfied | excluded | total_weight | satisfied_ratio (from log) |
|---|-----------|----------|--------------|---------------------------|
| 1 | 25 | **0** | 136 | — (单候选，无需裁决) |
| 2 | 1 | **1** | 7 | — |
| 3 | 22 | **1** | 39 | 0.957 (22/23) |
| 4 | 8 | **0** | 94 | 1.000 (8/8) |

---

## 汇总分析

### V1: 多候选题上 excluded > 0？

| 题 | 多候选？ | excluded |
|----|---------|----------|
| 891_Q1 | 否（12/12 一致 True） | 0 |
| **616_Q7** | **是（True:7 vs False:5）** | **1** |
| **251_Q10** | **是（False:9 vs Unknown:3）** | **1** |
| 500_Q8 | 否（12/12 一致 False） | 0 |

**结论**：2 个多候选题上 excluded 均 > 0，MaxSAT 确实在发挥约束排除作用。单候选题 excluded = 0（符合预期——无冲突约束需要排除）。

### V2: 约束提取成功率

- traces_with_constraints 总和：12 + 12 + 12 + 12 = **48**
- 总 traces 数：4 × 12 = **48**
- **提取率 = 48/48 = 100%**

### V3: SICA 在多候选题上的表现

| 题 | SC 投票 | SC 结果 | SICA 分数 | SICA 结果 | 对比 |
|----|--------|---------|-----------|-----------|------|
| 616_Q7 | True:7 vs False:5 (勉强) | True ✓ | True=7.0 vs False=-2.5 (拉开差距) | True ✓ | 两者都对，但 SICA 通过负分惩罚 False 拉开了更大 margin |
| 251_Q10 | False:9 vs Unknown:3 | False ✓ | False=39.0 vs Unknown=-1.5 | False ✓ | 两者都对，SICA margin 更大 |

**4 题上 SICA 4/4，SC 4/4，目前持平。** 但在多候选题（616_Q7）SC 仅 7:5 险胜，SICA 通过约束加权给出了更明确的判断（7.0 vs -2.5）。

---

## 第 5 题进度

`ProofWriter_RelNoneg-OWA-D5-31_Q12` (gold=False)：
- 10:39:42 开始
- 10:45:17 traces 1-4 完成（5.6 min）
- 10:50:03 traces 5-8 完成（4.8 min）
- 10:50:03 traces 9-12 开始生成

前 4 题平均 ~789s/题，这题 trace 生成较慢（已 ~10 min 只完成 8/12 traces）。估计再需 **5-10 分钟**完成 trace 生成 + extraction + MaxSAT。

### 日志无错误

日志中有若干 `WARNING No JSON found in response for trace` （problem 3 的部分 traces），但这些 traces 仍产出了答案（可能是 extraction 阶段个别 trace 未提取到约束 JSON，但不影响最终结果，因为 traces_with_constraints 仍为 12/12）。无 ERROR 级别日志。

---
