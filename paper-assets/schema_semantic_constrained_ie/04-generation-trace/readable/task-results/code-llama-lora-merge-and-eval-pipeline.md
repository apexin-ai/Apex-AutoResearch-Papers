# code llama lora merge and eval pipeline

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_lora_merge_and_eval_pipeline_20260515T171548_result.json`
- **Structured JSON:** [`ae7530bb4dcced294d0c.json`](../../sessions/ae/ae7530bb4dcced294d0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 执行结果汇总

### 1. cuda:1 释放
- **已释放**: 0 MiB, 0% utilization (kill 283829 成功)
- cuda:0: 17169 MiB / 89% — 正在运行 unconstrained eval (PID 287677)

### 2. 根分区空间
- **无需清理**: 12G used / 19G avail (38%)
- 两个 merged checkpoint 已是 symlink 到数据盘 `/root/autodl-tmp/checkpoints/`
- Steps 2-3 跳过

### 3. Llama LoRA 合并
- **已完成** — 4/4 shards 完整，位于 `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged`
  - shard 1: 4.7 GB
  - shard 2: 4.7 GB
  - shard 3: 4.6 GB
  - shard 4: 1.1 GB
- Llama 基座路径确认: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`

### 4. Registry 更新
- `w5_llama_lora_scierc_training`: **DONE** — metrics 已写入 (train_loss=0.023, eval_loss=0.060, token_acc=99.2%/98.2%)
- `w5_llama_lora_scierc_unconstrained_eval`: **DONE**, conclusion=success

### 5. Unconstrained eval
- **已完成**: 100/100 样本已处理 (PID 287677 仍驻留 cuda:0)
- 输出: `outputs/w5_llama_lora_scierc_unconstrained.jsonl` (189KB)
- 无需重新提交

### 6. type_mask_processor.py
- **已是 clean 版本**: 399 行, 0 个 cf_fallback 引用。无需恢复。

**所有步骤均已就绪。** 下一步可以直接启动 constrained eval (full_s1 mode) — cuda:1 空闲可用，type_mask_processor 已是正确版本。

---
