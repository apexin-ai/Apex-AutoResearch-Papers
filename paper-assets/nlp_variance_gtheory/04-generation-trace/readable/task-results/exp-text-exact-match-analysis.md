# exp text exact match analysis

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_text_exact_match_analysis_20260520T185810_result.json`
- **Structured JSON:** [`0c423e6626fafae47f08.json`](../../sessions/0c/0c423e6626fafae47f08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组结果都拿到了。以下是完整的 text_exact_match 方差分解结果及与 binary correct 的对比分析。

---

## text_exact_match 方差分解结果（5400 obs, 6 facets）

| 排名 | Component | Estimate | % | 95% CI |
|------|-----------|----------|---|--------|
| 1 | **residual** | 0.061132 | **40.7%** | [0.0576, 0.0621] |
| 2 | **prompt_template:item_id** | 0.056303 | **37.5%** | [0.0468, 0.0643] |
| 3 | **temperature** | 0.025345 | **16.9%** | [0.0186, 0.0310] |
| 4 | temperature:item_id | 0.003716 | 2.5% | [0.0017, 0.0054] |
| 5 | precision:temperature | 0.001896 | 1.3% | [0.0008, 0.0036] |
| 6 | precision:item_id | 0.000944 | 0.6% | [0.0000, 0.0030] |
| 7 | ordering:item_id | 0.000451 | 0.3% | [0.0000, 0.0012] |
| 8–22 | 其余 15 个分量 | ~0 | <0.3% | — |

**总方差**: 0.1503

---

## 与 binary correct 结果的对比

| Component | correct (%) | text_exact_match (%) | 变化 |
|-----------|-------------|----------------------|------|
| **item_id** | **58.4%** | **0.0%** | 大幅下降 |
| **residual** | 17.6% | **40.7%** | +23.1pp，大幅上升 |
| **prompt_template:item_id** | 5.7% | **37.5%** | +31.8pp，大幅上升 |
| **temperature** | 0.0% | **16.9%** | 从零到第三大 |
| precision:item_id | 7.2% | 0.6% | 大幅下降 |
| temperature:item_id | 6.8% | 2.5% | 下降 |
| seed:item_id | 2.7% | 0.0% | 消失 |
| precision:temperature | ~0% | 1.3% | 新增显著 |
| precision | 0.9% | 0.0% | 消失 |

---

## 关键发现

**1. item_id 主效应消失 (58.4% → 0%)**：binary correct 下题目难度是最大方差来源；但 text_exact_match 衡量的是"生成文本是否确定性一致"，难度信息被吸收掉了——一个难题可能始终答错（text 一致），match 率反而很高。

**2. prompt_template:item_id 跃升为第二大分量 (5.7% → 37.5%)**：不同 prompt 模板让不同题目产生不同文本措辞，即使答案正确性不变。这说明 prompt wording 对生成文本的具体形式有巨大影响——是文本级不确定性的核心来源。

**3. temperature 成为显著主效应 (0% → 16.9%)**：temperature=0 时文本几乎完全确定性，temperature>0 时大量文本 mismatch。binary correct 下 temperature 影响不大（答案对错稳定），但文本级 exact match 对 temperature 极其敏感。

**4. residual 大幅上升 (17.6% → 40.7%)**：40.7% 的方差无法被 6 个 facet 的主效应和二阶交互解释——高阶交互（≥3-way）或未建模的随机性（infrastructure nondeterminism）贡献显著。这正是 text_exact_match 更能捕获的 infrastructure-level variance。

**5. precision 相关分量**：precision:temperature 从 ~0% 升至 1.3%（CI 不含零），说明精度与温度在文本级有显著交互——某些 precision×temperature 组合下文本确定性表现不同。但 precision 主效应和 precision:item_id 反而下降，表明精度对"文本是否一致"的影响主要通过与 temperature 的交互体现，而非独立效应。

---
