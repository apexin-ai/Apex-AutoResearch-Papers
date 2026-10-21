# paper check abstract

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_check_abstract_20260524T212524_result.json`
- **Structured JSON:** [`8dfb9a12982088dd1445.json`](../../sessions/8d/8dfb9a12982088dd1445.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Abstract 全文

```latex
Fine-tuned Vision-Language-Action (VLA) models can achieve high task success rates yet remain
behaviorally unsafe: on SafeLIBERO Level~I, OpenVLA attains 90.7\% task success but only 78.0\%
collision avoidance.
This paper presents the first factorial study isolating how auxiliary spatial supervision during
VLA fine-tuning affects collision avoidance.
Multiple conditions on OpenVLA-OFT with LoRA vary gradient flow, label content, spatial reference
frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth
labels), Random OCC (random binary labels), Detach OCC (encoder gradients blocked), Detach+LN
(LayerNorm replacing BatchNorm), Depth (egocentric depth prediction), Cutoff@\{15K--45K\}
(gradient flow for the first $N$ of 50K steps), and Reverse Cutoff (gradient flow for the last
15K steps only).
The central finding is that the Detach OCC degradation ($-$3.4\,pp CAR vs.\ Vanilla) decomposes
into two mechanistically distinct pathways: BatchNorm interference accounts for all
representational drift (replacing BN with LayerNorm recovers pretrained CKA to Vanilla level and
1.9\,pp CAR; Detach+LN 0.765), while gradient flow absence costs a modest additional 1.5\,pp
(within statistical uncertainty) through behavioral regularization beyond representation
preservation. Gradient norms fall to 1--13\% of baseline under gradient detachment; BatchNorm
interference drives representations away from pretrained features (CKA dropping to 0.31--0.54),
while Detach+LN (LayerNorm substitution) fully recovers pretrained CKA despite retaining
\texttt{stop\_gradient}. Full OCC and Random OCC maintain encoder gradient norms at
0.87--1.14$\times$ baseline, preserve pretrained representations (CKA $\geq$ 0.95), and CAR
within 1.7\,pp of Vanilla (78.0--79.7\%).
Within the variance of our experiments, label content type does not significantly affect downstream
safety metrics: structured occupancy, random binary maps, and egocentric depth yield comparable
collision avoidance when gradient flow is maintained.
Cutoff@35K retains high task success (93.3\%) with CAR statistically indistinguishable from Vanilla
($-$0.1\,pp); preliminary cutoff experiments suggest that gradient flow \emph{continuity} matters
more than mere existence---mid-training transitions between gradient-flow and Detach modes
introduce seed-dependent outcome variability not observed under consistent training regimes.
Because the auxiliary head is discarded after training, these spatial losses add zero inference
cost and require no ground-truth spatial labels at deployment.
```

---

## 检查点评估

### a) Dual mechanism (BN interference + gradient flow absence)
**一致。** 明确描述了"two mechanistically distinct pathways"：BN interference 贡献 1.9pp，gradient flow absence 贡献 1.5pp，合计 3.4pp。比例 56%/44% 未显式给出，但数字可推算（1.9/3.4=56%, 1.5/3.4=44%）。

### b) Representation-behavior dissociation (CKA 恢复但 CAR 仍低)
**一致。** "Detach+LN (LayerNorm substitution) fully recovers pretrained CKA despite retaining `stop_gradient`"，同时 Detach+LN CAR = 0.765 仍低于 Vanilla 0.780。CKA 恢复 + CAR 仍有 1.5pp gap = dissociation 概念在。但 abstract 未使用 "representation-behavior dissociation" 这一术语。

### c) Existence regularization
**部分缺失。** "existence regularization" 一词未出现。概念通过 Random OCC ≈ Full OCC 的结果和"label content type does not significantly affect"间接传达，但未提炼为明确的 framing term。Abstract 更侧重 "gradient flow continuity" 而非 "existence regularization"。

### d) 数字核查

| 指标 | Abstract 值 | 参考值 | 判定 |
|------|------------|--------|------|
| Full OCC CAR | 范围 78.0–79.7% 中的上界 → 0.797 | 0.797 | **一致** |
| Detach CAR | 78.0% − 3.4pp = 74.6% → 0.746 | 0.746 | **一致** |
| Vanilla CAR | 78.0% | 0.780 | **一致** |
| Random OCC CAR | 范围 78.0–79.7% 内（隐含） | 0.789 | **一致**（未单独列出） |
| Detach+LN CAR | 0.765 | 0.765 | **一致** |

所有数字与参考值吻合。

### e) 过时或不准确的 claim
未发现明显不准确的 claim。

---

## 建议修改

1. **引入 "existence regularization" 术语。** 这是当前核心叙事的关键概念，但 abstract 中完全缺失。建议在描述 Random OCC ≈ Full OCC 发现处加入，例如将 "behavioral regularization beyond representation preservation" 改为更明确的 "existence regularization — the mere presence of auxiliary gradient flow, regardless of label content, regularizes encoder training"。

2. **显式点出 representation-behavior dissociation。** 目前 CKA 恢复与 CAR 仍低的对比分散在两处，读者需自行拼接。建议用一句话明确："This reveals a representation-behavior dissociation: recovering pretrained representations (CKA) is necessary but not sufficient for recovering safety behavior (CAR)."

3. **Abstract 偏长。** 当前约 280 词，CoRL 通常建议 150–200 词。Cutoff 实验细节（Cutoff@35K 的具体数字、continuity vs. existence 的讨论）可压缩或移至正文，为核心 message 留出空间。

---
