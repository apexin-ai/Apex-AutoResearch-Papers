# ops diagnose sft 15B d005 s123 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-sft-15B-d005-s123-v2_20260515T133247_result.json`
- **Structured JSON:** [`54de5b3f4119b4b55239.json`](../../sessions/54/54de5b3f4119b4b55239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：**SUCCESS**

| 项目 | 值 |
|------|-----|
| 结论 | 训练成功完成 |
| 进度 | 3177/3177 steps (100%), epoch=1.0 |
| 耗时 | 1h46m53s |
| train_loss | 1.2639 |
| mean_token_accuracy | 0.6855 |
| checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter` |
| adapter 大小 | 73.9MB (`adapter_model.safetensors`) |
| 日志 | `/tmp/sft_15B_d005_s123_v2.log` |

Registry 已更新为 DONE/success，cron 已删除。

---
