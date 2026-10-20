# cleanup kill reeval process

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_kill_reeval_process_20260520T052305_result.json`
- **Structured JSON:** [`c355da49b76e760f8c7b.json`](../../sessions/c3/c355da49b76e760f8c7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**1. deepseek_vota re-eval 残留进程：不存在**
`ps aux | grep "deepseek_vota"` 无匹配结果，cuda:1 上没有残留的 deepseek_vota re-eval 进程。无需 kill。

**2. codellama13b_ae_only_seed123 (PID=583496)**
- 状态：**运行中**，已运行 2h18m
- 训练进度：233/444 steps（~52%），~33s/it，预计还需 ~1h57m
- eval_results.json：尚未生成

**3. deepseek_exception_only_seed123_v2 (PID=591985)**
- 状态：**运行中**，已运行 23m39s
- 训练进度：100/444 steps（~23%），~14.7s/it，预计还需 ~1h24m
- eval_results.json：尚未生成

两个实验都在正常训练，GPU 0/1 各 98-100% 利用率。

---
