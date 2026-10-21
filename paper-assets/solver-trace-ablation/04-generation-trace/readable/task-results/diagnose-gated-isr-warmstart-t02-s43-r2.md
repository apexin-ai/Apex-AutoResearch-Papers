# diagnose gated isr warmstart t02 s43 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gated-isr-warmstart-t02-s43-r2_20260516T173633_result.json`
- **Structured JSON:** [`b655b6eb9f043589e79d.json`](../../sessions/b6/b655b6eb9f043589e79d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**root_cause**: 实验没有崩溃——已正常完成 300 步并保存最终模型。"没有 W&B metrics" 是因为配置文件 `configs/grpo_isr_warmstart_v3.yaml` 显式设置了 `no_wandb: true`。

**evidence**:
- `reward_log.jsonl` 有完整 300 行（step 1→300）
- 最终模型 safetensors（~15GB）和 checkpoint-300 已保存
- trainer_state.json 显示 `global_step: 300`
- 训练时间段：2026-05-16 16:52→17:23（约 31 分钟）
- 配置中 `no_wandb: true` 导致无 W&B 上报

**reward collapse 情况**（虽然没导致崩溃，但训练质量差）:
- 300 步中 219 步（73%）reward_mean=0.0
- τ=0.2 门槛过严，大部分 step 被 ISR gate 过滤，有效梯度信号极稀疏

**recommendation**: 
- 实验已完成，不需要重试
- 如需 W&B tracking，去掉 `no_wandb: true` 或改为 `no_wandb: false`
- 73% zero-reward 表明 τ=0.2 对 s43 确实过严（与已知结论一致：τ=0.15 的 s43 已成功），这个 run 的模型质量很可能不如 τ=0.15 版本

---
