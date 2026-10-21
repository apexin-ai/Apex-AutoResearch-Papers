# paper entropy std d trace

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_entropy-std-d-trace_20260523T103849_result.json`
- **Structured JSON:** [`40a501cac02b26e533f7.json`](../../sessions/40/40a501cac02b26e533f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据溯源完成。以下是完整汇报。

---

## 任务 1：entropy_std d=0.55 溯源

### 结论：**d=0.55 无法精确追溯到任何现存数据或计算脚本**

所有可复现的计算结果：

| 数据集/方法 | d 值 |
|---|---|
| 8-gen pooled (gen-1 vs gen-2+, `tost_equivalence.json`) | **0.457** [CI: 0.435, 0.479] |
| 8-gen bootstrap (`tost_bootstrap.json`) | 0.458 |
| 6-gen pooled (gen-1 vs gen-2+, `features_all_models.csv`) | 0.493 |
| 8-gen per-generator avg (gen-1 vs gen-2+) | mean=0.463, median=0.507 |
| 6-gen per-generator avg (gen-1 vs gen-2+) | mean=0.496, median=0.524 |
| gen-0→gen-1 step d (`trend_analysis.json`) | 0.558 |
| Single-gen Pythia-2.8B (gen-1 vs gen-2+) | 0.389 |

**最可能来源**：gen-0→gen-1 步长 d=0.558（来自 `trend_analysis.json`），四舍五入后被误用为 "pooled d=0.55"，但这个值仅代表首步变化，不是论文声称的整体 effect size。

### 内部矛盾

同一个 `appendix_ddr_validation.tex` 中存在两个不同值：
- **第85行**: `entropy std ($d{=}0.49$)` ← 接近实际 6-gen 数据 0.493
- **第101/112行**: `entropy std ($d{=}0.55$)` ← 无数据支撑

### 当前正确值

应使用 **d = 0.46**（8-gen, gen-1 vs gen-2+, 95% CI [0.44, 0.48]）。

论文中需要修正的位置（均写 d=0.55）：
- `abstract.tex:4`
- `introduction.tex:9, 25`
- `results.tex:71, 76`
- `appendix_ddr_validation.tex:101, 112, 121`

同时 `appendix_ddr_validation.tex:85` 的 d=0.49 虽更接近但也应统一修正。

---

## 任务 2：Table 4 (cross-ref) 校验

**Table 4 值与服务器数据一致**（数据源：`review_p2f_cross_ref_bias.json`，5-gen LOGO 子集）：

| Reference | 论文值 | 服务器值 | 匹配 |
|---|---|---|---|
| Pythia-410M | 0.803 | 0.8034 | ✓ |
| OLMo-2-1B | 0.807 | 0.8072 | ✓ |
| Qwen3-0.6B | 0.816 | 0.8158 | ✓ |
| Spread | 0.013 | 0.0124 | ✓ (rounded) |

**注意事项**：Table 4 使用 5-gen 子集（olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b），不包含 Llama、Mistral、Qwen3-8B。论文其他表格均使用 8-gen 配置，需评估是否更新 Table 4 到 8-gen。

---

### 总结

- **d=0.55**：**陈旧值，无数据支撑**。正确值为 d=0.46（8-gen）或 d=0.49（6-gen）。涉及 abstract、intro、results、appendix 共 ~9 处需修正。
- **Table 4**：数据正确，无需修正内容值。但注意其使用 5-gen 子集与其他表格的 8-gen 不一致。

---
