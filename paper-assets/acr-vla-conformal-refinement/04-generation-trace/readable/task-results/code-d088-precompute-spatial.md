# code d088 precompute spatial

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d088-precompute-spatial_20260520T162453_result.json`
- **Structured JSON:** [`0ec6f83c87ccdab75ea9.json`](../../sessions/0e/0ec6f83c87ccdab75ea9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Per-sample 文件结构：`obs_features (960,)`, `vla_action (5,6)`, `expert_action (5,6)`, `task_name`。但这是 K=1 数据，无法从单 sample 计算 variance。

**Spatial K=10 聚合 cache 不存在。** 服务器上只有：
- `crm_cache_k1/object/`: K=1, 72507 samples, object benchmark
- `crm_cache_k1/spatial/`: 空目录
- `crm_cache_k1_openvla/object/`: ~46353 samples

两个问题：
1. **没有 Spatial 数据** — spatial 目录是空的
2. **K=1 不是 K=10** — 单 sample 无法计算 action variance

**可行替代方案：**

**A) 用 K=1 Object 数据 + expert deviation 作为 uncertainty proxy。** 每个 sample 有 `vla_action` 和 `expert_action`，可以用 `|vla_action - expert_action|` 的 norm 作为 uncertainty label。这是 CPU 操作，数据已经就绪（72507 samples）。需要给 `precompute_uncertainty_labels.py` 加一个 `--mode per_sample` 模式。

**B) 在有 GPU 的时候跑 `--mode sample` 对 spatial benchmark 做 K=10 采样。** 需要 GPU + SmolVLA，不是 CPU 操作。

建议先走 A 跑通整个 pipeline（precompute → train uncertainty head），然后有 GPU 时再补 spatial K=10 数据。需要我执行方案 A 吗？

---
