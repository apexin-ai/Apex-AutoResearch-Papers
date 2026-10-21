# diag real occ data dryrun

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_real_occ_data_dryrun_20260520T123303_result.json`
- **Structured JSON:** [`131bb41714aed68cbbe8.json`](../../sessions/13/131bb41714aed68cbbe8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 metrics 文件（WandB disabled + log_freq=10 > 5 steps）。但核心验证已足够。

---

## 汇报

### 1. Tasks 2/3/8 完成状态

全部完成。PIDs 104228/104229/104234 已退出。

| task_id | task_name | demo 数 | 状态 |
|---|---|---|---|
| 0 | between_plate_ramekin | 50/50 | ✅ |
| 2 | from_table_center | 50/50 | ✅ |
| 3 | on_cookie_box | 50/50 | ✅ |
| 4 | in_top_drawer | 进行中 | 🔄 PID 104230 |
| 8 | next_to_plate | 50/50 | ✅ |

另外 5 个 occ 文件（tasks 1/5/6/7/9）是旧的损坏残留（bad object header），不在本次提取范围内。

### 2. 真实 occ 数据质量

| 指标 | 真实数据（4 tasks） | dummy 参考 | 判定 |
|---|---|---|---|
| occ_rate | 0.397–0.439 | 0.15 | ✅ 符合 30-50% |
| h_diff | 0.040–0.047 | 0.256 | ✅ 强空间结构 |
| v_diff | 0.037–0.041 | 0.256 | ✅ 同上 |
| t01_diff | 0–8 pixels | ~990 | ✅ 极高时间一致性 |
| shape | (89-151, 64, 64) | - | ✅ 分辨率正确 |
| dtype | bool | - | ✅ |

BEV 可视化显示清晰的桌面俯视结构（上半密集物体区，下半空闲），mid-trajectory 帧有碗移动的细微变化。数据质量优秀，远非随机噪声。

### 3. 5-step Dry-run 结果

- **occ_index.json**：已生成（9 tasks，跳过 wooden_cabinet 源文件损坏）
- **预加载**：4 files, 21,965 samples, 85.8 MB, 0.4s（跳过 5 个损坏/锁定文件）
- **occ_head 参数**：1,213,313（已创建并加入训练）
- **训练速度**：~1.2–1.9 s/step（合理）
- **完成状态**：5/5 steps 无报错退出
- **occ_loss 数值**：未能捕获（WANDB_MODE=disabled 且 log_freq=10 > 5 steps），但 FocalLoss(random_logits, real_target) ~0.8 确认计算路径正常
- **警告**：部分 batch 命中无 occ 数据的 task → fallback 返回全零，符合预期容错行为

### 4. 结论

**真实数据可用于正式训练。** 具体：

- 4 个 task 的 occ 数据质量确认合格（task 0/2/3/8）
- task 4 提取仍在进行
- 管线端到端跑通：预加载 → batch transform → occ_loss 计算 → 反向传播
- 正式训练前需要：
  1. 等 task 4 完成
  2. 删除 5 个损坏的 occ HDF5 文件（tasks 1/5/6/7/9 的残留）
  3. 重新提取 tasks 1/5/6/7/9（或仅用已有的 5 个 task 先跑）
  4. 重建 occ_index.json

---
