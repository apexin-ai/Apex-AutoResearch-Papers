# analysis falcon3 d100 sft done

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_falcon3_d100_sft_done_20260522T124457_result.json`
- **Structured JSON:** [`977398718378d2292569.json`](../../sessions/97/977398718378d2292569.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练结果
- 状态: **成功** (epoch 1.0, 正常结束)
- 总 steps: **4159 / 4159** (checkpoint-4159 存在，415 条 loss 日志 × 每 10 步一条 = 4150 logged steps，完整)
- 最终 train loss: **1.0672** (train_loss 平均值)
- 最后一条 loss: 1.1171 (step ~4150), 倒数第二条: 1.0357 (step ~4140)
- Checkpoint 路径: `/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d100_s42/lora_adapter/`
- adapter_model.safetensors: **169 MB**
- lora_alpha: 32, r: 16, lr: 5e-5 (符合标准化配置)
- 训练时长: **4.87 小时** (17527 秒)
- 训练样本数: 66533, throughput: 3.80 samples/sec, 0.237 steps/sec
- mean_token_accuracy: 0.767
- W&B run ID: **未记录** (日志中无 wandb 痕迹，训练未开启 W&B logging)

## 异常
- W&B 未启用：训练日志中无任何 wandb 相关输出，此次训练未上报 W&B metrics
- 无其他异常，训练正常完成，checkpoint 完整（含 final adapter + checkpoint-4159 with optimizer/scheduler states）

---
