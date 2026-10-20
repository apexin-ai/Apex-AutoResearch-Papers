# monitor qwen s015 check v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_qwen_s015_check_v2_20260514T191305_result.json`
- **Structured JSON:** [`ade3974444ad4a282fdc.json`](../../sessions/ad/ade3974444ad4a282fdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Qwen s015 — 已完成 ✓ (500/500)

两个条件均于 2026-05-15 ~03:02/03:11 完成。

| 条件 | sparsity | median II | 95% CI | mean II | mean 95% CI |
|------|----------|-----------|--------|---------|-------------|
| **importance** | high | +0.0002 | [+0.0001, +0.0004] | -0.0833 | [-0.0971, -0.0703] |
| **importance** | low | +0.0549 | [+0.0388, +0.0680] | +0.2498 | [+0.1470, +0.3490] |
| **importance** | mid | +0.0010 | [-0.0000, +0.0068] | +0.2109 | [+0.0336, +0.4635] |
| **random** | high | +0.0885 | [+0.0791, +0.0997] | +0.7632 | [-0.9275, +1.8201] |
| **random** | low | +0.1059 | [+0.0945, +0.1226] | -0.6152 | [-5.1270, +1.8180] |
| **random** | mid | +0.0865 | [+0.0621, +0.1172] | +16.3278 | [-2.0971, +49.4450] |

- **Importance → PASS** (low vs mid CI 不重叠)
- **Random → FAIL** (三个 sparsity 区间的 median II 都在 ~0.09 附近，无显著分化)

### DeepSeek s015 — 已完成 ✓ (500/500)

| 条件 | sparsity | median II | 95% CI |
|------|----------|-----------|--------|
| **importance** | high | +0.0065 | [+0.0055, +0.0077] |
| **importance** | low | +0.3973 | [+0.3705, +0.4258] |
| **importance** | mid | +0.0814 | [+0.0725, +0.0938] |
| **random** | high | +0.1030 | [+0.0900, +0.1147] |
| **random** | low | +0.1178 | [+0.1052, +0.1336] |
| **random** | mid | +0.1295 | [+0.1138, +0.1445] |

- **Importance → PASS**, **Random → FAIL**（与 Qwen 结论一致）

### s020 进度 — 运行中

| 任务 | 进度 | 备注 |
|------|------|------|
| ds_imp_s020 | 92/500 | ~18% |
| ds_rand_s020 | 139/500 | ~28% |
| qw_imp_s020 | 30/500 | ~6% |
| qw_rand_s020 | 11/500 | ~2% |

### GPU 状态

| GPU | 利用率 | 显存使用 |
|-----|--------|----------|
| 0 | 77% | 20.9 / 97.9 GB |
| 1 | 77% | 24.2 / 97.9 GB |
| 2 | 77% | 25.1 / 97.9 GB |
| 3 | 78% | 20.6 / 97.9 GB |

4 张 GPU 全部在跑，分别对应 4 个 s020 任务。按当前速度，s020 预计还需数小时完成。

---
