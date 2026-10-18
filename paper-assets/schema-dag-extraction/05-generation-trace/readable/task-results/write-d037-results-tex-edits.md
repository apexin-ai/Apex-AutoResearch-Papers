# write d037 results tex edits

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_d037_results_tex_edits_20260516T034134_result.json`
- **Structured JSON:** [`d8b6f6deeb38a1fc95cb.json`](../../sessions/d8/d8b6f6deeb38a1fc95cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。编译 0 错误，15 页。

改动摘要：
1. **§4.1 NER**: recall 改为 macro-avg (0.52/0.55)，加 bootstrap CI + permutation p=0.31 + 重叠说明
2. **§4.2 pairwise**: 在 Table 2 后讨论中加 cluster-robust CI（Few-NERD [0.057,0.190]，MAVEN [0.070,0.139]），Table 保留 pair-level CI
3. **§4.3 新段 Practical magnitude**: IQR=0.054 → 2.2pp gap，quartile 对比 3.9pp，P10-P90 4.2pp，明确 31.2pp 是 extreme-batch
4. **31.2pp 所有出现**（6处）均加 "extreme-batch" caveat 或指向 §practical_magnitude
5. **§4 开头**: 加 v1 prompt 总注
6. **§4.4**: Figure ref 改为 "Figure X in Appendix A"
7. **framework→pattern**: results.tex 中无 "framework"，无需改动
8. bibtex 有 3 个预存 warning（cite key 不匹配），非本次引入

---
