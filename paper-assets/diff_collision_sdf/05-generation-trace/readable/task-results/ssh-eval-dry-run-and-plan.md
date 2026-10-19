# ssh eval dry run and plan

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_dry_run_and_plan_20260520T202735_result.json`
- **Structured JSON:** [`c95135b56b9b509a2334.json`](../../sessions/c9/c95135b56b9b509a2334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. eval_batch.sh dry run — PASS
脚本语法正确，路径解析正常。14 个 eval job 中：
- 4 个 resolve 成功（baseline×2 + a1×2，均 seed0）
- seed1 全部 SKIP（未训练）
- A3 全部 SKIP（checkpoint 在 westd-45947，本地不存在）

自动选取的 checkpoint step：baseline_spatial→18000, baseline_object→20000, a1_spatial→18000, a1_object→4000

### 2. eval_safelibero.py import — PASS

### 3. norm_stats.json — PASS
不需要独立 symlink。norm_stats.json 嵌入在每个 checkpoint 的 `assets/` 子目录中（如 `18000/assets/safelibero_spatial/norm_stats.json`），policy 加载时自动读取。

### 4. Checkpoint 列表

**westd-35807:**
| 实验 | 可用 steps |
|------|-----------|
| baseline_spatial_bowl | 16000, 18000, best |
| baseline_object_pudding | 18000, 20000, best |
| a1_sdf_spatial_bowl | 14000, 16000, 18000, best |
| a1_sdf_object_pudding | 2000, 4000, best (**仍在训练，远离30K**) |

**westd-45947:**
| 实验 | 可用 steps |
|------|-----------|
| a3_grad_refine_spatial_bowl | 6000, 8000, 10000, best |
| a3_grad_refine_object_pudding | 8000, 10000, 12000, best |

### 5. eval_plan.md — 已写入
`/root/colliforce-vla/docs/eval_plan.md`

### 需注意的问题
- **A1 object_pudding 训练进度落后**：当前仅 step 4000，其他实验已到 18000-20000
- **A3 eval 需跨服务器 scp**：eval_batch.sh 期望 checkpoint 在本地 `/root/autodl-tmp/checkpoints/a3_grad_refine_*/`，训练完成后需从 westd-45947 拷贝过来

---
