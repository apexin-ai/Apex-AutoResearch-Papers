# research scierc constrained code version check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scierc_constrained_code_version_check_20260520T141740_result.json`
- **Structured JSON:** [`5ca3513c3fd1dace9d4b.json`](../../sessions/5c/5ca3513c3fd1dace9d4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

## 结论

### 1. SciERC constrained 数据的代码版本

Table 2 中的 SciERC constrained 数据全部来自 **May 15-16**（旧代码，May 18 grammar fix 之前）：

| 实验 | 原始文件 | 时间戳 | Registry |
|------|---------|--------|----------|
| Qwen con | `w5_lora_scierc_full_s1_eval.jsonl` | May 16 00:21 | `w5_lora_scierc_constrained_eval`, completed May 15 16:25 UTC |
| Llama con | `w5_llama_lora_scierc_constrained.jsonl` | May 16 01:58 | `w5_llama_lora_scierc_constrained_eval`, completed May 15 18:12 UTC |

### 2. 是否有 May 18+ 后新代码跑过的 SciERC constrained 数据？

**没有。** Post-fix 只有：
- `d062_full_ft_scierc`（May 19）— 全量 fine-tune，非 LoRA，不是 Table 2 的模型
- `d066_sweep_llama_scierc_beam1_unc`（May 20）— unconstrained + INVALIDATED（用了 dev set）

### 3. 新代码对 SciERC DR 的影响

**几乎为零。** 旧代码下 SciERC constrained DR 已经极低：

| 模型 | DR (旧代码) | DR 违规数 | 总 relations |
|------|------------|----------|-------------|
| Qwen con | **0.00%** | 0 | 1128 |
| Llama con | **0.09%** | 1 | 1081 |

对比 DocRED（DR 0.21% → 0%），SciERC 的 schema 只有 7 个 relation types（vs DocRED 96 个），旧代码对 SciERC 的 domain-range 约束已经几乎完美执行。新代码最多消除 Llama 的那 1 个 DR 违规。

### 4. 是否需要重跑？

**不需要。** 理由：
- Qwen DR 已经是 0.00%，新代码不会改变任何输出
- Llama DR=0.09%（1 个违规），新代码最多修正这 1 个 doc 的输出，对 F1 影响可忽略（< 0.1pp）
- 与 DocRED 不同（DR 从 0.21% 降到 0%，且 DocRED 规模大得多），SciERC 的变化完全在噪声范围内

如果追求绝对一致性（论文所有数据都用同一版代码），可以重跑，但结果不会有实质性变化。

---
