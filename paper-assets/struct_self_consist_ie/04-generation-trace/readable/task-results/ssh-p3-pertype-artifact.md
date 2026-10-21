# ssh p3 pertype artifact

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p3_pertype_artifact_20260521T213858_result.json`
- **Structured JSON:** [`5e139e2c8968003d085a.json`](../../sessions/5e/5e139e2c8968003d085a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已保存到 `artifacts/fewnerd_per_type_mv_analysis.md`。

## 汇报

### Per-Type MV Analysis Data

**数据来源**
- FewNERD, 8 coarse entity types, N=8 samples
- finetuned 3-epoch (fewnerd_mf4v2, seeds 42/123/456) + base model (exp_021, seed 42)
- 服务器 JSON: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_per_type_mv_analysis.json`

### 关键发现

**θ=0.5 (strict MV) 时出现强正相关**——与之前报告的 +0.90 吻合：

| 配置 | Pearson r | p-value |
|------|-----------|---------|
| exp_021, θ=0.5 | **+0.87** | **0.005** |
| mf4v2, θ=0.5 | +0.77 | 0.024 |

**θ=0.25 (liberal, 2/N) 时相关性不显著**（r=-0.52, p=0.19）且方向相反。

### 机制解释

- θ=0.5 是强过滤器：easy types（person, location）样本一致性高，MV 保留大部分实体；hard types（other, building）样本多样，MV 丢弃过多实体 → 大幅 F1 下降
- θ=0.25 允许更多样本贡献实体，反而让 hard types 受益（聚合多样的正确实体）
- 之前报告的 "Corr ≈ +0.90 (p=0.002)" 最可能对应 **exp_021 θ=0.5**（Pearson r=0.87, p=0.005），数值略有差异可能是筛选条件不同

---
