# ssh d019 verify and hdf5 check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d019-verify-and-hdf5-check_20260515T171326_result.json`
- **Structured JSON:** [`069b73056247663b6039.json`](../../sessions/06/069b73056247663b6039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. D019 脚本去重：✅ 已删除**
- `train_instruction_probes.py` — 不存在
- `train_goal_probe.py` — 不存在
- `analyze_goal_results.py` — 不存在

**2. HDF5 完整性：10/10 OK**
- 10 个文件全部可读，每个 50 demos，obs 含 `agentview_rgb/ee_ori/ee_pos`
- 文件大小 427MB–971MB，无异常

**3. 特征提取进度：**
- **trained: 6/10**（正在提取第 7 个 `put_the_bowl_on_top_of_the_cabinet`，~5%）
- **untrained: 5/10**（正在提取第 6 个 `put_the_bowl_on_the_stove`，~40%）
- 两个提取任务均在正常运行中，速度约 ~40 step/s

---
