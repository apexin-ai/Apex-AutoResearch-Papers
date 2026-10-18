# ops cqa1 fix deploy abc

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-fix-deploy-abc_20260524T114609_result.json`
- **Structured JSON:** [`7c883fb2838bd90fc319.json`](../../sessions/7c/7c883fb2838bd90fc319.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项操作全部完成。汇报：

### A. Registry 修正 — eval_pi05_l2norm_k095_goal_seed42_postfix
- **conclusion** → `success`
- **metrics** → overall_sr=90.8% (454/500)，per-task 全部录入
- **checkpoint_path** → `N/A (eval only)`
- **log_path** → `/tmp/eval_pi05_l2norm_k095_goal_postfix.log`

### B. Long Random k=0.3 — GPU 1
- **exp_id**: `eval_pi05_random_k03_long_seed42_postfix`
- **PID**: 326332
- **tmux**: `eval_random_k03_long`
- **log**: `/tmp/eval_pi05_random_k03_long_postfix.log`
- **status**: RUNNING

### C. Spatial Random k=0.3 — GPU 2
- **exp_id**: `eval_pi05_random_k03_spatial_seed42_postfix_v2`
- **PID**: 326500
- **tmux**: `eval_random_k03_spatial`
- **log**: `/tmp/eval_pi05_random_k03_spatial_postfix_v2.log`
- **status**: RUNNING

cqa1 GPU 分布：GPU 0/3 被其他任务占用，GPU 1/2 刚部署 B/C。

---
