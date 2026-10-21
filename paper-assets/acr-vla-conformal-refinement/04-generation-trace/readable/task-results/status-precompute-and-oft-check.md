# status precompute and oft check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_precompute-and-oft-check_20260522T164921_result.json`
- **Structured JSON:** [`d876039c15a24a47bb2f.json`](../../sessions/d8/d876039c15a24a47bb2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### Part 1: SmolVLA Wrapper Precompute (bjb2-28827)

`crm_cache_smolvla_k10/` — **3 个 suite 已完成，long 未开始**：

| Suite | Partials | Merged Files | 状态 |
|-------|----------|-------------|------|
| spatial | 48 (0→24000) | obs_features.pt, k_samples.pt, expert_actions.pt | ✅ 完成 |
| goal | 49 (0→24500) | obs_features.pt, k_samples.pt, expert_actions.pt | ✅ 完成 |
| object | 57 (0→28500) | obs_features.pt, k_samples.pt, expert_actions.pt | ✅ 完成 |
| **long** | — | — | ❌ 目录不存在 |

### Native cache (`crm_cache_lerobot_k10/`)
空目录，无输出。

### bjb2-28827 GPU 当前用途
GPU 3-5 正在跑 **pi05 goal precompute**（不是 SmolVLA），3 shard 并行，每卡 ~9.9GB：
```
python src/train_crm.py --precompute --benchmark goal --K 10 --model pi05 --cache_dir /root/autodl-tmp/crm_cache_pi05/
```
GPU 0 有一个 tmux session `eval-pi05-crm-spatial-seed42`（当前空闲）。

---

### Part 2: OFT LIBERO fix (bjb2-40593)

GPU 空闲（0%, 3 MiB）。`quick_eval.py` (PID 87169) 刚启动就 **崩溃了**：

```
ValueError: ObservationProcessorStep requires an observation in the transition.
```

出错位置：Task 0 ("pick up the alphabet soup and place it in the basket")，在 `env_preprocessor(batch)` 调用时。看起来 LIBERO env 返回的 transition 缺少 observation 字段，processor pipeline 拒绝处理。

---
