# analysis eval command prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-command-prep_20260516T003947_result.json`
- **Structured JSON:** [`5da7cbe9b9175c2d20b2.json`](../../sessions/5d/5da7cbe9b9175c2d20b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/ced_eval_commands.md` 并注册。

内容：两个完整 eval 命令（基于 eval_flat_nli_s44 模板），提交前需：
1. `ls` 确认最终 checkpoint 目录名替换 `&lt;CHECKPOINT>`
2. `nvidia-smi` 确认目标 GPU 空闲后替换 `&lt;GPU>`
3. `--sft_adapter /root/autodl-tmp/sft_output` 已包含

---
