# code r16 gollie comparison

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r16_gollie_comparison_20260521T033212_result.json`
- **Structured JSON:** [`f453b096018a0a000d70.json`](../../sessions/f4/f453b096018a0a000d70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Option 2 adopted** — GoLLIE prompt格式与OntoCoDec的JSON FSM约束不兼容，无法直接组合。改用已有的GoLLIE-7B实验数据(D063) + 论文公开数据。

**关键对比 (document-level, SciERC):**

| Method | Model | Setting | E-F1 | R-F1 | DR% | ET% |
|--------|-------|---------|------|------|-----|-----|
| GoLLIE | CodeLlama-7B | ZS | 9.17 | 0.0 | 0.0 | 0.0 |
| OntoCoDec unc | Qwen-3-8B | ZS | 31.39 | 8.25 | 15.37 | 0.40 |
| OntoCoDec S1 | Qwen-3-8B | ZS | 31.45 | 8.38 | 0.93 | 0.0 |
| KnowCoder | LLaMA2-7B | FT | - | 40.0 | - | - |
| OntoCoDec S1 | Llama-3.1-8B | FT | 67.09 | 45.47 | 0.09 | 0.0 |

**核心发现：**
- GoLLIE通过Python dataclass格式获得0%类型违规，但F1极低（E-F1=9.17%, R-F1=0%, 45%文档空输出）
- OntoCoDec S1在保持F1的同时消除ET/RV违规，DR从15.37%降至0.93%
- OntoCoDec FT+S1 (R-F1=45.47) 超过KnowCoder公开的40.0
- 两种方法互补：GoLLIE约束输出格式（结构合规），OntoCoDec约束生成内容（语义合规）

GoLLIE论文未评估SciERC，我们的GoLLIE-7B实验是原创数据。

---
