# ops parallel clean reeval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_parallel-clean-reeval_20260523T132450_result.json`
- **Structured JSON:** [`05f8273e7f9bed632c83.json`](../../sessions/05/05f8273e7f9bed632c83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 路并行已启动并确认正常分配。

## 最终报告

### 当前 GPU 分配

| GPU | 内存使用 | 任务 | Chain PID | 预计完成 |
|-----|---------|------|-----------|---------|
| **0** | 18.3/97.9 GB | 训练 (mistral contam_25) + **clean_s6 → s7 → s8** | 141101 | ~100 min |
| **1** | 8.7/97.9 GB | **contam_15_s1** → clean → clean_s2 | 140751 | ~90 min |
| **2** | 8.7/97.9 GB | **clean_s3 → s4 → s5** | 140827 | ~90 min |
| **3** | 17.4/97.9 GB | 训练 (mistral contam_25_s2) + **clean_s9 → s10** → contam_5 mistral | 141486 | ~100 min |

### 已完成的 re-eval
- contam_50_s1 ✓ (21:28)
- contam_25 llama ✓ (21:32)
- contam_15_s2, contam_50_s2, contam_5 llama ✓ (更早)

### 正在进行
- **contam_15_s1**: GPU 1 重跑中（之前被误杀在 50%）
- **10 个 clean seeds**: 4 路并行（3+3+2+2 分配）

### 清理工作
- 杀掉了 14 个重复/错误分配的进程（主因：`eval_lz.py --gpu` 参数覆盖 `CUDA_VISIBLE_DEVICES`，导致 `CUDA_VISIBLE_DEVICES=1 --gpu 0` 的进程全跑到 GPU 0 上）
- 保留了两个正在训练的 mistral 进程

### 预计全部完成时间
~**100 分钟**（约 23:10 CST），远在 6 小时目标内。

监控命令：
```bash
cat /tmp/eval_clean_status.log  # 查看整体进度
tail -3 /tmp/eval_clean_gpu{0,1,2,3}.log  # 查看各 GPU 日志
```

---
