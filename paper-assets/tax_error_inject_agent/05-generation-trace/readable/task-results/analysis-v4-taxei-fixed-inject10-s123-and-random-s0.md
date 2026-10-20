# analysis v4 taxei fixed inject10 s123 and random s0

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-fixed-inject10-s123-and-random-s0_20260515T184908_result.json`
- **Structured JSON:** [`d5f0ac953ee3dbc99aa7.json`](../../sessions/d5/d5f0ac953ee3dbc99aa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。汇总如下：

---

## v4-taxei-fixed-inject10-s123
- **状态**: 成功 (EXIT_CODE=0)
- **最终 loss**: 0.3097 (step 1635)，train_loss 均值 = 0.4234
- **Epoch loss 趋势**: ep1=0.4376 → ep2=0.3488 → ep3=0.3097
- **训练时长**: 58 min 17s (3496.6s)
- **Checkpoint**: `/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/` — 1.5G，含 checkpoint-545/1090/1635（3 epochs 全保存）
- **W&B run ID**: 无（日志中无 wandb 记录）
- **异常**: bitsandbytes libnvJitLink.so.13 加载警告（不影响训练）

## v4-random-fixed-inject10-s0
- **状态**: 成功 (EXIT_CODE=0)
- **最终 loss**: 0.2760 (step 1635)，train_loss 均值 = 0.4227
- **Epoch loss 趋势**: ep1=0.4941 → ep2=0.3394 → ep3=0.2760
- **训练时长**: 58 min 51s (3530.8s)
- **Checkpoint**: `/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/` — 1.5G，含 checkpoint-545/1090/1635（3 epochs 全保存）
- **W&B run ID**: 无（日志中无 wandb 记录）
- **异常**: 同上 bitsandbytes 警告（不影响训练）

## 对比分析

| 指标 | TaxEI (s123) | Random (s0) |
|------|-------------|-------------|
| 平均 train_loss | 0.4234 | 0.4227 |
| Epoch 1 loss | 0.4376 | 0.4941 |
| Epoch 3 loss | 0.3097 | 0.2760 |
| Token acc (最终) | 0.888 | 0.907 |
| 训练时长 | 58m17s | 58m51s |

- 两个实验的平均 train_loss 几乎相同（0.423 vs 0.423），在参考范围 0.4-0.8 内正常偏低
- Random 实验 epoch 1 起始 loss 更高（0.494 vs 0.438），但 epoch 3 收敛更低（0.276 vs 0.310），收敛幅度更大
- 两者最终 token accuracy 都在 ~89-91%，Random 略高
- 无异常模式，训练正常收敛

---
