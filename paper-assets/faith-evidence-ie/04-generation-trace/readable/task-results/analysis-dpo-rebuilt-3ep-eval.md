# analysis dpo rebuilt 3ep eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dpo_rebuilt_3ep_eval_20260523T133847_result.json`
- **Structured JSON:** [`91f57caace3a54ca9fce.json`](../../sessions/91/91f57caace3a54ca9fce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：NEGATIVE — 3 epoch DPO 确认过拟合。**

核心对比：

| 指标 | 1ep | 3ep | 变化 |
|------|-----|-----|------|
| **ign_f1** | 0.3223 | 0.3076 | **-4.6%** |
| ign_recall | 0.3820 | 0.3466 | -9.3% |
| ign_precision | 0.2787 | 0.2765 | -0.8% |
| **edcr** | 0.8123 | 0.7503 | **-7.6%** |
| evi_f1 (TP) | 0.8090 | 0.8484 | +4.9% |
| n_truncated | 175 | 220 | +25.7% |

过拟合机制：
- 训练 accuracy 持续上升（ep1 ~0.78 → ep3 ~0.87），但 eval ign_f1 下降 — 经典过拟合
- **recall 是主要受害者**（-9.3%），模型变得更保守，提取更少的关系
- **EDCR 显著下降**（-7.6%），更多 distractor 句子被引用
- **生成更冗长**（truncated +25.7%），输出更频繁触达 2048 token 上限

**1 epoch 是 DPO 的最佳训练时长。** 分析报告已写入 artifacts 并注册，registry 已更新为 DONE/negative。

---
