# ops cleanup and depth launch 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-and-depth-launch-10894_20260522T064745_result.json`
- **Structured JSON:** [`030510c4db9c16bd9511.json`](../../sessions/03/030510c4db9c16bd9511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报：任务已在先前 session 完成

**当前状态（westd-10894）**

1. **checkpoint 清理**：4 个目标目录（ablation_random_occ_s0/s1, ablation_occ_detach_s0/s1）已不存在。当前 `/root/autodl-tmp/checkpoints/` 仅剩 ablation_occ_detach_s2、ablation_random_occ_s2、depth_s2、depth_s3。磁盘 250G 已用 37G，**可用 214G (85% free)**。

2. **代码文件已就位**：
   - finetune.py: 55693 B
   - datasets.py: 23158 B
   - occ_head.py: 5159 B
   - data_utils.py: 7011 B

3. **depth_data 已就位**：9 个 task 的 HDF5 + depth_index.json，位置 `/root/occsafe_vla/depth_data/`。

4. **训练已运行**（registry 显示均为 RUNNING，updated_at 2026-05-22T07:01）：
   - **depth_s2** (cuda:2, seed=44, PID 942037)：step 100, depth_loss=0.1294, action_loss=0.3262, ~1.07 it/s, ETA ~13h
   - **depth_s3** (cuda:3, seed=45, PID 940106, master_port=29501)：step 113, depth_loss=0.2577, action_loss=0.3516, ~1.06 it/s, ETA ~13h

5. **GPU 占用**：cuda:0 (random_occ_s2) 99% / cuda:1 (occ_detach_s2) 99% / cuda:2 (depth_s2) 83% / cuda:3 (depth_s3) 84%，4 卡全负载，各 ~62GB 显存。

无需重复执行任何操作。

---
