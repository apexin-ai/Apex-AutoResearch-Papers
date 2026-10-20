# diagnostic gpu status 20260515

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_gpu_status_20260515_20260515T143206_result.json`
- **Structured JSON:** [`dfa55fafd29cb9c1e80d.json`](../../sessions/df/dfa55fafd29cb9c1e80d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## GPU 状态 & 实验进度报告

### 1. GPU 总览

| GPU | 显存 | 利用率 | 实验 | PID |
|-----|------|--------|------|-----|
| cuda:0 | 46,523 / 97,887 MiB | 93% | tau_07_seed42 (τ=0.7) | 209829 |
| cuda:1 | 46,523 / 97,887 MiB | 86% | tau_05_seed42 (τ=0.5) | 205657 |
| cuda:2 | 42,472 / 97,887 MiB | 99% | **tau_095_seed42 (τ=0.95)** ← 新实验，刚启动 | 215505 |
| cuda:3 | 46,523 / 97,887 MiB | 99% | tau_09_seed42 (τ=0.9) | 213283 |

### 2. tau_09_seed42 — 运行中 ✓

PID 213278（bash wrapper）→ PID 213283（python）在 cuda:3 上正常运行。

- 进度：**873 / 6,103** (14.3%)
- 已用时：32 min
- 预计剩余：~3h15m
- 预计完成：约 3h47m 后

### 3. tau_05_seed42 — 运行中

- 进度：**2,585 / 6,103** (42.4%)
- 已用时：1h37m
- 预计剩余：~2h07m
- 速度：2.16 s/it

### 4. tau_07_seed42 — 运行中

- 进度：**1,449 / 6,103** (23.7%)
- 已用时：56 min
- 预计剩余：~2h54m
- 速度：2.24 s/it

### 5. nmin1_seed42 — 训练完成 ✓ / Eval 未执行 ✗

训练正常结束（EXIT_CODE=0），耗时 4h50m，模型已保存到 `output/models/nmin1_seed42/final/`。

**Eval 未运行**：`eval_results.json` 和 `posthoc_eval_nmin1_seed42.json` 均不存在。cuda:2 已被 tau_095_seed42 占用，无法立即执行 eval。

**b 分布** (n_min=1, 24,412 samples)：

| 指标 | 值 |
|------|-----|
| mean | 7.197 |
| median | 1.746 |
| std | 8.374 |
| p25 / p75 | 0.803 / 20.000 |
| zero | 1.9% |
| < 0.5 | 13.1% |
| [0.5, 1) | 19.1% |
| [1, 2) | 21.1% |
| **≥ 2** | **46.7%** |

alpha_eff：mean=0.714, median=0.800

b 分布显示近半数 batch (46.7%) 的 b≥2，且 p75 直接打到上限 20.0——n_min=1 时加权极其激进，大量 batch 被强力上/下权。与 n_min=2/3 相比，预期 PPL 可能偏高。

### 6. 与 baseline 对比（待 eval）

| 配置 | n_min | PPL | 状态 |
|------|-------|-----|------|
| adaptive_fix | 2 | 17.650 | 已完成 |
| adaptive | 3 | 17.690 | 已完成 |
| **nmin1** | **1** | **?** | **训练完成，等待 eval** |

### 7. 新发现

cuda:2 上有人提交了 **tau_095_seed42**（τ=0.95）实验，刚启动 42 秒。nmin1 eval 需等某张卡空闲后再执行——最早可在 tau_05 完成后（~2h）用 cuda:1 跑。

---
