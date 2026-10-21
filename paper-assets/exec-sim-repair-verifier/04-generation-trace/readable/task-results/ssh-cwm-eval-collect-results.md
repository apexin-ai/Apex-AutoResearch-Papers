# ssh cwm eval collect results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-eval-collect-results_20260524T160221_result.json`
- **Structured JSON:** [`48a0ccf8c7f79084dbfe.json`](../../sessions/48/48a0ccf8c7f79084dbfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 已完成的 3 个 CWM ckpt300 reeval 任务

| 任务 | GPU | 总样本 | Accuracy | Unparseable | Unparseable% | F1-macro | 与CLS差异 | 完成时间 (CST) |
|------|-----|--------|----------|-------------|--------------|----------|-----------|----------------|
| CWM s42/ckpt300/seq2048 | 0 | 9784 | **68.20%** | 4754 | 48.59% | 63.87 | −15.43pp | 05-24 23:01 |
| CWM s456/ckpt300/seq2048 | 1 | 9784 | **66.09%** | 5979 | 61.11% | 60.29 | −17.54pp | 05-24 20:49 |
| CWM s123/ckpt300/seq2048 | 2 | 9784 | **63.91%** | 5366 | 54.84% | 55.19 | −19.72pp | 05-24 21:11 |

**3-seed 平均**: accuracy = **66.07%**, unparseable% = **54.85%**

对比参考值：
- CLS 8B repo-level: 83.63%
- 之前报的 CWM 8B: 66.48 ± 1.15%
- 本次 CWM 8B ckpt300 reeval: **66.07 ± 2.15%**（与之前的值一致）

---

## GPU 3 任务进度（CWM s42/ckpt6100/seq8192）

| 指标 | 值 |
|------|-----|
| 进度 | **9548/9784**（97.6%） |
| Running accuracy | **70.2~70.3%** |
| 速度 | ~4 samples / 20s |
| 剩余样本 | 236 |
| **预计完成** | **~20 分钟内**（约 00:25 CST） |

参考：同一 ckpt6100 之前在 seq4096 上的结果是 69.5%（unparseable 61.96%）。当前 seq8192 版本 running accuracy 70.2-70.3%，略有提升。

---

## 结果文件路径

| 文件 | 说明 |
|------|------|
| `/root/autodl-tmp/eval_results/cwm_8b_s42_ckpt300_reeval/eval_repo_cwm.json` | s42 完整结果 |
| `/root/autodl-tmp/eval_results/cwm_8b_s456_ckpt300_reeval/eval_repo_cwm.json` | s456 完整结果 |
| `/root/autodl-tmp/eval_results/cwm_8b_s123_ckpt300_reeval/eval_repo_cwm.json` | s123 完整结果 |
| `/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s42_ckpt6100_seq8192_eval/results_incremental.jsonl` | ckpt6100 增量结果（9548行） |
| `/tmp/cwm_s42_ckpt6100_seq8192.log` | ckpt6100 实时日志 |

---
