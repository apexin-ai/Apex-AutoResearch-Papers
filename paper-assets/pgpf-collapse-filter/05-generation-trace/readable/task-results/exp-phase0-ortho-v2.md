# exp phase0 ortho v2

**pgpf collapse filter** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase0_ortho_v2_20260513T062027_result.json`
- **Structured JSON:** [`b3a676d918d0e42d7e79.json`](../../sessions/b3/b3a676d918d0e42d7e79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**执行摘要：**
- 杀掉旧 `phase0_ortho` 进程（使用旧代码，Step 2 无批量生成/无进度日志）
- rsync 同步了 8 个 pgpf 源文件到服务器
- 写了新 `phase0_orthogonality.py`，关键修复：
  - Step 1: 训练后保存 checkpoint，重跑时自动加载跳过训练
  - Step 2: batch_size=8 批量生成 + attention_mask + 每 100 样本进度日志 + try/except 容错
  - Step 3: 双卡评分（ft model cuda:0, base model cuda:1）
  - Step 4+5: 相关矩阵 + scatter plots + heatmap
- 已提交为 `phase0_ortho_v2`（PID 10520），registry 状态 RUNNING

---
