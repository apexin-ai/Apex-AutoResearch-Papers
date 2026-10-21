# monitor full server check loop26

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_full-server-check-loop26_20260518T003609_result.json`
- **Structured JSON:** [`9124d6172a8ffcd144a4.json`](../../sessions/91/9124d6172a8ffcd144a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

```
=== SEETACLOUD (all 4 jobs still running) ===

GPU 0 — CLS v4 (8192 seq): 8320/9784 (85.1%), running_acc=71.2%
  ETA: ~1.2h (~09:50 UTC)

GPU 1 — CWM s42: 2470/9784 (25.2%), running_acc=57.5%
  ETA: ~26h (~May 19 11:00 UTC)

GPU 2 — CLS s123 (8192 seq): 7320/9784 (74.8%), running_acc=74.9%
  ETA: ~2.7h (~11:15 UTC)

GPU 3 — CWM s123: 2147/9784 (21.9%), running_acc=62.1%
  ETA: ~28h (~May 19 12:30 UTC)

Disk: 185G/250G (74%)
```

```
=== HOME (GPU idle, all jobs completed) ===

3-shot func-level (test=1890):
  DeepSeek-6.7B:  Acc=59.95%  Pass_F1=44.13  Fail_F1=68.78  Unparse=0%
  Qwen3-8B:       Acc=68.78%  Pass_F1=64.46  Fail_F1=72.17  Unparse=0%

3-shot repo-level Qwen3-8B (test=9784):
  ⚠️ Acc=72.96%  Pass_F1=84.36  Fail_F1=0.0  Unparse=100%
  所有预测都 unparseable，默认为 pass → 实际等于 majority baseline

0-shot repo-level (test=9784):
  Qwen3-8B:       Acc=49.90%  Pass_F1=48.95  Fail_F1=50.81  Unparse=0%
  DeepSeek-6.7B:  Acc=48.54%  Pass_F1=64.70  Fail_F1=5.09   Unparse=8.7%

0-shot func-level Qwen3-8B (test=1890):
  Acc=68.73%  Pass_F1=65.50  Fail_F1=71.41  Unparse=0.32%
```

关键发现：
1. **CLS v4 和 CLS s123 的 8192 eval 今天内能完成**，目前 running_acc 分别为 71.2% 和 74.9%
2. **CWM 两个 eval 还需约 26-28 小时**（May 19 中午左右）
3. **3-shot repo-level Qwen3 结果无效** — 100% unparseable，所有输出都无法解析为 pass/fail，全部被默认为 pass，等效于 majority class baseline (72.96%)
4. Home 服务器 GPU 空闲，可安排新任务

---
