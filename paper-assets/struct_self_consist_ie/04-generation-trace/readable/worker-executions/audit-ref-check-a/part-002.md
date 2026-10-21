# audit ref check A — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-ref-check-a.md) · [Structured JSON](../../../sessions/74/74a4ffb6e0cb24b5566f.json)

## Round 1

### Tool result

_source line 463 · 2026-05-26T11:09:33.448Z_

<details><summary>↩ Tool result · `toolu_01EkTmUsAakTnTXGi5VSYT8x`</summary>

```text
# Authors of arXiv:1908.05731

Based on the webpage, the four authors listed for this paper are:

1. Kyra Yee
2. Nathan Ng
3. Yann N. Dauphin
4. Michael Auli

These names appear in the "Authors:" section and are repeated in the DBLP bibliography section at the bottom of the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ad4ad56d-41fb-42ee-b372-4b9b467aab9d",
  "uuid": "f6d02f4b-d1e6-463a-b545-6b07a02b3085",
  "tool_use_result": {
    "bytes": 45656,
    "code": 200,
    "codeText": "OK",
    "result": "# Authors of arXiv:1908.05731\n\nBased on the webpage, the four authors listed for this paper are:\n\n1. Kyra Yee\n2. Nathan Ng\n3. Yann N. Dauphin\n4. Michael Auli\n\nThese names appear in the \"Authors:\" section and are repeated in the DBLP bibliography section at the bottom of the page.",
    "durationMs": 2504,
    "url": "https://arxiv.org/abs/1908.05731"
  }
}
```

</details>

---


### Assistant

_source line 464_

<details><summary>Logged reasoning block</summary>

