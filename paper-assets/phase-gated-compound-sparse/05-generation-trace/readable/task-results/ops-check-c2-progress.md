# ops check c2 progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_c2_progress_20260514T180050_result.json`
- **Structured JSON:** [`15a8c36bb6dedbce8e0f.json`](../../sessions/15/15a8c36bb6dedbce8e0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

```
c2_n500_deepseek:
  进程状态: alive (PID 130124 gpu0, PID 130263 gpu1)
  条件进度: imp_s015 470/500, imp_s020~s030 0/500 | rand_s015 495/500, rand_s020~s030 0/500
  当前在跑: imp_s015 (gpu0), rand_s015 (gpu1, 即将完成)
  速率: ~1.8-1.9 prob/min
  预估 ETA (全部完成): 2026-05-15 ~16:10 UTC

c2_qw_n500:
  进程状态: alive (PID 131864 gpu2, PID 132002 gpu3)
  条件进度: imp_s015 357/500, imp_s020~s030 0/500 | rand_s015 374/500, rand_s020~s030 0/500
  当前在跑: imp_s015 (gpu2), rand_s015 (gpu3)
  速率: ~1.4-1.5 prob/min (比 DeepSeek 慢 ~25%)
  预估 ETA (全部完成): 2026-05-15 ~21:08 UTC
```

另外注意到 GPU3 上还有一个 c5b_pilot 进程 (PID 153367) 刚启动 ~5 分钟，在跑 `run_c5b_pilot.py --sparsity 0.25`，与 qw_rand (也声明 gpu 0 / CUDA_VISIBLE_DEVICES=3) 可能存在 GPU 显存竞争。

---
