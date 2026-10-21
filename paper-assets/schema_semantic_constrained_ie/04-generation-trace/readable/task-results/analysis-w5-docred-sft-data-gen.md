# analysis w5 docred sft data gen

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_docred_sft_data_gen_20260515T175244_result.json`
- **Structured JSON:** [`e31676ce34ade1c80e74.json`](../../sessions/e3/e31676ce34ade1c80e74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## w5_docred_sft_data_gen 实验结果报告

### 1. 日志状态
**成功完成，无报错。** `EXIT_CODE=0`,流程：加载约束规范 → 加载 Qwen3-8B tokenizer → 处理 train_annotated.json (3053 文档) → 处理 dev.json (998 文档)。

### 2. 数据规模
| 文件 | 行数 | 大小 | 实体总数 | 关系总数 | 均值实体/文档 | 均值关系/文档 |
|------|------|------|---------|---------|---------------|---------------|
| sft_train.jsonl | 3053 | 19M | 59,493 | 38,180 | 19.49 | 12.51 |
| sft_dev.jsonl | 998 | 6.0M | 19,528 | 12,275 | 19.57 | 12.30 |

跳过空文档：0。

### 3. 格式与质量
- **JSON 格式：** 4051 行全部解析通过，0 行损坏或缺字段。
- **字段：** 每行包含 `prompt`, `completion`, `doc_id`, `n_entities`, `n_relations`。
- **Prompt 结构：** Qwen3 chat 模板（`<|im_start|>...<|im_end|>` + `&lt;think>\n\n&lt;/think>`），包含 6 个实体类型 (PER/ORG/LOC/TIME/NUM/MISC) 和 96 个 DocRED 关系类型清单。
- **Completion 结构：** 合法 JSON，含 `entities`(text+type) 和 `relations`(head/tail/type/head_type/tail_type) 字段，三元组与文档内容一致（如 "Skai TV → Piraeus → headquarters location"）。

### 4. 异常/警告
无。数据可直接用于 SFT 训练。

---
