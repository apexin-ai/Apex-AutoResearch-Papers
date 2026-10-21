# cpu e4 comparison table fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_e4_comparison_table_fix_20260521T122306_result.json`
- **Structured JSON:** [`31481c748307aee5693f.json`](../../sessions/31/31481c748307aee5693f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the analysis.

---

## Part 1: Comparison Table 修正

### 数据盘点

**Frontier ensemble (4 families):**
- Oracle gain: +7.86pp ✓ (4-model cross-oracle 0.8361 vs best single oracle 0.7575)
- Greedy-selection gain: +11.89pp (4-model greedy-selection 0.7571 vs best single greedy 0.6382)
- **Cross-model MV gain: 未计算。** E4 分析脚本 (`e4_ensemble_scaling.py`) 只计算了 greedy-selection oracle 和 cross-oracle，没有 pooled-sample MV。

**Fine-tuned ensemble (2 families):**
- MV gain: +0.61pp ✓（报告值，可能是多数据集均值）
- FewNERD 具体值：mixed_uniform (0.7916) − best single greedy (0.7841) = +0.75pp
- **Cross-model oracle gain: 未计算。** B5 脚本只做了 entity construction (MV 变体)，没有计算 best-sample-across-models oracle。

### 结论：两个方案都缺数据点

| 方案 | Fine-tuned 需要 | Frontier 需要 | 可行性 |
|------|----------------|--------------|--------|
| A (统一 oracle gain) | cross-model oracle（B5未算） | 已有 +7.86pp | ❌ 缺 fine-tuned oracle |
| B (统一 MV gain) | 已有 +0.61pp | cross-model MV（E4未算） | ❌ 缺 frontier MV |

**更糟的是：3/4 frontier 原始数据（GPT-5.5, Gemini, DeepSeek）已不在服务器上。** 只有 Claude Sonnet 4 的 `results.jsonl` 存在。无法从原始数据重算缺失指标。

### 可用的近似值

如果接受近似，可以提供：

**方案 A 近似（oracle gain）：**

| Setting | Cross-family r | Oracle gain |
|---------|---------------|-------------|
| Fine-tuned (2 families) | 0.67 | **无法计算**（需要 instance-level cross-model oracle） |
| Frontier (4 families) | 0.50 | +7.86pp |

**方案 B 近似（MV gain）：**

| Setting | Cross-family r | MV gain |
|---------|---------------|---------|
| Fine-tuned (2 families) | 0.67 | +0.61pp（报告值）/ +0.75pp（FewNERD） |
| Frontier (4 families) | 0.50 | **无法精确计算** |

Frontier 可用的 MV 相关代理值：
- 平均 within-model MV gain = (1.39 + 1.45 + 1.58 + 2.51) / 4 = **+1.73pp**，但这是单模型内部 MV gain，不是 cross-model pooled MV
- 4-model greedy-selection gain = +11.89pp，但这是 model-routing oracle，不是 MV

**建议**：如果要修 comparison table，最诚实的做法是统一用一个可比指标。可以考虑：
- 把 metric 改为 greedy-selection oracle gain（fine-tuned 有 B5 的 mixed_uniform vs best greedy 可做近似）
- 或者在 table 注释中明确标注不同 metric，而不是假装它们可比

---

## Part 2: k=1 Greedy-Selection 数值核实

### 脚本逻辑分析

`e4_ensemble_scaling.py` 第 163-193 行，k=1 的计算：

```python
for combo in combinations(models, 1):  # 4 个单模型 combo
    gs_vals = []
    for i, iid in enumerate(common_ids):
        gs_vals.append(max(model_greedy[m][i] for m in combo))  # k=1 时就是该模型的 greedy F1
    greedy_sels.append(instance_avg(gs_vals))  # 该模型的平均 greedy F1
gs_mean = np.mean(greedy_sels)  # 4 个模型平均
```

k=1 时 `greedy_sel` = 4 个模型 greedy F1 的算术平均。

### 数值矛盾

| 计算方式 | 值 |
|---------|-----|
| 脚本逻辑 → (0.6382 + 0.6301 + 0.6068 + 0.3992) / 4 | **0.5686** |
| JSON scaling_curve k=1 greedy_sel | **0.5558** |
| 差异 | 0.0128 (1.28pp) |

同样的问题出现在 k=1 cross_oracle：

| 计算方式 | 值 |
|---------|-----|
| 脚本逻辑 → (0.7203 + 0.7575 + 0.6544 + 0.7140) / 4 | **0.7116** |
| JSON scaling_curve k=1 cross_oracle | **0.7306** |
| 差异 | 0.0190 (1.90pp) |

### 根因

**JSON 数据文件不是由 `e4_ensemble_scaling.py` 直接生成的。** 证据：
- 脚本输出 key 是 `greedy_selection_mean`，JSON 中是 `greedy_sel`
- 脚本输出含 `sample_pool_oracle_mean` 和 `n_combinations`，JSON 中没有
- JSON 含 `n_samples_per_model`, `temperature`, `matching` 等 meta 字段，脚本不生成这些

JSON 是手工编纂的，scaling_curve 的值来源不明——可能来自不同版本的分析脚本或不同的 instance 子集。

### 哪个值正确

- **Per-model greedy F1**（0.6382, 0.6301, 0.6068, 0.3992）：来自各模型独立运行的 `summary.json`，可信度高
- **k=1 greedy_sel = 0.5558**：与上述值数学矛盾，不可信
- 正确的 k=1 greedy_sel 应为 **0.5686**
- 正确的 k=1 cross_oracle 应为 **0.7116**

**k=4 的值无法从 per-model 数据验证**（需要 instance-level cross-model 计算），且 3/4 原始数据已丢失。

### 总结

| 问题 | 结论 |
|------|------|
| k=1 的定义 | 对所有 C(4,1)=4 种单模型选择，计算 instance-average greedy F1，再求均值 |
| 为什么与算术均值不同 | **不应该不同**——数学上等价。差异来自 JSON 手工编纂错误 |
| 正确数值 | k=1 greedy_sel = **0.5686**（非 0.5558），k=1 cross_oracle = **0.7116**（非 0.7306） |
| k=2,3,4 的值 | 无法验证——原始数据缺失 |

---
