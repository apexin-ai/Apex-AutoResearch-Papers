# eval 3B d000 s42 gpu3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_3B_d000_s42_gpu3_20260514T002643_result.json`
- **Structured JSON:** [`9360acc53acd260cb062.json`](../../sessions/93/9360acc53acd260cb062.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 3 当前被占用**，无法立即提交。

当前 GPU 3 上运行的是：
- **PID 242591**: `evaluate.py` — 3B s123 eval (`Qwen2.5-3B_d000_s123`)
- 输出目录为空，刚开始跑

GPU 4 也在跑 1.5B s42 eval（PID 243300）。

两个方案：
1. **等 GPU 3 的 s123 eval 跑完**后再提交 s42 eval（可以用 nohup 写个等待脚本）
2. **换到其他 GPU**（GPU 1/2 各有 ~3.7GB 占用，34%/32% 利用率，剩余 ~21GB 够用）

你要哪个方案？

---
