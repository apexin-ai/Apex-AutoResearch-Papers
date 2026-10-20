# code llama docred sft data gen

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_docred_sft_data_gen_20260515T180719_result.json`
- **Structured JSON:** [`9a3d902b7aad9f16b0fa.json`](../../sessions/9a/9a3d902b7aad9f16b0fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**结果汇总：**

| 文件 | 路径 | 大小 | 样本数 |
|------|------|------|--------|
| train | `data/docred/sft_train_llama.jsonl` | 19M | 3053 |
| dev | `data/docred/sft_dev_llama.jsonl` | 6.1M | 998 |

**格式验证：**
- 每行均可解析为合法 JSON
- Prompt 使用 Llama 3.1 chat template（`<|begin_of_text|>`, `<|start_header_id|>`, `<|eot_id|>`），无 Qwen token
- Completion 均为合法 JSON，包含 `entities` + `relations` 字段
- Prompt 包含 6 个实体类型和 96 个 DocRED 关系类型
- Prompt 通过 `build_messages` + `_chat_template_kwargs` 与推理脚本字节级对齐
- 现有 Qwen 版 SFT 文件未被修改

---
