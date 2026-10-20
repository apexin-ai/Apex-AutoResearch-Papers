# audit ref check B — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-ref-check-b.md) · [Structured JSON](../../../sessions/2b/2be4181d4974f860afc8.json)

## Round 5

### Tool result

_source line 378 · 2026-05-26T10:25:44.894Z_

<details><summary>↩ Tool result · `toolu_01Vmy71FHqachuEU6xjrtdo9`</summary>

```text
Now I have all the information needed. Here is the structured verification report.

---

## Citation Verification Report

### 1. kuhn2023semantic
**Lorenz Kuhn, Yarin Gal, Sebastian Farquhar (2023). "Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation". ICLR 2023. arXiv:2302.09664.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Lorenz Kuhn, Yarin Gal, Sebastian Farquhar |
| Year correct | ✓ | 2023 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | ICLR 2023 |
| arXiv ID correct | ✓ | 2302.09664 |

**Verdict: ALL CORRECT**

---

### 2. lightman2024verify
**Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe (2024). "Let's Verify Step by Step". ICLR 2024. arXiv:2305.20050.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✗ | The arXiv PDF uses "Yura Burda" and "Harri Edwards", but DBLP/official proceedings list "Yuri Burda" and "Harrison Edwards". The bib entry matches the arXiv PDF, so this is acceptable but not fully canonical. |
| Year correct | ✓ | 2024 (ICLR 2024) |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | ICLR 2024 confirmed via OpenReview and proceedings |
| arXiv ID correct | ✓ | 2305.20050 |

**Verdict: MINOR ISSUE -- Author name forms "Yura Burda" / "Harri Edwards" are informal variants used on arXiv. The DBLP canonical forms are "Yuri Burda" / "Harrison Edwards". Either form is acceptable in practice.**

---

### 3. luan2018scierc
**Yi Luan, Luheng He, Mari Ostendorf, Hannaneh Hajishirzi (2018). "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction". EMNLP 2018. DOI: 10.18653/v1/D18-1360.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Yi Luan, Luheng He, Mari Ostendorf, Hannaneh Hajishirzi |
| Year correct | ✓ | 2018 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | EMNLP 2018, confirmed via ACL Anthology |
| DOI correct | ✓ | 10.18653/v1/D18-1360 |

**Verdict: ALL CORRECT**

---

### 4. yao2026consistency
**Xinzhi Yao, Claire Nédellec, Jingbo Xia, Robert Bossy (2026). "Consistency--accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data". Genomics & Informatics. DOI: 10.1186/s44342-025-00063-2.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Xinzhi Yao, Claire Nédellec, Jingbo Xia, Robert Bossy |
| Year correct | ✓ | Published 2026 (Genomics & Informatics, vol. 24, article 3, 2026) |
| Title correct | ✓ | Exact match (with en-dash in "Consistency--accuracy") |
| Venue correct | ✓ | Genomics & Informatics |
| DOI correct | ✓ | 10.1186/s44342-025-00063-2 |

**Verdict: ALL CORRECT** -- Note: the DOI has "2025" in the identifier string (s44342-**025**-00063-2) because DOIs are assigned at acceptance, but the publication year is 2026. This is normal for Springer journals.

---

### 5. sainz2024gollie
**Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre (2024). "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction". ICLR 2024. arXiv:2310.03668.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre |
| Year correct | ✓ | 2024 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | ICLR 2024 confirmed via OpenReview and proceedings |
| arXiv ID correct | ✓ | 2310.03668 |

**Verdict: ALL CORRECT**

---

### 6. snell2025scaling
**Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar (2025). "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning". ICLR 2025. arXiv:2408.03314.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar |
| Year correct | ✓ | ICLR 2025 |
| Title correct | ✗ | **Mismatch.** The bib entry says "...Scaling Parameters for Reasoning". The arXiv title is "Scaling LLM Test-Time Compute Optimally **can** be More Effective than Scaling **Model Parameters**" (no "for Reasoning", has "Model", lowercase "can"). The ICLR 2025 proceedings title is "Scaling LLM Test-Time Compute Optimally **Can** be More Effective than Scaling Parameters **for Reasoning**". So the bib title matches the ICLR proceedings title except for capitalization of "Can". |
| Venue correct | ✓ | ICLR 2025 (Oral) |
| arXiv ID correct | ✓ | 2408.03314 |

**Verdict: MINOR ISSUE -- The title in the bib entry matches the ICLR 2025 proceedings version, which differs slightly from the arXiv version (arXiv says "...Scaling Model Parameters" without "for Reasoning"; ICLR says "...Scaling Parameters for Reasoning"). If you cite the ICLR proceedings version, the bib title is correct. Just note that the arXiv title is different.**

---

### 7. taubenfeld2025cisc
**Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, Gal Yona (2025). "Confidence Improves Self-Consistency in LLMs". Findings of ACL 2025. DOI: 10.18653/v1/2025.findings-acl.1030.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, Gal Yona |
| Year correct | ✓ | 2025 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | Findings of ACL 2025, confirmed via ACL Anthology |
| DOI correct | ✓ | 10.18653/v1/2025.findings-acl.1030 |

**Verdict: ALL CORRECT**

---

### 8. thirukovalluru2024atomic
**Raghuveer Thirukovalluru, Yukun Huang, Bhuwan Dhingra (2024). "Atomic Self-Consistency for Better Long Form Generations". EMNLP 2024. DOI: 10.18653/v1/2024.emnlp-main.706.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Raghuveer Thirukovalluru, Yukun Huang, Bhuwan Dhingra |
| Year correct | ✓ | 2024 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | EMNLP 2024 (main), confirmed via ACL Anthology |
| DOI correct | ✓ | 10.18653/v1/2024.emnlp-main.706 |

**Verdict: ALL CORRECT**

---

### 9. tjongkimsang2003conll
**Erik F. Tjong Kim Sang, Fien De Meulder (2003). "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition". CoNLL 2003.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Erik F. Tjong Kim Sang, Fien De Meulder |
| Year correct | ✓ | 2003 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | CoNLL 2003 (Proceedings of the Seventh Conference on Natural Language Learning at HLT-NAACL 2003) |
| DOI/ID | N/A | No DOI provided; ACL Anthology ID is W03-0419 |

**Verdict: ALL CORRECT**

---

### 10. wang2023selfconsistency
**Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou (2023). "Self-Consistency Improves Chain of Thought Reasoning in Language Models". ICLR 2023. arXiv:2203.11171.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou |
| Year correct | ✓ | ICLR 2023 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | ICLR 2023 |
| arXiv ID correct | ✓ | 2203.11171 |

**Verdict: ALL CORRECT**

---

### 11. willard2023guided
**Brandon T. Willard, Remi Louf (2023). "Efficient Guided Generation for Large Language Models". arXiv:2307.09702.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Brandon T. Willard, Remi Louf (accent: Remi Louf) |
| Year correct | ✓ | 2023 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | Listed as arXiv preprint only, which is accurate -- DBLP also lists it only as CoRR abs/2307.09702 with no conference publication |
| arXiv ID correct | ✓ | 2307.09702 |

**Verdict: ALL CORRECT** -- Note: this paper remains an arXiv preprint and was not published at a peer-reviewed venue. The bib entry correctly lists it as arXiv only.

---

### 12. xia2025survey
**Zhiqiu Xia, Jinxuan Xu, Yuqian Zhang, Hang Liu (2025). "A Survey of Uncertainty Estimation Methods on Large Language Models". Findings of ACL 2025.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Zhiqiu Xia, Jinxuan Xu, Yuqian Zhang, Hang Liu |
| Year correct | ✓ | 2025 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | Findings of ACL 2025, confirmed via ACL Anthology |
| DOI/ID | N/A | No DOI was provided in the bib entry; ACL Anthology confirms the paper at 2025.findings-acl.1101 |

**Verdict: ALL CORRECT**

---

### 13. zheng2024llamafactory
**Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo (2024). "LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models". ACL 2024 System Demos, pp 400-410. DOI: 10.18653/v1/2024.acl-demos.38.**

| Check | Result | Notes |
|-------|--------|-------|
| Paper exists | ✓ | |
| Authors correct | ✓ | Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo |
| Year correct | ✓ | 2024 |
| Title correct | ✓ | Exact match |
| Venue correct | ✓ | ACL 2024 System Demonstrations, pp 400-410 |
| DOI correct | ✓ | 10.18653/v1/2024.acl-demos.38 |

**Verdict: ALL CORRECT**

---

## Summary

| # | Key | Verdict | Issues |
|---|-----|---------|--------|
| 1 | kuhn2023semantic | ✓ PASS | None |
| 2 | lightman2024verify | ⚠ MINOR | Author name forms: arXiv uses "Yura Burda"/"Harri Edwards"; DBLP canonical forms are "Yuri Burda"/"Harrison Edwards". Both acceptable. |
| 3 | luan2018scierc | ✓ PASS | None |
| 4 | yao2026consistency | ✓ PASS | None |
| 5 | sainz2024gollie | ✓ PASS | None |
| 6 | snell2025scaling | ⚠ MINOR | Title differs between arXiv version ("...Scaling Model Parameters") and ICLR proceedings version ("...Scaling Parameters for Reasoning"). Bib entry matches the ICLR proceedings title. |
| 7 | taubenfeld2025cisc | ✓ PASS | None |
| 8 | thirukovalluru2024atomic | ✓ PASS | None |
| 9 | tjongkimsang2003conll | ✓ PASS | None |
| 10 | wang2023selfconsistency | ✓ PASS | None |
| 11 | willard2023guided | ✓ PASS | Confirmed arXiv-only (no venue publication) |
| 12 | xia2025survey | ✓ PASS | None |
| 13 | zheng2024llamafactory | ✓ PASS | None |

**Overall: All 13 citations verified as real papers with correct metadata. Two entries have minor cosmetic issues (author name variants for #2, arXiv vs. proceedings title divergence for #6) -- neither requires correction.**

agentId: aabaae529e9394fae (use SendMessage with to: 'aabaae529e9394fae' to continue this agent)
&lt;usage>total_tokens: 39706
tool_uses: 21
duration_ms: 310183&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "3a7de409-e1ec-4d46-8a8d-29250e8c9581",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are verifying academic citations for correctness. For each entry below, search Google Scholar / DBLP to verify the paper exists and the metadata is correct. Use WebSearch for each entry.\n\nFor each entry, check: (1) authors correct, (2) year correct, (3) title correct, (4) venue correct, (5) DOI/arXiv ID correct, (6) paper actually exists.\n\nReturn a structured report for each entry with ✓/✗ for each check and details on any issues.\n\n## Entries to verify:\n\n1. **kuhn2023semantic**: Lorenz Kuhn, Yarin Gal, Sebastian Farquhar (2023). \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\". ICLR 2023. arXiv:2302.09664.\n   - Context: \"Semantic uncertainty\" and \"complementary model-internal alternatives\"\n\n2. **lightman2024verify**: Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe (2024). \"Let's Verify Step by Step\". ICLR 2024. arXiv:2305.20050.\n   - Context: \"trained verifiers\"\n\n3. **luan2018scierc**: Yi Luan, Luheng He, Mari Ostendorf, Hannaneh Hajishirzi (2018). \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\". EMNLP 2018. DOI: 10.18653/v1/D18-1360.\n   - Context: SciERC dataset citation\n\n4. **yao2026consistency**: Xinzhi Yao, Claire Nédellec, Jingbo Xia, Robert Bossy (2026). \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\". Genomics & Informatics. DOI: 10.1186/s44342-025-00063-2.\n   - Context: \"Prior work reports task-level correlations between consistency and accuracy\"\n\n5. **sainz2024gollie**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre (2024). \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\". ICLR 2024. arXiv:2310.03668.\n   - Context: \"generative IE\"\n\n6. **snell2025scaling**: Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar (2025). \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\". ICLR 2025. arXiv:2408.03314.\n   - Context: \"best-of-N with compute-optimal allocation\"\n\n7. **taubenfeld2025cisc**: Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, Gal Yona (2025). \"Confidence Improves Self-Consistency in LLMs\". Findings of ACL 2025. DOI: 10.18653/v1/2025.findings-acl.1030.\n   - Context: \"Reward-free selectors\"\n\n8. **thirukovalluru2024atomic**: Raghuveer Thirukovalluru, Yukun Huang, Bhuwan Dhingra (2024). \"Atomic Self-Consistency for Better Long Form Generations\". EMNLP 2024. DOI: 10.18653/v1/2024.emnlp-main.706.\n   - Context: \"atomic variants face limits where sub-output agreement does not yield selection gain\"\n\n9. **tjongkimsang2003conll**: Erik F. Tjong Kim Sang, Fien De Meulder (2003). \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\". CoNLL 2003.\n   - Context: CoNLL-2003 dataset citation\n\n10. **wang2023selfconsistency**: Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou (2023). \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\". ICLR 2023. arXiv:2203.11171.\n    - Context: Core self-consistency reference\n\n11. **willard2023guided**: Brandon T. Willard, Rémi Louf (2023). \"Efficient Guided Generation for Large Language Models\". arXiv:2307.09702.\n    - Context: \"constrained decoding\"\n\n12. **xia2025survey**: Zhiqiu Xia, Jinxuan Xu, Yuqian Zhang, Hang Liu (2025). \"A Survey of Uncertainty Estimation Methods on Large Language Models\". Findings of ACL 2025.\n    - Context: \"confidence estimation and uncertainty\"\n\n13. **zheng2024llamafactory**: Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo (2024). \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\". ACL 2024 System Demos, pp 400-410. DOI: 10.18653/v1/2024.acl-demos.38.\n    - Context: training framework citation\n",
    "agentId": "aabaae529e9394fae",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is the structured verification report.\n\n---\n\n## Citation Verification Report\n\n### 1. kuhn2023semantic\n**Lorenz Kuhn, Yarin Gal, Sebastian Farquhar (2023). \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\". ICLR 2023. arXiv:2302.09664.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Lorenz Kuhn, Yarin Gal, Sebastian Farquhar |\n| Year correct | ✓ | 2023 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | ICLR 2023 |\n| arXiv ID correct | ✓ | 2302.09664 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 2. lightman2024verify\n**Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe (2024). \"Let's Verify Step by Step\". ICLR 2024. arXiv:2305.20050.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✗ | The arXiv PDF uses \"Yura Burda\" and \"Harri Edwards\", but DBLP/official proceedings list \"Yuri Burda\" and \"Harrison Edwards\". The bib entry matches the arXiv PDF, so this is acceptable but not fully canonical. |\n| Year correct | ✓ | 2024 (ICLR 2024) |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | ICLR 2024 confirmed via OpenReview and proceedings |\n| arXiv ID correct | ✓ | 2305.20050 |\n\n**Verdict: MINOR ISSUE -- Author name forms \"Yura Burda\" / \"Harri Edwards\" are informal variants used on arXiv. The DBLP canonical forms are \"Yuri Burda\" / \"Harrison Edwards\". Either form is acceptable in practice.**\n\n---\n\n### 3. luan2018scierc\n**Yi Luan, Luheng He, Mari Ostendorf, Hannaneh Hajishirzi (2018). \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\". EMNLP 2018. DOI: 10.18653/v1/D18-1360.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Yi Luan, Luheng He, Mari Ostendorf, Hannaneh Hajishirzi |\n| Year correct | ✓ | 2018 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | EMNLP 2018, confirmed via ACL Anthology |\n| DOI correct | ✓ | 10.18653/v1/D18-1360 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 4. yao2026consistency\n**Xinzhi Yao, Claire Nédellec, Jingbo Xia, Robert Bossy (2026). \"Consistency--accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\". Genomics & Informatics. DOI: 10.1186/s44342-025-00063-2.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Xinzhi Yao, Claire Nédellec, Jingbo Xia, Robert Bossy |\n| Year correct | ✓ | Published 2026 (Genomics & Informatics, vol. 24, article 3, 2026) |\n| Title correct | ✓ | Exact match (with en-dash in \"Consistency--accuracy\") |\n| Venue correct | ✓ | Genomics & Informatics |\n| DOI correct | ✓ | 10.1186/s44342-025-00063-2 |\n\n**Verdict: ALL CORRECT** -- Note: the DOI has \"2025\" in the identifier string (s44342-**025**-00063-2) because DOIs are assigned at acceptance, but the publication year is 2026. This is normal for Springer journals.\n\n---\n\n### 5. sainz2024gollie\n**Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre (2024). \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\". ICLR 2024. arXiv:2310.03668.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre |\n| Year correct | ✓ | 2024 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | ICLR 2024 confirmed via OpenReview and proceedings |\n| arXiv ID correct | ✓ | 2310.03668 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 6. snell2025scaling\n**Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar (2025). \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\". ICLR 2025. arXiv:2408.03314.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar |\n| Year correct | ✓ | ICLR 2025 |\n| Title correct | ✗ | **Mismatch.** The bib entry says \"...Scaling Parameters for Reasoning\". The arXiv title is \"Scaling LLM Test-Time Compute Optimally **can** be More Effective than Scaling **Model Parameters**\" (no \"for Reasoning\", has \"Model\", lowercase \"can\"). The ICLR 2025 proceedings title is \"Scaling LLM Test-Time Compute Optimally **Can** be More Effective than Scaling Parameters **for Reasoning**\". So the bib title matches the ICLR proceedings title except for capitalization of \"Can\". |\n| Venue correct | ✓ | ICLR 2025 (Oral) |\n| arXiv ID correct | ✓ | 2408.03314 |\n\n**Verdict: MINOR ISSUE -- The title in the bib entry matches the ICLR 2025 proceedings version, which differs slightly from the arXiv version (arXiv says \"...Scaling Model Parameters\" without \"for Reasoning\"; ICLR says \"...Scaling Parameters for Reasoning\"). If you cite the ICLR proceedings version, the bib title is correct. Just note that the arXiv title is different.**\n\n---\n\n### 7. taubenfeld2025cisc\n**Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, Gal Yona (2025). \"Confidence Improves Self-Consistency in LLMs\". Findings of ACL 2025. DOI: 10.18653/v1/2025.findings-acl.1030.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, Gal Yona |\n| Year correct | ✓ | 2025 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | Findings of ACL 2025, confirmed via ACL Anthology |\n| DOI correct | ✓ | 10.18653/v1/2025.findings-acl.1030 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 8. thirukovalluru2024atomic\n**Raghuveer Thirukovalluru, Yukun Huang, Bhuwan Dhingra (2024). \"Atomic Self-Consistency for Better Long Form Generations\". EMNLP 2024. DOI: 10.18653/v1/2024.emnlp-main.706.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Raghuveer Thirukovalluru, Yukun Huang, Bhuwan Dhingra |\n| Year correct | ✓ | 2024 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | EMNLP 2024 (main), confirmed via ACL Anthology |\n| DOI correct | ✓ | 10.18653/v1/2024.emnlp-main.706 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 9. tjongkimsang2003conll\n**Erik F. Tjong Kim Sang, Fien De Meulder (2003). \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\". CoNLL 2003.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Erik F. Tjong Kim Sang, Fien De Meulder |\n| Year correct | ✓ | 2003 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | CoNLL 2003 (Proceedings of the Seventh Conference on Natural Language Learning at HLT-NAACL 2003) |\n| DOI/ID | N/A | No DOI provided; ACL Anthology ID is W03-0419 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 10. wang2023selfconsistency\n**Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou (2023). \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\". ICLR 2023. arXiv:2203.11171.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou |\n| Year correct | ✓ | ICLR 2023 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | ICLR 2023 |\n| arXiv ID correct | ✓ | 2203.11171 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 11. willard2023guided\n**Brandon T. Willard, Remi Louf (2023). \"Efficient Guided Generation for Large Language Models\". arXiv:2307.09702.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Brandon T. Willard, Remi Louf (accent: Remi Louf) |\n| Year correct | ✓ | 2023 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | Listed as arXiv preprint only, which is accurate -- DBLP also lists it only as CoRR abs/2307.09702 with no conference publication |\n| arXiv ID correct | ✓ | 2307.09702 |\n\n**Verdict: ALL CORRECT** -- Note: this paper remains an arXiv preprint and was not published at a peer-reviewed venue. The bib entry correctly lists it as arXiv only.\n\n---\n\n### 12. xia2025survey\n**Zhiqiu Xia, Jinxuan Xu, Yuqian Zhang, Hang Liu (2025). \"A Survey of Uncertainty Estimation Methods on Large Language Models\". Findings of ACL 2025.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Zhiqiu Xia, Jinxuan Xu, Yuqian Zhang, Hang Liu |\n| Year correct | ✓ | 2025 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | Findings of ACL 2025, confirmed via ACL Anthology |\n| DOI/ID | N/A | No DOI was provided in the bib entry; ACL Anthology confirms the paper at 2025.findings-acl.1101 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 13. zheng2024llamafactory\n**Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo (2024). \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\". ACL 2024 System Demos, pp 400-410. DOI: 10.18653/v1/2024.acl-demos.38.**\n\n| Check | Result | Notes |\n|-------|--------|-------|\n| Paper exists | ✓ | |\n| Authors correct | ✓ | Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo |\n| Year correct | ✓ | 2024 |\n| Title correct | ✓ | Exact match |\n| Venue correct | ✓ | ACL 2024 System Demonstrations, pp 400-410 |\n| DOI correct | ✓ | 10.18653/v1/2024.acl-demos.38 |\n\n**Verdict: ALL CORRECT**\n\n---\n\n## Summary\n\n| # | Key | Verdict | Issues |\n|---|-----|---------|--------|\n| 1 | kuhn2023semantic | ✓ PASS | None |\n| 2 | lightman2024verify | ⚠ MINOR | Author name forms: arXiv uses \"Yura Burda\"/\"Harri Edwards\"; DBLP canonical forms are \"Yuri Burda\"/\"Harrison Edwards\". Both acceptable. |\n| 3 | luan2018scierc | ✓ PASS | None |\n| 4 | yao2026consistency | ✓ PASS | None |\n| 5 | sainz2024gollie | ✓ PASS | None |\n| 6 | snell2025scaling | ⚠ MINOR | Title differs between arXiv version (\"...Scaling Model Parameters\") and ICLR proceedings version (\"...Scaling Parameters for Reasoning\"). Bib entry matches the ICLR proceedings title. |\n| 7 | taubenfeld2025cisc | ✓ PASS | None |\n| 8 | thirukovalluru2024atomic | ✓ PASS | None |\n| 9 | tjongkimsang2003conll | ✓ PASS | None |\n| 10 | wang2023selfconsistency | ✓ PASS | None |\n| 11 | willard2023guided | ✓ PASS | Confirmed arXiv-only (no venue publication) |\n| 12 | xia2025survey | ✓ PASS | None |\n| 13 | zheng2024llamafactory | ✓ PASS | None |\n\n**Overall: All 13 citations verified as real papers with correct metadata. Two entries have minor cosmetic issues (author name variants for #2, arXiv vs. proceedings title divergence for #6) -- neither requires correction.**"
      }
    ],
    "totalDurationMs": 310183,
    "totalTokens": 39706,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 34618,
      "output_tokens": 4205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 882
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4205,
          "cache_read_input_tokens": 34618,
          "cache_creation_input_tokens": 882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 882,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  }
}
```

