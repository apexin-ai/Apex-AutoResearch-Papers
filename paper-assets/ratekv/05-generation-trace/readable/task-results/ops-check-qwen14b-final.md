# ops check qwen14b final

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_qwen14b_final_20260515T112203_result.json`
- **Structured JSON:** [`4439154f61adaf08a6c2.json`](../../sessions/44/4439154f61adaf08a6c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen2.5-14B Profiling 完整结果

**状态**: 已完成（384/384 heads，耗时 161.3 min）

### 核心指标

| 指标 | 值 |
|------|-----|
| Baseline PPL | 5.8432 |
| Top-5% concentration | 0.3312 (19 heads) |
| t1/t5 ratio | 24.35 |
| L0 dominance | 15.50x |
| CV | 3.7418 |
| **Shape** | **Spike** |
| Positive delta heads | 370/384 |

### Top-10 敏感 heads

| Rank | Head | delta(2bit) |
|------|------|-------------|
| 1 | **L0H5** | **1.844940** |
| 2 | L0H4 | 0.236669 |
| 3 | L0H2 | 0.136971 |
| 4 | L28H4 | 0.099279 |
| 5 | L28H5 | 0.075760 |
| 6 | L27H4 | 0.071269 |
| 7 | L0H0 | 0.070018 |
| 8 | L28H6 | 0.063737 |
| 9 | L26H0 | 0.061462 |
| 10 | L31H3 | 0.061062 |

### 关键观察

1. **极端 Spike 形态**: L0H5 的 delta=1.845 是 Top-2 的 **7.8 倍**，t1/t5=24.35 是迄今所有模型中最极端的 spike
2. **L0 强主导**: L0 mean delta=0.303，其余层平均 ~0.020，L0 dominance=15.50x
3. **L28 是第二热区**: L28 有 3 个 head 进入 Top-10（H4/H5/H6），mean=0.047 是非 L0 层中最高
4. **中间层（L24-L31）形成弱峰**: mean delta 在 0.030-0.047 范围，尾部层（L35+）逐渐衰减

**GPU 状态**: 两块 GPU 均已释放（0 MiB / 97887 MiB，0% 利用率）。

---
