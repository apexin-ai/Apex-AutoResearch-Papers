# fix precompute long bjb1 restart

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_precompute-long-bjb1-restart_20260522T111201_result.json`
- **Structured JSON:** [`4a7e59eb31d8ebc7cdad.json`](../../sessions/4a/4a7e59eb31d8ebc7cdad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### bjb1-32546 — SmolVLA Long precompute (K=2, crm_cache_v5)

**不需要重新运行。** 原始崩溃 (`precompute-smolvla-long-bjb1-32546`) 的错误确实是目录不存在，但从日志看那是一个 **K=10** 的任务（错误写入了 crm_cache_v5）。而 K=2 的 Long cache 已由另一个 run 在今天 14:38-15:28 成功完成：

- `/root/autodl-tmp/crm_cache_v5/long/manifest.json`: 136090 samples, K=2, obs_dim=960
- 合并后的 `obs_features.pt` (523MB), `k_samples.pt` (33MB), `expert_actions.pt` (16MB) 全部就绪
- K=10 版本也在 `/root/autodl-tmp/crm_cache_k10/long/` 已完成（带 manifest + merged tensors）

### bjb2-28827 — Goal precompute

**正在运行中**，状态正常：
- 任务：**π0.5 Goal K=10** (model=pi05, cache_dir=crm_cache_pi05/)，不是 SmolVLA
- 3 个 shard 分别跑在 cuda:3/4/5，从 16:03 启动，CPU 占用 153%
- 每个 shard 已产出 9 个 partial 文件（到 sample 4500）
- 按当前速度（~500 samples/30min），预计还需 ~数小时完成

---
