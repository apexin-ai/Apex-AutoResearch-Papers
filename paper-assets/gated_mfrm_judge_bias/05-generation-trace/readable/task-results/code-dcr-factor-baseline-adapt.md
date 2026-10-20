# code dcr factor baseline adapt

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcr_factor_baseline_adapt_20260522T075456_result.json`
- **Structured JSON:** [`8c55ec9b960754e23e28.json`](../../sessions/8c/8c55ec9b960754e23e28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

11/11 测试全部通过。以下是完整产出：

---

## 1. DCR Factor 核心逻辑总结

**4 层污染分数含义：**
| 层级 | 名称 | 含义 | 我们的映射 (dcr_baseline.py) |
|------|------|------|--------------------------|
| s1 | Semantic | 语义级污染（模型接触过语义等价内容） | Score Elevation: 模型均分偏离群体均分的程度 |
| s2 | Information | 信息级污染（接触过 benchmark 元数据） | Easy-Item Advantage: 模型分数与 item 难度的相关性 |
| s3 | Data | 数据级污染（接触过测试数据本身） | Perfect-Score Rate: 满分条目比例 |
| s4 | Label | 标签级污染（接触过带标签的测试数据） | Judge Unanimity: 全部 judge 给出高分的 item 比例 |

**计算方式：** 4 个 [0,1] 分数输入模糊推理系统 → 5 条规则（Negligible/Minor/Moderate/Significant/Severe）→ 质心去模糊化 → DCR Factor ∈ [0,1]。调整后分数 = raw_accuracy × (1 - DCR)。

## 2. 适配层代码路径 + 验证

- **适配层:** `/root/gated_mfrm_judge_bias/baselines/dcr_adapter.py` — 语法验证 OK，dry-run + 全流程均通过
- **已有 DCR baseline:** `/root/gated_mfrm_judge_bias/baselines/dcr_baseline.py` — 11/11 测试通过
- **核心函数:** `pairwise_to_tensor()` 完成 pairwise JSONL → (N,I,J) tensor 转换，`run_dcr_on_exp001()` 端到端运行

## 3. 数据映射可行性评估

**可直接映射：**
- s1 (Score Elevation) ✅ — 从 tensor 的模型均分偏离直接计算
- s2 (Easy-Item Advantage) ✅ — item 难度 = 跨模型均分，与模型分数求相关即可
- s3 (Perfect-Score Rate) ✅ — pairwise win rate = 1.0 即为满分

**部分受限：**
- s4 (Judge Unanimity) ⚠️ — 当前 coverage 22%，多数 item 只有 1-3 个 judge 有评分，"全部 judge 一致给高分"的统计量不可靠。当数据收集完成后此问题消失。

**当前数据实况：** N=2, I=216, J=9, coverage=22%。DCR 和其他 baseline 可正常运行但结果仅供参考，需等 exp-001 数据收集完成后重跑。

## 4. DCR Factor 已观测到的高 s2 问题

两个模型的 s2（Information level）都在 0.69-0.77，导致 DCR Factor 偏高（0.50-0.62）。这是因为 pairwise win rate 天然与 item 难度强相关（弱模型在难题上 win rate 低、简单题上也低，但相关性结构与 pointwise accuracy 不同）。**这是 DCR 的固有局限：它的 4 层分数设计假设 pointwise accuracy 数据，直接用于 pairwise 数据时 s2 信号被放大。** 这恰好可以作为论文中论证 "contamination-only correction 在 judge bias 场景下不够" 的证据。

## 5. exp-004 集成建议

`dcr_adapter.py` 的 `run_all_baselines_on_exp001()` 已提供统一接口，所有 baseline 共享同一个 tensor。exp-004 只需：

```python
from baselines.dcr_adapter import run_all_baselines_on_exp001
results = run_all_baselines_on_exp001()
# results["baselines"]["dcr"]["theta_hat"]      → DCR 调整后 ability
# results["baselines"]["cyclic_judge"]["theta_hat"] → CyclicJudge baseline
# results["baselines"]["pref_leakage"]["theta_hat"] → PLS baseline
```

---
