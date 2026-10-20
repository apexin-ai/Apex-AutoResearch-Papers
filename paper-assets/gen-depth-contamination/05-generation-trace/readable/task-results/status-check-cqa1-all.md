# status check cqa1 all

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status-check_cqa1-all_20260520T032953_result.json`
- **Structured JSON:** [`041cf146abd817d0b613.json`](../../sessions/04/041cf146abd817d0b613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
### 1. exp_cross_transfer_llama8b_to_qwen7b_v2
状态: 运行中 (PID 275366, cuda:0)
命令: python scripts/run_deberta_cross_transfer.py --train_model wiki_llama8b --test_model wiki_qwen7b --gpu 0
进度: 5-fold CV, Fold 2/5 进行中, Epoch 2 step 1200/1500
      Fold 0-1 已完成, 每 fold ~12min
预计完成: ~12:00 CST (约 28 分钟后)

### 2. exp_deberta_arxiv_qwen1b5
状态: 运行中 (PID 276486, cuda:1)
命令: python scripts/run_deberta_arxiv.py
数据可用性: 是, 13200 samples (2200 docs × 6 depths), 加载成功
进度: 5-fold CV, Fold 3/5 进行中, Epoch 1 step 200/660
      Fold 0-2 已完成, 每 fold ~6.5min
预计完成: ~11:45 CST (约 13 分钟后)

### 3. GPU 状态 (nvidia-smi)
cuda:0 - RTX 4090 D | 20613/24564 MiB | 96% util | PID 275366 (cross_transfer llama8b→qwen7b)
cuda:1 - RTX 4090 D | 18173/24564 MiB | 97% util | PID 276486 (deberta arxiv qwen1b5)
cuda:2 - RTX 4090 D | 0/24564 MiB     | 0% util  | 空闲
cuda:3 - RTX 4090 D | 0/24564 MiB     | 0% util  | 空闲
```

两个实验在服务重启后均已重新启动并正常运行，cuda:2/3 空闲可用。

---