</details>

---


### Assistant

_source line 379_

<details><summary>Logged reasoning block</summary>

```text
All 5 agents have returned. Let me now compile the results and also check for citation context correctness (item 8 — whether citations are used correctly in context). Let me also do some additional verification for the issues found.

Let me summarize the findings from all 5 agents:

**Batch 1 issues:**
- kang2025selfcertainty: NeurIPS 38 → should be NeurIPS 39 (ERROR)
- fleiss1971agreement: missing volume (76) and pages (378-382) (MINOR)
- holm1979simple: unused bib entry


**Batch 2 issues:**
- lightman2024verify: author name forms minor (Yura/Yuri, Harri/Harrison)
- snell2025scaling: title differs between arXiv and ICLR proceedings (MINOR)
**Batch 3 issues:**
- geifman2017selective: NeurIPS 30 → should be NIPS (conference name in 2017)
- dong2024xgrammar: now published at MLSys 2025, should update venue
**Batch 4 issues:**
- chen2023twofailures: key-year mismatch (cosmetic)
**Batch 5 issues:**
- muennighoff2025s1: title casing (cosmetic)
- li2024simple: unused bib entry
- yee2019noisy: Missing author Nathan Ng (HIGH)
- li2023stepaware: Title mismatch - "Large Language Models" vs published "Language Models" (MEDIUM)
- shinn2023reflexion: Missing author Edward Berman (HIGH)
- wang2025gptner: Missing author Chen Guo (HIGH)
- xiao2022uncertainty: unused bib entry

Now I'm spot-checking citation context accuracy for the critical entries, particularly huang2024large where the context mentions "introspection boundary" but I need to verify this aligns with what the paper actually discusses.

Looking at huang2024large, the paper is about LLMs struggling with self-correction reasoning, and the authors are using "introspection boundary" as their own framing to describe Huang et al.'s findings about internal versus external introspection limitations. The citation usage seems appropriate even though the specific term originates from the citing authors, not the cited paper itself.

For xie2023zeroshot, I'm checking whether the context accurately describes the paper's contribution regarding entity voting for zero-shot NER.

The bergkirkpatrick2012empirical citation is somewhat loosely applied—the paper addresses statistical significance in NLP broadly rather than NER evaluation methodology specifically, though it's not fundamentally incorrect.

Now I'm ready to compile the final report, but first I want to verify the most critical issues the agents uncovered—particularly the missing authors, the kang2025selfcertainty NeurIPS paper number, and whether brown2024monkeys has moved beyond arXiv status. Let me do some targeted searches on these key findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "50e5ef6e-0540-472f-a571-186e2a239f65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsDFpq5EBZBeXFsstdR3UD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9634,
      "cache_creation_input_tokens": 16123,
      "cache_read_input_tokens": 45225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16123
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

_source line 380_

所有 5 批验证完成。做几个关键问题的二次确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "8c24e98c-1267-412c-8494-c5321b31a720",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsDFpq5EBZBeXFsstdR3UD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9634,
      "cache_creation_input_tokens": 16123,
      "cache_read_input_tokens": 45225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16123
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

_source line 381_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M64dyNPnFYV3P1P5turgkB`</summary>

```json
{
  "query": "\"Simple and Effective Noisy Channel Modeling for Neural Machine Translation\" authors EMNLP 2019 \"Nathan Ng\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "4e591987-eb6e-47de-b2f9-ee97954b282e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsDFpq5EBZBeXFsstdR3UD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9634,
      "cache_creation_input_tokens": 16123,
      "cache_read_input_tokens": 45225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16123
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

_source line 382_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YPk1NxXaPQk3LfxjzLcUWk`</summary>

```json
{
  "query": "\"Reflexion: Language Agents with Verbal Reinforcement Learning\" NeurIPS 2023 authors \"Edward Berman\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "d30aba21-ffaf-406f-a4bb-3cd3d9a93e93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsDFpq5EBZBeXFsstdR3UD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9634,
      "cache_creation_input_tokens": 16123,
      "cache_read_input_tokens": 45225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16123
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

_source line 383_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K6vzJNLr1HRq4BAxdMEBKz`</summary>

```json
{
  "query": "\"GPT-NER: Named Entity Recognition via Large Language Models\" NAACL 2025 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "10557ae1-982a-4046-a8da-70b720754c21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsDFpq5EBZBeXFsstdR3UD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9634,
      "cache_creation_input_tokens": 16123,
      "cache_read_input_tokens": 45225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16123
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

_source line 384_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UNDiZqsizd3k3xuRJHo2dh`</summary>

```json
{
  "query": "\"Making Language Models Better Reasoners with Step-Aware Verifier\" ACL 2023 title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "dcc332c1-fa1c-4d35-8f35-102868d1040e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsDFpq5EBZBeXFsstdR3UD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9634,
      "cache_creation_input_tokens": 16123,
      "cache_read_input_tokens": 45225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16123
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

_source line 385 · 2026-05-26T10:26:15.076Z_

<details><summary>↩ Tool result · `toolu_01M64dyNPnFYV3P1P5turgkB`</summary>

```text
Web search results for query: ""Simple and Effective Noisy Channel Modeling for Neural Machine Translation" authors EMNLP 2019 "Nathan Ng""

Links: [{"title":"Simple and Effective Noisy Channel Modeling for Neural Machine Translation","url":"https://www.researchgate.net/publication/335233114_Simple_and_Effective_Noisy_Channel_Modeling_for_Neural_Machine_Translation"},{"title":"[1908.05731] Simple and Effective Noisy Channel Modeling for Neural Machine Translation","url":"https://arxiv.org/abs/1908.05731"},{"title":"Simple and Effective Noisy Channel Modeling for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/D19-1571/"},{"title":"[PDF] Simple and Effective Noisy Channel Modeling for Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Simple-and-Effective-Noisy-Channel-Modeling-for-Yee-Ng/c7b361427a54b309caea8ef69ed59b50cd54ac67"},{"title":"Issue #57 - Simple and Effective Noisy Channel Modeling for Neural MT","url":"https://www.rws.com/language-weaver/blog/issue-57-simple-and-effective-noisy-channel-modeling-for-neural-mt/"},{"title":"Simple and Effective Noisy Channel Modeling for Neural ...","url":"https://aclanthology.org/D19-1571.pdf"},{"title":"Fast Online Neural Noisy Channel Modeling - fairseq","url":"https://huggingface.co/spaces/sriramelango/Social_Classification_Public/blob/main/fairseq/examples/fast_noisy_channel/README.md"}]

I found the paper you're looking for. Here are the search results:

"Simple and Effective Noisy Channel Modeling for Neural Machine Translation" was published at EMNLP-IJCNLP 2019 with authors Kyra Yee, Nathan Ng, Yann N. Dauphin, and Michael Auli.

The paper addresses previous neural noisy channel modeling approaches that relied on latent variable models processing the source and target sentence incrementally, and proposes an alternative approach based on standard sequence to sequence models which utilize the entire source. Experiments show that noisy channel models can outperform a direct model by up to 3.2 BLEU on WMT'17 German-English translation.

The paper is available at multiple sources including:
- arXiv: https://arxiv.org/abs/1908.05731
- ACL Anthology: https://aclanthology.org/D19-1571/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "1adaa05b-ffb8-4e98-b0e2-80642240dc3b",
  "tool_use_result": {
    "query": "\"Simple and Effective Noisy Channel Modeling for Neural Machine Translation\" authors EMNLP 2019 \"Nathan Ng\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FhnqRR8fHF3jXbATCqpTrr",
        "content": [
          {
            "title": "Simple and Effective Noisy Channel Modeling for Neural Machine Translation",
            "url": "https://www.researchgate.net/publication/335233114_Simple_and_Effective_Noisy_Channel_Modeling_for_Neural_Machine_Translation"
          },
          {
            "title": "[1908.05731] Simple and Effective Noisy Channel Modeling for Neural Machine Translation",
            "url": "https://arxiv.org/abs/1908.05731"
          },
          {
            "title": "Simple and Effective Noisy Channel Modeling for Neural Machine Translation - ACL Anthology",
            "url": "https://aclanthology.org/D19-1571/"
          },
          {
            "title": "[PDF] Simple and Effective Noisy Channel Modeling for Neural Machine Translation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Simple-and-Effective-Noisy-Channel-Modeling-for-Yee-Ng/c7b361427a54b309caea8ef69ed59b50cd54ac67"
          },
          {
            "title": "Issue #57 - Simple and Effective Noisy Channel Modeling for Neural MT",
            "url": "https://www.rws.com/language-weaver/blog/issue-57-simple-and-effective-noisy-channel-modeling-for-neural-mt/"
          },
          {
            "title": "Simple and Effective Noisy Channel Modeling for Neural ...",
            "url": "https://aclanthology.org/D19-1571.pdf"
          },
          {
            "title": "Fast Online Neural Noisy Channel Modeling - fairseq",
            "url": "https://huggingface.co/spaces/sriramelango/Social_Classification_Public/blob/main/fairseq/examples/fast_noisy_channel/README.md"
          }
        ]
      },
      "I found the paper you're looking for. Here are the search results:\n\n\"Simple and Effective Noisy Channel Modeling for Neural Machine Translation\" was published at EMNLP-IJCNLP 2019 with authors Kyra Yee, Nathan Ng, Yann N. Dauphin, and Michael Auli.\n\nThe paper addresses previous neural noisy channel modeling approaches that relied on latent variable models processing the source and target sentence incrementally, and proposes an alternative approach based on standard sequence to sequence models which utilize the entire source. Experiments show that noisy channel models can outperform a direct model by up to 3.2 BLEU on WMT'17 German-English translation.\n\nThe paper is available at multiple sources including:\n- arXiv: https://arxiv.org/abs/1908.05731\n- ACL Anthology: https://aclanthology.org/D19-1571/"
    ],
    "durationSeconds": 5.043001525000029
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-26T10:26:15.839Z_

<details><summary>↩ Tool result · `toolu_01K6vzJNLr1HRq4BAxdMEBKz`</summary>

```text
Web search results for query: ""GPT-NER: Named Entity Recognition via Large Language Models" NAACL 2025 authors full list"

Links: [{"title":"GPT-NER: Named Entity Recognition via Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.239/"},{"title":"GPT-NER: Named Entity Recognition via Large Language ...","url":"https://aclanthology.org/2025.findings-naacl.239.pdf"},{"title":"GPT-NER: Named Entity Recognition via Large Language Models","url":"https://tianweiz07.github.io/Papers/25-naacl.pdf"},{"title":"GPT-NER: Named Entity Recognition via Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/392503828_GPT-NER_Named_Entity_Recognition_via_Large_Language_Models"},{"title":"[2304.10428] GPT-NER: Named Entity Recognition via Large Language Models","url":"https://arxiv.org/abs/2304.10428"},{"title":"[PDF] GPT-NER: Named Entity Recognition via Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GPT-NER:-Named-Entity-Recognition-via-Large-Models-Wang-Sun/7c9f69848d28e0a7cbb00942ee83dab9773c23e4"},{"title":"(PDF) GPT-NER: Named Entity Recognition via Large Language Models","url":"https://www.researchgate.net/publication/370152988_GPT-NER_Named_Entity_Recognition_via_Large_Language_Models"},{"title":"[Quick Review] GPT-NER: Named Entity Recognition via Large Language Models","url":"https://liner.com/review/gptner-named-entity-recognition-via-large-language-models"}]

Based on the search results, the full list of authors for "GPT-NER: Named Entity Recognition via Large Language Models" published at NAACL 2025 (pages 4257–4275) are: Shuhe Wang, Xiaofei Sun, Xiaoya Li, Rongbin Ouyang, Fei Wu, Tianwei Zhang, Jiwei Li, and Guoyin Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "dbcbd5b9-e2fa-485a-a8f8-43a3c354caf8",
  "tool_use_result": {
    "query": "\"GPT-NER: Named Entity Recognition via Large Language Models\" NAACL 2025 authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01METt6zeiCDVPxDPWCM7pA7",
        "content": [
          {
            "title": "GPT-NER: Named Entity Recognition via Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-naacl.239/"
          },
          {
            "title": "GPT-NER: Named Entity Recognition via Large Language ...",
            "url": "https://aclanthology.org/2025.findings-naacl.239.pdf"
          },
          {
            "title": "GPT-NER: Named Entity Recognition via Large Language Models",
            "url": "https://tianweiz07.github.io/Papers/25-naacl.pdf"
          },
          {
            "title": "GPT-NER: Named Entity Recognition via Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/392503828_GPT-NER_Named_Entity_Recognition_via_Large_Language_Models"
          },
          {
            "title": "[2304.10428] GPT-NER: Named Entity Recognition via Large Language Models",
            "url": "https://arxiv.org/abs/2304.10428"
          },
          {
            "title": "[PDF] GPT-NER: Named Entity Recognition via Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GPT-NER:-Named-Entity-Recognition-via-Large-Models-Wang-Sun/7c9f69848d28e0a7cbb00942ee83dab9773c23e4"
          },
          {
            "title": "(PDF) GPT-NER: Named Entity Recognition via Large Language Models",
            "url": "https://www.researchgate.net/publication/370152988_GPT-NER_Named_Entity_Recognition_via_Large_Language_Models"
          },
          {
            "title": "[Quick Review] GPT-NER: Named Entity Recognition via Large Language Models",
            "url": "https://liner.com/review/gptner-named-entity-recognition-via-large-language-models"
          }
        ]
      },
      "Based on the search results, the full list of authors for \"GPT-NER: Named Entity Recognition via Large Language Models\" published at NAACL 2025 (pages 4257–4275) are: Shuhe Wang, Xiaofei Sun, Xiaoya Li, Rongbin Ouyang, Fei Wu, Tianwei Zhang, Jiwei Li, and Guoyin Wang."
    ],
    "durationSeconds": 5.796644909000024
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-26T10:26:18.764Z_

<details><summary>↩ Tool result · `toolu_01UNDiZqsizd3k3xuRJHo2dh`</summary>

```text
Web search results for query: ""Making Language Models Better Reasoners with Step-Aware Verifier" ACL 2023 title"

