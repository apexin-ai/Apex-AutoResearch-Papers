# plan 7b 14b batch prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_plan_7b-14b-batch-prep_20260518T070410_result.json`
- **Structured JSON:** [`c0d0bfd88c83b4de0738.json`](../../sessions/c0/c0d0bfd88c83b4de0738.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已创建并注册：`artifacts/batch_matrix_commands.md`

内容包含：
- **Batch 1 初始启动**（4 卡并行）：Qwen-7B×2 + 14B + Llama-8B 各 1 run
- **Batch 1 续**：Qwen-7B 共 8 runs（cuda:0/1 各 4 sequential），14B 4 runs（cuda:2），Llama 4 runs（cuda:3）
- **Batch 2**：Mistral 4 runs（cuda:0），Gemma 4 runs（cuda:1）
- 每条命令完整可复制：`CUDA_VISIBLE_DEVICES=N` + `source activate` + 全参数（`--lr 5e-5` 显式）
- 末尾 Summary Table 总览 24 runs 的 GPU/model/dosage/seed 分配

---
