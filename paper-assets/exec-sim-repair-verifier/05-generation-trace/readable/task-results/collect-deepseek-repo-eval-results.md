# collect deepseek repo eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_deepseek-repo-eval-results_20260517T173009_result.json`
- **Structured JSON:** [`44235cf52c2965cc2660.json`](../../sessions/44/44235cf52c2965cc2660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部在工作了。CWM s123 eval 已成功启动并正在推理。

现在计算速率估算 ETA。

```
=== GPU Status ===
GPU 0: 92%, 31379/32607 MiB — CLS v4 s42 eval
GPU 1: 53%, 17345/32607 MiB — CWM s42 eval
GPU 2: 91%, 31379/32607 MiB — CLS s123 eval
GPU 3: 55%, 17343/32607 MiB — CWM s123 eval (刚启动)

=== CLS v4 s42 (GPU 0) ===
Status: RUNNING
Progress: 1000/9784 (~10.2%)
Running accuracy: 69.9%
Rate: ~1000 samples/hr (batch=4)
ETA: ~8.8 hours remaining

=== CWM s42 (GPU 1) ===
Status: RUNNING
Progress: 344/9784 (~3.5%)
Running accuracy: 61.0%
Rate: ~344 samples/hr (batch=1, ~12s/sample)
ETA: ~27 hours remaining

=== CLS s123 (GPU 2) ===
Status: RUNNING
Progress: 880/9784 (~9.0%)
Running accuracy: 74.1%
Rate: ~880 samples/hr (batch=4)
ETA: ~10 hours remaining

=== CWM s123 (GPU 3) ===
Status: JUST STARTED (by me)
Progress: 6/9784
Running accuracy: 66.7% (too early)
Checkpoint used: checkpoint-8844 (last epoch, largest step)
ETA: ~28 hours (same rate as CWM s42)
```

**关键发现：**

1. **CLS evals 速度合理** — batch_size=4, seq8192, 约 2.5 min/40 samples, 预计 ~9-10h 完成
2. **CWM evals 很慢** — batch_size=1, 需要生成 max_new_tokens=512, 约 12s/sample, 预计 ~27-28h
3. **CWM s123 之前未启动** — 已在 GPU 3 上用 checkpoint-8844 (last epoch) 启动
4. **初步精度趋势**：
   - CLS v4 s42: ~70% (偏低于 s123)
   - CLS s123: ~74% (较好)
   - CWM s42: ~61%

**注意事项：**
- CWM eval 的 27h ETA 意味着明天这时候还没跑完。如果需要加速，可以考虑增大 batch_size 或减少 max_new_tokens（但会影响准确性）
- CLS v4 s42 的 70% 对比 s123 的 74% 低了 4 个点，可能因为 v4 用的是 checkpoint-4422 而非 best（s123 用了 best）

---
