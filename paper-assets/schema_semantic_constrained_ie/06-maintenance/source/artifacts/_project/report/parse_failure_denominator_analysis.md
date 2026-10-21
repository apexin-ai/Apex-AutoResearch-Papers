# Parse Failure Denominator Analysis

## 1. 当前计算方式

**Violation rates 的分母仅来自 successfully parsed documents，不含 parse failure 文档。**

代码逻辑（`violation_checker.py` / `violation_checker_docred.py`）：
- 遍历所有样本，若 `parsed_output is None` 则 `parse_failures += 1; continue`
- 只有成功解析的文档累积进 `total_pred_relations` / `total_pred_entities`
- 最终：`DR_pct = dr_violation_count / total_pred_relations × 100`

即：parse failure 文档既不贡献分子（violations = 0），也不贡献分母（relations = 0）。

---

## 2. "All-set" vs "Parsed-only" 对比

**方法**：假设 parse failure 文档若成功解析，会产生与已解析文档相同的平均 relations 数。则：

```
all_set_rate = current_rate × (parsed_docs / total_docs)
             = current_rate × (1 - parse_fail_rate)
```

### 重点案例：Llama DocRED ZS Constrained

| Metric | Parsed-only | All-set | Delta |
|--------|------------|---------|-------|
| DR | 2.55% | 2.32% | −0.23 pp |
| RV | 0% | 0% | — |
| ET | 0% | 0% | — |

- Parse failures: 91/998 (9.12%)
- 影响幅度：DR 下降 9.1%（相对）

### 全实验对比表

| Experiment | Parse Fail% | Metric | Parsed-only | All-set | Δ (pp) |
|-----------|------------|--------|-------------|---------|--------|
| **Llama DocRED ZS Constr.** | 9.12% | DR | 2.55% | 2.32% | −0.23 |
| Llama DocRED ZS Unconstr. | 6.81% | DR | 26.07% | 24.29% | −1.78 |
| Llama DocRED ZS Unconstr. | 6.81% | RV | 16.03% | 14.94% | −1.09 |
| **Qwen DocRED ZS Constr.** | 1.10% | DR | 10.21% | 10.10% | −0.11 |
| Qwen DocRED ZS Unconstr. | 1.20% | DR | 18.46% | 18.24% | −0.22 |
| Qwen DocRED ZS Unconstr. | 1.20% | RV | 29.66% | 29.30% | −0.36 |
| Qwen SciERC ZS Constr. | 0% | DR | 0.93% | 0.93% | 0 |
| **Qwen DocRED FT Constr.** | 8.52% | DR | 0.01% | 0.009% | −0.001 |
| Qwen DocRED FT Unconstr. | 7.11% | DR | 0.76% | 0.71% | −0.05 |
| **Llama DocRED FT Constr.** | 2.51% | DR | 0.20% | 0.195% | −0.005 |
| Llama DocRED FT Unconstr. | 2.30% | DR | 0.49% | 0.48% | −0.01 |

### 对 Constrained vs Unconstrained 差值的影响

关键问题：分母选择是否改变 "constrained 降低了多少 violation" 的结论？

以 Llama DocRED ZS 为例：
- Parsed-only: Δ(DR) = 26.07% − 2.55% = **23.52 pp reduction**
- All-set: Δ(DR) = 24.29% − 2.32% = **21.97 pp reduction**
- 结论变化：reduction 幅度从 23.52 → 21.97 pp，相对差异 6.6%

以 Qwen DocRED FT 为例：
- Parsed-only: Δ(DR) = 0.76% − 0.01% = **0.75 pp reduction** (98.7% relative)
- All-set: Δ(DR) = 0.71% − 0.009% = **0.70 pp reduction** (98.7% relative)
- 相对 reduction 比例不变

---

## 3. 结论

**差异不 material，不影响论文结论。**

理由：

1. **调整幅度小**：all-set 率 = parsed-only 率 × (1 − parse_fail_rate)。最大 parse failure 率为 9.12%（Llama DocRED ZS），对应最大调整仅 ~9% 相对缩减。

2. **Constrained 与 Unconstrained 受同向影响**：两者的 parse failure 率相近（同模型同数据集），因此差值（reduction）的变化更小。相对 reduction 比例几乎不变。

3. **FT 实验影响可忽略**：FT 后 violation 率已极低（<0.2%），即使 parse failure 率达 8.5%，绝对调整量 <0.01 pp。

4. **论文通常报告 parsed-only 率是合理做法**：violation checker 只能检测成功解析的输出，对 parse failure 文档无法判定是否违规。将其假设为 0-violation 加回分母是乐观估计（实际这些文档格式都错了，可能 violation 更高）。

**建议**：论文中保持当前 parsed-only 计算方式，在方法论部分注明分母为 "successfully parsed outputs"，并单独报告 parse failure rate 作为系统可靠性指标。
