# analysis qwen25 7b selfref 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen25_7b_selfref_001_20260523T024054_result.json`
- **Structured JSON:** [`13ee4d095b9bb235a6cc.json`](../../sessions/13/13ee4d095b9bb235a6cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验 qwen25_7b_selfref_001 结果总结

### 核心指标

| 指标 | 值 |
|------|-----|
| RF 4-class acc | **52.05%** (CI: 51.35%-52.71%) |
| LR 4-class acc | 48.79% (CI: 48.09%-49.48%) |
| RF 3-class (d1/d2/d3) | 51.87% (CI: 51.06%-52.70%) |
| Chance baseline | 25% (4-class) / 33.3% (3-class) |

### Pairwise AUC（RF）

| 对比 | AUC | 解读 |
|------|-----|------|
| d0 vs d1 | 0.697 | 相邻深度，最难区分 |
| d0 vs d2 | 0.895 | |
| d0 vs d3 | **0.957** | 距离越远越易区分 |
| d1 vs d2 | 0.673 | |
| d1 vs d3 | 0.844 | |
| d2 vs d3 | 0.659 | 相邻深度，最难区分 |

AUC 呈清晰的**单调递增模式**：深度差越大，区分度越高。

### 与 14B 对比

| | Qwen2.5-14B (nucleus) | Qwen2.5-7B self-ref |
|---|---|---|
| RF 4-class acc | ~54.05% | 52.05% |
| 差异 | — | -2.0pp |

7B 仅比 14B 低约 2 个百分点，信号强度非常接近。

### Top-5 特征
`p90_ppl`, `skew_ppl`, `p90_surprisal`, `kurt_ppl`, `var_surprisal` — 以 perplexity 尾部统计量为主导。

### Hypothesis 验证

**Confirmed.** 递归生成深度信号在 Qwen2.5-7B + self-reference 条件下持续存在：
- 4-class 准确率 52.05%，远超 chance (25%)，置信区间不含 25%
- 去掉 d0 后 3-class 仍有 51.87%（chance=33.3%），证明 d1-d3 之间有可分性
- Pairwise AUC 单调模式与 14B 一致
- 与 14B 差距极小（~2pp），支持 depth signal 非模型规模特异性的结论

**Conclusion: SUCCESS**

---
