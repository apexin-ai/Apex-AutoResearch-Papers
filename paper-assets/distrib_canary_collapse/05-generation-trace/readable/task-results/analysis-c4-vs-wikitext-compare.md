# analysis c4 vs wikitext compare

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_vs_wikitext_compare_20260518T203236_result.json`
- **Structured JSON:** [`08f8dc0a8bc70bf56d0a.json`](../../sessions/08/08f8dc0a8bc70bf56d0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析文件已写入。核心结果如下：

---

## 关键数据

| 指标 | C4 α=0.50 (gen0→10) | WikiText α=0.50 (gen0→10) |
|------|---------------------|--------------------------|
| entropy | 3.14 → 1.94 (**-38.2%**) | 3.23 → 2.63 (**-18.6%**) |
| perplexity | 24.4 → 122.8 (**+402%**) | 26.9 → 32.6 (**+21%**) |
| distinct_2 | 0.562 → 0.424 (-24.6%) | 0.518 → 0.251 (**-51.5%**) |
| distinct_3 | 0.873 → 0.686 (-21.5%) | 0.813 → 0.387 (**-52.4%**) |
| MAUVE | 0.691 → 0.078 (-88.7%) | 0.034 → 0.021 (-38.4%) |
| ECE | 0.011 → 0.258 (+23.5x) | 0.011 → 0.102 (+9.4x) |

## 根因：数据量差 159 倍

- **C4**: 4,500 样本，每代 ~4.4 epochs → 严重过拟合
- **WikiText**: 716,506 样本，每代 ~0.028 epochs → 几乎无过拟合

训练配置完全相同（5000 steps, batch_size 4, lr 5e-5），但 C4 数据量仅为 WikiText 的 1/159。

## 两种不同的 collapse 模式

1. **C4 = confidence collapse**：过拟合使模型逐代变得极度自信，entropy 单调下降，perplexity 爆炸（泛化崩溃），ECE 飙升。但词汇多样性下降反而较温和（distinct_2 仅 -24.6%），因为模型记住了小数据集的 n-gram 模式。

2. **WikiText = diversity collapse**：数据充足避免了过拟合（perplexity 仅 +21%），但迭代合成数据逐代削减词汇多样性（distinct_2 -51.5%），模型学会偏好高频模式、放弃低频表达。entropy 在 gen2 后稳定在 ~2.55。

## 额外注意

- WikiText gen0 MAUVE 仅 0.034（C4 为 0.691），基线已很低
- C4 用了 bf16，WikiText 用 fp32，存在混淆因素（但不足以解释 entropy -38% 的量级）
- 若要公平对比，需控制 epochs/gen 一致

---
