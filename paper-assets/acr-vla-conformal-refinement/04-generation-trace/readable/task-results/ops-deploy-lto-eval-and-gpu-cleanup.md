# ops deploy lto eval and gpu cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-lto-eval-and-gpu-cleanup_20260519T043316_result.json`
- **Structured JSON:** [`a468f0d94cdd5de7864a.json`](../../sessions/a4/a468f0d94cdd5de7864a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 报告

### 1. Kill 的实验

| exp_id (tmux) | GPU | 原因 |
|---|---|---|
| `eval-perdof-norm03-seed48` | cuda:0 | 与 K=5 seed47 共享 GPU 0 |
| `eval-obs-only-object-norm003-seed43` | cuda:1 | 释放 GPU 1 给 LTO eval |
| `eval-obs-only-norm003-seed46` | cuda:1 | 释放 GPU 1 给 LTO eval |
| `eval-obs-only-norm005-seed46` | cuda:2 | 释放 GPU 2 给 VLA-only baseline |
| `eval-obs-only-norm003-seed49-t16` | cuda:3 | 与 K=5 seed46 共享 GPU 3 |
| `eval-obs-only-norm003-seed45-t16` | cuda:3 | 与 K=5 seed46 共享 GPU 3 |

### 2. LTO eval 部署

- **exp_id**: `eval-lto-splitA-heldout`
- **GPU**: cuda:1 (独占)
- **held-out tasks**: ketchup, milk, orange_juice, salad_dressing, tomato_sauce
- **K=5, ε=0.2, seed=42, 10 rollouts**

### 3. VLA-only baseline 部署

- **exp_id**: `eval-lto-splitA-vla-only`
- **GPU**: cuda:2 (与 argmin baseline 共享，各 ~5.6GB，24GB 卡充裕)
- **同 held-out tasks, seed=42, 10 rollouts**

### 当前 GPU 布局 (bjb1-18228)

| GPU | 实验 |
|---|---|
| cuda:0 | K=5 seed47 (独占) |
| cuda:1 | LTO eval heldout (独占) |
| cuda:2 | argmin baseline + VLA-only baseline |
| cuda:3 | K=5 seed46 (独占，死进程释放中) |

---
