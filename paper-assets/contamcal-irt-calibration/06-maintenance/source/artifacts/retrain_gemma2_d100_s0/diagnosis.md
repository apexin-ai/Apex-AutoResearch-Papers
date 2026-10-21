# Diagnosis: retrain_gemma2_d100_s0

## 结论：训练已成功完成，监控系统误判为 failed

### 根本原因

**False positive failure**。训练正常完成（exit code=0），但实验管理系统因以下原因将其标记为 failed：

1. **无 W&B 集成**：`train_sft.py` 不包含任何 wandb 代码，监控无法通过 W&B 检测运行状态
2. **无 sentinel 文件**：服务器上 `find -name "*.sentinel"` 返回空，训练脚本未写 sentinel
3. **进程已结束**：训练在 10:12:08 完成，监控 5 次检查时进程已不存在

三条检测通道全部失效 → "process dead 5× with no sentinel/W&B — auto-resolved as failed"

### 训练日志关键信息

```
启动时间: Thu May 21 06:04:33 CST 2026
完成时间: Thu May 21 10:12:08 CST 2026 (耗时 ~4h7m)
总步数:   4159/4159 (100%)
Exit code: 0
train_loss: 1.257
mean_token_accuracy: 0.71
epoch: 1.0
```

```
命令:
CUDA_VISIBLE_DEVICES=0 python train_sft.py \
  --model-name gemma-2-9b --data-path sft_dosage_100.jsonl \
  --output-dir gemma-2-9b_d100_s0 --seed 0 \
  --lora-r 16 --lora-alpha 32 --lr 5e-5 \
  --batch-size 2 --grad-accum 8 --gradient-checkpointing
```

### Adapter 验证

```
路径: /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s0/lora_adapter/
adapter_model.safetensors: 216MB (存在)
adapter_config.json: lora_alpha=32, r=16 (正确)
checkpoint-4159/ 目录存在
脚本自验证: "SUCCESS: adapter verified"
```

### GPU cuda:0 当前状态

**空闲**。0MiB 显存占用，0% 利用率。训练已结束，无残留进程。

(GPU 1 有其他进程 PID 455006 占用 42902MiB，与本实验无关)

### 建议修复方案

1. **将实验状态从 failed 改为 completed** — 训练产出完整，无需重训
2. **后续任务可直接使用该 checkpoint** 进行 eval / compute_signals
3. **长期修复**：对 Gemma-2 训练脚本添加 sentinel 文件写入或 W&B 集成，避免监控盲区再次触发误判
