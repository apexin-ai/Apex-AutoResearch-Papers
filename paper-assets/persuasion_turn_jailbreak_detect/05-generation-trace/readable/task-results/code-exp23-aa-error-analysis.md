# code exp23 aa error analysis

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp23-aa-error-analysis_20260520T141908_result.json`
- **Structured JSON:** [`b8eeb8808552cc1ca435.json`](../../sessions/b8/b8eeb8808552cc1ca435.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出：`results/exp23_aa_error_analysis.json` + `scripts/exp23_aa_error_analysis.py`

## 结果摘要

**整体表现极强，错误稀疏且不一致：**

| Metric | Value |
|--------|-------|
| Majority vote accuracy | 98.3% |
| Majority vote FN / FP | 2 / 0 |
| Total error samples (any seed) | 7 / 118 |
| Consistent errors (all 3 seeds) | **0** |

**FN/FP 比例**：所有错误均为 FN（漏检 jailbreak），零 FP。模型从不误判 benign。

**Seed 差异**：seed 123 明显弱于其他两个（7 FN vs 各 1 FN），是主要噪声源。

**Error pattern：**
- **Turn 数**：错误集中在短对话（3-6 turns），7-8 turn 无错误。错误样本平均 10,480 chars vs 正确样本 12,788 chars——短对话更难检测。
- **Topic**：data privacy (2/8)、digital privacy (2/8)、identity verification (2/8)、social engineering (1/8)，其余 6 topic 零错误。
- **k-turn 诊断**：最难的两个样本（idx=20, idx=33）在所有 k-turn 截断下都几乎无法检测（0-1/3 votes）；其余 5 个样本在 k3/k5 时大多已能正确检测（2/3 votes），说明问题出在 seed 123 的模型不稳定性而非系统性盲区。
- **Cross-variant**：vanilla 模型对这 7 个样本全部检测失败（0/3 votes），9-class 在 5/7 样本上仍有 2/3 majority 正确——DAPT 的优势明显。

---
