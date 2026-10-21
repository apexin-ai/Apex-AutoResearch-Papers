# paper related work mtl

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related_work_mtl_20260523T065237_result.json`
- **Structured JSON:** [`267dd069811f17e0f9ae.json`](../../sessions/26/267dd069811f17e0f9ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。

**related_work.tex** (lines 47-50): 在 "Auxiliary Tasks and Regularization" 子节中插入了 `\paragraph{Multi-Task Gradient Dynamics.}` 段落（12 句），结构为：
1. 介绍 GradNorm/PCGrad/CAGrad/NashMTL 的共同前提（gradient conflict）
2. 用实验数据（cosine ≈ 0, conflict rate 42-57%）说明本文处于 benign regime，conflict management 不适用
3. 核心论点：gradient amplification (8-69×) 而非 conflict resolution
4. EWC 连接：auxiliary supervision 通过 shared gradient flow 隐式实现类似 EWC 的 feature protection

**references.bib**: 新增 6 条 bib 条目（chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, kirkpatrick2017ewc），放在 Multi-Task Learning / Regularization 分区内。

---
