# analysis d102 all training

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102_all_training_20260518T084854_result.json`
- **Structured JSON:** [`3a8dee509b6712927d40.json`](../../sessions/3a/3a8dee509b6712927d40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 D102 RSFT k=1 训练实验全部完成，registry 和 memory.md 已更新。

## 汇总表

| Experiment | Model | Seed | Status | train_loss | Steps | Epochs | Runtime | Checkpoint |
|---|---|---|---|---|---|---|---|---|
| d102_1_7b_rsft_k1_s42 | Qwen3-1.7B | 42 | **success** | 0.3063 | 567 | 3 | 15m | checkpoint-567 (279MB) |
| d102_llama_rsft_k1_s42 | LLaMA-3.1-8B | 42 | **success** | 0.3698 | 1107 | 3 | 43m | checkpoint-1107 (640MB) |
| d102_8b_rsft_k1_s42 | Qwen3-8B | 42 | **success** | 0.3877 | 1134 | 3 | 49m | checkpoint-1134 (666MB) |
| d102_8b_rsft_k1_s43 | Qwen3-8B | 43 | **success** | 0.3862 | 1134 | 3 | 48m | checkpoint-1134 (666MB) |

**k=1 vs k=3 对比：**
- 1.7B: k=1 loss 0.3063 vs k=3 loss 0.5234 (k=1 更低，但样本仅 3021 vs 9042)
- 8B: k=1 loss 0.3877 vs k=3 loss 0.3008 (k=1 更高)
- 8B seed 稳定性: s42=0.3877 vs s43=0.3862, delta=0.0015

无异常（无 OOM/NaN/early stop）。所有 checkpoint 文件完整，adapter_model.safetensors 大小合理。下一步需要 eval 验证 k=1 vs k=3 在 rel_f1 上的差异。

---
