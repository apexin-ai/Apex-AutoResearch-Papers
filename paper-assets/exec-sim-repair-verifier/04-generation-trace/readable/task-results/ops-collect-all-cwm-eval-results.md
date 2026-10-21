# ops collect all cwm eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-all-cwm-eval-results_20260519T011844_result.json`
- **Structured JSON:** [`a10bbcaf3ccea1fc388a.json`](../../sessions/a1/a10bbcaf3ccea1fc388a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

```
=== SEETACLOUD ===

GPU 0 - Qwen3-8B CWM s42 ckpt-400 @4096:
  Status: running (pid 778334, started 08:11)
  Progress: 576/9784 (5.9%)
  Overall Accuracy: 65.10% (375/576)
  Parseable Accuracy: 38.83% (73/188)
  Unparseable: 388/576 = 67.4%
  Log running_acc: 65.0%

GPU 1 - DeepSeek CWM s42 best @4096:
  Status: running (pid 662946, started May18)
  Progress: 9451/9784 (96.6%)
  Overall Accuracy: 56.81% (5369/9451)
  Parseable Accuracy: 38.77% (1792/4622)
  Unparseable: 4829/9451 = 51.1%
  (no tee log, JSONL only)

GPU 2 - DeepSeek CWM s42 e3 @2048 (D131):
  Status: running (pid 734440, started May18 21:51)
  Progress: 3772/9784 (38.6%)
  Overall Accuracy: 65.93% (2487/3772)
  Parseable Accuracy: 38.86% (408/1050)
  Unparseable: 2722/3772 = 72.2%
  Log running_acc: 65.9%
  Files: eval.log (315KB), results_incremental.jsonl (5.9MB)

GPU 3 - DeepSeek CWM s123 @4096:
  Status: running (pid 668680, started May18 01:32)
  Progress: 8950/9784 (91.5%)
  Overall Accuracy: 61.77% (5528/8950)
  Parseable Accuracy: 41.19% (1267/3076)
  Unparseable: 5874/8950 = 65.6%
  Log running_acc: 61.8%

=== HOME ===

GPU 0 - DeepSeek CWM s42 e2 @2048 (D133):
  Status: running (pid 15876, started 16:48)
  Progress: 5044/9784 (51.6%)
  Overall Accuracy: 67.17% (3388/5044)
  Parseable Accuracy: 45.79% (642/1402)
  Unparseable: 3642/5044 = 72.2%
  Log running_acc: 65.6%
  Files: eval.log (254KB), eval_resume.log (351KB), results_incremental.jsonl (11.6MB)
```

**关键发现：**

1. **全部 5 个 eval 都在跑，无一完成。** GPU1 (s42 best @4096) 最接近完成 (96.6%)，GPU3 (s123 @4096) 次之 (91.5%)。
2. **Unparseable rate 极高 (51-72%)。** Unparseable 默认 pred=1，而数据集 label=1 占 ~73%，所以 overall accuracy 被 unparseable 大幅抬升。
3. **Parseable accuracy 才是真实信号：38-46%。** 其中 Home 的 s42 e2 @2048 parseable acc 最高 (45.79%)，s42 best @4096 最低 (38.77%)。
4. **s42 best @4096 的 unparseable rate 明显低于其他 (51% vs 65-72%)，** 反而导致 overall accuracy 最低 (56.8%)，因为少了 unparseable->1 的 "免费" 正确。

---
