# fix fewnerd r value discrepancy

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fewnerd_r_value_discrepancy_20260516T061329_result.json`
- **Structured JSON:** [`3aa4aa98d565e1f1a825.json`](../../sessions/3a/3aa4aa98d565e1f1a825.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 差异来源

| 指标 | r 值 | 来源脚本 | dependent variable |
|------|------|----------|-------------------|
| Table 2 | **0.112** | `src/bootstrap_ci.py` | confusion **rate**: `(c12+c21) / (gold_t1+gold_t2)` |
| JSON | **0.138** | `scripts/cross_embedding_sensitivity.py` | confusion **count**: `c12+c21` (unnormalized) |

**根本原因**：两个脚本对同一批 1,953 个 type pair 使用了不同的因变量。

- `bootstrap_ci.py` 计算的是 confusion rate（混淆次数 / gold 实例总数），与论文 Section 4.2 的描述 *"the fraction of $t_i$ gold instances misclassified as $t_j$"* 一致
- `cross_embedding_sensitivity.py` 使用原始混淆计数，未按 gold 频次归一化

次要差异：文本匹配时 `bootstrap_ci.py` 用 case-sensitive，`cross_embedding_sensitivity.py` 用 case-insensitive。

**验证**：Table 2 的 $r^2 = 0.013$ 与 $0.112^2 = 0.0125 \approx 0.013$ 一致。

## 结论

**Table 2 的 r = 0.112 是正确的**，与论文方法描述匹配。不需要修改 LaTeX。

`cross_embedding_sensitivity_results.json` 的 r = 0.138 不是错误——它度量的是不同的东西（SCS 与 raw count 的相关性 vs. SCS 与 confusion rate 的相关性）。JSON 作为 cross-embedding robustness check 保留原值即可，不需要与 Table 2 统一。

**无需修改任何文件。**

---
