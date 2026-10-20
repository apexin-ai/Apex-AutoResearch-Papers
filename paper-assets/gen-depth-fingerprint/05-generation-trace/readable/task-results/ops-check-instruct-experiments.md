# ops check instruct experiments

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-instruct-experiments_20260515T154840_result.json`
- **Structured JSON:** [`40761cc343ae8b727d5c.json`](../../sessions/40/40761cc343ae8b727d5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. Qwen3-1.7B-Instruct — 已完成 ✓
- `review_p1c_instruct.json` 已存在（22:57 生成），4963 records，全 pipeline 完成
- **关键发现：instruct 微调反转了深度指纹方向**
  - hapax_ratio: instruct +0.48 vs base -0.67 (delta 1.15)
  - ttr: instruct +0.48 vs base -0.65 (delta 1.13)
  - entropy_mean: instruct +0.48 vs base -0.60 (delta 1.08)
  - `differential_depth_response: false`

### 2. OLMo-2-0425-1B-Instruct (GPU 0, PID 218484) — 生成中
- **进度**: 855 / ~5000 records (~17%)
- GPU 0: 50% util, 3638 MiB VRAM
- 速率 ~45 records/min → **预计还需 ~90 min，ETA ~01:20 UTC**
- Step 2 (features) 和 Step 3 (analysis) 尚未开始

### 3. Qwen3-0.6B-Instruct (GPU 2, PID 219116) — 生成中
- **进度**: 3343 / ~5000 records (~67%)
- GPU 2: 33% util, 1900 MiB VRAM
- 速率 ~186 records/min → **预计还需 ~9 min，ETA ~23:58 UTC**
- 小模型生成速度快很多，即将完成 Step 1

### GPU 总览
| GPU | 状态 | 温度 | VRAM | Util |
|-----|-------|------|------|------|
| 0 (5090) | OLMo instruct 生成 | 52°C | 3.6/32.6 GB | 50% |
| 1 (5090) | 空闲 | 29°C | 3 MiB | 0% |
| 2 (5090) | Qwen3-0.6B 生成 | 45°C | 1.9/32.6 GB | 33% |
| 3 (5090) | 空闲 | 27°C | 3 MiB | 0% |

---
