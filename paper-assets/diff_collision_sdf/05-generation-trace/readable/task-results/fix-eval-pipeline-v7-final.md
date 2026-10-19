# fix eval pipeline v7 final

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_pipeline_v7_final_20260521T201444_result.json`
- **Structured JSON:** [`89d1873db3c3ca809d1d.json`](../../sessions/89/89d1873db3c3ca809d1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 进程全速运行（CPU 499%, 2min elapsed）。每个 episode 约 2 分钟，Task 0 的 50 episodes 约需 100 分钟。无需继续等待。

---

## 汇报

### Bug 修复确认

| Bug | 状态 | 修改 |
|-----|------|------|
| **Bug 1: extra_delta_transform** | ✅ 已修 | `eval_safelibero.py` line 455-456: config 加载后强制 `extra_delta_transform=False`，并打印确认日志 |
| **Bug 2: next_ee 坐标** | ✅ 已修（修复前已存在） | Line 314 已经是 `next_ee = action[:3]`（绝对坐标），无需额外修改 |
| **Bug 3: 重复 no_refine 进程** | ✅ 已清理 | PID 235230, 236081 + 4 个额外残留旧 eval 进程（250563, 251373, 252143, 250971）全部 kill |

### Dry-run 结果（1 episode, Task 0）

- ✅ `[EVAL CONFIG] extra_delta_transform=False` — 确认生效
- ✅ 无 error/exception/traceback
- `collision_step=0`：初始步就碰撞 `white_storage_box_obstacle_1`（obstacle displacement 检测法，非 bug）
- `refine_count=0`：SDF 预测 min=0.665 远高于 margin=0.01，refiner 正确地未触发
- `smoothness=0.0045`，`max_displacement=0.822m`（obstacle 累计位移）

### A1 影响分析

A1 使用相同的 `eval_safelibero.py` 和 `load_policy()`。`extra_delta_transform=False` 修复在 model type 分支之前，**对 A1/baseline/A3 全部生效**。A1 checkpoint 在 westd-35807（`a1_sdf_object_pudding/`），如需 eval 需 SCP。

### 三组 Eval 提交状态

| 组 | 状态 | 位置 |
|----|------|------|
| **A3 refine (50ep×4tasks)** | 🟢 运行中 | tmux `eval_v8`, PID 256338 |
| **A3 no_refine (50ep×4tasks)** | ⏳ 排队 | A3 refine 完成后自动启动 |
| **Baseline (50ep×4tasks)** | ⏳ 排队 | A3 no_refine 完成后自动启动 |

三组串行在 cuda:1，通过 tmux session `eval_v8` 管理。

### Baseline checkpoint

✅ 已从 westd-35807 SCP 到 westd-45947（6.6GB model.safetensors + metadata.pt + assets/），耗时 ~25s（内网）。

### 监控命令

```bash
# 查看总体进度
tail -30 /root/autodl-tmp/eval_results/eval_v8_master.log

# 查看各组详细日志
tail -30 /root/autodl-tmp/eval_results/a3_object_pudding_refine_v8.log
tail -30 /root/autodl-tmp/eval_results/a3_object_pudding_no_refine_v8.log
tail -30 /root/autodl-tmp/eval_results/baseline_object_pudding_v8.log

# 预估总时长：~200 episodes/组 × 3组 × ~2min/ep ≈ 20h
```

---
