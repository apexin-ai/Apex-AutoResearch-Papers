# Research conversation: [Round 1 审稿请求]: **[Round 1 — 服务器重启后重新分配]** 你是 Reviewer 2，负责**新颖性、Related Work 完整性、论文整体呈现**。如果你已完成审稿，请直接提交；如果被服务器重启中断，请从头 — Part 6 of 6

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../research-conversation-round-1-round-1-reviewer-2-related-work.md) · [Structured JSON](../../../sessions/ba/ba825aee372f13ddad4c.json)

## Round 1

### Assistant

_source line 93 · 2026-05-16T17:02:55.519Z_

<details><summary>Logged reasoning block</summary>

```text
Now I've read the full paper. Let me compile my observations:

**Major structural findings:**

1. **Abstract is "TODO"** - "TODO: Abstract is to be written after experiments." This is a critical issue for submission.

2. **Related Work is "TODO"** - Section 2 says "TODO: Related work to be written". This is another critical issue.

3. **No Experiments/Results section** - The paper jumps from Method (Sections 3.1-3.4) directly to References on page 6. There are NO experimental results, no tables, no figures (other than the method description). 

The paper references §7.2 for comparing specifications, but there is no Section 7. There's also no Conclusion section at all.

**Page count**: The paper is 8 pages, but pages 6-8 are entirely references (3 pages of references). The actual content is only about 5.5 pages (introduction + method).

This is essentially an incomplete manuscript with only introduction and methodology sections written.

**Now let me evaluate the content that IS present, focusing on my assigned dimensions:**

### 1. Novelty/Excitement

The core idea is using IRT augmented with a contamination covariate to model response patterns, which is an interesting extension of standard item response theory.

The two-stage pipeline—first estimating per-item contamination exposure using Min-K++ and other signals, then fitting contamination-augmented 4PL IRT—is a reasonable approach. The finding that contamination effects are benchmark-dependent (varying in sign and magnitude) and the Min-K++ direction reversal observation are noteworthy.

Relative to existing literature on IRT for LLMs (TinyBenchmarks, PSN-IRT, HiBayES, and others) and contamination detection methods (Min-K++, etc.), the paper appears to be the first to combine these two concerns, though the execution is incomplete.

The main concern is that DCR (Li et al., 2025) already addresses decontaminated calibration and ranking, which directly overlaps with the novelty claim here. Since the Related Work section is still a TODO, it's unclear how this work differentiates itself—the technical contribution of adding a contamination covariate term to IRT feels somewhat incremental. That said, the "negative signal degradation" finding could be genuinely interesting if it holds up.

The Related Work section being incomplete makes a full assessment difficult, but from what's cited in the introduction, there's coverage of contamination detection methods, IRT applications to LLMs, and foundational IRT theory. However, the broader IRT literature on item compromise and differential item functioning seems to be missing, which could be relevant context. from educational measurement: The paper cites Eckerly 2017 but the educational measurement literature on item compromise (Sinharay 2017, cited in references) and differential item functioning is much broader. The DIF framework is actually very relevant to what they're doing.
- (b) Dynamic benchmark approaches: LiveBench is mentioned in introduction but other dynamic approaches like DynaEval, or benchmark renewal strategies
- (c) Probability calibration: Guo et al. 2017 "On Calibration of Modern Neural Networks" - this is about probability calibration which is different from score calibration, but the paper uses the term "calibration" which creates confusion
- (d) KDS (Knowledge Distillation Signatures) - mentioned in the task description but I need to check if it's cited. Looking at references... Xu et al. 2025a is about "Knowledge distillation signatures for efficient contamination detection" - yes, KDS is cited.
- (e) CDD - I don't see it explicitly mentioned. Actually, let me re-check. The task mentions CDD but I'm not sure it's cited.
- (f) Xu et al. 2025b "The emperor's new clothes" about systematic evaluation of contamination mitigation strategies

The paper has major structural gaps — the abstract and related work sections are missing entirely, and there are no experiments, results, figures, or tables. It's essentially just an introduction and methods with three pages of references out of eight total. The introduction does flow well and sets up the problem effectively, but the methods section needs to be completed with the actual technical details. formulation
- But without results, the claims in the introduction are entirely unsupported

### 4. Significance/Impact

Without experimental results, significance cannot be properly evaluated. The framework itself is interesting in concept, but its practical value depends entirely on whether the calibration actually works or provides meaningful insights.

### 5. Format compliance

- **Anonymity**: "Anonymous" is listed as author — good for double-blind
- **Date**: "May 13, 2026" — this should probably not be present in a blind submission
- **Page count**: 8 pages total, but only ~5.5 pages of content + 2.5 pages of references. The 8-page limit is for content, with unlimited references, so the actual content is well under the limit.
- **Template**: Appears to use acl_latex format

### ARR Review Form Dimensions (based on what I found):

- **Soundness** (1-5): The methodology is theoretically sound, but without experimental validation, many of the core claims remain unverified.
- **Excitement** (1-5): The concept has potential, though it feels somewhat incremental compared to existing work on IRT applied to LLMs and contamination detection methods.
- **Overall** (1-5): Still need to determine this based on the full assessment.
- **Reproducibility** (1-5): Difficult to assess without actual results or code availability.

I'm noticing a discrepancy between the requested 6-point scale and the standard ARR form which uses 1-5 with half-point increments. Since the official ARR guidelines use the 1-5 scale, I'll stick with that standard format.

Now I need to write the actual review. This paper is clearly incomplete and cannot be accepted in its current form. Let me also verify some of the key references mentioned to check for accuracy.

Looking at the references cited, most appear plausible given we're in May 2026 - the AAAI 2026 conference would have already occurred, and EMNLP 2025 is in the past. However, I'm noticing some references that seem questionable and worth scrutinizing further. I'm continuing through the reference list on pages 6 and 7, and I still don't see Barkley or Stallings anywhere. I'm seeing Lord 1980 for IRT foundations and Maris and Bechger 2009, but those Barkley and Stallings citations from page 4 remain unaccounted for in what I can see of the references. Growing Pains)
- Rao 2026 (Silicon bureaucracy)
- San Martin et al. 2009 (Consequential validity)
- Sinharay 2017 (Detection of item preknowledge)
- Talts et al. 2018 (SBC)
- Ultzsch and Nestler 2022 (Automatic differentiation variational inference for IRT)
- Wang et al. 2025 (fragility of benchmark evaluations)
- White et al. 2024 (LiveBench)
- Wu et al. 2025 (Self-critique as contamination signal)
- Xu et al. 2025a (KDS)
- Xu et al. 2025b (emperor's new clothes)

Page 8:
- Yang et al. 2024 (inference-time decontamination, EMNLP Findings 2024)
- Yang et al. 2026 (RL amplifies contamination)
- Zhang et al. 2025 (How much can we forget, ICML 2025)
- Zhuang et al. 2025 (HiBayES)

I'm noticing some citation mismatches in the document. Barkley 2017 and Stallings 2017 appear in the text but aren't in the bibliography, which suggests they might be fabricated references. There's also an error where the text cites Edwards et al. 2009 for reciprocal rank fusion, but the actual paper is by Cormack et al. 2009. I'm checking the other citations now—Maris and Bechger 2009 is there on page 7, and San Martin et al. 2009 checks out too. But Barkley 2017 and Stallings 2017 are cited in the text and completely missing from the bibliography, which is a clear error. Given how incomplete this paper is—the abstract is just a placeholder, the entire Related Work section is unfinished, and there are no experiments or results—this is definitely a reject. Let me structure my review around the critical issues.

I should still evaluate the methodology and novelty of what's actually written since that's my main responsibility. Before I finalize my review, I'm going to use the reference verification tool to double-check those missing citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f541b84c-d271-4d4b-a386-1acfa827bafd",
  "isSidechain": false,
  "requestId": "req_011Cb6c9BcXcoUa4tNWf7WMF",
  "type": "assistant",
  "uuid": "9ee99fc8-282d-4981-bc98-23e1851123a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sb8zkV5EsNRXFsK4EpZBv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1532,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 39393,
      "output_tokens": 3804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1532,
          "output_tokens": 3804,
          "cache_read_input_tokens": 39393,
          "cache_creation_input_tokens": 1362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1362
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-16T17:02:56.001Z_

论文读完。关键发现：Abstract 和 Related Work 均为 TODO 占位符，完全没有实验/结果章节。接下来验证引用真实性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ee99fc8-282d-4981-bc98-23e1851123a1",
  "isSidechain": false,
  "requestId": "req_011Cb6c9BcXcoUa4tNWf7WMF",
  "type": "assistant",
  "uuid": "d91678fa-1b24-41f7-80b3-7444484c6e90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sb8zkV5EsNRXFsK4EpZBv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1532,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 39393,
      "output_tokens": 3804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1532,
          "output_tokens": 3804,
          "cache_read_input_tokens": 39393,
          "cache_creation_input_tokens": 1362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1362
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 95 · 2026-05-16T17:02:56.257Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GYYn6aiBecuisGAEKRgSsn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__verify_references",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d91678fa-1b24-41f7-80b3-7444484c6e90",
  "isSidechain": false,
  "requestId": "req_011Cb6c9BcXcoUa4tNWf7WMF",
  "type": "assistant",
  "uuid": "877d9652-3c57-4ebd-8ecc-f2b1750f94e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sb8zkV5EsNRXFsK4EpZBv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1532,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 39393,
      "output_tokens": 3804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1532,
          "output_tokens": 3804,
          "cache_read_input_tokens": 39393,
          "cache_creation_input_tokens": 1362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1362
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-16T17:02:56.264Z_

<details><summary>↩ Tool result · `toolu_01GYYn6aiBecuisGAEKRgSsn`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__verify_references"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "877d9652-3c57-4ebd-8ecc-f2b1750f94e7",
  "isSidechain": false,
  "promptId": "4e3fc52f-dc1e-44b5-9d0f-d389164f223c",
  "type": "user",
  "uuid": "dde9bfc8-e3f7-4160-8069-468aa28e5fd0",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__verify_references"
    ],
    "query": "select:mcp__agent-ml-research__verify_references",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "877d9652-3c57-4ebd-8ecc-f2b1750f94e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 97 · 2026-05-16T17:03:00.483Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01ALynnUnDzBZe5dS6F4pPH2`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dde9bfc8-e3f7-4160-8069-468aa28e5fd0",
  "isSidechain": false,
  "requestId": "req_011Cb6cG5mVguxUcr8SsjhFQ",
  "type": "assistant",
  "uuid": "67896969-512c-4df0-9c7f-e89f9fdc87ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6buTDQAPKXCKrd9anUWdA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5694,
      "cache_read_input_tokens": 40755,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 40755,
          "cache_creation_input_tokens": 5694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5694
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-16T17:04:17.947Z_

