# ops prep bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-bjb2-40593_20260515T051551_result.json`
- **Structured JSON:** [`214743349d6243dd11d0.json`](../../sessions/21/214743349d6243dd11d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the summary:

### bjb2-40593 环境修复结果

| 项目 | 状态 |
|------|------|
| **Git repo** | 已修复 — `git init` + initial commit (38 files, 4347 lines) |
| **Python/CUDA** | Python 3.12.3, torch 2.10.0+cu128, CUDA=True, 1×RTX 4090 D (24GB) |
| **ML 包** | transformers 5.8.0, accelerate 1.13.0, datasets 4.8.4, einops 0.8.2 |
| **`from src.evaluate import *`** | OK (robosuite warning 可忽略) |

### 待解决问题

1. **CRM v3-norm checkpoints 不完整** — 只有 `perdof/crm_best.pt`，缺少 `obs_only/crm_best.pt` 和 `scalar_unc/crm_best.pt`。需要从其他服务器 scp 或重新训练。
2. **旧 CRM cache** — `/root/autodl-tmp/crm_cache/spatial/` 存在（含 partial 文件和 manifest），是旧版非 v3-norm 的缓存，未删除。
3. **Git 无 remote** — 当前是纯本地 repo，无 `.gitignore`（含 `__pycache__` 和 `.bak` 文件），无 remote URL。如需同步代码需手动设置 remote。

### 结论
GPU 环境可以立即跑实验，但仅限使用 `perdof` checkpoint 的实验。`obs_only` 和 `scalar_unc` 实验需要先补齐 checkpoints。

---
