# code d146 progress check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-progress-check_20260519T170415_result.json`
- **Structured JSON:** [`43faef9f5532af79de11.json`](../../sessions/43/43faef9f5532af79de11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D146 ProofFOL Pipeline 状态报告

### 1. Pipeline 正在运行
当前正在训练 **d146_pf_exec_s43**（第 2 个实验）。

### 2. 实验进度

| 实验 | 状态 | Step | 备注 |
|------|------|------|------|
| d146_pf_exec_s42 | **已完成** | 500/500 | 模型已保存（4 个 safetensors），无 classify.json |
| d146_pf_exec_s43 | **训练中** | 271/500 | checkpoint-250 已保存 |
| d146_pf_exec_s44 | 未开始 | — | — |
| d146_pf_isr_s42/s43/s44 | 未开始 | — | — |

### 3. GPU 状态
- 显存：**85,379 MiB / 97,887 MiB**（87%）
- GPU 利用率：**85%**

### 4. 训练指标（最新）
- **exec_s42 final**：reward=1.0, prove_rate=1.0, isr=0.0, step=500
- **exec_s43 current**：reward=1.0, prove_rate=1.0, isr=0.40, step=271

### 5. classify.json
D146 系列 **无 classify.json**。exec_s42 训练完成但尚未运行分类。可能 pipeline 设计为全部训练完后统一评估。

### 预估
exec_s43 剩余 229 步，按当前速度（271 步用了约 1 小时），预计 **~50 分钟后完成**。整个 pipeline（3 exec + 3 isr = 6 个实验）目前完成 1/6，正在跑 2/6。

---