<details><summary>↩ Tool result · `toolu_01ALynnUnDzBZe5dS6F4pPH2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 61, \"total_citations\": 93, \"unique_cited_keys\": 44, \"orphan_bib\": 17, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 30, \"online_not_found\": 24, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [\"barton1981\", \"battauz2011\", \"carroll2006\", \"culpepper2016\", \"embretson2000\", \"fuller1987\", \"jerzak2026\", \"liao2012\", \"mislevy1987\", \"park2023trak\", \"pruthi2020tracin\", \"reckase2009mirt\", \"sanmartin2015\", \"stefanski1985\", \"thissen2001\", \"wainer2007testlet\", \"westfall2016\"], \"missing_bib\": [], \"orphan_count\": 17, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"lord1980\", \"type\": \"book\", \"title\": \"Applications of Item Response Theory to Practical Testing Problems\", \"authors\": \"Lord, Frederic M.\", \"year\": \"1980\", \"venue\": \"\"}, {\"key\": \"eckerly2017\", \"type\": \"article\", \"title\": \"Detecting Item Compromise in the Context of Item Response Theory\", \"authors\": \"Eckerly, Carol\", \"year\": \"2017\", \"venue\": \"Applied Psychological Measurement\"}, {\"key\": \"sinharay2017\", \"type\": \"article\", \"title\": \"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\", \"authors\": \"Sinharay, Sandip\", \"year\": \"2017\", \"venue\": \"Journal of Educational and Behavioral Statistics\"}, {\"key\": \"deboeck2004\", \"type\": \"book\", \"title\": \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\", \"authors\": \"De Boeck, Paul and Wilson, Mark\", \"year\": \"2004\", \"venue\": \"\"}, {\"key\": \"adams1997\", \"type\": \"article\", \"title\": \"The Multidimensional Random Coefficients Multinomial Logit Model\", \"authors\": \"Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung\", \"year\": \"1997\", \"venue\": \"Applied Psychological Measurement\"}, {\"key\": \"mislevy1986\", \"type\": \"article\", \"title\": \"Bayes Modal Estimation in Item Response Models\", \"authors\": \"Mislevy, Robert J.\", \"year\": \"1986\", \"venue\": \"Psychometrika\"}, {\"key\": \"sanmartin2009\", \"type\": \"article\", \"title\": \"Consequential Validity of Item Response Theory Models for Measuring Latent Constructs\", \"authors\": \"San Mart\\\\'in, Ernesto and Del Pino, Guido and De Boeck, Paul\", \"year\": \"2009\", \"venue\": \"Psychometrika\"}, {\"key\": \"maris2009\", \"type\": \"article\", \"title\": \"On Interpreting the Model Parameters for the Three Parameter Logistic Model\", \"authors\": \"Maris, Gunter and Bechger, Timo\", \"year\": \"2009\", \"venue\": \"Measurement\"}, {\"key\": \"cormack2009\", \"type\": \"inproceedings\", \"title\": \"Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods\", \"authors\": \"Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan\", \"year\": \"2009\", \"venue\": \"Proceedings of the 32nd International ACM SIGIR Conference on Research and Devel...\"}, {\"key\": \"hoffman2014\", \"type\": \"article\", \"title\": \"The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo\", \"authors\": \"Hoffman, Matthew D. and Gelman, Andrew\", \"year\": \"2014\", \"venue\": \"Journal of Machine Learning Research\"}, {\"key\": \"carpenter2017\", \"type\": \"article\", \"title\": \"Stan: A Probabilistic Programming Language\", \"authors\": \"Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Go...\", \"year\": \"2017\", \"venue\": \"Journal of Statistical Software\"}, {\"key\": \"talts2018sbc\", \"type\": \"article\", \"title\": \"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\", \"authors\": \"Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gel...\", \"year\": \"2018\", \"venue\": \"arXiv preprint\"}, {\"key\": \"ulitzsch2022\", \"type\": \"article\", \"title\": \"Automatic Differentiation Variational Inference for Item Response Theory Models\", \"authors\": \"Ulitzsch, Esther and Nestler, Steffen\", \"year\": \"2022\", \"venue\": \"British Journal of Mathematical and Statistical Psychology\"}, {\"key\": \"duan2025minkpp\", \"type\": \"inproceedings\", \"title\": \"Min-K\\\\%++: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models\", \"authors\": \"Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai\", \"year\": \"2025\", \"venue\": \"Proceedings of the 13th International Conference on Learning Representations (IC...\"}, {\"key\": \"dekoninck2024constat\", \"type\": \"inproceedings\", \"title\": \"ConStat: Performance-Based Contamination Detection in Large Language Models\", \"authors\": \"De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems 37 (NeurIPS)\"}, {\"key\": \"wust2025selfcritique\", \"type\": \"article\", \"title\": \"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations\", \"authors\": \"W\\\\\\\"ust, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"xu2025kds\", \"type\": \"inproceedings\", \"title\": \"Knowledge Distillation Signatures for Efficient Contamination Detection\", \"authors\": \"Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning (ICML)\"}, {\"key\": \"oren2024proving\", \"type\": \"inproceedings\", \"title\": \"Proving Test Set Contamination in Black Box Language Models\", \"authors\": \"Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 12th International Conference on Learning Representations (IC...\"}, {\"key\": \"xu2025emperor\", \"type\": \"inproceedings\", \"title\": \"The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models\", \"authors\": \"Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning (ICML)\"}, {\"key\": \"dong2026dose\", \"type\": \"article\", \"title\": \"Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales\", \"authors\": \"Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"yang2026rl\", \"type\": \"article\", \"title\": \"Reinforcement Learning Amplifies Contamination in LLM Benchmark Evaluation\", \"authors\": \"Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"wang2025fragility\", \"type\": \"article\", \"title\": \"On the Fragility of Benchmark Evaluations for Large Language Models\", \"authors\": \"Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"zhang2025forget\", \"type\": \"inproceedings\", \"title\": \"How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models\", \"authors\": \"Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning (ICML)\"}, {\"key\": \"gu2026psnirt\", \"type\": \"inproceedings\", \"title\": \"PSN-IRT: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory\", \"authors\": \"Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun\", \"year\": \"2026\", \"venue\": \"Proceedings of the 40th AAAI Conference on Artificial Intelligence\"}, {\"key\": \"polo2026growing\", \"type\": \"article\", \"title\": \"Growing Pains: Understanding the Limitations and Potential of IRT for LLM Evaluation at Scale\", \"authors\": \"Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen,...\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"lyu2025atlas\", \"type\": \"article\", \"title\": \"ATLAS: Adaptive Testing via Latent Ability Scoring for Large Language Models\", \"authors\": \"Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"zhuang2025hibayes\", \"type\": \"article\", \"title\": \"HiBayES: Hierarchical Bayesian Evaluation System for Language Models\", \"authors\": \"Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"lalor2024irt\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Large Language Models with Item Response Theory\", \"authors\": \"Lalor, John P. and Yang, Yi and Smith, Noah A.\", \"year\": \"2024\", \"venue\": \"Proceedings of the 38th AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2025dcr\", \"type\": \"inproceedings\", \"title\": \"DCR: Decontaminated Calibration and Ranking for Benchmark Evaluation\", \"authors\": \"Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yang2024inference\", \"type\": \"inproceedings\", \"title\": \"Inference-Time Decontamination of Large Language Models for Benchmark Evaluation\", \"authors\": \"Yang, Shuo and Wei, Xin and Shi, Weicheng\", \"year\": \"2024\", \"venue\": \"Findings of the 2024 Conference on Empirical Methods in Natural Language Process...\"}, {\"key\": \"rao2026silicon\", \"type\": \"article\", \"title\": \"The Silicon Bureaucracy: Evaluating the Evaluators in LLM Benchmarking\", \"authors\": \"Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"hendrycks2021mmlu\", \"type\": \"inproceedings\", \"title\": \"Measuring Massive Multitask Language Understanding\", \"authors\": \"Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, M...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 9th International Conference on Learning Representations (ICL...\"}, {\"key\": \"cobbe2021gsm8k\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint\"}, {\"key\": \"clark2018arc\", \"type\": \"inproceedings\", \"title\": \"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\", \"authors\": \"Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal,...\", \"year\": \"2018\", \"venue\": \"arXiv preprint\"}, {\"key\": \"chen2021humaneval\", \"type\": \"article\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"authors\": \"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\", \"year\": \"2021\", \"venue\": \"arXiv preprint\"}, {\"key\": \"chang2025benchmarking\", \"type\": \"inproceedings\", \"title\": \"A Survey on Evaluation of Large Language Models\", \"authors\": \"Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zh...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"white2024livebench\", \"type\": \"article\", \"title\": \"LiveBench: A Challenging, Contamination-Free LLM Benchmark\", \"authors\": \"White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Ben...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"polo2024tinybenchmarks\", \"type\": \"inproceedings\", \"title\": \"TinyBenchmarks: Evaluating LLMs with Fewer Examples\", \"authors\": \"Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, G...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"han2026probing\", \"type\": \"inproceedings\", \"title\": \"Targeted Probing for Contamination Effects in Large Language Model Evaluations\", \"authors\": \"Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie\", \"year\": \"2026\", \"venue\": \"Findings of the 2026 Conference of the European Chapter of the Association for C...\"}, {\"key\": \"holland1993dif\", \"type\": \"book\", \"title\": \"Differential Item Functioning\", \"authors\": \"Holland, Paul W. and Wainer, Howard\", \"year\": \"1993\", \"venue\": \"\"}, {\"key\": \"thissen1993dif\", \"type\": \"incollection\", \"title\": \"Detection of Differential Item Functioning Using the Parameters of Item Response Models\", \"authors\": \"Thissen, David and Steinberg, Lynne and Wainer, Howard\", \"year\": \"1993\", \"venue\": \"Differential Item Functioning\"}, {\"key\": \"zumbo1999dif\", \"type\": \"book\", \"title\": \"A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary F...\", \"authors\": \"Zumbo, Bruno D.\", \"year\": \"1999\", \"venue\": \"\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"Proceedings of the 34th International Conference on Machine Learning (ICML)\"}, {\"key\": \"angelopoulos2023conformal\", \"type\": \"article\", \"title\": \"Conformal Prediction: A Gentle Introduction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen\", \"year\": \"2023\", \"venue\": \"Foundations and Trends in Machine Learning\"}, {\"key\": \"pruthi2020tracin\", \"type\": \"inproceedings\", \"title\": \"Estimating Training Data Influence by Tracing Gradient Descent\", \"authors\": \"Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund\", \"year\": \"2020\", \"venue\": \"Advances in Neural Information Processing Systems 33 (NeurIPS)\"}, {\"key\": \"park2023trak\", \"type\": \"inproceedings\", \"title\": \"TRAK: Attributing Model Behavior at Scale\", \"authors\": \"Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning (ICML)\"}, {\"key\": \"reckase2009mirt\", \"type\": \"book\", \"title\": \"Multidimensional Item Response Theory\", \"authors\": \"Reckase, Mark D.\", \"year\": \"2009\", \"venue\": \"\"}, {\"key\": \"sanmartin2015\", \"type\": \"article\", \"title\": \"On the Unidentifiability of the Fixed-Effects 3PL Model\", \"authors\": \"San Mart\\\\'in, Ernesto and Gonz\\\\'alez, Jorge and Tuerlinckx, Francis\", \"year\": \"2015\", \"venue\": \"Psychometrika\"}, {\"key\": \"mislevy1987\", \"type\": \"article\", \"title\": \"Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters\", \"authors\": \"Mislevy, Robert J.\", \"year\": \"1987\", \"venue\": \"Applied Psychological Measurement\"}, {\"key\": \"wainer2007testlet\", \"type\": \"book\", \"title\": \"Testlet Response Theory and Its Applications\", \"authors\": \"Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui\", \"year\": \"2007\", \"venue\": \"\"}, {\"key\": \"carroll2006\", \"type\": \"book\", \"title\": \"Measurement Error in Nonlinear Models: A Modern Perspective\", \"authors\": \"Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu...\", \"year\": \"2006\", \"venue\": \"\"}, {\"key\": \"fuller1987\", \"type\": \"book\", \"title\": \"Measurement Error Models\", \"authors\": \"Fuller, Wayne A.\", \"year\": \"1987\", \"venue\": \"\"}, {\"key\": \"stefanski1985\", \"type\": \"article\", \"title\": \"Covariate Measurement Error in Logistic Regression\", \"authors\": \"Stefanski, Leonard A. and Carroll, Raymond J.\", \"year\": \"1985\", \"venue\": \"Annals of Statistics\"}, {\"key\": \"battauz2011\", \"type\": \"article\", \"title\": \"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\", \"authors\": \"Battauz, Michela and Bellio, Ruggero\", \"year\": \"2011\", \"venue\": \"Psychometrika\"}, {\"key\": \"westfall2016\", \"type\": \"article\", \"title\": \"Statistically Controlling for Confounding Constructs Is Harder than You Think\", \"authors\": \"Westfall, Jacob and Yarkoni, Tal\", \"year\": \"2016\", \"venue\": \"PLoS ONE\"}, {\"key\": \"jerzak2026\", \"type\": \"article\", \"title\": \"Attenuation Bias with Latent Predictors\", \"authors\": \"Jerzak, Connor T. and Jessee, Stephen A.\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2507.22218\"}, {\"key\": \"embretson2000\", \"type\": \"book\", \"title\": \"Item Response Theory for Psychologists\", \"authors\": \"Embretson, Susan E. and Reise, Steven P.\", \"year\": \"2000\", \"venue\": \"\"}, {\"key\": \"thissen2001\", \"type\": \"book\", \"title\": \"Test Scoring\", \"authors\": \"Thissen, David and Wainer, Howard\", \"year\": \"2001\", \"venue\": \"\"}, {\"key\": \"barton1981\", \"type\": \"article\", \"title\": \"An Upper Asymptote for the Three-Parameter Logistic Item-Response Model\", \"authors\": \"Barton, Mark A. and Lord, Frederic M.\", \"year\": \"1981\", \"venue\": \"ETS Research Report Series\"}, {\"key\": \"culpepper2016\", \"type\": \"article\", \"title\": \"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\", \"authors\": \"Culpepper, Steven Andrew\", \"year\": \"2016\", \"venue\": \"Psychometrika\"}, {\"key\": \"liao2012\", \"type\": \"article\", \"title\": \"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Respons...\", \"authors\": \"Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang\", \"year\": \"2012\", \"venue\": \"Social Behavior and Personality\"}], \"tex_citations\": [{\"key\": \"chang2025benchmarking\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"yang2026rl\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"dong2026dose\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"wang2025fragility\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"rao2026silicon\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"duan2025minkpp\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"oren2024proving\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"dekoninck2024constat\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"wust2025selfcritique\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"xu2025kds\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"gu2026psnirt\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"polo2026growing\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"lyu2025atlas\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"lalor2024irt\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"polo2024tinybenchmarks\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"zhuang2025hibayes\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"yang2024inference\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"han2026probing\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"li2025dcr\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"xu2025emperor\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"zhang2025forget\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"white2024livebench\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"polo2024tinybenchmarks\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"eckerly2017\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"sinharay2017\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"deboeck2004\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"adams1997\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"mislevy1986\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"cormack2009\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"chang2025benchmarking\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"duan2025minkpp\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"oren2024proving\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"dekoninck2024constat\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wust2025selfcritique\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"xu2025kds\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wang2025fragility\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"wust2025selfcritique\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citep\"}, {\"key\": \"dong2026dose\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"citet\"}, {\"key\": \"yang2026rl\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"citet\"}, {\"key\": \"zhang2025forget\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"citet\"}, {\"key\": \"xu2025emperor\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"white2024livebench\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"yang2024inference\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"li2025dcr\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"rao2026silicon\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"guo2017calibration\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"citep\"}, {\"key\": \"lalor2024irt\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"gu2026psnirt\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"polo2026growing\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"lyu2025atlas\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"polo2024tinybenchmarks\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"zhuang2025hibayes\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"han2026probing\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"angelopoulos2023conformal\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"citep\"}, {\"key\": \"eckerly2017\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"sinharay2017\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"deboeck2004\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"adams1997\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"mislevy1986\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"holland1993dif\", \"file\": \"related_work.tex\", \"line\": 34, \"command\": \"citep\"}, {\"key\": \"thissen1993dif\", \"file\": \"related_work.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"zumbo1999dif\", \"file\": \"related_work.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"duan2025minkpp\", \"file\": \"method.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"dekoninck2024constat\", \"file\": \"method.tex\", \"line\": 18, \"command\": \"citep\"}, {\"key\": \"wust2025selfcritique\", \"file\": \"method.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"wang2025fragility\", \"file\": \"method.tex\", \"line\": 25, \"command\": \"citet\"}, {\"key\": \"cormack2009\", \"file\": \"method.tex\", \"line\": 28, \"command\": \"citep\"}, {\"key\": \"xu2025kds\", \"file\": \"method.tex\", \"line\": 35, \"command\": \"citep\"}, {\"key\": \"lord1980\", \"file\": \"method.tex\", \"line\": 41, \"command\": \"citep\"}, {\"key\": \"eckerly2017\", \"file\": \"method.tex\", \"line\": 71, \"command\": \"citep\"}, {\"key\": \"sinharay2017\", \"file\": \"method.tex\", \"line\": 71, \"command\": \"citep\"}, {\"key\": \"mislevy1986\", \"file\": \"method.tex\", \"line\": 73, \"command\": \"citep\"}, {\"key\": \"sanmartin2009\", \"file\": \"method.tex\", \"line\": 73, \"command\": \"citep\"}, {\"key\": \"sinharay2017\", \"file\": \"method.tex\", \"line\": 75, \"command\": \"citep\"}, {\"key\": \"deboeck2004\", \"file\": \"method.tex\", \"line\": 75, \"command\": \"citep\"}, {\"key\": \"maris2009\", \"file\": \"method.tex\", \"line\": 75, \"command\": \"citep\"}, {\"key\": \"hoffman2014\", \"file\": \"method.tex\", \"line\": 82, \"command\": \"citep\"}, {\"key\": \"carpenter2017\", \"file\": \"method.tex\", \"line\": 82, \"command\": \"citep\"}, {\"key\": \"sanmartin2009\", \"file\": \"method.tex\", \"line\": 85, \"command\": \"citep\"}, {\"key\": \"polo2026growing\", \"file\": \"method.tex\", \"line\": 88, \"command\": \"citep\"}, {\"key\": \"talts2018sbc\", \"file\": \"method.tex\", \"line\": 88, \"command\": \"citep\"}, {\"key\": \"ulitzsch2022\", \"file\": \"method.tex\", \"line\": 88, \"command\": \"citep\"}, {\"key\": \"hendrycks2021mmlu\", \"file\": \"experiments.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"cobbe2021gsm8k\", \"file\": \"experiments.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"clark2018arc\", \"file\": \"experiments.tex\", \"line\": 15, \"command\": \"citep\"}, {\"key\": \"chen2021humaneval\", \"file\": \"experiments.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"yang2026rl\", \"file\": \"experiments.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"carpenter2017\", \"file\": \"experiments.tex\", \"line\": 37, \"command\": \"citep\"}, {\"key\": \"hoffman2014\", \"file\": \"experiments.tex\", \"line\": 37, \"command\": \"citep\"}, {\"key\": \"gu2026psnirt\", \"file\": \"experiments.tex\", \"line\": 46, \"command\": \"citep\"}, {\"key\": \"polo2026growing\", \"file\": \"experiments.tex\", \"line\": 46, \"command\": \"citep\"}, {\"key\": \"xu2025emperor\", \"file\": \"experiments.tex\", \"line\": 48, \"command\": \"citet\"}, {\"key\": \"li2025dcr\", \"file\": \"experiments.tex\", \"line\": 49, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"lord1980\", \"title\": \"Applications of Item Response Theory to Practical Testing Problems\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Applications of Item Response Theory To Practical Testing Problems\", \"matched_year\": \"2012\", \"mismatch_fields\": [\"year: bib=1980 vs api=2012\"], \"note\": \"\"}, {\"key\": \"eckerly2017\", \"title\": \"Detecting Item Compromise in the Context of Item Response Theory\", \"status\": \"not_found\", \"confidence\": 0.301, \"matched_title\": \"SPIRIT 2013 explanation and elaboration: guidance for protocols of clinical trials\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"sinharay2017\", \"title\": \"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deboeck2004\", \"title\": \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\", \"matched_year\": \"2005\", \"mismatch_fields\": [\"first_author: bib=de boeck vs api=lenth\"], \"note\": \"\"}, {\"key\": \"adams1997\", \"title\": \"The Multidimensional Random Coefficients Multinomial Logit Model\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Multidimensional Random Coefficients Multinomial Logit Model\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mislevy1986\", \"title\": \"Bayes Modal Estimation in Item Response Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Bayes Modal Estimation in Item Response Models\", \"matched_year\": \"1986\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sanmartin2009\", \"title\": \"Consequential Validity of Item Response Theory Models for Measuring Latent Constructs\", \"status\": \"not_found\", \"confidence\": 0.419, \"matched_title\": \"Knowledge of the Firm and the Evolutionary Theory of the Multinational Corporation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"maris2009\", \"title\": \"On Interpreting the Model Parameters for the Three Parameter Logistic Model\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Interpreting the Model Parameters for the Three Parameter Logistic Model\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cormack2009\", \"title\": \"Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reciprocal rank fusion outperforms condorcet and individual rank learning methods\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hoffman2014\", \"title\": \"The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The No-U-turn sampler: adaptively setting path lengths in Hamiltonian Monte Carlo\", \"matched_year\": \"2014\", \"mismatch_fields\": [\"first_author: bib=hoffman vs api=homan\"], \"note\": \"\"}, {\"key\": \"carpenter2017\", \"title\": \"Stan: A Probabilistic Programming Language\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Stan: A Probabilistic Programming Language\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"talts2018sbc\", \"title\": \"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ulitzsch2022\", \"title\": \"Automatic Differentiation Variational Inference for Item Response Theory Models\", \"status\": \"not_found\", \"confidence\": 0.272, \"matched_title\": \"Partial Least Squares Structural Equation Modeling (PLS-SEM) Using R\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.27 below threshold 0.82\"}, {\"key\": \"duan2025minkpp\", \"title\": \"Min-K\\\\%++: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.375, \"matched_title\": \"Slingshot: cell lineage and pseudotime inference for single-cell transcriptomics\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"dekoninck2024constat\", \"title\": \"ConStat: Performance-Based Contamination Detection in Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"ConStat: Performance-Based Contamination Detection in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=de koninck vs api=dekoninck\"], \"note\": \"\"}, {\"key\": \"wust2025selfcritique\", \"title\": \"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations\", \"status\": \"not_found\", \"confidence\": 0.309, \"matched_title\": \"Challenges and Applications of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"xu2025kds\", \"title\": \"Knowledge Distillation Signatures for Efficient Contamination Detection\", \"status\": \"not_found\", \"confidence\": 0.341, \"matched_title\": \"Natural Products for Drug Discovery in the 21st Century: Innovations for Novel Drug Discovery\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"oren2024proving\", \"title\": \"Proving Test Set Contamination in Black Box Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Proving Test Set Contamination in Black Box Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xu2025emperor\", \"title\": \"The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.267, \"matched_title\": \"How Do Households Respond to Unreliable Water Supplies? A Systematic Review\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.27 below threshold 0.82\"}, {\"key\": \"dong2026dose\", \"title\": \"Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales\", \"status\": \"not_found\", \"confidence\": 0.337, \"matched_title\": \"Interventions to improve antibiotic prescribing practices for hospital inpatients\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"yang2026rl\", \"title\": \"Reinforcement Learning Amplifies Contamination in LLM Benchmark Evaluation\", \"status\": \"not_found\", \"confidence\": 0.333, \"matched_title\": \"Ethical and regulatory challenges of large language models in medicine\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"wang2025fragility\", \"title\": \"On the Fragility of Benchmark Evaluations for Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.509, \"matched_title\": \"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.51 below threshold 0.82\"}, {\"key\": \"zhang2025forget\", \"title\": \"How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.463, \"matched_title\": \"A Survey of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.46 below threshold 0.82\"}, {\"key\": \"gu2026psnirt\", \"title\": \"PSN-IRT: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory\", \"status\": \"not_found\", \"confidence\": 0.37, \"matched_title\": \"INDRA: Iterative Difficulty Refinement Attention for MCQ Difficulty Estimation for Indic Languages\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.37 below threshold 0.82\"}, {\"key\": \"polo2026growing\", \"title\": \"Growing Pains: Understanding the Limitations and Potential of IRT for LLM Evaluation at Scale\", \"status\": \"not_found\", \"confidence\": 0.368, \"matched_title\": \"Safety psychology and the ergonomics of commercial kitchens\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.37 below threshold 0.82\"}, {\"key\": \"lyu2025atlas\", \"title\": \"ATLAS: Adaptive Testing via Latent Ability Scoring for Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.306, \"matched_title\": \"Dictionary learning for integrative, multimodal and scalable single-cell analysis\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"zhuang2025hibayes\", \"title\": \"HiBayES: Hierarchical Bayesian Evaluation System for Language Models\", \"status\": \"not_found\", \"confidence\": 0.622, \"matched_title\": \"HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.62 below threshold 0.82\"}, {\"key\": \"lalor2024irt\", \"title\": \"Benchmarking Large Language Models with Item Response Theory\", \"status\": \"not_found\", \"confidence\": 0.359, \"matched_title\": \"Partial Least Squares Structural Equation Modeling (PLS-SEM) Using R\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.36 below threshold 0.82\"}, {\"key\": \"li2025dcr\", \"title\": \"DCR: Decontaminated Calibration and Ranking for Benchmark Evaluation\", \"status\": \"not_found\", \"confidence\": 0.273, \"matched_title\": \"Synthetic Data Beyond Generative Models: A Comprehensive Survey of How, Why, and Where\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.27 below threshold 0.82\"}, {\"key\": \"yang2024inference\", \"title\": \"Inference-Time Decontamination of Large Language Models for Benchmark Evaluation\", \"status\": \"not_found\", \"confidence\": 0.74, \"matched_title\": \"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.74 below threshold 0.82\"}, {\"key\": \"rao2026silicon\", \"title\": \"The Silicon Bureaucracy: Evaluating the Evaluators in LLM Benchmarking\", \"status\": \"not_found\", \"confidence\": 0.516, \"matched_title\": \"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.52 below threshold 0.82\"}, {\"key\": \"hendrycks2021mmlu\", \"title\": \"Measuring Massive Multitask Language Understanding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring Massive Multitask Language Understanding\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021gsm8k\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"clark2018arc\", \"title\": \"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2021humaneval\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Evaluating Large Language Models Trained on Code\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chang2025benchmarking\", \"title\": \"A Survey on Evaluation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on Evaluation of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"white2024livebench\", \"title\": \"LiveBench: A Challenging, Contamination-Free LLM Benchmark\", \"status\": \"not_found\", \"confidence\": 0.284, \"matched_title\": \"Racial bias in AI-mediated psychiatric diagnosis and treatment: a qualitative comparison of four large language models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.28 below threshold 0.82\"}, {\"key\": \"polo2024tinybenchmarks\", \"title\": \"TinyBenchmarks: Evaluating LLMs with Fewer Examples\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"tinyBenchmarks: evaluating LLMs with fewer examples\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"han2026probing\", \"title\": \"Targeted Probing for Contamination Effects in Large Language Model Evaluations\", \"status\": \"not_found\", \"confidence\": 0.344, \"matched_title\": \"The brain basis of emotion: A meta-analytic review\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"holland1993dif\", \"title\": \"Differential Item Functioning\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Differential Item Functioning\", \"matched_year\": \"2009\", \"mismatch_fields\": [\"year: bib=1993 vs api=2009\", \"first_author: bib=holland vs api=osterlind\"], \"note\": \"\"}, {\"key\": \"thissen1993dif\", \"title\": \"Detection of Differential Item Functioning Using the Parameters of Item Response Models\", \"status\": \"verified\", \"confidence\": 0.994, \"matched_title\": \"Detection of differential item functioning using the parameters of item response models.\", \"matched_year\": \"1993\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zumbo1999dif\", \"title\": \"A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores\", \"status\": \"not_found\", \"confidence\": 0.306, \"matched_title\": \"A Multidimensional Tool Based on the eHealth Literacy Framework: Development and Initial Validity Testing of the eHealth Literacy Questionnaire (eHLQ)\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"angelopoulos2023conformal\", \"title\": \"Conformal Prediction: A Gentle Introduction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Conformal Prediction: A Gentle Introduction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pruthi2020tracin\", \"title\": \"Estimating Training Data Influence by Tracing Gradient Descent\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Estimating Training Data Influence by Tracing Gradient Descent\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"park2023trak\", \"title\": \"TRAK: Attributing Model Behavior at Scale\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TRAK: Attributing Model Behavior at Scale\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reckase2009mirt\", \"title\": \"Multidimensional Item Response Theory\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multidimensional Item Response Theory\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sanmartin2015\", \"title\": \"On the Unidentifiability of the Fixed-Effects 3PL Model\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"On the Unidentifiability of the Fixed-Effects 3PL Model\", \"matched_year\": \"2014\", \"mismatch_fields\": [\"first_author: bib=san mart\\\\'in vs api=martı́n\"], \"note\": \"\"}, {\"key\": \"mislevy1987\", \"title\": \"Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"EXPLOITING AUXILIARY INFORMATION ABOUT EXAMINEES IN THE ESTIMATION OF ITEM PARAMETERS\", \"matched_year\": \"1986\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wainer2007testlet\", \"title\": \"Testlet Response Theory and Its Applications\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Testlet Response Theory and Its Applications\", \"matched_year\": \"2007\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"carroll2006\", \"title\": \"Measurement Error in Nonlinear Models: A Modern Perspective\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measurement error in nonlinear models: a modern perspective\", \"matched_year\": \"2006\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fuller1987\", \"title\": \"Measurement Error Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Measurement Error Models\", \"matched_year\": \"1988\", \"mismatch_fields\": [\"first_author: bib=fuller vs api=stefanski\"], \"note\": \"\"}, {\"key\": \"stefanski1985\", \"title\": \"Covariate Measurement Error in Logistic Regression\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Covariate Measurement Error in Logistic Regression\", \"matched_year\": \"1985\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"battauz2011\", \"title\": \"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"westfall2016\", \"title\": \"Statistically Controlling for Confounding Constructs Is Harder than You Think\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Statistically Controlling for Confounding Constructs Is Harder than You Think\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jerzak2026\", \"title\": \"Attenuation Bias with Latent Predictors\", \"status\": \"not_found\", \"confidence\": 0.379, \"matched_title\": \"Embedding IRT in Structural Equation Models: A Comparison With Regression Based on IRT Scores\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"embretson2000\", \"title\": \"Item Response Theory for Psychologists\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Item response theory for psychologists\", \"matched_year\": \"2000\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thissen2001\", \"title\": \"Test Scoring\", \"status\": \"not_found\", \"confidence\": 0.476, \"matched_title\": \"The Black-White Test Score Gap\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.48 below threshold 0.82\"}, {\"key\": \"barton1981\", \"title\": \"An Upper Asymptote for the Three-Parameter Logistic Item-Response Model\", \"status\": \"verified\", \"confidence\": 0.965, \"matched_title\": \"AN UPPER ASYMPTOTE FOR THE THREE‐PARAMETER LOGISTIC ITEM‐RESPONSE MODEL*\", \"matched_year\": \"1981\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culpepper2016\", \"title\": \"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liao2012\", \"title\": \"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67896969-512c-4df0-9c7f-e89f9fdc87ca",
  "isSidechain": false,
  "promptId": "4e3fc52f-dc1e-44b5-9d0f-d389164f223c",
  "type": "user",
  "uuid": "74092b17-eb1e-46e4-b665-3b9529b88b0a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 61, \\\"total_citations\\\": 93, \\\"unique_cited_keys\\\": 44, \\\"orphan_bib\\\": 17, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 30, \\\"online_not_found\\\": 24, \\\"online_mismatch\\\": 7}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"barton1981\\\", \\\"battauz2011\\\", \\\"carroll2006\\\", \\\"culpepper2016\\\", \\\"embretson2000\\\", \\\"fuller1987\\\", \\\"jerzak2026\\\", \\\"liao2012\\\", \\\"mislevy1987\\\", \\\"park2023trak\\\", \\\"pruthi2020tracin\\\", \\\"reckase2009mirt\\\", \\\"sanmartin2015\\\", \\\"stefanski1985\\\", \\\"thissen2001\\\", \\\"wainer2007testlet\\\", \\\"westfall2016\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 17, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"lord1980\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Applications of Item Response Theory to Practical Testing Problems\\\", \\\"authors\\\": \\\"Lord, Frederic M.\\\", \\\"year\\\": \\\"1980\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"eckerly2017\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Detecting Item Compromise in the Context of Item Response Theory\\\", \\\"authors\\\": \\\"Eckerly, Carol\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Applied Psychological Measurement\\\"}, {\\\"key\\\": \\\"sinharay2017\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\\\", \\\"authors\\\": \\\"Sinharay, Sandip\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Journal of Educational and Behavioral Statistics\\\"}, {\\\"key\\\": \\\"deboeck2004\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\\\", \\\"authors\\\": \\\"De Boeck, Paul and Wilson, Mark\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"adams1997\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Multidimensional Random Coefficients Multinomial Logit Model\\\", \\\"authors\\\": \\\"Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung\\\", \\\"year\\\": \\\"1997\\\", \\\"venue\\\": \\\"Applied Psychological Measurement\\\"}, {\\\"key\\\": \\\"mislevy1986\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Bayes Modal Estimation in Item Response Models\\\", \\\"authors\\\": \\\"Mislevy, Robert J.\\\", \\\"year\\\": \\\"1986\\\", \\\"venue\\\": \\\"Psychometrika\\\"}, {\\\"key\\\": \\\"sanmartin2009\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consequential Validity of Item Response Theory Models for Measuring Latent Constructs\\\", \\\"authors\\\": \\\"San Mart\\\\\\\\'in, Ernesto and Del Pino, Guido and De Boeck, Paul\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Psychometrika\\\"}, {\\\"key\\\": \\\"maris2009\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"On Interpreting the Model Parameters for the Three Parameter Logistic Model\\\", \\\"authors\\\": \\\"Maris, Gunter and Bechger, Timo\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Measurement\\\"}, {\\\"key\\\": \\\"cormack2009\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods\\\", \\\"authors\\\": \\\"Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Proceedings of the 32nd International ACM SIGIR Conference on Research and Devel...\\\"}, {\\\"key\\\": \\\"hoffman2014\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo\\\", \\\"authors\\\": \\\"Hoffman, Matthew D. and Gelman, Andrew\\\", \\\"year\\\": \\\"2014\\\", \\\"venue\\\": \\\"Journal of Machine Learning Research\\\"}, {\\\"key\\\": \\\"carpenter2017\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Stan: A Probabilistic Programming Language\\\", \\\"authors\\\": \\\"Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Go...\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Journal of Statistical Software\\\"}, {\\\"key\\\": \\\"talts2018sbc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\\\", \\\"authors\\\": \\\"Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gel...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"ulitzsch2022\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Automatic Differentiation Variational Inference for Item Response Theory Models\\\", \\\"authors\\\": \\\"Ulitzsch, Esther and Nestler, Steffen\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"British Journal of Mathematical and Statistical Psychology\\\"}, {\\\"key\\\": \\\"duan2025minkpp\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Min-K\\\\\\\\%++: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models\\\", \\\"authors\\\": \\\"Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 13th International Conference on Learning Representations (IC...\\\"}, {\\\"key\\\": \\\"dekoninck2024constat\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\", \\\"authors\\\": \\\"De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 37 (NeurIPS)\\\"}, {\\\"key\\\": \\\"wust2025selfcritique\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations\\\", \\\"authors\\\": \\\"W\\\\\\\\\\\\\\\"ust, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"xu2025kds\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Knowledge Distillation Signatures for Efficient Contamination Detection\\\", \\\"authors\\\": \\\"Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 42nd International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"oren2024proving\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Proving Test Set Contamination in Black Box Language Models\\\", \\\"authors\\\": \\\"Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal an...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 12th International Conference on Learning Representations (IC...\\\"}, {\\\"key\\\": \\\"xu2025emperor\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models\\\", \\\"authors\\\": \\\"Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 42nd International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"dong2026dose\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales\\\", \\\"authors\\\": \\\"Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"yang2026rl\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Reinforcement Learning Amplifies Contamination in LLM Benchmark Evaluation\\\", \\\"authors\\\": \\\"Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"wang2025fragility\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"On the Fragility of Benchmark Evaluations for Large Language Models\\\", \\\"authors\\\": \\\"Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"zhang2025forget\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models\\\", \\\"authors\\\": \\\"Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 42nd International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"gu2026psnirt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"PSN-IRT: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory\\\", \\\"authors\\\": \\\"Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Proceedings of the 40th AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"polo2026growing\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Growing Pains: Understanding the Limitations and Potential of IRT for LLM Evaluation at Scale\\\", \\\"authors\\\": \\\"Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen,...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"lyu2025atlas\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ATLAS: Adaptive Testing via Latent Ability Scoring for Large Language Models\\\", \\\"authors\\\": \\\"Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"zhuang2025hibayes\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"HiBayES: Hierarchical Bayesian Evaluation System for Language Models\\\", \\\"authors\\\": \\\"Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"lalor2024irt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Benchmarking Large Language Models with Item Response Theory\\\", \\\"authors\\\": \\\"Lalor, John P. and Yang, Yi and Smith, Noah A.\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 38th AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"li2025dcr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DCR: Decontaminated Calibration and Ranking for Benchmark Evaluation\\\", \\\"authors\\\": \\\"Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"yang2024inference\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Inference-Time Decontamination of Large Language Models for Benchmark Evaluation\\\", \\\"authors\\\": \\\"Yang, Shuo and Wei, Xin and Shi, Weicheng\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the 2024 Conference on Empirical Methods in Natural Language Process...\\\"}, {\\\"key\\\": \\\"rao2026silicon\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Silicon Bureaucracy: Evaluating the Evaluators in LLM Benchmarking\\\", \\\"authors\\\": \\\"Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"hendrycks2021mmlu\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Measuring Massive Multitask Language Understanding\\\", \\\"authors\\\": \\\"Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, M...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 9th International Conference on Learning Representations (ICL...\\\"}, {\\\"key\\\": \\\"cobbe2021gsm8k\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"clark2018arc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\\\", \\\"authors\\\": \\\"Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal,...\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"chen2021humaneval\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"authors\\\": \\\"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"chang2025benchmarking\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey on Evaluation of Large Language Models\\\", \\\"authors\\\": \\\"Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zh...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"white2024livebench\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LiveBench: A Challenging, Contamination-Free LLM Benchmark\\\", \\\"authors\\\": \\\"White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Ben...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint\\\"}, {\\\"key\\\": \\\"polo2024tinybenchmarks\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"TinyBenchmarks: Evaluating LLMs with Fewer Examples\\\", \\\"authors\\\": \\\"Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, G...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 41st International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"han2026probing\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Targeted Probing for Contamination Effects in Large Language Model Evaluations\\\", \\\"authors\\\": \\\"Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Findings of the 2026 Conference of the European Chapter of the Association for C...\\\"}, {\\\"key\\\": \\\"holland1993dif\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Differential Item Functioning\\\", \\\"authors\\\": \\\"Holland, Paul W. and Wainer, Howard\\\", \\\"year\\\": \\\"1993\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"thissen1993dif\\\", \\\"type\\\": \\\"incollection\\\", \\\"title\\\": \\\"Detection of Differential Item Functioning Using the Parameters of Item Response Models\\\", \\\"authors\\\": \\\"Thissen, David and Steinberg, Lynne and Wainer, Howard\\\", \\\"year\\\": \\\"1993\\\", \\\"venue\\\": \\\"Differential Item Functioning\\\"}, {\\\"key\\\": \\\"zumbo1999dif\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary F...\\\", \\\"authors\\\": \\\"Zumbo, Bruno D.\\\", \\\"year\\\": \\\"1999\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the 34th International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"angelopoulos2023conformal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Conformal Prediction: A Gentle Introduction\\\", \\\"authors\\\": \\\"Angelopoulos, Anastasios N. and Bates, Stephen\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Foundations and Trends in Machine Learning\\\"}, {\\\"key\\\": \\\"pruthi2020tracin\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Estimating Training Data Influence by Tracing Gradient Descent\\\", \\\"authors\\\": \\\"Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems 33 (NeurIPS)\\\"}, {\\\"key\\\": \\\"park2023trak\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"TRAK: Attributing Model Behavior at Scale\\\", \\\"authors\\\": \\\"Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 40th International Conference on Machine Learning (ICML)\\\"}, {\\\"key\\\": \\\"reckase2009mirt\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Multidimensional Item Response Theory\\\", \\\"authors\\\": \\\"Reckase, Mark D.\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"sanmartin2015\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"On the Unidentifiability of the Fixed-Effects 3PL Model\\\", \\\"authors\\\": \\\"San Mart\\\\\\\\'in, Ernesto and Gonz\\\\\\\\'alez, Jorge and Tuerlinckx, Francis\\\", \\\"year\\\": \\\"2015\\\", \\\"venue\\\": \\\"Psychometrika\\\"}, {\\\"key\\\": \\\"mislevy1987\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters\\\", \\\"authors\\\": \\\"Mislevy, Robert J.\\\", \\\"year\\\": \\\"1987\\\", \\\"venue\\\": \\\"Applied Psychological Measurement\\\"}, {\\\"key\\\": \\\"wainer2007testlet\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Testlet Response Theory and Its Applications\\\", \\\"authors\\\": \\\"Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui\\\", \\\"year\\\": \\\"2007\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"carroll2006\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Measurement Error in Nonlinear Models: A Modern Perspective\\\", \\\"authors\\\": \\\"Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu...\\\", \\\"year\\\": \\\"2006\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"fuller1987\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Measurement Error Models\\\", \\\"authors\\\": \\\"Fuller, Wayne A.\\\", \\\"year\\\": \\\"1987\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"stefanski1985\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Covariate Measurement Error in Logistic Regression\\\", \\\"authors\\\": \\\"Stefanski, Leonard A. and Carroll, Raymond J.\\\", \\\"year\\\": \\\"1985\\\", \\\"venue\\\": \\\"Annals of Statistics\\\"}, {\\\"key\\\": \\\"battauz2011\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\\\", \\\"authors\\\": \\\"Battauz, Michela and Bellio, Ruggero\\\", \\\"year\\\": \\\"2011\\\", \\\"venue\\\": \\\"Psychometrika\\\"}, {\\\"key\\\": \\\"westfall2016\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Statistically Controlling for Confounding Constructs Is Harder than You Think\\\", \\\"authors\\\": \\\"Westfall, Jacob and Yarkoni, Tal\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"PLoS ONE\\\"}, {\\\"key\\\": \\\"jerzak2026\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Attenuation Bias with Latent Predictors\\\", \\\"authors\\\": \\\"Jerzak, Connor T. and Jessee, Stephen A.\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2507.22218\\\"}, {\\\"key\\\": \\\"embretson2000\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Item Response Theory for Psychologists\\\", \\\"authors\\\": \\\"Embretson, Susan E. and Reise, Steven P.\\\", \\\"year\\\": \\\"2000\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"thissen2001\\\", \\\"type\\\": \\\"book\\\", \\\"title\\\": \\\"Test Scoring\\\", \\\"authors\\\": \\\"Thissen, David and Wainer, Howard\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"barton1981\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"An Upper Asymptote for the Three-Parameter Logistic Item-Response Model\\\", \\\"authors\\\": \\\"Barton, Mark A. and Lord, Frederic M.\\\", \\\"year\\\": \\\"1981\\\", \\\"venue\\\": \\\"ETS Research Report Series\\\"}, {\\\"key\\\": \\\"culpepper2016\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\\\", \\\"authors\\\": \\\"Culpepper, Steven Andrew\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"Psychometrika\\\"}, {\\\"key\\\": \\\"liao2012\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Respons...\\\", \\\"authors\\\": \\\"Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang\\\", \\\"year\\\": \\\"2012\\\", \\\"venue\\\": \\\"Social Behavior and Personality\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"chang2025benchmarking\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yang2026rl\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dong2026dose\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025fragility\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"rao2026silicon\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"duan2025minkpp\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"oren2024proving\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dekoninck2024constat\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wust2025selfcritique\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xu2025kds\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gu2026psnirt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"polo2026growing\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"lyu2025atlas\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lalor2024irt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"polo2024tinybenchmarks\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhuang2025hibayes\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yang2024inference\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"han2026probing\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2025dcr\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xu2025emperor\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zhang2025forget\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"white2024livebench\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"polo2024tinybenchmarks\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"eckerly2017\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"sinharay2017\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deboeck2004\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"adams1997\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mislevy1986\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cormack2009\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chang2025benchmarking\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"duan2025minkpp\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"oren2024proving\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dekoninck2024constat\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wust2025selfcritique\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xu2025kds\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025fragility\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wust2025selfcritique\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"dong2026dose\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"yang2026rl\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zhang2025forget\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"xu2025emperor\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"white2024livebench\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yang2024inference\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"li2025dcr\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"rao2026silicon\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lalor2024irt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"gu2026psnirt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"polo2026growing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"lyu2025atlas\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"polo2024tinybenchmarks\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"zhuang2025hibayes\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"han2026probing\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"angelopoulos2023conformal\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"eckerly2017\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"sinharay2017\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"deboeck2004\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"adams1997\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mislevy1986\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"holland1993dif\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"thissen1993dif\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"zumbo1999dif\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"duan2025minkpp\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dekoninck2024constat\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wust2025selfcritique\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"wang2025fragility\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"cormack2009\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xu2025kds\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"lord1980\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"eckerly2017\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 71, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"sinharay2017\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 71, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"mislevy1986\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 73, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"sanmartin2009\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 73, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"sinharay2017\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 75, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"deboeck2004\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 75, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"maris2009\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 75, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hoffman2014\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"carpenter2017\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 82, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"sanmartin2009\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 85, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"polo2026growing\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 88, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"talts2018sbc\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 88, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"ulitzsch2022\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 88, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hendrycks2021mmlu\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"cobbe2021gsm8k\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 14, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"clark2018arc\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"chen2021humaneval\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"yang2026rl\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"carpenter2017\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"hoffman2014\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"gu2026psnirt\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 46, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"polo2026growing\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 46, \\\"command\\\": \\\"citep\\\"}, {\\\"key\\\": \\\"xu2025emperor\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 48, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025dcr\\\", \\\"file\\\": \\\"experiments.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"citet\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"lord1980\\\", \\\"title\\\": \\\"Applications of Item Response Theory to Practical Testing Problems\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Applications of Item Response Theory To Practical Testing Problems\\\", \\\"matched_year\\\": \\\"2012\\\", \\\"mismatch_fields\\\": [\\\"year: bib=1980 vs api=2012\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"eckerly2017\\\", \\\"title\\\": \\\"Detecting Item Compromise in the Context of Item Response Theory\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.301, \\\"matched_title\\\": \\\"SPIRIT 2013 explanation and elaboration: guidance for protocols of clinical trials\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\"}, {\\\"key\\\": \\\"sinharay2017\\\", \\\"title\\\": \\\"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"deboeck2004\\\", \\\"title\\\": \\\"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\\\", \\\"matched_year\\\": \\\"2005\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=de boeck vs api=lenth\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"adams1997\\\", \\\"title\\\": \\\"The Multidimensional Random Coefficients Multinomial Logit Model\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Multidimensional Random Coefficients Multinomial Logit Model\\\", \\\"matched_year\\\": \\\"1997\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mislevy1986\\\", \\\"title\\\": \\\"Bayes Modal Estimation in Item Response Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Bayes Modal Estimation in Item Response Models\\\", \\\"matched_year\\\": \\\"1986\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sanmartin2009\\\", \\\"title\\\": \\\"Consequential Validity of Item Response Theory Models for Measuring Latent Constructs\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.419, \\\"matched_title\\\": \\\"Knowledge of the Firm and the Evolutionary Theory of the Multinational Corporation\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.42 below threshold 0.82\\\"}, {\\\"key\\\": \\\"maris2009\\\", \\\"title\\\": \\\"On Interpreting the Model Parameters for the Three Parameter Logistic Model\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Interpreting the Model Parameters for the Three Parameter Logistic Model\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cormack2009\\\", \\\"title\\\": \\\"Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reciprocal rank fusion outperforms condorcet and individual rank learning methods\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hoffman2014\\\", \\\"title\\\": \\\"The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The No-U-turn sampler: adaptively setting path lengths in Hamiltonian Monte Carlo\\\", \\\"matched_year\\\": \\\"2014\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=hoffman vs api=homan\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"carpenter2017\\\", \\\"title\\\": \\\"Stan: A Probabilistic Programming Language\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Stan: A Probabilistic Programming Language\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"talts2018sbc\\\", \\\"title\\\": \\\"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ulitzsch2022\\\", \\\"title\\\": \\\"Automatic Differentiation Variational Inference for Item Response Theory Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.272, \\\"matched_title\\\": \\\"Partial Least Squares Structural Equation Modeling (PLS-SEM) Using R\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.27 below threshold 0.82\\\"}, {\\\"key\\\": \\\"duan2025minkpp\\\", \\\"title\\\": \\\"Min-K\\\\\\\\%++: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.375, \\\"matched_title\\\": \\\"Slingshot: cell lineage and pseudotime inference for single-cell transcriptomics\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.38 below threshold 0.82\\\"}, {\\\"key\\\": \\\"dekoninck2024constat\\\", \\\"title\\\": \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=de koninck vs api=dekoninck\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wust2025selfcritique\\\", \\\"title\\\": \\\"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.309, \\\"matched_title\\\": \\\"Challenges and Applications of Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.31 below threshold 0.82\\\"}, {\\\"key\\\": \\\"xu2025kds\\\", \\\"title\\\": \\\"Knowledge Distillation Signatures for Efficient Contamination Detection\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.341, \\\"matched_title\\\": \\\"Natural Products for Drug Discovery in the 21st Century: Innovations for Novel Drug Discovery\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"oren2024proving\\\", \\\"title\\\": \\\"Proving Test Set Contamination in Black Box Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Proving Test Set Contamination in Black Box Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xu2025emperor\\\", \\\"title\\\": \\\"The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.267, \\\"matched_title\\\": \\\"How Do Households Respond to Unreliable Water Supplies? A Systematic Review\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.27 below threshold 0.82\\\"}, {\\\"key\\\": \\\"dong2026dose\\\", \\\"title\\\": \\\"Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.337, \\\"matched_title\\\": \\\"Interventions to improve antibiotic prescribing practices for hospital inpatients\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"yang2026rl\\\", \\\"title\\\": \\\"Reinforcement Learning Amplifies Contamination in LLM Benchmark Evaluation\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.333, \\\"matched_title\\\": \\\"Ethical and regulatory challenges of large language models in medicine\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.33 below threshold 0.82\\\"}, {\\\"key\\\": \\\"wang2025fragility\\\", \\\"title\\\": \\\"On the Fragility of Benchmark Evaluations for Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.509, \\\"matched_title\\\": \\\"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.51 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zhang2025forget\\\", \\\"title\\\": \\\"How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.463, \\\"matched_title\\\": \\\"A Survey of Large Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.46 below threshold 0.82\\\"}, {\\\"key\\\": \\\"gu2026psnirt\\\", \\\"title\\\": \\\"PSN-IRT: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.37, \\\"matched_title\\\": \\\"INDRA: Iterative Difficulty Refinement Attention for MCQ Difficulty Estimation for Indic Languages\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.37 below threshold 0.82\\\"}, {\\\"key\\\": \\\"polo2026growing\\\", \\\"title\\\": \\\"Growing Pains: Understanding the Limitations and Potential of IRT for LLM Evaluation at Scale\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.368, \\\"matched_title\\\": \\\"Safety psychology and the ergonomics of commercial kitchens\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.37 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lyu2025atlas\\\", \\\"title\\\": \\\"ATLAS: Adaptive Testing via Latent Ability Scoring for Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.306, \\\"matched_title\\\": \\\"Dictionary learning for integrative, multimodal and scalable single-cell analysis\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.31 below threshold 0.82\\\"}, {\\\"key\\\": \\\"zhuang2025hibayes\\\", \\\"title\\\": \\\"HiBayES: Hierarchical Bayesian Evaluation System for Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.622, \\\"matched_title\\\": \\\"HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.62 below threshold 0.82\\\"}, {\\\"key\\\": \\\"lalor2024irt\\\", \\\"title\\\": \\\"Benchmarking Large Language Models with Item Response Theory\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.359, \\\"matched_title\\\": \\\"Partial Least Squares Structural Equation Modeling (PLS-SEM) Using R\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.36 below threshold 0.82\\\"}, {\\\"key\\\": \\\"li2025dcr\\\", \\\"title\\\": \\\"DCR: Decontaminated Calibration and Ranking for Benchmark Evaluation\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.273, \\\"matched_title\\\": \\\"Synthetic Data Beyond Generative Models: A Comprehensive Survey of How, Why, and Where\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.27 below threshold 0.82\\\"}, {\\\"key\\\": \\\"yang2024inference\\\", \\\"title\\\": \\\"Inference-Time Decontamination of Large Language Models for Benchmark Evaluation\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.74, \\\"matched_title\\\": \\\"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.74 below threshold 0.82\\\"}, {\\\"key\\\": \\\"rao2026silicon\\\", \\\"title\\\": \\\"The Silicon Bureaucracy: Evaluating the Evaluators in LLM Benchmarking\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.516, \\\"matched_title\\\": \\\"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.52 below threshold 0.82\\\"}, {\\\"key\\\": \\\"hendrycks2021mmlu\\\", \\\"title\\\": \\\"Measuring Massive Multitask Language Understanding\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring Massive Multitask Language Understanding\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021gsm8k\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"clark2018arc\\\", \\\"title\\\": \\\"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2021humaneval\\\", \\\"title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Evaluating Large Language Models Trained on Code\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chang2025benchmarking\\\", \\\"title\\\": \\\"A Survey on Evaluation of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on Evaluation of Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"white2024livebench\\\", \\\"title\\\": \\\"LiveBench: A Challenging, Contamination-Free LLM Benchmark\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.284, \\\"matched_title\\\": \\\"Racial bias in AI-mediated psychiatric diagnosis and treatment: a qualitative comparison of four large language models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.28 below threshold 0.82\\\"}, {\\\"key\\\": \\\"polo2024tinybenchmarks\\\", \\\"title\\\": \\\"TinyBenchmarks: Evaluating LLMs with Fewer Examples\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"tinyBenchmarks: evaluating LLMs with fewer examples\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"han2026probing\\\", \\\"title\\\": \\\"Targeted Probing for Contamination Effects in Large Language Model Evaluations\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.344, \\\"matched_title\\\": \\\"The brain basis of emotion: A meta-analytic review\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"holland1993dif\\\", \\\"title\\\": \\\"Differential Item Functioning\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Differential Item Functioning\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [\\\"year: bib=1993 vs api=2009\\\", \\\"first_author: bib=holland vs api=osterlind\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thissen1993dif\\\", \\\"title\\\": \\\"Detection of Differential Item Functioning Using the Parameters of Item Response Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.994, \\\"matched_title\\\": \\\"Detection of differential item functioning using the parameters of item response models.\\\", \\\"matched_year\\\": \\\"1993\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zumbo1999dif\\\", \\\"title\\\": \\\"A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.306, \\\"matched_title\\\": \\\"A Multidimensional Tool Based on the eHealth Literacy Framework: Development and Initial Validity Testing of the eHealth Literacy Questionnaire (eHLQ)\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.31 below threshold 0.82\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"angelopoulos2023conformal\\\", \\\"title\\\": \\\"Conformal Prediction: A Gentle Introduction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Conformal Prediction: A Gentle Introduction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"pruthi2020tracin\\\", \\\"title\\\": \\\"Estimating Training Data Influence by Tracing Gradient Descent\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Estimating Training Data Influence by Tracing Gradient Descent\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"park2023trak\\\", \\\"title\\\": \\\"TRAK: Attributing Model Behavior at Scale\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"TRAK: Attributing Model Behavior at Scale\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"reckase2009mirt\\\", \\\"title\\\": \\\"Multidimensional Item Response Theory\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multidimensional Item Response Theory\\\", \\\"matched_year\\\": \\\"2009\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sanmartin2015\\\", \\\"title\\\": \\\"On the Unidentifiability of the Fixed-Effects 3PL Model\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On the Unidentifiability of the Fixed-Effects 3PL Model\\\", \\\"matched_year\\\": \\\"2014\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=san mart\\\\\\\\'in vs api=martı́n\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mislevy1987\\\", \\\"title\\\": \\\"Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"EXPLOITING AUXILIARY INFORMATION ABOUT EXAMINEES IN THE ESTIMATION OF ITEM PARAMETERS\\\", \\\"matched_year\\\": \\\"1986\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wainer2007testlet\\\", \\\"title\\\": \\\"Testlet Response Theory and Its Applications\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Testlet Response Theory and Its Applications\\\", \\\"matched_year\\\": \\\"2007\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"carroll2006\\\", \\\"title\\\": \\\"Measurement Error in Nonlinear Models: A Modern Perspective\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measurement error in nonlinear models: a modern perspective\\\", \\\"matched_year\\\": \\\"2006\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fuller1987\\\", \\\"title\\\": \\\"Measurement Error Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measurement Error Models\\\", \\\"matched_year\\\": \\\"1988\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=fuller vs api=stefanski\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"stefanski1985\\\", \\\"title\\\": \\\"Covariate Measurement Error in Logistic Regression\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Covariate Measurement Error in Logistic Regression\\\", \\\"matched_year\\\": \\\"1985\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"battauz2011\\\", \\\"title\\\": \\\"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\\\", \\\"matched_year\\\": \\\"2010\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"westfall2016\\\", \\\"title\\\": \\\"Statistically Controlling for Confounding Constructs Is Harder than You Think\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Statistically Controlling for Confounding Constructs Is Harder than You Think\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jerzak2026\\\", \\\"title\\\": \\\"Attenuation Bias with Latent Predictors\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.379, \\\"matched_title\\\": \\\"Embedding IRT in Structural Equation Models: A Comparison With Regression Based on IRT Scores\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.38 below threshold 0.82\\\"}, {\\\"key\\\": \\\"embretson2000\\\", \\\"title\\\": \\\"Item Response Theory for Psychologists\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Item response theory for psychologists\\\", \\\"matched_year\\\": \\\"2000\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thissen2001\\\", \\\"title\\\": \\\"Test Scoring\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.476, \\\"matched_title\\\": \\\"The Black-White Test Score Gap\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.48 below threshold 0.82\\\"}, {\\\"key\\\": \\\"barton1981\\\", \\\"title\\\": \\\"An Upper Asymptote for the Three-Parameter Logistic Item-Response Model\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 0.965, \\\"matched_title\\\": \\\"AN UPPER ASYMPTOTE FOR THE THREE‐PARAMETER LOGISTIC ITEM‐RESPONSE MODEL*\\\", \\\"matched_year\\\": \\\"1981\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culpepper2016\\\", \\\"title\\\": \\\"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"liao2012\\\", \\\"title\\\": \\\"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses\\\", \\\"matched_year\\\": \\\"2012\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 61, \"total_citations\": 93, \"unique_cited_keys\": 44, \"orphan_bib\": 17, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 30, \"online_not_found\": 24, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [\"barton1981\", \"battauz2011\", \"carroll2006\", \"culpepper2016\", \"embretson2000\", \"fuller1987\", \"jerzak2026\", \"liao2012\", \"mislevy1987\", \"park2023trak\", \"pruthi2020tracin\", \"reckase2009mirt\", \"sanmartin2015\", \"stefanski1985\", \"thissen2001\", \"wainer2007testlet\", \"westfall2016\"], \"missing_bib\": [], \"orphan_count\": 17, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"lord1980\", \"type\": \"book\", \"title\": \"Applications of Item Response Theory to Practical Testing Problems\", \"authors\": \"Lord, Frederic M.\", \"year\": \"1980\", \"venue\": \"\"}, {\"key\": \"eckerly2017\", \"type\": \"article\", \"title\": \"Detecting Item Compromise in the Context of Item Response Theory\", \"authors\": \"Eckerly, Carol\", \"year\": \"2017\", \"venue\": \"Applied Psychological Measurement\"}, {\"key\": \"sinharay2017\", \"type\": \"article\", \"title\": \"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\", \"authors\": \"Sinharay, Sandip\", \"year\": \"2017\", \"venue\": \"Journal of Educational and Behavioral Statistics\"}, {\"key\": \"deboeck2004\", \"type\": \"book\", \"title\": \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\", \"authors\": \"De Boeck, Paul and Wilson, Mark\", \"year\": \"2004\", \"venue\": \"\"}, {\"key\": \"adams1997\", \"type\": \"article\", \"title\": \"The Multidimensional Random Coefficients Multinomial Logit Model\", \"authors\": \"Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung\", \"year\": \"1997\", \"venue\": \"Applied Psychological Measurement\"}, {\"key\": \"mislevy1986\", \"type\": \"article\", \"title\": \"Bayes Modal Estimation in Item Response Models\", \"authors\": \"Mislevy, Robert J.\", \"year\": \"1986\", \"venue\": \"Psychometrika\"}, {\"key\": \"sanmartin2009\", \"type\": \"article\", \"title\": \"Consequential Validity of Item Response Theory Models for Measuring Latent Constructs\", \"authors\": \"San Mart\\\\'in, Ernesto and Del Pino, Guido and De Boeck, Paul\", \"year\": \"2009\", \"venue\": \"Psychometrika\"}, {\"key\": \"maris2009\", \"type\": \"article\", \"title\": \"On Interpreting the Model Parameters for the Three Parameter Logistic Model\", \"authors\": \"Maris, Gunter and Bechger, Timo\", \"year\": \"2009\", \"venue\": \"Measurement\"}, {\"key\": \"cormack2009\", \"type\": \"inproceedings\", \"title\": \"Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods\", \"authors\": \"Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan\", \"year\": \"2009\", \"venue\": \"Proceedings of the 32nd International ACM SIGIR Conference on Research and Devel...\"}, {\"key\": \"hoffman2014\", \"type\": \"article\", \"title\": \"The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo\", \"authors\": \"Hoffman, Matthew D. and Gelman, Andrew\", \"year\": \"2014\", \"venue\": \"Journal of Machine Learning Research\"}, {\"key\": \"carpenter2017\", \"type\": \"article\", \"title\": \"Stan: A Probabilistic Programming Language\", \"authors\": \"Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Go...\", \"year\": \"2017\", \"venue\": \"Journal of Statistical Software\"}, {\"key\": \"talts2018sbc\", \"type\": \"article\", \"title\": \"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\", \"authors\": \"Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gel...\", \"year\": \"2018\", \"venue\": \"arXiv preprint\"}, {\"key\": \"ulitzsch2022\", \"type\": \"article\", \"title\": \"Automatic Differentiation Variational Inference for Item Response Theory Models\", \"authors\": \"Ulitzsch, Esther and Nestler, Steffen\", \"year\": \"2022\", \"venue\": \"British Journal of Mathematical and Statistical Psychology\"}, {\"key\": \"duan2025minkpp\", \"type\": \"inproceedings\", \"title\": \"Min-K\\\\%++: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models\", \"authors\": \"Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai\", \"year\": \"2025\", \"venue\": \"Proceedings of the 13th International Conference on Learning Representations (IC...\"}, {\"key\": \"dekoninck2024constat\", \"type\": \"inproceedings\", \"title\": \"ConStat: Performance-Based Contamination Detection in Large Language Models\", \"authors\": \"De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems 37 (NeurIPS)\"}, {\"key\": \"wust2025selfcritique\", \"type\": \"article\", \"title\": \"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations\", \"authors\": \"W\\\\\\\"ust, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"xu2025kds\", \"type\": \"inproceedings\", \"title\": \"Knowledge Distillation Signatures for Efficient Contamination Detection\", \"authors\": \"Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning (ICML)\"}, {\"key\": \"oren2024proving\", \"type\": \"inproceedings\", \"title\": \"Proving Test Set Contamination in Black Box Language Models\", \"authors\": \"Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal an...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 12th International Conference on Learning Representations (IC...\"}, {\"key\": \"xu2025emperor\", \"type\": \"inproceedings\", \"title\": \"The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models\", \"authors\": \"Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning (ICML)\"}, {\"key\": \"dong2026dose\", \"type\": \"article\", \"title\": \"Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales\", \"authors\": \"Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"yang2026rl\", \"type\": \"article\", \"title\": \"Reinforcement Learning Amplifies Contamination in LLM Benchmark Evaluation\", \"authors\": \"Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"wang2025fragility\", \"type\": \"article\", \"title\": \"On the Fragility of Benchmark Evaluations for Large Language Models\", \"authors\": \"Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"zhang2025forget\", \"type\": \"inproceedings\", \"title\": \"How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models\", \"authors\": \"Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi\", \"year\": \"2025\", \"venue\": \"Proceedings of the 42nd International Conference on Machine Learning (ICML)\"}, {\"key\": \"gu2026psnirt\", \"type\": \"inproceedings\", \"title\": \"PSN-IRT: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory\", \"authors\": \"Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun\", \"year\": \"2026\", \"venue\": \"Proceedings of the 40th AAAI Conference on Artificial Intelligence\"}, {\"key\": \"polo2026growing\", \"type\": \"article\", \"title\": \"Growing Pains: Understanding the Limitations and Potential of IRT for LLM Evaluation at Scale\", \"authors\": \"Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen,...\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"lyu2025atlas\", \"type\": \"article\", \"title\": \"ATLAS: Adaptive Testing via Latent Ability Scoring for Large Language Models\", \"authors\": \"Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"zhuang2025hibayes\", \"type\": \"article\", \"title\": \"HiBayES: Hierarchical Bayesian Evaluation System for Language Models\", \"authors\": \"Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai\", \"year\": \"2025\", \"venue\": \"arXiv preprint\"}, {\"key\": \"lalor2024irt\", \"type\": \"inproceedings\", \"title\": \"Benchmarking Large Language Models with Item Response Theory\", \"authors\": \"Lalor, John P. and Yang, Yi and Smith, Noah A.\", \"year\": \"2024\", \"venue\": \"Proceedings of the 38th AAAI Conference on Artificial Intelligence\"}, {\"key\": \"li2025dcr\", \"type\": \"inproceedings\", \"title\": \"DCR: Decontaminated Calibration and Ranking for Benchmark Evaluation\", \"authors\": \"Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"yang2024inference\", \"type\": \"inproceedings\", \"title\": \"Inference-Time Decontamination of Large Language Models for Benchmark Evaluation\", \"authors\": \"Yang, Shuo and Wei, Xin and Shi, Weicheng\", \"year\": \"2024\", \"venue\": \"Findings of the 2024 Conference on Empirical Methods in Natural Language Process...\"}, {\"key\": \"rao2026silicon\", \"type\": \"article\", \"title\": \"The Silicon Bureaucracy: Evaluating the Evaluators in LLM Benchmarking\", \"authors\": \"Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy\", \"year\": \"2026\", \"venue\": \"arXiv preprint\"}, {\"key\": \"hendrycks2021mmlu\", \"type\": \"inproceedings\", \"title\": \"Measuring Massive Multitask Language Understanding\", \"authors\": \"Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, M...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 9th International Conference on Learning Representations (ICL...\"}, {\"key\": \"cobbe2021gsm8k\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint\"}, {\"key\": \"clark2018arc\", \"type\": \"inproceedings\", \"title\": \"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\", \"authors\": \"Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal,...\", \"year\": \"2018\", \"venue\": \"arXiv preprint\"}, {\"key\": \"chen2021humaneval\", \"type\": \"article\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"authors\": \"Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henriqu...\", \"year\": \"2021\", \"venue\": \"arXiv preprint\"}, {\"key\": \"chang2025benchmarking\", \"type\": \"inproceedings\", \"title\": \"A Survey on Evaluation of Large Language Models\", \"authors\": \"Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zh...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"white2024livebench\", \"type\": \"article\", \"title\": \"LiveBench: A Challenging, Contamination-Free LLM Benchmark\", \"authors\": \"White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Ben...\", \"year\": \"2024\", \"venue\": \"arXiv preprint\"}, {\"key\": \"polo2024tinybenchmarks\", \"type\": \"inproceedings\", \"title\": \"TinyBenchmarks: Evaluating LLMs with Fewer Examples\", \"authors\": \"Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, G...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 41st International Conference on Machine Learning (ICML)\"}, {\"key\": \"han2026probing\", \"type\": \"inproceedings\", \"title\": \"Targeted Probing for Contamination Effects in Large Language Model Evaluations\", \"authors\": \"Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie\", \"year\": \"2026\", \"venue\": \"Findings of the 2026 Conference of the European Chapter of the Association for C...\"}, {\"key\": \"holland1993dif\", \"type\": \"book\", \"title\": \"Differential Item Functioning\", \"authors\": \"Holland, Paul W. and Wainer, Howard\", \"year\": \"1993\", \"venue\": \"\"}, {\"key\": \"thissen1993dif\", \"type\": \"incollection\", \"title\": \"Detection of Differential Item Functioning Using the Parameters of Item Response Models\", \"authors\": \"Thissen, David and Steinberg, Lynne and Wainer, Howard\", \"year\": \"1993\", \"venue\": \"Differential Item Functioning\"}, {\"key\": \"zumbo1999dif\", \"type\": \"book\", \"title\": \"A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary F...\", \"authors\": \"Zumbo, Bruno D.\", \"year\": \"1999\", \"venue\": \"\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"Proceedings of the 34th International Conference on Machine Learning (ICML)\"}, {\"key\": \"angelopoulos2023conformal\", \"type\": \"article\", \"title\": \"Conformal Prediction: A Gentle Introduction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen\", \"year\": \"2023\", \"venue\": \"Foundations and Trends in Machine Learning\"}, {\"key\": \"pruthi2020tracin\", \"type\": \"inproceedings\", \"title\": \"Estimating Training Data Influence by Tracing Gradient Descent\", \"authors\": \"Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund\", \"year\": \"2020\", \"venue\": \"Advances in Neural Information Processing Systems 33 (NeurIPS)\"}, {\"key\": \"park2023trak\", \"type\": \"inproceedings\", \"title\": \"TRAK: Attributing Model Behavior at Scale\", \"authors\": \"Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 40th International Conference on Machine Learning (ICML)\"}, {\"key\": \"reckase2009mirt\", \"type\": \"book\", \"title\": \"Multidimensional Item Response Theory\", \"authors\": \"Reckase, Mark D.\", \"year\": \"2009\", \"venue\": \"\"}, {\"key\": \"sanmartin2015\", \"type\": \"article\", \"title\": \"On the Unidentifiability of the Fixed-Effects 3PL Model\", \"authors\": \"San Mart\\\\'in, Ernesto and Gonz\\\\'alez, Jorge and Tuerlinckx, Francis\", \"year\": \"2015\", \"venue\": \"Psychometrika\"}, {\"key\": \"mislevy1987\", \"type\": \"article\", \"title\": \"Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters\", \"authors\": \"Mislevy, Robert J.\", \"year\": \"1987\", \"venue\": \"Applied Psychological Measurement\"}, {\"key\": \"wainer2007testlet\", \"type\": \"book\", \"title\": \"Testlet Response Theory and Its Applications\", \"authors\": \"Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui\", \"year\": \"2007\", \"venue\": \"\"}, {\"key\": \"carroll2006\", \"type\": \"book\", \"title\": \"Measurement Error in Nonlinear Models: A Modern Perspective\", \"authors\": \"Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu...\", \"year\": \"2006\", \"venue\": \"\"}, {\"key\": \"fuller1987\", \"type\": \"book\", \"title\": \"Measurement Error Models\", \"authors\": \"Fuller, Wayne A.\", \"year\": \"1987\", \"venue\": \"\"}, {\"key\": \"stefanski1985\", \"type\": \"article\", \"title\": \"Covariate Measurement Error in Logistic Regression\", \"authors\": \"Stefanski, Leonard A. and Carroll, Raymond J.\", \"year\": \"1985\", \"venue\": \"Annals of Statistics\"}, {\"key\": \"battauz2011\", \"type\": \"article\", \"title\": \"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\", \"authors\": \"Battauz, Michela and Bellio, Ruggero\", \"year\": \"2011\", \"venue\": \"Psychometrika\"}, {\"key\": \"westfall2016\", \"type\": \"article\", \"title\": \"Statistically Controlling for Confounding Constructs Is Harder than You Think\", \"authors\": \"Westfall, Jacob and Yarkoni, Tal\", \"year\": \"2016\", \"venue\": \"PLoS ONE\"}, {\"key\": \"jerzak2026\", \"type\": \"article\", \"title\": \"Attenuation Bias with Latent Predictors\", \"authors\": \"Jerzak, Connor T. and Jessee, Stephen A.\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2507.22218\"}, {\"key\": \"embretson2000\", \"type\": \"book\", \"title\": \"Item Response Theory for Psychologists\", \"authors\": \"Embretson, Susan E. and Reise, Steven P.\", \"year\": \"2000\", \"venue\": \"\"}, {\"key\": \"thissen2001\", \"type\": \"book\", \"title\": \"Test Scoring\", \"authors\": \"Thissen, David and Wainer, Howard\", \"year\": \"2001\", \"venue\": \"\"}, {\"key\": \"barton1981\", \"type\": \"article\", \"title\": \"An Upper Asymptote for the Three-Parameter Logistic Item-Response Model\", \"authors\": \"Barton, Mark A. and Lord, Frederic M.\", \"year\": \"1981\", \"venue\": \"ETS Research Report Series\"}, {\"key\": \"culpepper2016\", \"type\": \"article\", \"title\": \"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\", \"authors\": \"Culpepper, Steven Andrew\", \"year\": \"2016\", \"venue\": \"Psychometrika\"}, {\"key\": \"liao2012\", \"type\": \"article\", \"title\": \"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Respons...\", \"authors\": \"Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang\", \"year\": \"2012\", \"venue\": \"Social Behavior and Personality\"}], \"tex_citations\": [{\"key\": \"chang2025benchmarking\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"yang2026rl\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citet\"}, {\"key\": \"dong2026dose\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"wang2025fragility\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"rao2026silicon\", \"file\": \"introduction.tex\", \"line\": 4, \"command\": \"citep\"}, {\"key\": \"duan2025minkpp\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"oren2024proving\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"dekoninck2024constat\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"wust2025selfcritique\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"xu2025kds\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"gu2026psnirt\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"polo2026growing\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"lyu2025atlas\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"lalor2024irt\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"polo2024tinybenchmarks\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"zhuang2025hibayes\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"yang2024inference\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"han2026probing\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"li2025dcr\", \"file\": \"introduction.tex\", \"line\": 6, \"command\": \"citep\"}, {\"key\": \"xu2025emperor\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"zhang2025forget\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"white2024livebench\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"polo2024tinybenchmarks\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"citep\"}, {\"key\": \"eckerly2017\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"sinharay2017\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"deboeck2004\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"adams1997\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"mislevy1986\", \"file\": \"introduction.tex\", \"line\": 10, \"command\": \"citep\"}, {\"key\": \"cormack2009\", \"file\": \"introduction.tex\", \"line\": 12, \"command\": \"citep\"}, {\"key\": \"chang2025benchmarking\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"duan2025minkpp\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"oren2024proving\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"dekoninck2024constat\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wust2025selfcritique\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"xu2025kds\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"citep\"}, {\"key\": \"wang2025fragility\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"wust2025selfcritique\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citep\"}, {\"key\": \"dong2026dose\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"citet\"}, {\"key\": \"yang2026rl\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"citet\"}, {\"key\": \"zhang2025forget\", \"file\": \"related_work.tex\", \"line\": 14, \"command\": \"citet\"}, {\"key\": \"xu2025emperor\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"white2024livebench\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"yang2024inference\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"li2025dcr\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"rao2026silicon\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"guo2017calibration\", \"file\": \"related_work.tex\", \"line\": 18, \"command\": \"citep\"}, {\"key\": \"lalor2024irt\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"gu2026psnirt\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"polo2026growing\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"lyu2025atlas\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"polo2024tinybenchmarks\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"zhuang2025hibayes\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citep\"}, {\"key\": \"han2026probing\", \"file\": \"related_work.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"angelopoulos2023conformal\", \"file\": \"related_work.tex\", \"line\": 25, \"command\": \"citep\"}, {\"key\": \"eckerly2017\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"sinharay2017\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"deboeck2004\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"adams1997\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citep\"}, {\"key\": \"mislevy1986\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"holland1993dif\", \"file\": \"related_work.tex\", \"line\": 34, \"command\": \"citep\"}, {\"key\": \"thissen1993dif\", \"file\": \"related_work.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"zumbo1999dif\", \"file\": \"related_work.tex\", \"line\": 34, \"command\": \"citet\"}, {\"key\": \"duan2025minkpp\", \"file\": \"method.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"dekoninck2024constat\", \"file\": \"method.tex\", \"line\": 18, \"command\": \"citep\"}, {\"key\": \"wust2025selfcritique\", \"file\": \"method.tex\", \"line\": 21, \"command\": \"citep\"}, {\"key\": \"wang2025fragility\", \"file\": \"method.tex\", \"line\": 25, \"command\": \"citet\"}, {\"key\": \"cormack2009\", \"file\": \"method.tex\", \"line\": 28, \"command\": \"citep\"}, {\"key\": \"xu2025kds\", \"file\": \"method.tex\", \"line\": 35, \"command\": \"citep\"}, {\"key\": \"lord1980\", \"file\": \"method.tex\", \"line\": 41, \"command\": \"citep\"}, {\"key\": \"eckerly2017\", \"file\": \"method.tex\", \"line\": 71, \"command\": \"citep\"}, {\"key\": \"sinharay2017\", \"file\": \"method.tex\", \"line\": 71, \"command\": \"citep\"}, {\"key\": \"mislevy1986\", \"file\": \"method.tex\", \"line\": 73, \"command\": \"citep\"}, {\"key\": \"sanmartin2009\", \"file\": \"method.tex\", \"line\": 73, \"command\": \"citep\"}, {\"key\": \"sinharay2017\", \"file\": \"method.tex\", \"line\": 75, \"command\": \"citep\"}, {\"key\": \"deboeck2004\", \"file\": \"method.tex\", \"line\": 75, \"command\": \"citep\"}, {\"key\": \"maris2009\", \"file\": \"method.tex\", \"line\": 75, \"command\": \"citep\"}, {\"key\": \"hoffman2014\", \"file\": \"method.tex\", \"line\": 82, \"command\": \"citep\"}, {\"key\": \"carpenter2017\", \"file\": \"method.tex\", \"line\": 82, \"command\": \"citep\"}, {\"key\": \"sanmartin2009\", \"file\": \"method.tex\", \"line\": 85, \"command\": \"citep\"}, {\"key\": \"polo2026growing\", \"file\": \"method.tex\", \"line\": 88, \"command\": \"citep\"}, {\"key\": \"talts2018sbc\", \"file\": \"method.tex\", \"line\": 88, \"command\": \"citep\"}, {\"key\": \"ulitzsch2022\", \"file\": \"method.tex\", \"line\": 88, \"command\": \"citep\"}, {\"key\": \"hendrycks2021mmlu\", \"file\": \"experiments.tex\", \"line\": 13, \"command\": \"citep\"}, {\"key\": \"cobbe2021gsm8k\", \"file\": \"experiments.tex\", \"line\": 14, \"command\": \"citep\"}, {\"key\": \"clark2018arc\", \"file\": \"experiments.tex\", \"line\": 15, \"command\": \"citep\"}, {\"key\": \"chen2021humaneval\", \"file\": \"experiments.tex\", \"line\": 16, \"command\": \"citep\"}, {\"key\": \"yang2026rl\", \"file\": \"experiments.tex\", \"line\": 23, \"command\": \"citet\"}, {\"key\": \"carpenter2017\", \"file\": \"experiments.tex\", \"line\": 37, \"command\": \"citep\"}, {\"key\": \"hoffman2014\", \"file\": \"experiments.tex\", \"line\": 37, \"command\": \"citep\"}, {\"key\": \"gu2026psnirt\", \"file\": \"experiments.tex\", \"line\": 46, \"command\": \"citep\"}, {\"key\": \"polo2026growing\", \"file\": \"experiments.tex\", \"line\": 46, \"command\": \"citep\"}, {\"key\": \"xu2025emperor\", \"file\": \"experiments.tex\", \"line\": 48, \"command\": \"citet\"}, {\"key\": \"li2025dcr\", \"file\": \"experiments.tex\", \"line\": 49, \"command\": \"citet\"}], \"online_verification\": [{\"key\": \"lord1980\", \"title\": \"Applications of Item Response Theory to Practical Testing Problems\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Applications of Item Response Theory To Practical Testing Problems\", \"matched_year\": \"2012\", \"mismatch_fields\": [\"year: bib=1980 vs api=2012\"], \"note\": \"\"}, {\"key\": \"eckerly2017\", \"title\": \"Detecting Item Compromise in the Context of Item Response Theory\", \"status\": \"not_found\", \"confidence\": 0.301, \"matched_title\": \"SPIRIT 2013 explanation and elaboration: guidance for protocols of clinical trials\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}, {\"key\": \"sinharay2017\", \"title\": \"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"deboeck2004\", \"title\": \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\", \"matched_year\": \"2005\", \"mismatch_fields\": [\"first_author: bib=de boeck vs api=lenth\"], \"note\": \"\"}, {\"key\": \"adams1997\", \"title\": \"The Multidimensional Random Coefficients Multinomial Logit Model\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Multidimensional Random Coefficients Multinomial Logit Model\", \"matched_year\": \"1997\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mislevy1986\", \"title\": \"Bayes Modal Estimation in Item Response Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Bayes Modal Estimation in Item Response Models\", \"matched_year\": \"1986\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sanmartin2009\", \"title\": \"Consequential Validity of Item Response Theory Models for Measuring Latent Constructs\", \"status\": \"not_found\", \"confidence\": 0.419, \"matched_title\": \"Knowledge of the Firm and the Evolutionary Theory of the Multinational Corporation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"maris2009\", \"title\": \"On Interpreting the Model Parameters for the Three Parameter Logistic Model\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Interpreting the Model Parameters for the Three Parameter Logistic Model\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cormack2009\", \"title\": \"Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reciprocal rank fusion outperforms condorcet and individual rank learning methods\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hoffman2014\", \"title\": \"The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The No-U-turn sampler: adaptively setting path lengths in Hamiltonian Monte Carlo\", \"matched_year\": \"2014\", \"mismatch_fields\": [\"first_author: bib=hoffman vs api=homan\"], \"note\": \"\"}, {\"key\": \"carpenter2017\", \"title\": \"Stan: A Probabilistic Programming Language\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Stan: A Probabilistic Programming Language\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"talts2018sbc\", \"title\": \"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ulitzsch2022\", \"title\": \"Automatic Differentiation Variational Inference for Item Response Theory Models\", \"status\": \"not_found\", \"confidence\": 0.272, \"matched_title\": \"Partial Least Squares Structural Equation Modeling (PLS-SEM) Using R\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.27 below threshold 0.82\"}, {\"key\": \"duan2025minkpp\", \"title\": \"Min-K\\\\%++: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.375, \"matched_title\": \"Slingshot: cell lineage and pseudotime inference for single-cell transcriptomics\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"dekoninck2024constat\", \"title\": \"ConStat: Performance-Based Contamination Detection in Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"ConStat: Performance-Based Contamination Detection in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=de koninck vs api=dekoninck\"], \"note\": \"\"}, {\"key\": \"wust2025selfcritique\", \"title\": \"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations\", \"status\": \"not_found\", \"confidence\": 0.309, \"matched_title\": \"Challenges and Applications of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"xu2025kds\", \"title\": \"Knowledge Distillation Signatures for Efficient Contamination Detection\", \"status\": \"not_found\", \"confidence\": 0.341, \"matched_title\": \"Natural Products for Drug Discovery in the 21st Century: Innovations for Novel Drug Discovery\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"oren2024proving\", \"title\": \"Proving Test Set Contamination in Black Box Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Proving Test Set Contamination in Black Box Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xu2025emperor\", \"title\": \"The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.267, \"matched_title\": \"How Do Households Respond to Unreliable Water Supplies? A Systematic Review\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.27 below threshold 0.82\"}, {\"key\": \"dong2026dose\", \"title\": \"Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales\", \"status\": \"not_found\", \"confidence\": 0.337, \"matched_title\": \"Interventions to improve antibiotic prescribing practices for hospital inpatients\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"yang2026rl\", \"title\": \"Reinforcement Learning Amplifies Contamination in LLM Benchmark Evaluation\", \"status\": \"not_found\", \"confidence\": 0.333, \"matched_title\": \"Ethical and regulatory challenges of large language models in medicine\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.33 below threshold 0.82\"}, {\"key\": \"wang2025fragility\", \"title\": \"On the Fragility of Benchmark Evaluations for Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.509, \"matched_title\": \"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.51 below threshold 0.82\"}, {\"key\": \"zhang2025forget\", \"title\": \"How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.463, \"matched_title\": \"A Survey of Large Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.46 below threshold 0.82\"}, {\"key\": \"gu2026psnirt\", \"title\": \"PSN-IRT: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory\", \"status\": \"not_found\", \"confidence\": 0.37, \"matched_title\": \"INDRA: Iterative Difficulty Refinement Attention for MCQ Difficulty Estimation for Indic Languages\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.37 below threshold 0.82\"}, {\"key\": \"polo2026growing\", \"title\": \"Growing Pains: Understanding the Limitations and Potential of IRT for LLM Evaluation at Scale\", \"status\": \"not_found\", \"confidence\": 0.368, \"matched_title\": \"Safety psychology and the ergonomics of commercial kitchens\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.37 below threshold 0.82\"}, {\"key\": \"lyu2025atlas\", \"title\": \"ATLAS: Adaptive Testing via Latent Ability Scoring for Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.306, \"matched_title\": \"Dictionary learning for integrative, multimodal and scalable single-cell analysis\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"zhuang2025hibayes\", \"title\": \"HiBayES: Hierarchical Bayesian Evaluation System for Language Models\", \"status\": \"not_found\", \"confidence\": 0.622, \"matched_title\": \"HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.62 below threshold 0.82\"}, {\"key\": \"lalor2024irt\", \"title\": \"Benchmarking Large Language Models with Item Response Theory\", \"status\": \"not_found\", \"confidence\": 0.359, \"matched_title\": \"Partial Least Squares Structural Equation Modeling (PLS-SEM) Using R\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.36 below threshold 0.82\"}, {\"key\": \"li2025dcr\", \"title\": \"DCR: Decontaminated Calibration and Ranking for Benchmark Evaluation\", \"status\": \"not_found\", \"confidence\": 0.273, \"matched_title\": \"Synthetic Data Beyond Generative Models: A Comprehensive Survey of How, Why, and Where\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.27 below threshold 0.82\"}, {\"key\": \"yang2024inference\", \"title\": \"Inference-Time Decontamination of Large Language Models for Benchmark Evaluation\", \"status\": \"not_found\", \"confidence\": 0.74, \"matched_title\": \"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.74 below threshold 0.82\"}, {\"key\": \"rao2026silicon\", \"title\": \"The Silicon Bureaucracy: Evaluating the Evaluators in LLM Benchmarking\", \"status\": \"not_found\", \"confidence\": 0.516, \"matched_title\": \"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.52 below threshold 0.82\"}, {\"key\": \"hendrycks2021mmlu\", \"title\": \"Measuring Massive Multitask Language Understanding\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring Massive Multitask Language Understanding\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021gsm8k\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"clark2018arc\", \"title\": \"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2021humaneval\", \"title\": \"Evaluating Large Language Models Trained on Code\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Evaluating Large Language Models Trained on Code\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chang2025benchmarking\", \"title\": \"A Survey on Evaluation of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on Evaluation of Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"white2024livebench\", \"title\": \"LiveBench: A Challenging, Contamination-Free LLM Benchmark\", \"status\": \"not_found\", \"confidence\": 0.284, \"matched_title\": \"Racial bias in AI-mediated psychiatric diagnosis and treatment: a qualitative comparison of four large language models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.28 below threshold 0.82\"}, {\"key\": \"polo2024tinybenchmarks\", \"title\": \"TinyBenchmarks: Evaluating LLMs with Fewer Examples\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"tinyBenchmarks: evaluating LLMs with fewer examples\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"han2026probing\", \"title\": \"Targeted Probing for Contamination Effects in Large Language Model Evaluations\", \"status\": \"not_found\", \"confidence\": 0.344, \"matched_title\": \"The brain basis of emotion: A meta-analytic review\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"holland1993dif\", \"title\": \"Differential Item Functioning\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Differential Item Functioning\", \"matched_year\": \"2009\", \"mismatch_fields\": [\"year: bib=1993 vs api=2009\", \"first_author: bib=holland vs api=osterlind\"], \"note\": \"\"}, {\"key\": \"thissen1993dif\", \"title\": \"Detection of Differential Item Functioning Using the Parameters of Item Response Models\", \"status\": \"verified\", \"confidence\": 0.994, \"matched_title\": \"Detection of differential item functioning using the parameters of item response models.\", \"matched_year\": \"1993\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zumbo1999dif\", \"title\": \"A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores\", \"status\": \"not_found\", \"confidence\": 0.306, \"matched_title\": \"A Multidimensional Tool Based on the eHealth Literacy Framework: Development and Initial Validity Testing of the eHealth Literacy Questionnaire (eHLQ)\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.31 below threshold 0.82\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"angelopoulos2023conformal\", \"title\": \"Conformal Prediction: A Gentle Introduction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Conformal Prediction: A Gentle Introduction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pruthi2020tracin\", \"title\": \"Estimating Training Data Influence by Tracing Gradient Descent\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Estimating Training Data Influence by Tracing Gradient Descent\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"park2023trak\", \"title\": \"TRAK: Attributing Model Behavior at Scale\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"TRAK: Attributing Model Behavior at Scale\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reckase2009mirt\", \"title\": \"Multidimensional Item Response Theory\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multidimensional Item Response Theory\", \"matched_year\": \"2009\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sanmartin2015\", \"title\": \"On the Unidentifiability of the Fixed-Effects 3PL Model\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"On the Unidentifiability of the Fixed-Effects 3PL Model\", \"matched_year\": \"2014\", \"mismatch_fields\": [\"first_author: bib=san mart\\\\'in vs api=martı́n\"], \"note\": \"\"}, {\"key\": \"mislevy1987\", \"title\": \"Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"EXPLOITING AUXILIARY INFORMATION ABOUT EXAMINEES IN THE ESTIMATION OF ITEM PARAMETERS\", \"matched_year\": \"1986\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wainer2007testlet\", \"title\": \"Testlet Response Theory and Its Applications\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Testlet Response Theory and Its Applications\", \"matched_year\": \"2007\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"carroll2006\", \"title\": \"Measurement Error in Nonlinear Models: A Modern Perspective\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measurement error in nonlinear models: a modern perspective\", \"matched_year\": \"2006\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fuller1987\", \"title\": \"Measurement Error Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Measurement Error Models\", \"matched_year\": \"1988\", \"mismatch_fields\": [\"first_author: bib=fuller vs api=stefanski\"], \"note\": \"\"}, {\"key\": \"stefanski1985\", \"title\": \"Covariate Measurement Error in Logistic Regression\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Covariate Measurement Error in Logistic Regression\", \"matched_year\": \"1985\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"battauz2011\", \"title\": \"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Structural Modeling of Measurement Error in Generalized Linear Models with Rasch Measures as Covariates\", \"matched_year\": \"2010\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"westfall2016\", \"title\": \"Statistically Controlling for Confounding Constructs Is Harder than You Think\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Statistically Controlling for Confounding Constructs Is Harder than You Think\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jerzak2026\", \"title\": \"Attenuation Bias with Latent Predictors\", \"status\": \"not_found\", \"confidence\": 0.379, \"matched_title\": \"Embedding IRT in Structural Equation Models: A Comparison With Regression Based on IRT Scores\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"embretson2000\", \"title\": \"Item Response Theory for Psychologists\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Item response theory for psychologists\", \"matched_year\": \"2000\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thissen2001\", \"title\": \"Test Scoring\", \"status\": \"not_found\", \"confidence\": 0.476, \"matched_title\": \"The Black-White Test Score Gap\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.48 below threshold 0.82\"}, {\"key\": \"barton1981\", \"title\": \"An Upper Asymptote for the Three-Parameter Logistic Item-Response Model\", \"status\": \"verified\", \"confidence\": 0.965, \"matched_title\": \"AN UPPER ASYMPTOTE FOR THE THREE‐PARAMETER LOGISTIC ITEM‐RESPONSE MODEL*\", \"matched_year\": \"1981\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culpepper2016\", \"title\": \"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting the 4-Parameter Item Response Model: Bayesian Estimation and Application\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"liao2012\", \"title\": \"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses\", \"matched_year\": \"2012\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "67896969-512c-4df0-9c7f-e89f9fdc87ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 99 · 2026-05-16T17:04:17.953Z_

```json
{
  "parentUuid": "74092b17-eb1e-46e4-b665-3b9529b88b0a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a6f25478-0650-4908-a1cc-15c58889f5a6",
  "timestamp": "2026-05-16T17:04:17.953Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 100_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: **[Round 1 — 服务器重启后重新分配]**  你是 Reviewer 2，负责**新颖性、Related Work 完整性、论文整体呈现**。如果你已完成审稿，请直接提交；如果被服务器重启中断，请从头开始。  ## 论文信息 - **Title**: ContamCal: Characterizing Benchmark-Dependent Contami…",
  "leafUuid": "a6f25478-0650-4908-a1cc-15c58889f5a6",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621"
}
```

---


### Runtime record

_source line 101_

```json
{
  "type": "ai-title",
  "aiTitle": "Review contamination-augmented IRT paper for EMNLP",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621"
}
```

---


### Assistant

_source line 102 · 2026-05-16T17:06:01.797Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! This is very rich data. Let me summarize the reference verification results:

**Summary:**
- Total bib entries: 61
- Unique cited keys: 44
- Orphan bib entries (in bib but not cited): 17
- Missing bib entries (cited but not in bib): 0
- Online verified: 30
- Online not found: 24
- Online mismatch: 7

**Key findings from reference verification:**

1. **17 orphan entries** (in .bib but never cited): barton1981, battauz2011, carroll2006, culpepper2016, embretson2000, fuller1987, jerzak2026, liao2012, mislevy1987, park2023trak, pruthi2020tracin, reckase2009mirt, sanmartin2015, stefanski1985, thissen2001, wainer2007testlet, westfall2016


2. **24 unverified references** are mostly recent preprints not yet indexed, but three stand out as potentially problematic: eckerly2017 on item compromise detection is cited as a key precedent but doesn't appear to exist, while sanmartin2009 on consequential validity and ulitzsch2022 on automatic differentiation variational inference for IRT also couldn't be found online.

3. I'm seeing seven mismatches that look like minor formatting issues—mostly year discrepancies (lord1980 appears as 2012, deboeck2004 as 2005, holland1993dif as 2009) and author name variations (hoffman vs homan, dekoninck2024constat formatting)—but eckerly2017 remains the most suspicious since the paper itself can't be located anywhere.

Actually, there's work on item compromise detection in psychometrics, and Sinharay 2017 checks out as legitimate research on item preknowledge detection, but eckerly2017 could be either a real but obscure paper or potentially fabricated. What's interesting is that the related_work.tex and experiments.tex files actually contain citations (I can see them at specific line numbers), yet the compiled PDF shows "TODO: Related work to be written" with no experiment sections visible—suggesting either the content is commented out or wasn't included in the final compilation.

As a reviewer, I can only assess what's actually in the submitted PDF, though the source files hint there might be more content. The discrepancy between what's in the .tex files and what appears in the PDF is worth noting, especially since the Related Work section on page 2 shows just a placeholder despite the source containing actual citations.

The experiments section is similarly puzzling—the .tex file references benchmarks like MMLU, GSM8K, ARC, and HumanEval, but these don't seem to appear in the compiled PDF.

So the paper structure is incomplete: the Abstract and Related Work are marked as TODO, the Experiments section exists in source but isn't rendering in the PDF, and what actually appears is just the Introduction, Method, and References. This is clearly a draft that's nowhere near submission-ready.

Let me now structure a comprehensive review based on what's actually visible in the PDF. I'm mapping out the actual structure of this paper—it has an intro, a placeholder for related work, and method sections covering multi-signal provenance mapping, contamination-augmented IRT, Bayesian inference, and score computation, followed by references. But there's no abstract, experiments, results, discussion, or conclusion, and the method references a section that doesn't exist in the PDF. This is clearly an incomplete draft that warrants a strong rejection.

Now I'm checking the technical details more carefully—the paper discusses contamination exposure signals combining several techniques, and I need to verify the citations. Looking at the source files, I see Cormack et al. (2009) is cited for reciprocal rank fusion, not Edwards as I initially thought from the low-resolution image. Let me compile my review based on these findings.

I have what I need to write this up. The manuscript is fundamentally incomplete—it's missing the abstract, related work section, all experimental results, and conclusion. This makes it unsuitable for review in its current state. I'm rating it a strong reject with a 1/5 overall score. The methodology itself seems reasonable in principle, but without any experiments or validation, I can't assess whether it actually works. The abstract is just a placeholder saying it'll be written after experiments are done, and there's no code, data, or reproducibility information at all.

Beyond the missing abstract and related work, the paper has no experimental section whatsoever—just introduction and methods—and it references a section that doesn't exist. The content is also well short of the page limit, sitting at only about five pages of actual material. These aren't minor revisions; the paper needs substantial completion before it can be properly evaluated.

There are also some concerning issues with the bibliography. Seventeen entries are cited but never used, and a couple of key references—particularly eckerly2017 on item compromise detection—can't be verified through standard academic databases. The novelty claim also looks shaky compared to DCR from Li et al. at EMNLP 2025, which appears to tackle nearly the same problem.

The paper's framing feels inconsistent too. It starts by positioning itself as a calibration tool, then pivots to being a diagnostic framework after acknowledging calibration doesn't work well. Without actual results, it's hard to tell if this shift makes sense or if it's just rationalizing negative findings. The technical contribution itself—adding a contamination covariate term to the 4PL IRT model—is fairly incremental, so the real novelty hinges on whether the multi-signal provenance mapping in the first stage produces something genuinely novel.

The key question is whether the per-benchmark contamination effects actually reveal meaningful patterns and whether the calibrated scores are practically useful, but neither of these has been validated yet. The claim about negative signal degradation could be interesting if properly demonstrated, though right now it's just stated without evidence. Compared to related work, ContamCal does add contamination modeling to IRT approaches, which is novel in principle, and it goes beyond detection to calibration like DCR does—but the differentiation from DCR remains unclear. The Related Work section is still incomplete, so I can't fully assess how well the paper positions itself.

Looking at what's cited in the introduction, there are references to educational measurement DIF literature and probability calibration work that apparently got written but aren't rendering in the PDF, plus some dynamic benchmark approaches like LiveBench that are mentioned but DynaEval isn't. There's also a date on the title page that could be a versioning issue, and the introduction references a Fisher information analysis that doesn't actually appear in the paper.

Now I'm deciding on the scoring scale—the Director specified a 6-point system, but the official ARR form uses 1-5 with half-point increments. I should follow the Director's instructions since those are my task parameters, though I'll note the official ARR dimensions as well.

For the review dimensions, I'm mapping the Director's requests (Novelty/Excitement, Clarity, Significance, Reproducibility) against the official ARR categories (Soundness, Excitement, Overall Assessment, Reproducibility, Reviewer Confidence). Most align well, though Clarity isn't a standard ARR dimension, so I'll need to address that separately.

Now I'm structuring the review output following the template format specified in my instructions—starting with an overall score and one-sentence summary, then a table of official dimension scores with brief justifications, followed by sections for critical issues, minor issues, and key strengths.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6f25478-0650-4908-a1cc-15c58889f5a6",
  "isSidechain": false,
  "requestId": "req_011Cb6cN6mgmyfTsLmbq3EQV",
  "type": "assistant",
  "uuid": "fff3d52f-bde5-4a12-8cee-8b39f641fc9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1BST5d6eEtwejYLWWpGB2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17122,
      "cache_read_input_tokens": 46449,
      "output_tokens": 8183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8183,
          "cache_read_input_tokens": 46449,
          "cache_creation_input_tokens": 17122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17122
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 103 · 2026-05-16T17:06:03.582Z_

论文读完，引用验证完成。核心发现：这是一份严重不完整的手稿——Abstract、Related Work 均为 TODO，完全没有实验/结果/结论章节。下面撰写完整审稿意见并提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff3d52f-bde5-4a12-8cee-8b39f641fc9f",
  "isSidechain": false,
  "requestId": "req_011Cb6cN6mgmyfTsLmbq3EQV",
  "type": "assistant",
  "uuid": "facd717b-cdd0-48a7-9938-0384869b1935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1BST5d6eEtwejYLWWpGB2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17122,
      "cache_read_input_tokens": 46449,
      "output_tokens": 8183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8183,
          "cache_read_input_tokens": 46449,
          "cache_creation_input_tokens": 17122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17122
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-16T17:07:30.056Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_012gcXSuu97zeQv9pHXTQgDQ`</summary>

