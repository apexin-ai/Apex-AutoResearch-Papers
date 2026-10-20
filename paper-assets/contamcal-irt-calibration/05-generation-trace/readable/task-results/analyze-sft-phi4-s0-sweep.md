# analyze sft phi4 s0 sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_sft_phi4_s0_sweep_20260520T145824_result.json`
- **Structured JSON:** [`febf98e3a1b525a69b44.json`](../../sessions/fe/febf98e3a1b525a69b44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## sft_phi4_s0_sweep 训练结果

### 状态：全部完成 (5/5 dosage, exit_code=0)

| Dosage | 开始时间 | 结束时间 | 耗时 | train_loss | mean_token_acc | entropy |
|--------|---------|---------|------|-----------|----------------|---------|
| d000 | 11:10 | 13:18 | 2h08m (7551s) | **1.184** | 0.7341 | 1.061 |
| d005 | 13:18 | 15:32 | 2h14m (7898s) | **1.185** | 0.7224 | 1.145 |
| d025 | 15:32 | 17:47 | 2h15m (7980s) | **1.186** | 0.7064 | 1.196 |
| d050 | 17:47 | 20:09 | 2h22m (8390s) | **1.189** | 0.7470 | 1.012 |
| d100 | 20:09 | 22:44 | 2h36m (9234s) | **1.192** | 0.7206 | 1.160 |

**总耗时**: ~11h34m (11:10 → 22:44)

### Checkpoint 路径

```
/root/autodl-tmp/exp001/checkpoints/phi-4_d000_s0/lora_adapter/
/root/autodl-tmp/exp001/checkpoints/phi-4_d005_s0/lora_adapter/
/root/autodl-tmp/exp001/checkpoints/phi-4_d025_s0/lora_adapter/
/root/autodl-tmp/exp001/checkpoints/phi-4_d050_s0/lora_adapter/
/root/autodl-tmp/exp001/checkpoints/phi-4_d100_s0/lora_adapter/
```

每个目录含 `.done` 标记文件、`train_config.json`、`lora_adapter/` 子目录。

### 配置确认
- lora_alpha=**32**, lora_r=16, lr=5e-5 (符合 C006 标准)
- seed=0, epochs=1, batch=1, grad_accum=16, max_seq_length=2048
- CUDA_VISIBLE_DEVICES=0 (显式设置)
- 无自动 eval（脚本仅含训练步骤）

### 观察
- train_loss 在 1.184–1.192 范围，随 dosage 增大略微上升（符合预期：更大 contamination dose → 更多数据 → 稍高 loss）
- 训练时长也随 dosage 单调增加（d000: 7551s → d100: 9234s），与数据量成正比
- 与 s42/s123 的 loss 趋势一致

### 结论：**SUCCESS**

三个种子 (s42, s123, s0) 的 Phi-4 SFT 全部完成，可进入下一步 eval + signal 计算流程。

---
