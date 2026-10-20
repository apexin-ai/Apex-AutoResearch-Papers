# ops westd process check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-process-check_20260516T010848_result.json`
- **Structured JSON:** [`0c02fcddd12a8acc7ff1.json`](../../sessions/0c/0c02fcddd12a8acc7ff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 进程状态报告

| GPU | 进程 | PID | 显存占用 | GPU利用率 | 任务详情 |
|-----|------|-----|---------|----------|---------|
| **cuda:0** | `eval_repo_cls.py` | 444502 | 17,600 MiB / 32,607 MiB | 77% | cls8b-s42-ckpt1000-test-mutation — 评估 `checkpoints_repo_cls_8b_s42_resume/checkpoint-1000`，启动于 08:54，已运行 ~15 min |
| **cuda:1** | `eval_repo_cls.py` | 444130 | 17,600 MiB / 32,607 MiB | 74% | cls8b-s42-resume-ckpt1000-test-mutation — 评估同一 checkpoint（resume 版），启动于 08:53，已运行 ~16 min |
| **cuda:2** | `train_repo_cwm.py` | 442200 | 29,264 MiB / 32,607 MiB | 95% | CWM 8B 训练，从 checkpoint-6100 恢复，启动于 08:41，已运行 ~28 min。**训练仍在进行中。** |
| **cuda:3** | `eval_repo_cwm.py` | 443221 | 21,124 MiB / 32,607 MiB | 87% | cwm8b-ckpt400-test-eval-v3，启动于 08:46，已运行 ~23 min |

### cuda:3 eval 进度
- 当前：**5464 / 9784**（55.8%）
- 其中 5287 条为增量恢复（跳过），新评估 177 条
- running_acc = **60.5%**（仅新评估样本的准确率）
- 速度：约 57 秒/batch(8)，预计还需 **~68 分钟**完成

### cuda:2 CWM 8B 训练 checkpoint 状态
最新 checkpoint：**checkpoint-6100**（2026-05-16 07:53）
保留的 checkpoints：400, 5800, 5900, 6000, 6100（save_total_limit=5，checkpoint-400 被保留）

### tmux sessions
- `ckpt_backup` — 创建于 May 14（自动备份脚本）
- `cwm8b-ckpt400-test-eval-v3` — 创建于 May 16 08:46（cuda:3 eval 进程）

**总结：4 张 GPU 全部满载运行，无空闲 GPU。**

---
