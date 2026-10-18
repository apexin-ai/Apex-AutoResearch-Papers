# ssh maven minilm pertype

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_maven-minilm-pertype_20260515T090030_result.json`
- **Structured JSON:** [`ca9c21241104f38a8a0e.json`](../../sessions/ca/ca9c21241104f38a8a0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `artifacts/maven_minilm_pertype_analysis.json`。

---

## 结果汇报

### Layer 2: Per-type F1 vs Mean BCS

| Embedding | Spearman ρ | p | Pearson r | Partial r (ctrl logfreq) |
|-----------|-----------|---|-----------|--------------------------|
| **MiniLM** | **+0.2075** | **0.011** | +0.1696 | +0.1327 (p=0.107) |
| Qwen3 | +0.1837 | 0.025 | +0.1753 | +0.1890 (p=0.021) |

**两个 embedding 方向完全一致：ρ > 0（高 BCS → 高 F1）。** MiniLM 甚至比 Qwen3 还更正（+0.21 vs +0.18）。

### Layer 1: Pairwise SCS vs Confusion

| Embedding | Pearson r | Spearman ρ | Nonzero-only ρ |
|-----------|-----------|-----------|-----------------|
| **MiniLM** | **+0.1201 (p≈0)** | **+0.0934 (p≈0)** | +0.1907 (p<0.001) |
| Qwen3 | -0.0070 (p=0.41) | +0.0033 (p=0.70) | -0.0433 (p=0.27) |

MiniLM 在 pairwise 层面反而有效：更相似的 type pair 确实更容易混淆（r=+0.12，高度显著）。Qwen3 在 pairwise 层面完全无信号。

### 结论

**假设被否定。** MiniLM × MAVEN 的 per-type ρ = +0.2075 > 0，与 Qwen3 方向相同。MAVEN 上 BCS-F1 正相关不是 Qwen3 same-domain compression 造成的——是 MAVEN event types 的 **intrinsic property**：语义邻居多的 type（高 mean BCS）往往是常见、中心化的类型（如 Attack, Death），LLM 本身就擅长抽取；而孤立 type 是冷门类型，F1 天然低。

**但 Layer 1 有亮点**：MiniLM 在 pairwise 层面能捕捉 type confusability（ρ=0.09, p≈0），Qwen3 完全不能。这说明 MiniLM 确实更好捕捉 pairwise confusability，但在 per-type 聚合后被 frequency/popularity confound 主导。

### 更新后的 2×3 矩阵

| | Few-NERD | FewRel | MAVEN |
|---|---|---|---|
| **Qwen3** | ρ=-0.293 (p=0.020) ✓ | pending | ρ=+0.189 (p=0.021) ✗ |
| **MiniLM** | ρ=+0.005 (p=0.969) ✗ | Δ=21-50pp ✓ | **ρ=+0.208 (p=0.011) ✗** |

MAVEN 列两个 embedding 都是正方向，问题出在 MAVEN 数据本身，不在 embedding。

---
