# ops gpu audit and orphan check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-and-orphan-check_20260515T194427_result.json`
- **Structured JSON:** [`607bda05cc0d2d84ec1d.json`](../../sessions/60/607bda05cc0d2d84ec1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是完整审计结果。

---

## GPU 利用率审计报告

### 1. 逐服务器 GPU 占用

**bjb1-18228 (4× RTX 4090)** — 4/4 占满

| GPU | Util | VRAM | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 21% | 5.2/24G | 390936 | crm_perdof, object, seed42, default norm (r2) |
| 1 | 18% | 3.8/24G | 365930 | crm_perdof, object, seed43, norm=0.1 |
| 2 | 23% | 3.3/24G | 356495 | crm_obs_only, object, seed43, norm=0.1 |
| 3 | 22% | 3.3/24G | 356701 | reconvla, object, seed43 |

**bjb1-32546 (6× RTX 4090)** — 6/6 占满

| GPU | Util | VRAM | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 20% | 4.7/24G | 121334 | crm_obs_only, object, seed42, norm=0.03 |
| 1 | 23% | 4.7/24G | 111718 | vla_only (mean), object, seed43 |
| 2 | 21% | 4.7/24G | 114673 | crm_scalar, object, seed43, norm=0.1 |
| 3 | 23% | 5.7/24G | 148797 | crm_obs_only, object, seed43, norm=0.2 (r2) |
| 4 | 21% | 5.2/24G | 134103 | crm_obs_only, object, seed42, default norm |
| 5 | 22% | 5.2/24G | 127741 | crm_perdof, object, seed42, norm=0.2 |

**bjb2-28827 (6× RTX 4090)** — 6/6 占满

| GPU | Util | VRAM | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 19% | 5.2/24G | 105947 | crm_perdof, object, seed42, norm=0.03 |
| 1 | 18% | 5.2/24G | 109655 | crm_perdof, object, seed42, norm=0.05 |
| 2 | 19% | 5.7/24G | 140759 | **crm_perdof, object, seed42, norm=0.3 (r3)** |
| 3 | 19% | 5.7/24G | 144513 | crm_perdof, object, seed43, norm=0.2 (r3) |
| 4 | 18% | 5.2/24G | 101616 | crm_obs_only, object, seed42, norm=0.05 |
| 5 | 19% | 5.2/24G | 103034 | crm_obs_only, object, seed42, norm=0.3 |

**bjb2-40593 (1× RTX 4090)** — 1/1 占满

| GPU | Util | VRAM | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 12% | 2.5/24G | 227434 | crm_obs_only, spatial, seed42, norm=0.03 |

### 2. eval-mag-perdof-norm03-object-r3 排查

**实际在跑：YES**

- 服务器：**bjb2-28827**，GPU 2，PID **140759**
- 命令：`python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json`
- 证据：进程 cmdline 中包含 `perdof` + `norm 0.3` + `r3`，grep 确认匹配

**不是孤儿条目**，而是 registry 中缺失 server/pid/gpu_id 元数据。建议补全 registry 条目。

### 3. 异常/空闲 GPU

- **无空闲 GPU**：17 张卡全部有 python 进程占用，与 registry 17 个 RUNNING 实验吻合
- **GPU 利用率普遍偏低（12%–24%）**：这是 eval 负载的正常特征——GPU 推理和 LIBERO 环境仿真（CPU 密集）交替执行
- **bjb2-40593 利用率最低（12%）**：该卡跑的是 spatial benchmark，且 VRAM 占用仅 2.5G，可能是较轻的评测任务

---
