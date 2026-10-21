# infra check occ extraction

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-occ-extraction_20260520T074653_result.json`
- **Structured JSON:** [`9bf8ca505a1f69360b9e.json`](../../sessions/9b/9bf8ca505a1f69360b9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度汇总

### 进程状态
| Task | 状态 | 已完成 Demo | 进度 |
|------|------|------------|------|
| 0 | 运行中 | 1/50 | 2% |
| 1 | 运行中 | 1/50 | 2% |
| 2 | 运行中 | 0/50 | 0% (demo_0 处理中) |
| 3 | 运行中 | 1/50 | 2% |
| 4 | 运行中 | 1/50 | 2% |
| 5 | 运行中 | 1/50 | 2% |
| 6 | 运行中 | 0/50 | 0% (demo_0 处理中) |
| 7 | 运行中 | 0/50 | 0% (demo_0 处理中) |
| 8 | 运行中 | 1/50 | 2% |
| 9 | **未启动** | 0/50 | HDF5 下载中 |

### Task 9 下载问题
- 文件 `pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate_demo.hdf5` 仍在下载
- 当前大小：338M（`.downloading` 状态），日志报 421M，速度极慢
- **有 2 个重复的下载进程**（PID 46027 和 46708），都在下同一个文件，可能互相干扰

### 输出数据
- 实际输出目录：`/root/occsafe_vla/occ_data/`（不是 `/root/autodl-tmp/data/occ_labels/`）
- 当前 9 个 .hdf5 文件，共 9MB（每个文件 ~600KB，对应 1 个 demo 的数据）

### 时间估算
- 启动时间：15:23，当前 15:48，已运行约 25 分钟
- 处理速度：~1.75s/frame，每个 demo ~100 frames → ~3 分钟/demo
- 启动开销（加载环境、扫描 geom）约 15-20 分钟，实际提取刚开始
- **剩余：每个 task 约 49 demos × 3 min ≈ 2.5 小时**
- 预计 task 0-8 完成时间：**~18:15-18:30 CST**
- Task 9 取决于下载何时完成，之后再加 ~2.5 小时

### 需要关注
1. **Task 9 有 2 个重复下载进程**，建议 kill 掉一个（PID 46708 是后启动的），或者两个都 kill 重新用 `source /etc/network_turbo` 加速后重新下载
2. 整体进度刚起步，所有 task 都在前 1-2 个 demo，没有失败的

---
