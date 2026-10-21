# paper d047 round1 compression

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d047_round1_compression_20260516T123803_result.json`
- **Structured JSON:** [`b245b6f94cfda70e1ab4.json`](../../sessions/b2/b245b6f94cfda70e1ab4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Summary:

**Results:**
1. **Compilation**: Clean — no errors, no undefined references, no multiply-defined labels
2. **Body pages**: 7 pages (sections 1–7 + Limitations fit within pp. 1–7; checklist starts p.8). The compression freed ~1 page of vertical space within the body (§4.1 went from 6 `\paragraph` blocks to 1 paragraph; Table 3 + within-pool table + interpretation moved to appendix).
3. **New appendix labels** all resolve correctly:
   - `app:bcs-controlled-table` → Appendix J (p.16)
   - `app:within-pool-method` → Appendix K (p.16)
   - `app:scs-ablation` → Appendix L (p.16)
   - `app:aggregation-sim` → Appendix M (p.16)

**Changes made:**
- **A1**: §4.1 compressed from 6 `\paragraph` blocks to single unified paragraph
- **A2**: `tab:bcs_controlled` moved to Appendix J; inline summary in §4.3
- **A3**: Within-pool methodology + `tab:within_pool` moved to Appendix K; one-liner replacement
- **D3**: Cluster bootstrap CIs added to `tab:pairwise` caption
- **F**: Aggregation sentence corrected (7% → 22%, ~3× with MC simulation reference)
- **E**: Three new appendix sections added (SCS ablation, within-pool method, aggregation sim)

---
