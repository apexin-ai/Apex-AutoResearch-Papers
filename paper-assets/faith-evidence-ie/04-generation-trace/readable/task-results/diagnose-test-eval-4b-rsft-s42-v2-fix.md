# diagnose test eval 4b rsft s42 v2 fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_test_eval_4b_rsft_s42_v2_fix_20260522T011529_result.json`
- **Structured JSON:** [`40dc0870cb4953766a71.json`](../../sessions/40/40dc0870cb4953766a71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**根因**：v2 命令有两个错误：
1. `--rsft_adapter` 不是 `test_inference.py` 的合法参数（EXIT_CODE=2 的直接原因）
2. base model 路径 `/models/Qwen/Qwen3-4B` 不存在（实际路径是 `/models/Qwen3-4B`）

**修复**：按 `test_inference.py` 的 nested LoRA 接口约定重新映射参数：
- `--model_path` → RSFT adapter (`rsft_output_ced_s42_v2`)
- `--base_model` → 基座模型 (`models/Qwen3-4B`)
- `--sft_adapter` → SFT adapter (`sft_output`)
- 删除 `--rsft_adapter`

**已提交** `test_eval_4b_rsft_s42_v3`，PID 151217，cuda:2（显存 0 MiB，干净），registry 已更新。

---
