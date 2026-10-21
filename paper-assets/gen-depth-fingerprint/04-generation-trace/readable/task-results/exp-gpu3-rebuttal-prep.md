# exp gpu3 rebuttal prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gpu3-rebuttal-prep_20260518T151007_result.json`
- **Structured JSON:** [`953071d05386cf6a5282.json`](../../sessions/95/953071d05386cf6a5282.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

## Per-generator TOST 等价性检验 (d < 0.20, α=0.05)

**18/56 tests 通过等价性检验。**

| Feature | 通过/总数 | 模式 |
|---|---|---|
| **entropy_min** | **8/8** | 所有 generator 均等价 |
| **entropy_max** | **6/8** | pythia-1b (d=0.21), pythia-2.8b (d=0.25) 未通过 |
| **tail_decay** | **4/8** | pythia 系列 + qwen3 小模型通过；llama/mistral/olmo/qwen3-8b 未通过但 d 接近边界 |
| entropy_mean | 0/8 | 全部 d > 0.86，强漂移 |
| ttr | 0/8 | 全部 d > 0.63，强漂移 |
| hapax_ratio | 0/8 | 全部 d > 0.50，强漂移 |
| entropy_std | 0/8 | 全部 d > 0.23，漂移 |

**Rebuttal 关键论点：**
1. **entropy_min 跨 generator 一致 near-stationary**（8/8 通过，最大 |d|=0.10），是最稳健的不变特征
2. **Near-stationary vs drifting 的二分法在 per-generator 层面同样成立**，不是 pooling artifact
3. Drifting features 的效应量极大（d > 0.5），与 near-stationary features（|d| < 0.10 典型值）形成鲜明对比
4. entropy_max 仅 pythia 系列轻微超出边界，tail_decay 的 borderline 情况可归因于模型族差异

产出文件：
- 服务器：`/root/gen-depth-fingerprint/results/tost_per_generator.json`
- 本地：`artifacts/_project/rebuttal/tost_per_generator.json`

---
