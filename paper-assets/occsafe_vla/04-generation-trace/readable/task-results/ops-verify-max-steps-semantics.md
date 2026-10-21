# ops verify max steps semantics

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_max_steps_semantics_20260524T181149_result.json`
- **Structured JSON:** [`00d470ff9ce961fc7ac4.json`](../../sessions/00/00d470ff9ce961fc7ac4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 源码证据

文件: `/root/occsafe_vla/openvla-oft/vla-scripts/finetune.py`

相关代码（逐字摘录）:

```python
# Line 1159
with tqdm.tqdm(total=cfg.max_steps, leave=False) as progress:

# Training loop body:
gradient_step_idx = batch_idx // cfg.grad_accumulation_steps

log_step = gradient_step_idx if not cfg.resume else cfg.resume_step + gradient_step_idx

# Termination condition:
if log_step == cfg.max_steps:
    print(f"Max step {cfg.max_steps} reached! Stopping training...")
    break
```

解读: **max_steps 是总步数（绝对值）**，因为终止条件是 `log_step == cfg.max_steps`，而 `log_step = resume_step + gradient_step_idx = 20000 + gradient_step_idx`。训练将在 `gradient_step_idx == 30005` 时停止（此时全局步数 = 50005）。

## 当前进度

| 实验 | gradient_step_idx | 全局 log_step | 预期终止 step | 状态 |
|------|-------------------|---------------|-------------|------|
| ablation_occ_detach_s0_retrain | N/A | N/A | 50005 | **已崩溃** (exit code 1) |
| full_occ_ln_s1 | ~371 | ~20371 | 50005 | 正常运行 |
| full_occ_ln_s2 | ~369 | ~20369 | 50005 | 正常运行 |

注：tqdm 显示 `371/50005` 是因为 `total=cfg.max_steps` 但实际只会跑到 `30005/50005` 就终止——进度条不会到 100%，这是个**显示 bug**，但训练逻辑正确。

## 结论

**full_occ_ln_s1 和 full_occ_ln_s2 不需要干预**——max_steps=50005 是绝对终止点，行为正确，将在全局 step 50005 时停止。

**ablation_occ_detach_s0_retrain 需要干预**——已崩溃（PID 775880 对应的 `vla-scripts/finetune.py` 以 exit code 1 退出，时间 2026-05-25_01:44:40）。需要查看崩溃原因并重启。是否需要我排查这个崩溃？

---
