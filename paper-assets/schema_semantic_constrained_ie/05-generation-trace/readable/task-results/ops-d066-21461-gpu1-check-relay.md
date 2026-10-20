# ops d066 21461 gpu1 check relay

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_21461_gpu1_check_relay_20260520T120842_result.json`
- **Structured JSON:** [`9433d3819057c53a10f9.json`](../../sessions/94/9433d3819057c53a10f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

10/551 samples processed, running smoothly on GPU1.

## 报告

### 1. Qwen beam8 s1 完成状态
- **文件**: `/root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam8_full_s1.jsonl`
- **行数**: 551 行（完整）
- **eval 结果**: E_F1=66.36, R_F1=43.65, 0 violations (ET/RV/DR/CF 全为 0%), 平均推理 5.058s

### 2. d066 beam sweep 配置清单（SciERC, Qwen）

| Config | 状态 | E_F1 | R_F1 | DR% | CF% | avg time |
|--------|------|------|------|-----|-----|----------|
| k=1 con (s1) | ✅ | 66.88 | 42.95 | 0.0 | 0.5 | 2.93s |
| k=1 unc | ✅ | 66.88 | 42.95 | 2.11 | 0.0 | 2.49s |
| k=2 con (s1) | ✅ | 67.71 | 44.60 | 0.0 | 0.11 | 3.46s |
| k=2 unc | ✅ | 67.79 | 44.75 | 1.54 | 0.0 | 2.95s |
| k=4 con (s1) | ✅ | 67.22 | 43.60 | 0.0 | 0.0 | 4.07s |
| k=4 unc | ✅ | 67.49 | 43.72 | 1.89 | 0.0 | 3.49s |
| k=8 con (s1) | ✅ | 66.36 | 43.65 | 0.0 | 0.0 | 5.06s |
| k=8 unc | ✅ | 66.40 | 43.17 | 1.77 | 0.0 | 4.19s |

**Qwen 8 configs 全部完成。** k=2 在 E_F1 和 R_F1 上表现最佳。constrained 消除了 DR violations（1.5-2.1% → 0%）。

**Llama 未完成配置**（8 个全未做）: beam{1,2,4,8} × {unc, s1}

### 3. 新启动配置
- **配置**: `llama_scierc_beam1_unconstrained`
- **PID**: 205314 (GPU1, 18338MiB)
- **输出**: `/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl`

### 4. GPU 状态
- **GPU0**: PID 194615 (d065_qwen_greedy_4096_r2), 18910MiB, 84% util
- **GPU1**: PID 205314 (llama beam1 unc), 18338MiB, 90% util

**注意**: 实际 sweep 跑的是 **SciERC** (551 samples)，不是任务描述中提到的 DocRED 200-doc subset。模型和数据目录均指向 SciERC。

---
