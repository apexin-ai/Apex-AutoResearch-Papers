# paper llama table3 update

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_llama_table3_update_20260514T214809_result.json`
- **Structured JSON:** [`447a5f32c05725392bd2.json`](../../sessions/44/447a5f32c05725392bd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied and verified.

**修改清单**：

`analysis.tex`:
- L27 Llama 描述：concentration 0.34 → 0.57；"spike-like" → "spike"；t1/t5 0.71 → 0.85；删除 t1/t2=21.7
- L42 Table 3 Llama 行：`$^\ddagger$` → `$^\dagger$`；0.34 → 0.57；0.71 → 0.85
- L71 diagnostic Spike 示例：Llama (0.34, $t_1/t_5{=}0.71$) → Llama (0.57, $t_1/t_5{=}0.85$)；"counterproductive or marginal" 此前已是 "no benefit or marginal"
- 新增 joint-diagnostic 必要性论证（紧接 "The joint condition" 之前）

`conclusion.tex`:
- L7 Llama 引用：$t_1/t_5{=}0.71$ → concentration 0.57, $t_1/t_5{=}0.85$

`experiments.tex`:
- L66-67 Llama narrative 与新数据对齐："low sensitivity heterogeneity" → 明确的 spike 解释（concentration 0.57, $t_1/t_5{=}0.85$，L2H5 主导）

**caption**：Gemma-2 仍用 `$^\ddagger$`（standard profiling, hires pending），caption 不变。

**验证**：全局 grep 已确认无残留 Llama context 的 0.34/0.71/$^\ddagger$/spike-like。

---
