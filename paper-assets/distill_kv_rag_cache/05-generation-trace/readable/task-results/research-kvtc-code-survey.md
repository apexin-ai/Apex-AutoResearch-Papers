# research kvtc code survey

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_kvtc-code-survey_20260514T042154_result.json`
- **Structured JSON:** [`fb6214f6ee6b59afa088.json`](../../sessions/fb/fb6214f6ee6b59afa088.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。核心发现:

**DP Solver**: `src/quantize.py:16-56`, error function 确认为 `λ_i / 4^b`。生产用贪心版在 `src/gpu_ops.py:10-57`。两者数学等价。

**RABA 修改方案**: ~55 行代码, 集中在 bit allocation 调用处。推荐方案 B——预聚合 weighted eigenvalues `weighted_λ_i = mean_t[(1 - p_r(t)) × pca_coeffs[t,i]²]`, 然后传入现有 DP/greedy allocator。不改量化、编码、解压路径。

**压缩比**: K1V3 配置直接达 8.9x (cosine ~0.987)。K2V4 + RABA 可在保持更高质量同时逼近 8x。

**关键低风险点**: 解压路径零改动 (bit_widths 已存 metadata), calibration 完全兼容, 与 adaptive budget 正交。

报告已注册为 artifact `art_20260514_43a9d0`。

---
