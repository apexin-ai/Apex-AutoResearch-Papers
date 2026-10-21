# ssh embedding ablation miniml fewnerd

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_embedding-ablation-miniml-fewnerd_20260515T075628_result.json`
- **Structured JSON:** [`39aaab3ed40a021fd3e6.json`](../../sessions/39/39aaab3ed40a021fd3e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个产出文件已生成。汇报结果：

---

## Embedding Ablation: Qwen3 vs MiniLM on Few-NERD

### BCS 分布差异

| 指标 | Qwen3 | MiniLM |
|------|-------|--------|
| mean | 0.808 | 0.195 |
| std | 0.060 | 0.144 |
| range | [0.44, 0.97] | [-0.05, 0.86] |

MiniLM 的 BCS 分布远比 Qwen3 分散（std 更大、均值更低）。Qwen3 embeddings 普遍高相似度（mean 0.81），MiniLM 区分度更好。

### 矩阵级相关

- 两个矩阵 off-diagonal 元素 Pearson r=0.355, Spearman ρ=0.335 — **弱正相关**，整体排序不一致
- Top-10 最高 BCS pairs 仅 **2/10 重叠**（sportsleague-sportsteam, actor-director）

### Per-type F1 vs mean_BCS 相关（n=63 types, freq≥5）

| Embedding | Spearman ρ | p-value | Pearson r | p-value |
|-----------|-----------|---------|-----------|---------|
| **Qwen3** | **-0.281** | **0.026** | -0.181 | 0.157 |
| MiniLM | 0.005 | 0.969 | -0.112 | 0.383 |

- **Qwen3 的 BCS 与 per-type F1 显著负相关**（ρ=-0.281, p=0.026），符合之前的发现（ρ=-0.293）
- **MiniLM 完全无相关**（ρ≈0, p=0.97）
- 两种 embedding 的 mean_BCS per type 几乎不相关（r=0.188, p=0.14）

### 解读

Embedding 选择**显著影响** BCS-F1 关联方向和强度。Qwen3（与抽取模型同源的 LLM embedding）能捕捉到"语义混淆 → F1 下降"的信号，而通用 sentence encoder MiniLM 不能。这**支持**使用 Qwen3 作为 BCS 计算模型的方法论一致性论点：extraction model 的内部语义空间才是 confusion 的真正来源。

### 产出文件
- `artifacts/fewnerd_bcs_matrix_minilm.pt` — MiniLM 66×66 similarity matrix
- `artifacts/embedding_ablation_fewnerd.json` — 完整对比分析数据

---
