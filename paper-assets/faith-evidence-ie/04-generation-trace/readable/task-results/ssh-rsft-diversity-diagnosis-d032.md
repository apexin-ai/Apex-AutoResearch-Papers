# ssh rsft diversity diagnosis d032

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-diversity-diagnosis-d032_20260515T010821_result.json`
- **Structured JSON:** [`799214b58ff6de9452b6.json`](../../sessions/79/799214b58ff6de9452b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**VERDICT: VIABLE** — RSFT 可行，继续跑生成。

| 指标 | 值 | 判断阈值 |
|------|------|---------|
| mean_std(ced_score) | **0.1189** | >0.05 ✓ |
| median_std(ced_score) | 0.0992 | — |
| top2-bottom2 gap | **0.2736** | >0.1 ✓ |
| median top2-bot2 gap | 0.2364 | — |
| mean evidence Jaccard | 0.8680 | (高=evidence重叠多) |

**CED 分布**: min=0.00, p25=0.35, median=0.57, p75=0.78, max=1.00

**关键发现**：

- 虽然 triple-set diversity 很低（Jaccard 0.87 = evidence 句子高度重叠），但 **CED score 方差足够大**（std=0.12, top2-bot2 gap=0.27）
- 这意味着即使 8 个 generation 提取的 triple 集合相似，它们选择的 evidence 质量有明显差异
- RSFT 用 CED score 做 top-k 筛选是有效的——每个 doc 的 best 和 worst generation 平均 CED 差 0.27

**结论**：diversity 危机只存在于 triple-set 层面，CED score 维度仍有充足选择信号。继续跑 RSFT 生成，后续用 top-25% CED 筛选即可。

（236 docs 已生成，详细 per-doc 结果存在 `/root/autodl-tmp/rsft_diversity_diag_results.json`）

---
