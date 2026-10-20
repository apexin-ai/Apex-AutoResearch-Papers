# code prep 1 7b eval scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_1_7b_eval_scripts_20260519T055940_result.json`
- **Structured JSON:** [`b3bd509d366a55dfd63d.json`](../../sessions/b3/b3bd509d366a55dfd63d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dry-run 通过，参数解析正确。

**汇报：**

脚本已创建并验证：
- `/root/autodl-tmp/freige/scripts/seed_expansion/eval_1_7b_s43_r2.sh` — s43 已可运行
- `/root/autodl-tmp/freige/scripts/seed_expansion/eval_1_7b_s44_r2.sh` — 等 s44 训练完成

**与用户模板的关键修正（基于实际代码）：**

| 用户模板 | 实际代码 |
|---|---|
| `python freige/inference.py` | `python -m freige.eval.inference` |
| `--rsft_adapter` | 不存在。`--model_path` 传 RSFT adapter，`--base_model` 传基础模型 |
| `--input_file` / `--output_file` | `--data_path`（目录）/ `--output_dir` |
| 分两步 inference + batch_eval.py | 一步完成推理+评测 |
| base model: `models/Qwen3-1.7B` | 实际路径 `models/Qwen/Qwen3-1.7B` |

s43 checkpoint 完整：adapter_model.safetensors (279MB) + adapter_config.json 均存在。

---