```json
{
  "text": "\n## Reviewer 2 — Round 1 审稿报告\n\n**论文**: ContamCal: Post-Hoc Calibration of Benchmark Scores under Training Data Contamination via Contamination-Augmented Item Response Theory\n**审查侧重**: 新颖性/Excitement、Related Work 完整性、论文整体呈现、Significance/Impact\n\n---\n\n## 总体评分\n\n**Overall**: 1/5 — Do not resubmit（当前形态不适合投稿）\n**一句话总结**: 该手稿严重不完整——Abstract 和 Related Work 均为 TODO 占位符，完全没有实验/结果/分析/结论章节，仅包含 Introduction + Method + References，无法作为完整论文进行同行评审。\n\n## 官方维度打分（来自 ACL ARR Review Form, 1-5 scale with 0.5 increments）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2/5 | 方法论描述本身看起来合理（contamination-augmented 4PL IRT + Bayesian inference），但所有 claims 均无实验支撑，无法判断技术正确性 |\n| Excitement | 2.5/5 | 核心思路（将污染暴露作为 IRT 协变量建模）有一定新意，但 DCR (Li et al., 2025) 已做了非常相似的 \"decontaminated calibration\"，增量贡献不清楚 |\n| Overall | 1/5 | 不完整手稿，不适合评审 |\n| Reproducibility | 1/5 | 无实验设置描述、无数据、无代码、无结果 |\n| Reviewer Confidence | 4/5 | 熟悉 IRT-for-LLM 和 contamination detection 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 是 TODO 占位符\n- 具体位置：Page 1, Abstract\n- 问题：Abstract 内容为 \"TODO: Abstract is to be written after experiments.\"\n- 为什么影响接收：没有 abstract 的论文不满足任何学术会议的最低提交要求。\n\n**N2** [critical] Related Work 是 TODO 占位符\n- 具体位置：Section 2 (Page 2)\n- 问题：Related Work 部分显示为 \"TODO: Related work to be written\"。注意：引用验证工具发现 `related_work.tex` 中实际存在引用（包括 DIF 文献 Holland 1993、Thissen 1993、Zumbo 1999，以及 Guo et al. 2017 probability calibration 等），但这些内容未渲染到最终 PDF。\n- 为什么影响接收：(1) 无法评估论文的 novelty claim（特别是 \"contamination calibration 是新问题\" 这一声称）；(2) 无法判断与 DCR、ConStat、PSN-IRT 等现有工作的关系和区分度；(3) 审稿侧重之一是 Related Work 完整性，但该章节不存在。\n\n**N3** [critical] 完全没有实验/结果/分析章节\n- 具体位置：论文在 Section 3.4 / Eq. 12（Page 5-6）后直接跳到 References\n- 问题：引用验证显示 `experiments.tex` 中存在对 MMLU、GSM8K、ARC、HumanEval 等 benchmark 的引用（lines 13-16），以及对 Stan/NUTS 的引用（line 37），说明实验章节有所规划但未编译到 PDF 中。Method 中提到 \"§7.2\" 用于比较 per-benchmark 和 global γ 的规格——但 §7 不存在。\n- 为什么影响接收：Introduction 中做出的所有关键 claims 均缺乏实验支撑：\n  - \"Min-K++ 方向逆转\"（污染有时降低分数）——仅为陈述，无数据\n  - \"per-benchmark γ_k 揭示异质性\"——无估计结果\n  - \"Bayesian credible intervals 显示检测信号依赖 benchmark 特性\"——无区间展示\n  - \"Fisher information analysis with a 1:4k condition swap\"（Introduction 中提及）——分析完全缺失\n  - \"dual-track validation\"（controlled MT contamination + observational analysis）——两条验证路线均不存在\n\n**N4** [critical] 没有 Conclusion 章节\n- 具体位置：论文在 References 处结束\n- 问题：缺少对发现的总结、局限性讨论、未来工作展望\n\n**N5** [critical] 正文内容严重不足\n- 具体位置：全文\n- 问题：实际内容约 5 页（Introduction ~2 页 + Method ~3 页），剩余 ~3 页为 References。ARR 允许 8 页正文 + 无限附录，当前内容远低于页数限制，说明论文远未完成。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 与 DCR (Li et al., 2025) 的区分不清\n- 具体位置：Introduction (Page 2)，Section 3.2 (Page 4)\n- 问题：EMNLP 2025 的 DCR 论文（\"Decontaminated Calibration and Ranking for Benchmark Evaluation\"）与 ContamCal 的目标高度重叠——都是对受污染 benchmark 分数进行事后校准。Introduction 仅简单提及 DCR，但 Related Work 为 TODO，无法了解两者在方法论、假设、适用范围上的本质区别。论文声称 \"contamination calibration 是一个新问题\" 但 DCR 的存在直接挑战了这一 novelty claim。\n- 建议：需要详细的方法对比（IRT-based vs. DCR 的方法）和实验 head-to-head 比较。\n\n**W2** [warning] 关键引用 eckerly2017 无法在线验证\n- 具体位置：Introduction (Page 1), Method Section 3.2 (Page 4)\n- 问题：`eckerly2017`（\"Detecting Item Compromise in the Context of Item Response Theory\", Applied Psychological Measurement, 41(2):85-101）是论文的核心理论依据之一，用于支撑 \"将 IRT item compromise 框架迁移到 LLM contamination\" 的论证。但 OpenAlex 查询未找到该文献。虽然教育测量领域的小众期刊可能不完全收录于 OpenAlex，但考虑到该引用对论文立论的重要性，作者应确认其真实性。（注：sinharay2017 同领域论文已通过验证。）\n- 建议：确认 eckerly2017 的准确引用信息，或改用已验证的替代文献。\n\n**W3** [warning] 从 \"校准工具\" 到 \"诊断框架\" 的叙事 pivot 缺乏说服力\n- 具体位置：Introduction (Pages 1-2)\n- 问题：Introduction 先以 \"post-hoc calibration\" 作为核心卖点立题，随后承认校准效果不理想，转而将贡献重新定位为 \"diagnostic framework\"。这一叙事转换在没有实验数据支撑的情况下显得像是对负面结果的事后合理化。如果校准确实失败，论文需要解释为什么诊断本身具有独立的学术价值，以及诊断结论如何被 downstream 用户使用。\n- 建议：如果最终实验证实校准失败，需要 (1) 正面呈现负面结果的价值；(2) 提供 actionable 的诊断使用案例。\n\n**W4** [warning] 17 个 orphan 文献条目\n- 具体位置：References (Pages 6-8)\n- 问题：.bib 文件中有 17 个条目从未在论文中引用（包括 barton1981, battauz2011, carroll2006, culpepper2016, embretson2000, fuller1987, jerzak2026 等）。这些大多是 IRT 和测量误差文献，暗示作者计划在 Related Work 或 Method 中使用但未完成。\n- 建议：提交前清理 .bib，确保每个条目都被引用。\n\n**W5** [warning] 核心技术贡献的增量性\n- 具体位置：Section 3.2 (Page 4), Eq. (8)\n- 问题：核心模型创新是在标准 4PL IRT 模型中加入一个污染协变量项 γ_k · ε_{ij}。从 IRT 建模角度看，这是对 explanatory IRT（De Boeck & Wilson 2004）的直接应用——向 item response function 添加一个外部协变量。技术上并非困难。论文的实际贡献更多在于 (1) 如何估计 ε_{ij}（Stage 1 多信号融合）和 (2) γ_k 的实证发现——但两者都缺乏实验验证。\n- 建议：需要实验证明 Stage 1 的 exposure 估计质量（与 ground truth 污染的相关性）、γ_k 估计的 posterior 不确定性、以及校准分数的实际效用。\n\n---\n\n## 小问题（不影响接收）\n\n- Title page 显示日期 \"May 13, 2026\"——虽然不违反匿名规则，但不必要的精确日期可能无意中泄露信息。\n- 多处引用的年份与 OpenAlex 记录有小幅偏差（lord1980, deboeck2004, holland1993dif 等），多为再版/在线版本差异，影响不大。\n- sanmartin2009（\"Consequential Validity of IRT Models\"）也无法在 OpenAlex 验证——与 eckerly2017 一样需要确认。\n\n---\n\n## 主要优势\n\n1. **问题定位合理**：从 contamination detection 推进到 calibration/correction 是文献中的自然缺口。现有方法（Min-K++, ConStat, KDS）仅做检测，不回答 \"检测到污染后怎么办\"。\n2. **方法论框架有理论基础**：将 IRT item compromise 文献（教育测量中的考题泄露检测）迁移到 LLM benchmark contamination 是一个有意义的跨领域类比。4PL IRT + Bayesian inference 的技术选择合理。\n3. **Multi-signal provenance mapping**（Section 3.1）的设计考虑了多种污染检测信号的互补性，包括 Min-K++、perplexity gap、signal survival analysis 和 RRF 融合，体现了对检测信号局限性的理解。\n4. **Measurement error model**（Section 3.2）正确处理了 ε_{ij} 作为噪声协变量的误差传播问题，这在将检测信号用于下游建模时是重要的技术细节。\n\n---\n\n## 新颖性深度评估（Reviewer 2 重点）\n\n### 与现有文献的增量贡献\n\n| 比较对象 | ContamCal 的增量 | 评估 |\n|----------|-----------------|------|\n| Min-K++ / ConStat / KDS (检测类) | 从检测推进到校准 | 方向正确，但实际校准效果未知 |\n| DCR (Li et al., EMNLP 2025) | 使用 IRT 框架而非 DCR 的方法 | 差异不清，需要 head-to-head |\n| TinyBenchmarks / PSN-IRT / HiBayES (IRT-for-LLM) | 加入 contamination 协变量 | 技术上直接，理论增量有限 |\n| Eckerly 2017 / Sinharay 2017 (item compromise IRT) | 从教育测量迁移到 LLM | 跨领域应用，但核心建模思路已有先例 |\n\n### \"负面结果 → 诊断框架\" 的学术价值\n\n- 负面结果论文在 ACL/EMNLP 有接收先例（Findings track 更宽容）\n- 但负面结果论文需要 (1) 充分的实验证据证明负面结果的系统性；(2) 对 \"为什么不 work\" 的深入分析；(3) 对社区的明确 actionable takeaway\n- 当前论文这三点均缺失\n\n### Min-K++ 方向逆转：潜在高价值发现，但...\n\n- 如果实验证实 Min-K++ 在特定 benchmark 上与性能呈负相关（即污染反而降低分数），这确实是对 contamination 研究社区的重要发现\n- 但该发现仅在 Introduction 中以一句话形式出现，没有任何实验验证\n- 独立支撑投稿需要：(1) 系统的 benchmark×model 矩阵分析；(2) 对逆转机制的因果推断或至少合理解释；(3) 对 Min-K++ 社区的实际 implication\n\n---\n\n## 总结判断\n\n当前手稿处于极早期阶段（仅有 Introduction + Method），距离可提交状态差距巨大。核心想法（contamination-augmented IRT）有一定学术兴趣，但 (1) 与 DCR 的差异化不足，(2) 技术增量有限（本质是向 IRT 加一个协变量），(3) 所有关键 claims 均无实验支撑。建议完成全部实验和写作后，以完整论文重新提交至下一个 ARR cycle。\n\n**建议处理**: 1/5 (Do not resubmit in current form) — 完成实验、Related Work、Abstract、Conclusion 后以完整稿件重新提交。\n",
  "reviewer_id": "2",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "facd717b-cdd0-48a7-9938-0384869b1935",
  "isSidechain": false,
  "requestId": "req_011Cb6cN6mgmyfTsLmbq3EQV",
  "type": "assistant",
  "uuid": "b769fd85-bab9-403c-b06b-91877ebbac39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1BST5d6eEtwejYLWWpGB2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17122,
      "cache_read_input_tokens": 46449,
      "output_tokens": 8183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8183,
          "cache_read_input_tokens": 46449,
          "cache_creation_input_tokens": 17122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17122
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 105_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: **[Round 1 — 服务器重启后重新分配]**  你是 Reviewer 2，负责**新颖性、Related Work 完整性、论文整体呈现**。如果你已完成审稿，请直接提交；如果被服务器重启中断，请从头开始。  ## 论文信息 - **Title**: ContamCal: Characterizing Benchmark-Dependent Contami…",
  "leafUuid": "b769fd85-bab9-403c-b06b-91877ebbac39",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621"
}
```

