# ops check ae only seeds progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_ae_only_seeds_progress_20260516T050128_result.json`
- **Structured JSON:** [`62892931d62df8a4eec4.json`](../../sessions/62/62892931d62df8a4eec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

| | ae_only_seed123 | ae_only_seed456 |
|---|---|---|
| **进程状态** | Running (PID 235494, GPU 0) | Running (PID 235571, GPU 1) |
| **训练进度** | **252/444 steps (57%)** | **222/444 steps (50%)** |
| **已运行** | ~1h21m | ~1h21m |
| **速度** | ~18.5s/step | ~19.0s/step |
| **剩余步数** | 192 steps | 222 steps |
| **预估剩余训练时间** | **~59 min** | **~70 min** |
| **预估训练完成** | ~约 50 分钟后 | ~约 1h10m 后 |

**注意事项**：
- 两个 tmux session 都是今天 **11:40** 创建的，实际只跑了约 1.5 小时，不是 15+ 小时。可能之前的实验被重启了。
- 训练完成后会自动链式执行 `eval/evaluate.py`，eval 结果会写入 `final/eval_results.json`。
- 目前各有一个 `checkpoint-148`（第 148 步的中间 checkpoint）。
- GPU 利用率均 100%，运行正常。

---
