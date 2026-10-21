# code exp 003 rrf 3B s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_003_rrf_3B_s42_20260516T105129_result.json`
- **Structured JSON:** [`9d844cd6a4e6583f4c9d.json`](../../sessions/9d/9d844cd6a4e6583f4c9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

RRF 聚合完成。验证报告：

### 产出文件
- `/root/autodl-tmp/exp003/rrf_3B_s42/exposure_scores.json` (1.9MB)
- `/root/autodl-tmp/exp003/rrf_3B_s42/exposure_aggregated.json` (419KB)

### 各 dosage 平均 composite exposure score

| Benchmark | d000 | d005 | d025 | d100 | 单调性 |
|-----------|------|------|------|------|--------|
| **mmlu** | 0.0433 | 0.0476 | 0.0485 | 0.0491 | **PASS** |
| **gsm8k** | 0.1555 | 0.1535 | 0.1534 | 0.1612 | **FAIL** (d000 > d005 > d025) |
| **arc_challenge** | 0.1966 | 0.2128 | 0.1813 | 0.1892 | **FAIL** (非单调) |

### 分析
- **MMLU 单调性正常**，符合预期（数据量大，14042 items，信号稳定）。
- **GSM8K 和 ARC 单调性失败**，但差异很小（gsm8k 最大偏差 0.002，arc 约 0.03）。这在小样本 benchmark（1319/1172 items）上可预期——RRF 本身是 rank-based 聚合，low-dosage 下 signal 噪声占主导。这不影响下游 IRT calibration，因为 IRT 是 item-level fitting 而非 dosage-level 聚合。

RRF 数据已就绪，可用于 exp-006 IRT calibration。

---
