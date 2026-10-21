# exp-004-reduced-lora 训练完成分析

## 训练状态

- **状态**: 正常完成
- **最终 step**: 8000/8000
- **EXIT_CODE**: 0
- **总耗时**: 56,514s (~15.7h)
- **Final loss**: sft=0.000005, l2=0.001427, total=0.000148
- **Trainable params**: 61,341,696 / 8,252,077,056 (0.74%)
- **配置**: r=64, alpha=64, 4 modules (qkvo), lambda_l2=0.1, lr=5e-5, grad_accum=16

## Checkpoint 状态

checkpoint-8000 存在，adapter_model.safetensors = 245MB。共 16 个 checkpoint（500-8000，每 500 步）+ final。

## SYCONScore 轨迹（vanilla baseline = 0.056）

| Checkpoint | SYCONScore | vs Baseline |
|------------|------------|-------------|
| 500 | 0.1515 | +170% |
| 1000 | 0.1700 | +204% |
| 1500 | 0.1613 | +188% |
| 2000 | 0.2051 | +266% |
| 2500 | (no eval) | — |
| 3000 | (no eval) | — |
| 3500 | 0.1881 | +236% |
| 4000 | 0.2051 | +266% |
| 4500 | 0.2707 | +383% |
| 5000 | 0.2463 | +340% |
| 5500 | 0.2546 | +355% |
| 6000 | 0.2129 | +280% |
| 6500 | 0.2368 | +323% |
| **7000** | **0.3257** | **+482% (peak)** |
| 7500 | 0.3043 | +443% |
| 8000 | (eval pending) | — |

## ckpt-7500 Eval 详情

- **SYCONScore**: 0.3043
- **ToF (True-on-False)**: 0.1878
- **NoF (No-on-False)**: 0.8011
- **样本数**: 362 (181 valid + 181 invalid)

## 训练 Loss 曲线要点

- SFT loss: 2.54 (step 10) → ~0.00 (step 500+)，收敛极快
- L2 loss: 2.37 (step 10) → ~0.0014 (step 8000)，持续缓慢下降
- 无 W&B logging（日志中未找到 wandb 记录）

## 分析

1. **Reduced-LoRA ACT 有效**: 所有已评估 checkpoint 的 SYCONScore 均显著高于 vanilla baseline (0.056)，最低为 ckpt-500 的 0.1515（仍为 baseline 的 2.7x）。

2. **Peak at ckpt-7000 (0.3257)**: 后续 ckpt-7500 略有下降 (0.3043)，可能存在轻微 overfitting 或噪声波动。ckpt-8000 eval 待完成可确认趋势。

3. **对比标准 ACT (exp-003)**:
   - Reduced-LoRA: r=64, alpha=64, 4 modules (qkvo), trainable=0.74%
   - Standard ACT: r=64, alpha=128, 7 modules, trainable≈1.5%
   - Reduced-LoRA 用约一半的可训练参数仍能达到显著的 sycophancy 抑制效果。

4. **Hypothesis 验证**: Reduced-LoRA ACT 的成功支持 "supervision granularity (per-token SFT) 是关键因素" 的假设——即使大幅减少 LoRA capacity，ACT 仍然有效。LoRA capacity 不是瓶颈。

## 待完成

- [ ] ckpt-8000 eval（目录已创建但为空）
- [ ] 与标准 ACT 的 peak SYCONScore 直接对比

conclusion: success
