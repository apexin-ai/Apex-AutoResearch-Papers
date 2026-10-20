# analysis exp 001 supplement ef

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_supplement_ef_20260515T060922_result.json`
- **Structured JSON:** [`78d13dc34618c454fb48.json`](../../sessions/78/78d13dc34618c454fb48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## (e) Phi Coefficient — FOL/Code 失败相关性

| Subset | N | Both✓ | FOL✓ | Code✓ | Both✗ | φ | χ² | p |
|--------|---|-------|------|-------|-------|---|---|---|
| **all** | 204 | 104 | 57 | 18 | 25 | **0.189** | 7.30 | **0.007** |
| GT=True | 72 | 46 | 12 | 8 | 6 | 0.203 | 2.96 | 0.086 |
| GT=False | 63 | 27 | 19 | 5 | 12 | **0.260** | 4.26 | **0.039** |
| GT=Unknown | 69 | 31 | 26 | 5 | 7 | 0.097 | 0.64 | 0.423 |

**解读**：整体 φ=0.189（弱相关，p=0.007 显著）。100 个错误样本中 **75 个（75%）是互补性失败**（仅一方出错），支持双表征互补性。GT=Unknown 子集 φ 最低（0.097，不显著），说明对 Unknown 类型两种表征的失败模式最独立。GT=False 子集 φ 最高（0.260），共同失败风险相对较大。

## (f) Cost-Effectiveness

| 指标 | 值 |
|------|-----|
| 单表征 tokens/样本（est.） | 3,016 |
| 双表征 base tokens/样本 | 6,032 (2.0x) |
| Repair 额外 tokens/repair样本 | 26,895 |
| **全 pipeline vs 单表征** | **5.76x** |
| Code-only 准确率 | 59.8% |
| FOL-only 准确率 | 78.9% |
| Oracle 上界 | 87.8% |
| Pipeline (repair) | 79.9% |
| Pipeline (repair+FOL fallback) | **81.4%** |
| **准确率增益 vs Code baseline** | **+21.6%** |
| 每单位额外成本的增益 | 0.045 |

**解读**：5.76x 成本换取 +21.6% 绝对准确率增益（59.8%→81.4%）。主要成本来自 repair 阶段（86/204 样本触发 repair，每个 repair 样本消耗约 26.9K 额外 tokens）。pipeline 准确率已接近 FOL-only 而非远超它，说明 repair 成功率（59/86=68.6%）是瓶颈——提升 repair 成功率可在不增加太多成本的前提下接近 oracle 上界（87.8%）。

---

脚本：`src/analysis_supplement_ef.py`
输出：`results/exp001_supplement_ef.json` + `results/exp001_supplement_ef.txt`

---
