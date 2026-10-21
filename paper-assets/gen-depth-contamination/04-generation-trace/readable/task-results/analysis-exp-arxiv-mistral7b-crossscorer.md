# analysis exp arXiv mistral7b crossscorer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_arXiv_mistral7b_crossscorer_20260518T030323_result.json`
- **Structured JSON:** [`896ff58449bc2fbe597f.json`](../../sessions/89/896ff58449bc2fbe597f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**K\* = 3，conclusion = success（scorer-independent）**

### Pairwise AUC 对比

| Depth Pair | Qwen-1.5B (原始) | Pythia-1.4B (cross) | Delta |
|---|---|---|---|
| 0v1 | 0.9848 | 0.9798 | -0.005 |
| 1v2 | 0.8201 | 0.8141 | -0.006 |
| **2v3** | **0.6275** | **0.6075** | **-0.020** |
| 3v4 | 0.5295 | 0.5489 | +0.019 |
| 4v5 | 0.5295 | 0.5391 | +0.010 |

两个 scorer 在 2v3 均 >0.60（Qwen 0.6275, Pythia 0.6075），3v4 均 <0.55，K\* 判定一致为 3。最大 AUC 差异仅 0.02。

### 关键结论

- **arXiv + Mistral-7B: K\*=3 是 scorer-independent 的真实信号**
- 与 Wikipedia 形成对比：Wiki 存在 scorer confound（Qwen→K\*=2, Pythia→K\*=1），arXiv 不存在
- 解释：arXiv 的 depth 信号更强更鲁棒，不受 scorer family 选择影响

Registry 已更新完整 metrics、log_path、notes。报告已注册至 artifacts。

---