Links: [{"title":"Making Language Models Better Reasoners with Step-Aware Verifier - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.291/"},{"title":"ACL2023: Making Language Models Better Reasoners with Step-Aware Verifier","url":"https://virtual2023.aclweb.org/paper_P5316.html"},{"title":"Making Language Models Better Reasoners with Step-Aware Verifier - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/making-language-models-better-reasoners-with-step-aware-verifier/"},{"title":"[2206.02336] Making Large Language Models Better Reasoners with Step-Aware Verifier","url":"https://arxiv.org/abs/2206.02336"},{"title":"Making Language Models Better Reasoners with Step-Aware Verifier | CoLab","url":"https://colab.ws/articles/10.18653/v1/2023.acl-long.291"},{"title":"[PDF] Making Language Models Better Reasoners with Step-Aware Verifier | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Making-Language-Models-Better-Reasoners-with-Li-Lin/e826ac71dad8c4ce36d82fb7add43e3d306bb7e1"},{"title":"Making Large Language Models Better Reasoners with Step-Aware Verifier","url":"https://arxiv.org/pdf/2206.02336"},{"title":"Making Large Language Models Better Reasoners with Step-Aware Verifier","url":"https://openreview.net/pdf?id=12-I0-XoAt6"},{"title":"Making Language Models Better Reasoners with Step-Aware Verifier | Request PDF","url":"https://www.researchgate.net/publication/372915794_Making_Language_Models_Better_Reasoners_with_Step-Aware_Verifier"}]

I found the paper you're looking for! Here are the key details:

**Title:** Making Language Models Better Reasoners with Step-Aware Verifier

**Authors:** Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen, Jian-Guang Lou, and Weizhu Chen

**Publication:** Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5315–5333, Toronto, Canada

**Main Contribution:** The paper presents DiVeRSe (Diverse Verifier on Reasoning Step), a novel approach that further enhances the reasoning capability of language models. DiVeRSe has three main components: first, it generates diverse prompts to explore different reasoning paths for the same question; second, it uses a verifier to filter out incorrect answers based on a weighted voting scheme; and third, it verifies each reasoning step individually instead of the whole chain.

**Results:** It achieves new state-of-the-art results on six of eight reasoning benchmarks (e.g., GSM8K 74.4% to 83.2%).

