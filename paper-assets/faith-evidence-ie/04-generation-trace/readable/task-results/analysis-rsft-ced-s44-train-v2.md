# analysis rsft ced s44 train v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rsft_ced_s44_train_v2_20260523T091956_result.json`
- **Structured JSON:** [`b79e5270e2ff97c19103.json`](../../sessions/b7/b79e5270e2ff97c19103.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**conclusion: success**

| 项目 | 值 |
|---|---|
| checkpoint_path | `/root/autodl-tmp/rsft_output_ced_s44` |
| log_path | `~/runs/faith-evidence-ie/rsft_ced_s44_train_v2.log` |
| 最终 train_loss | 0.6226（平均），最后一步 0.6334 |
| 最终 mean_token_accuracy | 0.847 |
| 训练时长 | 2104s ≈ 35分钟 |
| 总步数 | 510 steps, 3 epochs |
| adapter 大小 | 528MB (adapter_model.safetensors) |

训练正常完成，日志末尾 `RSFT training complete.`，`EXIT_CODE=0`，无 error/exception。Checkpoint 目录包含完整的 adapter 文件（adapter_model.safetensors、adapter_config.json、tokenizer）和中间 checkpoint（350/400/450/500/510）。

---
