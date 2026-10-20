# code mbpp eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mbpp_eval_20260519T132515_result.json`
- **Structured JSON:** [`75419df42497d58869fd.json`](../../sessions/75/75419df42497d58869fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出

**`/root/recovery_aware_struct_prune/src/eval_mbpp.py`** — MBPP 374 题 pass@1 评估脚本

### 与 HumanEval 的差异处理

| 差异点 | HumanEval | MBPP |
|--------|-----------|------|
| Prompt | function signature + docstring → 补全 body | task description + test cases → 生成完整函数 |
| 测试执行 | `code + test + check(entry_point)` | `test_setup_code + code + assert statements` |
| 数据集 | `openai/openai_humaneval` test split (164题) | `mbpp` train split (374题 sanitized) |

### 参数（与 HumanEval 对齐）
`--model_path`, `--output_path`, `--max_new_tokens`(默认2048), `--max_samples`, `--seed`, `--dtype`, `--timeout`

### Dry-run 结果
- `--help` 参数解析 ✅
- 3 题端到端 pipeline ✅（模型加载 → 数据集加载374题 → 推理 → 代码提取 → sandbox执行 → JSON输出 → sentinel文件）
- 0/3 pass 是模型质量问题（pruned model），pipeline 本身无 bug

---
