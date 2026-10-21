# experiment qwen3 1 7b sft eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_qwen3_1_7b_sft_eval_r2_20260516T081017_result.json`
- **Structured JSON:** [`c5f0935e51d13d20525c.json`](../../sessions/c5/c5f0935e51d13d20525c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：**
- Qwen3-1.7B SFT eval 已在 cuda:1 上启动（PID 319245）
- 模型从本地加载，无 HF 下载
- Base model: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`，SFT adapter: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16`（merge 方式）
- 推理中：247 batches，~27s/batch，预计 ~1.8h 完成
- Registry: `plan_006_qwen3_1_7b_sft_eval` → RUNNING

**注意：** cuda:1 上同时有另一个 worker 的 4B test eval（PID 319638，9.8GB）。当前总占用 ~15GB/32GB，两者目前都在正常推理，但需关注后续是否 OOM。

---
