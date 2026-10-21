# diagnose gemma2 d100 s123 exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gemma2-d100-s123-exit_20260520T051813_result.json`
- **Structured JSON:** [`8b1c8b2f612c25bacd7c.json`](../../sessions/8b/8b1c8b2f612c25bacd7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：训练成功完成。**

| 项目 | 状态 |
|------|------|
| PID 246861 | 已退出（正常结束） |
| 训练进度 | 4159/4159 steps, epoch=1.0 |
| train_loss | 1.256 |
| mean_token_accuracy | 0.7387 |
| lora_alpha | 32（C006 合规） |
| Checkpoint | `/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s123/lora_adapter/` (891MB, 含 adapter_model.safetensors + adapter_config.json + checkpoint-4159) |
| .done 标记 | 存在 |

Registry 已更新：status=DONE, conclusion=success。

**westd cuda:3 当前空闲（0% utilization, 0 MiB memory），可接新任务。**

---
