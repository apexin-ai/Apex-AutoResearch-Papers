# eval seed7 ood precollapse

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed7_ood_precollapse_20260521T211356_result.json`
- **Structured JSON:** [`a2400e9f981aedf886e7.json`](../../sessions/a2/a2400e9f981aedf886e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**阻塞**：exp029_seed7 原始 FSDP checkpoint（`/root/autodl-tmp/checkpoints/exp029-seed7/global_step_5/`，westd）已被删除，两台服务器均不存在。

当前可用的 seed7 相关 checkpoint：
- **exp029_seed7_high_kl** 在 bjb1：`/root/autodl-tmp/checkpoints/exp029-seed7-high-kl/global_step_5/actor/` 和 `global_step_7/actor/`
  - 但这是**不同实验**（KL coef=0.1 vs 原始 0.01），不是任务要求的原始 seed7 崩溃实验

westd 上现存 checkpoint 目录：
```
exp029-seed4, exp029-seed5, exp029-seed6, exp029-seed8, exp029_seed3
qwen_exp029_seed4_step15_hf, qwen_exp029_seed5_step10_hf, qwen_exp029_seed6_step15_hf
```

**选项**：
1. 任务无法按原计划执行（原始 seed7 checkpoint 已丢失）
2. 改用 exp029_seed7_high_kl step 5 做 OOD eval（已在 bjb1 上，省去传输，但 hypothesis 需调整为 high-KL 变体的 OOD 泛化）
3. 重新跑 exp029_seed7 训练获取 checkpoint（耗时 ~4h）

需要你决定如何处理。

---