---


### Runtime record

_source line 106_

```json
{
  "type": "ai-title",
  "aiTitle": "Review contamination-augmented IRT paper for EMNLP",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621"
}
```

---


### Tool result

_source line 107 · 2026-05-16T17:07:33.798Z_

<details><summary>↩ Tool result · `toolu_012gcXSuu97zeQv9pHXTQgDQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b769fd85-bab9-403c-b06b-91877ebbac39",
  "isSidechain": false,
  "promptId": "4e3fc52f-dc1e-44b5-9d0f-d389164f223c",
  "type": "user",
  "uuid": "fbd78bdf-b497-44cc-a76d-3797fb0a26d3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "b769fd85-bab9-403c-b06b-91877ebbac39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 108_

```json
{
  "type": "ai-title",
  "aiTitle": "Review contamination-augmented IRT paper for EMNLP",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621"
}
```

---


### Runtime record

_source line 109 · 2026-05-16T17:09:53.570Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T17:09:53.570Z",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "content": "[Round 1 审稿请求]:\n**[Round 1 — 交叉分享] 请逐条回应 Reviewer 1 的审稿意见**\n\n⚠️ **重要背景**：Reviewer 1 审阅的是一个更完整的论文版本（包含完整的实验结果、Table 1-9、Section 4-6），而你审阅的 PDF 是一个过期的编译版本（缺少实验章节渲染）。这是提交流程问题，不是你的审稿失误。请基于 Reviewer 1 描述的内容进行回应——即使你没有亲眼看到那些数据，你仍可以评估其论证逻辑、统计方法论和 claim 强度。\n\n---\n\n以下是 **Reviewer 1 的完整审稿意见**：\n\n## 总体评分\n**Overall**: 3/6 (Borderline Reject)\n**一句话总结**: 论文提出了有价值的诊断发现（Min-K++ 方向逆转、IRT 可辨识性边界），但核心跨尺度主张缺少 1.5B/3B 关键实验数据支撑，跨家族验证统计力严重不足（N=3），且\"不可能性\"结论可能仅适用于 IRT 这一特定方法而非一般性结构限制。\n\n## 通用维度打分（Top ML Venue 6 分制）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/6 | 中心主张（跨尺度单调衰减）的实验证据链断裂：仅展示 0.5B 和 7B 数据，1.5B/3B 缺失；跨家族结论建立在 N=3 非显著结果上 |\n| Novelty/Excitement | 4/6 | Min-K++ 方向逆转（Cohen's d = -1.55 到 -1.98）是对检测社区的重要警示；诊断框架视角有新意；但\"校准困难\"本身的洞察有限 |\n| Clarity | 4/6 | 写作总体清晰，narrative 逻辑自洽，诚实报告负面结果值得赞赏；但 Table 2 标题与内容不符 |\n| Significance | 3/6 | 负面结果论文可以有贡献，但 actionable takeaway 有限 |\n| Reproducibility | 3/6 | 控制 SFT 协议描述完整，但 1.5B/3B 数据缺失让审稿人无法验证核心主张 |\n\n## Must-Fix 问题\n\n**N1** [critical] 跨尺度核心主张缺失 1.5B/3B 实验数据\n- Table 2 仅展示 7B，Table 1 仅展示 0.5B。论文声称覆盖四个尺度但只展示两端数据。单调性需要至少三个点，缺少中间点让核心主张变成不可证伪的断言。\n\n**N2** [critical] 跨家族验证统计力严重不足\n- Llama-3.2-3B 仅 3 个剂量级别（N=3），所有 γ CI 包含零，Kendall τ 全部非显著。但论文从中推导 \"provably infeasible\" 的强结论。需要区分 \"证据不足\" 和 \"证据表明不一致\"。\n\n**N3** [critical] \"不可能性\"结论可能是方法特异的\n- 三重不可能性（开放权重、N≥50、容量混淆）都绑定在 IRT + multi-signal detection 上。N≥50 是 IRT 要求而非所有校准方法的要求。论文将方法限制上升为领域限制。\n\n## Should-Fix 问题\n\n**W1** Table 2 标题 \"across model scales\" 实际只有 7B\n**W2** Fisher Information 模拟缺乏独立可验证性（无图表，仅文字描述）\n**W3** 观测实验（Exp 4, 5）无地面真值条件下推理过度\n**W4** SFT ≠ 真实污染的 gap 可能被低估\n\n## 主要优势\n1. Min-K++ 方向逆转发现具有独立价值（Cohen's d = -1.55 到 -1.98，跨家族复制）\n2. 诚实报告负面结果的科学态度\n3. Calibration gating criterion 是有用的方法论贡献\n4. 控制 SFT 实验设计严谨\n5. \"Scale paradox\" 表述有洞察力\n\n---\n\n**请逐条回应**：对每个 Must-Fix 和 Should-Fix 问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供论据。\n\n特别关注：\n1. 你作为新颖性/Related Work 专家，对 Reviewer 1 的 N3（不可能性结论泛化问题）有何评估？\n2. Reviewer 1 给 Novelty 4/6，你是否同意这个评分？结合你对 DCR 重叠度的分析。\n3. Reviewer 1 认为 Min-K++ 逆转发现有独立价值——你是否同意？"
}
```

