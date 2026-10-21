# infra post restart gpu check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_post-restart-gpu-check_20260518T024313_result.json`
- **Structured JSON:** [`46ad23c14293531f25c7.json`](../../sessions/46/46ad23c14293531f25c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## GPU 状态报告

| GPU | 任务 | 状态 | 进度 | running_acc |
|-----|------|------|------|-------------|
| 0 | CLS v4 eval | **已完成** | 9784/9784 | 71.3% |
| 1 | CWM s42 eval | running | 3091/9784 (31.6%) | 56.8% |
| 2 | CLS s123 eval | running | 9240/9784 (94.4%) | 74.8% |
| 3 | CWM s123 eval | running | 2770/9784 (28.3%) | 62.3% |

### CLS v4 eval 结果 (GPU 0, 已完成)
- **Accuracy: 71.29%** (majority baseline: 72.96%, gap: -1.7pp)
- F1 macro: 44.39%
- F1 fail: 5.7% (P=25.5%, R=3.2%) / F1 pass: 83.1% (P=72.9%, R=96.5%)
- Confusion: TP=6890, FP=2561, FN=248, TN=85
- Unparseable: 247 (2.5%)
- 结果文件: `/root/autodl-tmp/eval_results/deepseek_cls_repo_v4_8192.json`

### 预计完成时间
- **CLS s123 (GPU 2)**: ~94% 完成，约 40 分钟内结束
- **CWM s42 (GPU 1)**: ~32%，约 20+ 小时
- **CWM s123 (GPU 3)**: ~28%，约 20+ 小时

### tmux sessions
- `cls-s123-eval-8192` (GPU 2)
- `cwm-s123-eval` (GPU 3)
- CWM s42 无 tmux（直接后台进程）

### 磁盘
- `/` (overlay): 21G/30G (69%)
- `/usr/bin/nvidia-smi` (数据盘): 398G/879G (48%)

---
