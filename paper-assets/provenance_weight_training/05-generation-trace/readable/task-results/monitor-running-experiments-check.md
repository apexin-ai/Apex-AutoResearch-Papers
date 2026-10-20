# monitor running experiments check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_running_experiments_check_20260515T184323_result.json`
- **Structured JSON:** [`0b0bd7891615b4f5d946.json`](../../sessions/0b/0b0bd7891615b4f5d946.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. nmin4_seed42 (cuda:1, PID 225265) — ✅ RUNNING

| 指标 | 值 |
|------|-----|
| 进度 | **1800/6103 (29%)** |
| 已用时 | 1h58m |
| 剩余 | ~2h31m |
| 速度 | 2.11 s/it |
| 配置 | n_min=4, batch_size=4 ✓ |
| b* | **全部 0.0** ✓（ESS=4.0 = n_min，无需 bonus） |
| weighted_loss | == unweighted_loss（符合预期） |

无异常。

---

### 2. ess_only_seed123 (cuda:0, PID 233872) — ✅ RUNNING

| 指标 | 值 |
|------|-----|
| 进度 | **1105/6103 (18%)** |
| 已用时 | 39m |
| 剩余 | ~2h56m |
| 速度 | 2.12 s/it |
| ESS | ≈2.0，b 非零（正常） |

无异常。

---

### 3. ess_only_seed456 (cuda:3, PID 233952) — ✅ RUNNING

| 指标 | 值 |
|------|-----|
| 进度 | **1105/6103 (18%)** |
| 已用时 | 39m |
| 剩余 | ~2h56m |
| 速度 | 2.12 s/it |
| ESS | ≈2.0，b 非零（正常） |

无异常。

---

### 4. bs8_seed42 (cuda:2, PID 236697) — ❌ 已终止

| 指标 | 值 |
|------|-----|
| 终止时进度 | **258/6103 (4%)** |
| 退出码 | **129 (SIGHUP)** — 被外部信号杀死 |
| 速度 | 2.24 s/it（终止前） |

**🔴 严重问题：n_min=4（不是预期的 n_min=2）**

日志开头配置确认：
```
weighting_method: adaptive
n_min: 4          ← 错误！应为 2
batch_size: 8     ← 正确
```

日志中 ESS 值 4~6 也印证了 n_min=4 而非 2。

**两个问题需要处理：**
1. 启动参数中 `--n_min 4` 应改为 `--n_min 2`
2. 进程已死（SIGHUP），需要以正确参数重新启动

---
