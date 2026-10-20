# ops fix cuda1 redeploy t15 a050 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-cuda1-redeploy-t15-a050-s43_20260523T030557_result.json`
- **Structured JSON:** [`57495992033db3a8374b.json`](../../sessions/57/57495992033db3a8374b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 registry 条目均已更新为 RUNNING。

## 汇报

### 1. 进程存活状态
- **PID 749427** (t15_a060_s43, cuda:0): **存活**，87% GPU, 11245 MiB, 306W
- **PID 750075** (t15_a050_s43, cuda:1): **存活**，89% GPU, 11245 MiB, 285W

### 2. 崩溃诊断
**无崩溃。** Director 报告的 cuda:1 "0%/0MiB" 是进程刚启动时的快照（模型尚未加载到 GPU）。`ps` etime 格式为 MM:SS（约 20 分钟），不是 HH:MM（20 小时），两个进程均在正常运行。

### 3. 无需重新部署
两个实验都在正常推进：
- **a060_s43** (cuda:0): gen_0 已完成（synthetic_data 11:12, metrics 11:14 CST），正在进入 gen_1
- **a050_s43** (cuda:1): gen_0 生成中，预计很快完成

### 4. 磁盘空间
- 根分区: 30G, 用 13G, 剩余 18G (42%)
- 数据盘 `/root/autodl-tmp`: **350G, 用 319G, 剩余 32G (92%)** ← 偏紧，但 T=15 两个实验预估 ~5-8GB 总占用，可以支撑

### 5. Registry 最终状态
- `scale_14b_t15_a060_s43_fp32`: **RUNNING** (新建, PID 749427, cuda:0, westd-17855)
- `scale_14b_t15_a050_s43_fp32`: **RUNNING** (已更新 spec, PID 750075, cuda:1, westd-17855)

---