```text
So the situation is:
- The arXiv version has 4 authors: Kyra Yee, Nathan Ng, Yann N. Dauphin, Michael Auli
- The ACL Anthology (EMNLP-IJCNLP 2019 proceedings) version has 3 authors: Kyra Yee, Yann Dauphin, Michael Auli (no Nathan Ng)

This is a discrepancy between the arXiv and proceedings versions. Since the bib entry cites it as an EMNLP-IJCNLP 2019 proceedings paper, it should match the proceedings author list, which has 3 authors. 

Actually, looking at the bib entry itself, it lists exactly those 3 authors—Yee, Dauphin, and Auli—which matches the proceedings version perfectly. So the bib is correct as-is, despite what the agent claimed about Nathan Ng being missing. The arXiv version includes an extra author that doesn't appear in the published proceedings—this kind of author change between preprint and final publication is unusual enough to warrant flagging as a note. Now I'm compiling the final report with all the verification results and issues I've found across the 64 papers. The arXiv version lists four authors while the proceedings version has three, and the bib entry's arXiv URL doesn't match this discrepancy. For the second author issue, the bib shows "Wang, Yang" as the ninth author but Semantic Scholar only lists nine authors total without that name, so I need to verify the actual publisher record. I've also found three unused bibliography entries that are either referenced by name in the text but never formally cited, or not mentioned anywhere at all. There's one more minor issue where the cite key includes "2023" but the year field correctly reflects the 2024 TMLR publication date.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ad4ad56d-41fb-42ee-b372-4b9b467aab9d",
  "uuid": "ce007cc1-325e-4097-9fcb-29a4fa52cfd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019x5A7oT32qikAcnV7vF6XG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 109560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 294
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 465_

All verifications complete. Let me now compile and write the final report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ad4ad56d-41fb-42ee-b372-4b9b467aab9d",
  "uuid": "f7736740-6480-4b52-b1b3-0efc06f2348b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019x5A7oT32qikAcnV7vF6XG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 109560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 294
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 466_

<details open><summary>🔧 Tool call — Write · `toolu_01K6SVMZME98KzHJFny453EM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ref_audit_worker_A.md",
  "content": "# 引用验证清单 (Worker A — Semantic Scholar 优先)\n\n**验证日期**: 2026-05-26\n**验证手段**: Semantic Scholar API + WebSearch fallback (ACL Anthology, arXiv, OpenReview, PMLR, NeurIPS proceedings)\n\n总 bib entries: **64**\n总 unique cite keys in tex: **61**\n未使用的 bib entries: `holm1979simple`, `li2024simple`, `xiao2022uncertainty`\ntex 中引用但 bib 缺失: **无**\n\n---\n\n## 总结\n\n| 类别 | 数量 |\n|------|------|\n| 论文真实存在 | 64/64 (100%) |\n| 完全匹配 (无任何问题) | 58 |\n| 需修正 (⚠️) | 3 |\n| 需关注 (注意事项) | 3 |\n| 严重问题 (❌ 虚假引用) | 0 |\n\n---\n\n## 需修正的条目\n\n### ⚠️ [li2023stepaware] — 标题多了 \"Large\"\n- **Bib 标题**: \"Making **Large** Language Models Better Reasoners with Step-Aware Verifier\"\n- **ACL 2023 proceedings 标题**: \"Making Language Models Better Reasoners with Step-Aware Verifier\"\n- **来源**: ACL Anthology 2023.acl-long.291 确认无 \"Large\"；arXiv:2206.02336 版本有 \"Large\"\n- **建议**: 既然 bib 引用的是 ACL 2023 proceedings，应使用 proceedings 标题，删除 \"Large\"\n\n### ⚠️ [yee2019noisy] — arXiv 与 proceedings 作者列表不一致\n- **Bib 作者**: Yee, Dauphin, Auli (3人)\n- **ACL Anthology D19-1571**: Yee, Dauphin, Auli (3人) ← bib 匹配 proceedings\n- **arXiv:1908.05731**: Yee, **Ng**, Dauphin, Auli (4人)\n- **问题**: Bib 的 URL 指向 arXiv (4人版本)，但作者列表只有 3 人（匹配 proceedings）。建议统一：要么加上 Nathan Ng（匹配 arXiv），要么将 URL 改为 ACL Anthology 链接\n\n### ⚠️ [holm1979simple] — 方法被引用但未 \\cite\n- **现状**: 论文正文多次提及 \"Holm--Bonferroni\" 方法（至少 15 次），但从未使用 `\\cite{holm1979simple}`\n- **建议**: 在首次提及 Holm--Bonferroni 时添加 `\\cite{holm1979simple}`\n\n---\n\n## 需关注的条目\n\n### 📝 [snell2025scaling] — arXiv 与 ICLR proceedings 标题不同\n- **Bib 标题**: \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\"\n- **arXiv 标题**: \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\"\n- **ICLR 2025 proceedings 标题**: \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\"\n- **结论**: Bib 使用了 ICLR proceedings 标题，技术上正确。但注意 arXiv 版本标题不同。\n\n### 📝 [xu2024llmie] — 作者 \"Wang, Yang\" 在 S2 中未出现\n- **Bib 作者**: 10人（含 Wang, Yang）\n- **Semantic Scholar**: 9人（无 Wang, Yang）\n- **结论**: 需对照 Springer 出版商页面确认。S2 数据可能不完整。\n\n### 📝 [chen2023twofailures] — cite key 与 year field 不一致\n- **Cite key**: chen**2023**twofailures\n- **Year field**: 2024\n- **实际**: arXiv 2023.05, TMLR 2024. Year field 2024 正确（TMLR 出版年），但 key 中 2023 可能误导\n\n---\n\n## 未使用的 bib entries\n\n| Cite key | 标题 | 说明 |\n|----------|------|------|\n| `holm1979simple` | A Simple Sequentially Rejective Multiple Test Procedure | 方法被引用但未 \\cite（见上方⚠️） |\n| `li2024simple` | A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction | 完全未引用 |\n| `xiao2022uncertainty` | Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis | 完全未引用 |\n\n---\n\n## 逐条验证\n\n### 1. [landesberg2026bon] Landesberg (2026). \"When LLM Judge Scores Look Good but Best-of-N Decisions Fail\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：N/A\n- DOI/arXiv：✓ (2603.12520)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 concurrent work documenting correlation-selection gap in BoN reasoning\n- **结论：✅ OK**\n\n### 2. [holm1979simple] Holm (1979). \"A Simple Sequentially Rejective Multiple Test Procedure\". Scand. J. Stats.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓ Sture Holm\n- 年份：✓ 1979\n- 标题：✓\n- Venue：✓ Scandinavian Journal of Statistics, 6(2), 65-70\n- 卷期页码：✓\n- DOI/arXiv：✓ (10.1037/h0031619 — wait, that's Fleiss. Holm doesn't have DOI in bib)\n- 论文存在：✓\n- 引用上下文：⚠️ 方法被多次引用但从未 \\cite\n- **结论：⚠️ 需修正 — 添加 \\cite**\n\n### 3. [brown2024monkeys] Brown et al. (2024). \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2407.21787)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 best-of-N scaling / test-time compute\n- **结论：✅ OK**\n\n### 4. [chen2024usc] Chen et al. (2024). \"Universal Self-Consistency for Large Language Model Generation\". ICML 2024 Workshop.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2023 arXiv; 2024 workshop correct)\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2311.17311)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 free-form SC variant\n- **结论：✅ OK**\n\n### 5. [cobbe2021verifiers] Cobbe et al. (2021). \"Training Verifiers to Solve Math Word Problems\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2110.14168)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 trained verifiers\n- **结论：✅ OK**\n\n### 6. [derczynski2017wnut] Derczynski et al. (2017). \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\". W-NUT 2017.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 WNUT-17 dataset\n- **结论：✅ OK**\n\n### 7. [ding2021fewnerd] Ding et al. (2021). \"Few-NERD: A Few-shot Named Entity Recognition Dataset\". ACL 2021.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2021.acl-long.248)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 Few-NERD dataset\n- **结论：✅ OK**\n\n### 8. [eikema2022sampling] Eikema & Aziz (2022). \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\". EMNLP 2022.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2021 arXiv; 2022 EMNLP correct)\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2022.emnlp-main.754)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR decoding\n- **结论：✅ OK**\n\n### 9. [freitag2022high] Freitag et al. (2022). \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\". TACL.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (TACL vol 10 = 2022)\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (10, 811-825)\n- DOI：✓ (10.1162/tacl_a_00491)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR success in MT\n- **结论：✅ OK**\n\n### 10. [fleiss1971agreement] Fleiss (1971). \"Measuring nominal scale agreement among many raters.\" Psychological Bulletin.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.1037/h0031619)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 Fleiss' kappa 统计方法\n- **结论：✅ OK**\n\n### 11. [geng2024confidence] Geng et al. (2024). \"A Survey of Confidence Estimation and Calibration in Large Language Models\". NAACL 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2024.naacl-long.366)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 confidence estimation survey\n- **结论：✅ OK**\n\n### 12. [kadavath2022language] Kadavath et al. (2022). \"Language Models (Mostly) Know What They Know\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2207.05221)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 LP well-calibrated at population level\n- **结论：✅ OK**\n\n### 13. [kang2025selfcertainty] Kang et al. (2025). \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\". NeurIPS 2025.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2502.18581)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 reward-free selector\n- **结论：✅ OK**\n\n### 14. [kuhn2023semantic] Kuhn et al. (2023). \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\". ICLR 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2302.09664)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 semantic uncertainty\n- **结论：✅ OK**\n\n### 15. [lightman2024verify] Lightman et al. (2024). \"Let's Verify Step by Step\". ICLR 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2305.20050)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 trained verifiers (step-by-step)\n- **结论：✅ OK**\n\n### 16. [luan2018scierc] Luan et al. (2018). \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\". EMNLP 2018.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/D18-1360)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 SciERC dataset\n- **结论：✅ OK**\n\n### 17. [yao2026consistency] Yao et al. (2026). \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\". Genomics & Informatics.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.1186/s44342-025-00063-2)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 task-level consistency-accuracy correlation for NER/RE\n- **结论：✅ OK**\n\n### 18. [sainz2024gollie] Sainz et al. (2024). \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\". ICLR 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2023; ICLR 2024 correct)\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2310.03668)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 generative IE\n- **结论：✅ OK**\n\n### 19. [snell2025scaling] Snell et al. (2025). \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\". ICLR 2025.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**部分**\n- 作者：✓\n- 年份：✓\n- 标题：📝 arXiv 标题不同 (\"Scaling Model Parameters\")，但 bib 使用 ICLR proceedings 标题，可接受\n- Venue：✓\n- DOI/arXiv：✓ (2408.03314)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 test-time compute scaling\n- **结论：✅ OK（注意 arXiv/proceedings 标题差异）**\n\n### 20. [taubenfeld2025cisc] Taubenfeld et al. (2025). \"Confidence Improves Self-Consistency in LLMs\". Findings ACL 2025.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2025.findings-acl.1030)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 reward-free selector / confidence-weighted SC\n- **结论：✅ OK**\n\n### 21. [thirukovalluru2024atomic] Thirukovalluru et al. (2024). \"Atomic Self-Consistency for Better Long Form Generations\". EMNLP 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2024.emnlp-main.706)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 atomic SC variant\n- **结论：✅ OK**\n\n### 22. [tjongkimsang2003conll] Sang & De Meulder (2003). \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\". CoNLL 2003.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 CoNLL-2003 dataset\n- **结论：✅ OK**\n\n### 23. [wang2023selfconsistency] Wang et al. (2023). \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\". ICLR 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2203.11171)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 original self-consistency method\n- **结论：✅ OK**\n\n### 24. [willard2023guided] Willard & Louf (2023). \"Efficient Guided Generation for Large Language Models\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ (arXiv preprint)\n- DOI/arXiv：✓ (2307.09702)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 constrained decoding (Outlines)\n- **结论：✅ OK**\n\n### 25. [xia2025survey] Xia et al. (2025). \"A Survey of Uncertainty Estimation Methods on Large Language Models\". Findings ACL 2025.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 uncertainty estimation survey\n- **结论：✅ OK**\n\n### 26. [zheng2024llamafactory] Zheng et al. (2024). \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\". ACL 2024 Demos.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (400-410)\n- DOI：✓ (10.18653/v1/2024.acl-demos.38)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 fine-tuning framework\n- **结论：✅ OK**\n\n### 27. [zhou2024uniner] Zhou et al. (2024). \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\". ICLR 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2308.03279)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 generative IE\n- **结论：✅ OK**\n\n### 28. [muller2021understanding] Müller & Sennrich (2021). \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\". ACL 2021.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2021.acl-long.22)\n- 卷期页码：✓ (259-272)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR decoding\n- **结论：✅ OK**\n\n### 29. [eikema2025structured] Eikema et al. (2025). \"Structure-Conditional Minimum Bayes Risk Decoding\". EMNLP 2025.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2510.20700)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR utilities degrade on structured outputs\n- **结论：✅ OK**\n\n### 30. [jinnai2024mbr] Jinnai et al. (2024). \"Model-Based Minimum Bayes Risk Decoding for Text Generation\". ICML 2024.\n- 在线验证：PMLR **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2311.05263)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 model-based MBR\n- **结论：✅ OK**\n\n### 31. [ratinov2009design] Ratinov & Roth (2009). \"Design Challenges and Misconceptions in Named Entity Recognition\". CoNLL 2009.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (147-155)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 NER evaluation methodology (0.5pp threshold)\n- **结论：✅ OK**\n\n### 32. [bergkirkpatrick2012empirical] Berg-Kirkpatrick et al. (2012). \"An Empirical Investigation of Statistical Significance in NLP\". EMNLP-CoNLL 2012.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (995-1005)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 statistical significance threshold (1.0pp)\n- **结论：✅ OK**\n\n### 33. [tian2023calibration] Tian et al. (2023). \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\". EMNLP 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (5433-5442)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 LP calibration / verbalized confidence\n- **结论：✅ OK**\n\n### 34. [yun2025price] Yun et al. (2025). \"The Price of Format: Diversity Collapse in LLMs\". Findings EMNLP 2025.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 diversity collapse under constrained decoding\n- **结论：✅ OK**\n\n### 35. [gao2023scaling] Gao et al. (2023). \"Scaling Laws for Reward Model Overoptimization\". ICML 2023.\n- 在线验证：PMLR **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 BoN scaling laws\n- **结论：✅ OK**\n\n### 36. [platt1999probabilistic] Platt (1999). \"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\". MIT Press.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ (Advances in Large Margin Classifiers, MIT Press)\n- 卷期页码：✓ (61-74)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 Platt scaling (calibration)\n- **结论：✅ OK**\n\n### 37. [guo2017calibration] Guo et al. (2017). \"On Calibration of Modern Neural Networks\". ICML 2017.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (1321-1330)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 temperature scaling (calibration)\n- **结论：✅ OK**\n\n### 38. [geifman2017selective] Geifman & El-Yaniv (2017). \"Selective Classification for Deep Neural Networks\". NeurIPS 2017.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (1705.08500)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 selective prediction\n- **结论：✅ OK**\n\n### 39. [dong2024xgrammar] Dong et al. (2024). \"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2411.15100)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 constrained decoding engine\n- **结论：✅ OK**\n\n### 40. [lin2022teaching] Lin et al. (2022). \"Teaching Models to Express Their Uncertainty in Words\". TMLR.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ (Transactions on Machine Learning Research)\n- DOI/arXiv：✓ (2205.14334)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 verbalized confidence\n- **结论：✅ OK**\n\n### 41. [farquhar2024detecting] Farquhar et al. (2024). \"Detecting hallucinations in large language models using semantic entropy\". Nature.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ Nature\n- 卷期页码：✓ (630, 625-630)\n- DOI：✓ (10.1038/s41586-024-07421-0)\n- 论文存在：✓\n- 引用上下文：✓ — 引用在 differentiation table (hallucination detection via semantic entropy)\n- **结论：✅ OK**\n\n### 42. [chen2023twofailures] Chen et al. (2024). \"Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs\". TMLR.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (year field = 2024, matching TMLR publication)\n- 标题：✓\n- Venue：✓ (TMLR)\n- DOI/arXiv：✓ (2305.14279)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 SC failure cases\n- **结论：✅ OK（cite key 中 2023 与 year 2024 不一致，但不影响论文编译）**\n\n### 43. [aggarwal2023adaptive] Aggarwal et al. (2023). \"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs\". EMNLP 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2305.11860)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 adaptive consistency / sample allocation\n- **结论：✅ OK**\n\n### 44. [xie2023zeroshot] Xie et al. (2023). \"Empirical Study of Zero-Shot NER with ChatGPT\". EMNLP 2023.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (7935-7956)\n- DOI：✓ (10.18653/v1/2023.emnlp-main.493)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 entity voting for zero-shot NER\n- **结论：✅ OK**\n\n### 45. [muennighoff2025s1] Muennighoff et al. (2025). \"s1: Simple Test-Time Scaling\". EMNLP 2025.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2501.19393)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 extended reasoning / test-time scaling\n- **结论：✅ OK**\n\n### 46. [eikema2020map] Eikema & Aziz (2020). \"Is MAP Decoding All You Need? The Inadequacy of the Mode in Neural Machine Translation\". COLING 2020.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (4506-4520)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR / MAP decoding inadequacy\n- **结论：✅ OK**\n\n### 47. [kumar2004minimum] Kumar & Byrne (2004). \"Minimum Bayes-Risk Decoding for Statistical Machine Translation\". HLT-NAACL 2004.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (169-176)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR decoding foundational work\n- **结论：✅ OK**\n\n### 48. [dembczynski2011exact] Dembczyński et al. (2011). \"An Exact Algorithm for F-Measure Maximization\". NeurIPS 2011.\n- 在线验证：NeurIPS proceedings **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (24, 1404-1412)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 F-measure threshold complexity\n- **结论：✅ OK**\n\n### 49. [desai2020calibration] Desai & Durrett (2020). \"Calibration of Pre-trained Transformers\". EMNLP 2020.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (295-302)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 calibrated LMs\n- **结论：✅ OK**\n\n### 50. [huang2024large] Huang et al. (2024). \"Large Language Models Cannot Self-Correct Reasoning Yet\". ICLR 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2023 arXiv; ICLR 2024 correct)\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 introspection boundary / self-correction limitation\n- **结论：✅ OK**\n\n### 51. [li2024simple] Li et al. (2024). \"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction\". Findings EMNLP 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2402.13364)\n- 论文存在：✓\n- 引用上下文：N/A — **未在 tex 中引用**\n- **结论：✅ 论文真实，但未被引用（建议删除或添加引用）**\n\n### 52. [xie2024selfimproving] Xie et al. (2024). \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\". NAACL 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 SC-based self-annotation for NER\n- **结论：✅ OK**\n\n### 53. [madaan2023selfrefine] Madaan et al. (2023). \"Self-Refine: Iterative Refinement with Self-Feedback\". NeurIPS 2023.\n- 在线验证：NeurIPS proceedings **找到** | 匹配度：**完全**\n- 作者：✓ (16 authors confirmed via NeurIPS proceedings, including Katherine Hermann)\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 iterative self-refinement\n- **结论：✅ OK**\n\n### 54. [angelopoulos2023conformal] Angelopoulos & Bates (2023). \"Conformal Prediction: A Gentle Introduction\". Foundations and Trends in ML.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (16(4), 494-591)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 conformal prediction\n- **结论：✅ OK**\n\n### 55. [malinin2021uncertainty] Malinin & Gales (2021). \"Uncertainty Estimation in Autoregressive Structured Prediction\". ICLR 2021.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 uncertainty in structured prediction\n- **结论：✅ OK**\n\n### 56. [yee2019noisy] Yee et al. (2019). \"Simple and Effective Noisy Channel Modeling for Neural Machine Translation\". EMNLP-IJCNLP 2019.\n- 在线验证：ACL Anthology + arXiv **找到** | 匹配度：**部分**\n- 作者：⚠️ ACL Anthology (D19-1571) 列 3 人，arXiv 列 4 人（+Nathan Ng）。Bib 匹配 proceedings 版 3 人，但 URL 指向 arXiv 4 人版\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (1908.05731)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 noisy channel models\n- **结论：⚠️ 需修正 — 作者列表与 arXiv URL 不一致（见上方详述）**\n\n### 57. [li2023stepaware] Li et al. (2023). \"Making Large Language Models Better Reasoners with Step-Aware Verifier\". ACL 2023.\n- 在线验证：ACL Anthology **找到** | 匹配度：**部分**\n- 作者：✓\n- 年份：✓\n- 标题：⚠️ ACL Anthology: \"Making Language Models Better Reasoners...\" (无 \"Large\")；arXiv: \"Making **Large** Language Models Better Reasoners...\"。Bib 使用 arXiv 标题但引用 ACL proceedings\n- Venue：✓\n- DOI/arXiv：✓ (2206.02336)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 step-aware verifier / trained verifiers\n- **结论：⚠️ 需修正 — 标题应删除 \"Large\" 以匹配 ACL proceedings**\n\n### 58. [xiao2022uncertainty] Xiao et al. (2022). \"Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis\". Findings EMNLP 2022.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：N/A — **未在 tex 中引用**\n- **结论：✅ 论文真实，但未被引用（建议删除或添加引用）**\n\n### 59. [li2026rewardtail] Li et al. (2026). \"Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2602.01485)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 reward-tail-guided search\n- **结论：✅ OK**\n\n### 60. [shinn2023reflexion] Shinn et al. (2023). \"Reflexion: Language Agents with Verbal Reinforcement Learning\". NeurIPS 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓ (5 authors, matching NeurIPS proceedings; S2 erroneously adds \"Beck Labash\" as 6th)\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 iterative self-verification\n- **结论：✅ OK**\n\n### 61. [xu2024llmie] Xu et al. (2024). \"Large Language Models for Generative Information Extraction: A Survey\". Frontiers of Computer Science.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**部分**\n- 作者：📝 Bib 列 10 人含 \"Wang, Yang\"；S2 列 9 人无 \"Wang, Yang\"。需对照出版商确认\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (18(6), 186357)\n- DOI：✓ (10.1007/s11704-024-40555-y)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 LLM-based IE survey\n- **结论：✅ OK（作者 \"Wang, Yang\" 待出版商确认）**\n\n### 62. [wang2025gptner] Wang et al. (2025). \"GPT-NER: Named Entity Recognition via Large Language Models\". Findings NAACL 2025.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2023 arXiv; NAACL 2025 correct)\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 self-verification in NER\n- **结论：✅ OK**\n\n### 63. [gero2023selfverification] Gero et al. (2023). \"Self-Verification Improves Few-Shot Clinical Information Extraction\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ (arXiv preprint)\n- DOI/arXiv：✓ (2306.00024)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 self-verification in clinical IE\n- **结论：✅ OK**\n\n### 64. [wadhwa2023revisiting] Wadhwa et al. (2023). \"Revisiting Relation Extraction in the era of Large Language Models\". ACL 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (15566-15589)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 LLM-based RE benchmark\n- **结论：✅ OK**\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ad4ad56d-41fb-42ee-b372-4b9b467aab9d",
  "uuid": "b32f586e-1d01-4762-82b3-c3019daeec67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019x5A7oT32qikAcnV7vF6XG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 109560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 294
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-26T11:12:48.083Z_

