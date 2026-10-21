# ops urgent gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-gpu-status-check_20260515T135408_result.json`
- **Structured JSON:** [`a84f3b9dc92e21040016.json`](../../sessions/a8/a84f3b9dc92e21040016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 进程状态总览

| GPU | PID | 实验名 | 运行时长 | 显存 | 状态 |
|-----|-----|--------|----------|------|------|
| 0 | 368823/368818 | cwm-rank32-ablation-v2 | ~1h23m (已结束) | 0 MiB (已释放) | **COMPLETED** ✓ |
| 1 | 295794 (wrapper: 295789) | repo-level-cls-8b-s42-resume | 16:05:59 | 27304 MiB | RUNNING |
| 2 | 266816 | repo-level-cwm-8b-conda-v4 | 20:09:50 | 30724 MiB | RUNNING |
| 3 | 367292 (子进程: 367297) | cwm8b-ckpt400-test-eval | 01:37:43 | 16994 MiB | RUNNING |

---

### cwm-rank32-ablation-v2 训练完成详情

**训练指标：**
- 总步数：1434 steps，3 epochs
- 最终 train_loss：**0.0152**（平均 train_loss：0.2536）
- eval_loss：**0.0688**
- 训练时长：5003s (~1h23m)

**评估结果（test set, 1890 examples）：**
- Overall accuracy：**87.0%**（+35.2pp vs majority baseline）
- Exact match rate：**83.4%**
- fail F1：87.1%，pass F1：86.9%
- MVP-B CRITERIA：**PASS**

**Checkpoints (`/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_rank32/`)：**
- `best/` — adapter_model.safetensors (90MB)
- `checkpoint-1434/`
- `checkpoint-478/`

**EXIT_CODE=0**

---

### 原始 nvidia-smi 输出

```
# --query-compute-apps (第1次查询时 GPU 0 还有进程)
368818, GPU-fc6e...(GPU 0), 13966 MiB
295794, GPU-9345...(GPU 1), 27304 MiB
266816, GPU-19c6...(GPU 2), 30724 MiB
367297, GPU-02eb...(GPU 3), 16994 MiB

# --query-gpu (第2次查询时 GPU 0 进程已退出)
0, NVIDIA GeForce RTX 5090, 0 MiB
1, NVIDIA GeForce RTX 5090, 27313 MiB
2, NVIDIA GeForce RTX 5090, 30733 MiB
3, NVIDIA GeForce RTX 5090, 17003 MiB
```

**GPU 0 现在空闲，可以调度新任务。**

---
