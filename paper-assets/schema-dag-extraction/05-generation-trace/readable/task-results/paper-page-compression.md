# paper page compression

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_page_compression_20260516T082034_result.json`
- **Structured JSON:** [`ccba7997617d6f148abd.json`](../../sessions/cc/ccba7997617d6f148abd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

压缩完成。结果：

**最终页数：正文 7 页**（通过 Conclusion 结束在第 7 页中部），远低于 8 页目标。从原始 ~10 页缩减了约 3 页。

**各策略贡献��**

| 策略 | 估计节省 |
|------|---------|
| §5 batch composition table → Appendix | ~0.3 页 |
| §2 Related Work 压缩（3 subsections → 3 paragraphs） | ~0.4 页 |
| §4.5 Centrality confound 精简 | ~0.15 页 |
| §4 practical_magnitude 精简 | ~0.15 页 |
| 全局 tightening（intro、pairwise、prompt sensitivity、cross-model、DocRED、multi-channel、SDGD、discussion、limitations、experimental setup） | ~2.0 页 |

**各 section 页面占比（大致）：**
- Introduction: pp 1–2 (1.5 页)
- Related Work: p 2–3 (0.5 页)
- Experimental Setup: pp 3–4 (1.5 页)
- Results: pp 4–6 (2.5 页)
- SDGD: pp 6–7 (0.7 页)
- Discussion + Conclusion: p 7 (0.3 页)

**验证：**
- 无 undefined citations / broken references
- 所有 `\ref{tab:batch_composition}` 引用指向 Appendix 中的 table
- Appendix 中新增 §Batch Composition Results 独立可读
- 所有定量 claim 和 exp_id 引用保留完整

---
