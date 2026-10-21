# ops gpu status and results pull

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_and_results_pull_20260525T090807_result.json`
- **Structured JSON:** [`6b8b3d779af906825fb3.json`](../../sessions/6b/6b8b3d779af906825fb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

---

### 1. westd-35807 — GPU 状态

| GPU | 型号 | 利用率 | 显存占用 | 状态 |
|-----|------|--------|----------|------|
| 0 | RTX PRO 6000 (96GB) | 46% | 8.1 GB | eval s1_l005 (port 8000) |
| 1 | RTX PRO 6000 (96GB) | 0% | 8.1 GB | eval s1_l01 (port 8001) |
| 2 | RTX PRO 6000 (96GB) | 0% | 8.1 GB | eval s2_l005 (port 8002) |
| 3 | RTX PRO 6000 (96GB) | 0% | 8.1 GB | eval s2_l01 (port 8003) |

### 2. 30K Eval 进度（均在运行中，未完成）

4 个 tmux session 于 13:25 启动，输出目录已创建但结果 JSON 尚未写入。

| Eval | 当前进度 | 速度 | 预计完成 |
|------|---------|------|---------|
| s1_l005 | **60/200** (30%) | ~40s/ep | ~18:40 |
| s1_l01 | **56/200** (28%) | ~39s/ep | ~18:40 |
| s2_l005 | **50/200** (25%) | ~37s/ep | ~18:40 |
| s2_l01 | **47/200** (24%) | ~44s/ep | ~19:00 |

**全部约 18:40-19:00 完成。**

### 3. OpenVLA 下载状态

**已完成。** aria2 日志显示 `ALL_DOWNLOADS_DONE`，无 aria2 进程运行。`.aria2` 文件是残留元数据，可清理。

| 文件 | 大小 |
|------|------|
| model-00001-of-00003.safetensors | 6.5G |
| model-00002-of-00003.safetensors | 6.5G |
| model-00003-of-00003.safetensors | 1.1G |
| config.json + 其他 | ~153K |

### 4. westd-45947 — LoRA Baseline 训练

| GPU | 利用率 | 显存占用 | 任务 | 进度 | ETA |
|-----|--------|----------|------|------|-----|
| 0 | **100%** | 27.1 GB | lora_s0 (seed 0) | **19468/30000 (65%)** | ~13.5h → **May 26 ~06:30** |
| 1 | **100%** | 27.1 GB | lora_s1 (seed 1) | **19473/30000 (65%)** | ~13.5h → **May 26 ~06:30** |

两个 seed 均从 step 16800 resume（12:40 启动），速度 ~4.62 s/step，loss ~0.01。

---
