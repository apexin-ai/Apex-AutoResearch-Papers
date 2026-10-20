# analysis p1c base rho verify

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p1c-base-rho-verify_20260515T153415_result.json`
- **Structured JSON:** [`aeaf7f86bc546b16c2c8.json`](../../sessions/ae/aeaf7f86bc546b16c2c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个特征完全匹配。

## 验证结果

### BASE_MODEL_RHO 硬编码值（analyze_instruct.py）

| 特征 | 硬编码值 | 计算值 | 匹配 |
|------|---------|--------|------|
| hapax_ratio | -0.6696 | -0.6696 | ✓ |
| ttr | -0.6523 | -0.6523 | ✓ |
| entropy_mean | -0.6022 | -0.6022 | ✓ |
| entropy_std | -0.1882 | -0.1882 | ✓ |
| entropy_max | 0.0884 | 0.0884 | ✓ |
| entropy_min | -0.4062 | -0.4062 | ✓ |
| tail_decay | -0.0698 | -0.0698 | ✓ |

### 结论

- **是否匹配：是**，所有 7 个值精确匹配（diff < 0.001）
- **数据来源：** `/root/gen-depth-fingerprint/data/features_qwen3-1.7b.csv`（4617 条记录，Qwen3-1.7B-Base，pooled across all seeds，depths 0-4）
- **确认是同架构对比：** BASE_MODEL_RHO 确实来自 Qwen3-1.7B-Base，与 Qwen3-1.7B-Instruct 构成同架构 base/instruct 对比
- **与论文 pooled 6-gen 值不同的原因：** 论文报告的 hapax=-0.558 是跨 6 个生成器（model families）的 pooled 值；此处 -0.6696 是 Qwen3-1.7B-Base 单模型的 pooled Spearman ρ，两者统计口径不同，不矛盾

---
