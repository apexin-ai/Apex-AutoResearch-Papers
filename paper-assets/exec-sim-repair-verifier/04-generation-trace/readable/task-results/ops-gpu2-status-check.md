# ops gpu2 status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu2-status-check_20260519T140905_result.json`
- **Structured JSON:** [`a9b9ae97ddf00e7c7491.json`](../../sessions/a9/a9b9ae97ddf00e7c7491.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 2：DeepSeek CWM s42 eval 正在跑

- **进程**: `eval_repo_cwm.py` (PID 833672)，DeepSeek-Coder-6.7B-Instruct，checkpoint-13266
- **进度**: **1156/9784 (11.8%)**，running_acc=**59.9%**
- 启动时间: 20:39，已跑约 1.5 小时
- 预估剩余: ~11 小时（每 4 样本约 20 秒）

### 全部 GPU 状态

| GPU | 利用率 | 显存 | 任务 | 进度 |
|-----|--------|------|------|------|
| **0** | 91% | 27.7/32.6 GB | Qwen3-8B CWM repo s42 eval (ckpt-400, seq4096) | 6984/9784 (71.4%), acc=63.9% |
| **1** | 0% | 0/32.6 GB | Qwen3-8B CLS repo s456 train v2（刚启动，加载中） | 刚加载 tokenizer |
| **2** | 85% | 28.2/32.6 GB | **DeepSeek CWM repo s42 eval** (ckpt-13266, seq4096) | 1156/9784 (11.8%), acc=59.9% |
| **3** | 0% | 0/32.6 GB | 空闲 | — |

Reviewer 之前报的 9.4% 和现在的 11.8% 对得上，同一个 eval 在正常推进。DeepSeek CWM 的 running_acc 约 59.9%，比 GPU 0 上 Qwen3-8B 的 63.9% 低约 4 个点。

---