---


### Runtime record

_source line 110 · 2026-05-16T17:09:53.571Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T17:09:53.571Z",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 111 · 2026-05-16T17:09:53.562Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbd78bdf-b497-44cc-a76d-3797fb0a26d3",
  "isSidechain": false,
  "promptId": "56687575-614d-4221-9c76-557468d72229",
  "type": "user",
  "isMeta": true,
  "uuid": "da800139-c238-4900-bf2f-025937d9efd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 112 · 2026-05-16T17:09:53.563Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da800139-c238-4900-bf2f-025937d9efd5",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "7bcfff45-4fe5-47d0-ae77-acd8fd47217a",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "c592a4b2-96bb-47f9-a63d-289dac06a5a4",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 3

## Round 3

7 recorded events


### User

_source line 113 · 2026-05-16T17:09:53.651Z_

[Round 1 审稿请求]:
**[Round 1 — 交叉分享] 请逐条回应 Reviewer 1 的审稿意见**

⚠️ **重要背景**：Reviewer 1 审阅的是一个更完整的论文版本（包含完整的实验结果、Table 1-9、Section 4-6），而你审阅的 PDF 是一个过期的编译版本（缺少实验章节渲染）。这是提交流程问题，不是你的审稿失误。请基于 Reviewer 1 描述的内容进行回应——即使你没有亲眼看到那些数据，你仍可以评估其论证逻辑、统计方法论和 claim 强度。

