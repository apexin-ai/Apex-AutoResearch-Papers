# ops diagnose sft 15B d025 s123 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-sft-15B-d025-s123-v2_20260515T133518_result.json`
- **Structured JSON:** [`8681be9057e3921e9d35.json`](../../sessions/86/8681be9057e3921e9d35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 cron 需要删除。

## 诊断报告：exp_001_sft_15B_d025_s123_v2

**结果：SUCCESS**

| 项目 | 值 |
|---|---|
| 训练状态 | 完成 (epoch 1.0, 3384/3384 steps) |
| train_loss | 1.2723 |
| mean_token_accuracy | 0.7466 |
| 训练时长 | 6730s (~1h52m) |
| throughput | 8.04 samples/s, 0.50 steps/s |
| Checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter/adapter_model.safetensors` (74MB) |
| 日志 | `/tmp/sft_15B_d025_s123_v2.log` |

**注意事项**：
- bitsandbytes 启动时报 `libnvJitLink.so.13` 错误，未影响训练（非致命）
- exit file 记录 exit code=1，时间戳早于训练完成时间，属于早期失败尝试的残留
- 未执行 merge（脚本未传 `--merge` 参数），如需 merged model 需另行执行

Registry 已更新为 DONE/success，checkpoint_path 和 log_path 已记录。

---
