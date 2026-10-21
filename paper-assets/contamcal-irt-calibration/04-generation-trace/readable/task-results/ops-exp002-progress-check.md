# ops exp002 progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp002-progress-check_20260514T104036_result.json`
- **Structured JSON:** [`ad0017ae263c93bbac48.json`](../../sessions/ad/ad0017ae263c93bbac48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-002 Signal Pipeline 状态报告

### 进程
- **PID 349740** (bash wrapper) / **349745** (run_batch.py) — 存活
- **PID 351640** — 当前活跃的 compute_signals.py 子进程，GPU 0 占用 2762 MiB

### 进度：3/9 已完成（全部失败），4/9 正在运行

| Task | Dosage/Benchmark | 状态 | 时间 |
|------|---------|------|------|
| 1/9 | d000/mmlu | FAIL | 18:32→18:36 |
| 2/9 | d000/gsm8k | FAIL | 18:36→18:38 |
| 3/9 | d000/arc_challenge | FAIL | 18:38→18:41 |
| 4/9 | d005/mmlu | **运行中** | 18:41→ |
| 5-9 | d005,d100 × 剩余 | 未开始 | — |

### 致命 Bug：全部 9 个 task 都会失败

**根因：** `signal_minkpp.py:96` — bfloat16 tensor 无法直接转 numpy：

```python
# 当前（崩溃）
return token_log_probs[0].cpu().numpy()

# 修复
return token_log_probs[0].cpu().float().numpy()
```

**影响：** 每个 task 按顺序计算 embedding → minkpp → selfcritique。embedding 成功产出，但 minkpp 崩溃导致整个 compute_signals.py 非零退出，selfcritique 也未执行。

### 已产出文件
仅 d000 的 3 个 embedding 信号文件（~7MB），无 minkpp、无 selfcritique。

### 预估
- 剩余 6 个 task 每个 ~3 分钟后崩溃，全部走完约 **20 分钟**
- 全部 9/9 都会标记 FAIL

### 建议操作
1. Kill 当前进程（让它跑完也行，反正会攒下 embedding 文件）
2. 修复 `signal_minkpp.py:96`：加 `.float()` 
3. 用 `--skip-completed` 重跑（需确认 run_batch.py 判断"完成"的逻辑——当前基于 exit code 标记 FAIL，可能不会跳过）

---
