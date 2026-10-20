# code verify retry params and fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_retry_params_and_fix_20260518T000031_result.json`
- **Structured JSON:** [`d3cc1ee7c9cf8d6a1178.json`](../../sessions/d3/d3cc1ee7c9cf8d6a1178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 参数确认

| | Llama retry | Qwen retry |
|---|---|---|
| **命令** | `run_constrained_extraction.py --mode full_s1 --dataset wikievents --model_path .../Meta-Llama-3.1-8B-Instruct --max_new_tokens 8192 --resume` | `run_constrained_extraction.py --mode full_s1 --dataset wikievents --model_path .../Qwen3-8B --max_new_tokens 8192 --resume` |
| **max_new_tokens** | **8192** (确认：失败文档 raw output 平均 ~7362 tokens，最大 ~8460 tokens，明显命中 8192 上限) | **8192** (从 `ps aux` 直接确认命令行) |

## Llama retry 结果分析

- 已完成：215 success / 31 fail（246 total）
- 31 个失败中 **29 个是 token 截断**（raw output 没有 JSON 闭合），2 个是其他 parse 错误
- 平均 raw output ~29,447 chars (~7,362 tokens)，max ~33,841 chars (~8,460 tokens)

## 执行的修复动作

- 从 `wikievents_llama_constrained_full.jsonl` 移除 31 个 failure 行（保留 215 success）
- 备份：`wikievents_llama_constrained_full.jsonl.bak_before16k`
- **启动 `llama_retry_16k` tmux session**：cuda:1，`--max_new_tokens 16384 --resume`
- 已验证：cuda:1 使用中 (86% util, 16.5GB VRAM)

## Qwen retry 当前状态

- **运行中**：cuda:0, `--max_new_tokens 8192`
- 进度：238/246（还剩 8 个文档）
- 当前统计：205 success / 33 fail（预计最终 ~206-210 success）
- Qwen retry 完成后，如果也有截断失败，同样需要移除 failure 行并用 16384 重试（等 Llama 用完 cuda:1，或在 cuda:0 上继续）

---
