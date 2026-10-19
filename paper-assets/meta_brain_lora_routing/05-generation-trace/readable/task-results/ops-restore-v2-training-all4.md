# ops restore v2 training all4

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restore_v2_training_all4_20260516T141407_result.json`
- **Structured JSON:** [`1aa544faffe7d7cc819d.json`](../../sessions/1a/1aa544faffe7d7cc819d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 卡全部确认跑起来了。

## 结果汇总

| GPU | 类型 | PID | 起始 step | 剩余 steps | 预计完成 |
|-----|------|-----|-----------|-----------|---------|
| 0 | universal | 835558 | 4000 | 6000 | ~8.3h (6000×5s/step) |
| 1 | spatial | 835698 | 1000 | 9000 | ~12.5h |
| 2 | visual | 835846 | 6000 | 4000 | ~5.6h |
| 3 | physical | 836032 | 6000 | 4000 | ~5.6h |

**GPU 状态**: 4 卡均 ~12.7 GB 显存, 99% 利用率, ~5s/step

**执行过程中的修复**:
1. 训练脚本不支持 resume → 给 `train_lora_expert.py` 打了 patch，加了 `--resume_from` 参数（PeftModel.from_pretrained 加载 adapter + 从 checkpoint step 恢复 global_step）
2. wandb 未配置 → 加了 `--no_wandb` 跳过

---
