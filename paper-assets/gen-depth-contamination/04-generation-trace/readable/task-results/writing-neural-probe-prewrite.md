# writing neural probe prewrite

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_neural-probe-prewrite_20260514T055243_result.json`
- **Structured JSON:** [`705d043f234853af3002.json`](../../sessions/70/705d043f234853af3002.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

草稿已写入 `artifacts/drafts/neural_probe_analysis.tex` 并注册。

**内容结构：**

| 部分 | 内容 |
|------|------|
| **Setup** | frozen Qwen2.5-1.5B → avg-pool → MLP (1536→512→256→6), 5-fold GroupKFold |
| **Results** | K\*\_neural=3（2v3 AUC=0.6195±0.0094 > θ=0.60），1v2 margin 从 +0.0114 扩大到 +0.0983，3v4=0.5930 差 θ 仅 0.007 |
| **K\* hierarchy** | K\*\_theory ≥ K\*\_neural=3 ≥ K\*\_15D=2，"representation-dependent deepening" 叙事 |
| **Branch (a)** | exp-006 成功 → neural probe 的第三边界为 graduated filtering 的子分类提供动机 |
| **Branch (b)** | exp-006 不显著 → 第三边界主要是理论意义，操作建议不变（depth≥2 合并处理） |

所有 Qwen-cont 单数据集数字均标注 `% TODO: pending cross-model validation`，Pythia/OLMo 留 placeholder 注释，未编造数据。两个文本分支以注释块形式保留，根据 exp-006 结果取消注释对应版本即可。

---
