# check post restart status

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_post_restart_status_20260522T020905_result.json`
- **Structured JSON:** [`e03e4c8f009977c8ac72.json`](../../sessions/e0/e03e4c8f009977c8ac72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. accum_pythia_nuc_002 — **已完成** ✓

进程已停止（重启后不在），但运行日志显示 `EXIT_CODE=0`，pipeline 正常完成。

关键 metrics（mix25, 25% human）：
| 指标 | 值 |
|------|-----|
| Overall accuracy | 0.7077 |
| Balanced accuracy | 0.7077 |
| d1-d3 balanced acc | 0.6115 |
| Full-replacement baseline | 0.8428 |
| Delta vs baseline | -0.1351 |
| 耗时 | 2.4h |

Per-class recall: d0=0.996, d1=0.706, d2=0.439, d3=0.690

结果已保存到 `results/accumulation_v3/pythia_nucleus/mix25/summary.json`。

### 2. conditional_pi_001 — **部分完成，中途崩溃** ✗

完成了 **7/N 个 cell**（pythia_nucleus, pythia_temp09, pythia_topk50, olmo_nucleus, olmo_temp09, olmo_topk50, gpt2xl_nucleus），在第 8 个 cell **gpt2xl_temp09** 的 `rf.fit()` 阶段崩溃：

```
ValueError: Input X contains infinity or a value too large for dtype('float32').
```

`gpt2xl_temp09/features.jsonl` 中有 inf 或极大值。已完成的 7 个 cell 结果保存在 `per_cell_pi.json` 和 `bootstrap_ranks.json`。

### 3. 服务器状态

| 资源 | 状态 |
|------|------|
| GPU | RTX PRO 6000 (98GB), 空闲 (0% util, 0MB used) |
| 磁盘 | 177G/250G used (71%) |

### 需要处理

`conditional_pi_001` 需要修复后重跑。原因是 `gpt2xl_temp09` 的特征数据含 inf/极大值。可以在 `compute_pi` 里加 `np.nan_to_num` 或 `np.clip` 预处理，然后只跑剩余未完成的 cell（gpt2xl_temp09 及之后的）。

---