You can access the paper at the ACL Anthology: https://aclanthology.org/2023.acl-long.291/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "681983a8-876a-4680-8485-f5612b04a6b5",
  "tool_use_result": {
    "query": "\"Making Language Models Better Reasoners with Step-Aware Verifier\" ACL 2023 title",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nz4zQA2wKLxmfD9ffxDtwy",
        "content": [
          {
            "title": "Making Language Models Better Reasoners with Step-Aware Verifier - ACL Anthology",
            "url": "https://aclanthology.org/2023.acl-long.291/"
          },
          {
            "title": "ACL2023: Making Language Models Better Reasoners with Step-Aware Verifier",
            "url": "https://virtual2023.aclweb.org/paper_P5316.html"
          },
          {
            "title": "Making Language Models Better Reasoners with Step-Aware Verifier - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/publication/making-language-models-better-reasoners-with-step-aware-verifier/"
          },
          {
            "title": "[2206.02336] Making Large Language Models Better Reasoners with Step-Aware Verifier",
            "url": "https://arxiv.org/abs/2206.02336"
          },
          {
            "title": "Making Language Models Better Reasoners with Step-Aware Verifier | CoLab",
            "url": "https://colab.ws/articles/10.18653/v1/2023.acl-long.291"
          },
          {
            "title": "[PDF] Making Language Models Better Reasoners with Step-Aware Verifier | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Making-Language-Models-Better-Reasoners-with-Li-Lin/e826ac71dad8c4ce36d82fb7add43e3d306bb7e1"
          },
          {
            "title": "Making Large Language Models Better Reasoners with Step-Aware Verifier",
            "url": "https://arxiv.org/pdf/2206.02336"
          },
          {
            "title": "Making Large Language Models Better Reasoners with Step-Aware Verifier",
            "url": "https://openreview.net/pdf?id=12-I0-XoAt6"
          },
          {
            "title": "Making Language Models Better Reasoners with Step-Aware Verifier | Request PDF",
            "url": "https://www.researchgate.net/publication/372915794_Making_Language_Models_Better_Reasoners_with_Step-Aware_Verifier"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Title:** Making Language Models Better Reasoners with Step-Aware Verifier\n\n**Authors:** Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen, Jian-Guang Lou, and Weizhu Chen\n\n**Publication:** Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5315–5333, Toronto, Canada\n\n**Main Contribution:** The paper presents DiVeRSe (Diverse Verifier on Reasoning Step), a novel approach that further enhances the reasoning capability of language models. DiVeRSe has three main components: first, it generates diverse prompts to explore different reasoning paths for the same question; second, it uses a verifier to filter out incorrect answers based on a weighted voting scheme; and third, it verifies each reasoning step individually instead of the whole chain.\n\n**Results:** It achieves new state-of-the-art results on six of eight reasoning benchmarks (e.g., GSM8K 74.4% to 83.2%).\n\nYou can access the paper at the ACL Anthology: https://aclanthology.org/2023.acl-long.291/"
    ],
    "durationSeconds": 8.553991868000011
  }
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-26T10:26:20.647Z_

<details><summary>↩ Tool result · `toolu_01YPk1NxXaPQk3LfxjzLcUWk`</summary>

```text
Web search results for query: ""Reflexion: Language Agents with Verbal Reinforcement Learning" NeurIPS 2023 authors "Edward Berman""

Links: [{"title":"Reflexion: language agents with verbal reinforcement learning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html"},{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"Reflexion: language agents with verbal reinforcement learning | OpenReview","url":"https://openreview.net/forum?id=vAElhFcKW6"},{"title":"Reflexion: language agents with verbal reinforcement learning","url":"https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/noahshinn/reflexion/tree/main"},{"title":"GitHub - RbKomar/reflexion-forked: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/RbKomar/reflexion-forked"},{"title":"[Paper Note] Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, NeurIPS'23, 2023.03 · Issue #512 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/512"}]

I found the research paper you're looking for! Here are the key details:

**Paper Title:** Reflexion: Language Agents with Verbal Reinforcement Learning

**Authors:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao

**Conference:** NeurIPS 2023

**ArXiv ID:** 2303.11366

**Overview:** Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.

The paper is available on multiple platforms including:
- arXiv: https://arxiv.org/abs/2303.11366
- NeurIPS proceedings: https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html
- GitHub repository with code: https://github.com/noahshinn/reflexion


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "4279c0f5-d208-4cae-aeae-6dfe766fcdb9",
  "tool_use_result": {
    "query": "\"Reflexion: Language Agents with Verbal Reinforcement Learning\" NeurIPS 2023 authors \"Edward Berman\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_018yth34X6xjD87pLRvjDTan",
        "content": [
          {
            "title": "Reflexion: language agents with verbal reinforcement learning",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html"
          },
          {
            "title": "[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2303.11366"
          },
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub",
            "url": "https://github.com/noahshinn/reflexion"
          },
          {
            "title": "Reflexion: language agents with verbal reinforcement learning | OpenReview",
            "url": "https://openreview.net/forum?id=vAElhFcKW6"
          },
          {
            "title": "Reflexion: language agents with verbal reinforcement learning",
            "url": "https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/html/2303.11366"
          },
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://github.com/noahshinn/reflexion/tree/main"
          },
          {
            "title": "GitHub - RbKomar/reflexion-forked: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://github.com/RbKomar/reflexion-forked"
          },
          {
            "title": "[Paper Note] Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, NeurIPS'23, 2023.03 · Issue #512 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/512"
          }
        ]
      },
      "I found the research paper you're looking for! Here are the key details:\n\n**Paper Title:** Reflexion: Language Agents with Verbal Reinforcement Learning\n\n**Authors:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\n\n**Conference:** NeurIPS 2023\n\n**ArXiv ID:** 2303.11366\n\n**Overview:** Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.\n\nThe paper is available on multiple platforms including:\n- arXiv: https://arxiv.org/abs/2303.11366\n- NeurIPS proceedings: https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html\n- GitHub repository with code: https://github.com/noahshinn/reflexion"
    ],
    "durationSeconds": 10.610479984000035
  }
}
```

</details>

---


### Assistant

_source line 389_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed the key issues:

1. **yee2019noisy**: Confirmed - Nathan Ng is a missing author. The ACL Anthology listing shows 4 authors: Kyra Yee, Nathan Ng, Yann N. Dauphin, Michael Auli.

2. **shinn2023reflexion**: Confirmed - Edward Berman is a missing author. NeurIPS proceedings show 6 authors: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao.
   
3. **wang2025gptner**: The ACL Anthology search results list 8 authors matching the bib entry, but the agent claimed there's a 9th author "Chen Guo" that I can't verify in the official listing. The author list appears to be cut off in the search results, so I need to look more carefully at the complete information.

4. **li2023stepaware**: The published ACL 2023 version has the title "Making Language Models Better Reasoners with Step-Aware Verifier" without "Large," while the bib entry includes "Large" in the title. The arXiv preprint does have "Large," so this is a discrepancy between the preprint and published versions.

I should also verify whether brown2024monkeys and cobbe2021verifiers are still only available as arXiv preprints or if they've been published elsewhere, and check the citation contexts for these papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "e880a116-398f-4f21-9a63-fb07332f4457",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkZ4L4PRfrLtRYtkfkgJt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1462,
      "cache_creation_input_tokens": 12500,
      "cache_read_input_tokens": 61348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12500
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

_source line 390_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Np8j9U5efzFBiT9NEuEJTx`</summary>

```json
{
  "query": "\"Large Language Monkeys\" Brown Juravsky 2024 conference published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "8a5a8723-626f-407d-a10b-cf98fd52a490",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkZ4L4PRfrLtRYtkfkgJt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1462,
      "cache_creation_input_tokens": 12500,
      "cache_read_input_tokens": 61348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12500
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

_source line 391_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RyMwnbo6iEhoQKMJ57ZF38`</summary>

```json
{
  "query": "\"Training Verifiers to Solve Math Word Problems\" Cobbe 2021 conference published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "c03e54f6-fba0-4663-9db1-3b2cc903485d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkZ4L4PRfrLtRYtkfkgJt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1462,
      "cache_creation_input_tokens": 12500,
      "cache_read_input_tokens": 61348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12500
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

_source line 392_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QG9Y2RhCnRA4p2a6RPnQ3C`</summary>

```json
{
  "query": "\"Scalable Best-of-N Selection\" \"Self-Certainty\" Kang Zhao Song NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "9aa97991-c862-4c52-8788-ceaf5e97141c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkZ4L4PRfrLtRYtkfkgJt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1462,
      "cache_creation_input_tokens": 12500,
      "cache_read_input_tokens": 61348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12500
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

_source line 393 · 2026-05-26T10:26:41.197Z_

<details><summary>↩ Tool result · `toolu_01RyMwnbo6iEhoQKMJ57ZF38`</summary>

```text
Web search results for query: ""Training Verifiers to Solve Math Word Problems" Cobbe 2021 conference published venue"

Links: [{"title":"[PDF] Training Verifiers to Solve Math Word Problems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Verifiers-to-Solve-Math-Word-Problems-Cobbe-Kosaraju/d6045d2ccc9c09ca1671348de86d07da6bc28eea"},{"title":"[2110.14168] Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/abs/2110.14168"},{"title":"[Paper Note] Training Verifiers to Solve Math Word Problems, Karl Cobbe+, arXiv'21, 2021.10 · Issue #1618 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1618"},{"title":"(Open Access) Training Verifiers to Solve Math Word Problems (2021) | Karl Cobbe | 2 Citations","url":"https://scispace.com/papers/training-verifiers-to-solve-math-word-problems-2jokilm0qa"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://www.researchgate.net/publication/355698629_Training_Verifiers_to_Solve_Math_Word_Problems"},{"title":"Training Verifiers to Solve Math Word Problems - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2110.14168"},{"title":"Paper page - Training Verifiers to Solve Math Word Problems","url":"https://huggingface.co/papers/2110.14168"},{"title":"dblp: Training Verifiers to Solve Math Word Problems.","url":"https://dblp.org/rec/journals/corr/abs-2110-14168.html"}]

Based on the search results, "Training Verifiers to Solve Math Word Problems" by Karl Cobbe and colleagues was published on arXiv in 2021. More specifically, the paper was first submitted on October 27, 2021.

The paper was published as a preprint on arXiv rather than at a traditional academic conference. It is catalogued as CoRR abs/2110.14168 (2021), where CoRR stands for "Computing Research Repository" on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "fcd2471c-3124-4897-9fa1-c48a23386569",
  "tool_use_result": {
    "query": "\"Training Verifiers to Solve Math Word Problems\" Cobbe 2021 conference published venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KkHhZURFhxZProHG7Y7pLX",
        "content": [
          {
            "title": "[PDF] Training Verifiers to Solve Math Word Problems | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Training-Verifiers-to-Solve-Math-Word-Problems-Cobbe-Kosaraju/d6045d2ccc9c09ca1671348de86d07da6bc28eea"
          },
          {
            "title": "[2110.14168] Training Verifiers to Solve Math Word Problems",
            "url": "https://arxiv.org/abs/2110.14168"
          },
          {
            "title": "[Paper Note] Training Verifiers to Solve Math Word Problems, Karl Cobbe+, arXiv'21, 2021.10 · Issue #1618 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/1618"
          },
          {
            "title": "(Open Access) Training Verifiers to Solve Math Word Problems (2021) | Karl Cobbe | 2 Citations",
            "url": "https://scispace.com/papers/training-verifiers-to-solve-math-word-problems-2jokilm0qa"
          },
          {
            "title": "Training Verifiers to Solve Math Word Problems",
            "url": "https://www.researchgate.net/publication/355698629_Training_Verifiers_to_Solve_Math_Word_Problems"
          },
          {
            "title": "Training Verifiers to Solve Math Word Problems - ar5iv - arXiv",
            "url": "https://ar5iv.labs.arxiv.org/html/2110.14168"
          },
          {
            "title": "Paper page - Training Verifiers to Solve Math Word Problems",
            "url": "https://huggingface.co/papers/2110.14168"
          },
          {
            "title": "dblp: Training Verifiers to Solve Math Word Problems.",
            "url": "https://dblp.org/rec/journals/corr/abs-2110-14168.html"
          }
        ]
      },
      "Based on the search results, \"Training Verifiers to Solve Math Word Problems\" by Karl Cobbe and colleagues was published on arXiv in 2021. More specifically, the paper was first submitted on October 27, 2021.\n\nThe paper was published as a preprint on arXiv rather than at a traditional academic conference. It is catalogued as CoRR abs/2110.14168 (2021), where CoRR stands for \"Computing Research Repository\" on arXiv."
    ],
    "durationSeconds": 6.649027769000036
  }
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-26T10:26:41.586Z_

<details><summary>↩ Tool result · `toolu_01Np8j9U5efzFBiT9NEuEJTx`</summary>

```text
Web search results for query: ""Large Language Monkeys" Brown Juravsky 2024 conference published venue"

Links: [{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | Scaling Intelligence Lab at Stanford University","url":"https://scalingintelligence.stanford.edu/pubs/large_language_monkeys/"},{"title":"Monkey Business: a Dataset of Large LLM Sample Collections for Math and Code Tasks | Scaling Intelligence Lab at Stanford University","url":"https://scalingintelligence.stanford.edu/blogs/monkeys/"},{"title":"[2407.21787] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/abs/2407.21787"},{"title":"GitHub - ScalingIntelligence/large_language_monkeys","url":"https://github.com/ScalingIntelligence/large_language_monkeys"},{"title":"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://arxiv.org/pdf/2407.21787"},{"title":"dblp: Large Language Monkeys: Scaling Inference Compute with Repeated Sampling.","url":"https://dblp.org/rec/journals/corr/abs-2407-21787.html"},{"title":"(PDF) Large Language Monkeys: Scaling Inference Compute with Repeated Sampling","url":"https://www.researchgate.net/publication/382739350_Large_Language_Monkeys_Scaling_Inference_Compute_with_Repeated_Sampling"},{"title":"[Research Paper Summary] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | by Himanshu Bamoria | Athina AI | Medium","url":"https://medium.com/athina-ai/large-language-monkeys-scaling-inference-compute-with-repeated-sampling-4de85a3e1384"},{"title":"[PDF] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Monkeys:-Scaling-Inference-Compute-Brown-Juravsky/f66b6049946a10080d1f2a7ee6a40e5cca3ee6a0"},{"title":"(PDF) How Do Large Language Monkeys Get Their Power (Laws)?","url":"https://www.researchgate.net/publication/389351809_How_Do_Large_Language_Monkeys_Get_Their_Power_Laws"}]

Based on the search results, here's what I found about "Large Language Monkeys" by Brown and Juravsky:

## Publication Details

The paper "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling" is authored by Bradley Brown and Jordan Juravsky, along with Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, and Azalia Mirhoseini.

## Published Venue

The paper was published on arXiv as CoRR abs/2407.21787 in 2024. This is a preprint server rather than a traditional conference venue.

## Publication Date

The paper was dated July 31, 2024.

The search results indicate this is an arXiv preprint publication rather than a conference paper. There is no indication in the search results that it was presented at or published in a traditional conference venue in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "fda83d13-7088-49fc-a7b4-ec2d9f95a22e",
  "tool_use_result": {
    "query": "\"Large Language Monkeys\" Brown Juravsky 2024 conference published venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WvAu4Bfr6P4ubRkGfipAhs",
        "content": [
          {
            "title": "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | Scaling Intelligence Lab at Stanford University",
            "url": "https://scalingintelligence.stanford.edu/pubs/large_language_monkeys/"
          },
          {
            "title": "Monkey Business: a Dataset of Large LLM Sample Collections for Math and Code Tasks | Scaling Intelligence Lab at Stanford University",
            "url": "https://scalingintelligence.stanford.edu/blogs/monkeys/"
          },
          {
            "title": "[2407.21787] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling",
            "url": "https://arxiv.org/abs/2407.21787"
          },
          {
            "title": "GitHub - ScalingIntelligence/large_language_monkeys",
            "url": "https://github.com/ScalingIntelligence/large_language_monkeys"
          },
          {
            "title": "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling",
            "url": "https://arxiv.org/pdf/2407.21787"
          },
          {
            "title": "dblp: Large Language Monkeys: Scaling Inference Compute with Repeated Sampling.",
            "url": "https://dblp.org/rec/journals/corr/abs-2407-21787.html"
          },
          {
            "title": "(PDF) Large Language Monkeys: Scaling Inference Compute with Repeated Sampling",
            "url": "https://www.researchgate.net/publication/382739350_Large_Language_Monkeys_Scaling_Inference_Compute_with_Repeated_Sampling"
          },
          {
            "title": "[Research Paper Summary] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | by Himanshu Bamoria | Athina AI | Medium",
            "url": "https://medium.com/athina-ai/large-language-monkeys-scaling-inference-compute-with-repeated-sampling-4de85a3e1384"
          },
          {
            "title": "[PDF] Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Large-Language-Monkeys:-Scaling-Inference-Compute-Brown-Juravsky/f66b6049946a10080d1f2a7ee6a40e5cca3ee6a0"
          },
          {
            "title": "(PDF) How Do Large Language Monkeys Get Their Power (Laws)?",
            "url": "https://www.researchgate.net/publication/389351809_How_Do_Large_Language_Monkeys_Get_Their_Power_Laws"
          }
        ]
      },
      "Based on the search results, here's what I found about \"Large Language Monkeys\" by Brown and Juravsky:\n\n## Publication Details\n\nThe paper \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\" is authored by Bradley Brown and Jordan Juravsky, along with Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, and Azalia Mirhoseini.\n\n## Published Venue\n\nThe paper was published on arXiv as CoRR abs/2407.21787 in 2024. This is a preprint server rather than a traditional conference venue.\n\n## Publication Date\n\nThe paper was dated July 31, 2024.\n\nThe search results indicate this is an arXiv preprint publication rather than a conference paper. There is no indication in the search results that it was presented at or published in a traditional conference venue in 2024."
    ],
    "durationSeconds": 7.723816271000018
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-26T10:26:43.441Z_

<details><summary>↩ Tool result · `toolu_01QG9Y2RhCnRA4p2a6RPnQ3C`</summary>

```text
Web search results for query: ""Scalable Best-of-N Selection" "Self-Certainty" Kang Zhao Song NeurIPS 2025"

Links: [{"title":"NeurIPS Poster Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://neurips.cc/virtual/2025/poster/120166"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty | OpenReview","url":"https://openreview.net/forum?id=29FRqmVQK8"},{"title":"[2502.18581] Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/abs/2502.18581"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/pdf/2502.18581"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/scalable-best-n-selection-large-language-models"},{"title":"[Literature Review] Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://www.themoonlight.io/en/review/scalable-best-of-n-selection-for-large-language-models-via-self-certainty"}]

Great! I found the paper. Here's what I found:

The paper "Scalable Best-of-N Selection for Large Language Models via Self-Certainty" was presented as a poster at NeurIPS 2025 by Zhewei Kang, Xuandong Zhao, and Dawn Song.

**Main Contribution:**

The authors propose self-certainty, a novel and efficient metric that leverages the inherent probability distribution of LLM outputs to estimate response quality without requiring external reward models.

**Key Features:**

The research demonstrates that self-certainty (1) scales effectively with increasing sample size N, akin to reward models but without the computational overhead; (2) complements chain-of-thought, improving reasoning performance beyond greedy decoding; and (3) generalizes to open-ended tasks where traditional self-consistency methods fall short.

**Background:**

Current state-of-the-art methods often employ computationally intensive reward models for response evaluation and selection. Reward-free alternatives, like self-consistency and universal self-consistency, are limited in their ability to handle open-ended generation tasks or scale effectively.

The paper has been published on arXiv and is available on OpenReview, with code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "24f3ff39-9f7a-482f-a7f0-ba2c38c8d45d",
  "tool_use_result": {
    "query": "\"Scalable Best-of-N Selection\" \"Self-Certainty\" Kang Zhao Song NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T8EEJc8L2vZcMJjwxKfWea",
        "content": [
          {
            "title": "NeurIPS Poster Scalable Best-of-N Selection for Large Language Models via Self-Certainty",
            "url": "https://neurips.cc/virtual/2025/poster/120166"
          },
          {
            "title": "Scalable Best-of-N Selection for Large Language Models via Self-Certainty | OpenReview",
            "url": "https://openreview.net/forum?id=29FRqmVQK8"
          },
          {
            "title": "[2502.18581] Scalable Best-of-N Selection for Large Language Models via Self-Certainty",
            "url": "https://arxiv.org/abs/2502.18581"
          },
          {
            "title": "Scalable Best-of-N Selection for Large Language Models via Self-Certainty",
            "url": "https://arxiv.org/pdf/2502.18581"
          },
          {
            "title": "Scalable Best-of-N Selection for Large Language Models via Self-Certainty | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/scalable-best-n-selection-large-language-models"
          },
          {
            "title": "[Literature Review] Scalable Best-of-N Selection for Large Language Models via Self-Certainty",
            "url": "https://www.themoonlight.io/en/review/scalable-best-of-n-selection-for-large-language-models-via-self-certainty"
          }
        ]
      },
      "Great! I found the paper. Here's what I found:\n\nThe paper \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\" was presented as a poster at NeurIPS 2025 by Zhewei Kang, Xuandong Zhao, and Dawn Song.\n\n**Main Contribution:**\n\nThe authors propose self-certainty, a novel and efficient metric that leverages the inherent probability distribution of LLM outputs to estimate response quality without requiring external reward models.\n\n**Key Features:**\n\nThe research demonstrates that self-certainty (1) scales effectively with increasing sample size N, akin to reward models but without the computational overhead; (2) complements chain-of-thought, improving reasoning performance beyond greedy decoding; and (3) generalizes to open-ended tasks where traditional self-consistency methods fall short.\n\n**Background:**\n\nCurrent state-of-the-art methods often employ computationally intensive reward models for response evaluation and selection. Reward-free alternatives, like self-consistency and universal self-consistency, are limited in their ability to handle open-ended generation tasks or scale effectively.\n\nThe paper has been published on arXiv and is available on OpenReview, with code available on GitHub."
    ],
    "durationSeconds": 8.329951346000016
  }
}
```

</details>

---


### Assistant

_source line 396_

<details><summary>Logged reasoning block</summary>

```text
Good. So:
- brown2024monkeys: still arXiv-only. Correct as listed.
- cobbe2021verifiers: still arXiv-only. Correct as listed.
- kang2025selfcertainty: NeurIPS 2025 poster. The bib says "NeurIPS 38" but NeurIPS 2025 is the 39th conference. Let me confirm: NeurIPS 2017 = 31st, NeurIPS 2018 = 32nd, NeurIPS 2019 = 33rd, NeurIPS 2020 = 34th, NeurIPS 2021 = 35th, NeurIPS 2022 = 36th, NeurIPS 2023 = 37th, NeurIPS 2024 = 38th, NeurIPS 2025 = 39th. 

So the bib entry has the wrong conference number—it should be 39, not 38.

Now let me look more carefully at the ACL Anthology entry for wang2025gptner to verify the author details. Continuing through the remaining corrections: several entries are missing authors entirely—Ng should be listed as one of four authors in yee2019noisy, and Berman needs to be added to shinn2023reflexion's author list. The li2023stepaware entry has a title discrepancy where the bibliography says "Large Language Models" but the actual ACL 2023 publication omits "Large." I also notice dong2024xgrammar has since been published at MLSys 2025, so that venue information should be updated from its arXiv status. For the older citations, fleiss1971agreement is missing its volume and page numbers, geifman2017selective uses the outdated "NeurIPS 30" nomenclature when it should just be "NIPS" for 2017, and lightman2024verify has minor author name variations that could be standardized. I'm still reviewing the snell2025scaling entry.

Now I'm checking the citation contexts to verify they're being used appropriately. The huang2024large citation supports the claim about models struggling with self-evaluation, though "introspection boundary" appears to be the authors' own framing rather than terminology from Huang's paper—but this is still a reasonable application of the source material.

For kirkpatrick2012empirical, the citation attributes the 1.0pp significance threshold specifically to NER evaluation methodology, when the paper actually addresses statistical significance in NLP more broadly. It does cover NER, so the citation isn't wrong, just somewhat imprecise in its framing.

The xie2023zeroshot citation for entity voting in zero-shot NER checks out correctly. I have what I need to finalize the report now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "1c6ac6d7-7d87-4138-84c9-3069d5e94b82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ucyBUobRBwNJbf4eP3TNy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4436,
      "cache_read_input_tokens": 73848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4436
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

_source line 397_

所有验证完成。现在编写完整报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "100eabf2-79c5-4806-b713-1347890a3e6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ucyBUobRBwNJbf4eP3TNy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4436,
      "cache_read_input_tokens": 73848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4436
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

_source line 398_

<details open><summary>🔧 Tool call — Write · `toolu_01TJc5REpeAnCkbowzBqjS4W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ref_audit_worker_B.md",
  "content": "# 引用验证清单 (Worker B — Google Scholar / DBLP 优先)\n\n**验证日期**: 2026-05-26\n**验证方式**: WebSearch (Google Scholar, DBLP, ACL Anthology, arXiv, NeurIPS/ICML proceedings)\n\n总 bib entries: **64**\n总 cite keys in tex: **61**\n未使用的 bib entries: `holm1979simple`, `li2024simple`, `xiao2022uncertainty`\ntex 中引用但 bib 缺失: **无**\n\n---\n\n## 问题汇总\n\n| 严重性 | 条目 | 问题 |\n|--------|------|------|\n| ⚠️ 需修正 | `kang2025selfcertainty` | NeurIPS volume 号错：写了 38，应为 39（NeurIPS 2025 = 第 39 届） |\n| ⚠️ 需修正 | `yee2019noisy` | 缺少作者 Nathan Ng（应为 4 人，非 3 人） |\n| ⚠️ 需修正 | `shinn2023reflexion` | 缺少作者 Edward Berman（应为 6 人，非 5 人） |\n| ⚠️ 需修正 | `li2023stepaware` | 标题不一致：bib 写 \"Making **Large** Language Models...\"，ACL 2023 正式版为 \"Making Language Models...\"（无 \"Large\"） |\n| ⚠️ 建议修正 | `dong2024xgrammar` | 已在 MLSys 2025 正式发表，bib 仅列 arXiv preprint，建议更新 venue |\n| ⚠️ 建议修正 | `fleiss1971agreement` | 缺少 volume (76) 和 pages (378–382) |\n| ⚠️ 建议修正 | `geifman2017selective` | \"NeurIPS 30\" 时间上不准确，2017 年会议名称仍为 NIPS（2018 年才改名 NeurIPS） |\n| 🧹 清理 | `holm1979simple` | 未被引用，可移除 |\n| 🧹 清理 | `li2024simple` | 未被引用，可移除 |\n| 🧹 清理 | `xiao2022uncertainty` | 未被引用，可移除 |\n\n---\n\n## 逐条验证\n\n### 1. [landesberg2026bon] Landesberg (2026). \"When LLM Judge Scores Look Good but Best-of-N Decisions Fail\". arXiv:2603.12520.\n- 在线验证：arXiv ✓ 找到\n- 作者：✓\n- 年份：✓ 2026\n- 标题：✓\n- Venue：✓ arXiv preprint\n- DOI/arXiv：✓ 2603.12520\n- 论文存在：✓\n- 引用上下文：✓ — \"\\citet{landesberg2026bon} independently document a correlation-selection gap in best-of-N reasoning: global judge r=0.47 masks within-prompt r=0.27\" 准确描述了论文内容\n- **结论：✅ OK**\n\n### 2. [holm1979simple] Holm (1979). \"A Simple Sequentially Rejective Multiple Test Procedure\". Scandinavian J. Statistics 6(2), 65–70.\n- 在线验证：Google Scholar ✓ 找到（经典论文，5万+引用）\n- 作者：✓ Sture Holm\n- 年份：✓ 1979\n- 标题：✓\n- Venue：✓ Scandinavian Journal of Statistics, Vol 6, No 2, pp 65–70\n- DOI/arXiv：N/A（1979年无DOI）\n- 论文存在：✓\n- 引用上下文：N/A — **未在任何 tex 文件中被引用**\n- **结论：⚠️ 未使用，建议移除或确认是否需要**\n\n### 3. [brown2024monkeys] Brown et al. (2024). \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\". arXiv:2407.21787.\n- 在线验证：arXiv ✓ | Google Scholar ✓\n- 作者：✓ Brown, Juravsky, Ehrlich, Clark, Le, Ré, Mirhoseini\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ arXiv preprint（确认仍为 preprint，未正式发表于会议）\n- DOI/arXiv：✓ 2407.21787\n- 论文存在：✓\n- 引用上下文：✓ — 用于引用推理任务中 inference compute scaling、oracle F1 scaling 对比\n- **结论：✅ OK**\n\n### 4. [chen2024usc] Chen et al. (2024). \"Universal Self-Consistency for Large Language Model Generation\". ICML 2024 Workshop on In-Context Learning. arXiv:2311.17311.\n- 在线验证：arXiv ✓ | ICML 2024 workshop ✓\n- 作者：✓ 全部 10 位作者正确\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICML 2024 Workshop on In-Context Learning\n- DOI/arXiv：✓ 2311.17311\n- 论文存在：✓\n- 引用上下文：✓ — \"free-form variants face limits where sub-output agreement does not yield selection gain\"\n- **结论：✅ OK**\n\n### 5. [cobbe2021verifiers] Cobbe et al. (2021). \"Training Verifiers to Solve Math Word Problems\". arXiv:2110.14168.\n- 在线验证：arXiv ✓ | Google Scholar ✓\n- 作者：✓ 全部 12 位作者正确\n- 年份：✓ 2021\n- 标题：✓\n- Venue：✓ arXiv preprint（确认仍为 preprint）\n- DOI/arXiv：✓ 2110.14168\n- 论文存在：✓\n- 引用上下文：✓ — 作为 \"trained verifiers\" 引用，准确\n- **结论：✅ OK**\n\n### 6. [derczynski2017wnut] Derczynski et al. (2017). \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\". W-NUT 2017.\n- 在线验证：ACL Anthology ✓ (W17-4418)\n- 作者：✓ Derczynski, Nichols, van Erp, Limsopatham\n- 年份：✓ 2017\n- 标题：✓\n- Venue：✓ W-NUT 2017\n- DOI/arXiv：N/A\n- 论文存在：✓\n- 引用上下文：✓ — WNUT-17 数据集来源引用\n- **结论：✅ OK**\n\n### 7. [ding2021fewnerd] Ding et al. (2021). \"Few-NERD: A Few-shot Named Entity Recognition Dataset\". ACL 2021, pp 3198–3213.\n- 在线验证：ACL Anthology ✓ (2021.acl-long.248)\n- 作者：✓ 全部 8 位作者正确\n- 年份：✓ 2021\n- 标题：✓\n- Venue：✓ ACL 2021 Long Papers\n- 卷期页码：✓ pp 3198–3213\n- DOI：✓ 10.18653/v1/2021.acl-long.248\n- 论文存在：✓\n- 引用上下文：✓ — Few-NERD 数据集来源引用\n- **结论：✅ OK**\n\n### 8. [eikema2022sampling] Eikema, Aziz (2022). \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\". EMNLP 2022, pp 10978–10993.\n- 在线验证：ACL Anthology ✓ (2022.emnlp-main.754)\n- 作者：✓\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ EMNLP 2022\n- 卷期页码：✓ pp 10978–10993\n- DOI：✓ 10.18653/v1/2022.emnlp-main.754\n- 论文存在：✓\n- 引用上下文：✓ — MBR decoding 标准引用\n- **结论：✅ OK**\n\n### 9. [freitag2022high] Freitag et al. (2022). \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\". TACL 10, pp 811–825.\n- 在线验证：ACL Anthology ✓ (2022.tacl-1.47)\n- 作者：✓ Freitag, Grangier, Tan, Liang\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ TACL, volume 10\n- 卷期页码：✓ pp 811–825\n- DOI：✓ 10.1162/tacl_a_00491\n- 论文存在：✓\n- 引用上下文：✓ — \"MBR's success in machine translation\"\n- **结论：✅ OK**\n\n### 10. [fleiss1971agreement] Fleiss (1971). \"Measuring nominal scale agreement among many raters.\" Psychological Bulletin.\n- 在线验证：Google Scholar ✓（经典论文）\n- 作者：✓ Joseph L. Fleiss\n- 年份：✓ 1971\n- 标题：✓\n- Venue：✓ Psychological Bulletin\n- DOI：✓ 10.1037/h0031619\n- 论文存在：✓\n- 引用上下文：✓ — \"inter-rater agreement adapted to entity sets\"\n- **结论：⚠️ 需修正** — 缺少 `volume = {76}` 和 `pages = {378--382}`\n\n### 11. [geng2024confidence] Geng et al. (2024). \"A Survey of Confidence Estimation and Calibration in Large Language Models\". NAACL 2024.\n- 在线验证：ACL Anthology ✓ (2024.naacl-long.366)\n- 作者：✓ 全部 6 位作者正确\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ NAACL 2024 Long Papers\n- DOI：✓ 10.18653/v1/2024.naacl-long.366\n- 论文存在：✓\n- 引用上下文：✓ — confidence estimation 引用\n- **结论：✅ OK**\n\n### 12. [kadavath2022language] Kadavath et al. (2022). \"Language Models (Mostly) Know What They Know\". arXiv:2207.05221.\n- 在线验证：arXiv ✓ | Google Scholar ✓\n- 作者：✓ 全部 34 位作者正确\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ arXiv preprint\n- DOI/arXiv：✓ 2207.05221\n- 论文存在：✓\n- 引用上下文：✓ — \"LP is well-calibrated at population level\"\n- **结论：✅ OK**\n\n### 13. [kang2025selfcertainty] Kang, Zhao, Song (2025). \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\". NeurIPS 2025.\n- 在线验证：arXiv ✓ (2502.18581) | NeurIPS 2025 poster ✓\n- 作者：✓ Kang, Zhao, Song\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✗ — bib 写 \"Advances in Neural Information Processing Systems **38**\"，但 NeurIPS 2025 是第 **39** 届（NeurIPS 2024 = 38th）\n- DOI/arXiv：✓ 2502.18581\n- 论文存在：✓\n- 引用上下文：✓ — \"Reward-free selectors\"\n- **结论：⚠️ 需修正** — volume 号 38 → 39\n\n### 14. [kuhn2023semantic] Kuhn, Gal, Farquhar (2023). \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\". ICLR 2023.\n- 在线验证：arXiv ✓ (2302.09664) | OpenReview ✓\n- 作者：✓\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ ICLR 2023\n- DOI/arXiv：✓ 2302.09664\n- 论文存在：✓\n- 引用上下文：✓ — \"Semantic uncertainty\" 和 \"model-internal alternatives\"\n- **结论：✅ OK**\n\n### 15. [lightman2024verify] Lightman et al. (2024). \"Let's Verify Step by Step\". ICLR 2024.\n- 在线验证：arXiv ✓ (2305.20050) | OpenReview ✓\n- 作者：✓ 全部 10 位作者正确（注：arXiv 用 \"Yura Burda\"/\"Harri Edwards\"，DBLP 用 \"Yuri Burda\"/\"Harrison Edwards\"，两种形式均可接受）\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICLR 2024\n- DOI/arXiv：✓ 2305.20050\n- 论文存在：✓\n- 引用上下文：✓ — \"trained verifiers\"\n- **结论：✅ OK**\n\n### 16. [luan2018scierc] Luan et al. (2018). \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\". EMNLP 2018.\n- 在线验证：ACL Anthology ✓ (D18-1360)\n- 作者：✓ Luan, He, Ostendorf, Hajishirzi\n- 年份：✓ 2018\n- 标题：✓\n- Venue：✓ EMNLP 2018\n- DOI：✓ 10.18653/v1/D18-1360\n- 论文存在：✓\n- 引用上下文：✓ — SciERC 数据集来源引用\n- **结论：✅ OK**\n\n### 17. [yao2026consistency] Yao et al. (2026). \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\". Genomics & Informatics.\n- 在线验证：Google Scholar ✓ | DOI ✓\n- 作者：✓ Yao, Nédellec, Xia, Bossy\n- 年份：✓ 2026\n- 标题：✓\n- Venue：✓ Genomics & Informatics\n- DOI：✓ 10.1186/s44342-025-00063-2\n- 论文存在：✓\n- 引用上下文：✓ — \"Prior work reports task-level correlations between consistency and accuracy\"\n- **结论：✅ OK**\n\n### 18. [sainz2024gollie] Sainz et al. (2024). \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\". ICLR 2024.\n- 在线验证：arXiv ✓ (2310.03668) | OpenReview ✓\n- 作者：✓ Sainz, García-Ferrero, Agerri, Lopez de Lacalle, Rigau, Agirre\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICLR 2024\n- DOI/arXiv：✓ 2310.03668\n- 论文存在：✓\n- 引用上下文：✓ — \"generative IE\"\n- **结论：✅ OK**\n\n### 19. [snell2025scaling] Snell et al. (2025). \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\". ICLR 2025.\n- 在线验证：arXiv ✓ (2408.03314) | OpenReview ✓\n- 作者：✓ Snell, Lee, Xu, Kumar\n- 年份：✓ 2025\n- 标题：✓（bib 标题与 ICLR proceedings 版一致；arXiv 版标题略有不同——\"Scaling Model Parameters\" vs \"Scaling Parameters for Reasoning\"）\n- Venue：✓ ICLR 2025 (Oral)\n- DOI/arXiv：✓ 2408.03314\n- 论文存在：✓\n- 引用上下文：✓ — \"best-of-N with compute-optimal allocation\"\n- **结论：✅ OK**\n\n### 20. [taubenfeld2025cisc] Taubenfeld et al. (2025). \"Confidence Improves Self-Consistency in LLMs\". Findings of ACL 2025.\n- 在线验证：ACL Anthology ✓ | DOI ✓\n- 作者：✓ Taubenfeld, Sheffer, Ofek, Feder, Goldstein, Gekhman, Yona\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ Findings of ACL 2025\n- DOI：✓ 10.18653/v1/2025.findings-acl.1030\n- 论文存在：✓\n- 引用上下文：✓ — \"Reward-free selectors\"\n- **结论：✅ OK**\n\n### 21. [thirukovalluru2024atomic] Thirukovalluru, Huang, Dhingra (2024). \"Atomic Self-Consistency for Better Long Form Generations\". EMNLP 2024.\n- 在线验证：ACL Anthology ✓ (2024.emnlp-main.706)\n- 作者：✓\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ EMNLP 2024 main\n- DOI：✓ 10.18653/v1/2024.emnlp-main.706\n- 论文存在：✓\n- 引用上下文：✓ — \"atomic variants face limits where sub-output agreement does not yield selection gain\"\n- **结论：✅ OK**\n\n### 22. [tjongkimsang2003conll] Tjong Kim Sang, De Meulder (2003). \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\". CoNLL 2003.\n- 在线验证：ACL Anthology ✓ (W03-0419)\n- 作者：✓\n- 年份：✓ 2003\n- 标题：✓\n- Venue：✓ CoNLL 2003\n- DOI/arXiv：N/A\n- 论文存在：✓\n- 引用上下文：✓ — CoNLL-2003 数据集来源引用\n- **结论：✅ OK**\n\n### 23. [wang2023selfconsistency] Wang et al. (2023). \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\". ICLR 2023.\n- 在线验证：arXiv ✓ (2203.11171) | OpenReview ✓\n- 作者：✓ 全部 8 位作者正确\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ ICLR 2023\n- DOI/arXiv：✓ 2203.11171\n- 论文存在：✓\n- 引用上下文：✓ — 核心 self-consistency 引用\n- **结论：✅ OK**\n\n### 24. [willard2023guided] Willard, Louf (2023). \"Efficient Guided Generation for Large Language Models\". arXiv:2307.09702.\n- 在线验证：arXiv ✓ | DBLP ✓\n- 作者：✓ Brandon T. Willard, Rémi Louf\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ arXiv preprint（确认仍为 preprint，无正式 venue）\n- DOI/arXiv：✓ 2307.09702\n- 论文存在：✓\n- 引用上下文：✓ — \"constrained decoding\"\n- **结论：✅ OK**\n\n### 25. [xia2025survey] Xia et al. (2025). \"A Survey of Uncertainty Estimation Methods on Large Language Models\". Findings of ACL 2025.\n- 在线验证：ACL Anthology ✓ (2025.findings-acl.1101)\n- 作者：✓ Xia, Xu, Zhang, Liu\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ Findings of ACL 2025\n- DOI/arXiv：N/A\n- 论文存在：✓\n- 引用上下文：✓ — confidence estimation 引用\n- **结论：✅ OK**\n\n### 26. [zheng2024llamafactory] Zheng et al. (2024). \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\". ACL 2024 System Demos, pp 400–410.\n- 在线验证：ACL Anthology ✓ (2024.acl-demos.38)\n- 作者：✓ Zheng, Zhang, Zhang, Ye, Luo\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ACL 2024 System Demonstrations\n- 卷期页码：✓ pp 400–410\n- DOI：✓ 10.18653/v1/2024.acl-demos.38\n- 论文存在：✓\n- 引用上下文：✓ — 训练框架引用\n- **结论：✅ OK**\n\n### 27. [zhou2024uniner] Zhou et al. (2024). \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\". ICLR 2024.\n- 在线验证：OpenReview ✓ | arXiv ✓ (2308.03279)\n- 作者：✓ Zhou, Zhang, Gu, Chen, Poon\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICLR 2024\n- DOI/arXiv：✓ 2308.03279\n- 论文存在：✓\n- 引用上下文：✓ — \"generative IE\"\n- **结论：✅ OK**\n\n### 28. [muller2021understanding] Müller, Sennrich (2021). \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\". ACL 2021, pp 259–272.\n- 在线验证：ACL Anthology ✓ (2021.acl-long.22)\n- 作者：✓\n- 年份：✓ 2021\n- 标题：✓\n- Venue：✓ ACL 2021 Long Papers\n- 卷期页码：✓ pp 259–272\n- DOI：✓ 10.18653/v1/2021.acl-long.22\n- 论文存在：✓\n- 引用上下文：✓ — MBR decoding\n- **结论：✅ OK**\n\n### 29. [eikema2025structured] Eikema, Rutkiewicz, Giulianelli (2025). \"Structure-Conditional Minimum Bayes Risk Decoding\". EMNLP 2025.\n- 在线验证：ACL Anthology ✓ (2025.emnlp-main.1616) | arXiv ✓ (2510.20700)\n- 作者：✓\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ EMNLP 2025\n- DOI/arXiv：✓ 2510.20700\n- 论文存在：✓\n- 引用上下文：✓ — \"MBR utilities degrade on structured outputs\"\n- **结论：✅ OK**\n\n### 30. [jinnai2024mbr] Jinnai et al. (2024). \"Model-Based Minimum Bayes Risk Decoding for Text Generation\". ICML 2024.\n- 在线验证：PMLR ✓ (v235, pp 22326–22347) | arXiv ✓ (2311.05263)\n- 作者：✓ Jinnai, Morimura, Honda, Ariu, Abe\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICML 2024\n- DOI/arXiv：✓ 2311.05263\n- 论文存在：✓\n- 引用上下文：✓ — \"extension to summarization, code generation, and captioning\"\n- **结论：✅ OK**\n\n### 31. [ratinov2009design] Ratinov, Roth (2009). \"Design Challenges and Misconceptions in Named Entity Recognition\". CoNLL 2009, pp 147–155.\n- 在线验证：ACL Anthology ✓ (W09-1119)\n- 作者：✓\n- 年份：✓ 2009\n- 标题：✓\n- Venue：✓ CoNLL 2009\n- 卷期页码：✓ pp 147–155\n- 论文存在：✓\n- 引用上下文：✓ — \"threshold below which NER differences are considered negligible\"\n- **结论：✅ OK**\n\n### 32. [bergkirkpatrick2012empirical] Berg-Kirkpatrick, Burkett, Klein (2012). \"An Empirical Investigation of Statistical Significance in NLP\". EMNLP-CoNLL 2012, pp 995–1005.\n- 在线验证：ACL Anthology ✓ (D12-1091)\n- 作者：✓\n- 年份：✓ 2012\n- 标题：✓\n- Venue：✓ EMNLP-CoNLL 2012\n- 卷期页码：✓ pp 995–1005\n- 论文存在：✓\n- 引用上下文：✓ — \"significant-difference threshold established in NER evaluation methodology\"（论文研究 NLP 整体的统计显著性，含 NER，引用可接受）\n- **结论：✅ OK**\n\n### 33. [tian2023calibration] Tian et al. (2023). \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\". EMNLP 2023, pp 5433–5442.\n- 在线验证：ACL Anthology ✓ (2023.emnlp-main.330)\n- 作者：✓ 全部 8 位作者正确\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ EMNLP 2023\n- 卷期页码：✓ pp 5433–5442\n- 论文存在：✓\n- 引用上下文：✓ — \"LP is well-calibrated at population level\" 和 verbalized confidence\n- **结论：✅ OK**\n\n### 34. [yun2025price] Yun et al. (2025). \"The Price of Format: Diversity Collapse in LLMs\". Findings of EMNLP 2025.\n- 在线验证：ACL Anthology ✓ (2025.findings-emnlp.836)\n- 作者：✓ Yun, An, Wang, Peng, Shang\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ Findings of EMNLP 2025\n- 论文存在：✓\n- 引用上下文：✓ — \"diversity collapse under constrained decoding\"\n- **结论：✅ OK**\n\n### 35. [gao2023scaling] Gao, Schulman, Hilton (2023). \"Scaling Laws for Reward Model Overoptimization\". ICML 2023.\n- 在线验证：PMLR ✓ (v202, pp 10835–10866)\n- 作者：✓\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ ICML 2023\n- 论文存在：✓\n- 引用上下文：✓ — \"BoN scaling laws\"\n- **结论：✅ OK**\n\n### 36. [platt1999probabilistic] Platt (1999). \"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\". Advances in Large Margin Classifiers, pp 61–74. MIT Press.\n- 在线验证：Google Scholar ✓（经典论文）\n- 作者：✓ John C. Platt\n- 年份：✓ 1999\n- 标题：✓\n- Venue：✓ Advances in Large Margin Classifiers, MIT Press\n- 卷期页码：✓ pp 61–74\n- 论文存在：✓\n- 引用上下文：✓ — \"Platt scaling fits a logistic regression\"\n- **结论：✅ OK**\n\n### 37. [guo2017calibration] Guo et al. (2017). \"On Calibration of Modern Neural Networks\". ICML 2017, pp 1321–1330.\n- 在线验证：PMLR ✓ (v70)\n- 作者：✓ Guo, Pleiss, Sun, Weinberger\n- 年份：✓ 2017\n- 标题：✓\n- Venue：✓ ICML 2017\n- 卷期页码：✓ pp 1321–1330\n- 论文存在：✓\n- 引用上下文：✓ — \"temperature scaling divides logits by a scalar\"\n- **结论：✅ OK**\n\n### 38. [geifman2017selective] Geifman, El-Yaniv (2017). \"Selective Classification for Deep Neural Networks\". NeurIPS 30.\n- 在线验证：NeurIPS proceedings ✓ | arXiv ✓ (1705.08500)\n- 作者：✓\n- 年份：✓ 2017\n- 标题：✓\n- Venue：⚠️ — bib 写 \"Advances in Neural Information Processing Systems\" volume 30，但 2017 年会议名称仍为 **NIPS**（2018 年才改名 NeurIPS）。\"NeurIPS 30\" 不准确，应为 \"NIPS 2017\" 或 \"Advances in Neural Information Processing Systems 30\"\n- DOI/arXiv：✓ 1705.08500\n- 论文存在：✓\n- 引用上下文：✓ — \"selective prediction\" 和 \"support abstention\"\n- **结论：⚠️ 建议修正** — venue 名称时间错误（NIPS vs NeurIPS）。实际影响较小，因 booktitle 用的是通用的 \"Advances in Neural Information Processing Systems\"。\n\n### 39. [dong2024xgrammar] Dong et al. (2024). \"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\". arXiv:2411.15100.\n- 在线验证：arXiv ✓ | MLSys 2025 ✓\n- 作者：✓ Dong, Ruan, Cai, Lai, Xu, Zhao, Chen\n- 年份：✓/⚠️ — arXiv preprint 2024，但已在 **MLSys 2025** 正式发表\n- 标题：✓\n- Venue：⚠️ — bib 仅列 arXiv preprint，但论文已被 MLSys 2025 接收并发表\n- DOI/arXiv：✓ 2411.15100\n- 论文存在：✓\n- 引用上下文：✓ — constrained decoding engine\n- **结论：⚠️ 建议修正** — 应更新为 MLSys 2025 venue\n\n### 40. [lin2022teaching] Lin, Hilton, Evans (2022). \"Teaching Models to Express Their Uncertainty in Words\". TMLR.\n- 在线验证：arXiv ✓ (2205.14334) | TMLR ✓\n- 作者：✓\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ Transactions on Machine Learning Research (TMLR)\n- DOI/arXiv：✓ 2205.14334\n- 论文存在：✓\n- 引用上下文：✓ — verbalized confidence baseline\n- **结论：✅ OK**\n\n### 41. [farquhar2024detecting] Farquhar et al. (2024). \"Detecting hallucinations in large language models using semantic entropy\". Nature 630, pp 625–630.\n- 在线验证：Nature ✓ | Google Scholar ✓\n- 作者：✓ Farquhar, Kossen, Kuhn, Gal\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ Nature, volume 630\n- 卷期页码：✓ pp 625–630\n- DOI：✓ 10.1038/s41586-024-07421-0\n- 论文存在：✓\n- 引用上下文：✓ — novelty comparison table\n- **结论：✅ OK**\n\n### 42. [chen2023twofailures] Chen et al. (2024). \"Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs\". TMLR.\n- 在线验证：arXiv ✓ (2305.14279) | TMLR ✓\n- 作者：✓ Chen, Phang, Parrish, Padmakumar, Zhao, Bowman, Cho\n- 年份：✓ year=2024 正确（TMLR 发表年）；cite key 用 2023 反映 preprint 年，可接受\n- 标题：✓\n- Venue：✓ TMLR\n- DOI/arXiv：✓ 2305.14279\n- 论文存在：✓\n- 引用上下文：✓ — \"SC can fail when consistent outputs are wrong\"\n- **结论：✅ OK**（key-year 轻微不一致但可接受）\n\n### 43. [aggarwal2023adaptive] Aggarwal et al. (2023). \"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs\". EMNLP 2023.\n- 在线验证：arXiv ✓ (2305.11860) | EMNLP 2023 ✓\n- 作者：✓ Aggarwal, Madaan, Yang, Mausam\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ EMNLP 2023\n- DOI/arXiv：✓ 2305.11860\n- 论文存在：✓\n- 引用上下文：✓ — novelty comparison table\n- **结论：✅ OK**\n\n### 44. [xie2023zeroshot] Xie et al. (2023). \"Empirical Study of Zero-Shot NER with ChatGPT\". EMNLP 2023, pp 7935–7956.\n- 在线验证：ACL Anthology ✓ (2023.emnlp-main.493)\n- 作者：✓ Xie, Li, Zhang, Zhang, Liu, Wang\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ EMNLP 2023\n- 卷期页码：✓ pp 7935–7956\n- DOI：✓ 10.18653/v1/2023.emnlp-main.493\n- 论文存在：✓\n- 引用上下文：✓ — \"propose entity voting for zero-shot NER\"\n- **结论：✅ OK**\n\n### 45. [muennighoff2025s1] Muennighoff et al. (2025). \"s1: Simple Test-Time Scaling\". EMNLP 2025.\n- 在线验证：arXiv ✓ (2501.19393) | ACL Anthology ✓ (2025.emnlp-main.1025)\n- 作者：✓ 全部 10 位作者正确\n- 年份：✓ 2025\n- 标题：✓（注：原作者用全小写 \"s1: Simple test-time scaling\"，bib 用 title case，BibTeX style 会自动处理）\n- Venue：✓ EMNLP 2025\n- DOI/arXiv：✓ 2501.19393\n- 论文存在：✓\n- 引用上下文：✓ — \"extended reasoning\"\n- **结论：✅ OK**\n\n### 46. [eikema2020map] Eikema, Aziz (2020). \"Is MAP Decoding All You Need? The Inadequacy of the Mode in Neural Machine Translation\". COLING 2020, pp 4506–4520.\n- 在线验证：ACL Anthology ✓ (2020.coling-main.398)\n- 作者：✓\n- 年份：✓ 2020\n- 标题：✓\n- Venue：✓ COLING 2020\n- 卷期页码：✓ pp 4506–4520\n- 论文存在：✓\n- 引用上下文：✓ — MBR decoding foundational reference\n- **结论：✅ OK**\n\n### 47. [kumar2004minimum] Kumar, Byrne (2004). \"Minimum Bayes-Risk Decoding for Statistical Machine Translation\". HLT-NAACL 2004, pp 169–176.\n- 在线验证：ACL Anthology ✓ (N04-1022)\n- 作者：✓\n- 年份：✓ 2004\n- 标题：✓\n- Venue：✓ HLT-NAACL 2004\n- 卷期页码：✓ pp 169–176\n- 论文存在：✓\n- 引用上下文：✓ — MBR decoding foundational reference\n- **结论：✅ OK**\n\n### 48. [dembczynski2011exact] Dembczyński et al. (2011). \"An Exact Algorithm for F-Measure Maximization\". NeurIPS 24, pp 1404–1412.\n- 在线验证：NeurIPS proceedings ✓\n- 作者：✓ Dembczyński, Waegeman, Cheng, Hüllermeier\n- 年份：✓ 2011\n- 标题：✓\n- Venue：✓ NeurIPS (NIPS) 2011, vol 24\n- 卷期页码：✓ pp 1404–1412\n- 论文存在：✓\n- 引用上下文：✓ — \"Set-level F1 admits no closed-form threshold\"\n- **结论：✅ OK**\n\n### 49. [desai2020calibration] Desai, Durrett (2020). \"Calibration of Pre-trained Transformers\". EMNLP 2020, pp 295–302.\n- 在线验证：ACL Anthology ✓ (2020.emnlp-main.21)\n- 作者：✓\n- 年份：✓ 2020\n- 标题：✓\n- Venue：✓ EMNLP 2020\n- 卷期页码：✓ pp 295–302\n- 论文存在：✓\n- 引用上下文：✓ — \"calibrated LMs\"\n- **结论：✅ OK**\n\n### 50. [huang2024large] Huang et al. (2024). \"Large Language Models Cannot Self-Correct Reasoning Yet\". ICLR 2024.\n- 在线验证：OpenReview ✓ (IkmD3fKBPQ)\n- 作者：✓ Huang, Chen, Mishra, Zheng, Yu, Song, Zhou\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICLR 2024\n- 论文存在：✓\n- 引用上下文：✓ — \"introspection boundary\"（论文论证 LLM 无法 self-correct reasoning，用于支持 models encode quality internally but can't self-judge 的论点）\n- **结论：✅ OK**\n\n### 51. [li2024simple] Li, Ramprasad, Zhang (2024). \"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction\". Findings of EMNLP 2024.\n- 在线验证：ACL Anthology ✓ | arXiv ✓ (2402.13364)\n- 作者：✓\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ Findings of EMNLP 2024\n- DOI/arXiv：✓ 2402.13364\n- 论文存在：✓\n- 引用上下文：N/A — **未在任何 tex 文件中被引用**\n- **结论：⚠️ 未使用，建议移除或确认是否需要**\n\n### 52. [xie2024selfimproving] Xie et al. (2024). \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\". NAACL 2024.\n- 在线验证：ACL Anthology ✓ (2024.naacl-short.49)\n- 作者：✓ Xie, Li, Zhang, Liu, Wang\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ NAACL 2024 (Short Papers, pp 583–593)\n- 论文存在：✓\n- 引用上下文：✓ — \"extend this with SC-based self-annotation\"\n- **结论：✅ OK**\n\n### 53. [madaan2023selfrefine] Madaan et al. (2023). \"Self-Refine: Iterative Refinement with Self-Feedback\". NeurIPS 36.\n- 在线验证：NeurIPS proceedings ✓\n- 作者：✓ 全部 16 位作者正确\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ NeurIPS 2023 (volume 36)\n- 论文存在：✓\n- 引用上下文：✓ — \"iterative self-refinement\"\n- **结论：✅ OK**\n\n### 54. [angelopoulos2023conformal] Angelopoulos, Bates (2023). \"Conformal Prediction: A Gentle Introduction\". Foundations and Trends in ML, 16(4), pp 494–591.\n- 在线验证：ACM DL ✓ | Google Scholar ✓\n- 作者：✓\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ Foundations and Trends in Machine Learning\n- 卷期页码：✓ Vol 16, No 4, pp 494–591\n- 论文存在：✓\n- 引用上下文：✓ — \"conformal prediction\"\n- **结论：✅ OK**\n\n### 55. [malinin2021uncertainty] Malinin, Gales (2021). \"Uncertainty Estimation in Autoregressive Structured Prediction\". ICLR 2021.\n- 在线验证：OpenReview ✓\n- 作者：✓ Andrey Malinin, Mark Gales\n- 年份：✓ 2021\n- 标题：✓\n- Venue：✓ ICLR 2021\n- 论文存在：✓\n- 引用上下文：✓ — \"uncertainty for structured prediction\"\n- **结论：✅ OK**\n\n### 56. [yee2019noisy] Yee, Dauphin, Auli (2019). \"Simple and Effective Noisy Channel Modeling for Neural Machine Translation\". EMNLP-IJCNLP 2019.\n- 在线验证：ACL Anthology ✓ (D19-1571) | arXiv ✓ (1908.05731)\n- 作者：✗ — bib 列 3 位作者（Yee, Dauphin, Auli），但 ACL Anthology 和 arXiv 均列 **4 位作者**：Kyra Yee, **Nathan Ng**, Yann N. Dauphin, Michael Auli。**缺少 Nathan Ng**。\n- 年份：✓ 2019\n- 标题：✓\n- Venue：✓ EMNLP-IJCNLP 2019\n- DOI/arXiv：✓ 1908.05731\n- 论文存在：✓\n- 引用上下文：✓ — \"noisy channel models\"\n- **结论：⚠️ 需修正** — 缺少作者 Nathan Ng\n\n### 57. [li2023stepaware] Li et al. (2023). \"Making Large Language Models Better Reasoners with Step-Aware Verifier\". ACL 2023.\n- 在线验证：ACL Anthology ✓ (2023.acl-long.291) | arXiv ✓ (2206.02336)\n- 作者：✓ Li, Lin, Zhang, Fu, Chen, Lou, Chen\n- 年份：✓ 2023\n- 标题：✗ — bib 写 \"Making **Large** Language Models Better Reasoners with Step-Aware Verifier\"，但 ACL 2023 正式发表标题为 \"Making Language Models Better Reasoners with Step-Aware Verifier\"（**无 \"Large\"**）。arXiv 版本标题含 \"Large\"，但应以正式发表版为准。\n- Venue：✓ ACL 2023\n- DOI/arXiv：✓ 2206.02336\n- 论文存在：✓\n- 引用上下文：✓ — \"trained verifiers\"\n- **结论：⚠️ 需修正** — 标题应删除 \"Large\"，与 ACL 2023 正式发表版一致\n\n### 58. [xiao2022uncertainty] Xiao et al. (2022). \"Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis\". Findings of EMNLP 2022.\n- 在线验证：ACL Anthology ✓ (2022.findings-emnlp.538)\n- 作者：✓ Xiao, Liang, Bhatt, Neiswanger, Salakhutdinov, Morency\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ Findings of EMNLP 2022\n- 论文存在：✓\n- 引用上下文：N/A — **未在任何 tex 文件中被引用**\n- **结论：⚠️ 未使用，建议移除或确认是否需要**\n\n### 59. [li2026rewardtail] Li, Qian, Mou (2026). \"Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search\". arXiv:2602.01485.\n- 在线验证：arXiv ✓\n- 作者：✓\n- 年份：✓ 2026\n- 标题：✓\n- Venue：✓ arXiv preprint\n- DOI/arXiv：✓ 2602.01485\n- 论文存在：✓\n- 引用上下文：✓ — \"reward-tail-guided search\"\n- **结论：✅ OK**\n\n### 60. [shinn2023reflexion] Shinn et al. (2023). \"Reflexion: Language Agents with Verbal Reinforcement Learning\". NeurIPS 36.\n- 在线验证：NeurIPS proceedings ✓ | arXiv ✓ (2303.11366)\n- 作者：✗ — bib 列 5 位作者（Shinn, Cassano, Gopinath, Narasimhan, Yao），但 NeurIPS 2023 正式 proceedings 列 **6 位作者**：Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao。**缺少 Edward Berman**。\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ NeurIPS 2023 (volume 36)\n- 论文存在：✓\n- 引用上下文：✓ — \"Iterative self-verification\"\n- **结论：⚠️ 需修正** — 缺少作者 Edward Berman\n\n### 61. [xu2024llmie] Xu et al. (2024). \"Large Language Models for Generative Information Extraction: A Survey\". Frontiers of Computer Science, 18(6):186357.\n- 在线验证：Springer ✓ | Google Scholar ✓\n- 作者：✓ 全部 10 位作者正确\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ Frontiers of Computer Science\n- 卷期页码：✓ Vol 18, No 6, 186357\n- DOI：✓ 10.1007/s11704-024-40555-y\n- 论文存在：✓\n- 引用上下文：✓ — \"LLM-based IE has expanded rapidly\"\n- **结论：✅ OK**\n\n### 62. [wang2025gptner] Wang et al. (2025). \"GPT-NER: Named Entity Recognition via Large Language Models\". Findings of NAACL 2025.\n- 在线验证：ACL Anthology ✓ (2025.findings-naacl.239)\n- 作者：✓ Wang, Sun, Li, Ouyang, Wu, Zhang, Li, Wang（8 位，与 ACL Anthology 一致）\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ Findings of NAACL 2025\n- 论文存在：✓\n- 引用上下文：✓ — \"Self-verification approaches that prompt LLMs to validate their own extractions improve NER\"\n- **结论：✅ OK**\n\n### 63. [gero2023selfverification] Gero et al. (2023). \"Self-Verification Improves Few-Shot Clinical Information Extraction\". arXiv:2306.00024.\n- 在线验证：arXiv ✓\n- 作者：✓ Gero, Singh, Cheng, Naumann, Galley, Gao, Poon\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ arXiv preprint（确认仍为 preprint，无正式 venue）\n- DOI/arXiv：✓ 2306.00024\n- 论文存在：✓\n- 引用上下文：✓ — \"clinical IE\"\n- **结论：✅ OK**\n\n### 64. [wadhwa2023revisiting] Wadhwa, Amir, Wallace (2023). \"Revisiting Relation Extraction in the era of Large Language Models\". ACL 2023, pp 15566–15589.\n- 在线验证：ACL Anthology ✓ (2023.acl-long.868)\n- 作者：✓\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ ACL 2023 Long Papers\n- 卷期页码：✓ pp 15566–15589\n- 论文存在：✓\n- 引用上下文：✓ — \"benchmark LLM-based RE, confirming that structured outputs pose challenges distinct from free-form generation\"\n- **结论：✅ OK**\n\n---\n\n## 统计\n\n| 类别 | 数量 |\n|------|------|\n| ✅ OK | 54 |\n| ⚠️ 需修正 | 4 (kang2025selfcertainty, yee2019noisy, shinn2023reflexion, li2023stepaware) |\n| ⚠️ 建议修正 | 3 (dong2024xgrammar, fleiss1971agreement, geifman2017selective) |\n| 🧹 未使用 | 3 (holm1979simple, li2024simple, xiao2022uncertainty) |\n| ❌ 论文不存在 / hallucinated | **0** |\n\n**所有 64 篇论文均为真实存在的论文，无 hallucinated citations。**\n\n---\n\n## 建议修复清单（按优先级排序）\n\n### 必须修复\n1. **`kang2025selfcertainty`**: booktitle 中 \"38\" → \"39\"\n2. **`yee2019noisy`**: 添加缺失作者 `Nathan Ng`（第二作者位置）\n3. **`shinn2023reflexion`**: 添加缺失作者 `Edward Berman`（Cassano 和 Gopinath 之间）\n4. **`li2023stepaware`**: title 中删除 \"Large\"（\"Making Language Models Better Reasoners...\"）\n\n### 建议修复\n5. **`dong2024xgrammar`**: 更新为 MLSys 2025 正式 venue\n6. **`fleiss1971agreement`**: 添加 `volume = {76}`, `pages = {378--382}`\n7. **`geifman2017selective`**: venue 无需改动（booktitle 已使用通用 \"Advances in Neural Information Processing Systems\"）\n\n### 清理\n8. 移除 3 个未引用 entry：`holm1979simple`, `li2024simple`, `xiao2022uncertainty`\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "27803580-603d-47d2-85c6-1cf43fca1816",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ucyBUobRBwNJbf4eP3TNy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4436,
      "cache_read_input_tokens": 73848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4436
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

_source line 399 · 2026-05-26T10:30:41.841Z_

<details><summary>↩ Tool result · `toolu_01TJc5REpeAnCkbowzBqjS4W`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ref_audit_worker_B.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "2af65d14-492b-4c23-a513-2baf14790749",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ref_audit_worker_B.md",
    "content": "# 引用验证清单 (Worker B — Google Scholar / DBLP 优先)\n\n**验证日期**: 2026-05-26\n**验证方式**: WebSearch (Google Scholar, DBLP, ACL Anthology, arXiv, NeurIPS/ICML proceedings)\n\n总 bib entries: **64**\n总 cite keys in tex: **61**\n未使用的 bib entries: `holm1979simple`, `li2024simple`, `xiao2022uncertainty`\ntex 中引用但 bib 缺失: **无**\n\n---\n\n## 问题汇总\n\n| 严重性 | 条目 | 问题 |\n|--------|------|------|\n| ⚠️ 需修正 | `kang2025selfcertainty` | NeurIPS volume 号错：写了 38，应为 39（NeurIPS 2025 = 第 39 届） |\n| ⚠️ 需修正 | `yee2019noisy` | 缺少作者 Nathan Ng（应为 4 人，非 3 人） |\n| ⚠️ 需修正 | `shinn2023reflexion` | 缺少作者 Edward Berman（应为 6 人，非 5 人） |\n| ⚠️ 需修正 | `li2023stepaware` | 标题不一致：bib 写 \"Making **Large** Language Models...\"，ACL 2023 正式版为 \"Making Language Models...\"（无 \"Large\"） |\n| ⚠️ 建议修正 | `dong2024xgrammar` | 已在 MLSys 2025 正式发表，bib 仅列 arXiv preprint，建议更新 venue |\n| ⚠️ 建议修正 | `fleiss1971agreement` | 缺少 volume (76) 和 pages (378–382) |\n| ⚠️ 建议修正 | `geifman2017selective` | \"NeurIPS 30\" 时间上不准确，2017 年会议名称仍为 NIPS（2018 年才改名 NeurIPS） |\n| 🧹 清理 | `holm1979simple` | 未被引用，可移除 |\n| 🧹 清理 | `li2024simple` | 未被引用，可移除 |\n| 🧹 清理 | `xiao2022uncertainty` | 未被引用，可移除 |\n\n---\n\n## 逐条验证\n\n### 1. [landesberg2026bon] Landesberg (2026). \"When LLM Judge Scores Look Good but Best-of-N Decisions Fail\". arXiv:2603.12520.\n- 在线验证：arXiv ✓ 找到\n- 作者：✓\n- 年份：✓ 2026\n- 标题：✓\n- Venue：✓ arXiv preprint\n- DOI/arXiv：✓ 2603.12520\n- 论文存在：✓\n- 引用上下文：✓ — \"\\citet{landesberg2026bon} independently document a correlation-selection gap in best-of-N reasoning: global judge r=0.47 masks within-prompt r=0.27\" 准确描述了论文内容\n- **结论：✅ OK**\n\n### 2. [holm1979simple] Holm (1979). \"A Simple Sequentially Rejective Multiple Test Procedure\". Scandinavian J. Statistics 6(2), 65–70.\n- 在线验证：Google Scholar ✓ 找到（经典论文，5万+引用）\n- 作者：✓ Sture Holm\n- 年份：✓ 1979\n- 标题：✓\n- Venue：✓ Scandinavian Journal of Statistics, Vol 6, No 2, pp 65–70\n- DOI/arXiv：N/A（1979年无DOI）\n- 论文存在：✓\n- 引用上下文：N/A — **未在任何 tex 文件中被引用**\n- **结论：⚠️ 未使用，建议移除或确认是否需要**\n\n### 3. [brown2024monkeys] Brown et al. (2024). \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\". arXiv:2407.21787.\n- 在线验证：arXiv ✓ | Google Scholar ✓\n- 作者：✓ Brown, Juravsky, Ehrlich, Clark, Le, Ré, Mirhoseini\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ arXiv preprint（确认仍为 preprint，未正式发表于会议）\n- DOI/arXiv：✓ 2407.21787\n- 论文存在：✓\n- 引用上下文：✓ — 用于引用推理任务中 inference compute scaling、oracle F1 scaling 对比\n- **结论：✅ OK**\n\n### 4. [chen2024usc] Chen et al. (2024). \"Universal Self-Consistency for Large Language Model Generation\". ICML 2024 Workshop on In-Context Learning. arXiv:2311.17311.\n- 在线验证：arXiv ✓ | ICML 2024 workshop ✓\n- 作者：✓ 全部 10 位作者正确\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICML 2024 Workshop on In-Context Learning\n- DOI/arXiv：✓ 2311.17311\n- 论文存在：✓\n- 引用上下文：✓ — \"free-form variants face limits where sub-output agreement does not yield selection gain\"\n- **结论：✅ OK**\n\n### 5. [cobbe2021verifiers] Cobbe et al. (2021). \"Training Verifiers to Solve Math Word Problems\". arXiv:2110.14168.\n- 在线验证：arXiv ✓ | Google Scholar ✓\n- 作者：✓ 全部 12 位作者正确\n- 年份：✓ 2021\n- 标题：✓\n- Venue：✓ arXiv preprint（确认仍为 preprint）\n- DOI/arXiv：✓ 2110.14168\n- 论文存在：✓\n- 引用上下文：✓ — 作为 \"trained verifiers\" 引用，准确\n- **结论：✅ OK**\n\n### 6. [derczynski2017wnut] Derczynski et al. (2017). \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\". W-NUT 2017.\n- 在线验证：ACL Anthology ✓ (W17-4418)\n- 作者：✓ Derczynski, Nichols, van Erp, Limsopatham\n- 年份：✓ 2017\n- 标题：✓\n- Venue：✓ W-NUT 2017\n- DOI/arXiv：N/A\n- 论文存在：✓\n- 引用上下文：✓ — WNUT-17 数据集来源引用\n- **结论：✅ OK**\n\n### 7. [ding2021fewnerd] Ding et al. (2021). \"Few-NERD: A Few-shot Named Entity Recognition Dataset\". ACL 2021, pp 3198–3213.\n- 在线验证：ACL Anthology ✓ (2021.acl-long.248)\n- 作者：✓ 全部 8 位作者正确\n- 年份：✓ 2021\n- 标题：✓\n- Venue：✓ ACL 2021 Long Papers\n- 卷期页码：✓ pp 3198–3213\n- DOI：✓ 10.18653/v1/2021.acl-long.248\n- 论文存在：✓\n- 引用上下文：✓ — Few-NERD 数据集来源引用\n- **结论：✅ OK**\n\n### 8. [eikema2022sampling] Eikema, Aziz (2022). \"Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation\". EMNLP 2022, pp 10978–10993.\n- 在线验证：ACL Anthology ✓ (2022.emnlp-main.754)\n- 作者：✓\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ EMNLP 2022\n- 卷期页码：✓ pp 10978–10993\n- DOI：✓ 10.18653/v1/2022.emnlp-main.754\n- 论文存在：✓\n- 引用上下文：✓ — MBR decoding 标准引用\n- **结论：✅ OK**\n\n### 9. [freitag2022high] Freitag et al. (2022). \"High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics\". TACL 10, pp 811–825.\n- 在线验证：ACL Anthology ✓ (2022.tacl-1.47)\n- 作者：✓ Freitag, Grangier, Tan, Liang\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ TACL, volume 10\n- 卷期页码：✓ pp 811–825\n- DOI：✓ 10.1162/tacl_a_00491\n- 论文存在：✓\n- 引用上下文：✓ — \"MBR's success in machine translation\"\n- **结论：✅ OK**\n\n### 10. [fleiss1971agreement] Fleiss (1971). \"Measuring nominal scale agreement among many raters.\" Psychological Bulletin.\n- 在线验证：Google Scholar ✓（经典论文）\n- 作者：✓ Joseph L. Fleiss\n- 年份：✓ 1971\n- 标题：✓\n- Venue：✓ Psychological Bulletin\n- DOI：✓ 10.1037/h0031619\n- 论文存在：✓\n- 引用上下文：✓ — \"inter-rater agreement adapted to entity sets\"\n- **结论：⚠️ 需修正** — 缺少 `volume = {76}` 和 `pages = {378--382}`\n\n### 11. [geng2024confidence] Geng et al. (2024). \"A Survey of Confidence Estimation and Calibration in Large Language Models\". NAACL 2024.\n- 在线验证：ACL Anthology ✓ (2024.naacl-long.366)\n- 作者：✓ 全部 6 位作者正确\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ NAACL 2024 Long Papers\n- DOI：✓ 10.18653/v1/2024.naacl-long.366\n- 论文存在：✓\n- 引用上下文：✓ — confidence estimation 引用\n- **结论：✅ OK**\n\n### 12. [kadavath2022language] Kadavath et al. (2022). \"Language Models (Mostly) Know What They Know\". arXiv:2207.05221.\n- 在线验证：arXiv ✓ | Google Scholar ✓\n- 作者：✓ 全部 34 位作者正确\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ arXiv preprint\n- DOI/arXiv：✓ 2207.05221\n- 论文存在：✓\n- 引用上下文：✓ — \"LP is well-calibrated at population level\"\n- **结论：✅ OK**\n\n### 13. [kang2025selfcertainty] Kang, Zhao, Song (2025). \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\". NeurIPS 2025.\n- 在线验证：arXiv ✓ (2502.18581) | NeurIPS 2025 poster ✓\n- 作者：✓ Kang, Zhao, Song\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✗ — bib 写 \"Advances in Neural Information Processing Systems **38**\"，但 NeurIPS 2025 是第 **39** 届（NeurIPS 2024 = 38th）\n- DOI/arXiv：✓ 2502.18581\n- 论文存在：✓\n- 引用上下文：✓ — \"Reward-free selectors\"\n- **结论：⚠️ 需修正** — volume 号 38 → 39\n\n### 14. [kuhn2023semantic] Kuhn, Gal, Farquhar (2023). \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\". ICLR 2023.\n- 在线验证：arXiv ✓ (2302.09664) | OpenReview ✓\n- 作者：✓\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ ICLR 2023\n- DOI/arXiv：✓ 2302.09664\n- 论文存在：✓\n- 引用上下文：✓ — \"Semantic uncertainty\" 和 \"model-internal alternatives\"\n- **结论：✅ OK**\n\n### 15. [lightman2024verify] Lightman et al. (2024). \"Let's Verify Step by Step\". ICLR 2024.\n- 在线验证：arXiv ✓ (2305.20050) | OpenReview ✓\n- 作者：✓ 全部 10 位作者正确（注：arXiv 用 \"Yura Burda\"/\"Harri Edwards\"，DBLP 用 \"Yuri Burda\"/\"Harrison Edwards\"，两种形式均可接受）\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICLR 2024\n- DOI/arXiv：✓ 2305.20050\n- 论文存在：✓\n- 引用上下文：✓ — \"trained verifiers\"\n- **结论：✅ OK**\n\n### 16. [luan2018scierc] Luan et al. (2018). \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\". EMNLP 2018.\n- 在线验证：ACL Anthology ✓ (D18-1360)\n- 作者：✓ Luan, He, Ostendorf, Hajishirzi\n- 年份：✓ 2018\n- 标题：✓\n- Venue：✓ EMNLP 2018\n- DOI：✓ 10.18653/v1/D18-1360\n- 论文存在：✓\n- 引用上下文：✓ — SciERC 数据集来源引用\n- **结论：✅ OK**\n\n### 17. [yao2026consistency] Yao et al. (2026). \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\". Genomics & Informatics.\n- 在线验证：Google Scholar ✓ | DOI ✓\n- 作者：✓ Yao, Nédellec, Xia, Bossy\n- 年份：✓ 2026\n- 标题：✓\n- Venue：✓ Genomics & Informatics\n- DOI：✓ 10.1186/s44342-025-00063-2\n- 论文存在：✓\n- 引用上下文：✓ — \"Prior work reports task-level correlations between consistency and accuracy\"\n- **结论：✅ OK**\n\n### 18. [sainz2024gollie] Sainz et al. (2024). \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\". ICLR 2024.\n- 在线验证：arXiv ✓ (2310.03668) | OpenReview ✓\n- 作者：✓ Sainz, García-Ferrero, Agerri, Lopez de Lacalle, Rigau, Agirre\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICLR 2024\n- DOI/arXiv：✓ 2310.03668\n- 论文存在：✓\n- 引用上下文：✓ — \"generative IE\"\n- **结论：✅ OK**\n\n### 19. [snell2025scaling] Snell et al. (2025). \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning\". ICLR 2025.\n- 在线验证：arXiv ✓ (2408.03314) | OpenReview ✓\n- 作者：✓ Snell, Lee, Xu, Kumar\n- 年份：✓ 2025\n- 标题：✓（bib 标题与 ICLR proceedings 版一致；arXiv 版标题略有不同——\"Scaling Model Parameters\" vs \"Scaling Parameters for Reasoning\"）\n- Venue：✓ ICLR 2025 (Oral)\n- DOI/arXiv：✓ 2408.03314\n- 论文存在：✓\n- 引用上下文：✓ — \"best-of-N with compute-optimal allocation\"\n- **结论：✅ OK**\n\n### 20. [taubenfeld2025cisc] Taubenfeld et al. (2025). \"Confidence Improves Self-Consistency in LLMs\". Findings of ACL 2025.\n- 在线验证：ACL Anthology ✓ | DOI ✓\n- 作者：✓ Taubenfeld, Sheffer, Ofek, Feder, Goldstein, Gekhman, Yona\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ Findings of ACL 2025\n- DOI：✓ 10.18653/v1/2025.findings-acl.1030\n- 论文存在：✓\n- 引用上下文：✓ — \"Reward-free selectors\"\n- **结论：✅ OK**\n\n### 21. [thirukovalluru2024atomic] Thirukovalluru, Huang, Dhingra (2024). \"Atomic Self-Consistency for Better Long Form Generations\". EMNLP 2024.\n- 在线验证：ACL Anthology ✓ (2024.emnlp-main.706)\n- 作者：✓\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ EMNLP 2024 main\n- DOI：✓ 10.18653/v1/2024.emnlp-main.706\n- 论文存在：✓\n- 引用上下文：✓ — \"atomic variants face limits where sub-output agreement does not yield selection gain\"\n- **结论：✅ OK**\n\n### 22. [tjongkimsang2003conll] Tjong Kim Sang, De Meulder (2003). \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\". CoNLL 2003.\n- 在线验证：ACL Anthology ✓ (W03-0419)\n- 作者：✓\n- 年份：✓ 2003\n- 标题：✓\n- Venue：✓ CoNLL 2003\n- DOI/arXiv：N/A\n- 论文存在：✓\n- 引用上下文：✓ — CoNLL-2003 数据集来源引用\n- **结论：✅ OK**\n\n### 23. [wang2023selfconsistency] Wang et al. (2023). \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\". ICLR 2023.\n- 在线验证：arXiv ✓ (2203.11171) | OpenReview ✓\n- 作者：✓ 全部 8 位作者正确\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ ICLR 2023\n- DOI/arXiv：✓ 2203.11171\n- 论文存在：✓\n- 引用上下文：✓ — 核心 self-consistency 引用\n- **结论：✅ OK**\n\n### 24. [willard2023guided] Willard, Louf (2023). \"Efficient Guided Generation for Large Language Models\". arXiv:2307.09702.\n- 在线验证：arXiv ✓ | DBLP ✓\n- 作者：✓ Brandon T. Willard, Rémi Louf\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ arXiv preprint（确认仍为 preprint，无正式 venue）\n- DOI/arXiv：✓ 2307.09702\n- 论文存在：✓\n- 引用上下文：✓ — \"constrained decoding\"\n- **结论：✅ OK**\n\n### 25. [xia2025survey] Xia et al. (2025). \"A Survey of Uncertainty Estimation Methods on Large Language Models\". Findings of ACL 2025.\n- 在线验证：ACL Anthology ✓ (2025.findings-acl.1101)\n- 作者：✓ Xia, Xu, Zhang, Liu\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ Findings of ACL 2025\n- DOI/arXiv：N/A\n- 论文存在：✓\n- 引用上下文：✓ — confidence estimation 引用\n- **结论：✅ OK**\n\n### 26. [zheng2024llamafactory] Zheng et al. (2024). \"LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models\". ACL 2024 System Demos, pp 400–410.\n- 在线验证：ACL Anthology ✓ (2024.acl-demos.38)\n- 作者：✓ Zheng, Zhang, Zhang, Ye, Luo\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ACL 2024 System Demonstrations\n- 卷期页码：✓ pp 400–410\n- DOI：✓ 10.18653/v1/2024.acl-demos.38\n- 论文存在：✓\n- 引用上下文：✓ — 训练框架引用\n- **结论：✅ OK**\n\n### 27. [zhou2024uniner] Zhou et al. (2024). \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\". ICLR 2024.\n- 在线验证：OpenReview ✓ | arXiv ✓ (2308.03279)\n- 作者：✓ Zhou, Zhang, Gu, Chen, Poon\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICLR 2024\n- DOI/arXiv：✓ 2308.03279\n- 论文存在：✓\n- 引用上下文：✓ — \"generative IE\"\n- **结论：✅ OK**\n\n### 28. [muller2021understanding] Müller, Sennrich (2021). \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\". ACL 2021, pp 259–272.\n- 在线验证：ACL Anthology ✓ (2021.acl-long.22)\n- 作者：✓\n- 年份：✓ 2021\n- 标题：✓\n- Venue：✓ ACL 2021 Long Papers\n- 卷期页码：✓ pp 259–272\n- DOI：✓ 10.18653/v1/2021.acl-long.22\n- 论文存在：✓\n- 引用上下文：✓ — MBR decoding\n- **结论：✅ OK**\n\n### 29. [eikema2025structured] Eikema, Rutkiewicz, Giulianelli (2025). \"Structure-Conditional Minimum Bayes Risk Decoding\". EMNLP 2025.\n- 在线验证：ACL Anthology ✓ (2025.emnlp-main.1616) | arXiv ✓ (2510.20700)\n- 作者：✓\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ EMNLP 2025\n- DOI/arXiv：✓ 2510.20700\n- 论文存在：✓\n- 引用上下文：✓ — \"MBR utilities degrade on structured outputs\"\n- **结论：✅ OK**\n\n### 30. [jinnai2024mbr] Jinnai et al. (2024). \"Model-Based Minimum Bayes Risk Decoding for Text Generation\". ICML 2024.\n- 在线验证：PMLR ✓ (v235, pp 22326–22347) | arXiv ✓ (2311.05263)\n- 作者：✓ Jinnai, Morimura, Honda, Ariu, Abe\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICML 2024\n- DOI/arXiv：✓ 2311.05263\n- 论文存在：✓\n- 引用上下文：✓ — \"extension to summarization, code generation, and captioning\"\n- **结论：✅ OK**\n\n### 31. [ratinov2009design] Ratinov, Roth (2009). \"Design Challenges and Misconceptions in Named Entity Recognition\". CoNLL 2009, pp 147–155.\n- 在线验证：ACL Anthology ✓ (W09-1119)\n- 作者：✓\n- 年份：✓ 2009\n- 标题：✓\n- Venue：✓ CoNLL 2009\n- 卷期页码：✓ pp 147–155\n- 论文存在：✓\n- 引用上下文：✓ — \"threshold below which NER differences are considered negligible\"\n- **结论：✅ OK**\n\n### 32. [bergkirkpatrick2012empirical] Berg-Kirkpatrick, Burkett, Klein (2012). \"An Empirical Investigation of Statistical Significance in NLP\". EMNLP-CoNLL 2012, pp 995–1005.\n- 在线验证：ACL Anthology ✓ (D12-1091)\n- 作者：✓\n- 年份：✓ 2012\n- 标题：✓\n- Venue：✓ EMNLP-CoNLL 2012\n- 卷期页码：✓ pp 995–1005\n- 论文存在：✓\n- 引用上下文：✓ — \"significant-difference threshold established in NER evaluation methodology\"（论文研究 NLP 整体的统计显著性，含 NER，引用可接受）\n- **结论：✅ OK**\n\n### 33. [tian2023calibration] Tian et al. (2023). \"Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback\". EMNLP 2023, pp 5433–5442.\n- 在线验证：ACL Anthology ✓ (2023.emnlp-main.330)\n- 作者：✓ 全部 8 位作者正确\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ EMNLP 2023\n- 卷期页码：✓ pp 5433–5442\n- 论文存在：✓\n- 引用上下文：✓ — \"LP is well-calibrated at population level\" 和 verbalized confidence\n- **结论：✅ OK**\n\n### 34. [yun2025price] Yun et al. (2025). \"The Price of Format: Diversity Collapse in LLMs\". Findings of EMNLP 2025.\n- 在线验证：ACL Anthology ✓ (2025.findings-emnlp.836)\n- 作者：✓ Yun, An, Wang, Peng, Shang\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ Findings of EMNLP 2025\n- 论文存在：✓\n- 引用上下文：✓ — \"diversity collapse under constrained decoding\"\n- **结论：✅ OK**\n\n### 35. [gao2023scaling] Gao, Schulman, Hilton (2023). \"Scaling Laws for Reward Model Overoptimization\". ICML 2023.\n- 在线验证：PMLR ✓ (v202, pp 10835–10866)\n- 作者：✓\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ ICML 2023\n- 论文存在：✓\n- 引用上下文：✓ — \"BoN scaling laws\"\n- **结论：✅ OK**\n\n### 36. [platt1999probabilistic] Platt (1999). \"Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods\". Advances in Large Margin Classifiers, pp 61–74. MIT Press.\n- 在线验证：Google Scholar ✓（经典论文）\n- 作者：✓ John C. Platt\n- 年份：✓ 1999\n- 标题：✓\n- Venue：✓ Advances in Large Margin Classifiers, MIT Press\n- 卷期页码：✓ pp 61–74\n- 论文存在：✓\n- 引用上下文：✓ — \"Platt scaling fits a logistic regression\"\n- **结论：✅ OK**\n\n### 37. [guo2017calibration] Guo et al. (2017). \"On Calibration of Modern Neural Networks\". ICML 2017, pp 1321–1330.\n- 在线验证：PMLR ✓ (v70)\n- 作者：✓ Guo, Pleiss, Sun, Weinberger\n- 年份：✓ 2017\n- 标题：✓\n- Venue：✓ ICML 2017\n- 卷期页码：✓ pp 1321–1330\n- 论文存在：✓\n- 引用上下文：✓ — \"temperature scaling divides logits by a scalar\"\n- **结论：✅ OK**\n\n### 38. [geifman2017selective] Geifman, El-Yaniv (2017). \"Selective Classification for Deep Neural Networks\". NeurIPS 30.\n- 在线验证：NeurIPS proceedings ✓ | arXiv ✓ (1705.08500)\n- 作者：✓\n- 年份：✓ 2017\n- 标题：✓\n- Venue：⚠️ — bib 写 \"Advances in Neural Information Processing Systems\" volume 30，但 2017 年会议名称仍为 **NIPS**（2018 年才改名 NeurIPS）。\"NeurIPS 30\" 不准确，应为 \"NIPS 2017\" 或 \"Advances in Neural Information Processing Systems 30\"\n- DOI/arXiv：✓ 1705.08500\n- 论文存在：✓\n- 引用上下文：✓ — \"selective prediction\" 和 \"support abstention\"\n- **结论：⚠️ 建议修正** — venue 名称时间错误（NIPS vs NeurIPS）。实际影响较小，因 booktitle 用的是通用的 \"Advances in Neural Information Processing Systems\"。\n\n### 39. [dong2024xgrammar] Dong et al. (2024). \"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\". arXiv:2411.15100.\n- 在线验证：arXiv ✓ | MLSys 2025 ✓\n- 作者：✓ Dong, Ruan, Cai, Lai, Xu, Zhao, Chen\n- 年份：✓/⚠️ — arXiv preprint 2024，但已在 **MLSys 2025** 正式发表\n- 标题：✓\n- Venue：⚠️ — bib 仅列 arXiv preprint，但论文已被 MLSys 2025 接收并发表\n- DOI/arXiv：✓ 2411.15100\n- 论文存在：✓\n- 引用上下文：✓ — constrained decoding engine\n- **结论：⚠️ 建议修正** — 应更新为 MLSys 2025 venue\n\n### 40. [lin2022teaching] Lin, Hilton, Evans (2022). \"Teaching Models to Express Their Uncertainty in Words\". TMLR.\n- 在线验证：arXiv ✓ (2205.14334) | TMLR ✓\n- 作者：✓\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ Transactions on Machine Learning Research (TMLR)\n- DOI/arXiv：✓ 2205.14334\n- 论文存在：✓\n- 引用上下文：✓ — verbalized confidence baseline\n- **结论：✅ OK**\n\n### 41. [farquhar2024detecting] Farquhar et al. (2024). \"Detecting hallucinations in large language models using semantic entropy\". Nature 630, pp 625–630.\n- 在线验证：Nature ✓ | Google Scholar ✓\n- 作者：✓ Farquhar, Kossen, Kuhn, Gal\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ Nature, volume 630\n- 卷期页码：✓ pp 625–630\n- DOI：✓ 10.1038/s41586-024-07421-0\n- 论文存在：✓\n- 引用上下文：✓ — novelty comparison table\n- **结论：✅ OK**\n\n### 42. [chen2023twofailures] Chen et al. (2024). \"Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs\". TMLR.\n- 在线验证：arXiv ✓ (2305.14279) | TMLR ✓\n- 作者：✓ Chen, Phang, Parrish, Padmakumar, Zhao, Bowman, Cho\n- 年份：✓ year=2024 正确（TMLR 发表年）；cite key 用 2023 反映 preprint 年，可接受\n- 标题：✓\n- Venue：✓ TMLR\n- DOI/arXiv：✓ 2305.14279\n- 论文存在：✓\n- 引用上下文：✓ — \"SC can fail when consistent outputs are wrong\"\n- **结论：✅ OK**（key-year 轻微不一致但可接受）\n\n### 43. [aggarwal2023adaptive] Aggarwal et al. (2023). \"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs\". EMNLP 2023.\n- 在线验证：arXiv ✓ (2305.11860) | EMNLP 2023 ✓\n- 作者：✓ Aggarwal, Madaan, Yang, Mausam\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ EMNLP 2023\n- DOI/arXiv：✓ 2305.11860\n- 论文存在：✓\n- 引用上下文：✓ — novelty comparison table\n- **结论：✅ OK**\n\n### 44. [xie2023zeroshot] Xie et al. (2023). \"Empirical Study of Zero-Shot NER with ChatGPT\". EMNLP 2023, pp 7935–7956.\n- 在线验证：ACL Anthology ✓ (2023.emnlp-main.493)\n- 作者：✓ Xie, Li, Zhang, Zhang, Liu, Wang\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ EMNLP 2023\n- 卷期页码：✓ pp 7935–7956\n- DOI：✓ 10.18653/v1/2023.emnlp-main.493\n- 论文存在：✓\n- 引用上下文：✓ — \"propose entity voting for zero-shot NER\"\n- **结论：✅ OK**\n\n### 45. [muennighoff2025s1] Muennighoff et al. (2025). \"s1: Simple Test-Time Scaling\". EMNLP 2025.\n- 在线验证：arXiv ✓ (2501.19393) | ACL Anthology ✓ (2025.emnlp-main.1025)\n- 作者：✓ 全部 10 位作者正确\n- 年份：✓ 2025\n- 标题：✓（注：原作者用全小写 \"s1: Simple test-time scaling\"，bib 用 title case，BibTeX style 会自动处理）\n- Venue：✓ EMNLP 2025\n- DOI/arXiv：✓ 2501.19393\n- 论文存在：✓\n- 引用上下文：✓ — \"extended reasoning\"\n- **结论：✅ OK**\n\n### 46. [eikema2020map] Eikema, Aziz (2020). \"Is MAP Decoding All You Need? The Inadequacy of the Mode in Neural Machine Translation\". COLING 2020, pp 4506–4520.\n- 在线验证：ACL Anthology ✓ (2020.coling-main.398)\n- 作者：✓\n- 年份：✓ 2020\n- 标题：✓\n- Venue：✓ COLING 2020\n- 卷期页码：✓ pp 4506–4520\n- 论文存在：✓\n- 引用上下文：✓ — MBR decoding foundational reference\n- **结论：✅ OK**\n\n### 47. [kumar2004minimum] Kumar, Byrne (2004). \"Minimum Bayes-Risk Decoding for Statistical Machine Translation\". HLT-NAACL 2004, pp 169–176.\n- 在线验证：ACL Anthology ✓ (N04-1022)\n- 作者：✓\n- 年份：✓ 2004\n- 标题：✓\n- Venue：✓ HLT-NAACL 2004\n- 卷期页码：✓ pp 169–176\n- 论文存在：✓\n- 引用上下文：✓ — MBR decoding foundational reference\n- **结论：✅ OK**\n\n### 48. [dembczynski2011exact] Dembczyński et al. (2011). \"An Exact Algorithm for F-Measure Maximization\". NeurIPS 24, pp 1404–1412.\n- 在线验证：NeurIPS proceedings ✓\n- 作者：✓ Dembczyński, Waegeman, Cheng, Hüllermeier\n- 年份：✓ 2011\n- 标题：✓\n- Venue：✓ NeurIPS (NIPS) 2011, vol 24\n- 卷期页码：✓ pp 1404–1412\n- 论文存在：✓\n- 引用上下文：✓ — \"Set-level F1 admits no closed-form threshold\"\n- **结论：✅ OK**\n\n### 49. [desai2020calibration] Desai, Durrett (2020). \"Calibration of Pre-trained Transformers\". EMNLP 2020, pp 295–302.\n- 在线验证：ACL Anthology ✓ (2020.emnlp-main.21)\n- 作者：✓\n- 年份：✓ 2020\n- 标题：✓\n- Venue：✓ EMNLP 2020\n- 卷期页码：✓ pp 295–302\n- 论文存在：✓\n- 引用上下文：✓ — \"calibrated LMs\"\n- **结论：✅ OK**\n\n### 50. [huang2024large] Huang et al. (2024). \"Large Language Models Cannot Self-Correct Reasoning Yet\". ICLR 2024.\n- 在线验证：OpenReview ✓ (IkmD3fKBPQ)\n- 作者：✓ Huang, Chen, Mishra, Zheng, Yu, Song, Zhou\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ ICLR 2024\n- 论文存在：✓\n- 引用上下文：✓ — \"introspection boundary\"（论文论证 LLM 无法 self-correct reasoning，用于支持 models encode quality internally but can't self-judge 的论点）\n- **结论：✅ OK**\n\n### 51. [li2024simple] Li, Ramprasad, Zhang (2024). \"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction\". Findings of EMNLP 2024.\n- 在线验证：ACL Anthology ✓ | arXiv ✓ (2402.13364)\n- 作者：✓\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ Findings of EMNLP 2024\n- DOI/arXiv：✓ 2402.13364\n- 论文存在：✓\n- 引用上下文：N/A — **未在任何 tex 文件中被引用**\n- **结论：⚠️ 未使用，建议移除或确认是否需要**\n\n### 52. [xie2024selfimproving] Xie et al. (2024). \"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\". NAACL 2024.\n- 在线验证：ACL Anthology ✓ (2024.naacl-short.49)\n- 作者：✓ Xie, Li, Zhang, Liu, Wang\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ NAACL 2024 (Short Papers, pp 583–593)\n- 论文存在：✓\n- 引用上下文：✓ — \"extend this with SC-based self-annotation\"\n- **结论：✅ OK**\n\n### 53. [madaan2023selfrefine] Madaan et al. (2023). \"Self-Refine: Iterative Refinement with Self-Feedback\". NeurIPS 36.\n- 在线验证：NeurIPS proceedings ✓\n- 作者：✓ 全部 16 位作者正确\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ NeurIPS 2023 (volume 36)\n- 论文存在：✓\n- 引用上下文：✓ — \"iterative self-refinement\"\n- **结论：✅ OK**\n\n### 54. [angelopoulos2023conformal] Angelopoulos, Bates (2023). \"Conformal Prediction: A Gentle Introduction\". Foundations and Trends in ML, 16(4), pp 494–591.\n- 在线验证：ACM DL ✓ | Google Scholar ✓\n- 作者：✓\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ Foundations and Trends in Machine Learning\n- 卷期页码：✓ Vol 16, No 4, pp 494–591\n- 论文存在：✓\n- 引用上下文：✓ — \"conformal prediction\"\n- **结论：✅ OK**\n\n### 55. [malinin2021uncertainty] Malinin, Gales (2021). \"Uncertainty Estimation in Autoregressive Structured Prediction\". ICLR 2021.\n- 在线验证：OpenReview ✓\n- 作者：✓ Andrey Malinin, Mark Gales\n- 年份：✓ 2021\n- 标题：✓\n- Venue：✓ ICLR 2021\n- 论文存在：✓\n- 引用上下文：✓ — \"uncertainty for structured prediction\"\n- **结论：✅ OK**\n\n### 56. [yee2019noisy] Yee, Dauphin, Auli (2019). \"Simple and Effective Noisy Channel Modeling for Neural Machine Translation\". EMNLP-IJCNLP 2019.\n- 在线验证：ACL Anthology ✓ (D19-1571) | arXiv ✓ (1908.05731)\n- 作者：✗ — bib 列 3 位作者（Yee, Dauphin, Auli），但 ACL Anthology 和 arXiv 均列 **4 位作者**：Kyra Yee, **Nathan Ng**, Yann N. Dauphin, Michael Auli。**缺少 Nathan Ng**。\n- 年份：✓ 2019\n- 标题：✓\n- Venue：✓ EMNLP-IJCNLP 2019\n- DOI/arXiv：✓ 1908.05731\n- 论文存在：✓\n- 引用上下文：✓ — \"noisy channel models\"\n- **结论：⚠️ 需修正** — 缺少作者 Nathan Ng\n\n### 57. [li2023stepaware] Li et al. (2023). \"Making Large Language Models Better Reasoners with Step-Aware Verifier\". ACL 2023.\n- 在线验证：ACL Anthology ✓ (2023.acl-long.291) | arXiv ✓ (2206.02336)\n- 作者：✓ Li, Lin, Zhang, Fu, Chen, Lou, Chen\n- 年份：✓ 2023\n- 标题：✗ — bib 写 \"Making **Large** Language Models Better Reasoners with Step-Aware Verifier\"，但 ACL 2023 正式发表标题为 \"Making Language Models Better Reasoners with Step-Aware Verifier\"（**无 \"Large\"**）。arXiv 版本标题含 \"Large\"，但应以正式发表版为准。\n- Venue：✓ ACL 2023\n- DOI/arXiv：✓ 2206.02336\n- 论文存在：✓\n- 引用上下文：✓ — \"trained verifiers\"\n- **结论：⚠️ 需修正** — 标题应删除 \"Large\"，与 ACL 2023 正式发表版一致\n\n### 58. [xiao2022uncertainty] Xiao et al. (2022). \"Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis\". Findings of EMNLP 2022.\n- 在线验证：ACL Anthology ✓ (2022.findings-emnlp.538)\n- 作者：✓ Xiao, Liang, Bhatt, Neiswanger, Salakhutdinov, Morency\n- 年份：✓ 2022\n- 标题：✓\n- Venue：✓ Findings of EMNLP 2022\n- 论文存在：✓\n- 引用上下文：N/A — **未在任何 tex 文件中被引用**\n- **结论：⚠️ 未使用，建议移除或确认是否需要**\n\n### 59. [li2026rewardtail] Li, Qian, Mou (2026). \"Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search\". arXiv:2602.01485.\n- 在线验证：arXiv ✓\n- 作者：✓\n- 年份：✓ 2026\n- 标题：✓\n- Venue：✓ arXiv preprint\n- DOI/arXiv：✓ 2602.01485\n- 论文存在：✓\n- 引用上下文：✓ — \"reward-tail-guided search\"\n- **结论：✅ OK**\n\n### 60. [shinn2023reflexion] Shinn et al. (2023). \"Reflexion: Language Agents with Verbal Reinforcement Learning\". NeurIPS 36.\n- 在线验证：NeurIPS proceedings ✓ | arXiv ✓ (2303.11366)\n- 作者：✗ — bib 列 5 位作者（Shinn, Cassano, Gopinath, Narasimhan, Yao），但 NeurIPS 2023 正式 proceedings 列 **6 位作者**：Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao。**缺少 Edward Berman**。\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ NeurIPS 2023 (volume 36)\n- 论文存在：✓\n- 引用上下文：✓ — \"Iterative self-verification\"\n- **结论：⚠️ 需修正** — 缺少作者 Edward Berman\n\n### 61. [xu2024llmie] Xu et al. (2024). \"Large Language Models for Generative Information Extraction: A Survey\". Frontiers of Computer Science, 18(6):186357.\n- 在线验证：Springer ✓ | Google Scholar ✓\n- 作者：✓ 全部 10 位作者正确\n- 年份：✓ 2024\n- 标题：✓\n- Venue：✓ Frontiers of Computer Science\n- 卷期页码：✓ Vol 18, No 6, 186357\n- DOI：✓ 10.1007/s11704-024-40555-y\n- 论文存在：✓\n- 引用上下文：✓ — \"LLM-based IE has expanded rapidly\"\n- **结论：✅ OK**\n\n### 62. [wang2025gptner] Wang et al. (2025). \"GPT-NER: Named Entity Recognition via Large Language Models\". Findings of NAACL 2025.\n- 在线验证：ACL Anthology ✓ (2025.findings-naacl.239)\n- 作者：✓ Wang, Sun, Li, Ouyang, Wu, Zhang, Li, Wang（8 位，与 ACL Anthology 一致）\n- 年份：✓ 2025\n- 标题：✓\n- Venue：✓ Findings of NAACL 2025\n- 论文存在：✓\n- 引用上下文：✓ — \"Self-verification approaches that prompt LLMs to validate their own extractions improve NER\"\n- **结论：✅ OK**\n\n### 63. [gero2023selfverification] Gero et al. (2023). \"Self-Verification Improves Few-Shot Clinical Information Extraction\". arXiv:2306.00024.\n- 在线验证：arXiv ✓\n- 作者：✓ Gero, Singh, Cheng, Naumann, Galley, Gao, Poon\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ arXiv preprint（确认仍为 preprint，无正式 venue）\n- DOI/arXiv：✓ 2306.00024\n- 论文存在：✓\n- 引用上下文：✓ — \"clinical IE\"\n- **结论：✅ OK**\n\n### 64. [wadhwa2023revisiting] Wadhwa, Amir, Wallace (2023). \"Revisiting Relation Extraction in the era of Large Language Models\". ACL 2023, pp 15566–15589.\n- 在线验证：ACL Anthology ✓ (2023.acl-long.868)\n- 作者：✓\n- 年份：✓ 2023\n- 标题：✓\n- Venue：✓ ACL 2023 Long Papers\n- 卷期页码：✓ pp 15566–15589\n- 论文存在：✓\n- 引用上下文：✓ — \"benchmark LLM-based RE, confirming that structured outputs pose challenges distinct from free-form generation\"\n- **结论：✅ OK**\n\n---\n\n## 统计\n\n| 类别 | 数量 |\n|------|------|\n| ✅ OK | 54 |\n| ⚠️ 需修正 | 4 (kang2025selfcertainty, yee2019noisy, shinn2023reflexion, li2023stepaware) |\n| ⚠️ 建议修正 | 3 (dong2024xgrammar, fleiss1971agreement, geifman2017selective) |\n| 🧹 未使用 | 3 (holm1979simple, li2024simple, xiao2022uncertainty) |\n| ❌ 论文不存在 / hallucinated | **0** |\n\n**所有 64 篇论文均为真实存在的论文，无 hallucinated citations。**\n\n---\n\n## 建议修复清单（按优先级排序）\n\n### 必须修复\n1. **`kang2025selfcertainty`**: booktitle 中 \"38\" → \"39\"\n2. **`yee2019noisy`**: 添加缺失作者 `Nathan Ng`（第二作者位置）\n3. **`shinn2023reflexion`**: 添加缺失作者 `Edward Berman`（Cassano 和 Gopinath 之间）\n4. **`li2023stepaware`**: title 中删除 \"Large\"（\"Making Language Models Better Reasoners...\"）\n\n### 建议修复\n5. **`dong2024xgrammar`**: 更新为 MLSys 2025 正式 venue\n6. **`fleiss1971agreement`**: 添加 `volume = {76}`, `pages = {378--382}`\n7. **`geifman2017selective`**: venue 无需改动（booktitle 已使用通用 \"Advances in Neural Information Processing Systems\"）\n\n### 清理\n8. 移除 3 个未引用 entry：`holm1979simple`, `li2024simple`, `xiao2022uncertainty`\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 400_

报告已写入 `artifacts/ref_audit_worker_B.md`。

核心发现：
- **64 篇论文全部真实存在，无 hallucinated citations**
- **4 条必须修复**：`kang2025selfcertainty`（NeurIPS volume 38→39）、`yee2019noisy`（缺作者 Nathan Ng）、`shinn2023reflexion`（缺作者 Edward Berman）、`li2023stepaware`（标题多了 "Large"）
- **3 条建议修复**：`dong2024xgrammar`（应更新为 MLSys 2025）、`fleiss1971agreement`（缺 volume/pages）、`geifman2017selective`（NIPS/NeurIPS 命名）
- **3 条未使用 entry** 可清理：`holm1979simple`、`li2024simple`、`xiao2022uncertainty`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "uuid": "b491faca-98f3-421e-959c-69a35574ad57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jd7V5tTft2jaXpau51zgCY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16520,
      "cache_read_input_tokens": 78284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16520
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


### Runtime record

_source line 401_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779858000,
    "rateLimitType": "seven_day",
    "utilization": 0.99,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "90dda229-658c-49fd-8fae-0d88d9cf26d1",
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1"
}
```

---


### Task result

_source line 402_

报告已写入 `artifacts/ref_audit_worker_B.md`。

核心发现：
- **64 篇论文全部真实存在，无 hallucinated citations**
- **4 条必须修复**：`kang2025selfcertainty`（NeurIPS volume 38→39）、`yee2019noisy`（缺作者 Nathan Ng）、`shinn2023reflexion`（缺作者 Edward Berman）、`li2023stepaware`（标题多了 "Large"）
- **3 条建议修复**：`dong2024xgrammar`（应更新为 MLSys 2025）、`fleiss1971agreement`（缺 volume/pages）、`geifman2017selective`（NIPS/NeurIPS 命名）
- **3 条未使用 entry** 可清理：`holm1979simple`、`li2024simple`、`xiao2022uncertainty`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 749664,
  "duration_api_ms": 1968558,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "d4dccfe0-a914-4279-acc5-7f9ba758aaa1",
  "total_cost_usd": 6.785260749999998,
  "usage": {
    "input_tokens": 11111,
    "cache_creation_input_tokens": 82963,
    "cache_read_input_tokens": 582059,
    "output_tokens": 30552,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 82963,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 252,
        "cache_read_input_tokens": 78284,
        "cache_creation_input_tokens": 16520,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 16520
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1166559,
      "outputTokens": 37707,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 105,
      "costUSD": 2.405094000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14192,
      "outputTokens": 57685,
      "cacheReadInputTokens": 2923976,
      "cacheCreationInputTokens": 224815,
      "webSearchRequests": 0,
      "costUSD": 4.38016675,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3403b85b-982e-4336-b4ad-910a9bb4e780"
}
```

</details>

---
