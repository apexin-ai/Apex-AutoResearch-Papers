# diag temp progress check v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_temp-progress-check-v2_20260518T162926_result.json`
- **Structured JSON:** [`3cd194942ab66c32a93d.json`](../../sessions/3c/3cd194942ab66c32a93d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== tmux sessions ===
temp_olmo:    存在 — OLMo t=0.5 generation: 69% (682/995 seeds), ~7.6s/it
temp_qwen06:  存在 — Qwen3-0.6B t=0.5 generation: 46% (461/996 seeds), ~13.1s/it
temp_monitor: 存在 — 每 120s 轮询，最新记录 00:29 CST

=== Generation 数据 ===
olmo_t05:    进行中 — seeds: 682/995, lines: 3359, ETA ~40min (≈01:10 CST)
olmo_t09:    未开始 — 目录不存在，等 t=0.5 跑完后自动启动
qwen06_t05:  进行中 — seeds: 461/996, lines: 2195, ETA ~1h55m (≈02:25 CST)
qwen06_t09:  未开始 — 目录不存在，等 t=0.5 跑完后自动启动

=== Feature extraction + Classification ===
尚无温度实验的新 feature CSV（olmo-t05/t09, qwen06-t05/t09）
已有 results: temp_curve_binary_logo.json（pythia-2.8b 和 qwen3-1.7b 的温度曲线）:
  - pythia-2.8b:  t=0.5 F1=0.814, t=0.7 F1=0.740, t=0.9 F1=0.480
  - qwen3-1.7b:   t=0.5 F1=0.751, t=0.7 F1=0.751, t=0.9 F1=0.566, t=1.0 F1=0.367
monitor 脚本会在 4 组 generation 全部完成后自动触发 feature extraction

=== GPU 状态 ===
GPU 0: 使用中 — 3625/32607 MiB, 49% util — OLMo t=0.5 generation
GPU 1: 使用中 — 1825/32607 MiB, 32% util — Qwen3-0.6B t=0.5 generation
GPU 2: 空闲 — 3/32607 MiB, 0% util
GPU 3: 空闲 — 3/32607 MiB, 0% util
```

**关键时间线估算**：OLMo t=0.5 约 01:10 完成 → 自动切 t=0.9；Qwen3-0.6B t=0.5 约 02:25 完成 → 自动切 t=0.9。t=0.9 的生成速度与 t=0.5 类似，所以全部 4 组数据预计约 **04:30–05:00 CST** 完成，之后 monitor 自动触发 feature extraction 和 classification。GPU 2/3 空闲可用。

---
