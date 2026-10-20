# check code deberta and olmo final

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_code_deberta_and_olmo_final_20260520T060518_result.json`
- **Structured JSON:** [`808f3b3e910dae5f7fb5.json`](../../sessions/80/808f3b3e910dae5f7fb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 1. Code DeBERTa (exp_deberta_code_qwen1b5)
状态: **运行中**
- PID 285392 存活，已运行 ~36 min，GPU 3 占用 99% / 19.6 GB
- 5-fold CV（26400 train / 6600 val per fold）
- 当前进度：Fold 1/5, Epoch 3/3, step 1400/1650
- Fold 0 已完成，Fold 1 即将完成，还剩 Fold 2-4
- 每 fold ~19 min，预计还需 **~60 min**
- results 目录为空，无输出 JSON

### 2. OLMo 10k Bootstrap
状态: **前置 pipeline 运行中，bootstrap 尚未启动**
- PID 282889 存活，已运行 1h23m，GPU 2 占用 3.1 GB
- `run_pipeline.py --model_path OLMo-1B-hf --num_samples 5000 --max_depth 5`
- 数据生成完成：depth_0~5.jsonl 各 5000 行（最后文件写于 13:48）
- 当前阶段：feature extraction（`features.csv` 尚不存在）
- `results/olmo_c4_cont/` 为空
- 10k bootstrap 脚本 `olmo_c4_bootstrap_ci.py` 需 pipeline 输出的 `features.csv` 才能运行，目前是 **阻塞状态**

**结论**：两个任务都在运行中，registry 标记 RUNNING 是正确的。DeBERTa 预计还需 ~1h，OLMo pipeline 完成时间不确定（feature extraction 阶段），完成后还需单独跑 bootstrap CI。

---
