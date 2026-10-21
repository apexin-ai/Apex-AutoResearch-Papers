# ops check mink detectgpt progress

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_mink_detectgpt_progress_20260518T191356_result.json`
- **Structured JSON:** [`b4b9746e9f1427f95b74.json`](../../sessions/b4/b4b9746e9f1427f95b74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

## gpu-6000pro-2: Min-K% Prob — 进行中

- **进程**: PID 994671，运行中（已跑 ~206 分钟）
- **score 文件**: 24/27 完成
  - pythia (nucleus/temp09/topk50) × 3 K values = 9 ✓
  - olmo (nucleus/temp09/topk50) × 3 K values = 9 ✓
  - gpt2xl_nucleus × 3 K values = 3 ✓
  - gpt2xl_temp09 × 3 K values = 3 ✓
  - **gpt2xl_topk50**: 正在计算 logprob，进度 27% (112/417 batches)
- **`mink_prob_results.json`**: 尚未生成（需全部 27 个 score 文件完成后聚合）
- **预计剩余时间**: gpt2xl_topk50 logprob ~4.5 分钟完成，之后还有 3 个 K 值的 scoring + 聚合。预计 **10-15 分钟内完成**。

---

## westd-48862: DetectGPT — 已完成

- **进程**: 已结束（无运行中进程）
- **`detectgpt_results.json`**: 已生成
- **注意**: 缺少 `pythia_nucleus_scores.npz`（8/9 cells 有 score 文件），但结果 JSON 中也只有 8 个 cell
- 配置: scoring_model=`gpt2-large`, perturbation_model=`t5-large`, 5 perturbations, 200 samples/depth

**DetectGPT 完整结果**:

| Cell | Method | 4class_acc | d1d3_bal_acc |
|------|--------|-----------|-------------|
| gpt2xl_nucleus | A | 0.285 | 0.318 |
| gpt2xl_nucleus | B | 0.250 | 0.325 |
| gpt2xl_nucleus | C | 0.401 | 0.310 |
| gpt2xl_temp09 | A | 0.280 | 0.318 |
| gpt2xl_temp09 | B | 0.296 | 0.370 |
| gpt2xl_temp09 | C | 0.414 | 0.302 |
| gpt2xl_topk50 | A | 0.311 | 0.323 |
| gpt2xl_topk50 | B | 0.265 | 0.348 |
| gpt2xl_topk50 | C | 0.369 | 0.240 |
| olmo_nucleus | A | 0.259 | 0.338 |
| olmo_nucleus | B | 0.249 | 0.330 |
| olmo_nucleus | C | 0.309 | 0.243 |
| olmo_temp09 | A | 0.254 | 0.325 |
| olmo_temp09 | B | 0.253 | 0.337 |
| olmo_temp09 | C | 0.298 | 0.177 |
| olmo_topk50 | A | 0.253 | 0.320 |
| olmo_topk50 | B | 0.255 | 0.340 |
| olmo_topk50 | C | 0.243 | 0.252 |
| pythia_temp09 | A | 0.325 | 0.325 |
| pythia_temp09 | B | 0.332 | 0.332 |
| pythia_temp09 | C | 0.218 | 0.218 |
| pythia_topk50 | A | 0.318 | 0.318 |
| pythia_topk50 | B | 0.337 | 0.337 |
| pythia_topk50 | C | 0.202 | 0.202 |

**Summary**: mean 4class_acc = 0.291, mean d1d3_bal_acc = 0.302 (8 cells)。4 类随机基线 0.25，DetectGPT 几乎没有超出随机水平。

---
