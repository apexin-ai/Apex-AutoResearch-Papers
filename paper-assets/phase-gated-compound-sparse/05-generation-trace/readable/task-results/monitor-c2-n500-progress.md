# monitor c2 n500 progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_c2_n500_progress_20260514T220417_result.json`
- **Structured JSON:** [`140591ec299311293111.json`](../../sessions/14/140591ec299311293111.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全了。汇总如下：

---

## 实验进度汇总（截至 CST 06:06, May 15）

### GPU 状态
| GPU | 利用率 | 显存使用 | 状态 |
|-----|--------|---------|------|
| 0 | 77% | 33.4/97.9 GB | 正常 |
| 1 | 98% | 33.9/97.9 GB | 正常 |
| 2 | 96% | 34.1/97.9 GB | 正常 |
| 3 | 77% | 34.7/97.9 GB | 正常 |

无异常，4 块 GPU 全部在跑。

---

### 实验 1: c2_n500_deepseek (GPU 0+1)

| Condition | 状态 | 进度 | 速率 | ETA |
|-----------|------|------|------|-----|
| imp_s015 | **完成** | 500/500 | — | — |
| imp_s020 | 进行中 | **412/500 (82%)** | ~115/hr | ~06:52 |
| imp_s025 | 待开始 | — | — | ~11:12 |
| imp_s030 | 待开始 | — | — | ~15:30 |
| rand_s015 | **完成** | 500/500 | — | — |
| rand_s020 | 进行中 | **460/500 (92%)** | ~114/hr | ~06:27 |
| rand_s025 | 待开始 | — | — | ~10:47 |
| rand_s030 | 待开始 | — | — | ~15:07 |

s015 参考耗时：imp ~4h50m, rand ~4h24m

---

### 实验 2: c2_qw_n500_r3 (GPU 2+3)

| Condition | 状态 | 进度 | 速率 | ETA |
|-----------|------|------|------|-----|
| imp_s015 | **完成** | 500/500 | — | — |
| imp_s020 | 进行中 | **455/500 (91%)** | ~148/hr | ~06:24 |
| imp_s025 | 待开始 | — | — | ~09:48 |
| imp_s030 | 待开始 | — | — | ~13:12 |
| rand_s015 | **完成** | 500/500 | — | — |
| rand_s020 | 进行中 | **438/500 (88%)** | ~150/hr | ~06:31 |
| rand_s025 | 待开始 | — | — | ~09:55 |
| rand_s030 | 待开始 | — | — | ~13:19 |

s015 参考耗时：imp ~5h10m, rand ~5h19m

---

### 总结
- **完成**: 4/16 conditions（全部 s015）
- **进行中**: 4/16 conditions（全部 s020，均 >80%，将在 ~30-50min 内完成）
- **待开始**: 8/16 conditions（全部 s025 + s030）
- **预计全部完成**: DeepSeek ~15:30 CST, Qwen ~13:19 CST（约 7-9 小时后）
- **异常**: 无。进程正常，GPU 利用率高，无 OOM。

---
