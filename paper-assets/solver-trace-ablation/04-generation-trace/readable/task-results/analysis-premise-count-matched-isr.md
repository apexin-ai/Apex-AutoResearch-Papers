# analysis premise count matched isr

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_premise-count-matched-isr_20260514T154703_result.json`
- **Structured JSON:** [`9a992094643ff5e77720.json`](../../sessions/9a/9a992094643ff5e77720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。所有三个任务的结果：

---

## Task 1: Premise-count-matched ISR — 完全验证

从 eval JSON 重新派生，数字与 r5 artifact 完全一致：

| Bucket | ISR n | ISR mean | Rnd n | Rnd mean | Δ |
|--------|-------|----------|-------|----------|---|
| 1 | 2 | 0.5000 | 0 | — | — |
| 2 | 13 | 0.9077 | 0 | — | — |
| 3 | 2 | 0.2500 | 4 | 0.4375 | **-0.1875** (Random 更高) |
| 4 | 0 | — | 0 | — | — |
| 5+ | 9 | 0.2595 | 19 | 0.2026 | +0.0569 |

**Matched (≥3 premises): ISR=0.2578 vs Random=0.2434, ratio=1.06x**

**结论：2.4x 是 premise-count 分布 artifact。** ISR genuine 57.7% 的样本在 ≤2 premises 桶（Random 在此桶为 0），LOO 删 1/2 premise 机械性地给出 ISR ≥ 0.5。在唯一重叠区间（≥3 premises），两者几乎无差异。n=3 桶中 Random 反而更高。

---

## Task 2: H1 计数差异 — 已解决

| Normalization | Random s42 H1 |
|---------------|---------------|
| strip | 56/79 |
| strip+collapse | 56/79 |
| strip+lower | 56/79 |
| strip+lower+nospace | 56/79 |
| alnum+lower | 61/79 |

所有四种合理 normalization 都给出 56/79。58 在任何 normalization 下都不可复现——可能来自旧的中间运行或不同的分类逻辑。**56/79 (70.9%) 为权威数字。**

---

## Task 3: genuine_isr_crosscheck.md — 已是最新

当前文件已是 r5 版本，所有修正均已到位：
- Section 3 正确显示 Random H1=56/79 (70.9%)、H7=0%，注明 conclusion embedding 是 GRPO-universal
- Section 5b 包含完整 premise-count-matched 分析
- 原始"Random 无 conclusion embedding, H1=0%"的错误已被替换

无需额外修改，也无需重新注册 artifact。

---
