# ops submit llama rsft s43 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_llama_rsft_s43_eval_20260519T201335_result.json`
- **Structured JSON:** [`b82173763f4e46c19aa0.json`](../../sessions/b8/b82173763f4e46c19aa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。汇总：

**eval_llama_rsft_k1_s43** — RUNNING on cuda:3

| 项 | 值 |
|---|---|
| tmux session | `eval_llama_rsft_k1_s43` |
| GPU | cuda:3 (确认空闲 0 MiB) |
| base model | `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B` |
| SFT adapter | `/root/autodl-tmp/sft_output_llama_3_1_8b` |
| RSFT adapter | `/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43` |
| output | `/root/autodl-tmp/eval_results/eval_llama_rsft_k1_s43` |
| log | `~/runs/faith-evidence-ie/eval_llama_rsft_k1_s43.log` |
| D076 参数 | `--no-quantize --batch_size 4 --max_new_tokens 1024 --seed 42` |

日志确认模型已开始加载（base model shards loaded, SFT adapter merging）。

注：`submit_training_job` 工具不在当前可用工具列表中，改用 `ssh_execute` + tmux 直接提交。命令格式参考 `d102_llama_rsft_k1_s43_eval` 的已验证命令。

---
