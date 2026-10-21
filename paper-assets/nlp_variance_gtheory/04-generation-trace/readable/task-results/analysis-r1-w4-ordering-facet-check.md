# analysis r1 w4 ordering facet check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r1_w4_ordering_facet_check_20260521T195344_result.json`
- **Structured JSON:** [`19962477ad1d3ea001c2.json`](../../sessions/19/19962477ad1d3ea001c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整图景清晰。下面是结论。

---

## R1-W4 结论：Ordering facet 在 GSM8K/MATH 的实现检查

### 1. 代码实现摘要

`run_experiment.py:75-101` 的 `_build_prompt()` 函数按 benchmark 路由：

| Benchmark | ordering 是否传入 prompt builder | 机制 |
|-----------|------|------|
| **MMLU** | **是** | `few_shot[subject][str(ordering)]` — 选择 5 个 dev-set 示例的不同排列 |
| GSM8K | **否** | `format_gsm8k_prompt(template_id, question, few_shot)` — 无 ordering 参数 |
| MATH | **否** | `format_math_prompt(template_id, question, few_shot)` — 无 ordering 参数 |
| ARC | **否** | `format_arc_prompt(...)` — 无 ordering 参数 |
| HellaSwag | **否** | `format_hellaswag_prompt(...)` — 无 ordering 参数 |

**关键澄清**：ordering 的实际含义是 **few-shot 示例排列顺序**（不是 ABCD 选项轮转）。仅 MMLU 的 few-shot 数据按 `{subject → {ordering_id → [examples]}}` 组织，其他 benchmark 的 few-shot 是 flat list。

### 2. 数据验证

**GSM8K**（6 models）：

| Model | Ordering 1 | 2 | 3 | 4 | Max-Min diff | Identical |
|-------|-----------|---|---|---|-------------|-----------|
| deepseek | 0.3858 | 0.3858 | 0.3871 | 0.3871 | 0.00134* | **True** |
| gemma | 0.8047 | 0.8047 | 0.8047 | 0.8047 | 0.0 | True |
| internlm | 0.6781 | 0.6781 | 0.6781 | 0.6781 | 0.0 | True |
| llama | 0.4897 | 0.4897 | 0.4897 | 0.4897 | 0.0 | True |
| mistral | 0.3065 | 0.3065 | 0.3065 | 0.3065 | 0.0 | True |
| qwen | 0.6222 | 0.6222 | 0.6222 | 0.6222 | 0.0 | True |

\* deepseek 的差异因 ordering 3/4 各缺 1 个 condition（49 vs 50 conditions）。在完整匹配的 9800 行中，4 个 ordering 的 correct 值 **完全一致（0 差异行）**。

**MATH**（4 models with ordering column）：全部 diff=0.0，perfectly identical。

**ARC/HellaSwag**（llama 抽查）：diff=0.0，也是 no-op。

**MMLU 对照**（llama）：diff=0.0042，ordering **有实际效应**。

### 3. 结论

**Ordering 在 GSM8K/MATH（以及 ARC/HellaSwag）上是结构性 no-op。** 这不是经验发现，而是代码逻辑决定的——prompt builder 对这些 benchmark 根本不读 ordering 值，4 个 ordering level 生成完全相同的 prompt，因此 SS(ordering) = 0 by construction。

仅 MMLU 的 ordering facet 有实际效应（通过改变 few-shot 示例的呈现顺序影响准确率）。

### 4. 论文写法建议

1. **Design 章节**：将 ordering 定义为 "the permutation order of few-shot demonstration examples"（而非 ABCD 选项轮转），明确说明该 facet 仅对 MMLU 有操作性效应
2. **方差分解讨论**：注明 GSM8K/MATH/ARC/HellaSwag 的 σ²(ordering) = 0 是结构性零（structurally zero），非经验结果。可在 footnote 或 Limitations 中简要说明
3. **设计合理性**：保留全 benchmark 的 ordering 交叉是为了维持平衡析因结构，方便统一的 G-study 框架。但应避免将 ordering 对这些 benchmark 的零方差解读为"ordering 不重要"的经验证据

---
