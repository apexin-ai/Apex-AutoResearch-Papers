# ops full status and submit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_and_submit_20260516T174504_result.json`
- **Structured JSON:** [`99b51a4df2e7ea3d2739.json`](../../sessions/99/99b51a4df2e7ea3d2739.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
codellama13b_vota_seed42: 仍在跑, step 395/444 (89%), 预计 ~24 min 完成
GPU 0: 占用(PID 293829) — eval/evaluate.py exception_only_nomarker (Qwen-1.5B) → 未提交
GPU 1: 占用(PID 279483) — codellama13b_vota_seed42 训练 → 未提交
nomarker_seed123: 未提交（GPU 0 被 eval 占用）
nomarker_seed456: 未提交（GPU 1 被 vota 训练占用）
```

两张卡都在忙，等当前任务完成后再提交下一批。vota 训练约 24 分钟后结束，eval 占用内存较小(4.3GB)应该会更快完成。

---
