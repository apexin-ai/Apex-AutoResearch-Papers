# analysis v3 lora universal r48

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v3_lora_universal_r48_20260516T232557_result.json`
- **Structured JSON:** [`728f239e855463ff0ee9.json`](../../sessions/72/728f239e855463ff0ee9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
STATUS: success
METRICS:
  initial_train_loss: 1.6695 (step 50, earliest logged)
  final_train_loss: 0.4302 (step 9999)
  loss_reduction_ratio: 3.882 (1.6695 / 0.4302)
  total_steps: 9999 (of 10000 planned)
  training_time_minutes: ~173 min (04:30:44 → 07:23:11)
  checkpoint_path: /root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final
  checkpoints_saved: [step_1000, step_2000, step_3000, step_4000, step_5000, step_6000, step_7000, step_8000, step_9000, final]
  errors: 0
  tracebacks: 0
NOTES:
  - 训练正常完成，EXIT_CODE=0
  - LoRA rank=48, alpha=96, trainable params=11,059,200 (0.31%)
  - 与 r16 对比：final_loss 从 0.603 降至 0.4302，改善 28.7%
  - loss_reduction_ratio (3.882) 高于 r16 的 3.239，说明更高 rank 有更大的拟合能力
  - 训练时长 ~173 min，与 r16 的 170 min 接近（rank 增大对速度影响很小）
  - 日志以 50 步为间隔记录，实际初始 loss 可能比 1.6695 更高（step=50 已经经过 warmup）
```

---