---

以下是 **Reviewer 1 的完整审稿意见**：

## 总体评分
**Overall**: 3/6 (Borderline Reject)
**一句话总结**: 论文提出了有价值的诊断发现（Min-K++ 方向逆转、IRT 可辨识性边界），但核心跨尺度主张缺少 1.5B/3B 关键实验数据支撑，跨家族验证统计力严重不足（N=3），且"不可能性"结论可能仅适用于 IRT 这一特定方法而非一般性结构限制。

## 通用维度打分（Top ML Venue 6 分制）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/6 | 中心主张（跨尺度单调衰减）的实验证据链断裂：仅展示 0.5B 和 7B 数据，1.5B/3B 缺失；跨家族结论建立在 N=3 非显著结果上 |
| Novelty/Excitement | 4/6 | Min-K++ 方向逆转（Cohen's d = -1.55 到 -1.98）是对检测社区的重要警示；诊断框架视角有新意；但"校准困难"本身的洞察有限 |
| Clarity | 4/6 | 写作总体清晰，narrative 逻辑自洽，诚实报告负面结果值得赞赏；但 Table 2 标题与内容不符 |
| Significance | 3/6 | 负面结果论文可以有贡献，但 actionable takeaway 有限 |
| Reproducibility | 3/6 | 控制 SFT 协议描述完整，但 1.5B/3B 数据缺失让审稿人无法验证核心主张 |

