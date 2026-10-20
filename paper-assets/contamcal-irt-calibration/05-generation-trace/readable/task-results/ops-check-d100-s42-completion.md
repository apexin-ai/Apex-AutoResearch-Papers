# ops check d100 s42 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-d100-s42-completion_20260518T172102_result.json`
- **Structured JSON:** [`e735bf294c5b07662a3b.json`](../../sessions/e7/e735bf294c5b07662a3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 项目 | 状态 |
|---|---|
| **训练完成** | 成功。日志末尾有 `Training complete.`，4159/4159 steps 全部完成 |
| **最终指标** | train_loss=**0.987**, mean_token_accuracy=**0.7452**, epoch=1.0, 总耗时 6384s (~1h46m) |
| **最后 log step 指标** | step 4150: loss=1.029, mean_token_accuracy=0.7604 |
| **Checkpoint 完整性** | 完整。关键文件均存在: |
| | `adapter_model.safetensors` (154MB) |
| | `adapter_config.json` (lora_alpha=**32**, r=16, dropout=0.05) |
| | `tokenizer.json` (10.9MB) + `tokenizer_config.json` |
| | `training_args.bin` + `README.md` + `chat_template.jinja` |
| | 子目录 `checkpoint-4159/` (最终 step checkpoint) |
| **cuda:0** | **空闲**，0MiB 显存占用，GPU-Util 0% |
| **其他 GPU** | cuda:1/2/3 均在使用中 (PID 42743, 38920, 36943) |

训练成功完成，checkpoint 完整，cuda:0 已空闲可分配新任务。

---