<details><summary>↩ Tool result · `toolu_01K6SVMZME98KzHJFny453EM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ref_audit_worker_A.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ad4ad56d-41fb-42ee-b372-4b9b467aab9d",
  "uuid": "c7937552-7746-4ff2-8df6-efc020cc9960",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ref_audit_worker_A.md",
    "content": "# 引用验证清单 (Worker A — Semantic Scholar 优先)\n\n**验证日期**: 2026-05-26\n**验证手段**: Semantic Scholar API + WebSearch fallback (ACL Anthology, arXiv, OpenReview, PMLR, NeurIPS proceedings)\n\n总 bib entries: **64**\n总 unique cite keys in tex: **61**\n未使用的 bib entries: `holm1979simple`, `li2024simple`, `xiao2022uncertainty`\ntex 中引用但 bib 缺失: **无**\n\n---\n\n## 总结\n\n| 类别 | 数量 |\n|------|------|\n| 论文真实存在 | 64/64 (100%) |\n| 完全匹配 (无任何问题) | 58 |\n| 需修正 (⚠️) | 3 |\n| 需关注 (注意事项) | 3 |\n| 严重问题 (❌ 虚假引用) | 0 |\n\n---\n\n## 需修正的条目\n\n### ⚠️ [li2023stepaware] — 标题多了 \"Large\"\n- **Bib 标题**: \"Making **Large** Language Models Better Reasoners with Step-Aware Verifier\"\n- **ACL 2023 proceedings 标题**: \"Making Language Models Better Reasoners with Step-Aware Verifier\"\n- **来源**: ACL Anthology 2023.acl-long.291 确认无 \"Large\"；arXiv:2206.02336 版本有 \"Large\"\n- **建议**: 既然 bib 引用的是 ACL 2023 proceedings，应使用 proceedings 标题，删除 \"Large\"\n\n### ⚠️ [yee2019noisy] — arXiv 与 proceedings 作者列表不一致\n- **Bib 作者**: Yee, Dauphin, Auli (3人)\n- **ACL Anthology D19-1571**: Yee, Dauphin, Auli (3人) ← bib 匹配 proceedings\n- **arXiv:1908.05731**: Yee, **Ng**, Dauphin, Auli (4人)\n- **问题**: Bib 的 URL 指向 arXiv (4人版本)，但作者列表只有 3 人（匹配 proceedings）。建议统一：要么加上 Nathan Ng（匹配 arXiv），要么将 URL 改为 ACL Anthology 链接\n\n### ⚠️ [holm1979simple] — 方法被引用但未 \\cite\n- **现状**: 论文正文多次提及 \"Holm--Bonferroni\" 方法（至少 15 次），但从未使用 `\\cite{holm1979simple}`\n- **建议**: 在首次提及 Holm--Bonferroni 时添加 `\\cite{holm1979simple}`\n\n---\n\n## 需关注的条目\n\n### 📝 [snell2025scaling] — arXiv 与 ICLR proceedings 标题不同\n- **Bib 标题**: \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\"\n- **arXiv 标题**: \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\"\n- **ICLR 2025 proceedings 标题**: \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\"\n- **结论**: Bib 使用了 ICLR proceedings 标题，技术上正确。但注意 arXiv 版本标题不同。\n\n### 📝 [xu2024llmie] — 作者 \"Wang, Yang\" 在 S2 中未出现\n- **Bib 作者**: 10人（含 Wang, Yang）\n- **Semantic Scholar**: 9人（无 Wang, Yang）\n- **结论**: 需对照 Springer 出版商页面确认。S2 数据可能不完整。\n\n### 📝 [chen2023twofailures] — cite key 与 year field 不一致\n- **Cite key**: chen**2023**twofailures\n- **Year field**: 2024\n- **实际**: arXiv 2023.05, TMLR 2024. Year field 2024 正确（TMLR 出版年），但 key 中 2023 可能误导\n\n---\n\n## 未使用的 bib entries\n\n| Cite key | 标题 | 说明 |\n|----------|------|------|\n| `holm1979simple` | A Simple Sequentially Rejective Multiple Test Procedure | 方法被引用但未 \\cite（见上方⚠️） |\n| `li2024simple` | A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction | 完全未引用 |\n| `xiao2022uncertainty` | Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis | 完全未引用 |\n\n---\n\n## 逐条验证\n\n### 1. [landesberg2026bon] Landesberg (2026). \"When LLM Judge Scores Look Good but Best-of-N Decisions Fail\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：N/A\n- DOI/arXiv：✓ (2603.12520)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 concurrent work documenting correlation-selection gap in BoN reasoning\n- **结论：✅ OK**\n\n### 2. [holm1979simple] Holm (1979). \"A Simple Sequentially Rejective Multiple Test Procedure\". Scand. J. Stats.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓ Sture Holm\n- 年份：✓ 1979\n- 标题：✓\n- Venue：✓ Scandinavian Journal of Statistics, 6(2), 65-70\n- 卷期页码：✓\n- DOI/arXiv：✓ (10.1037/h0031619 — wait, that's Fleiss. Holm doesn't have DOI in bib)\n- 论文存在：✓\n- 引用上下文：⚠️ 方法被多次引用但从未 \\cite\n- **结论：⚠️ 需修正 — 添加 \\cite**\n\n### 3. [brown2024monkeys] Brown et al. (2024). \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2407.21787)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 best-of-N scaling / test-time compute\n- **结论：✅ OK**\n\n### 4. [chen2024usc] Chen et al. (2024). \"Universal Self-Consistency for Large Language Model Generation\". ICML 2024 Workshop.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2023 arXiv; 2024 workshop correct)\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2311.17311)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 free-form SC variant\n- **结论：✅ OK**\n\n### 5. [cobbe2021verifiers] Cobbe et al. (2021). \"Training Verifiers to Solve Math Word Problems\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2110.14168)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 trained verifiers\n- **结论：✅ OK**\n\n### 6. [derczynski2017wnut] Derczynski et al. (2017). \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\". W-NUT 2017.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 WNUT-17 dataset\n- **结论：✅ OK**\n\n### 7. [ding2021fewnerd] Ding et al. (2021). \"Few-NERD: A Few-shot Named Entity Recognition Dataset\". ACL 2021.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2021.acl-long.248)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 Few-NERD dataset\n- **结论：✅ OK**\n\n### 8. [eikema2022sampling] Eikema & Aziz (2022). \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\". EMNLP 2022.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2021 arXiv; 2022 EMNLP correct)\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2022.emnlp-main.754)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR decoding\n- **结论：✅ OK**\n\n### 9. [freitag2022high] Freitag et al. (2022). \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\". TACL.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (TACL vol 10 = 2022)\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (10, 811-825)\n- DOI：✓ (10.1162/tacl_a_00491)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR success in MT\n- **结论：✅ OK**\n\n### 10. [fleiss1971agreement] Fleiss (1971). \"Measuring nominal scale agreement among many raters.\" Psychological Bulletin.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.1037/h0031619)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 Fleiss' kappa 统计方法\n- **结论：✅ OK**\n\n### 11. [geng2024confidence] Geng et al. (2024). \"A Survey of Confidence Estimation and Calibration in Large Language Models\". NAACL 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2024.naacl-long.366)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 confidence estimation survey\n- **结论：✅ OK**\n\n### 12. [kadavath2022language] Kadavath et al. (2022). \"Language Models (Mostly) Know What They Know\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2207.05221)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 LP well-calibrated at population level\n- **结论：✅ OK**\n\n### 13. [kang2025selfcertainty] Kang et al. (2025). \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\". NeurIPS 2025.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2502.18581)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 reward-free selector\n- **结论：✅ OK**\n\n### 14. [kuhn2023semantic] Kuhn et al. (2023). \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\". ICLR 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2302.09664)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 semantic uncertainty\n- **结论：✅ OK**\n\n### 15. [lightman2024verify] Lightman et al. (2024). \"Let's Verify Step by Step\". ICLR 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2305.20050)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 trained verifiers (step-by-step)\n- **结论：✅ OK**\n\n### 16. [luan2018scierc] Luan et al. (2018). \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\". EMNLP 2018.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/D18-1360)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 SciERC dataset\n- **结论：✅ OK**\n\n### 17. [yao2026consistency] Yao et al. (2026). \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\". Genomics & Informatics.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.1186/s44342-025-00063-2)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 task-level consistency-accuracy correlation for NER/RE\n- **结论：✅ OK**\n\n### 18. [sainz2024gollie] Sainz et al. (2024). \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\". ICLR 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2023; ICLR 2024 correct)\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2310.03668)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 generative IE\n- **结论：✅ OK**\n\n### 19. [snell2025scaling] Snell et al. (2025). \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\". ICLR 2025.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**部分**\n- 作者：✓\n- 年份：✓\n- 标题：📝 arXiv 标题不同 (\"Scaling Model Parameters\")，但 bib 使用 ICLR proceedings 标题，可接受\n- Venue：✓\n- DOI/arXiv：✓ (2408.03314)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 test-time compute scaling\n- **结论：✅ OK（注意 arXiv/proceedings 标题差异）**\n\n### 20. [taubenfeld2025cisc] Taubenfeld et al. (2025). \"Confidence Improves Self-Consistency in LLMs\". Findings ACL 2025.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2025.findings-acl.1030)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 reward-free selector / confidence-weighted SC\n- **结论：✅ OK**\n\n### 21. [thirukovalluru2024atomic] Thirukovalluru et al. (2024). \"Atomic Self-Consistency for Better Long Form Generations\". EMNLP 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2024.emnlp-main.706)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 atomic SC variant\n- **结论：✅ OK**\n\n### 22. [tjongkimsang2003conll] Sang & De Meulder (2003). \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\". CoNLL 2003.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 CoNLL-2003 dataset\n- **结论：✅ OK**\n\n### 23. [wang2023selfconsistency] Wang et al. (2023). \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\". ICLR 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2203.11171)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 original self-consistency method\n- **结论：✅ OK**\n\n### 24. [willard2023guided] Willard & Louf (2023). \"Efficient Guided Generation for Large Language Models\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ (arXiv preprint)\n- DOI/arXiv：✓ (2307.09702)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 constrained decoding (Outlines)\n- **结论：✅ OK**\n\n### 25. [xia2025survey] Xia et al. (2025). \"A Survey of Uncertainty Estimation Methods on Large Language Models\". Findings ACL 2025.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 uncertainty estimation survey\n- **结论：✅ OK**\n\n### 26. [zheng2024llamafactory] Zheng et al. (2024). \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\". ACL 2024 Demos.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (400-410)\n- DOI：✓ (10.18653/v1/2024.acl-demos.38)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 fine-tuning framework\n- **结论：✅ OK**\n\n### 27. [zhou2024uniner] Zhou et al. (2024). \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\". ICLR 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2308.03279)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 generative IE\n- **结论：✅ OK**\n\n### 28. [muller2021understanding] Müller & Sennrich (2021). \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\". ACL 2021.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI：✓ (10.18653/v1/2021.acl-long.22)\n- 卷期页码：✓ (259-272)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR decoding\n- **结论：✅ OK**\n\n### 29. [eikema2025structured] Eikema et al. (2025). \"Structure-Conditional Minimum Bayes Risk Decoding\". EMNLP 2025.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2510.20700)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR utilities degrade on structured outputs\n- **结论：✅ OK**\n\n### 30. [jinnai2024mbr] Jinnai et al. (2024). \"Model-Based Minimum Bayes Risk Decoding for Text Generation\". ICML 2024.\n- 在线验证：PMLR **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2311.05263)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 model-based MBR\n- **结论：✅ OK**\n\n### 31. [ratinov2009design] Ratinov & Roth (2009). \"Design Challenges and Misconceptions in Named Entity Recognition\". CoNLL 2009.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (147-155)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 NER evaluation methodology (0.5pp threshold)\n- **结论：✅ OK**\n\n### 32. [bergkirkpatrick2012empirical] Berg-Kirkpatrick et al. (2012). \"An Empirical Investigation of Statistical Significance in NLP\". EMNLP-CoNLL 2012.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (995-1005)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 statistical significance threshold (1.0pp)\n- **结论：✅ OK**\n\n### 33. [tian2023calibration] Tian et al. (2023). \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\". EMNLP 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (5433-5442)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 LP calibration / verbalized confidence\n- **结论：✅ OK**\n\n### 34. [yun2025price] Yun et al. (2025). \"The Price of Format: Diversity Collapse in LLMs\". Findings EMNLP 2025.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 diversity collapse under constrained decoding\n- **结论：✅ OK**\n\n### 35. [gao2023scaling] Gao et al. (2023). \"Scaling Laws for Reward Model Overoptimization\". ICML 2023.\n- 在线验证：PMLR **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 BoN scaling laws\n- **结论：✅ OK**\n\n### 36. [platt1999probabilistic] Platt (1999). \"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\". MIT Press.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ (Advances in Large Margin Classifiers, MIT Press)\n- 卷期页码：✓ (61-74)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 Platt scaling (calibration)\n- **结论：✅ OK**\n\n### 37. [guo2017calibration] Guo et al. (2017). \"On Calibration of Modern Neural Networks\". ICML 2017.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (1321-1330)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 temperature scaling (calibration)\n- **结论：✅ OK**\n\n### 38. [geifman2017selective] Geifman & El-Yaniv (2017). \"Selective Classification for Deep Neural Networks\". NeurIPS 2017.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (1705.08500)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 selective prediction\n- **结论：✅ OK**\n\n### 39. [dong2024xgrammar] Dong et al. (2024). \"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2411.15100)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 constrained decoding engine\n- **结论：✅ OK**\n\n### 40. [lin2022teaching] Lin et al. (2022). \"Teaching Models to Express Their Uncertainty in Words\". TMLR.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ (Transactions on Machine Learning Research)\n- DOI/arXiv：✓ (2205.14334)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 verbalized confidence\n- **结论：✅ OK**\n\n### 41. [farquhar2024detecting] Farquhar et al. (2024). \"Detecting hallucinations in large language models using semantic entropy\". Nature.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ Nature\n- 卷期页码：✓ (630, 625-630)\n- DOI：✓ (10.1038/s41586-024-07421-0)\n- 论文存在：✓\n- 引用上下文：✓ — 引用在 differentiation table (hallucination detection via semantic entropy)\n- **结论：✅ OK**\n\n### 42. [chen2023twofailures] Chen et al. (2024). \"Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs\". TMLR.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (year field = 2024, matching TMLR publication)\n- 标题：✓\n- Venue：✓ (TMLR)\n- DOI/arXiv：✓ (2305.14279)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 SC failure cases\n- **结论：✅ OK（cite key 中 2023 与 year 2024 不一致，但不影响论文编译）**\n\n### 43. [aggarwal2023adaptive] Aggarwal et al. (2023). \"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs\". EMNLP 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2305.11860)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 adaptive consistency / sample allocation\n- **结论：✅ OK**\n\n### 44. [xie2023zeroshot] Xie et al. (2023). \"Empirical Study of Zero-Shot NER with ChatGPT\". EMNLP 2023.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (7935-7956)\n- DOI：✓ (10.18653/v1/2023.emnlp-main.493)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 entity voting for zero-shot NER\n- **结论：✅ OK**\n\n### 45. [muennighoff2025s1] Muennighoff et al. (2025). \"s1: Simple Test-Time Scaling\". EMNLP 2025.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2501.19393)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 extended reasoning / test-time scaling\n- **结论：✅ OK**\n\n### 46. [eikema2020map] Eikema & Aziz (2020). \"Is MAP Decoding All You Need? The Inadequacy of the Mode in Neural Machine Translation\". COLING 2020.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (4506-4520)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR / MAP decoding inadequacy\n- **结论：✅ OK**\n\n### 47. [kumar2004minimum] Kumar & Byrne (2004). \"Minimum Bayes-Risk Decoding for Statistical Machine Translation\". HLT-NAACL 2004.\n- 在线验证：ACL Anthology **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (169-176)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 MBR decoding foundational work\n- **结论：✅ OK**\n\n### 48. [dembczynski2011exact] Dembczyński et al. (2011). \"An Exact Algorithm for F-Measure Maximization\". NeurIPS 2011.\n- 在线验证：NeurIPS proceedings **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (24, 1404-1412)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 F-measure threshold complexity\n- **结论：✅ OK**\n\n### 49. [desai2020calibration] Desai & Durrett (2020). \"Calibration of Pre-trained Transformers\". EMNLP 2020.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (295-302)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 calibrated LMs\n- **结论：✅ OK**\n\n### 50. [huang2024large] Huang et al. (2024). \"Large Language Models Cannot Self-Correct Reasoning Yet\". ICLR 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2023 arXiv; ICLR 2024 correct)\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 introspection boundary / self-correction limitation\n- **结论：✅ OK**\n\n### 51. [li2024simple] Li et al. (2024). \"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction\". Findings EMNLP 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2402.13364)\n- 论文存在：✓\n- 引用上下文：N/A — **未在 tex 中引用**\n- **结论：✅ 论文真实，但未被引用（建议删除或添加引用）**\n\n### 52. [xie2024selfimproving] Xie et al. (2024). \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\". NAACL 2024.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 SC-based self-annotation for NER\n- **结论：✅ OK**\n\n### 53. [madaan2023selfrefine] Madaan et al. (2023). \"Self-Refine: Iterative Refinement with Self-Feedback\". NeurIPS 2023.\n- 在线验证：NeurIPS proceedings **找到** | 匹配度：**完全**\n- 作者：✓ (16 authors confirmed via NeurIPS proceedings, including Katherine Hermann)\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 iterative self-refinement\n- **结论：✅ OK**\n\n### 54. [angelopoulos2023conformal] Angelopoulos & Bates (2023). \"Conformal Prediction: A Gentle Introduction\". Foundations and Trends in ML.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (16(4), 494-591)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 conformal prediction\n- **结论：✅ OK**\n\n### 55. [malinin2021uncertainty] Malinin & Gales (2021). \"Uncertainty Estimation in Autoregressive Structured Prediction\". ICLR 2021.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 uncertainty in structured prediction\n- **结论：✅ OK**\n\n### 56. [yee2019noisy] Yee et al. (2019). \"Simple and Effective Noisy Channel Modeling for Neural Machine Translation\". EMNLP-IJCNLP 2019.\n- 在线验证：ACL Anthology + arXiv **找到** | 匹配度：**部分**\n- 作者：⚠️ ACL Anthology (D19-1571) 列 3 人，arXiv 列 4 人（+Nathan Ng）。Bib 匹配 proceedings 版 3 人，但 URL 指向 arXiv 4 人版\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (1908.05731)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 noisy channel models\n- **结论：⚠️ 需修正 — 作者列表与 arXiv URL 不一致（见上方详述）**\n\n### 57. [li2023stepaware] Li et al. (2023). \"Making Large Language Models Better Reasoners with Step-Aware Verifier\". ACL 2023.\n- 在线验证：ACL Anthology **找到** | 匹配度：**部分**\n- 作者：✓\n- 年份：✓\n- 标题：⚠️ ACL Anthology: \"Making Language Models Better Reasoners...\" (无 \"Large\")；arXiv: \"Making **Large** Language Models Better Reasoners...\"。Bib 使用 arXiv 标题但引用 ACL proceedings\n- Venue：✓\n- DOI/arXiv：✓ (2206.02336)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 step-aware verifier / trained verifiers\n- **结论：⚠️ 需修正 — 标题应删除 \"Large\" 以匹配 ACL proceedings**\n\n### 58. [xiao2022uncertainty] Xiao et al. (2022). \"Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis\". Findings EMNLP 2022.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：N/A — **未在 tex 中引用**\n- **结论：✅ 论文真实，但未被引用（建议删除或添加引用）**\n\n### 59. [li2026rewardtail] Li et al. (2026). \"Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- DOI/arXiv：✓ (2602.01485)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 reward-tail-guided search\n- **结论：✅ OK**\n\n### 60. [shinn2023reflexion] Shinn et al. (2023). \"Reflexion: Language Agents with Verbal Reinforcement Learning\". NeurIPS 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓ (5 authors, matching NeurIPS proceedings; S2 erroneously adds \"Beck Labash\" as 6th)\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 iterative self-verification\n- **结论：✅ OK**\n\n### 61. [xu2024llmie] Xu et al. (2024). \"Large Language Models for Generative Information Extraction: A Survey\". Frontiers of Computer Science.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**部分**\n- 作者：📝 Bib 列 10 人含 \"Wang, Yang\"；S2 列 9 人无 \"Wang, Yang\"。需对照出版商确认\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (18(6), 186357)\n- DOI：✓ (10.1007/s11704-024-40555-y)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 LLM-based IE survey\n- **结论：✅ OK（作者 \"Wang, Yang\" 待出版商确认）**\n\n### 62. [wang2025gptner] Wang et al. (2025). \"GPT-NER: Named Entity Recognition via Large Language Models\". Findings NAACL 2025.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓ (S2 shows 2023 arXiv; NAACL 2025 correct)\n- 标题：✓\n- Venue：✓\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 self-verification in NER\n- **结论：✅ OK**\n\n### 63. [gero2023selfverification] Gero et al. (2023). \"Self-Verification Improves Few-Shot Clinical Information Extraction\". arXiv.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓ (arXiv preprint)\n- DOI/arXiv：✓ (2306.00024)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 self-verification in clinical IE\n- **结论：✅ OK**\n\n### 64. [wadhwa2023revisiting] Wadhwa et al. (2023). \"Revisiting Relation Extraction in the era of Large Language Models\". ACL 2023.\n- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**\n- 作者：✓\n- 年份：✓\n- 标题：✓\n- Venue：✓\n- 卷期页码：✓ (15566-15589)\n- 论文存在：✓\n- 引用上下文：✓ — 引用为 LLM-based RE benchmark\n- **结论：✅ OK**\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 468_

报告已写入 `artifacts/ref_audit_worker_A.md`。

**核心结论**：64 条 bib entries 全部真实存在，无虚假引用。

**需修正（3 项）**：
1. **[li2023stepaware]** — 标题多了 "Large"，ACL 2023 proceedings 无此词
2. **[yee2019noisy]** — 作者列表（3人）与 bib 中 arXiv URL 指向的版本（4人，含 Nathan Ng）不一致
3. **[holm1979simple]** — Holm-Bonferroni 方法在正文中被引用 15+ 次但从未 `\cite`，bib entry 未被使用

**需关注（3 项）**：
- `snell2025scaling`: arXiv 与 ICLR proceedings 标题不同，bib 使用 proceedings 版，可接受
- `xu2024llmie`: 作者 "Wang, Yang" 在 S2 中缺失，需对照出版商确认
- `li2024simple`, `xiao2022uncertainty`: 在 bib 中但未被引用，建议删除或添加引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ad4ad56d-41fb-42ee-b372-4b9b467aab9d",
  "uuid": "a50099d0-c47f-463d-9400-9330d858a9c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJod2afTxtK6nWR4VBaz3u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14365,
      "cache_read_input_tokens": 109854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14365
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 469_

报告已写入 `artifacts/ref_audit_worker_A.md`。

**核心结论**：64 条 bib entries 全部真实存在，无虚假引用。

**需修正（3 项）**：
1. **[li2023stepaware]** — 标题多了 "Large"，ACL 2023 proceedings 无此词
2. **[yee2019noisy]** — 作者列表（3人）与 bib 中 arXiv URL 指向的版本（4人，含 Nathan Ng）不一致
3. **[holm1979simple]** — Holm-Bonferroni 方法在正文中被引用 15+ 次但从未 `\cite`，bib entry 未被使用

**需关注（3 项）**：
- `snell2025scaling`: arXiv 与 ICLR proceedings 标题不同，bib 使用 proceedings 版，可接受
- `xu2024llmie`: 作者 "Wang, Yang" 在 S2 中缺失，需对照出版商确认
- `li2024simple`, `xiao2022uncertainty`: 在 bib 中但未被引用，建议删除或添加引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 379110,
  "duration_api_ms": 1775105,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "ad4ad56d-41fb-42ee-b372-4b9b467aab9d",
  "total_cost_usd": 7.645014300000006,
  "usage": {
    "input_tokens": 135,
    "cache_creation_input_tokens": 30939,
    "cache_read_input_tokens": 835277,
    "output_tokens": 21823,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30939,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 332,
        "cache_read_input_tokens": 109854,
        "cache_creation_input_tokens": 14365,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 14365
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 461391,
      "outputTokens": 22780,
      "cacheReadInputTokens": 469093,
      "cacheCreationInputTokens": 90351,
      "webSearchRequests": 33,
      "costUSD": 1.0651390499999993,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3829,
      "outputTokens": 86058,
      "cacheReadInputTokens": 4343173,
      "cacheCreationInputTokens": 358031,
      "webSearchRequests": 0,
      "costUSD": 6.579875250000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "origin": {
    "kind": "task-notification"
  },
  "uuid": "f2b5f9e0-9d2f-4381-83ec-9ab198348e87"
}
```

</details>

---
