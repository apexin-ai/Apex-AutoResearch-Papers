# ops status check all gpu

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_all_gpu_20260518T155426_result.json`
- **Structured JSON:** [`5b3ee67d2902a2e56a28.json`](../../sessions/5b/5b3ee67d2902a2e56a28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. olmo_seed43 (gpu-6000pro-2 cuda:1) — 进行中

| 步骤 | 状态 |
|------|------|
| Step 1: finetune d0 | ✅ |
| Step 2: generate d1 | ✅ (5000/5000) |
| Step 3: finetune d1 | ✅ (loss=1.6473) |
| **Step 4: generate d2** | **进行中 318/5000 (6.4%)** |
| Step 5-8 | 待执行 |

**整体进度: ~40%**（8 步中完成 3 步，第 4 步刚开始）。OLMo-1B 生成速度较快，预计 d2 生成约 30-40 分钟；剩余 step 5-8（train d2 + gen d3 + feature extract + RF eval）再需约 1.5-2 小时。

---

### 2. qwen25_14b_scale_002 (gpu-6000pro-2 cuda:0) — 进行中

当前：**Phase 3.3b Generate d3 — 3354/5000 (67.1%)**

d0-d2 全部完成，d3 生成接近完成。之后还有 Phase 4（feature extraction）+ Phase 5（classification）。**整体约 85%**，预计 1-1.5 小时内完成。

---

### 3. qwen25_14b_scale_003 (westd-48862 cuda:0) — 进行中

当前：**Phase 3.3b Generate d3 — 1233/5000 (24.7%)**

d0-d2 全部完成，d3 生成中。之后还有 Phase 4 + Phase 5。**整体约 75%**，预计 2-3 小时内完成。

---

### GPU 使用总览

| 服务器 | GPU | 显存占用 | 利用率 | 状态 |
|--------|-----|----------|--------|------|
| gpu-6000pro-2 | cuda:0 | 32.4G / 97.9G | 87% | qwen25_14b_scale_002 |
| gpu-6000pro-2 | cuda:1 | 10.0G / 97.9G | 65% | olmo_seed43 |
| westd-48862 | cuda:0 | 32.4G / 97.9G | 92% | qwen25_14b_scale_003 |
| **westd-48862** | **cuda:1** | **0G / 97.9G** | **0%** | **空闲** |

westd-48862 的 cuda:1 完全空闲，可用于新实验。

---
