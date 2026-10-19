# audit gpu collision k2mean

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu-collision-k2mean_20260526T134430_result.json`
- **Structured JSON:** [`0d911762e7a85898563d.json`](../../sessions/0d/0d911762e7a85898563d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。bjb1-32546 上 6 个 GPU 跑的是新部署的 pi05 v2-baselines r2 和 crm-k2 实验，每个 GPU 一个进程，无碰撞。

---

## GPU 碰撞审计报告

### 结论：当前无活跃 GPU 碰撞

所有 5 台服务器已检查完毕。没有任何 GPU 上存在多进程共享的情况。

---

### 各服务器状态

| 服务器 | GPU 数 | 活跃进程 | 碰撞 |
|--------|--------|----------|------|
| bjb1-18228 | 4x RTX 4090 | **0** (全部空闲) | 无 |
| bjb2-24035 | - | **0** | 无 |
| bjb2-28827 | - | **0** | 无 |
| cqa1-32758 | 6x RTX 4090 D | **6** (每 GPU 1 个) | 无 |
| bjb1-32546 | 6x GPU | **6** (每 GPU 1 个) | 无 |

---

### A. bjb1-18228 止血结果

**无需止血 — 所有进程已死亡。** PID 150245/150250/151593/153192 均不存在。

v2-baselines 的 goal s42 结果文件存在但 **全部 0% SR**（10 个 task 全部 0/20）。这 **不是 GPU 碰撞导致的**，是已知的 **pi05 模型加载 bug**（376 missing_keys，LM/projector 权重未加载），和之前 eval-pi05-vla-only-object-seed42/43/44 的 0% SR 完全一致。

K2mean goal s42 在 12:21 正常完成（96.5% SR），先于 v2-baselines 部署，未受影响。K2mean spatial/object/long 实验无输出文件，从未启动。

---

### B. cqa1-32758 cuda:0 审查

**无碰撞。** GPU 0 上只有 PID 216649（pi05 crm_obs_only long s44），独占。PID 392694（k2mean-goal-s42-r2）已不存在。GPU 1 上有新的 k2mean-goal-s42-r3（PID 429869）。

cqa1 6 个 GPU 进程身份：
- GPU 0: pi05 crm_obs_only long s44
- GPU 1: pi05 k2mean goal s42 r3
- GPU 2: pi05 adaptive object s43
- GPU 3-5: 其他 pi05 实验

---

### C. bjb2-24035 审查

无进程。`eval_long_vla_only_pi05_seed42_4090.json` 完成但 **0% SR** — 同样是 pi05 模型加载 bug。

---

### D. bjb1-32546 审查

6 个 GPU 各 1 个进程，无碰撞。当前进程是新部署的 pi05 实验：
- GPU 0-2: v2-baselines r2（spatial/object/goal s42）
- GPU 3-5: crm-k2 object s42/s43/s44

之前 registry 中的 SmolVLA RUNNING 实验（eval-crm-*-d149 等）进程已消失。

---

### 1. 干净的实验（独占 GPU，正常运行中）

**cqa1-32758** (6 个):
- pi05-crm-k2-long-s44 (GPU 0)
- pi05-k2mean-goal-s42-r3 (GPU 1)
- pi05-adaptive-object-s43 (GPU 2)
- pi05-adaptive-object-s44 (GPU 3)
- pi05-adaptive-long-s43 (GPU 4)
- pi05-adaptive-long-s44 (GPU 5)

**bjb1-32546** (6 个):
- pi05-vla-only-spatial-s42-r2 (GPU 0)
- pi05-vla-only-object-s42-r2 (GPU 1)
- pi05-vla-only-goal-s42-r2 (GPU 2)
- pi05-crm-k2-object-s42 (GPU 3)
- pi05-crm-k2-object-s43 (GPU 4)
- pi05-crm-k2-object-s44 (GPU 5)

### 2. 需要 invalidate 的实验

| 实验 | 服务器 | SR | 失败原因 |
|------|--------|-----|----------|
| pi05-vla-only-goal-s42-4090 | bjb1-18228 | 0% | pi05 模型加载 bug (376 missing_keys) |
| pi05-vla-only-long-s42-4090 | bjb2-24035 | 0% | pi05 模型加载 bug (376 missing_keys) |

注：spatial/object v2-baselines 在 bjb1-18228 上无输出文件，进程消失前可能未完成。

### 3. 已 kill 的进程

无。所有进程已自行终止。

### 4. 空闲 GPU（可用于重调度）

| 服务器 | 空闲 GPU |
|--------|----------|
| **bjb1-18228** | cuda:0, cuda:1, cuda:2, cuda:3 (全部 4 个) |
| **bjb2-24035** | 全部空闲 |
| **bjb2-28827** | 全部空闲 |

### 5. Registry 陈旧条目（标记 RUNNING 但无进程）

需要清理 RUNNING→DONE/FAILED 状态：
- `precompute-pi05-long-2048-r2` (bjb1-18228)
- `precompute-pi05-object-2048-r2` (bjb1-18228)
- `eval-supp-obj-reconvla-s47` (bjb2-28827)
- `eval-supp-goal-reconvla-s47` (bjb2-28827)
- `eval-supp-goal-k2mean-s47` (bjb2-28827)
- `eval-supp-goal-crm-norm005-s47` (bjb2-28827)
- `eval-supp-goal-adapt-tau025-s47` (bjb2-28827)
- bjb1-32546 上多个 SmolVLA eval-crm-*-d149 条目

---

### 核心结论

**不是 GPU 碰撞问题，是 pi05 模型加载 bug。** v2-baselines 在 bjb1-18228 和 bjb2-24035 上的 0% SR 与之前 eval-pi05-vla-only-object 的 0% SR 模式完全一致（376 missing_keys）。bjb1-32546 上已有人部署了 r2 re-runs，正在运行中。

---
