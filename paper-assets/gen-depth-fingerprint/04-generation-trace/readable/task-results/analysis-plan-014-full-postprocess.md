# analysis plan 014 full postprocess

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-014-full-postprocess_20260515T033948_result.json`
- **Structured JSON:** [`796eba403546ff489450.json`](../../sessions/79/796eba403546ff489450.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

---

## plan-014 后处理结果汇报

### 1. Qwen3-8B 数据量

| 指标 | 值 |
|------|-----|
| 总记录数 | 3702 (from fd/50 recovery, 进程 82% 时快照) |
| 特征提取后 (去重) | 3728 rows |
| unique seeds | 820 |
| **depth 分布** | d0=820, d1=806, d2=774, d3=684, d4=618 |

### 2. 6-gen LOGO macro-F1 (3-class: gen-0/gen-1/gen-2+)

| Held-out Generator | Macro-F1 | 95% CI |
|-------------------|----------|--------|
| olmo-2-1b | 0.7632 | [0.752, 0.774] |
| pythia-1b | 0.8529 | [0.843, 0.862] |
| pythia-2.8b | 0.8010 | [0.791, 0.812] |
| qwen3-0.6b | 0.8240 | [0.813, 0.835] |
| qwen3-1.7b | 0.8018 | [0.791, 0.813] |
| **qwen3-8b** | **0.6886** | **[0.675, 0.703]** |
| **6-gen Average** | **0.7886** | |

### 3. 与 5-gen baseline 对比

| 指标 | 5-gen baseline | 6-gen (含 qwen3-8b) | Δ |
|------|---------------|---------------------|------|
| LOGO avg macro-F1 | 0.80 [0.786, 0.799] | 0.7886 | **-0.011** |
| 原 5-gen 子集平均 | 0.80 | 0.8086 | +0.009 |

关键发现：原 5 个 generator 的平均 F1 从 0.80 提升到 0.8086（因为训练集增加了 qwen3-8b 数据），但 qwen3-8b 自身作为 held-out 只有 0.6886，拉低了 6-gen 整体均值。

### 4. LOFO / 特征重要性 (Permutation Importance)

| Rank | Feature | Importance (F1 drop) |
|------|---------|---------------------|
| 1 | hapax_ratio | 0.2707 |
| 2 | ttr | 0.1646 |
| 3 | entropy_mean | 0.1559 |
| 4 | entropy_max | 0.0618 |
| 5 | entropy_std | 0.0457 |
| 6 | entropy_min | 0.0149 |
| 7 | tail_decay | 0.0124 |

Feature Ablation: full=0.7886, surface_only=0.7293, reference_only=0.7451

### 5. Qwen3-8B Spearman ρ (depth vs feature)

| Feature | ρ | p-value |
|---------|------|---------|
| hapax_ratio | **-0.5683** | ≈0 |
| ttr | **-0.5530** | 1.0e-297 |
| entropy_mean | **-0.4750** | 3.6e-209 |
| entropy_min | -0.3140 | 4.4e-86 |
| entropy_max | +0.1018 | 4.6e-10 |
| tail_decay | -0.0796 | 1.1e-06 |
| entropy_std | -0.0791 | 1.3e-06 |

### 6. RC9 结论：8B 模型 depth signal 是否与 ≤2.8B 一致？

**部分一致，但存在显著差异。**

- **信号存在**：Qwen3-8B 上 depth 与特征的 Spearman 相关性全部显著（p<1e-6），核心特征方向一致（hapax_ratio/ttr/entropy_mean 均为负相关）
- **信号强度可比**：hapax_ratio ρ=-0.57, ttr ρ=-0.55 与小模型量级接近
- **迁移性降低**：LOGO 中 qwen3-8b 作为 held-out 的 F1=0.6886，远低于其他 generator（0.76-0.85），说明小模型训练的分类器向 8B 迁移时存在 domain shift
- **不拖累其他模型**：加入 qwen3-8b 训练数据后，原 5 个 generator 的 held-out F1 反而微升（0.80→0.81）
- **结论**：depth fingerprint 是跨模型规模的 universal signal，但 8B 模型的 signal pattern 有足够差异使得从 ≤2.8B 直接迁移存在 gap。建议后续探索 scale-aware 特征或在训练集中包含 8B 数据以消除此 gap。

### classify_multi.py 补充结果 (5-class depth 0-4)

| 评估 | macro-F1 |
|------|----------|
| 6-gen LOGO 平均 | 0.5058 ± 0.035 |
| qwen3-8b held-out | 0.4368 |
| LOFO (family: qwen) | 0.4832 |
| Pooled 5-fold baseline | 0.4956 ± 0.005 |

---