## Must-Fix 问题

**N1** [critical] 跨尺度核心主张缺失 1.5B/3B 实验数据
- Table 2 仅展示 7B，Table 1 仅展示 0.5B。论文声称覆盖四个尺度但只展示两端数据。单调性需要至少三个点，缺少中间点让核心主张变成不可证伪的断言。

**N2** [critical] 跨家族验证统计力严重不足
- Llama-3.2-3B 仅 3 个剂量级别（N=3），所有 γ CI 包含零，Kendall τ 全部非显著。但论文从中推导 "provably infeasible" 的强结论。需要区分 "证据不足" 和 "证据表明不一致"。

**N3** [critical] "不可能性"结论可能是方法特异的
- 三重不可能性（开放权重、N≥50、容量混淆）都绑定在 IRT + multi-signal detection 上。N≥50 是 IRT 要求而非所有校准方法的要求。论文将方法限制上升为领域限制。

## Should-Fix 问题

**W1** Table 2 标题 "across model scales" 实际只有 7B
**W2** Fisher Information 模拟缺乏独立可验证性（无图表，仅文字描述）
**W3** 观测实验（Exp 4, 5）无地面真值条件下推理过度
**W4** SFT ≠ 真实污染的 gap 可能被低估

## 主要优势
1. Min-K++ 方向逆转发现具有独立价值（Cohen's d = -1.55 到 -1.98，跨家族复制）
2. 诚实报告负面结果的科学态度
3. Calibration gating criterion 是有用的方法论贡献
4. 控制 SFT 实验设计严谨
5. "Scale paradox" 表述有洞察力

---

**请逐条回应**：对每个 Must-Fix 和 Should-Fix 问题，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并提供论据。

