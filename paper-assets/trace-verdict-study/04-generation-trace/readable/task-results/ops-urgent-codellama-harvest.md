# ops urgent codellama harvest

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_codellama_harvest_20260518T030141_result.json`
- **Structured JSON:** [`c2d3030cf9fec9089562.json`](../../sessions/c2/c2d3030cf9fec9089562.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 状态
| GPU | Temp | Power | Util | VRAM |
|-----|------|-------|------|------|
| 0 | 29°C | 35W/600W | 0% | 49175/97887 MiB (空闲) |
| 1 | 73°C | 513W/600W | 100% | 36535/97887 MiB (训练中) |

---

### A) codellama13b_full_trace_tail256_seed42
- **进程**: dead (已结束)
- **训练**: 已完成
- **Eval**: 已完成
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail256_seed42/final/`
- **结果**:
```json
{
  "accuracy": 0.7790,
  "majority_baseline": 0.7151,
  "lift": 0.0639,
  "n": 1190,
  "pass_precision": 0.8559, "pass_recall": 0.8308, "pass_f1": 0.8432,
  "fail_precision": 0.6044, "fail_recall": 0.6490, "fail_f1": 0.6259
}
```

---

### B) codellama13b_full_trace_tail1024_seed42
- **进程**: dead
- **训练**: **启动即失败** — `python: can't open file '/root/trace-verdict-study/train.py': [Errno 2] No such file or directory`
- **Eval**: 未跑
- **Checkpoint**: 不存在 (目录都没创建)
- **问题**: 启动命令用了错误的 `train.py` 路径，从未开始训练

---

### C) codellama13b_full_trace_head2048_seed42
- **进程**: alive (GPU 1, PID 391758)
- **训练**: **404/444 steps (91%)**, 约 19 分钟后完成
- **Eval**: 未跑 (训练未完成)
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_head2048_seed42/` 下有 `checkpoint-148`, `checkpoint-296`

---

### 需要处理
1. **tail1024_seed42 需要重新启动** — 路径错误导致完全没跑。需要找到正确的 train.py 路径后重新提交。
2. **head2048_seed42 约 19 分钟后完成训练** — 完成后需确认 eval 是否自动运行，否则手动触发。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "accuracy": 0.779,
    "majority_baseline": 0.7151,
    "lift": 0.0639,
    "n": 1190,
    "pass_precision": 0.8559,
    "pass_recall": 0.8308,
    "pass_f1": 0.8432,
    "fail_precision": 0.6044,
    "fail_recall": 0.649,
    "fail_f1": 0.6259
  }
}
```

</details>

---
