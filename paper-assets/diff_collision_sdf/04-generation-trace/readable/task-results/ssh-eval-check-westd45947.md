# ssh eval check westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_check_westd45947_20260521T233843_result.json`
- **Structured JSON:** [`694d91275f3d8b51b1b7.json`](../../sessions/69/694d91275f3d8b51b1b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### eval_refine (cuda:1, PID 263983) — 正在运行，无需重启

已经是 v9 配置：
- `TORCH_COMPILE_DISABLE=1` ✓
- `refined=0` (extra_delta_transform=False) ✓
- 无死锁，正常推进

**进度** (4 tasks × 50 eps):

| Task | 状态 | TSR | CAR |
|------|------|-----|-----|
| 0 orange_juice | 完成 | 0.0% | 96.0% |
| 1 chocolate_pudding | 完成 | 0.0% | 22.0% |
| 2 milk | 20/50 进行中 | - | - |
| 3 bbq_sauce | 待运行 | - | - |

**预计剩余**: ~2h（每 ep ~1.4min, 剩余 30+50=80 eps）

### a3_spatial (cuda:0, PID 191747)

spatial_bowl 训练 step 11531/30000 (38%), ~4s/step, 剩余约 20.5h。

### 待办

当前只跑了 A3 refine 一组。任务要求三组串行（A3 refine → A3 no_refine → baseline）。两个 checkpoint 都已就位：
- A3 refine: `.../a3_grad_refine_object_pudding/.../best` ✓
- Baseline: `.../baseline_object_pudding/.../best` ✓

refine eval 完成后需要启动后续两组。需要确认 "A3 no_refine" 具体指什么——是同一个 A3 checkpoint 但关闭某个 refine flag，还是另一个 checkpoint？

---
