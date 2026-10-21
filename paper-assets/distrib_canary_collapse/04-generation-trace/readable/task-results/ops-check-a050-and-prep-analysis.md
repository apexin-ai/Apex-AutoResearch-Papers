# ops check a050 and prep analysis

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-a050-and-prep-analysis_20260515T051619_result.json`
- **Structured JSON:** [`aa464d1624ea70293cf9.json`](../../sessions/aa/aa464d1624ea70293cf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## a050 实验状态：**RUNNING**

| 项目 | 值 |
|------|-----|
| PID | 73737，已运行 3h56m |
| 当前进度 | **Generation 10/10**（最后一代），正在生成合成数据 |
| 已完成 | gen_0 ~ gen_9（共 10 个目录） |
| gen_10 | 目录已创建，内容为空（刚开始） |

**每代耗时约 25 min**（从目录时间戳推算），gen_10 于 13:16 开始 → **预计 ~20-25 min 后完成**。

### 最新完成的 gen_9 指标
```
ppl=32.11, entropy=2.633, eff_rank=59.53, mauve=0.0194
self_bleu=0.016, distinct_1=0.062, distinct_2=0.256, ece=0.097
```

### 分析脚本就绪确认
- `analyze_alpha_sweep.py` — **就绪** ✓（支持 `--max_lag`, `--n_permutations` 参数）
- `gen_dose_response.py` — **就绪** ✓（试运行已生成 `dose_response_drift.csv`，24 行）

> 注意：实验输出的是每代 `gen_X/metrics.json`，不存在 `all_metrics.json`。a050 完成后可直接运行 3-point 分析。

---
