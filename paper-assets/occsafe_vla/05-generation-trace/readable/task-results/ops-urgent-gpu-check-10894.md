# ops urgent gpu check 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_gpu_check_10894_20260525T001837_result.json`
- **Structured JSON:** [`4146ce9b34b38fcf93b8.json`](../../sessions/41/4146ce9b34b38fcf93b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## 完整状态报告

### westd-10894 (4x RTX PRO 6000, 96GB)

#### Eval 结果: full_occ_ln_s0 ✅ 已完成
| 指标 | 值 |
|------|-----|
| **TSR** | **0.9300 (93.0%)** |
| **CAR** | **0.7660 (76.6%)** |
| Total episodes | 500 (10 tasks x 50) |
| Total collisions | 117 |
| Max displacement | 0.4916 |
| 结果文件 | `/root/occsafe_vla/artifacts/safelibero_libero_spatial_20260525_072028.json` |

#### GPU 状态

| GPU | 任务 | 状态 | 进度 | 预计剩余 |
|-----|------|------|------|----------|
| 0 | ablation_occ_detach_s0_retrain (resumed 20k) | 运行中 | 23775/50005 (48%) | ~7h |
| **1** | **空闲** | eval 已完成，无进程 | - | - |
| 2 | full_occ_ln_s1 (resumed 20k) | 运行中 | 23539/50005 (47%) | ~7h |
| 3 | full_occ_ln_s2 (resumed 20k) | 运行中 | 23598/50005 (47%) | ~7h |

#### ⚠️ 磁盘空间 - 严重警告
- 根分区: 21G/30G (70%)
- **autodl-tmp: 216G/250G (87%)**
- 所有 3 个训练任务原先在 **step 30000 保存 checkpoint 时因 `No space left on device` 崩溃**（01:38-01:44），已从 20k checkpoint 重启
- **这些 resumed 任务约 7h 后再次到达 step 30000，会再次触发 checkpoint 保存 → 大概率再次磁盘满崩溃**
- 需要立即清理磁盘空间（删除旧/不完整的 30k checkpoint 等）

---

### westd-34685 (4x RTX PRO 6000, 96GB)

#### GPU 状态

| GPU | 任务 | 状态 | 进度 | 预计剩余 |
|-----|------|------|------|----------|
| 0 | cutoff_45k_s1 (resumed 20k) | 运行中 | 10172/50005 (20%) | ~10.3h |
| 1 | cutoff_15k_s1 | 运行中 (PID 861222) | 日志未找到 | 需查日志位置 |
| 2 | cutoff_25k_s2 | 运行中 | 27116/50005 (54%) | ~5.9h |
| 3 | reverse_cutoff_s2 | 运行中 | 27063/50005 (54%) | ~6h |

- cutoff_45k_s1 同样在 step 30000 因磁盘满崩溃（05:27:01），已从 20k 重启
- cutoff_15k_s1 的日志不在 `/root/runs/occsafe_vla/cutoff_15k_s1.log`（只有 cutoff_15k_s0）
- 磁盘空间: 根 13G/30G (41%), autodl-tmp 216G/350G (62%) — **磁盘空间充足**

#### 最新 AUX loss 快照
| 任务 | step | occ_loss | action_loss |
|------|------|----------|-------------|
| cutoff_25k_s2 | 27100 | 0.0107 | 0.0879 |
| reverse_cutoff_s2 | 27000 | 0.1495 | 0.0854 |

---

### 空闲卡
- **westd-10894 GPU 1** — 空闲可用
- westd-34685 — 无空闲卡

### 紧急行动建议
1. **westd-10894 磁盘清理** — 必须在 ~7h 内完成，否则 3 个训练再次崩溃。需要清理 autodl-tmp 上的旧/损坏 checkpoint
2. **cutoff_15k_s1 日志** — 需要定位 GPU 1 上的进程对应的日志文件

---
