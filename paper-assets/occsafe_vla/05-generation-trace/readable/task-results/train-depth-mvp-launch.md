# train depth mvp launch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_depth-mvp-launch_20260522T025804_result.json`
- **Structured JSON:** [`f97e4da606b27f5138e7.json`](../../sessions/f9/f97e4da606b27f5138e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 代码验证

**Bug fix（关键）：** `datasets.py` 中 `_preload_depth_data` (L134) 和 `_load_depth_label` (L370) 使用 `task_info["file"]`，但 depth_index.json 的 key 是 `"depth_file"`。已修复为 `task_info["depth_file"]`，同时修正变量名 `occ_path` → `depth_path`。不修此 bug 所有 depth 数据都会加载失败变全零。

**Task 9 处理：** 缺失的 task 是 `pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate`。代码已有 fallback 机制：`_load_depth_label` 对 missing task 返回全零 tensor + 打印一次 warning，不会 crash。该 task 的 depth loss 会被训练为预测零值（次优但可接受，仅影响 1/10 tasks，且 depth_loss_weight=0.01 带衰减）。

**Dry-run：** 2 步测试通过，`depth_loss=0.6730`（非 nan/inf），forward + backward 无报错。

### 训练状态

| 实验 | GPU | Seed | PID | tmux session | 初始 metrics |
|------|-----|------|-----|-------------|-------------|
| depth_s0 | cuda:1 | 42 | 13063 | depth_s0 | step 100: depth=0.2206, action=0.3359 |
| depth_s1 | cuda:2 | 43 | 13286 | depth_s1 | step 300: depth=0.1303, action=0.3691 |

速度 ~1.08 it/s，ETA ~13h（约 May 23 00:00 UTC 完成）。

### 磁盘空间

清理后 210G 可用（41% 使用率）：
- 删除 occ_s0、occ_s2 checkpoints（已完成评估，32G）
- 删除 occ_s1_fresh 早期 checkpoints 7500-25000（118G）
- occ_s1_fresh 保留 27500-45000 + base

**注意：** 210G 足够约 17500 步的 checkpoint（~7 对 × 14G/个 × 2 runs = 196G）。occ_s1_fresh 约 45 分钟内完成，之后可再释放 ~98G。后续可能需要额外清理老的 depth checkpoints 以支撑完整 50K 步训练。

---
