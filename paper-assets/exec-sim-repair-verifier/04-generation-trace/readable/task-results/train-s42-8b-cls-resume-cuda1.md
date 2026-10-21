# train s42 8b cls resume cuda1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_s42-8b-cls-resume-cuda1_20260514T214716_result.json`
- **Structured JSON:** [`07828ba70db7dab6d3c9.json`](../../sessions/07/07828ba70db7dab6d3c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活（PID 295789，运行 1分48秒）。tokenize 70k 条 2048 长度样本预计需要 3-5 分钟。之后加载 8B 模型到 cuda:1 显存会升到 ~17GB。

**任务完成：**

| 项目 | 状态 |
|------|------|
| ckpt-600 | 存在 ✓ |
| cuda:1 | 空闲，已分配 ✓ |
| PID | 295789，运行中 ✓ |
| Registry | `repo-level-cls-8b-s42-resume` → RUNNING ✓ |
| 参数修正 | `--epochs 3`、`--dataloader_num_workers 0`、`--save_total_limit 35` ✓ |
| output_dir | `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/`（独立于原始训练）✓ |
| 日志 | `~/runs/exec-sim-repair-verifier/repo-level-cls-8b-s42-resume.log` |

当前正在 tokenize 数据，预计几分钟后模型加载上 GPU 开始从 step 600 resume 训练。

---
