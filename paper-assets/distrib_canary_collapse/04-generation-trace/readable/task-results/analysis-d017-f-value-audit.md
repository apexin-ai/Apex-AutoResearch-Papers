# analysis d017 f value audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d017-f-value-audit_20260515T174116_result.json`
- **Structured JSON:** [`d0e48065bb48a211ceb9.json`](../../sessions/d0/d0e48065bb48a211ceb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。结论非常清晰：

## 结果

| 方向 | 处理方式 | F 统计量范围 | p 值范围 | 来源文件 |
|------|----------|-------------|---------|---------|
| **canary→diversity** | | | | |
| token_entropy→distinct_1 | **differenced** | **612–2615** | 0.001–0.011 | permutation_granger.json |
| token_entropy→distinct_1 | undifferenced | 200–501 | 0.002–0.008 | 同上 |
| token_entropy→distinct_2 | differenced | 226–1798 | 0.001–0.016 | 同上 |
| token_entropy→distinct_2 | undifferenced | 114–550 | 0.001–0.012 | 同上 |
| token_entropy→distinct_3 | differenced | 95–738 | 0.001–0.027 | 同上 |
| token_entropy→distinct_3 | undifferenced | 101–232 | 0.002–0.011 | 同上 |
| ece→distinct_1 | differenced | 567–6124 | 0.001–0.002 | 同上 |
| ece→distinct_1 | undifferenced | 84–3370 | 0.001–0.005 | 同上 |
| ece→distinct_2 | differenced | 171–7643 | 0.001–0.009 | 同上 |
| ece→distinct_2 | undifferenced | 124–249 | 0.001–0.002 | 同上 |
| ece→distinct_3 | differenced | 71–921 | 0.001–0.016 | 同上 |
| ece→distinct_3 | undifferenced | 74–236 | 0.001–0.006 | 同上 |
| **canary→perplexity** | | | | |
| token_entropy→perplexity | undifferenced | 16–36 | 0.015–0.052 | 同上 |
| token_entropy→perplexity | **differenced** | **≈0–0.3** | **0.47–0.99** | 同上 |
| ece→perplexity | undifferenced | 12–25 | 0.013–0.039 | 同上 |
| ece→perplexity | **differenced** | **≈0–0.6** | **0.35–0.96** | 同上 |

---

## 结论

**F=612–2615 属于 First-Differenced，不是 Undifferenced。**

- `token_entropy→distinct_1` 的 **differenced** F 范围恰好是 612.1–2614.8，与论文标注的 "F=612-2615" 精确吻合
- 同一对的 **undifferenced** F 范围是 199.5–501.1，远小于 612

**图 Panel (a) 标注有误**：如果 F=612-2615 被标在 Undifferenced 列，需要移到 First-Differenced 列。paper_framing.md 的说法（"差分後仍 4/4 seed 顯著，F=612-2615"）是正确的。

canary→perplexity 方向的标注是正确的：undifferenced F=16-36，differenced F≈0（p=0.99）。

---
