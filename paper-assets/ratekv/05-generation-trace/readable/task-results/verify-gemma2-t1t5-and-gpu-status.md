# verify gemma2 t1t5 and gpu status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_gemma2_t1t5_and_gpu_status_20260515T144022_result.json`
- **Structured JSON:** [`69f8f1122a26e597c056.json`](../../sessions/69/69f8f1122a26e597c056.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手。汇总如下：

---

## 任务 1：Gemma-2-9B hires t1/t5

**从 `gemma2_hires_bf16_2bitonly_profiles.json` 计算（336 heads）：**

| 指标 | 值 |
|------|-----|
| Total heads | 336 |
| Positive-delta heads | 310 |
| n_top1 (ceil 1%) | 4 heads |
| n_top5 (ceil 5%) | 17 heads |
| Total positive sum | 4.0993 |
| Top-5% sum | 0.9572 |
| Top-1% sum (4 heads) | 0.4348 |
| top5_concentration | 0.2335 |
| **t1/t5 (top1% group / top5% group)** | **0.4543** |
| **t1/t5 (single top head / top5% sum)** | **0.1991** (0.1906 / 0.9572) |

Top-1 head 是 **L0H1** (delta=0.1906)，显著领先但没有 Llama/Yi 那种一骑绝尘的 spike。

**shape_metrics.json 中 Gemma-2-9B（来自常规 profiling，非 hires）：**

| 指标 | 值 |
|------|-----|
| top5_concentration | 0.2299 |
| top1_share | 0.0404 |
| top1_top5_ratio | 0.1757 |
| top1_top2_ratio | 1.5213 |
| cv | 1.2344 |
| gini | 0.5305 |

**注意差异**：shape_metrics 的 top1_share=0.0404 vs hires 的 0.1061（top1%群）/ 单头 0.0465。数据源不同（`gemma2_profiling_results.json` vs hires bf16 2bitonly），deltas 绝对值有差异，但分布形状一致——Gemma-2 属于 **低集中度**（类似 Mistral），无 dominant head。

---

## 任务 2：GPU 0 状态

| 项目 | 结果 |
|------|------|
| PID 340906 | **仍存活** — 跑着 `run_mistral_hires_bf16_2bitonly.py --gpu cuda:0 --batch_size 2` |
| GPU 0 | 18,007 MiB / 97,887 MiB, **100% utilization** |
| GPU 1 | 15,257 MiB / 97,887 MiB, **0% utilization** |

GPU 0 未释放，Mistral hires 任务仍在占用。

---
