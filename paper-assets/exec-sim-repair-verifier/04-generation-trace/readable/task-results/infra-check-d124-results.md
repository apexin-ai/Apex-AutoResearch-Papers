# infra check D124 results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-D124-results_20260518T040028_result.json`
- **Structured JSON:** [`6dd2db933b217730af8a.json`](../../sessions/6d/6dd2db933b217730af8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## GPU 全局状态

| GPU | 利用率 | 显存 | 任务 | 进度 |
|-----|--------|------|------|------|
| **0** | 99% | 24.9/32.6 GB | CLS v5 **训练** (`train_unified.py --task cls`) | tmux 面板为空（可能在训练循环中无实时输出） |
| **1** | 50% | 17.5/32.6 GB | CWM s42 best eval (`eval_repo_cwm.py --checkpoint_dir .../best/`) | **3452/9784** (35.3%) |
| **2** | 54% | 17.3/32.6 GB | **D124** CWM s42 epoch2 eval (PID 700398) | **172/9784** (1.8%) |
| **3** | 52% | 17.5/32.6 GB | CWM s123 eval (`checkpoint-8844`) | **3121/9784** (31.9%), running_acc=61.7% |

## D124 状态

- **完成：否**，仍在运行
- 当前进度：**172/9784** (1.8%)
- running_acc: **67.4%**
- 启动时间：11:25，运行约 35 分钟
- 速率：约 12.5s/sample → 预计总时长 ~33 小时
- tmux session `cwm-s42-epoch2-eval` 存在，PID 700398 活跃

## 注意

- GPU 0 的 `deepseek-cls-repo-v5` tmux 面板无输出，但进程活跃（PID 698038, 24.8GB 显存, 99% 利用率），正在训练
- GPU 1 运行的是 CWM **best checkpoint** eval（不是 epoch3），进度 35.3%，无 eval.log（只有 jsonl）
- GPU 3 CWM s123 eval 进度 31.9%，running_acc=61.7%

---
