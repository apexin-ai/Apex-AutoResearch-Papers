# ops cwm eval progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm-eval-progress-check_20260524T054634_result.json`
- **Structured JSON:** [`614666e5f374da9c2ba7.json`](../../sessions/61/614666e5f374da9c2ba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。以下是 4 路 CWM eval 状态：

```
GPU 0: [运行中] cwm_8b_s456 ckpt300 seq2048 reeval | 6176/9784 (63.1%) | acc=66.0% | ETA ~21:00
GPU 1: [运行中] cwm_8b_s42  ckpt300 seq2048 reeval | 4784/9784 (48.9%) | acc=68.5% | ETA ~23:10
GPU 2: [运行中] cwm_8b_s123 ckpt300 seq2048 reeval | 6016/9784 (61.5%) | acc=63.6% | ETA ~21:15
GPU 3: [运行中] cwm_8b_s42  ckpt6100 seq8192 eval  | 2364/9784 (24.2%) | 无日志    | ETA ~00:30 (May 25)
```

速度参考：
- GPU 0/1/2：~8 samples/57s（batch_size=8, seq2048）
- GPU 3：~11.6 samples/min（batch_size=4, seq8192），因为长序列所以更慢

GPU 3 是独立的 ckpt6100 + seq8192 配置，无 nohup.log（可能直接 tmux 或前台运行），进度从 results_incremental.jsonl 行数推算。

---
