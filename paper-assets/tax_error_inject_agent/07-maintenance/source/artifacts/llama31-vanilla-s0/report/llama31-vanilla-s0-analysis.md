# llama31-vanilla-s0 训练分析

## 状态：✅ 训练成功完成

## 基本信息
- 模型: Meta-Llama-3.1-8B-Instruct + LoRA (rank=16)
- 数据: sft_vanilla_v4.jsonl (4358 条)
- 配置: 3 epochs, batch_size=4, grad_accum=2, lr=1e-4, max_len=4096, seed=0
- 服务器: autodl-5090, 单卡, bf16, gradient_checkpointing

## Checkpoint
- 最终: `/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635`
- Epoch 1: checkpoint-545
- Epoch 2: checkpoint-1090
- Epoch 3: checkpoint-1635

## 关键 Metrics

| Metric | Step 10 | Epoch 1 (step 540) | Epoch 2 (step 1090) | Epoch 3 (step 1630) | Final avg |
|--------|---------|---------------------|----------------------|----------------------|-----------|
| loss | 1.102 | 0.481 | 0.362 | 0.273 | 0.398 |
| token_acc | 0.715 | 0.840 | 0.871 | 0.897 | 0.909 |

## 训练时长
- 总时间: 1h 9m 19s (4158.6s)
- 速度: 2.54 s/it, 3.14 samples/s
- 总步数: 1635
- GPU hours: ~1.16h

## 异常/警告
- bitsandbytes 加载警告 (libnvJitLink.so.13 缺失)，未影响训练
- 无其他异常，loss 曲线正常单调收敛
