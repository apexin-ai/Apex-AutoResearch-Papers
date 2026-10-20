# analysis prevalence matched ablation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prevalence-matched-ablation_20260514T231011_result.json`
- **Structured JSON:** [`457b10ffe162c8697c8e.json`](../../sessions/45/457b10ffe162c8697c8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 关键发现：label agreement = 100%

2-LF conf≥2 的 4,017 个 window 上，3-LF 和 2-LF 标签 **完全一致**。当 file_diff 和 outcome_bp 都同意时，cmd_rep 无法翻转 majority vote。所以标签差异不是问题——**真正的混淆因素是训练数据量**：移除 cmd_rep 使可用 conf≥2 训练数据从 43,366 缩减到 4,017（10.8x）。

### Method A: 共同评估集 (N=54, stag=98%)

| Model | Macro-F1 |
|-------|----------|
| 3-LF  | 1.0000   |
| 2-LF  | 1.0000   |
| Delta | 0.0000   |

太小不具统计意义。

### Method B: Prevalence-matched (3-LF test set, N=6122, bootstrap 100x)

| Target stag | 3-LF F1 | 2-LF F1 | Delta | 95% CI |
|-------------|---------|---------|-------|--------|
| 19.2% (自然) | 0.9763 | 0.6822 | **-0.2941** | [-0.2949, -0.2942] |
| 50.0% | 0.9763 | 0.6822 | **-0.2941** | [-0.2941, -0.2941] |
| 80.0% | 0.9490 | 0.8635 | **-0.0854** | [-0.1098, -0.0666] |
| 96.3% | 0.8149 | 0.8363 | +0.0214 | [-0.0364, +0.0645] |

McNemar test (natural): χ²=1551.4, **p≈0** (3LF right & 2LF wrong: 1678 vs 反之 43)

### Method C: Cross-label (N=4017, 96% stag, labels 100% identical)

| Condition | Macro-F1 | 95% CI |
|-----------|----------|--------|
| 3-LF model | 0.9509 | [0.9326, 0.9662] |
| 2-LF model | 0.9707 | [0.9548, 0.9836] |

2-LF 在自己的训练分布上略优（+0.02），符合预期。

### 结论

**移除 cmd_rep 在公平对比下显著伤害性能。** 原始 -6.5pp delta 被两个因素混淆：
1. 不同的 test prevalence（19% vs 96%）
2. 不同的训练数据量（30K vs 2.8K）

在相同 test set 和 prevalence 下，3-LF 模型以 **29.4pp** 优势碾压 2-LF（0.9763 vs 0.6822）。只有在极端 96% stag prevalence 下两者持平（差异不显著）。**根本原因不是 cmd_rep 的标签质量（标签 100% 一致），而是移除 cmd_rep 后可用训练数据萎缩了 10 倍。**

---