特别关注：
1. 你作为新颖性/Related Work 专家，对 Reviewer 1 的 N3（不可能性结论泛化问题）有何评估？
2. Reviewer 1 给 Novelty 4/6，你是否同意这个评分？结合你对 DCR 重叠度的分析。
3. Reviewer 1 认为 Min-K++ 逆转发现有独立价值——你是否同意？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bcfff45-4fe5-47d0-ae77-acd8fd47217a",
  "isSidechain": false,
  "promptId": "56687575-614d-4221-9c76-557468d72229",
  "type": "user",
  "uuid": "4ffb7ac8-50e3-4cc1-a4d1-ba90e505ed31",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 114 · 2026-05-16T17:10:29.223Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me to do a cross-review response to Reviewer 1's findings. Important context: Reviewer 1 reviewed a more complete version of the paper that includes experiments (Tables 1-9, Sections 4-6), while I reviewed an outdated compiled PDF missing those sections.

I need to respond to each Must-Fix and Should-Fix issue with [AGREE] or [REBUT], and address the three specific questions at the end.

Let me think through each issue carefully:

**N1 - Missing 1.5B/3B data for cross-scale claims**
This is a soundness issue. 

If the paper claims to cover four scales but only shows two endpoints (0.5B and 7B), that's a legitimate gap—monotonicity claims really do need intermediate points to be credible. I agree with this critique.

**N2 - Cross-family validation statistical power (N=3)**
With only 3 dose levels for Llama-3.2-3B and all γ confidence intervals including zero, the Kendall τ test comes back non-significant. Drawing "provably infeasible" conclusions from underpowered tests conflates Type II error with actual impossibility, which is methodologically problematic. I agree.

**N3 - "Impossibility" conclusion may be method-specific**
This is worth considering—the findings might be tied to the specific scaling law framework rather than representing a fundamental constraint.

The paper treats the limitations of IRT plus multi-signal detection as universal impossibility results for contamination calibration, but those constraints around open weights, sample size requirements, and capacity confounding are really just artifacts of the IRT approach. Other methods like DCR's approach, or entirely different calibration frameworks, might sidestep these issues entirely. This actually ties back to my concern about how the paper differentiates itself from DCR—if the "impossibility" is just IRT-specific, then DCR's method could plausibly work in cases where ContamCal hits a wall.

I find this concern compelling and it strengthens my novelty assessment.

**W1 - Table 2 title mismatch**
Clear presentation issue, straightforward to fix.

**W2 - Fisher Information simulation lacks visual verification**
Important analysis should have accompanying figures.

**W3 - Observational experiments (Exp 4, 5) over inference without ground truth**
This is a standard challenge in contamination research.

**W4 - SFT ≠ real contamination gap**
The controlled nature of SFT—where benchmark items are deliberately injected—differs meaningfully from how contamination actually occurs in practice through natural web crawls and partial overlaps. This gap between the experimental setup and real-world conditions could limit how well the findings translate, though I acknowledge this tension is somewhat inherent to the research design.

On the impossibility generalization question, the paper's "triple impossibility" claim is its boldest contribution, yet it rests on IRT-specific foundations. Looking at the educational measurement literature on item compromise detection, impossibility results there are similarly method-dependent rather than universal.  The paper should explicitly scope its claims to IRT-based approaches rather than contamination calibration broadly, especially since DCR uses a non-IRT framework that might sidestep these constraints entirely.

Regarding the novelty rating, I initially scored this lower because I couldn't access the experiments, but the actual findings—the Min-K++ reversal with substantial effect sizes, the scale paradox, the calibration gating criterion—do push the contribution higher than my initial assessment. Still, a 4/6 feels slightly optimistic given the overlap with existing work like DCR.

The Min-K++ reversal stands out as the paper's most compelling contribution, with effect sizes large enough to matter practically for the contamination detection community. That said, this finding might be better positioned as a focused workshop or short paper rather than carrying the weight of a full submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ffb7ac8-50e3-4cc1-a4d1-ba90e505ed31",
  "isSidechain": false,
  "requestId": "req_011Cb6cnrEmhZVtQWQkPNPpY",
  "type": "assistant",
  "uuid": "76a4b2c1-11a2-4e62-80a9-07baa71c5a1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VpW2WiT5ZHzUGRPhRhUsW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 56313,
      "cache_read_input_tokens": 11841,
      "output_tokens": 5809,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 56313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5809,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 56313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 56313
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 38299
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 115 · 2026-05-16T17:10:30.109Z_

收到。我基于 Reviewer 1 描述的实验内容和我对论文 method + novelty/related work 的分析，逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76a4b2c1-11a2-4e62-80a9-07baa71c5a1f",
  "isSidechain": false,
  "requestId": "req_011Cb6cnrEmhZVtQWQkPNPpY",
  "type": "assistant",
  "uuid": "5e2095b9-5779-41b1-89db-c8889d3e2d5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VpW2WiT5ZHzUGRPhRhUsW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 56313,
      "cache_read_input_tokens": 11841,
      "output_tokens": 5809,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 56313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5809,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 56313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 56313
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 38299
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-16T17:12:12.468Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_014NvvevKxZu2k6qgBqwnV7w`</summary>

```json
{
  "text": "\n## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n**背景说明**：我审阅的 PDF 为过期编译版（缺少实验章节），以下回应基于 Reviewer 1 描述的实验内容 + 我对 Method/Introduction/Related Work 的独立分析。\n\n---\n\n## Must-Fix 逐条回应\n\n### [AGREE] R1-N1: 跨尺度核心主张缺失 1.5B/3B 实验数据\n\n同意这是严重的证据链断裂。\n\n补充理由：从方法论角度看，ContamCal 的核心模型（Eq. 8 的 contamination-augmented 4PL IRT）中 γ_k 的估计依赖于足够的 item-level 变异。不同模型尺度下，ability θ_i 和 contamination exposure ε_{ij} 的联合分布可能存在非线性关系——0.5B 和 7B 是能力谱的两端，中间尺度（1.5B/3B）恰好处于 \"模型已有一定能力但尚未完全掌握 benchmark 内容\" 的过渡区间。论文方法中的 few-examinee regime 讨论（Section 3.3）承认 N < 50 时 IRT 参数估计不稳定，但如果连中间尺度的数据都不展示，读者无法判断 γ 的 \"单调衰减\" 是真实模式还是两点连线的 artifact。\n\n此外，从 IRT 文献看，item difficulty (b_j) 和 person ability (θ_i) 之间的匹配度（information function 峰值位置）对参数估计精度至关重要。中间尺度模型可能恰好处于 information function 最高效的区域——缺少这些数据点意味着论文可能遗漏了最有信息量的观测。\n\n### [AGREE] R1-N2: 跨家族验证统计力严重不足（N=3）\n\n强烈同意。这是我最关注的方法论问题之一。\n\n补充理由：从 Bayesian IRT 的角度看，N=3 dose levels 意味着 γ 的 posterior 几乎完全由 prior（论文使用 γ_k ~ N(0,1)）主导。此时 \"CI 包含零\" 不能解读为 \"效应不存在\"，只能解读为 \"数据对 prior 几乎没有更新\"。论文从这种极低统计力的结果推导出 \"provably infeasible\" 是经典的 **absence of evidence ≠ evidence of absence** 错误。\n\n更具体地说：如果 Kendall τ 的 power analysis 显示在 N=3 时检测 medium effect (τ ≈ 0.3) 的统计力低于 20%，那么非显著结果完全在预期内，不应用来支撑任何方向的结论。论文应该：(1) 报告 post-hoc power；(2) 明确标注 \"inconclusive\" 而非暗示 \"infeasible\"。\n\n### [AGREE with qualification] R1-N3: \"不可能性\"结论可能是方法特异的\n\n**同意核心判断，并从 novelty/related work 视角提供更强的论据。**\n\n这是我作为 Reviewer 2（novelty + related work 侧重）最需要深入讨论的问题。\n\n**1. 三重不可能性的逻辑拆解：**\n\n论文的\"三重不可能性\"（开放权重要求、N≥50 要求、能力-污染混淆）实际上是三个不同层次的限制：\n\n- **开放权重要求**：这是 Min-K++ 等 membership inference 方法的限制，不是所有污染检测/校准方法的限制。ConStat (De Koninck et al., 2024) 基于 performance patterns 工作，不需要模型权重。如果 Stage 1 的 exposure estimation 不依赖 Min-K++（例如用 ConStat 风格的 behavioral signal），整个开放权重限制就消失了。\n- **N≥50 要求**：如 Reviewer 1 正确指出，这是 IRT 的统计要求，不是校准的一般要求。DCR (Li et al., EMNLP 2025) 使用非 IRT 方法进行 decontaminated calibration，可能在小样本下也能工作。论文将 IRT 的样本量需求上升为 \"contamination calibration 领域的基本限制\" 是过度泛化。\n- **能力-污染混淆**：这可能是三者中最有泛化潜力的观察——如果高能力模型系统性地暴露于更多训练数据（包括 benchmark items），那么任何基于观测数据的方法都面临 confounding。但论文没有正式证明这个 confounding 是不可解的（例如通过 instrumental variable 或 RCT 设计），而是直接从 IRT 框架内的不可辨识性跳到了一般性不可能性。\n\n**2. Related Work 视角的关键缺失：**\n\n论文的不可能性论证缺少与以下工作的对比：\n- **DCR (Li et al., 2025)**：如果 DCR 在不需要 IRT、不需要开放权重的条件下实现了某种程度的 decontaminated calibration，那么 ContamCal 的 \"不可能性\" 结论就被 DCR 的存在性直接反驳了（或至少需要解释为什么 DCR 的 \"校准\" 不算真正的校准）。\n- **DIF 文献 (Holland & Wainer 1993; Zumbo 1999)**：教育测量中的 item compromise 检测已有数十年历史。该文献对 \"在什么条件下 item compromise 的效应可被估计\" 有严格的理论分析（例如 anchor item 策略、DIF contrast coding）。论文没有讨论这些已有的可辨识性条件是否适用于 LLM setting。\n- **Causal inference 方法**：能力-污染混淆本质上是一个 causal identification 问题。文献中有大量处理 confounding 的方法（IV, RDD, difference-in-differences），论文没有讨论这些方法是否可能打破 confounding。\n\n**3. 建议的修正方向：**\n\n将 \"三重不可能性\" 重新表述为 \"在 IRT + membership-inference-based detection 框架下的三重限制\"，并明确讨论 (a) 其他方法框架是否共享这些限制；(b) 在什么条件下这些限制可以被放松。这样做会降低 claim 的震撼性，但大幅提高其可信度。\n\n---\n\n## Should-Fix 逐条回应\n\n### [AGREE] R1-W1: Table 2 标题 \"across model scales\" 实际只有 7B\n\n直接的呈现错误。与 N1 相关——如果中间尺度数据确实缺失，标题的 misleading 性质更严重。\n\n### [AGREE] R1-W2: Fisher Information 模拟缺乏独立可验证性\n\n同意。Fisher Information analysis 是论文 calibration gating criterion 的理论基础（也是 Introduction 中提到的 \"1:4k condition swap\" 分析的一部分）。这么关键的分析仅以文字描述呈现，没有图表，读者无法独立评估其有效性。建议至少提供 (1) information matrix 的 heatmap；(2) condition number vs. sample size 的关系图。\n\n### [AGREE with qualification] R1-W3: 观测实验推理过度\n\n基本同意。在没有 ground truth contamination labels 的观测数据上，γ 的估计反映的是 \"与 Min-K++ signal 相关的性能变异\"，不等同于 \"真实污染效应\"。但我对此问题的严重性评估略低于 R1——观测实验的价值在于 ecological validity（展示方法在真实条件下的行为），只要论文明确标注 \"associational, not causal\" 即可。\n\n### [AGREE] R1-W4: SFT ≠ 真实污染的 gap\n\n同意。SFT 是 deliberate, concentrated injection；真实污染是 incidental, distributed exposure through web crawls。这个 gap 影响的不仅是效果大小，还可能影响效应方向——SFT 可能产生的 \"过拟合特定答案格式\" 效应在真实污染中未必出现。论文应讨论这个 external validity limitation。\n\n---\n\n## Director 指定的三个焦点问题\n\n### 1. 对 R1-N3（不可能性泛化）的深度评估\n\n**立场：强烈同意 R1 的判断，并认为这可能是论文最大的概念性弱点。**\n\n如上详述，论文的 \"不可能性\" 论证存在三层泛化跳跃：\n- 从 IRT → 所有参数化校准方法\n- 从 Min-K++ based exposure → 所有 exposure estimation 方法\n- 从 \"当前证据不足以拒绝零假设\" → \"理论上不可能\"\n\n每一层跳跃都缺乏严格的证明。特别是，DCR (Li et al., 2025) 的存在直接构成了对 \"contamination calibration 不可能\" 的反例——除非论文能论证 DCR 的 \"calibration\" 实际上不是真正的 calibration（但这需要形式化定义什么算 \"真正的 calibration\"）。\n\n从积极角度看，如果论文将不可能性结论严格限定在 IRT 框架内，这反而可以成为一个有用的理论贡献：它告诉后续研究者 \"不要在 IRT 框架内尝试 contamination calibration，除非满足 X, Y, Z 条件\"。但这需要将 claim 从 \"contamination calibration is fundamentally impossible\" 修改为 \"IRT-based contamination calibration requires conditions that are rarely met in practice\"。\n\n### 2. Reviewer 1 给 Novelty 4/6 是否合理？\n\n**我认为偏高，建议 3/6 到 3.5/6。**\n\n理由：\n\n**(a) DCR 重叠度问题**（我的核心关切）：\nReviewer 1 似乎没有深入讨论 DCR (Li et al., EMNLP 2025) 与 ContamCal 的关系。DCR 的全称是 \"Decontaminated Calibration and Ranking for Benchmark Evaluation\"——这与 ContamCal 的目标几乎完全重合。虽然方法不同（IRT vs. DCR 的方法），但 problem framing 高度相似。论文声称 \"contamination calibration 是一个新问题\" 这一 novelty claim 被 DCR 的存在直接削弱。\n\n**(b) 技术增量有限**：\n核心建模创新是在 4PL IRT 的 item response function 中加入 γ_k · ε_{ij} 项。这是 explanatory IRT (De Boeck & Wilson, 2004) 的标准操作——向 IRT 模型添加 item-level covariates。技术难度不高，真正的贡献在于 (1) Stage 1 multi-signal fusion 的设计和 (2) 实证发现。但 Stage 1 使用的方法（Min-K++, perplexity gap, RRF 融合）都是已有方法的组合。\n\n**(c) 有利因素**：\n- Min-K++ 逆转发现确实有新意（如果效应量和跨家族复制都 robust）\n- 将教育测量的 item compromise 框架迁移到 LLM contamination 是有价值的跨领域工作\n- Calibration gating criterion 是实用的方法论工具\n\n综合评估：存在 genuine novelty，但不足以达到 4/6（\"would make effort to attend\"）。3/6（\"might mention points; would attend if time available\"）更准确。\n\n### 3. Min-K++ 逆转发现是否有独立价值？\n\n**同意 Reviewer 1 的判断——这可能是论文最有价值的贡献。**\n\n理由：\n- **效应量大**：Cohen's d = -1.55 到 -1.98 是非常大的效应（远超常规 d > 0.8 的 \"large\" 标准），表明这不是噪声\n- **跨家族复制**：如果在 Qwen 和 Llama 家族都观察到方向逆转，这增加了发现的可信度\n- **实际影响**：大量研究直接使用 Min-K++ score 作为 \"更高 = 更可能被污染\" 的指标。方向逆转意味着在某些 benchmark 上，这种解读不仅错误而且方向相反——这对 contamination detection 社区的实践有直接影响\n\n**但有两个保留意见：**\n\n1. **机制不清**：为什么 Min-K++ 在某些 benchmark 上逆转？可能的解释包括 (a) benchmark items 的分布特性（多选题 vs. 开放题）；(b) SFT 导致的 token-level probability recalibration；(c) 模型容量与 benchmark 难度的交互效应。论文需要至少提出一个可检验的机制假说。\n2. **SFT vs. 真实污染的 concern**（呼应 R1-W4）：SFT 注入是高强度、集中式的 exposure，可能引发与自然污染不同的 probability landscape 变化。Min-K++ 逆转是否在自然污染条件下也会出现，需要 observational data 的佐证。\n\n**独立成文的可行性**：如果将 Min-K++ 逆转作为独立发现投稿（短文 / workshop paper / Findings），需要 (1) 更多 benchmark 的覆盖；(2) 机制分析；(3) 对 detection community 的具体 guideline（何时 Min-K++ 可信，何时不可信）。当前嵌入 ContamCal 框架中，这个发现的可见性反而被稀释了。\n\n---\n\n## 修正后评分（基于 R1 描述的完整论文内容）\n\n了解到论文实际包含完整的实验章节（Tables 1-9, Sections 4-6），我修正对实验相关维度的评分：\n\n| 维度 | 原评分（基于不完整 PDF）| 修正评分（基于 R1 描述）| 变化理由 |\n|------|----------------------|----------------------|----------|\n| Soundness | 2/5 | 2.5/5 | 实验存在但有 N1-N3 的严重缺陷 |\n| Excitement | 2.5/5 | 3/5 | Min-K++ 逆转发现有实际价值，但 DCR 重叠和技术增量有限仍是问题 |\n| Overall | 1/5 | 2/5 | 从 \"不可提交\" 上调至 \"resubmit next cycle\"——核心框架有潜力但证据链和 claim scope 都需要大幅修正 |\n| Reproducibility | 1/5 | 2.5/5 | 控制 SFT 协议描述完整（R1 优势 4），但 1.5B/3B 缺失仍影响可复现性 |\n\n**修正后 Overall: 2/5 (Resubmit next cycle)**\n",
  "reviewer_id": "2",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e2095b9-5779-41b1-89db-c8889d3e2d5d",
  "isSidechain": false,
  "requestId": "req_011Cb6cnrEmhZVtQWQkPNPpY",
  "type": "assistant",
  "uuid": "79e67a4f-8a1a-414f-bf8e-ac6692e64e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VpW2WiT5ZHzUGRPhRhUsW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 56313,
      "cache_read_input_tokens": 11841,
      "output_tokens": 5809,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 56313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5809,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 56313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 56313
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 38299
      }
    }
  }
}
```

</details>

---


### Runtime record

_source line 117_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: **[Round 1 — 交叉分享] 请逐条回应 Reviewer 1 的审稿意见**  ⚠️ **重要背景**：Reviewer 1 审阅的是一个更完整的论文版本（包含完整的实验结果、Table 1-9、Section 4-6），而你审阅的 PDF 是一个过期的编译版本（缺少实验章节渲染）。这是提交流程问题，不是你的审稿失误。请基于 Reviewer 1 描述的内…",
  "leafUuid": "79e67a4f-8a1a-414f-bf8e-ac6692e64e7e",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621"
}
```

---


### Runtime record

_source line 118_

```json
{
  "type": "ai-title",
  "aiTitle": "Review contamination-augmented IRT paper for EMNLP",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621"
}
```

---


### Tool result

_source line 119 · 2026-05-16T17:12:16.127Z_

<details><summary>↩ Tool result · `toolu_014NvvevKxZu2k6qgBqwnV7w`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79e67a4f-8a1a-414f-bf8e-ac6692e64e7e",
  "isSidechain": false,
  "promptId": "56687575-614d-4221-9c76-557468d72229",
  "type": "user",
  "uuid": "481e6e59-1af3-4f21-950f-76f2441021bd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "79e67a4f-8a1a-414f-bf8e-ac6692e64e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_2_27d6671a",
  "sessionId": "4c0b8d24-9d0d-40a8-a02e-1cd040850621",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
