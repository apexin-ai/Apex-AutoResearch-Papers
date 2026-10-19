# fix eval pipeline v6

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_pipeline_v6_20260521T201341_result.json`
- **Structured JSON:** [`511c59aec536429d6fd0.json`](../../sessions/51/511c59aec536429d6fd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval_v6_a3 正在加载模型。一切正常。

---

## 汇报

### 1. Bug B 修复 ✅
- **文件**: `/root/colliforce-vla/scripts/eval_safelibero.py` 行 314
- **修改**: `next_ee = current_ee + action[:3]` → `next_ee = action[:3]`
- openpi 使用 AbsoluteActions，action[:3] 本身就是绝对目标位置，不需要加 current_ee

### 2. Bug A 排查结果 ✅ — 根因找到并修复
两个子问题：

**A.1 — Settle 步数不足**：原代码只用 5 步 settle，但诊断发现多个障碍物（尤其 milk_obstacle_1）在 5 步后仍在大幅运动（z 从 0.96→0.14，位移 0.82m）。改为 50 步。

**A.2 — 跟踪了工作空间外的障碍物**：Level II 配置下，6 个障碍物中只有 1 个（moka_pot）在工作空间内（x,y ∈ [-0.5, 0.5], z > 0），其余被放在 10-20m 外。AEGIS 源码只跟踪工作空间内的障碍物，但我们跟踪了全部 6 个。添加了 AEGIS 标准的工作空间边界过滤。

**修复效果**：
- collision_step: 0 → **219**（从虚假碰撞变为真实碰撞）
- max_displacement: 0.822m → **0.033m**

### 3. Bug C 阈值调研 ✅
- 当前值：`COLLISION_THRESHOLD = 0.001`（1mm，L1 范数 `np.sum(np.abs(...))`）
- **AEGIS 源码确认**：`main_aegis.py` 行 370 使用完全相同的阈值和检测方式 `np.sum(np.abs(...)) > 0.001`
- **结论**：阈值与 AEGIS 标准一致，无需修改

### 4. Dry-run 结果

| 指标 | 修复前（v5） | 修复后（v10） |
|------|-------------|--------------|
| collision_step | 0（虚假） | **219**（真实） |
| max_displacement | 0.822m | **0.033m** |
| refine_count | 0 | 0 |
| sdf_min | 0.42 | **0.81** |
| TSR | 0% | 0% |
| CAR | 0% | 0% |

refine_count 仍为 0：SDF 预测值始终远高于 refine_margin（sdf_min=0.81 >> margin=0.01），所以 refinement 未触发。这可能说明 SDF decoder 预测偏高或 refine_margin 需要调高。

### 5. 全量 eval 状态
- **A3 refine (50ep)** — 已提交，tmux session `eval_v6_a3`，westd-45947 GPU 1，预计 ~2.5h
- **A3 no_refine (50ep)** — 排在 refine 后串行执行
- **Baseline (50ep)** — **被阻塞**：westd-35807 所有 4 GPU 都在训练中，无空闲 GPU。19GB 的 baseline checkpoint 也无法跨服务器传输到 westd-45947。需要等 westd-35807 有 GPU 空闲后再跑。

---
