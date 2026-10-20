# code table4 grid search v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_table4-grid-search-v2_20260517T115144_result.json`
- **Structured JSON:** [`d49b258930e55372ee6a.json`](../../sessions/d4/d49b258930e55372ee6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。109秒跑完全部 56 个评估。结果已保存到 `table4_grid_search.json`。

完整结果：

| Method | est100_md3 | est100_md6 | est200_md3 | est200_md6 | Best 3-class | Best Binary |
|---|---|---|---|---|---|---|
| **avg_logprob** | .6746/.7091 | .6736/.7070 | .6746/.7091 | .6734/.7072 | **0.7091** (100,3) | **0.6746** (100,3) |
| **fastdetectgpt** | .5823/.6646 | .5768/.6626 | .5785/.6644 | .5688/.6599 | **0.6646** (100,3) | **0.5823** (100,3) |
| **binoculars** | .5315/.4090 | .5334/.4082 | .5325/.4101 | .5391/.4110 | **0.4110** (200,6) | **0.5391** (200,6) |
| **ld_score** | .6752/.6320 | .6752/.6298 | .6753/.6318 | .6750/.6300 | **0.6320** (100,3) | **0.6753** (200,3) |
| **4det_ensemble** | .6943/.7784 | .7019/.7851 | .6982/.7826 | .7000/.7852 | **0.7852** (200,6) | **0.7019** (100,6) |
| **4det_surface** | .7031/.7826 | .7091/.7938 | .7075/.7894 | .7082/.7951 | **0.7951** (200,6) | **0.7091** (100,6) |
| **7feature_ours** | .7040/.7480 | .7072/.7680 | .7066/.7621 | .7052/.7740 | **0.7740** (200,6) | **0.7072** (100,6) |

格式为 binary/multiclass F1。

关键发现：
- 单 detector 方法对超参不敏感（变化 < 0.01）
- 多特征方法（4det_ensemble, 4det_surface, 7feature_ours）受益于更大 max_depth=6
- **4det_surface 在 (200,6) 下 3-class F1=0.7951，超过 7feature_ours 的 0.7740**
- 之前 Table 3 v6 给 7feature_ours 用 (200,6) 而给 baselines 用 (100,3)，统一超参后差距变小

---
