# code mvp semantic collect

**contrastive graph jailbreak detect** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-semantic-collect_20260517T074444_result.json`
- **Structured JSON:** [`5bea5ef97453cb1d77e7.json`](../../sessions/5b/5bea5ef97453cb1d77e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results collected. Here is the complete MVP Round 2 (semantic embedding) final report:

---

## MVP Round 2 完整结果 — 语义 Embedding

### In-Distribution 5-Fold CV

| Model | AUROC | F1 |
|-------|-------|-----|
| GIN+SupCon | 0.8687 ± 0.0303 | 0.7606 ± 0.0557 |
| RF Baseline | 0.9704 ± 0.0062 | 0.9027 ± 0.0226 |

### GIN+SupCon Leave-One-Out Holdout (10 failure modes)

| Mode | AUROC | F1 | Precision | Recall | Description |
|------|------:|---:|----------:|-------:|-------------|
| FM1 | 0.8712 | 0.7158 | 0.7083 | 0.7234 | Generates harmful content |
| FM2 | 0.8189 | 0.6024 | 0.6250 | 0.5814 | Fails to filter tool results |
| FM3 | 0.9019 | 0.7789 | 0.7872 | 0.7708 | Calls tools with incomplete info |
| FM4 | 0.9092 | 0.7706 | 0.7241 | 0.8235 | Calls tools before obtaining info |
| FM5 | 0.7689 | 0.6542 | 0.6034 | 0.7143 | Ignores known constraints |
| FM6 | 0.7921 | 0.6230 | 1.0000 | 0.4524 | Ignores implicit risks |
| FM7 | 0.8515 | 0.7826 | 0.9730 | 0.6545 | Incorrect tool parameters |
| FM8 | 0.8278 | 0.7556 | 0.8500 | 0.6800 | Ignores tool issues |
| FM9 | 0.8721 | 0.7629 | 0.7400 | 0.7872 | Fails to call necessary tools |
| FM10 | 0.8612 | 0.7455 | 0.6949 | 0.8039 | Trusts tool results without validation |
| **Mean** | **0.8475 ± 0.0431** | **0.7191 ± 0.0643** | | | |

### RF Baseline Leave-One-Out Holdout

| Mode | AUROC | F1 | Precision | Recall |
|------|------:|---:|----------:|-------:|
| FM1 | 0.9674 | 0.8372 | 0.9231 | 0.7660 |
| FM2 | 0.9651 | 0.8052 | 0.9118 | 0.7209 |
| FM3 | 0.9814 | 0.8913 | 0.9318 | 0.8542 |
| FM4 | 0.9671 | 0.9091 | 0.9375 | 0.8824 |
| FM5 | 0.9342 | 0.8046 | 0.9211 | 0.7143 |
| FM6 | 0.9683 | 0.9157 | 0.9268 | 0.9048 |
| FM7 | 0.9774 | 0.9057 | 0.9412 | 0.8727 |
| FM8 | 0.9237 | 0.8842 | 0.9333 | 0.8400 |
| FM9 | 0.9735 | 0.9247 | 0.9348 | 0.9149 |
| FM10 | 0.9643 | 0.8387 | 0.9286 | 0.7647 |
| **Mean** | **0.9622 ± 0.0176** | **0.8716 ± 0.0436** | | |

### MVP Gate Assessment

| Criterion | Value | Threshold | Result |
|-----------|-------|-----------|--------|
| GIN holdout avg AUROC | 0.8475 | > 0.70 | **PASS** |
| GIN vs RF delta | -11.5 pp | > +5 pp | **FAIL** |
| **Overall** | | | **FAIL** |

### Per-Graph-Size Analysis

| Group | Count | Attack | Benign | Attack Rate |
|-------|------:|-------:|-------:|------------:|
| Small (≤3 nodes) | 913 | 480 | 433 | 52.6% |
| Large (≥4 nodes) | 170 | 3 | 167 | 1.8% |

Graph structure extremely sparse: 666/1083 graphs (61.5%) have **0 edges**. Only 66/1083 (6.1%) have ≥2 edges.

### 关键发现

1. GIN+SupCon 通过绝对 AUROC 门槛 (0.8475 > 0.70)，但 **大幅落后于 RF baseline** (-11.5 pp)
2. RF 在 holdout 场景下极为稳定 (0.9622 ± 0.0176)，GIN 方差更大 (0.8475 ± 0.0431)
3. 数据集图结构极其稀疏 (61.5% 无边)，graph size 与标签高度相关 (大图几乎全是 benign)，RF 可以直接利用这些简单统计特征
4. GIN 无法从当前的稀疏图结构中学到比节点级特征聚合更有用的信息

### 修复记录
- FM4 和 FM10 因 BatchNorm 在 batch_size=1 时崩溃，已通过 `drop_last=True` 修复并补跑

---
