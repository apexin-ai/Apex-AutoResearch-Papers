# ssh emergency disk cleanup 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_emergency_disk_cleanup_35807_20260520T143427_result.json`
- **Structured JSON:** [`a032dc35f27afff3a603.json`](../../sessions/a0/a032dc35f27afff3a603.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。汇总：

---

## 结果

### 1. 磁盘清理前后对比

| | Used | Avail | Use% |
|---|---|---|---|
| 清理前 | 350G | 248K | **100%** |
| 清理后 | 248G | **103G** | 71% |

**释放空间：~102GB**

### 2. SAVE_TOTAL_LIMIT 修改确认
- **westd-35807**: `SAVE_TOTAL_LIMIT = 2` ✓
- **westd-45947**: `SAVE_TOTAL_LIMIT = 2` ✓

运行中的进程不受影响（常量已加载到内存），下次重启生效。

### 3. 三个实验存活确认

| PID | 运行时间 | CPU% | GPU 显存 |
|---|---|---|---|
| 95429 | 16h12m | 127% | 37358 MiB |
| 100319 | 16h00m | 124% | 37358 MiB |
| 185994 | 6h10m | 68% | 13376 MiB |

全部存活，GPU 正常占用。

### 4. 当前 checkpoint 占用

| 实验 | 占用 |
|---|---|
| a1_sdf_spatial_bowl_seed0 | 27G |
| baseline_object_pudding_seed0 | 110G |
| baseline_spatial_bowl_seed0 | 92G |
| **合计** | **229G** |

### 5. 剩余空间评估

- 可用空间：**103G**
- SAVE_TOTAL_LIMIT 改为 2 后，每个实验最多保留 2 个 checkpoint（~22G），但对运行中进程不生效
- 当前 baseline_object_pudding 已占 110G（约 10 个 checkpoint），baseline_spatial_bowl 占 92G — 这两个实验下次保存新 checkpoint 时磁盘会继续增长
- **风险**：运行中的进程仍用 SAVE_TOTAL_LIMIT=3，每次新保存 ~11G checkpoint，3 个实验同时保存一轮就是 ~33G，103G 可用空间大约撑 3 轮保存

**建议**：手动清理 baseline_object_pudding_seed0 和 baseline_spatial_bowl_seed0 中的旧 checkpoint（只保留最新 2 个），可再释放 ~150G，彻底消除磁盘风险。是否执行？

---
