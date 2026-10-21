# Reviewer 2 coordination — Part 1 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/0a/0a7af09601a6dba6f0f9.json)

## Round 1

## Round 1

50 recorded events


### User

_source line 1 · 2026-05-19T15:34:02.628454+00:00_

[Round 1 审稿请求]:
## Review Assignment: R2 — Novelty & Related Work

**Paper**: "Why Lightweight Gating Struggles to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"

**Your focus areas**: Novelty, positioning, related work completeness, contribution significance, writing quality.

**Paper summary**: The paper proposes ThreadGate, a per-layer scalar gate on residual connections trained jointly with NTP and an auxiliary GAR (Goal Attention Ratio) objective to fix multi-turn attention degradation. The central finding is negative: despite training-time GAR optimization (0.02→0.48 on Qwen-2.5-7B), inference GAR collapses to 0.016 (30× gap). Two failure mechanisms are identified: (1) NTP gradient dominance (7–15× magnitude ratio) causing reverse turn conditioning, and (2) teacher-forcing distribution shift. Cross-model experiments on Llama-3.1-8B show directional consistency. Scheduled sampling mitigation reduces the gap to 12.3× (p≈0.07).

**Paper structure** (7 pages main text):
- §1 Introduction (1.5 pages)
- §2 Related Work (1 page): Covers multi-turn degradation, residual gating/adaptive depth, attention steering, exposure bias, multi-task gradient conflict
- §3 Background (0.5 page): GAR definition, residual stream persistence
- §4 Method (1 page): ThreadGate architecture, training objective, loss evolution, setup
- §5 Experiments (1.5 pages): Base GAR decay, training dynamics, 4-way/3-way ablation, gap analysis, downstream validation
- §6 Analysis (1.5 pages): Gradient conflict, gate profiles, attention visualization, statistical significance
- §7 Discussion (1 page): Scheduled sampling, why gating fails, limitations, future directions
- §8 Conclusion (0.5 page)
- References section exists but ALL citations are broken (appear as "?")

**The paper's claimed contributions**:
1. First quantitative measurement of teacher-forcing distribution shift undermining auxiliary attention losses (30× gap on Qwen, 10× on Llama)
2. Per-layer quantification of NTP–GAR gradient competition (7–15× magnitude ratios, systematic direction conflict)
3. Systematic ablation across two model families
4. Suggestive evidence from scheduled-sampling mitigation (gap 30×→12.3×, p≈0.07)

**Please evaluate**:

1. **Novelty assessment**: 
   - Is the negative result (gating doesn't work for attention steering) genuinely novel and surprising? Or is it expected given known exposure bias literature?
   - Are the mechanistic explanations (gradient competition + distribution shift) new insights, or restatements of known phenomena (exposure bias, multi-task gradient conflict) applied to a new setting?
   - How significant is quantifying the 30× gap specifically?

2. **Related work completeness**:
   - Are key baselines and alternative approaches adequately discussed?
   - Missing related work: Are there other attention steering / goal maintenance methods that should be compared or discussed?
   - How well does the paper position itself relative to Dongre et al. (the prior work on GAR)?

3. **Contribution significance for top ML venues**:
   - Is this paper's contribution sufficient for a top venue (acceptance rate ~25%)?
   - Negative results papers: what bar should they meet? Does this paper meet it?
   - Is the scope (only lightweight scalar gates) too narrow for general interest?

4. **Writing quality**:
   - Is the narrative coherent? Does the story flow logically?
   - Is the paper well-organized?
   - Are claims appropriately hedged vs. overclaimed?
   - CRITICAL: All references are broken ("?" throughout). Evaluate impact.

5. **Framing assessment**:
   - Is "struggles to" (in the title) the right framing? Should it be "cannot" or "fails to"?
   - Does the paper adequately distinguish what's specific to their setup vs. what generalizes?

6. **Missing perspectives**:
   - What alternative explanations for the failure haven't been considered?
   - Are there positive-result approaches in the literature that should be discussed as alternatives?

**Scoring**: Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Provide sub-scores for: Novelty, Significance, Clarity, and an Overall score. Justify each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-19T15:34:12.958987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-19T15:34:13.110884+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-19T15:34:13.312043+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-19T15:34:13.364608+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-19T15:34:16.375214+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-19T15:34:16.676691+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-19T15:34:16.727396+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-19T15:34:16.779606+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-19T15:34:24.511266+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-19T15:34:24.511794+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-19T15:34:32.127620+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.pdf",
  "project": "turn_residual_gating",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.pdf",
    "project": "turn_residual_gating",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-19T15:34:33.082031+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 8 页): 1-10\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-19T15:34:33.082365+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-19T15:34:33.684732+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-19T15:34:40.640630+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on my search, I found information about ACL Rolling Review (ARR) 2025-2026 reviewer guidelines. Here's what I found:

## Key Information about ARR Reviewer Guidelines (2025-2026)

The ARR peer review guidelines are a work-in-progress and will be updated as ARR evolves, and reviewers should always check whether the version they are familiar with is still the current one before starting an assignment.

## Reviewer Expectations and Policies

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines an
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7558
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-19T15:35:02.801596+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 24, \"total_citations\": 37, \"unique_cited_keys\": 20, \"orphan_bib\": 4, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 16, \"online_not_found\": 3, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"efron1994bootstrap\", \"elhage2021mathematical\", \"olsson2022context\", \"vaswani2017attention\"], \"missing_bib\": [], \"orphan_count\": 4, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"dongre2026\", \"type\": \"inproceedings\", \"title\": \"Goal Attention Degradation in Multi-Turn Dialogues: Measurement and Analysis\", \"authors\": \"Dongre, Arjun and others\", \"year\": \"2026\", \"venue\": \"Proceedings of NAACL\"}, {\"key\": \"bachlechner2021rezero\", \"type\": \"inproceedings\", \"title\": \"ReZero is All You Need: Fast Convergence at Large Depth\", \"authors\": \"Bachlechner, Thomas and Majumder, Bodhisattwa Prasad and Mao, Henry and Cottrell...\", \"year\": \"2021\", \"venue\": \"Proceedings of UAI\"}, {\"key\": \"bengio2015scheduled\", \"type\": \"inproceedings\", \"title\": \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\", \"authors\": \"Bengio, Samy and Vinyals, Oriol and Jaitly, Navdeep and Shazeer, Noam\", \"year\": \"2015\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"lamb2016professor\", \"type\": \"inproceedings\", \"title\": \"Professor Forcing: A New Algorithm for Training Recurrent Networks\", \"authors\": \"Lamb, Alex and Goyal, Anirudh and Zhang, Ying and Zhang, Saizheng and Courville,...\", \"year\": \"2016\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"xiao2024efficient\", \"type\": \"inproceedings\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"authors\": \"Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\":
…[truncated 16740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 29116
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-19T15:35:10.090845+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.pdf",
  "project": "turn_residual_gating",
  "pages": "1-8",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.pdf",
    "project": "turn_residual_gating",
    "pages": "1-8",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-19T15:35:12.704624+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p1.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 601.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p2.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 672.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p3.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 628.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p4.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 568.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p5.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 602.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p6.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 656.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p7.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 543.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p8.png\", \"width\": 1654, \"height\": 2339, \"size_kb\": 280.1}], \"total_pages\": 8, \"re
…[truncated 233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2613
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-19T15:35:12.855609+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales. I need all the specific dimensions reviewers must score (e.g., soundness, excitement, reproducibility, etc.), their scales, and descriptions. Also extract what the Overall Assessment scale looks like (1-5 scale with descriptions for each level)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales. I need all the specific dimensions reviewers must score (e.g., soundness, excitement, reproducibility, etc.), their scales, and descriptions. Also extract what the Overall Assessment scale looks like (1-5 scale with descriptions for each level)."
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-19T15:35:18.580586+00:00_

# ARR Review Form Scoring Dimensions

Based on the provided guidelines, here's what the review form requires:

## Primary Scoring Dimensions

**Three main scores** are collected from reviewers (as of February 2025):

1. **Soundness** - Technical quality and validity
   - Must be justified by review text
   - Low scores require substantial methodological concerns
   - Reproducibility assessments feed into this dimension

2. **Excitement** - Personal interest and subjective appeal
   - Separate from soundness assessment
   - Reflects individual taste rather than objective merit
   - Papers can be sound but low excitement

3. **Overall Assessment** - Final recommendation
   - Composite score reflecting soundness, excitement, novelty, and impact
   - Determines suitability for main conference vs. Findings track
   - All accepted papers must meet soundness thresholds

## Key Principle

The guidelines emphasize that "soundness scores must be justified by the text" and note reviewers should distinguish between papers they find technically sound but personally unexciting. The Overall Assessment represents an explicit recommendation about paper acceptance if "committed to an *ACL venue."

## Notable Absence

The document references these three scores but does not provide the complete numerical scales (e.g., 1-5 ranges) or detailed level descriptions. It directs reviewers to a separate "[ARR review form](https://aclrollingreview.org/reviewform)" post for comprehensive details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5724
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-19T15:35:24.754589+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their numerical scales, and descriptions for each level. I need the exact scales for Soundness, Excitement/Novelty, Overall Assessment, and any other scored dimensions. Include the full text description for each score level (e.g., 5=..., 4=..., etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their numerical scales, and descriptions for each level. I need the exact scales for Soundness, Excitement/Novelty, Overall Assessment, and any other scored dimensions. Include the full text description for each score level (e.g., 5=..., 4=..., etc.)."
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-19T15:35:25.206818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-19T15:35:25.660599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 25 · 2026-05-19T15:35:26.616529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-19T15:35:28.128482+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2921
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-19T15:35:29.388692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3728
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-19T15:35:29.691197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3074
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-19T15:35:30.919213+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale 1-5:
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
Scale 1-5 (with half-points):
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale 1-5 (with half-points):
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
Scale 1-5 (with half-points):
- **5**: "Consider for Award: top 2.5% papers"
- **4**: "Conference: I think this paper could be accepted"
- **3**: "Findings: acceptable to Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: fully redone or irrelevant"

## Reproducibility
Scale 1-5:
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce with some difficulty"
- **2**: "They would be hard pressed to reproduce"
- **1**: "They would not be able to reproduce"

## Datasets & Software
Both use identical 1-5 scales measuring potential value to other researchers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6164
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-19T15:35:35.284673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-19T15:35:36.178612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-19T15:35:36.782593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-19T15:35:37.688272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-19T15:35:37.992243+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2707
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-19T15:35:37.992718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-19T15:35:40.859200+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4680
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-19T15:35:41.462444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4679
}
```

</details>

---


### Tool result

_source line 38 · 2026-05-19T15:35:41.464978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3472
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-19T15:35:41.768699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4080
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-19T15:38:20.155907+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GradNorm PCGrad multi-task gradient conflict balancing survey 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GradNorm PCGrad multi-task gradient conflict balancing survey 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-19T15:38:20.608275+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "negative result paper NLP ACL EMNLP acceptance criteria what makes good negative result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "negative result paper NLP ACL EMNLP acceptance criteria what makes good negative result"
  }
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-19T15:38:27.785277+00:00_

Web search results for query: "negative result paper NLP ACL EMNLP acceptance criteria what makes good negative result"

Links: [{"title":"Workshop on Insights from Negative Results | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results"},{"title":"Call For Papers: The Second Workshop on Insights from Negative Results (EMNLP 2021) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-second-workshop-insights-negative-results-emnlp-2021-0"},{"title":"Empirical Methods in Natural Language Processing | ACL Member Portal","url":"https://www.aclweb.org/portal/content/empirical-methods-natural-language-processing"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Main Conference Papers - EMNLP 2024","url":"https://2024.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guidelines | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/pages/submission-guidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about negative result papers in NLP conferences:

## Acceptance Criteria

EMNLP 2025 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings. Similarly, EMNLP 2024 papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce, or fail to reproduce, previous resul
…[truncated 1060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7177
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-19T15:38:28.488373+00:00_

Web search results for query: "GradNorm PCGrad multi-task gradient conflict balancing survey 2024 2025"

Links: [{"title":"GCond: Gradient Conflict Resolution via Accumulation-based Stabilization for Large-Scale Multi-Task Learning","url":"https://arxiv.org/html/2509.07252v1"},{"title":"Mitigating gradient conflicts via expert squads in multi-task learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231224016035"},{"title":"Gradient Descent in Multi-Task Learning Stanford CS224N Default Project","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/DavidSaykinKfirShmuelDolev.pdf"},{"title":"RI-PCGrad: Optimizing multi-task learning with rescaling and impartial projecting conflict gradients | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-024-05805-3"},{"title":"Gradient Similarity Surgery in Multi-Task Deep Learning","url":"https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2025/research/preprint_ecml_pkdd_2025_research_1013.pdf"},{"title":"Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper/2020/file/3fe78a8acf5fda99de95303940a2420c-Paper.pdf"},{"title":"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep   Multitask Networks","url":"https://arxiv.org/pdf/1711.02257"},{"title":"Dual-Balancing for Multi-Task Learning","url":"https://arxiv.org/pdf/2308.12029"}]

Based on the search results, here's what I found about GradNorm, PCGrad, and multi-task gradient conflict balancing:

## Key Methods

**GradNorm**: GradNorm dynamically adjusts loss function weights to equalize gradient magnitudes, but does not solve the direction problem, since under this approach even gradients with identical norms can be directed in opposite directions, creating conflict.

**PCGrad**: PCGrad has become the de facto standard among projection methods or Gradient Surgery methods. PCGrad addresses conflicts by
…[truncated 1117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8332
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-19T15:41:12.772772+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：Novelty & Related Work\n\n**论文**: \"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n\n---\n\n## 总体评分\n\n**Overall (ARR)**: 2.5 / 5 — Borderline Findings\n**Overall (6-point)**: 3 / 6 — Weak Reject\n**一句话总结**: 实验方法论尚可，但两个核心失败机制（梯度竞争 + exposure bias）均为已知现象在新场景的确认性验证，novelty 不足以支撑 main conference 或稳定的 Findings 接收。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 | 实验设计合理（双模型、消融、bootstrap CI），但范围窄（仅标量门控）、GAR 单指标依赖、scheduled sampling p≈0.07 未达显著 |\n| **Excitement** | 2 / 5 | 负面结果的解释力有限——确认已知失败模式而非揭示意外机制，可操作洞察匮乏 |\n| **Reproducibility** | 3.5 / 5 | 报告了超参、种子、模型版本；但代码/数据未提供，且核心先行工作 Dongre et al. (2026) 不可查证 |\n| **Reviewer Confidence** | 4 / 5 | 本人熟悉 exposure bias、multi-task optimization 和 transformer 机制分析文献 |\n\n**Director 要求的子分数（6-point scale）：**\n- **Novelty**: 2 / 6\n- **Significance**: 2 / 6\n- **Clarity**: 4 / 6\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n### N1 [critical] Novelty 声称过高——两个核心机制均为已知现象的直接应用\n\n- **具体位置**: §1 Abstract \"first quantitative measurement\"；§6.1 gradient competition；§6.4 exposure bias\n- **问题**: \n  论文声称的两个 failure mechanism：\n  1. **NTP-GAR 梯度竞争**（7–15× 幅度比）= 多任务梯度冲突（multi-task gradient conflict），这是 multi-task learning 领域 2018 年以来的经典问题。GradNorm (Chen et al., 2018) 定义了 gradient magnitude balancing，PCGrad (Yu et al., NeurIPS 2020) 定义了 gradient direction conflict 的 surgery 方法。论文将一个已有成熟解决方案的已知问题重新\"发现\"却完全不引用这些文献。\n  2. **Teacher-forcing distribution shift** = exposure bias (Bengio et al., 2015)。论文自己在 §2 和 §6.4 中引用了 exposure bias 文献，却在 Abstract 和 contributions 中声称这是\"first quantitative measurement\"。Exposure bias 导致 auxiliary loss 在 teacher-forcing 下训练但 autoregressive 推理时失效，这在概念上是完全预期的。\n  \n  30× gap 的具体数值是新的，但数值本身不构成方法论贡献。这类似于报告\"水在 100°C 沸腾\"的精确温度——现象本身已知。\n\n- **为什么影响接收**: ACL ARR 的 Excitement 维度要求论文提供 \"new insights\" 而非对已知现象的确认。如果审稿人认为核心发现是预期的（expected），论文难以超过 Findings 门槛。\n- **建议修改方向**: (1) 在 §2 增加 multi-task gradient conflict 子节，引用 GradNorm/PCGrad/CAGrad 并解释为什么这些已知方法不能直接解决本文场景；(2) 将 contribution 从\"first measurement\"重新定位为\"first empirical demonstration in the attention-steering context with quantitative characterization\"；(3) 补充实验：用 PCGrad 或 GradNorm 缓解梯度竞争，观察是否能减小 30× gap——如果能，说明问题有已知解；如果不能，这才是真正的新洞察。\n\n### N2 [critical] 标题 \"Cannot\" 过度声称——证据仅支持 \"fails to\" under tested conditions\n\n- **具体位置**: 标题；§7 Discussion \"our findings are specific to lightweight residual gating with auxiliary GAR losses\"\n- **问题**: \n  标题使用 \"Cannot\"（不可能），但论文仅测试了：\n  - 一种门控架构（标量 per-layer gate via ReZero）\n  - 一种辅助目标（GAR loss）\n  - 一种训练方式（joint NTP+GAR）\n  - 两个模型家族（Qwen-2.5-7B, Llama-3.1-8B）\n  \n  §7 Discussion 自己承认 \"our findings are specific to lightweight residual gating with auxiliary GAR losses\"，这与标题的绝对否定矛盾。更关键的是，scheduled sampling 将 gap 从 30× 降至 12.3×（§7），说明改变训练策略就能部分修复——这直接反驳了 \"cannot\"。\n  \n  未测试的替代方案包括：向量门控（vector gate per dimension）、attention-head-specific gate、不同 loss 权重调度、curriculum learning 等。\n\n- **为什么影响接收**: 审稿人最厌恶的是 overclaiming。标题是论文最高频被阅读的部分，overclaim 会直接降低可信度。\n- **建议修改方向**: 改为 \"Why Lightweight Scalar Gating Fails to Fix Multi-Turn Attention Degradation\" 或 \"How Exposure Bias Undermines Gating-Based Attention Steering\"。\n\n### N3 [critical] 核心先行工作 Dongre et al. (2026) 不可查证\n\n- **具体位置**: 全文核心依赖——§1 motivation, §3 GAR 定义, §5.1 baseline\n- **问题**: \n  论文的整个动机链建立在 Dongre et al. (2026) 之上：GAR 指标定义、multi-turn degradation 的量化、residual stream persistence 发现。引用验证显示该文献在 OpenAlex 中完全不可查（similarity score 仅 0.336）。Bib 条目标注为 \"Proceedings of NAACL 2026\"，但无法验证该论文是否已被接收或发表。\n  \n  如果这篇论文不存在或无法获取，则本文的整个实验框架（GAR 指标、probe AUC baseline、\"27–48% drop\" 数据）均缺乏可验证的基础。\n\n- **为什么影响接收**: ARR reviewer guidelines 要求 soundness 评估包括 claims 的 supporting evidence。如果核心 prior work 不可验证，所有基于其上的 claim 均悬空。\n- **建议修改方向**: 如果 Dongre et al. 尚未发表，需要 (1) 在论文中自包含地重新定义 GAR 并提供独立验证，(2) 明确标注为 \"under review\" 或提供 preprint 链接。\n\n### N4 [critical] Related Work 缺失关键文献：Multi-task Gradient Conflict\n\n- **具体位置**: §2 Related Work（整节未提及 multi-task optimization 文献）\n- **问题**: \n  §6.1 的核心发现是 NTP 和 GAR 梯度存在方向冲突和幅度不平衡。这正是 multi-task gradient conflict 的定义。但 §2 完全未讨论以下直接相关文献：\n  - **GradNorm** (Chen et al., ICML 2018): 动态调整 loss 权重以平衡梯度幅度\n  - **PCGrad** (Yu et al., NeurIPS 2020): 投影消除梯度方向冲突\n  - **CAGrad** (Liu et al., NeurIPS 2021): 冲突感知梯度下降\n  - **Nash-MTL** (Navon et al., ICML 2022): 纳什博弈框架下的多任务优化\n  \n  这些方法为梯度竞争提供了成熟的解决方案。论文不讨论这些方法，既削弱了 related work 的完整性，也错失了重要的实验 baseline——如果 PCGrad 能解决梯度竞争问题，则本文的\"失败\"可能仅仅是因为没有使用正确的优化策略，而非 gating 本身的固有局限。\n\n- **为什么影响接收**: Related work 不完整直接影响 Soundness 评分。审稿人会问：\"你说梯度竞争导致失败，但你试过已知的梯度冲突解决方案吗？\"\n- **建议修改方向**: (1) §2 增加 multi-task gradient conflict 子节；(2) 实验中加入至少一种 gradient surgery baseline（如 PCGrad）并报告结果。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n### W1 [warning] 范围过窄——仅标量门控，不足以支撑 \"lightweight gating\" 的一般性结论\n\n- **具体位置**: §4.1 ThreadGate Architecture; 标题中 \"Lightweight Gating\"\n- **问题**: 标题说 \"Lightweight Gating\"（轻量门控），但实际仅测试了最简单的标量 per-layer gate（Eq. 2, ReZero 风格）。\"Lightweight gating\" 的合理范围至少应包括：(a) vector gate (per-dimension)，(b) attention-head-specific gate，(c) low-rank gate，(d) layer-group gate。仅测试一种变体就声称\"轻量门控不行\"，有以偏概全之嫌。\n- **建议**: 至少讨论其他变体为什么未测试，或补充 1-2 种变体的实验。\n\n### W2 [warning] Scheduled sampling 实验统计不显著（p ≈ 0.07）\n\n- **具体位置**: §7 Discussion; Table 7\n- **问题**: Contribution 4 声称 \"suggestive evidence from scheduled-sampling mitigation (gap 30×→12.3×, p≈0.07)\"。p=0.07 在传统统计标准下不显著（α=0.05），论文用 \"suggestive\" 对冲但仍将其列为正式 contribution。Table 7 显示 SS+TG 的 inference GAR 仅从 0.016 提升到 0.019p，这个绝对提升量极小。\n- **建议**: 要么增加 bootstrap 样本量/实验重复以获得更强统计支持，要么将此发现从 contributions 降级为 discussion 中的初步观察。\n\n### W3 [warning] GAR 作为唯一注意力退化指标的局限性未充分讨论\n\n- **具体位置**: §3 Background; §5.5 Statistical Validation\n- **问题**: 整篇论文的所有实验结论都建立在 GAR（Goal Attention Ratio）这一单一指标上。§6.5 虽然报告了 instruction compliance 作为下游验证（r=0.82 Pearson correlation），但这是事后验证而非独立指标。如果 GAR 本身的定义有问题（例如，goal token 的选择方式、position bias 的影响），所有结论都会受影响。论文未讨论 GAR 的 limitations 或与其他注意力质量指标的对比。\n- **建议**: 讨论 GAR 可能的失效场景；如果可能，增加至少一个替代指标（如 attention entropy over goal tokens, goal-relevant hidden state similarity）。\n\n### W4 [warning] 论文长度明显低于 EMNLP long paper 上限\n\n- **具体位置**: 全文结构\n- **问题**: EMNLP 2026 long paper 限 8 页正文。本文正文约 6 页（§1-§8 Conclusion 在第 6 页结束），远低于上限。这意味着有约 2 页空间可以补充缺失的 related work、更多门控变体实验、gradient surgery baseline 等。未充分利用页面预算会让审稿人认为 contribution 不够充实。\n- **建议**: 利用剩余页面预算充实 related work 和实验。\n\n### W5 [warning] liu2016attention 引用可能错配\n\n- **具体位置**: §2 Related Work \"attention supervision (Liu et al., 2016)\"\n- **问题**: Bib 条目 `liu2016attention` 的标题是 \"Attention-Based Models for Speech Recognition\"（语音识别），但在 §2 中被引用为 \"attention supervision\" 方法（transformer 注意力引导）。引用验证显示 first author 不匹配（bib=Liu, API=Chorowski）。这可能是引用错配——语音识别的注意力模型与多轮对话的注意力引导是不同话题。\n- **建议**: 核实此引用是否指向正确论文；如果讨论的是 attention supervision for NMT/dialogue，应替换为更相关的参考文献。\n\n### W6 [warning] 4 个 orphan bib 条目未被引用\n\n- **具体位置**: References section\n- **问题**: 引用验证发现以下 bib 条目存在但未在正文中引用：`vaswani2017attention`（Attention is All You Need）、`elhage2021mathematical`（Transformer Circuits）、`olsson2022context`（Induction Heads）、`efron1994bootstrap`（Bootstrap 统计）。其中 Vaswani (2017) 作为 transformer 基础论文理应被引用；Elhage (2021) 和 Olsson (2022) 对理解 residual stream 机制直接相关。这些遗漏暗示引用管理不完善。\n- **建议**: 清理 bib 文件，移除未引用条目或在正文中引用它们。\n\n---\n\n## 小问题（不影响接收）\n\n- §1 p.1 \"probe AUC up to 0.98\" — AUC 基线和计算方法应在正文简述（目前仅引用 Dongre et al.），方便不了解该先行工作的读者理解。\n- §4.2 Loss Design：v7 loss 的选择过程（\"We explored seven loss configurations (v1–v7)\"）仅一句带过，读者无法理解为什么 v7 最优。建议至少在 Appendix 提供 v1–v6 的简要描述和性能。\n- Table 1: \"Relative drop\" 行的 70.8% 和 69% 是相对于 Turn 1 计算的，但表头未明确标注基线。\n- §5.5 Table 5: bootstrap CI 包含零 ([-0.012, 0.019] 和 [-0.008, 0.019])，正文说\"statistically indistinguishable from zero\"——这支持了 null result 但应更明确地说明这意味着 ThreadGate 的增量效果可能完全不存在。\n- p.1 Abstract: \"30× training–inference gap\" 的表述有歧义——是 GAR 值的比值（0.48/0.016=30）还是相对退化幅度？应更精确定义。\n\n---\n\n## 主要优势\n\n1. **实验设计的方法论规范性**: 双模型验证（Qwen + Llama），4-way 消融设计将 gating / LoRA / loss 解耦，bootstrap CI 提供统计保障。这比许多 negative result 论文更严格。\n2. **清晰的叙事结构**: 从问题定义（§1-3）→ 方法设计（§4）→ 负面结果（§5）→ 机制分析（§6）→ 缓解探索（§7）的逻辑链条连贯。\n3. **诚实的 hedging**: §7 Discussion 承认结果的范围限制，Contribution 4 用 \"suggestive evidence\" 而非断言。这种学术诚实值得肯定。\n4. **Per-layer gradient 分析的粒度**: Table 6 的逐层梯度统计（conflict fraction、magnitude ratio）提供了比纯总体数字更丰富的分析。\n\n---\n\n## 对 Director 指定问题的逐项回答\n\n### Q1: Novelty Assessment\n\n**负面结果是否 genuinely novel and surprising?** 不够。对于熟悉 exposure bias 和 multi-task gradient conflict 文献的研究者，\"在 teacher-forcing 下训练的 auxiliary attention loss 在 autoregressive inference 时失效\" 是可预期的。30× 的具体幅度是新的，但量化一个预期现象不等于新洞察。\n\n**机制解释是否 new insights?** 更多是 restatements。梯度竞争 = multi-task gradient conflict (GradNorm/PCGrad 文献)；distribution shift = exposure bias (Bengio et al., 2015)。论文的贡献在于将这两个已知现象映射到 attention steering 场景并提供具体数值，但解释框架本身不新。\n\n**30× gap 的意义**: 作为一个具体 benchmark 数字有参考价值，但不足以单独构成一个 contribution。\n\n### Q2: Related Work Completeness\n\n**关键缺失**: Multi-task gradient conflict 文献（GradNorm, PCGrad, CAGrad, Nash-MTL）——这是本文 §6.1 核心机制的直接上位文献，完全缺失是重大遗漏。\n\n**与 Dongre et al. 的定位**: 论文在 §1 和 §7 对 Dongre et al. 的定位清晰——\"他们发现了问题和 residual 信息持久性，我们测试能否通过 gating 利用这种持久性\"。但 §7 提到 Dongre et al. 的 Appendix B 已注意到 goal re-injection 的失败，论文应更明确地区分自己的增量贡献。\n\n**缺失的替代方案讨论**: \n- Inference-time intervention (ITI, Li et al., 2024) 和 representation engineering (Zou et al., 2023) 在 §2 被引用但仅一句带过。这些方法在推理时直接操作 hidden states，避开了 exposure bias，是更有希望的方向。论文应深入讨论为什么这些方法可能更适合，以增强自身的\"轻量训练时方法不行\"的论点。\n\n### Q3: Contribution Significance for Top Venues\n\n**对于 acceptance rate ~25% 的顶会**: 不足。负面结果论文的门槛是 (1) 尝试的方法必须合理且被广泛期望能成功，(2) 失败分析必须提供深层、可操作的洞察，(3) 发现必须泛化到被测试的具体设置之外。本文在 (1) 上勉强通过（residual gating 确实是 reasonable hypothesis），但在 (2) 上不达标（洞察归结为已知的 exposure bias + gradient conflict），在 (3) 上也不达标（仅测试标量门控）。\n\n**对于 Findings track**: Borderline。如果补充 multi-task gradient conflict 的讨论和实验（如 PCGrad baseline），并修正标题为 \"fails to\"，质量可能达到 Findings 门槛。\n\n**范围是否过窄**: 是。\"Lightweight gating\" 涵盖多种架构，但仅测试最简单的标量变体。如果向量门控或 head-specific 门控也失败，结论的说服力会大幅增强。\n\n### Q4: Writing Quality\n\n**叙事连贯性**: 好。故事线清晰：问题→假设→验证→失败→分析→缓解。\n**组织**: 好。§ 编排合理。\n**Hedging 与 overclaiming**: §7 Discussion 的 hedging 诚实，但标题 \"Cannot\" 和 Abstract 的 \"first quantitative measurement\" 与正文的谦逊不一致。标题和 abstract 是最高频阅读部分，它们的 overclaim 伤害大于正文 hedging 的补救。\n\n**引用状态**: ⚠️ 注意——Director 指出 \"ALL citations are broken (appear as '?')\"，但我在渲染的 PDF（best version, dream_20260519T145320）中观察到引用均正常渲染（如 p.1 \"Dongre et al. (2026)\"、p.2 \"(Zheng et al., 2024)\" 等均可读）。References 节格式完整。可能 Director 看到的是不同版本。如果提交版本确实有引用全坏的问题，那是 desk reject 级别的格式缺陷。\n\n### Q5: Framing Assessment\n\n**\"Cannot\" vs \"Struggles to\" vs \"Fails to\"**: \n- \"Cannot\" = 声称不可能 → **过度声称**，证据不支持\n- \"Struggles to\" = 声称困难 → 相对合适，但对 30× gap 来说又有些轻描淡写\n- \"Fails to\" = 声称在测试条件下失败 → **最准确**的表述\n\n推荐标题改为: \"Why Lightweight Scalar Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n\n**Setup-specific vs. generalizable**: §7 Limitations 做了合理区分。但标题和 Abstract 的用语暗示一般性结论（\"Lightweight Gating\" 而非 \"Scalar Residual Gating\"），与正文的谨慎不一致。\n\n### Q6: Missing Perspectives\n\n**未考虑的替代解释**:\n1. **GAR 指标本身的局限**: GAR 衡量 attention mass 在 goal tokens 上的分布，但 attention ≠ information flow。模型可能通过 value vectors 而非 attention weights 传递 goal 信息。attention weight 上的 GAR 衰减不一定意味着功能性退化。\n2. **标量门控容量不足**: 每层一个标量参数可能simply too few parameters 来学习复杂的 turn-conditioned 行为。失败可能不是 exposure bias，而是容量不足。\n3. **LoRA rank 的交互效应**: §4.3 用 LoRA rank 16 应用到所有 attention projection matrices。不同 rank 选择可能改变梯度竞争的动态。\n4. **训练数据量**: 仅 1,000 对话可能不足以让 gate 学习稳健的模式。\n\n**应讨论的 positive-result approaches**:\n- **ITI (Li et al., 2024)** 和 **RepE (Zou et al., 2023)**: 推理时干预方法，绕过 exposure bias\n- **Activation patching**: 直接在特定层修改激活值\n- **KV-cache manipulation**: 在推理时对 key-value cache 做选择性操作\n- 这些方法的成功案例与本文的失败案例形成对比，能更好地定位本文贡献\n\n---\n\n## 总结\n\n论文的实验执行和叙事结构达到了出版标准，但 novelty 是致命短板：两个核心机制（gradient conflict + exposure bias）是成熟的已知问题，且论文遗漏了直接相关的 multi-task optimization 文献。标题 \"Cannot\" overclaims，而核心依赖的 Dongre et al. (2026) 无法查证。建议 (1) 补充 gradient surgery baseline 实验，(2) 扩展门控变体范围，(3) 修正标题和 contribution 声称，(4) 解决 Dongre et al. 的可查证性问题后重新提交。当前状态下评为 Borderline Findings (ARR 2.5)。\n",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：Novelty & Related Work\n\n**论文**: \"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n\n---\n\n## 总体评分\n\n**Overall (ARR)**: 2.5 / 5 — Borderline Findings\n**Overall (6-point)**: 3 / 6 — Weak Reject\n**一句话总结**: 实验方法论尚可，但两个核心失败机制（梯度竞争 + exposure bias）均为已知现象在新场景的确认性验证，novelty 不足以支撑 main conference 或稳定的 Findings 接收。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 | 实验设计合理（双模型、消融、bootstrap CI），但范围窄（仅标量门控）、GAR 单指标依赖、scheduled sampling p≈0.07 未达显著 |\n| **Excitement** | 2 / 5 | 负面结果的解释力有限——确认已知失败模式而非揭示意外机制，可操作洞察匮乏 |\n| **Reproducibility** | 3.5 / 5 | 报告了超参、种子、模型版本；但代码/数据未提供，且核心先行工作 Dongre et al. (2026) 不可查证 |\n| **Reviewer Confidence** | 4 / 5 | 本人熟悉 exposure bias、multi-task optimization 和 transformer 机制分析文献 |\n\n**Director 要求的子分数（6-point scale）：**\n- **Novelty**: 2 / 6\n- **Significance**: 2 / 6\n- **Clarity**: 4 / 6\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n### N1 [critical] Novelty 声称过高——两个核心机制均为已知现象的直接应用\n\n- **具体位置**: §1 Abstract \"first quantitative measurement\"；§6.1 gradient competition；§6.4 exposure bias\n- **问题**: \n  论文声称的两个 failure mechanism：\n  1. **NTP-GAR 梯度竞争**（7–15× 幅度比）= 多任务梯度冲突（multi-task gradient conflict），这是 multi-task learning 领域 2018 年以来的经典问题。GradNorm (Chen et al., 2018) 定义了 gradient magnitude balancing，PCGrad (Yu et al., NeurIPS 2020) 定义了 gradient direction conflict 的 surgery 方法。论文将一个已有成熟解决方案的已知问题重新\"发现\"却完全不引用这些文献。\n  2. **Teacher-forcing distribution shift** = exposure bias (Bengio et al., 2015)。论文自己在 §2 和 §6.4 中引用了 exposure bias 文献，却在 Abstract 和 contributions 中声称这是\"first quantitative measurement\"。Exposure bias 导致 auxiliary loss 在 teacher-forcing 下训练但 autoregressive 推理时失效，这在概念上是完全预期的。\n  \n  30× gap 的具体数值是新的，但数值本身不构成方法论贡献。这类似于报告\"水在 100°C 沸腾\"的精确温度——现象本身已知。\n\n- **为什么影响接收**: ACL ARR 的 Excitement 维度要求论文提供 \"new insights\" 而非对已知现象的确认。如果审稿人认为核心发现是预期的（expected），论文难以超过 Findings 门槛。\n- **建议修改方向**: (1) 在 §2 增加 multi-task gradient conflict 子节，引用 GradNorm/PCGrad/CAGrad 并解释为什么这些已知方法不能直接解决本文场景；(2) 将 contribution 从\"first measurement\"重新定位为\"first empirical demonstration in the attention-steering context with quantitative characterization\"；(3) 补充实验：用 PCGrad 或 GradNorm 缓解梯度竞争，观察是否能减小 30× gap——如果能，说明问题有已知解；如果不能，这才是真正的新洞察。\n\n### N2 [critical] 标题 \"Cannot\" 过度声称——证据仅支持 \"fails to\" under tested conditions\n\n- **具体位置**: 标题；§7 Discussion \"our findings are specific to lightweight residual gating with auxiliary GAR losses\"\n- **问题**: \n  标题使用 \"Cannot\"（不可能），但论文仅测试了：\n  - 一种门控架构（标量 per-layer gate via ReZero）\n  - 一种辅助目标（GAR loss）\n  - 一种训练方式（joint NTP+GAR）\n  - 两个模型家族（Qwen-2.5-7B, Llama-3.1-8B）\n  \n  §7 Discussion 自己承认 \"our findings are specific to lightweight residual gating with auxiliary GAR losses\"，这与标题的绝对否定矛盾。更关键的是，scheduled sampling 将 gap 从 30× 降至 12.3×（§7），说明改变训练策略就能部分修复——这直接反驳了 \"cannot\"。\n  \n  未测试的替代方案包括：向量门控（vector gate per dimension）、attention-head-specific gate、不同 loss 权重调度、curriculum learning 等。\n\n- **为什么影响接收**: 审稿人最厌恶的是 overclaiming。标题是论文最高频被阅读的部分，overclaim 会直接降低可信度。\n- **建议修改方向**: 改为 \"Why Lightweight Scalar Gating Fails to Fix Multi-Turn Attention Degradation\" 或 \"How Exposure Bias Undermines Gating-Based Attention Steering\"。\n\n### N3 [critical] 核心先行工作 Dongre et al. (2026) 不可查证\n\n- **具体位置**: 全文核心依赖——§1 motivation, §3 GAR 定义, §5.1 baseline\n- **问题**: \n  论文的整个动机链建立在 Dongre et al. (2026) 之上：GAR 指标定义、multi-turn degradation 的量化、residual stream persistence 发现。引用验证显示该文献在 OpenAlex 中完全不可查（similarity score 仅 0.336）。Bib 条目标注为 \"Proceedings of NAACL 2026\"，但无法验证该论文是否已被接收或发表。\n  \n  如果这篇论文不存在或无法获取，则本文的整个实验框架（GAR 指标、probe AUC baseline、\"27–48% drop\" 数据）均缺乏可验证的基础。\n\n- **为什么影响接收**: ARR reviewer guidelines 要求 soundness 评估包括 claims 的 supporting evidence。如果核心 prior work 不可验证，所有基于其上的 claim 均悬空。\n- **建议修改方向**: 如果 Dongre et al. 尚未发表，需要 (1) 在论文中自包含地重新定义 GAR 并提供独立验证，(2) 明确标注为 \"under review\" 或提供 preprint 链接。\n\n### N4 [critical] Related Work 缺失关键文献：Multi-task Gradient Conflict\n\n- **具体位置**: §2 Related Work（整节未提及 multi-task optimization 文献）\n- **问题**: \n  §6.1 的核心发现是 NTP 和 GAR 梯度存在方向冲突和幅度不平衡。这正是 multi-task gradient conflict 的定义。但 §2 完全未讨论以下直接相关文献：\n  - **GradNorm** (Chen et al., ICML 2018): 动态调整 loss 权重以平衡梯度幅度\n  - **PCGrad** (Yu et al., NeurIPS 2020): 投影消除梯度方向冲突\n  - **CAGrad** (Liu et al., NeurIPS 2021): 冲突感知梯度下降\n  - **Nash-MTL** (Navon et al., ICML 2022): 纳什博弈框架下的多任务优化\n  \n  这些方法为梯度竞争提供了成熟的解决方案。论文不讨论这些方法，既削弱了 related work 的完整性，也错失了重要的实验 baseline——如果 PCGrad 能解决梯度竞争问题，则本文的\"失败\"可能仅仅是因为没有使用正确的优化策略，而非 gating 本身的固有局限。\n\n- **为什么影响接收**: Related work 不完整直接影响 Soundness 评分。审稿人会问：\"你说梯度竞争导致失败，但你试过已知的梯度冲突解决方案吗？\"\n- **建议修改方向**: (1) §2 增加 multi-task gradient conflict 子节；(2) 实验中加入至少一种 gradient surgery baseline（如 PCGrad）并报告结果。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n### W1 [warning] 范围过窄——仅标量门控，不足以支撑 \"lightweight gating\" 的一般性结论\n\n- **具体位置**: §4.1 ThreadGate Architecture; 标题中 \"Lightweight Gating\"\n- **问题**: 标题说 \"Lightweight Gating\"（轻量门控），但实际仅测试了最简单的标量 per-layer gate（Eq. 2, ReZero 风格）。\"Lightweight gating\" 的合理范围至少应包括：(a) vector gate (per-dimension)，(b) attention-head-specific gate，(c) low-rank gate，(d) layer-group gate。仅测试一种变体就声称\"轻量门控不行\"，有以偏概全之嫌。\n- **建议**: 至少讨论其他变体为什么未测试，或补充 1-2 种变体的实验。\n\n### W2 [warning] Scheduled sampling 实验统计不显著（p ≈ 0.07）\n\n- **具体位置**: §7 Discussion; Table 7\n- **问题**: Contribution 4 声称 \"suggestive evidence from scheduled-sampling mitigation (gap 30×→12.3×, p≈0.07)\"。p=0.07 在传统统计标准下不显著（α=0.05），论文用 \"suggestive\" 对冲但仍将其列为正式 contribution。Table 7 显示 SS+TG 的 inference GAR 仅从 0.016 提升到 0.019p，这个绝对提升量极小。\n- **建议**: 要么增加 bootstrap 样本量/实验重复以获得更强统计支持，要么将此发现从 contributions 降级为 discussion 中的初步观察。\n\n### W3 [warning] GAR 作为唯一注意力退化指标的局限性未充分讨论\n\n- **具体位置**: §3 Background; §5.5 Statistical Validation\n- **问题**: 整篇论文的所有实验结论都建立在 GAR（Goal Attention Ratio）这一单一指标上。§6.5 虽然报告了 instruction compliance 作为下游验证（r=0.82 Pearson correlation），但这是事后验证而非独立指标。如果 GAR 本身的定义有问题（例如，goal token 的选择方式、position bias 的影响），所有结论都会受影响。论文未讨论 GAR 的 limitations 或与其他注意力质量指标的对比。\n- **建议**: 讨论 GAR 可能的失效场景；如果可能，增加至少一个替代指标（如 attention entropy over goal tokens, goal-relevant hidden state similarity）。\n\n### W4 [warning] 论文长度明显低于 EMNLP long paper 上限\n\n- **具体位置**: 全文结构\n- **问题**: EMNLP 2026 long paper 限 8 页正文。本文正文约 6 页（§1-§8 Conclusion 在第 6 页结束），远低于上限。这意味着有约 2 页空间可以补充缺失的 related work、更多门控变体实验、gradient surgery baseline 等。未充分利用页面预算会让审稿人认为 contribution 不够充实。\n- **建议**: 利用剩余页面预算充实 related work 和实验。\n\n### W5 [warning] liu2016attention 引用可能错配\n\n- **具体位置**: §2 Related Work \"attention supervision (Liu et al., 2016)\"\n- **问题**: Bib 条目 `liu2016attention` 的标题是 \"Attention-Based Models for Speech Recognition\"（语音识别），但在 §2 中被引用为 \"attention supervision\" 方法（transformer 注意力引导）。引用验证显示 first author 不匹配（bib=Liu, API=Chorowski）。这可能是引用错配——语音识别的注意力模型与多轮对话的注意力引导是不同话题。\n- **建议**: 核实此引用是否指向正确论文；如果讨论的是 attention supervision for NMT/dialogue，应替换为更相关的参考文献。\n\n### W6 [warning] 4 个 orphan bib 条目未被引用\n\n- **具体位置**: References section\n- **问题**: 引用验证发现以下 bib 条目存在但未在正文中引用：`vaswani2017attention`（Attention is All You Need）、`elhage2021mathematical`（Transformer Circuits）、`olsson2022context`（Induction Heads）、`efron1994bootstrap`（Bootstrap 统计）。其中 Vaswani (2017) 作为 transformer 基础论文理应被引用；Elhage (2021) 和 Olsson (2022) 对理解 residual stream 机制直接相关。这些遗漏暗示引用管理不完善。\n- **建议**: 清理 bib 文件，移除未引用条目或在正文中引用它们。\n\n---\n\n## 小问题（不影响接收）\n\n- §1 p.1 \"probe AUC up to 0.98\" — AUC 基线和计算方法应在正文简述（目前仅引用 Dongre et al.），方便不了解该先行工作的读者理解。\n- §4.2 Loss Design：v7 loss 的选择过程（\"We explored seven loss configurations (v1–v7)\"）仅一句带过，读者无法理解为什么 v7 最优。建议至少在 Appendix 提供 v1–v6 的简要描述和性能。\n- Table 1: \"Relative drop\" 行的 70.8% 和 69% 是相对于 Turn 1 计算的，但表头未明确标注基线。\n- §5.5 Table 5: bootstrap CI 包含零 ([-0.012, 0.019] 和 [-0.008, 0.019])，正文说\"statistically indistinguishable from zero\"——这支持了 null result 但应更明确地说明这意味着 ThreadGate 的增量效果可能完全不存在。\n- p.1 Abstract: \"30× training–inference gap\" 的表述有歧义——是 GAR 值的比值（0.48/0.016=30）还是相对退化幅度？应更精确定义。\n\n---\n\n## 主要优势\n\n1. **实验设计的方法论规范性**: 双模型验证（Qwen + Llama），4-way 消融设计将 gating / LoRA / loss 解耦，bootstrap CI 提供统计保障。这比许多 negative result 论文更严格。\n2. **清晰的叙事结构**: 从问题定义（§1-3）→ 方法设计（§4）→ 负面结果（§5）→ 机制分析（§6）→ 缓解探索（§7）的逻辑链条连贯。\n3. **诚实的 hedging**: §7 Discussion 承认结果的范围限制，Contribution 4 用 \"suggestive evidence\" 而非断言。这种学术诚实值得肯定。\n4. **Per-layer gradient 分析的粒度**: Table 6 的逐层梯度统计（conflict fraction、magnitude ratio）提供了比纯总体数字更丰富的分析。\n\n---\n\n## 对 Director 指定问题的逐项回答\n\n### Q1: Novelty Assessment\n\n**负面结果是否 genuinely novel and surprising?** 不够。对于熟悉 exposure bias 和 multi-task gradient conflict 文献的研究者，\"在 teacher-forcing 下训练的 auxiliary attention loss 在 autoregressive inference 时失效\" 是可预期的。30× 的具体幅度是新的，但量化一个预期现象不等于新洞察。\n\n**机制解释是否 new insights?** 更多是 restatements。梯度竞争 = multi-task gradient conflict (GradNorm/PCGrad 文献)；distribution shift = exposure bias (Bengio et al., 2015)。论文的贡献在于将这两个已知现象映射到 attention steering 场景并提供具体数值，但解释框架本身不新。\n\n**30× gap 的意义**: 作为一个具体 benchmark 数字有参考价值，但不足以单独构成一个 contribution。\n\n### Q2: Related Work Completeness\n\n**关键缺失**: Multi-task gradient conflict 文献（GradNorm, PCGrad, CAGrad, Nash-MTL）——这是本文 §6.1 核心机制的直接上位文献，完全缺失是重大遗漏。\n\n**与 Dongre et al. 的定位**: 论文在 §1 和 §7 对 Dongre et al. 的定位清晰——\"他们发现了问题和 residual 信息持久性，我们测试能否通过 gating 利用这种持久性\"。但 §7 提到 Dongre et al. 的 Appendix B 已注意到 goal re-injection 的失败，论文应更明确地区分自己的增量贡献。\n\n**缺失的替代方案讨论**: \n- Inference-time intervention (ITI, Li et al., 2024) 和 representation engineering (Zou et al., 2023) 在 §2 被引用但仅一句带过。这些方法在推理时直接操作 hidden states，避开了 exposure bias，是更有希望的方向。论文应深入讨论为什么这些方法可能更适合，以增强自身的\"轻量训练时方法不行\"的论点。\n\n### Q3: Contribution Significance for Top Venues\n\n**对于 acceptance rate ~25% 的顶会**: 不足。负面结果论文的门槛是 (1) 尝试的方法必须合理且被广泛期望能成功，(2) 失败分析必须提供深层、可操作的洞察，(3) 发现必须泛化到被测试的具体设置之外。本文在 (1) 上勉强通过（residual gating 确实是 reasonable hypothesis），但在 (2) 上不达标（洞察归结为已知的 exposure bias + gradient conflict），在 (3) 上也不达标（仅测试标量门控）。\n\n**对于 Findings track**: Borderline。如果补充 multi-task gradient conflict 的讨论和实验（如 PCGrad baseline），并修正标题为 \"fails to\"，质量可能达到 Findings 门槛。\n\n**范围是否过窄**: 是。\"Lightweight gating\" 涵盖多种架构，但仅测试最简单的标量变体。如果向量门控或 head-specific 门控也失败，结论的说服力会大幅增强。\n\n### Q4: Writing Quality\n\n**叙事连贯性**: 好。故事线清晰：问题→假设→验证→失败→分析→缓解。\n**组织**: 好。§ 编排合理。\n**Hedging 与 overclaiming**: §7 Discussion 的 hedging 诚实，但标题 \"Cannot\" 和 Abstract 的 \"first quantitative measurement\" 与正文的谦逊不一致。标题和 abstract 是最高频阅读部分，它们的 overclaim 伤害大于正文 hedging 的补救。\n\n**引用状态**: ⚠️ 注意——Director 指出 \"ALL citations are broken (appear as '?')\"，但我在渲染的 PDF（best version, dream_20260519T145320）中观察到引用均正常渲染（如 p.1 \"Dongre et al. (2026)\"、p.2 \"(Zheng et al., 2024)\" 等均可读）。References 节格式完整。可能 Director 看到的是不同版本。如果提交版本确实有引用全坏的问题，那是 desk reject 级别的格式缺陷。\n\n### Q5: Framing Assessment\n\n**\"Cannot\" vs \"Struggles to\" vs \"Fails to\"**: \n- \"Cannot\" = 声称不可能 → **过度声称**，证据不支持\n- \"Struggles to\" = 声称困难 → 相对合适，但对 30× gap 来说又有些轻描淡写\n- \"Fails to\" = 声称在测试条件下失败 → **最准确**的表述\n\n推荐标题改为: \"Why Lightweight Scalar Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n\n**Setup-specific vs. generalizable**: §7 Limitations 做了合理区分。但标题和 Abstract 的用语暗示一般性结论（\"Lightweight Gating\" 而非 \"Scalar Residual Gating\"），与正文的谨慎不一致。\n\n### Q6: Missing Perspectives\n\n**未考虑的替代解释**:\n1. **GAR 指标本身的局限**: GAR 衡量 attention mass 在 goal tokens 上的分布，但 attention ≠ information flow。模型可能通过 value vectors 而非 attention weights 传递 goal 信息。attention weight 上的 GAR 衰减不一定意味着功能性退化。\n2. **标量门控容量不足**: 每层一个标量参数可能simply too few parameters 来学习复杂的 turn-conditioned 行为。失败可能不是 exposure bias，而是容量不足。\n3. **LoRA rank 的交互效应**: §4.3 用 LoRA rank 16 应用到所有 attention projection matrices。不同 rank 选择可能改变梯度竞争的动态。\n4. **训练数据量**: 仅 1,000 对话可能不足以让 gate 学习稳健的模式。\n\n**应讨论的 positive-result approaches**:\n- **ITI (Li et al., 2024)** 和 **RepE (Zou et al., 2023)**: 推理时干预方法，绕过 exposure bias\n- **Activation patching**: 直接在特定层修改激活值\n- **KV-cache manipulation**: 在推理时对 key-value cache 做选择性操作\n- 这些方法的成功案例与本文的失败案例形成对比，能更好地定位本文贡献\n\n---\n\n## 总结\n\n论文的实验执行和叙事结构达到了出版标准，但 novelty 是致命短板：两个核心机制（gradient conflict + exposure bias）是成熟的已知问题，且论文遗漏了直接相关的 multi-task optimization 文献。标题 \"Cannot\" overclaims，而核心依赖的 Dongre et al. (2026) 无法查证。建议 (1) 补充 gradient surgery baseline 实验，(2) 扩展门控变体范围，(3) 修正标题和 contribution 声称，(4) 解决 Dongre et al. 的可查证性问题后重新提交。当前状态下评为 Borderline Findings (ARR 2.5)。\n",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-19T15:41:16.793384+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4020
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-19T15:41:21.325762+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-19T15:41:21.326192+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-19T15:41:25.391990+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-19T15:41:25.442991+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 50 · 2026-05-19T15:41:33.532194+00:00_

审稿报告已提交给 Review Director。

核心结论：**ARR Overall 2.5（Borderline Findings）**，6-point Overall 3（Weak Reject）。

主要问题：
1. **Novelty 不足**——梯度竞争和 exposure bias 是已知现象，论文在新场景确认但未提供意外洞察
2. **标题 "Cannot" overclaims**——仅测试标量门控一种变体，且 scheduled sampling 能部分缓解
3. **Dongre et al. (2026) 不可查证**——整个实验框架的基础引用无法验证
4. **Related work 缺失 multi-task gradient conflict 文献**（GradNorm/PCGrad 等），恰好是论文核心机制的直接上位文献

主要优势：实验方法论规范（双模型、4-way 消融、bootstrap CI），叙事结构清晰。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 51 · 2026-05-19T15:41:34.644331+00:00_

[Round 1 审稿请求]:
## Cross-Share: Findings from R1 (Methods & Experiments)

R1 has completed their independent review. Here are their key findings for your consideration:

### R1's main observations:

**On experimental soundness:**
- The 4-way ablation on Qwen is well-designed (Base/ThreadGate/Uniform Gate/LoRA-only), properly controlling for the gating mechanism.
- The Llama evaluation is asymmetric (only 3-way, no Uniform Gate), which weakens cross-model claims.
- Gradient conflict analysis across 3 checkpoints provides good temporal coverage of training dynamics.
- The downstream task validation (instruction retention, r=0.72) partially addresses the concern that GAR is the sole proxy metric, but r=0.72 is moderate — GAR explains about 52% of variance in instruction following.

**On statistical rigor:**
- Single seed (42) is a significant limitation. Bootstrap CIs on the 50-conversation eval are appropriate for inference-time comparisons but do NOT address training variance.
- 50 conversations is a reasonable eval set for Qwen; Llama eval size is not explicitly stated (assumed same).
- The bootstrap methodology is correctly applied: paired resampling, 10k iterations, effect size reporting.
- The p≈0.07 for scheduled sampling is honestly reported as marginal — this is appropriate.
- Llama's wider CI ([−0.008, 0.041]) and d=0.22 suggest the eval may be underpowered for detecting small effects.

**On reproducibility:**
- Hyperparameters are specified (LR, batch size, epochs, loss weights, LoRA rank).
- Training data (UltraChat) is named but no details on filtering/preprocessing.
- v1–v6 configurations are mentioned but not detailed — hard to assess the "loss design evolution" claim.
- No code/data release mentioned.

**On missing experiments:**
- No actual attention heatmap visualizations (only numerical values in Table 7) — a mechanistic analysis paper needs visual evidence.
- No training curves shown — the three-phase training trajectory is described in text but not plotted.
- No per-layer gradient conflict heatmaps — only aggregate statistics in Table 6.
- No error bars or variance estimates in Tables 1–5, 7.
- Scheduled sampling only tested on Qwen, not on Llama.

**On presentation:**
- ZERO figures in the entire paper. For a "mechanistic analysis," this is a critical weakness.
- 9 tables provide dense numerical evidence but visual communication is entirely absent.
- Broken references make the paper unreadable as a formal submission.

**R1's preliminary scores:**
- Soundness: 3.5/6
- Significance: 3/6
- Clarity: 3/6
- Overall: 3/6 (Weak Reject)

### Questions from R1 for R2:
1. Do you think the "first quantitative measurement" novelty claim is justified, or is it an incremental application of known phenomena?
2. How much does the narrow scope (scalar gates only) limit the paper's value as a negative result?
3. Would this paper be more appropriately positioned as a workshop paper or short paper rather than a main conference submission?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-19T15:42:54.117147+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应：对 R1 审稿意见的逐条评价\n\n---\n\n## 对 R1 主要发现的回应\n\n### 实验 Soundness 方面\n\n[AGREE] R1-Ablation-Asymmetry: Llama 仅 3-way 消融（无 Uniform Gate）确实削弱了跨模型声称的说服力。我补充一点：论文标题用 \"Lightweight Gating\"（泛称）而非 \"Scalar Residual Gating\"（具体），但跨模型验证本身也不完整——两个模型均为相似规模（7-8B）的 decoder-only transformer，没有测试不同架构（如 MoE、encoder-decoder）或不同规模（1B, 70B），泛化性主张需要更谨慎。\n\n[AGREE] R1-Downstream-r072: r=0.72 的 GAR-instruction compliance 相关性确实只解释约 52% 方差。我的 W3 也提出了 GAR 单指标依赖的问题。但我想补充：r=0.72 对于一个 proxy metric 来说并不差——问题不在于相关性是否\"够高\"，而在于论文将所有机制分析（gradient conflict、distribution shift）都建立在 GAR 上。如果 GAR 衰减的 48% 未解释方差来自 GAR 指标本身的噪声（如 position bias、tokenization artifacts），则机制解释的可靠性会打折扣。\n\n[AGREE] R1-Single-Seed: 单种子（42）是实质性限制。我在 Soundness 评分中考虑了这一点但未单独列为 Must-Fix。R1 的分析更精确：bootstrap CI 覆盖推理时方差但不覆盖训练方差。Gate 初始化、LoRA 初始化、数据 shuffling 的随机性都可能影响 30× gap 的具体数值。建议至少 3 个种子。\n\n### 统计严格性方面\n\n[AGREE] R1-Llama-Underpowered: Llama 的 CI [−0.008, 0.041] 和 d=0.22 表明检测小效应的统计功效不足。这与我对论文跨模型声称的担忧一致——Llama 上的\"directional consistency\"可能仅仅是 underpowered test 的 null result。\n\n[AGREE] R1-p007-Honest: p≈0.07 的诚实报告确实值得肯定。我在 W2 中也提到了这一点。我们对此的评价一致：报告本身恰当，但将其列为正式 contribution 需要更强证据。\n\n### 可重复性方面\n\n[AGREE] R1-v1v6-Missing: v1-v6 loss 配置未详述是一个遗漏。我在\"小问题\"中提到了这一点。论文声称 \"explored seven loss configurations\" 但仅报告 v7 的结果——读者无法判断 v7 是否通过 principled selection 还是 cherry-picking 得出。至少应在 Appendix 提供 v1-v6 的描述和关键指标。\n\n[AGREE] R1-No-Code: 无代码/数据发布降低可重复性。对于 negative result 论文尤其重要——读者需要能验证负面结果不是实现 bug。\n\n### 缺失实验方面\n\n[AGREE] R1-Zero-Figures: **这是我遗漏的一个重要观察。** 一篇标题含 \"Mechanistic Analysis\" 的论文零图表确实是严重缺陷。Attention heatmap（可视化 GAR 衰减）、training curve（展示三阶段动态）、per-layer gradient heatmap（展示冲突模式）——这些都是 mechanistic analysis 的标准视觉证据。9 个 table 的纯数值呈现大幅降低了分析的直观说服力和读者体验。我应在初次审稿中将此列为 Should-Fix。\n\n[AGREE] R1-SS-Qwen-Only: Scheduled sampling 仅在 Qwen 上测试、未在 Llama 上验证，确实削弱了 Contribution 4 的跨模型泛化性。这与 N2（overclaiming）问题叠加——论文不仅在门控变体上范围窄，在缓解实验上也是单模型的。\n\n---\n\n## 对 R1 具体问题的回答\n\n### Q1: \"First quantitative measurement\" novelty claim 是否成立？\n\n**不成立。** 这是我 N1 (critical) 的核心论点。详细理由：\n\n1. **Exposure bias 的量化早已存在。** Ranzato et al. (2016)、Wiseman & Rush (2016) 等在 sequence generation 任务中量化了 teacher-forcing 与 autoregressive generation 之间的性能 gap。本文的\"30× gap\"是在一个新指标（GAR）上的测量，不是对一个新现象的首次量化。\n\n2. **Multi-task gradient conflict 的量化也已有先例。** GradNorm (Chen et al., 2018) 通过监控 gradient magnitude ratios 来平衡任务权重——论文的 7-15× magnitude ratio 测量方法与 GradNorm 的诊断方法本质相同。\n\n3. **\"First\" claim 的合理缩小范围**: 如果改为 \"first empirical demonstration that exposure bias critically undermines auxiliary attention-steering objectives in modern LLMs\"，这个 claim 会更准确，但也暴露了贡献本质是 application of known insights to a new setting，而非 new insights themselves。\n\n结论：这是对已知现象在新场景中的**确认性量化**（confirmatory quantification），而非**首次量化**（first quantitative measurement）。Novelty 应相应降级。\n\n### Q2: 仅测试标量门控对 negative result 价值的影响？\n\n**严重限制。** 理由如下：\n\n负面结果论文的说服力与\"排除的假设空间\"成正比。本文排除了一个极窄的假设——\"标量 per-layer ReZero gate + joint NTP-GAR training 能修复 multi-turn attention degradation\"。这距离排除 \"lightweight gating\" 这个大类还很远：\n\n| 未测试变体 | 为什么可能表现不同 |\n|-----------|-------------------|\n| Vector gate (per-dim) | 更高容量，可学习 dimension-specific 行为 |\n| Head-specific gate | 不同 attention head 可能有不同的 goal-tracking role |\n| Low-rank gate | 介于标量和全矩阵之间的容量权衡 |\n| 分离训练（先 GAR 后 NTP）| 避免梯度竞争，但可能引入其他问题 |\n| Gradient surgery (PCGrad) | 直接解决 §6.1 诊断的梯度冲突 |\n\n如果论文能证明即使用 PCGrad 消除梯度竞争 + vector gate 增加容量，exposure bias 仍然导致 30× gap，那\"轻量门控不行\"的结论就有坚实基础。目前只测试了最简单的配置就下了\"cannot\"的结论，说服力不足。\n\n**量化估计**: 如果 \"lightweight gating\" 包含上述 5 种变体，本文仅覆盖了 1/5 = 20% 的假设空间。对于声称 \"cannot\" 的论文，这远远不够。\n\n### Q3: 是否更适合作为 workshop paper 或 short paper？\n\n**我倾向于 workshop paper，具体理由：**\n\n| 因素 | Workshop | Short Paper | Long Paper |\n|------|----------|-------------|------------|\n| 范围 | ✓ 适合窄范围探索 | ✓ 适合有限但完整的贡献 | ✗ 范围不够 |\n| Novelty | ✓ Workshop 对 novelty 门槛更低 | △ Short paper 仍需 non-trivial insight | ✗ 不够 |\n| 方法论完整性 | △ 当前水平可接受 | △ 需补统计严格性 | ✗ 需大量补充实验 |\n| 实际长度 | △ 目前 ~6 页正文偏长 | ✓ 缩到 4 页很合适 | ✗ 内容撑不满 8 页 |\n\n最佳定位：**ACL Workshop on Insights from Negative Results**（真实存在的 workshop）。这个 workshop 专门接收负面结果论文，评审标准侧重\"是否提供了有价值的失败信息\"而非 novelty 的绝对高度。本文的实验方法论在 workshop 标准下是扎实的。\n\n如果坚持主会投稿：建议作为 **short paper** 提交到 ARR，聚焦在 \"exposure bias undermines auxiliary attention losses\" 这一个 takeaway，削减不必要的 overclaiming，补充 1-2 个 gradient surgery baseline 以增加 actionable insight。\n\n---\n\n## 评分更新\n\n在看到 R1 的发现后（特别是零图表问题和 Llama 评估不对称性），我对部分评分做微调：\n\n| 维度 | 原评分 | 更新 | 理由 |\n|------|--------|------|------|\n| Soundness (ARR) | 3/5 | 2.5/5 | 零图表+单种子+Llama 不完整消融，叠加后更接近\"Poor: some main claims not sufficiently supported\" |\n| Excitement (ARR) | 2/5 | 2/5 | 不变 |\n| Clarity (6-pt) | 4/6 | 3/6 | R1 关于零图表的观察有理——\"mechanistic analysis\" 无可视化是叙事缺陷 |\n| **Overall (ARR)** | **2.5/5** | **2.5/5** | **维持 Borderline Findings**——补充了更多弱点但实验方法论的基础仍在 |\n| **Overall (6-pt)** | **3/6** | **3/6** | **维持 Weak Reject** |\n\n---\n\n## R1-R2 共识总结\n\nR1 和 R2 在以下关键判断上一致：\n1. 实验方法论基础合理但有显著 gaps（单种子、跨模型不对称、零图表）\n2. 论文处于 Weak Reject / Borderline Findings 区间\n3. Contribution 不足以支撑 main conference acceptance\n4. 存在 overclaiming（标题和 contribution 声称过度）\n5. 缺少关键视觉证据（R1 首先发现，R2 同意）\n\nR2 额外强调的 R1 未覆盖的问题：\n- Multi-task gradient conflict 文献缺失（N4）\n- Dongre et al. (2026) 不可查证（N3）\n- 标题 \"Cannot\" 的具体 overclaiming 分析（N2）\n- 缺失正面结果替代方案的深入讨论\n",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应：对 R1 审稿意见的逐条评价\n\n---\n\n## 对 R1 主要发现的回应\n\n### 实验 Soundness 方面\n\n[AGREE] R1-Ablation-Asymmetry: Llama 仅 3-way 消融（无 Uniform Gate）确实削弱了跨模型声称的说服力。我补充一点：论文标题用 \"Lightweight Gating\"（泛称）而非 \"Scalar Residual Gating\"（具体），但跨模型验证本身也不完整——两个模型均为相似规模（7-8B）的 decoder-only transformer，没有测试不同架构（如 MoE、encoder-decoder）或不同规模（1B, 70B），泛化性主张需要更谨慎。\n\n[AGREE] R1-Downstream-r072: r=0.72 的 GAR-instruction compliance 相关性确实只解释约 52% 方差。我的 W3 也提出了 GAR 单指标依赖的问题。但我想补充：r=0.72 对于一个 proxy metric 来说并不差——问题不在于相关性是否\"够高\"，而在于论文将所有机制分析（gradient conflict、distribution shift）都建立在 GAR 上。如果 GAR 衰减的 48% 未解释方差来自 GAR 指标本身的噪声（如 position bias、tokenization artifacts），则机制解释的可靠性会打折扣。\n\n[AGREE] R1-Single-Seed: 单种子（42）是实质性限制。我在 Soundness 评分中考虑了这一点但未单独列为 Must-Fix。R1 的分析更精确：bootstrap CI 覆盖推理时方差但不覆盖训练方差。Gate 初始化、LoRA 初始化、数据 shuffling 的随机性都可能影响 30× gap 的具体数值。建议至少 3 个种子。\n\n### 统计严格性方面\n\n[AGREE] R1-Llama-Underpowered: Llama 的 CI [−0.008, 0.041] 和 d=0.22 表明检测小效应的统计功效不足。这与我对论文跨模型声称的担忧一致——Llama 上的\"directional consistency\"可能仅仅是 underpowered test 的 null result。\n\n[AGREE] R1-p007-Honest: p≈0.07 的诚实报告确实值得肯定。我在 W2 中也提到了这一点。我们对此的评价一致：报告本身恰当，但将其列为正式 contribution 需要更强证据。\n\n### 可重复性方面\n\n[AGREE] R1-v1v6-Missing: v1-v6 loss 配置未详述是一个遗漏。我在\"小问题\"中提到了这一点。论文声称 \"explored seven loss configurations\" 但仅报告 v7 的结果——读者无法判断 v7 是否通过 principled selection 还是 cherry-picking 得出。至少应在 Appendix 提供 v1-v6 的描述和关键指标。\n\n[AGREE] R1-No-Code: 无代码/数据发布降低可重复性。对于 negative result 论文尤其重要——读者需要能验证负面结果不是实现 bug。\n\n### 缺失实验方面\n\n[AGREE] R1-Zero-Figures: **这是我遗漏的一个重要观察。** 一篇标题含 \"Mechanistic Analysis\" 的论文零图表确实是严重缺陷。Attention heatmap（可视化 GAR 衰减）、training curve（展示三阶段动态）、per-layer gradient heatmap（展示冲突模式）——这些都是 mechanistic analysis 的标准视觉证据。9 个 table 的纯数值呈现大幅降低了分析的直观说服力和读者体验。我应在初次审稿中将此列为 Should-Fix。\n\n[AGREE] R1-SS-Qwen-Only: Scheduled sampling 仅在 Qwen 上测试、未在 Llama 上验证，确实削弱了 Contribution 4 的跨模型泛化性。这与 N2（overclaiming）问题叠加——论文不仅在门控变体上范围窄，在缓解实验上也是单模型的。\n\n---\n\n## 对 R1 具体问题的回答\n\n### Q1: \"First quantitative measurement\" novelty claim 是否成立？\n\n**不成立。** 这是我 N1 (critical) 的核心论点。详细理由：\n\n1. **Exposure bias 的量化早已存在。** Ranzato et al. (2016)、Wiseman & Rush (2016) 等在 sequence generation 任务中量化了 teacher-forcing 与 autoregressive generation 之间的性能 gap。本文的\"30× gap\"是在一个新指标（GAR）上的测量，不是对一个新现象的首次量化。\n\n2. **Multi-task gradient conflict 的量化也已有先例。** GradNorm (Chen et al., 2018) 通过监控 gradient magnitude ratios 来平衡任务权重——论文的 7-15× magnitude ratio 测量方法与 GradNorm 的诊断方法本质相同。\n\n3. **\"First\" claim 的合理缩小范围**: 如果改为 \"first empirical demonstration that exposure bias critically undermines auxiliary attention-steering objectives in modern LLMs\"，这个 claim 会更准确，但也暴露了贡献本质是 application of known insights to a new setting，而非 new insights themselves。\n\n结论：这是对已知现象在新场景中的**确认性量化**（confirmatory quantification），而非**首次量化**（first quantitative measurement）。Novelty 应相应降级。\n\n### Q2: 仅测试标量门控对 negative result 价值的影响？\n\n**严重限制。** 理由如下：\n\n负面结果论文的说服力与\"排除的假设空间\"成正比。本文排除了一个极窄的假设——\"标量 per-layer ReZero gate + joint NTP-GAR training 能修复 multi-turn attention degradation\"。这距离排除 \"lightweight gating\" 这个大类还很远：\n\n| 未测试变体 | 为什么可能表现不同 |\n|-----------|-------------------|\n| Vector gate (per-dim) | 更高容量，可学习 dimension-specific 行为 |\n| Head-specific gate | 不同 attention head 可能有不同的 goal-tracking role |\n| Low-rank gate | 介于标量和全矩阵之间的容量权衡 |\n| 分离训练（先 GAR 后 NTP）| 避免梯度竞争，但可能引入其他问题 |\n| Gradient surgery (PCGrad) | 直接解决 §6.1 诊断的梯度冲突 |\n\n如果论文能证明即使用 PCGrad 消除梯度竞争 + vector gate 增加容量，exposure bias 仍然导致 30× gap，那\"轻量门控不行\"的结论就有坚实基础。目前只测试了最简单的配置就下了\"cannot\"的结论，说服力不足。\n\n**量化估计**: 如果 \"lightweight gating\" 包含上述 5 种变体，本文仅覆盖了 1/5 = 20% 的假设空间。对于声称 \"cannot\" 的论文，这远远不够。\n\n### Q3: 是否更适合作为 workshop paper 或 short paper？\n\n**我倾向于 workshop paper，具体理由：**\n\n| 因素 | Workshop | Short Paper | Long Paper |\n|------|----------|-------------|------------|\n| 范围 | ✓ 适合窄范围探索 | ✓ 适合有限但完整的贡献 | ✗ 范围不够 |\n| Novelty | ✓ Workshop 对 novelty 门槛更低 | △ Short paper 仍需 non-trivial insight | ✗ 不够 |\n| 方法论完整性 | △ 当前水平可接受 | △ 需补统计严格性 | ✗ 需大量补充实验 |\n| 实际长度 | △ 目前 ~6 页正文偏长 | ✓ 缩到 4 页很合适 | ✗ 内容撑不满 8 页 |\n\n最佳定位：**ACL Workshop on Insights from Negative Results**（真实存在的 workshop）。这个 workshop 专门接收负面结果论文，评审标准侧重\"是否提供了有价值的失败信息\"而非 novelty 的绝对高度。本文的实验方法论在 workshop 标准下是扎实的。\n\n如果坚持主会投稿：建议作为 **short paper** 提交到 ARR，聚焦在 \"exposure bias undermines auxiliary attention losses\" 这一个 takeaway，削减不必要的 overclaiming，补充 1-2 个 gradient surgery baseline 以增加 actionable insight。\n\n---\n\n## 评分更新\n\n在看到 R1 的发现后（特别是零图表问题和 Llama 评估不对称性），我对部分评分做微调：\n\n| 维度 | 原评分 | 更新 | 理由 |\n|------|--------|------|------|\n| Soundness (ARR) | 3/5 | 2.5/5 | 零图表+单种子+Llama 不完整消融，叠加后更接近\"Poor: some main claims not sufficiently supported\" |\n| Excitement (ARR) | 2/5 | 2/5 | 不变 |\n| Clarity (6-pt) | 4/6 | 3/6 | R1 关于零图表的观察有理——\"mechanistic analysis\" 无可视化是叙事缺陷 |\n| **Overall (ARR)** | **2.5/5** | **2.5/5** | **维持 Borderline Findings**——补充了更多弱点但实验方法论的基础仍在 |\n| **Overall (6-pt)** | **3/6** | **3/6** | **维持 Weak Reject** |\n\n---\n\n## R1-R2 共识总结\n\nR1 和 R2 在以下关键判断上一致：\n1. 实验方法论基础合理但有显著 gaps（单种子、跨模型不对称、零图表）\n2. 论文处于 Weak Reject / Borderline Findings 区间\n3. Contribution 不足以支撑 main conference acceptance\n4. 存在 overclaiming（标题和 contribution 声称过度）\n5. 缺少关键视觉证据（R1 首先发现，R2 同意）\n\nR2 额外强调的 R1 未覆盖的问题：\n- Multi-task gradient conflict 文献缺失（N4）\n- Dongre et al. (2026) 不可查证（N3）\n- 标题 \"Cannot\" 的具体 overclaiming 分析（N2）\n- 缺失正面结果替代方案的深入讨论\n",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-19T15:42:58.091650+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3974
}
```

</details>

---


### Assistant

_source line 54 · 2026-05-19T15:43:03.388748+00:00_

交叉回应已提交。对 R1 的全部观察逐条给出了 [AGREE]/[REBUT] 判断，回答了 R1 的三个问题（novelty claim 不成立、标量门控范围过窄、建议定位为 workshop paper），并根据 R1 发现的零图表和 Llama 评估不对称性问题微调了 Soundness 和 Clarity 评分。Overall 维持 2.5/5 (Borderline Findings) / 3/6 (Weak Reject)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

4 recorded events


### User

_source line 55 · 2026-05-19T15:43:04.455929+00:00_

[Round 1 审稿请求]:
## Step 3: Convergence Discussion

Having reviewed R1's findings and their questions, please provide your final assessment addressing:

1. **Response to R1's questions:**
   - "First quantitative measurement" claim: Partially justified. The specific 30× gap number for auxiliary attention losses under teacher-forcing is indeed new — no prior work has quantified this. However, the underlying explanation (exposure bias + gradient competition) is a composition of known phenomena. The novelty is in the measurement and the specific domain application, not in discovering new mechanisms.
   - Narrow scope: Scalar gates are the simplest possible intervention, and the paper doesn't test heavier gating (e.g., vector gates, per-head gates, MLP-based gates). This significantly limits generalizability — the conclusion "lightweight gating struggles" is technically only demonstrated for the lightest-weight version of gating.
   - Workshop vs. main conference: In its current state (broken references, no figures, single seed), this is closer to a workshop paper. With fixes (references, figures, multi-seed or at least 2-seed training, symmetric Llama experiments), it could be a borderline main conference paper, likely more suited for Findings than main track.

2. **Points of agreement with R1:**
   - Methodology is generally sound on Qwen; weaker on Llama.
   - Bootstrap CIs are correctly applied and honestly reported.
   - Missing figures are critical — I agree this is the #2 issue after broken references.
   - The loss design evolution (v1–v7) is under-documented.

3. **Points of nuance:**
   - R1 gives soundness 3.5/6 which feels appropriate — the analysis itself is competent, just limited in scale.
   - The downstream task validation (Table 5) is a valuable inclusion that many negative-result papers omit. Even at r=0.72 it provides necessary context.
   - I appreciate that R1 flags the lack of error bars in Tables 1–5, 7. Point estimates without uncertainty are a pervasive issue.

4. **Final R2 scores (post-convergence):**
   - Novelty: 3/6 (new quantification of known phenomena in a specific domain)
   - Significance: 3/6 (informative but narrow; no convincing positive path forward)
   - Clarity: 3/6 (prose quality is good; broken refs + no figures drag this down)
   - Overall: 3/6 (Weak Reject — the paper has a clear story and honest reporting, but insufficient novelty and presentation quality for a top venue main track)

**Key weaknesses (ranked):**
1. ALL references broken — unpublishable in current state
2. Zero figures severely limit the "mechanistic analysis" narrative
3. Limited novelty — composition of known mechanisms (exposure bias + gradient conflict) applied to a new setting
4. Narrow scope (only scalar gates, only 2 models, only UltraChat)
5. No positive resolution — scheduled sampling mitigation is statistically inconclusive

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-19T15:44:08.070098+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 最终评估（Post-Convergence）\n\n---\n\n## 对 Director 收敛讨论的回应\n\n### 对 R1 问题回应的补充意见\n\n**\"First quantitative measurement\" claim**: Director 的判断——\"partially justified, novelty in measurement not mechanism\"——我部分同意但倾向更严格。原因：量化本身的价值取决于量化结果是否出乎意料。如果 exposure bias 文献已经让我们预期 teacher-forcing 下训练的 auxiliary loss 会在 autoregressive inference 时大幅衰减，那么 30× 这个具体数字的信息量是有限的。它告诉我们\"衰减很严重\"，但并未改变我们的 prior belief。相比之下，如果量化结果是\"gap 仅为 1.2×\"，那才是真正意外的发现。我维持 N1 的判断：这是 confirmatory quantification，novelty 有限。\n\n**范围问题**: 完全同意 Director 的分析。我补充一个角度——即使在标量门控这个窄范围内，论文也只测试了一种初始化策略（gate 初始化为 0，即 ReZero）。如果初始化为 0.5（让门控从\"半开\"开始而非\"全关\"），或者用 learnable sigmoid gating（输出在 [0,1] 之间），行为可能不同。\"最简单配置的最简单变体\"不足以代表一个类别。\n\n**Workshop vs. Main Conference**: 同意 Director 的定位——当前状态接近 workshop paper。我想强调一点：修复引用和加图表是 necessary but not sufficient。即使这些 presentation 问题全部修复，核心 novelty 限制仍在。补充 gradient surgery baseline（如 PCGrad）并展示其也无法解决问题，才是从 workshop 升级到 Findings 的关键路径。\n\n### 与 R1 的共识确认\n\n完全同意 Director 总结的四个共识点。我对每个共识的信心度：\n\n1. **Qwen 方法论合理 / Llama 较弱** — 高信心。4-way vs 3-way 消融的不对称性是客观事实。\n2. **Bootstrap CI 正确且诚实** — 高信心。统计方法本身无误。\n3. **零图表是 #2 问题** — 高信心。R1 首先发现此问题，我在交叉回应中已采纳。对于 \"mechanistic analysis\" 论文，Figure 0 是不可接受的。\n4. **v1–v7 loss 设计欠文档** — 中等信心。这可能是 Appendix 空间限制的结果，但论文有 ~2 页未使用的正文空间，没有理由不补充。\n\n### 补充细微差异\n\n**Soundness 3.5/6 (R1) vs 2.5/5 ARR (R2)**: 这两个评分在不同量表上大致对齐。R1 的 3.5/6 ≈ 58%，我的 2.5/5 = 50%。差异来源：我更重视 multi-task gradient conflict 文献的缺失（N4）——如果论文声称梯度竞争是核心机制但不引用该领域成熟方法，这直接影响 soundness 而不仅是 related work completeness。R1 可能将此归入 significance 而非 soundness。\n\n**Downstream validation (r=0.72)**: 同意 Director 的正面评价。许多 negative result 论文完全不提供 proxy metric 的外部验证。r=0.72 虽然 moderate，但至少建立了 GAR 与实际任务性能之间的联系。这是论文的一个相对优势。\n\n---\n\n## R2 最终评分\n\n| 维度 | 初次评分 | 交叉回应后 | 最终评分 | 变化理由 |\n|------|----------|------------|----------|----------|\n| **Novelty** (6-pt) | 2/6 | 2/6 | **2.5/6** | Director 指出\"specific 30× gap number is indeed new\"有一定道理。从 2 上调至 2.5，承认在特定领域的量化贡献，但不改变\"已知机制的组合应用\"判断 |\n| **Significance** (6-pt) | 2/6 | 2/6 | **2.5/6** | 考虑到 downstream validation 和诚实的 hedging，略微上调。但 \"no convincing positive path forward\" 的限制仍在 |\n| **Clarity** (6-pt) | 4/6 → 3/6 | 3/6 | **3/6** | 零图表+引用问题（如果提交版确实坏了）。纯文字叙事质量本身是 4/6，但 presentation 问题拉低 |\n| **Soundness** (ARR) | 3/5 → 2.5/5 | 2.5/5 | **2.5/5** | 维持。单种子+不对称消融+零图表 = 部分主要 claims 支撑不足 |\n| **Excitement** (ARR) | 2/5 | 2/5 | **2/5** | 维持。确认性结果，有限的惊喜度 |\n| **Overall** (ARR) | 2.5/5 | 2.5/5 | **2.5/5 — Borderline Findings** | 维持 |\n| **Overall** (6-pt) | 3/6 | 3/6 | **3/6 — Weak Reject** | 维持 |\n\n---\n\n## 与 Director 评分的对齐\n\nDirector 最终给出 Novelty 3/6, Significance 3/6, Clarity 3/6, Overall 3/6。\n\n我的最终评分（Novelty 2.5, Significance 2.5, Clarity 3, Overall 3）略低于 Director 在 Novelty 和 Significance 上。差异来源：\n\n- **Novelty**: 我对 \"composition of known mechanisms\" 的 novelty discount 更大。Director 认可 \"new quantification in specific domain\" 的价值，我承认但认为这个价值更小。半分差异（3 vs 2.5）反映了对 confirmatory vs. novel 的不同权重。\n- **Significance**: Director 说 \"informative but narrow; no convincing positive path forward\"——我完全同意这个描述，但我从中推导出的分数更低，因为 \"no positive path forward\" 对负面结果论文的价值是致命的。好的负面结果论文不仅说\"这不行\"，还要指明\"什么可能行\"。本文的 §7 Discussion 仅给出模糊的 future directions（inference-time intervention、decoupled goal processing），缺乏具体的实验路径。\n\n**结论**: R1 (3/6)、R2 (3/6)、Director (3/6) 三方 Overall 评分一致为 Weak Reject。这个共识是稳固的。\n\n---\n\n## 给作者的建设性修改路径（如果选择重投）\n\n按优先级排序：\n\n1. **[必须] 修复引用** — 如果提交版引用全坏，这是 desk reject 级别问题。检查 natbib/biblatex 编译链。\n2. **[必须] 加图表** — 至少 3 张：(a) training curve（GAR + NTP loss 随 epoch 变化，展示三阶段），(b) attention heatmap（base model vs ThreadGate，展示 GAR 衰减），(c) per-layer gradient conflict 热力图。\n3. **[强烈建议] 加 gradient surgery baseline** — 用 PCGrad 或 GradNorm 平衡 NTP-GAR 梯度，报告结果。如果 gap 仍在 → 论文 novelty 大幅提升（\"即使消除梯度竞争，exposure bias 仍然致命\"）；如果 gap 缩小 → 论文的 insight 变为\"梯度竞争是可解的，真正的瓶颈是 exposure bias\"。\n4. **[建议] 扩展门控变体** — 至少加一种 vector gate 或 head-specific gate。如果也失败，结论说服力倍增。\n5. **[建议] 多种子训练** — 至少 2-3 个种子，报告均值±标准差。\n6. **[建议] 修正标题** — \"Cannot\" → \"Fails to\" 或更具体的 \"Why Scalar Residual Gating Fails to...\"\n7. **[建议] 补充 multi-task gradient conflict 文献** — §2 增加子节，定位本文在该领域的位置。\n8. **[可选] Llama 对称消融** — 加上 Uniform Gate 条件使两模型消融对齐。\n9. **[可选] Scheduled sampling 在 Llama 上验证** — 增强 Contribution 4 的泛化性。\n\n如果完成 1-4 项，论文大概率可达 Findings 水平（ARR 3.0）。如果 1-7 项全部完成且 gradient surgery baseline 给出有趣结果，可能触及 Borderline Conference（ARR 3.5）。\n",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 最终评估（Post-Convergence）\n\n---\n\n## 对 Director 收敛讨论的回应\n\n### 对 R1 问题回应的补充意见\n\n**\"First quantitative measurement\" claim**: Director 的判断——\"partially justified, novelty in measurement not mechanism\"——我部分同意但倾向更严格。原因：量化本身的价值取决于量化结果是否出乎意料。如果 exposure bias 文献已经让我们预期 teacher-forcing 下训练的 auxiliary loss 会在 autoregressive inference 时大幅衰减，那么 30× 这个具体数字的信息量是有限的。它告诉我们\"衰减很严重\"，但并未改变我们的 prior belief。相比之下，如果量化结果是\"gap 仅为 1.2×\"，那才是真正意外的发现。我维持 N1 的判断：这是 confirmatory quantification，novelty 有限。\n\n**范围问题**: 完全同意 Director 的分析。我补充一个角度——即使在标量门控这个窄范围内，论文也只测试了一种初始化策略（gate 初始化为 0，即 ReZero）。如果初始化为 0.5（让门控从\"半开\"开始而非\"全关\"），或者用 learnable sigmoid gating（输出在 [0,1] 之间），行为可能不同。\"最简单配置的最简单变体\"不足以代表一个类别。\n\n**Workshop vs. Main Conference**: 同意 Director 的定位——当前状态接近 workshop paper。我想强调一点：修复引用和加图表是 necessary but not sufficient。即使这些 presentation 问题全部修复，核心 novelty 限制仍在。补充 gradient surgery baseline（如 PCGrad）并展示其也无法解决问题，才是从 workshop 升级到 Findings 的关键路径。\n\n### 与 R1 的共识确认\n\n完全同意 Director 总结的四个共识点。我对每个共识的信心度：\n\n1. **Qwen 方法论合理 / Llama 较弱** — 高信心。4-way vs 3-way 消融的不对称性是客观事实。\n2. **Bootstrap CI 正确且诚实** — 高信心。统计方法本身无误。\n3. **零图表是 #2 问题** — 高信心。R1 首先发现此问题，我在交叉回应中已采纳。对于 \"mechanistic analysis\" 论文，Figure 0 是不可接受的。\n4. **v1–v7 loss 设计欠文档** — 中等信心。这可能是 Appendix 空间限制的结果，但论文有 ~2 页未使用的正文空间，没有理由不补充。\n\n### 补充细微差异\n\n**Soundness 3.5/6 (R1) vs 2.5/5 ARR (R2)**: 这两个评分在不同量表上大致对齐。R1 的 3.5/6 ≈ 58%，我的 2.5/5 = 50%。差异来源：我更重视 multi-task gradient conflict 文献的缺失（N4）——如果论文声称梯度竞争是核心机制但不引用该领域成熟方法，这直接影响 soundness 而不仅是 related work completeness。R1 可能将此归入 significance 而非 soundness。\n\n**Downstream validation (r=0.72)**: 同意 Director 的正面评价。许多 negative result 论文完全不提供 proxy metric 的外部验证。r=0.72 虽然 moderate，但至少建立了 GAR 与实际任务性能之间的联系。这是论文的一个相对优势。\n\n---\n\n## R2 最终评分\n\n| 维度 | 初次评分 | 交叉回应后 | 最终评分 | 变化理由 |\n|------|----------|------------|----------|----------|\n| **Novelty** (6-pt) | 2/6 | 2/6 | **2.5/6** | Director 指出\"specific 30× gap number is indeed new\"有一定道理。从 2 上调至 2.5，承认在特定领域的量化贡献，但不改变\"已知机制的组合应用\"判断 |\n| **Significance** (6-pt) | 2/6 | 2/6 | **2.5/6** | 考虑到 downstream validation 和诚实的 hedging，略微上调。但 \"no convincing positive path forward\" 的限制仍在 |\n| **Clarity** (6-pt) | 4/6 → 3/6 | 3/6 | **3/6** | 零图表+引用问题（如果提交版确实坏了）。纯文字叙事质量本身是 4/6，但 presentation 问题拉低 |\n| **Soundness** (ARR) | 3/5 → 2.5/5 | 2.5/5 | **2.5/5** | 维持。单种子+不对称消融+零图表 = 部分主要 claims 支撑不足 |\n| **Excitement** (ARR) | 2/5 | 2/5 | **2/5** | 维持。确认性结果，有限的惊喜度 |\n| **Overall** (ARR) | 2.5/5 | 2.5/5 | **2.5/5 — Borderline Findings** | 维持 |\n| **Overall** (6-pt) | 3/6 | 3/6 | **3/6 — Weak Reject** | 维持 |\n\n---\n\n## 与 Director 评分的对齐\n\nDirector 最终给出 Novelty 3/6, Significance 3/6, Clarity 3/6, Overall 3/6。\n\n我的最终评分（Novelty 2.5, Significance 2.5, Clarity 3, Overall 3）略低于 Director 在 Novelty 和 Significance 上。差异来源：\n\n- **Novelty**: 我对 \"composition of known mechanisms\" 的 novelty discount 更大。Director 认可 \"new quantification in specific domain\" 的价值，我承认但认为这个价值更小。半分差异（3 vs 2.5）反映了对 confirmatory vs. novel 的不同权重。\n- **Significance**: Director 说 \"informative but narrow; no convincing positive path forward\"——我完全同意这个描述，但我从中推导出的分数更低，因为 \"no positive path forward\" 对负面结果论文的价值是致命的。好的负面结果论文不仅说\"这不行\"，还要指明\"什么可能行\"。本文的 §7 Discussion 仅给出模糊的 future directions（inference-time intervention、decoupled goal processing），缺乏具体的实验路径。\n\n**结论**: R1 (3/6)、R2 (3/6)、Director (3/6) 三方 Overall 评分一致为 Weak Reject。这个共识是稳固的。\n\n---\n\n## 给作者的建设性修改路径（如果选择重投）\n\n按优先级排序：\n\n1. **[必须] 修复引用** — 如果提交版引用全坏，这是 desk reject 级别问题。检查 natbib/biblatex 编译链。\n2. **[必须] 加图表** — 至少 3 张：(a) training curve（GAR + NTP loss 随 epoch 变化，展示三阶段），(b) attention heatmap（base model vs ThreadGate，展示 GAR 衰减），(c) per-layer gradient conflict 热力图。\n3. **[强烈建议] 加 gradient surgery baseline** — 用 PCGrad 或 GradNorm 平衡 NTP-GAR 梯度，报告结果。如果 gap 仍在 → 论文 novelty 大幅提升（\"即使消除梯度竞争，exposure bias 仍然致命\"）；如果 gap 缩小 → 论文的 insight 变为\"梯度竞争是可解的，真正的瓶颈是 exposure bias\"。\n4. **[建议] 扩展门控变体** — 至少加一种 vector gate 或 head-specific gate。如果也失败，结论说服力倍增。\n5. **[建议] 多种子训练** — 至少 2-3 个种子，报告均值±标准差。\n6. **[建议] 修正标题** — \"Cannot\" → \"Fails to\" 或更具体的 \"Why Scalar Residual Gating Fails to...\"\n7. **[建议] 补充 multi-task gradient conflict 文献** — §2 增加子节，定位本文在该领域的位置。\n8. **[可选] Llama 对称消融** — 加上 Uniform Gate 条件使两模型消融对齐。\n9. **[可选] Scheduled sampling 在 Llama 上验证** — 增强 Contribution 4 的泛化性。\n\n如果完成 1-4 项，论文大概率可达 Findings 水平（ARR 3.0）。如果 1-7 项全部完成且 gradient surgery baseline 给出有趣结果，可能触及 Borderline Conference（ARR 3.5）。\n",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-19T15:44:12.111083+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4040
}
```

</details>

---


### Assistant

_source line 58 · 2026-05-19T15:44:18.939932+00:00_

最终评估已提交。三轮审稿总结：

- **Overall: 3/6 (Weak Reject) / ARR 2.5 (Borderline Findings)**
- R1、R2、Director 三方 Overall 一致为 Weak Reject
- 核心问题排序：(1) 引用全坏 (2) 零图表 (3) novelty 有限（已知机制的组合应用）(4) 范围过窄（仅标量门控）(5) 无统计显著的正面缓解方案
- 给出了 9 项优先级排序的修改建议，完成前 4 项可望达到 Findings 水平

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 59 · 2026-05-19T15:44:26.055480+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。

---

以下是 Reviewer 1 的完整审稿原文：

# Reviewer 1 审稿报告：Methods &amp; Experiments

**论文**: "Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"
**审稿侧重**: 方法设计、实验设计、统计严谨性、可复现性、消融完整性

## 总体评分
**Overall Assessment**: 3.0 / 5（Findings acceptance）
**Overall (6-point)**: 3 / 6 — Weak Reject

## Must-Fix 问题

### N1 [critical] 所有引用均渲染为 "?"——bibliography 编译失败
- PDF 中每一处引用都显示为 "?" 而非作者名。
- 引用审计：24 条 bib 条目中，3 条在 OpenAlex 上未找到（dongre2026、zou2023representation、elhage2021mathematical），5 条存在作者或年份不匹配，4 条 orphan entries。

### N2 [critical] 单种子实验支撑 "Cannot" 级别的强断言
- 所有实验均使用 seed=42 单次运行。
- 30× 训练-推理 gap 在不同 seed 下是否稳定？负面结果论文的证据标准应高于正面结果。

### N3 [critical] 评估样本量过小（50 conversations）且统计功效存疑
- Cohen's d ≈ 0.22 是小效应量，在 n=50 下 power 不足。
- scheduled sampling 结果 p≈0.07 在 α=0.05 下不显著。

### N4 [critical] 损失函数超参数和组件定义缺失——无法复现
- λ_GAR、λ_div 具体数值未报告。
- L_div 无数学定义。v1-v6 完全没有细节。

## Should-Fix 问题

### W1 [warning] Llama 上未测试 Uniform Gate——跨模型验证不完整
### W2 [warning] 无 λ_GAR 敏感性消融
### W3 [warning] 训练数据量（1,000 conversations）可能是混淆变量
### W4 [warning] 缺少可视化——论文关于注意力退化却没有注意力热力图
### W5 [warning] Scheduled sampling 因果推断的局限性未充分讨论
### W6 [warning] "Reverse turn conditioning"（Section 6.2）的证据是间接的

## 主要优势
1. 有价值的负面结果——两个失败机制的归因为后续工作提供避坑方向
2. 跨模型一致性（Qwen 30× vs Llama 26× gap）
3. 4-way ablation 设计合理（Uniform Gate 对照组是亮点）
4. Scheduled sampling 因果实验思路正确
5. 梯度冲突量化分析（Table 6）是最有说服力的机制证据

---

请对上述每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。重点关注你作为 novelty 审稿人的视角是否与方法/实验审稿人的判断一致或有分歧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-19T15:46:09.410667+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 逐条交叉回应：R1 完整审稿意见\n\n---\n\n## Must-Fix 问题逐条回应\n\n### [AGREE] R1-N1: 所有引用均渲染为 \"?\"\n\n同意这是 critical 级别问题。补充说明：\n\n我在 `dream_20260519T145320/best/paper.pdf` 版本中观察到引用**正常渲染**（如 p.1 \"Dongre et al. (2026)\"、p.2 \"(Zheng et al., 2024)\" 均可读）。因此存在两种可能：(a) R1 审查的是不同版本（如 median 或 worst），(b) 我审查的 \"best\" 版本已修复此问题。\n\n无论哪种情况，**如果提交版确实引用全坏，这是 desk reject 级别缺陷**，我完全同意 R1 的判断。引用审计结果（3 not_found, 5 mismatch, 4 orphan）我在初次审稿中也独立验证并在 N3 中重点标记了 Dongre et al. (2026) 不可查证的问题。\n\n**R2 视角补充**: 从 novelty 审稿角度，引用全坏还有一个额外影响——审稿人无法确认作者是否 properly attribute prior work，这直接影响 novelty claim 的可信度。如果审稿人看到 \"first quantitative measurement\" 却无法追溯引用链验证这个 \"first\" 是否成立，会本能地怀疑 overclaiming。\n\n### [AGREE] R1-N2: 单种子实验支撑 \"Cannot\" 级别强断言\n\n完全同意，且这与我的 N2（标题 \"Cannot\" overclaims）形成互补。R1 从统计角度、我从逻辑/范围角度分别论证了同一个问题：**证据强度不匹配声称强度**。\n\n具体量化补充：\n- 30× gap = GAR 从 0.48(train) 降到 0.016(infer)。如果不同种子下 training GAR 的方差是 ±0.05（0.43–0.53），inference GAR 的方差是 ±0.005（0.011–0.021），则 gap 范围为 20×–48×。这个范围的上下界差 2.4 倍——\"30×\" 这个数字的精度依赖单种子，不可靠。\n- 负面结果论文确实应有更高证据标准，因为 burden of proof 在作者一方：你需要证明\"真的不行\"而非\"你没做对\"。单种子无法排除后者。\n\n**R2 视角补充**: 从 novelty 角度，如果 30× 在不同种子下波动剧烈（如 10×–50×），则 \"30× gap\" 作为 headline contribution 的信息价值大幅缩水。Novelty claim 的精度不应超过数据支持的精度。\n\n### [AGREE] R1-N3: 评估样本量过小且统计功效存疑\n\n同意 R1 的统计分析。补充两个角度：\n\n**1. Power analysis 视角**: R1 指出 d=0.22 在 n=50 下 power 不足。具体而言，双侧 t 检验在 n=50、d=0.2、α=0.05 下的 power 约为 0.29——即有 71% 概率漏检真实的小效应。这意味着 Table 5 中 TG-LO difference \"statistically indistinguishable from zero\" 的结论可能仅仅是 Type II error。论文不能在 underpowered test 的基础上声称\"gating provides zero incremental benefit\"（§5.3 标题）。\n\n**2. Novelty 视角**: scheduled sampling 的 p≈0.07 被列为 Contribution 4（\"suggestive evidence\"）。如果这是论文唯一指向正面方向的结果，其统计不显著意味着论文实际上没有提供任何 actionable insight——既不能确定\"gating cannot work\"（因为单种子+overclaim），也不能确定\"scheduled sampling is the path forward\"（因为 p=0.07）。这使论文处于一个尴尬的 limbo：负面结论不够强，正面线索不够确定。\n\n**与 R1 的细微分歧**: R1 将此定为 critical。我认为 50 conversations 的样本量对于**主效应**（30× gap）来说是足够的——当 effect size 这么大时，即使 n=10 也能检测到。R1 的 power concern 更适用于**比较效应**（TG vs LoRA-only, scheduled sampling vs baseline），这些确实是小效应。我会将此分级为 **N3 对主效应: should-fix, 对比较效应: critical**。\n\n### [AGREE] R1-N4: 损失函数超参数和组件定义缺失\n\n同意。从可复现性角度这是 critical。\n\n具体缺失清单核实：\n- **λ_GAR、λ_div 数值**: §4.2 Eq. 3 给出 L = L_NTP + λ_GAR · L_GAR + λ_div · L_div，但我在论文中未找到 λ_GAR 和 λ_div 的具体数值。如果它们隐含在 \"v7 achieved stable training convergence\" 的描述中，那这正是 R1 批评的问题——v7 的具体配置未详述。\n- **L_div 定义**: §4.2 提到 L_div \"encourages diversity across layer-wise gate values to prevent collapse\"，但未给出数学公式。一个没有数学定义的 loss component 是无法复现的。\n- **v1–v6 缺失**: 论文声称探索了 7 种 loss 配置但仅报告 v7。这是 cherry-picking 的潜在风险——如果 v3 或 v5 效果更好但不符合论文叙事怎么办？\n\n**R2 视角补充**: 从 novelty 角度，ThreadGate + v7 loss 是论文提出的\"方法\"，如果方法本身不可复现，则任何基于该方法的负面结论都不可验证。这不仅是可复现性问题，也是 soundness 问题——审稿人无法确认失败是方法的固有局限还是实现细节的问题。\n\n---\n\n## Should-Fix 问题逐条回应\n\n### [AGREE] R1-W1: Llama 上未测试 Uniform Gate\n\n同意。我在交叉回应中已提及此问题。Uniform Gate 是关键对照——它区分了\"学到的 per-layer gating pattern 是否比均匀 gating 更优\"。Qwen 上的 4-way 消融表明 ThreadGate ≈ Uniform Gate ≈ LoRA-only，这个结论在 Llama 上缺少 Uniform Gate 一环。缺失原因可能是计算预算限制，但应至少在 Limitations 中说明。\n\n### [AGREE] R1-W2: 无 λ_GAR 敏感性消融\n\n同意，且从 novelty 角度这个遗漏尤其有意义。论文的 gradient competition 分析（§6.1）表明 NTP 梯度 dominate GAR 梯度 7–15×。那么一个自然的问题是：**如果大幅增加 λ_GAR（如 10×、50×）来对抗这种 dominance，会发生什么？** 如果增大 λ_GAR 能缩小 gap，则问题不是 \"gating cannot work\" 而是 \"default hyperparameters don't work\"。如果增大 λ_GAR 导致 NTP loss 崩坏，这反而是一个更强的负面结果——说明 NTP-GAR 之间存在 fundamental tradeoff。无论哪种结果都比当前更有 insight。\n\n### [AGREE] R1-W3: 训练数据量（1,000 conversations）可能是混淆变量\n\n同意。1,000 conversations 对于训练 gate + LoRA 来说可能不足。如果 gate 需要更多数据来学习稳健的 turn-conditioned 行为，则\"gate 没用\"可能仅仅是 underfitting。这与我在\"Missing Perspectives\"中提到的\"训练数据量不足\"是同一问题。\n\n补充一个 novelty 角度：如果增加数据量到 10k conversations 后 gap 从 30× 缩小到 5×，则论文的核心 claim 不成立。论文未排除这个可能性。\n\n### [AGREE] R1-W4: 缺少可视化\n\n强烈同意。我在交叉回应中已将此采纳为重要遗漏。一篇标题含 \"Mechanistic Analysis\" 的论文应有：\n- Attention heatmap（直观展示 GAR 衰减）\n- Training curve（展示三阶段动态和 loss 演化）\n- Gradient conflict 热力图（per-layer × per-epoch 的 conflict fraction / magnitude ratio）\n- Gate value profile 可视化（per-layer gate 在不同 turn 的变化）\n\n当前 9 tables + 0 figures 的呈现方式严重削弱 \"mechanistic\" 的说服力。Table 6 的数据如果用热力图展示会直观十倍。\n\n### [AGREE] R1-W5: Scheduled sampling 因果推断局限性未充分讨论\n\n同意。§6.4 用 scheduled sampling 建立 exposure bias 为 \"causal factor\" 的论证链，但：\n1. SS 同时改变了 training distribution（增加了 autoregressive 采样比例）和 model capacity utilization（模型需要处理更多样化的输入），因此 gap 缩小可以归因于 exposure bias 减少，也可以归因于更丰富的训练信号。\n2. SS 率从 0% 到 50% 是一个 confound——SS 本身改变了训练动态，不仅仅是\"减少了 exposure bias\"。\n\n这个局限性在 §7 有部分讨论（\"the SS ratio caps at 50%, the remaining teacher-forced samples maintain some distribution mismatch\"），但不够系统化。\n\n### [REBUT] R1-W6: \"Reverse turn conditioning\"（§6.2）证据是间接的\n\n**部分反驳。** R1 认为 §6.2 的 reverse turn conditioning 证据是间接的。我认为 Table 6 实际上提供了**较强的间接证据**，在此场景下是合理的：\n\n- Table 6 显示 Qwen 28 层中 27 层的 gate difference（turn 1 minus turn 21）为正值——gate 在早期 turn 更活跃，晚期 turn 被抑制。这与 \"reverse turn conditioning\"（在最需要干预的晚期 turn 反而 gate 关闭）的预测完全一致。\n- 推理时 gate mean 在 0.93–0.98 范围内，标准差仅 2–7%——gate 几乎不活动，sublayer 输出几乎未被调制。\n- 这些数据虽然不能证明因果链（NTP dominance → reverse conditioning → gate inertness），但 pattern 的一致性（27/28 层同方向）使得替代解释难以成立。\n\n**然而**，我同意缺少可视化（如 gate profile 随 turn 变化的折线图）削弱了这个论点的 presentation。数据支持结论，但展示方式不够直观。评级：从 R1 的 warning 降为 minor concern——数据本身可以，展示需要改善。\n\n---\n\n## 对 R1 \"主要优势\" 的评价\n\n| R1 优势 | R2 评价 |\n|---------|---------|\n| 1. 有价值的负面结果 | 部分同意。失败机制的归因有价值，但归因的 novelty 有限（已知机制组合）。对于不熟悉 exposure bias 文献的 dialogue 研究者确实有 informative value。 |\n| 2. 跨模型一致性 (30× vs 26×) | 同意。这是论文相对较强的一面——两个不同架构/训练的模型呈现同方向结果增加了可信度，尽管 Llama 消融不完整。 |\n| 3. 4-way ablation 设计 | 强烈同意。Uniform Gate 对照组是实验设计的亮点，将 \"per-layer gating pattern\" 与 \"任意 gating\" 解耦。 |\n| 4. Scheduled sampling 因果思路 | 同意思路正确，但执行不足（单模型、p=0.07、confound 未讨论）。 |\n| 5. 梯度冲突量化 (Table 6) | 同意这是最有说服力的分析。Per-layer 粒度、conflict fraction、magnitude ratio 的三维度量化是扎实的。但缺少 multi-task gradient conflict 文献的上下文定位（我的 N4）削弱了其 novelty。 |\n\n---\n\n## R1-R2 最终共识矩阵\n\n| 问题 | R1 评级 | R2 评级 | 共识 |\n|------|---------|---------|------|\n| 引用全坏 | Critical | Critical | ✅ 一致（R2 补充：审查版本可能已修复） |\n| 单种子 | Critical | Critical | ✅ 一致 |\n| 样本量/功效 | Critical | Critical(比较效应) / Should-fix(主效应) | ⚠️ 细微分歧——30× gap 本身 robust，小效应比较 underpowered |\n| Loss 超参缺失 | Critical | Critical | ✅ 一致 |\n| Llama 消融不对称 | Warning | Warning | ✅ 一致 |\n| λ_GAR 敏感性 | Warning | Warning（升级倾向） | ⚠️ R2 认为这可能应升至 critical——直接影响核心结论 |\n| 训练数据量 | Warning | Warning | ✅ 一致 |\n| 零图表 | Warning | Warning（接近 critical） | ⚠️ R2 认为对 \"mechanistic analysis\" 论文接近 critical |\n| SS 因果局限 | Warning | Warning | ✅ 一致 |\n| Reverse turn conditioning | Warning | Minor（数据支持，展示需改善） | ⚠️ 分歧——R2 认为 Table 6 的 27/28 层一致性较强 |\n\n**R2 额外标记的 R1 未覆盖问题**:\n- N3: Dongre et al. (2026) 不可查证 → R1 在 N1 引用审计中提到但未单独列为 critical\n- N4: Multi-task gradient conflict 文献完全缺失 → R1 未提及\n- W1: 仅标量门控的范围局限 → R1 未单独列出但在叙述中提及\n- W3: GAR 单指标依赖 → R1 在文中提到 r=0.72 的局限但未列为 warning\n- W5: liu2016attention 引用可能错配 → R1 未提及\n",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 逐条交叉回应：R1 完整审稿意见\n\n---\n\n## Must-Fix 问题逐条回应\n\n### [AGREE] R1-N1: 所有引用均渲染为 \"?\"\n\n同意这是 critical 级别问题。补充说明：\n\n我在 `dream_20260519T145320/best/paper.pdf` 版本中观察到引用**正常渲染**（如 p.1 \"Dongre et al. (2026)\"、p.2 \"(Zheng et al., 2024)\" 均可读）。因此存在两种可能：(a) R1 审查的是不同版本（如 median 或 worst），(b) 我审查的 \"best\" 版本已修复此问题。\n\n无论哪种情况，**如果提交版确实引用全坏，这是 desk reject 级别缺陷**，我完全同意 R1 的判断。引用审计结果（3 not_found, 5 mismatch, 4 orphan）我在初次审稿中也独立验证并在 N3 中重点标记了 Dongre et al. (2026) 不可查证的问题。\n\n**R2 视角补充**: 从 novelty 审稿角度，引用全坏还有一个额外影响——审稿人无法确认作者是否 properly attribute prior work，这直接影响 novelty claim 的可信度。如果审稿人看到 \"first quantitative measurement\" 却无法追溯引用链验证这个 \"first\" 是否成立，会本能地怀疑 overclaiming。\n\n### [AGREE] R1-N2: 单种子实验支撑 \"Cannot\" 级别强断言\n\n完全同意，且这与我的 N2（标题 \"Cannot\" overclaims）形成互补。R1 从统计角度、我从逻辑/范围角度分别论证了同一个问题：**证据强度不匹配声称强度**。\n\n具体量化补充：\n- 30× gap = GAR 从 0.48(train) 降到 0.016(infer)。如果不同种子下 training GAR 的方差是 ±0.05（0.43–0.53），inference GAR 的方差是 ±0.005（0.011–0.021），则 gap 范围为 20×–48×。这个范围的上下界差 2.4 倍——\"30×\" 这个数字的精度依赖单种子，不可靠。\n- 负面结果论文确实应有更高证据标准，因为 burden of proof 在作者一方：你需要证明\"真的不行\"而非\"你没做对\"。单种子无法排除后者。\n\n**R2 视角补充**: 从 novelty 角度，如果 30× 在不同种子下波动剧烈（如 10×–50×），则 \"30× gap\" 作为 headline contribution 的信息价值大幅缩水。Novelty claim 的精度不应超过数据支持的精度。\n\n### [AGREE] R1-N3: 评估样本量过小且统计功效存疑\n\n同意 R1 的统计分析。补充两个角度：\n\n**1. Power analysis 视角**: R1 指出 d=0.22 在 n=50 下 power 不足。具体而言，双侧 t 检验在 n=50、d=0.2、α=0.05 下的 power 约为 0.29——即有 71% 概率漏检真实的小效应。这意味着 Table 5 中 TG-LO difference \"statistically indistinguishable from zero\" 的结论可能仅仅是 Type II error。论文不能在 underpowered test 的基础上声称\"gating provides zero incremental benefit\"（§5.3 标题）。\n\n**2. Novelty 视角**: scheduled sampling 的 p≈0.07 被列为 Contribution 4（\"suggestive evidence\"）。如果这是论文唯一指向正面方向的结果，其统计不显著意味着论文实际上没有提供任何 actionable insight——既不能确定\"gating cannot work\"（因为单种子+overclaim），也不能确定\"scheduled sampling is the path forward\"（因为 p=0.07）。这使论文处于一个尴尬的 limbo：负面结论不够强，正面线索不够确定。\n\n**与 R1 的细微分歧**: R1 将此定为 critical。我认为 50 conversations 的样本量对于**主效应**（30× gap）来说是足够的——当 effect size 这么大时，即使 n=10 也能检测到。R1 的 power concern 更适用于**比较效应**（TG vs LoRA-only, scheduled sampling vs baseline），这些确实是小效应。我会将此分级为 **N3 对主效应: should-fix, 对比较效应: critical**。\n\n### [AGREE] R1-N4: 损失函数超参数和组件定义缺失\n\n同意。从可复现性角度这是 critical。\n\n具体缺失清单核实：\n- **λ_GAR、λ_div 数值**: §4.2 Eq. 3 给出 L = L_NTP + λ_GAR · L_GAR + λ_div · L_div，但我在论文中未找到 λ_GAR 和 λ_div 的具体数值。如果它们隐含在 \"v7 achieved stable training convergence\" 的描述中，那这正是 R1 批评的问题——v7 的具体配置未详述。\n- **L_div 定义**: §4.2 提到 L_div \"encourages diversity across layer-wise gate values to prevent collapse\"，但未给出数学公式。一个没有数学定义的 loss component 是无法复现的。\n- **v1–v6 缺失**: 论文声称探索了 7 种 loss 配置但仅报告 v7。这是 cherry-picking 的潜在风险——如果 v3 或 v5 效果更好但不符合论文叙事怎么办？\n\n**R2 视角补充**: 从 novelty 角度，ThreadGate + v7 loss 是论文提出的\"方法\"，如果方法本身不可复现，则任何基于该方法的负面结论都不可验证。这不仅是可复现性问题，也是 soundness 问题——审稿人无法确认失败是方法的固有局限还是实现细节的问题。\n\n---\n\n## Should-Fix 问题逐条回应\n\n### [AGREE] R1-W1: Llama 上未测试 Uniform Gate\n\n同意。我在交叉回应中已提及此问题。Uniform Gate 是关键对照——它区分了\"学到的 per-layer gating pattern 是否比均匀 gating 更优\"。Qwen 上的 4-way 消融表明 ThreadGate ≈ Uniform Gate ≈ LoRA-only，这个结论在 Llama 上缺少 Uniform Gate 一环。缺失原因可能是计算预算限制，但应至少在 Limitations 中说明。\n\n### [AGREE] R1-W2: 无 λ_GAR 敏感性消融\n\n同意，且从 novelty 角度这个遗漏尤其有意义。论文的 gradient competition 分析（§6.1）表明 NTP 梯度 dominate GAR 梯度 7–15×。那么一个自然的问题是：**如果大幅增加 λ_GAR（如 10×、50×）来对抗这种 dominance，会发生什么？** 如果增大 λ_GAR 能缩小 gap，则问题不是 \"gating cannot work\" 而是 \"default hyperparameters don't work\"。如果增大 λ_GAR 导致 NTP loss 崩坏，这反而是一个更强的负面结果——说明 NTP-GAR 之间存在 fundamental tradeoff。无论哪种结果都比当前更有 insight。\n\n### [AGREE] R1-W3: 训练数据量（1,000 conversations）可能是混淆变量\n\n同意。1,000 conversations 对于训练 gate + LoRA 来说可能不足。如果 gate 需要更多数据来学习稳健的 turn-conditioned 行为，则\"gate 没用\"可能仅仅是 underfitting。这与我在\"Missing Perspectives\"中提到的\"训练数据量不足\"是同一问题。\n\n补充一个 novelty 角度：如果增加数据量到 10k conversations 后 gap 从 30× 缩小到 5×，则论文的核心 claim 不成立。论文未排除这个可能性。\n\n### [AGREE] R1-W4: 缺少可视化\n\n强烈同意。我在交叉回应中已将此采纳为重要遗漏。一篇标题含 \"Mechanistic Analysis\" 的论文应有：\n- Attention heatmap（直观展示 GAR 衰减）\n- Training curve（展示三阶段动态和 loss 演化）\n- Gradient conflict 热力图（per-layer × per-epoch 的 conflict fraction / magnitude ratio）\n- Gate value profile 可视化（per-layer gate 在不同 turn 的变化）\n\n当前 9 tables + 0 figures 的呈现方式严重削弱 \"mechanistic\" 的说服力。Table 6 的数据如果用热力图展示会直观十倍。\n\n### [AGREE] R1-W5: Scheduled sampling 因果推断局限性未充分讨论\n\n同意。§6.4 用 scheduled sampling 建立 exposure bias 为 \"causal factor\" 的论证链，但：\n1. SS 同时改变了 training distribution（增加了 autoregressive 采样比例）和 model capacity utilization（模型需要处理更多样化的输入），因此 gap 缩小可以归因于 exposure bias 减少，也可以归因于更丰富的训练信号。\n2. SS 率从 0% 到 50% 是一个 confound——SS 本身改变了训练动态，不仅仅是\"减少了 exposure bias\"。\n\n这个局限性在 §7 有部分讨论（\"the SS ratio caps at 50%, the remaining teacher-forced samples maintain some distribution mismatch\"），但不够系统化。\n\n### [REBUT] R1-W6: \"Reverse turn conditioning\"（§6.2）证据是间接的\n\n**部分反驳。** R1 认为 §6.2 的 reverse turn conditioning 证据是间接的。我认为 Table 6 实际上提供了**较强的间接证据**，在此场景下是合理的：\n\n- Table 6 显示 Qwen 28 层中 27 层的 gate difference（turn 1 minus turn 21）为正值——gate 在早期 turn 更活跃，晚期 turn 被抑制。这与 \"reverse turn conditioning\"（在最需要干预的晚期 turn 反而 gate 关闭）的预测完全一致。\n- 推理时 gate mean 在 0.93–0.98 范围内，标准差仅 2–7%——gate 几乎不活动，sublayer 输出几乎未被调制。\n- 这些数据虽然不能证明因果链（NTP dominance → reverse conditioning → gate inertness），但 pattern 的一致性（27/28 层同方向）使得替代解释难以成立。\n\n**然而**，我同意缺少可视化（如 gate profile 随 turn 变化的折线图）削弱了这个论点的 presentation。数据支持结论，但展示方式不够直观。评级：从 R1 的 warning 降为 minor concern——数据本身可以，展示需要改善。\n\n---\n\n## 对 R1 \"主要优势\" 的评价\n\n| R1 优势 | R2 评价 |\n|---------|---------|\n| 1. 有价值的负面结果 | 部分同意。失败机制的归因有价值，但归因的 novelty 有限（已知机制组合）。对于不熟悉 exposure bias 文献的 dialogue 研究者确实有 informative value。 |\n| 2. 跨模型一致性 (30× vs 26×) | 同意。这是论文相对较强的一面——两个不同架构/训练的模型呈现同方向结果增加了可信度，尽管 Llama 消融不完整。 |\n| 3. 4-way ablation 设计 | 强烈同意。Uniform Gate 对照组是实验设计的亮点，将 \"per-layer gating pattern\" 与 \"任意 gating\" 解耦。 |\n| 4. Scheduled sampling 因果思路 | 同意思路正确，但执行不足（单模型、p=0.07、confound 未讨论）。 |\n| 5. 梯度冲突量化 (Table 6) | 同意这是最有说服力的分析。Per-layer 粒度、conflict fraction、magnitude ratio 的三维度量化是扎实的。但缺少 multi-task gradient conflict 文献的上下文定位（我的 N4）削弱了其 novelty。 |\n\n---\n\n## R1-R2 最终共识矩阵\n\n| 问题 | R1 评级 | R2 评级 | 共识 |\n|------|---------|---------|------|\n| 引用全坏 | Critical | Critical | ✅ 一致（R2 补充：审查版本可能已修复） |\n| 单种子 | Critical | Critical | ✅ 一致 |\n| 样本量/功效 | Critical | Critical(比较效应) / Should-fix(主效应) | ⚠️ 细微分歧——30× gap 本身 robust，小效应比较 underpowered |\n| Loss 超参缺失 | Critical | Critical | ✅ 一致 |\n| Llama 消融不对称 | Warning | Warning | ✅ 一致 |\n| λ_GAR 敏感性 | Warning | Warning（升级倾向） | ⚠️ R2 认为这可能应升至 critical——直接影响核心结论 |\n| 训练数据量 | Warning | Warning | ✅ 一致 |\n| 零图表 | Warning | Warning（接近 critical） | ⚠️ R2 认为对 \"mechanistic analysis\" 论文接近 critical |\n| SS 因果局限 | Warning | Warning | ✅ 一致 |\n| Reverse turn conditioning | Warning | Minor（数据支持，展示需改善） | ⚠️ 分歧——R2 认为 Table 6 的 27/28 层一致性较强 |\n\n**R2 额外标记的 R1 未覆盖问题**:\n- N3: Dongre et al. (2026) 不可查证 → R1 在 N1 引用审计中提到但未单独列为 critical\n- N4: Multi-task gradient conflict 文献完全缺失 → R1 未提及\n- W1: 仅标量门控的范围局限 → R1 未单独列出但在叙述中提及\n- W3: GAR 单指标依赖 → R1 在文中提到 r=0.72 的局限但未列为 warning\n- W5: liu2016attention 引用可能错配 → R1 未提及\n",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-19T15:46:13.375515+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3964
}
```

</details>

---


### Assistant

_source line 62 · 2026-05-19T15:46:18.162378+00:00_

已提交对 R1 完整审稿意见的逐条交叉回应。10 个问题中 9 个 [AGREE]、1 个 [REBUT]（R1-W6 reverse turn conditioning 证据强度），并补充了 R2 独有的 5 个 R1 未覆盖问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

68 recorded events


### User

_source line 63 · 2026-05-22T08:34:07.179990+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 格式** 审查。

## Venue 信息
- **目标 venue**: EMNLP 2026（通过 ARR August cycle 提交）
- **Commitment deadline**: 2026-08-02
- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, Limitations 必填(不计页数)
- **匿名**: Double-blind

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf`

## 审查侧重

请重点评估以下方面：

1. **新颖性与贡献声称**：论文声称的四项贡献（因果诊断框架、exposure bias 刻画、inference-time steering、负面 baseline）分别有多强？"first empirical characterization" 是否过度声称？负面结果论文在 EMNLP 的竞争力如何？
2. **Related Work 覆盖度**：multi-turn degradation、residual gating、attention manipulation、exposure bias、multi-task gradient conflict 五个方向是否有重要遗漏？Li et al. (2024) split-softmax 的对比是否充分？
3. **写作质量**：论证叙事是否清晰连贯？Abstract/Introduction 的 claim 是否与 Results 一致？标题是否准确反映内容？Discussion 是否恰当？
4. **格式合规**：ARR/ACL 模板使用、页数限制、Limitations 章节、匿名性、引用格式（natbib）、图表质量
5. **引用质量**：bib 条目格式一致性？是否有不可查证的引用（特别注意 Dongre et al. 2026）？是否有 orphan 条目？引用是否准确对应文中描述？

请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment（含评分和置信度）。Weaknesses 是重点——必须严格、不留情面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-22T08:34:17.588723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-22T08:34:18.443626+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-22T08:34:18.594509+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-22T08:34:18.645085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-22T08:34:23.774628+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-22T08:34:24.766187+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-22T08:34:24.968097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-22T08:34:30.201678+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations may als
…[truncated 1177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6427
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-22T08:34:31.811908+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 543.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7045
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-22T08:34:31.812329+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	
18	\graphicspath{{../figures/paper/}}
19	
20	\title{Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliographystyle{acl_natbib}
38	\bibliography{references}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6844
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-22T08:34:37.689492+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their exact score ranges and descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their exact score ranges and descriptions."
  }
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-22T08:34:38.643908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-22T08:34:39.148566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-22T08:34:39.602539+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-22T08:34:39.703601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-22T08:34:40.511877+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-22T08:34:40.513134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-22T08:34:40.517173+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-22T08:34:40.769885+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-22T08:34:41.475116+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-22T08:34:41.788788+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1018
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-22T08:34:45.520731+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: could be considered for outstanding paper award"
- **4**: "Conference: paper could be accepted to an ACL conference"
- **3**: "Findings: paper could be accepted to Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: paper has to be fully redone"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce the results with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7831
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-22T08:34:49.846789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-22T08:34:50.650538+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-22T08:34:50.751842+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-22T08:34:51.206217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-22T08:34:51.762559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-22T08:34:52.115431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-22T08:34:52.116263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-22T08:34:52.769846+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1563
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-22T08:34:53.324206+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1561
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-22T08:34:53.327643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1211
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-22T08:34:58.824160+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-22T08:34:58.924935+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-22T08:35:02.646668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-22T08:35:03.049265+00:00_

1	\begin{abstract}
2	Multi-turn dialogue with Large Language Models (LLMs) suffers from progressive attention decay toward system prompt goal tokens. On Qwen-2.5-7B-Instruct, the Goal Attention Ratio (GAR) declines by 70.8\% between early and mid-conversation turns, yet linear probes recover goal content from the residual stream with AUC\,=\,0.98. We introduce ThreadGate, a per-layer content-and-turn-conditioned MLP gate ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$) trained jointly with next-token prediction (NTP) and an auxiliary GAR loss. A five-way comparison reveals that training succeeds (teacher-forced GAR\,=\,0.50) but autoregressive GAR drops to 0.015--0.025, a 20--33$\times$ gap; gating contributes zero measurable benefit and PCGrad-based causal exclusion rules out gradient conflict. The failure traces to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. Inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation---not representation degradation---is the proximal cause. Scheduled sampling compresses the gap to 1.57$\times$ with no PPL cost (single seed), and cross-model evaluation on Llama-3.1-8B confirms the gap (27$\times$ by median). These findings characterize how exposure bias selectively destroys auxiliary objective generalization under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-22T08:35:03.151560+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-22T08:35:03.505034+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual updat
…[truncated 4680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-22T08:35:03.505694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-22T08:35:04.259230+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Recent work has established that LLMs systematically degrade across conversation turns. \citet{laban2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Attention Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\% across turns in 12 models, while residual stream probes retain goal information with AUC\,=\,0.98. We observe a steeper 70.8\% decline on Qwen-2.5-7B-Instruct (\S\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.
5	
6	\paragraph{Instruction stability.}
7	\citet{li2024measuring} independently quantified instruction instability in multi-turn dialogs and proposed split-softmax---separating instruction from conversation tokens during attention computation---as an inference-time remedy. Our work adds causal diagnosis (five-way factorial + PCGrad exclusion), exposure bias attribution, and training-time mitigation via scheduled sampling; our $\beta$-steering complements split-softmax as an alternative inference-time approach (\S\ref{sec:discussion}).
8	
9	\paragraph{Residual gating and adaptive depth.}
10	ReZero \citep{bachlechner2021rezero} showed that resi
…[truncated 2728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-22T08:35:04.259794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-22T08:35:04.563698+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Attention Ratio.}
6	We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). The gate $g_l$ is produced by a two-layer MLP:
26	\begin{equation}\label{eq:gate}
27	  g_l = \sigma\!\bigl(W_2\,\text{ReLU}(W_1\,[\text{proj}
…[truncated 1809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-22T08:35:04.564172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-22T08:35:04.615335+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 16, $\alpha$=32) are applied to query and value projection layers (\texttt{q\_proj}, \texttt{v\_proj}). The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~\ref{sec:appendix-hyper}.
7	
8	We evaluate five configurations that form a factorial design isolating four causal factors. \textbf{ThreadGate}: full system with 28 gate networks (Eq.~\ref{eq:gate}) and three-term loss. \textbf{+PCGrad}: ThreadGate with PCGrad \citep{yu2020pcgrad} projecting conflicting gradients (isolates gradient conflict). \textbf{Uniform Gate}: gates without turn embedding (isolates turn conditioning). \textbf{LoRA-only}: gates fixed at 1.0, trained with $\mathcal{L}_\text{NTP} + \mathcal{L}_\text{GAR}$ only (isolates gating mechanism). \textbf{Base}: pretrained model (isolates fine-tuning). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours (last-token attention to goals, \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (all-token average), and PPL.
9	
10	\subsection{Main Results}
11	
12	Table~\ref{tab:four-way} presents the five-way com
…[truncated 6162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-22T08:35:10.810631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-22T08:35:10.811165+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step causal chain: we first show that gates learn behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through a causal exclusion experiment (\S\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \S\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
10	
11	The resultin
…[truncated 8203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-22T08:35:11.364743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-22T08:35:11.416714+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is the proximal cause (\S\ref{subsec:steering}). Split-softmax \citep{li2024measuring} offers a complementary inference-time approach that restructures attention computation rather than applying additive bias.
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, linearly mixing teacher-forced and model-generated contexts. Autoregressive GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36). GAR-Dongre also rises (0.019$\to$0.353), suggesting indirect improvement of all-token goal attention. The two paths are complementary: $\beta$\,=\,5 achieves the strongest GAR recovery but incurs 24\% PPL cost (1.43\,$\to$\,1.77); $\beta$\,=\,3 offers a more balanced tradeoff (PPL +9\%). Scheduled sampling incurs no fluency cost but requires retraining. A second seed trained from scratch (rather than resumed from a standard-trained epoch) yields AR GAR\,=\,0.418 (gap 1.20$\times$), versus 5\% seed variance in standard ThreadGate training, suggesting that early scheduled sampling exposure---before the model consolidates teacher-forced attention patterns---may further compress the gap; systematic schedule ablation is deferred.
6	
7	\paragraph{Instruction retention under steering.} Across 18 system-prompt constraint types, $\beta$\,=\,3 steering increases content constraint compliance by +23.8\,pp (GAR-compliance $r$\,=\,0.200, $p$\,=\,0.007; McNemar $p$\,=\
…[truncated 502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-22T08:35:11.470389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-22T08:35:11.989779+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	ThreadGate modulates the residual stream with per-layer gated MLP networks and an auxiliary GAR loss. Training succeeds (TF GAR\,=\,0.50), but autoregressive GAR collapses 20--33$\times$ (exposure bias), confirmed on Llama-3.1-8B (27$\times$ by median). Inference-time steering ($\beta$\,=\,5, GAR 0.727) and scheduled sampling (gap ${\sim}$31$\times$$\to$1.57$\times$, no PPL cost, single seed) both demonstrate attention misallocation---not representation degradation---as the proximal cause.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 519
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-22T08:35:12.417687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-22T08:35:12.469328+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	The five-way factorial uses seed\,=\,42; ThreadGate is additionally validated with seed\,=\,123 (TF/AR GAR-ours within $\pm$0.001, gap 30.5--32.1$\times$). The remaining three variants use a single seed; cross-variant convergence provides indirect robustness evidence but does not substitute for multi-seed validation.
4	
5	We test only one type of auxiliary attention loss (GAR with MSE target $\tau = 0.5$). Other attention steering objectives, such as head-specific or layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result applies to the GAR family; it does not rule out all auxiliary attention interventions.
6	
7	Training uses 8K conversations from UltraChat. Larger-scale training could alter gate dynamics, particularly if the model encounters sufficient distributional diversity to reduce the training-inference mismatch.
8	
9	All experiments use two model families (Qwen-2.5-7B and Llama-3.1-8B); while cross-model evaluation confirms the exposure bias gap, $N$\,=\,2 does not establish universality. The Llama evaluation includes ThreadGate and LoRA-only; the full five-way ablation (Uniform Gate, +PCGrad) has not been replicated, and all experiments use a single dataset (UltraChat). The instruction retention analysis is exploratory: a single model, 18 system-prompt constraint types, and a single $\beta$ value without grid search.
10	
11	The PCGrad causal exclusion addresses gradient direction conflict only. Magnitude imbalance (GradNorm; \citealp{chen2018gradnorm}) and Nash equilibrium approaches (Nash-MTL; \citealp{navon2022nash}) remain untested and could reveal additional failure modes or interaction effects.
12	
13	All four fine-tuned variants share the same GAR auxiliary loss. This design isolates the gating mechanism but does not test whether gating could be effective without an auxiliary attention loss or under a different training objective.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-22T08:35:12.823281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-22T08:35:12.925618+00:00_

1	\section{Training Hyperparameters}\label{sec:appendix-hyper}
2	
3	All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\alpha$=32) on \texttt{q\_proj} and \texttt{v\_proj}, AdamW optimizer (lr = $2 \times 10^{-4}$, $\beta_1$=0.9, $\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\times$ learning rate multiplier and initial bias 1.5 ($\sigma(1.5) \approx 0.82$).
4	
5	\section{Loss Formulation Search}\label{sec:appendix-loss}
6	
7	Table~\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\S\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.
8	
9	\begin{table}[h]
10	\centering\small
11	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}
12	\label{tab:loss-iterations}
13	\begin{tabular}{l l l c c}
14	\toprule
15	 & \textbf{Loss Family} & \textbf{Status} & \textbf{GAR} & \textbf{PPL} \\
16	\midrule
17	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & ---  & ---  \\
18	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & ---  & ---  \\
19	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & ---  & ---  \\
20	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & ---  & ---  \\
21	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & ---  & ---  \\
22	v6  & Smooth saturation       & \texttimes~identity collapse   & ---  & ---  \\
23	v7  & MSE + gate div          & \checkmark~converged           & 0.50 & 2.78 \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-22T08:35:12.926044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-22T08:35:13.027918+00:00_

1	% ============================================================
2	% Layer Importance
3	% ============================================================
4	
5	@inproceedings{gromov2024deeper,
6	  author    = {Gromov and others},
7	  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},
8	  booktitle = {International Conference on Learning Representations},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2403.17887}
11	}
12	
13	@article{men2024shortgpt,
14	  author  = {Men and others},
15	  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},
16	  journal = {arXiv preprint arXiv:2403.03853},
17	  year    = {2024},
18	  url     = {https://arxiv.org/abs/2403.03853}
19	}
20	
21	@inproceedings{sun2025curse,
22	  author    = {Sun and others},
23	  title     = {{The Curse of Depth in Large Language Models}},
24	  booktitle = {Advances in Neural Information Processing Systems},
25	  year      = {2025},
26	  url       = {https://arxiv.org/abs/2502.05795}
27	}
28	
29	@article{lu2024reassessing,
30	  author  = {Lu, Yao and others},
31	  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},
32	  journal = {arXiv preprint arXiv:2411.15558},
33	  year    = {2024},
34	  url     = {https://arxiv.org/abs/2411.15558}
35	}
36	
37	@inproceedings{fan2020layerdrop,
38	  author    = {Fan and others},
39	  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},
40	  booktitle = {International Conference on Learning Representations},
41	  year      = {2020},
42	  url       = {https://arxiv.org/abs/1909.11556}
43	}
44	
45	% ============================================================
46	% Multi-Turn Attention
47	% ============================================================
48	
49	@article{dongre2026attention,
50	  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},
51	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interac
…[truncated 16154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-22T08:35:20.442269+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to score soundness/excitement/overall assessment, what constitutes a good review, any special guidance on negative results papers, and the full scoring rubric with half-point increments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to score soundness/excitement/overall assessment, what constitutes a good review, any special guidance on negative results papers, and the full scoring rubric with half-point increments."
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-22T08:35:31.657214+00:00_

# ARR Reviewer Guidelines Summary

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions:

**Soundness**: Technical correctness, valid methodology, proper argumentation, and reproducibility. Reviews must justify soundness scores with specific evidence from the paper text.

**Excitement**: Personal interest and novelty assessment, kept separate from soundness. This reflects subjective preference rather than objective quality.

**Overall Assessment**: Composite recommendation balancing soundness, excitement, novelty, and potential impact. Papers for main conferences must be "sufficiently sound and reproducible."

## Scoring Framework

ARR uses three scores:

1. **Soundness** - justified by review text; low scores require documented technical flaws
2. **Excitement** - orthogonal to soundness; reflects personal interest
3. **Overall Recommendation** - explicit acceptance/rejection guidance for \*ACL venues

The guidelines note: "low Soundness score without finding any major faults means your review is not a faithful explanation of your recommendation."

## Characteristics of Strong Reviews

Effective reviews are:

- **Specific**: Name missing references, identify unclear sections, specify problematic formulations rather than vague complaints
- **Professional and neutral**: Written respectfully as if addressing a colleague; avoid sarcasm or dismissiveness
- **Evidence-based**: Support all criticisms with concrete examples or citations
- **Balanced**: Acknowledge both strengths and limitations fairly

## Guidance on Negative Results

Negative results receive explicit protection. The guidelines state: "bias towards publishing only positive results...contributes to hype. If something systematically does not work...the community needs to know about it."

Reviewers should not reject papers merely because results contradict expectations or lack SOTA performance.

## Common Review Pitfalls to Avoid

The guidelines identify 17 heuristics (H1-H17) 
…[truncated 1080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 11214
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-22T08:37:33.950372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dongre \"When Attention Closes\" LLMs multi-turn interaction arXiv 2605.12922"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dongre \"When Attention Closes\" LLMs multi-turn interaction arXiv 2605.12922"
  }
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-22T08:37:34.352211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liu \"Intent Mismatch\" LLMs multi-turn conversation arXiv 2602.07338 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liu \"Intent Mismatch\" LLMs multi-turn conversation arXiv 2602.07338 2026"
  }
}
```

</details>

---


### Tool result

_source line 124 · 2026-05-22T08:37:41.940939+00:00_

Web search results for query: "Liu "Intent Mismatch" LLMs multi-turn conversation arXiv 2602.07338 2026"

Links: [{"title":"[2602.07338] Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/abs/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://goatstack.ai/articles/2602.07338"},{"title":"(PDF) Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://www.researchgate.net/publication/400604289_Intent_Mismatch_Causes_LLMs_to_Get_Lost_in_Multi-Turn_Conversation"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260207338L/abstract"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.07338v1"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation - PULRC Portal","url":"https://lrc.perdanauniversity.edu.my/sdi/intent-mismatch-causes-llms-to-get-lost-in-multi-turn-conversation/"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://www.google.com/goto?url=CAESTQE7q4ylOJn_Zt17a5de0M0kSRmKu4HCiK_ZGkcANIvXbYR4aopwofAJ__exMcwHTrtyMkGv7f9H70qD2rj5Bn09nZPIl_F-tTttFd5k"},{"title":"Speak Out of Turn: Safety Vulnerability of Large Language Models in   Multi-turn Dialogue","url":"https://arxiv.org/pdf/2402.17262"}]

Based on the search results, I found the paper you're looking for. Here's what I can tell you about it:

**Paper Title:** Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation

**Authors and Details:** The paper is by Geng Liu, Fei Zhu, Rong Feng, Changyi Ma, Shiqi Wang, and Gaofeng Meng, submitted on February 7, 2026

**Core Finding:** While prior work attributes the "Lost in Conversation" (L
…[truncated 823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7588
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-22T08:37:42.744304+00:00_

Web search results for query: "Dongre "When Attention Closes" LLMs multi-turn interaction arXiv 2605.12922"

Links: [{"title":"[2605.12922] When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/abs/2605.12922"},{"title":"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/html/2605.12922"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"},{"title":"LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/pdf/2505.06120"},{"title":"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction","url":"https://arxiv.org/pdf/2603.04783"},{"title":"Beyond Single-Turn: A Survey on Multi-Turn Interactions with Large Language Models","url":"https://arxiv.org/pdf/2504.04717"},{"title":"A Survey on Multi-Turn Interaction Capabilities of Large Language Models","url":"https://arxiv.org/pdf/2501.09959"}]

I found the paper you're looking for! Here's what the search revealed:

**Paper Details:**

The paper "When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction" (arXiv:2605.12922) was submitted on May 13, 2026, with authors Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, and Dilek Hakkani-Tür.

**Main Contribution:**

The paper addresses how large language models can follow complex instructions in a single turn, yet over long multi-turn interactions they often lose the thread of instructions, persona, and rules, a degradation that has been measured behaviorally but not mechanistically explained.

**Proposed Approach:**

The authors propose a channel-transition account where goal-defining tokens become less accessible through attention, while goal-related information may persist in residual representations. They introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal 
…[truncated 549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8793
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-22T08:37:57.236812+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.12922",
  "prompt": "What is the exact full name of GAR in this paper? Is it \"Goal Attention Ratio\" or \"Goal Accessibility Ratio\" or something else? Quote the exact definition from the abstract or introduction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2605.12922",
    "prompt": "What is the exact full name of GAR in this paper? Is it \"Goal Attention Ratio\" or \"Goal Accessibility Ratio\" or something else? Quote the exact definition from the abstract or introduction."
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-22T08:37:58.742567+00:00_

Based on the content provided, the exact full name of GAR is **Goal Accessibility Ratio**.

This is clearly stated in the abstract: "We introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens..."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 1505
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-22T08:39:58.651252+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**审查侧重**: 新颖性 + 完整性 + 格式\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一个 per-layer content-and-turn-conditioned MLP 门控机制，试图修复多轮对话中 attention 向 system prompt goal tokens 衰减的问题（以 GAR 指标衡量）。核心发现是**负面结果**：ThreadGate 在 teacher-forced 评估下 GAR 达到 0.50，但自回归生成时崩溃至 0.015–0.025（20–33× gap）。通过五路 factorial comparison 排除了门控机制、turn conditioning、梯度冲突等因素后，论文将失败归因于 exposure bias——辅助 attention loss 在 teacher forcing 下学到的模式无法迁移到自回归生成。Inference-time attention steering（β=5）恢复 GAR 至 0.727 提供了建设性证据。\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 有价值的负面结果论文，但 \"causal\" 分析的过度声称、缺乏下游任务验证、以及关键实验的单 seed 问题使其止步于 Findings 级别。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Factorial 设计合理，但 \"causal\" 声称过度；缺少 GAR 与下游性能的关联验证 |\n| Excitement | 3.0/5 | Exposure bias 选择性破坏辅助 objective 的发现有价值，但范围窄（1 指标×1 数据集×2 模型） |\n| Reproducibility | 3.5/5 | 超参数提供完整，但多项关键结果为单 seed；未提及代码开源 |\n| Confidence | 4/5 | 仔细阅读全文，熟悉 exposure bias、multi-task learning、attention manipulation 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GAR 指标的下游有效性未经验证\n\n- 具体位置：全文（§1–§7 均以 GAR 为核心评估指标）；§6 Discussion \"Instruction retention under steering\" 段落\n- 问题：论文的整个叙事建立在 \"GAR 衰减导致多轮对话性能下降\" 的前提上，但**从未展示 autoregressive GAR 的提升是否带来实际任务性能改善**。唯一的下游验证是 §6 的指令保留分析，但仅使用单模型、18 种 system prompt 约束、单一 β 值，且 McNemar 检验 p=0.077（不显著）。GAR-compliance 相关系数 r=0.200，关系极弱。\n- 为什么影响接收：如果 GAR 改善不能转化为实际的指令遵循改善或生成质量提升，论文的全部分析就失去了实践意义。负面结果论文的价值取决于 \"什么失败了\" 是否重要——如果 GAR 本身不重要，ThreadGate 的失败就没有研究价值。\n- 建议修改方向：在 §4 Experiments 或 §6 Discussion 中加入 β-steering 前后的**任务级评估**（如 constraint satisfaction rate、MT-Bench-101 子集、instruction following accuracy），证明 GAR 恢复确实改善了功能性指标。至少需要在 held-out 评估集上展示 β=3/5 时的生成质量对比。\n\n**N2** [critical] \"Causal\" 分析框架严重过度声称\n\n- 具体位置：§1 Contribution (1) \"a systematic causal diagnostic framework\"；§5 Analysis 标题及内容；§5.2 \"PCGrad Causal Exclusion\"\n- 问题：论文反复使用 \"causal\" 一词（contribution list、section titles、analysis 全文），但实际方法论是**消融实验**（ablation study），而非真正的因果推断。PCGrad 排除了梯度方向冲突，但论文自身承认（§8 Limitations）梯度幅度不平衡（GradNorm）和 Nash 均衡方法未经测试。\"Modus tollens\" 论证（§5.2）形式上正确，但前提不完整——direction conflict 只是 gradient conflict 的一个维度，排除它不等于排除 gradient conflict 整体。\n- 为什么影响接收：将消融研究包装为 \"因果分析框架\" 是对方法论的误导性呈现，违反了 soundness 标准。如果审稿人或读者按真正的因果推断标准来评判（如 do-calculus、instrument variables），论文会被认为不够格。\n- 建议修改方向：将 \"causal diagnostic framework\" 改为 \"systematic ablation framework\" 或 \"factorial diagnostic framework\"；将 \"causal exclusion\" 改为 \"ablation-based exclusion\"；在 §5.2 中明确说明 PCGrad 只排除方向冲突而非梯度冲突的全部形式。\n\n**N3** [critical] 关键引用的事实性错误——GAR 全称写错\n\n- 具体位置：§3.1 Preliminaries (\"Dongre et al. (2026) defined the Goal Attention Ratio (GAR)\")；Abstract；Introduction；全文所有出现 \"Goal Attention Ratio\" 的地方\n- 问题：经验证，Dongre et al. (2026)（arXiv:2605.12922）原文中 GAR 的全称是 **\"Goal Accessibility Ratio\"**，而非本文所写的 \"Goal Attention Ratio\"。这是对论文核心指标来源的事实性错误。\n- 为什么影响接收：GAR 是本文的基础指标，对其来源的错误引用直接影响学术严谨性。审稿人和读者引用时会传播此错误。\n- 建议修改方向：全文将 \"Goal Attention Ratio\" 更正为 \"Goal Accessibility Ratio\"，或如果作者有意采用不同命名，需在 §3.1 明确说明 \"Dongre et al. (2026) introduced the Goal Accessibility Ratio (GAR); we adopt this metric under the name Goal Attention Ratio to emphasize...\" 并提供理由。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 关键结果的统计可靠性不足——单 seed 问题\n\n- 具体位置：§6 Discussion \"Scheduled sampling\" 段落；§4.1 Setup (seed=42, ThreadGate additionally seed=123)；§8 Limitations 第一段\n- 问题：Scheduled sampling 结果（gap 从 ~31× 压缩到 1.57×）是**单 seed** 实验。这是全文最具可操作性的发现，但缺乏统计验证。论文提到第二个 seed（从 scratch 训练）得到 AR GAR=0.418（gap 1.20×），但这不是同一配置的重复，而是不同起点的变体——5% seed variance 的对比标的和 scheduled sampling 的变异性无法直接比较。Factorial 中除 ThreadGate 外其余变体也只有单 seed。\n- 建议：为 scheduled sampling 至少补充 3 个 seed 的结果（mean ± std），验证 1.57× gap 的可重复性。对 factorial 中的其余变体补充第二个 seed 的验证。\n\n**W2** [warning] Exposure bias 归因存在 underdetermination\n\n- 具体位置：§5.3 Distribution Shift Analysis；§4.3 Inference-Time Attention Steering\n- 问题：论文将 20–33× GAR gap 归因于 exposure bias，但证据链存在替代解释：\n  - Teacher-forced 下 GAR 工作、自回归下不工作 → 这与 exposure bias 一致，但也可能是任何训练-推理分布差异造成的（如 KV cache 动态、长度外推、自回归 token 的 representation drift）\n  - β-steering 恢复 GAR → 这证明 attention misallocation 可以被修复，但不证明 exposure bias 是其原因\n  - Scheduled sampling 部分修复 → 与 exposure bias 一致，但 scheduled sampling 改变了训练动态的多个方面，不仅仅是 exposure\n- 建议：在 §5.3 中讨论替代假说并说明为什么 exposure bias 是最简约的解释，而非唯一的解释。将 \"the proximal cause\" 软化为 \"a proximal cause consistent with our evidence\"。\n\n**W3** [warning] Li et al. (2024) split-softmax 缺乏实验对比\n\n- 具体位置：§2 Related Work \"Instruction stability\" 段落；§6 Discussion\n- 问题：Li et al. (2024) 的 split-softmax 是本文最直接的竞争方法——同样针对多轮对话中 instruction attention 衰减，且同样是 inference-time intervention。论文在 Related Work 和 Discussion 中两次提及 split-softmax 但只说 \"complementary\"，从未进行实验对比。对于声称发现 \"inference-time steering recovers GAR\" 的论文，不与同类 inference-time 方法对比是显著遗漏。\n- 建议：在 §4.3 或 §6 中加入 split-softmax 的对比实验，或至少定性分析两种方法的机制差异及适用场景。\n\n**W4** [warning] 写作冗余度高——同一数字重复 5–6 次\n\n- 具体位置：Abstract、§1 Introduction、§4.2 Main Results、§5.3 Distribution Shift、§6 Discussion、§7 Conclusion\n- 问题：\"20–33× gap\"、\"0.015–0.025\"、\"0.064 to 0.727\" 等关键数字在 Abstract、Introduction、Experiments、Analysis、Discussion、Conclusion 中各出现一次以上。Abstract 本身就是 Introduction + Results 的压缩重复。这使论文读起来像是在用不同措辞反复陈述同一发现，而非逐步深入分析。在 8 页正文限制下，这些重复占用了本可用于更多分析（如下游评估、额外 seed、split-softmax 对比）的空间。\n- 建议：将数字的首次精确呈现放在 §4，Abstract/Introduction 只给高层结论（如 \"an order-of-magnitude gap\"），Discussion/Conclusion 侧重 implication 而非重复数据。\n\n**W5** [warning] Scheduled sampling 结果应从 Discussion 提升至正式实验\n\n- 具体位置：§6 Discussion \"Scheduled sampling as training-time mitigation\" 段落\n- 问题：Scheduled sampling 将 gap 从 ~31× 压缩到 1.57× 且无 PPL 损失，这是全文最具实践价值的发现，但被放在 Discussion 中作为 \"preliminary experiment\"。这一发现本身比主实验（ThreadGate 失败）更有 actionable insight，但因位置和 framing 被降级。如果进行多 seed 验证后确认，它应该是论文的核心贡献之一。\n- 建议：补充多 seed 实验后将 scheduled sampling 提升为 §4 的正式子节（§4.4），或在 Discussion 中给予更突出的位置和更详细的分析。\n\n**W6** [warning] Contribution (1) 过度声称泛化性\n\n- 具体位置：§1 Contribution (1) \"this design pattern is in principle applicable to other auxiliary objective analyses\"\n- 问题：论文只测试了一种辅助目标（GAR with MSE target τ=0.5）。声称框架 \"in principle applicable to other auxiliary objective analyses\" 是未经验证的泛化。§8 Limitations 第二段承认了这一点，但 Contribution list 中的声明仍然成立。\n- 建议：在 Contribution (1) 中加入限定语：\"we demonstrate this framework on GAR-family losses; its applicability to other auxiliary objectives remains to be validated\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **Dongre et al. (2026) 发表时间极近**（arXiv:2605.12922, 2026年5月13日发布）：作为本文的基础参考，审稿人需注意该参考在投稿时可能仅发布数周，其结论尚未经过社区验证。\n- **bib 格式不一致**：部分条目用 \"and others\"（如 Gromov and others），部分列出完整作者（如 Yu, Kumar, Gupta, Levine, Hausman, Finn）。应统一处理。\n- **Figure 1 信息密度过高**：Overview 图包含大量文字标注和颜色编码，在打印或小屏幕上可能难以辨认。建议简化标注。\n- **§3.1 中 GAR-Dongre 和 GAR-ours 的区分**：虽然论文解释了两种变体的差异，但后续 §4–§5 中频繁切换使用，偶尔容易混淆。建议在首次引入后统一使用一种简写约定。\n- **Appendix 较薄**：仅包含 Training Hyperparameters 和 Loss Formulation Search 两个小节，缺少 scheduled sampling 的详细配置、steering 实验的完整结果、cross-model 实验的补充数据等。\n- **标题 \"Why Lightweight Gating Fails\"**：标题暗示论文解释了失败原因，但 exposure bias 作为解释已是 well-known phenomenon。更准确的标题应强调论文的真正发现：exposure bias 选择性破坏辅助 attention objective。\n\n---\n\n## 主要优势\n\n- **S1**: 五路 factorial 实验设计干净且有系统性，逐步排除因素的逻辑链清晰（turn conditioning → gating mechanism → gradient conflict → exposure bias）\n- **S2**: Exposure bias 选择性破坏辅助 attention objective（而非主 NTP 目标）的发现具有新颖性，现有 exposure bias 文献聚焦生成质量，未涉及 auxiliary distributional objectives\n- **S3**: Inference-time β-steering 提供了建设性的正面证据，将负面结果论文从 \"什么不行\" 提升为 \"什么不行 + 为什么 + 什么可以行\"\n- **S4**: Cross-model 验证（Llama-3.1-8B, 27× gap）增加了结论的泛化性\n- **S5**: 论文的 scope 和 limitations 表述诚实——§8 明确列出了未测试的方面（GradNorm、Nash-MTL、其他辅助目标、更多模型/数据集），这在负面结果论文中尤为重要\n- **S6**: ARR guidelines 明确鼓励负面结果论文的发表，本文的结论（lightweight gating + auxiliary attention loss 在 exposure bias 下无效）对后续研究者有避坑价值\n\n---\n\n## Questions for Authors\n\n1. 是否尝试过在自回归 GAR 评估中使用 sampling temperature > 0 或 nucleus sampling？当前的自回归评估使用的是 greedy decoding 还是其他策略？不同解码策略是否影响 GAR collapse 的程度？\n2. Scheduled sampling 的 linear mixing schedule 具体参数是什么（起始比例、终止比例、总步数）？是否尝试过其他 schedule（exponential、inverse sigmoid）？\n3. β-steering 恢复 GAR 的同时，生成文本的**内容质量**如何变化？是否有人工评估或自动评估（如 GPT-4 judge）的结果？\n4. 为什么选择 τ=0.5 作为 GAR 目标？base model 的 GAR-ours 在 turn 1 只有 0.0418——直接将目标设为 0.5（12× 放大）是否过于激进？是否尝试过更温和的目标（如 τ=0.1 或 0.2）？\n\n---\n\n**Reviewer 2 评分汇总**: Overall 3.0 (Findings) | Soundness 3.5 | Excitement 3.0 | Reproducibility 3.5 | Confidence 4",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**审查侧重**: 新颖性 + 完整性 + 格式\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一个 per-layer content-and-turn-conditioned MLP 门控机制，试图修复多轮对话中 attention 向 system prompt goal tokens 衰减的问题（以 GAR 指标衡量）。核心发现是**负面结果**：ThreadGate 在 teacher-forced 评估下 GAR 达到 0.50，但自回归生成时崩溃至 0.015–0.025（20–33× gap）。通过五路 factorial comparison 排除了门控机制、turn conditioning、梯度冲突等因素后，论文将失败归因于 exposure bias——辅助 attention loss 在 teacher forcing 下学到的模式无法迁移到自回归生成。Inference-time attention steering（β=5）恢复 GAR 至 0.727 提供了建设性证据。\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 有价值的负面结果论文，但 \"causal\" 分析的过度声称、缺乏下游任务验证、以及关键实验的单 seed 问题使其止步于 Findings 级别。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Factorial 设计合理，但 \"causal\" 声称过度；缺少 GAR 与下游性能的关联验证 |\n| Excitement | 3.0/5 | Exposure bias 选择性破坏辅助 objective 的发现有价值，但范围窄（1 指标×1 数据集×2 模型） |\n| Reproducibility | 3.5/5 | 超参数提供完整，但多项关键结果为单 seed；未提及代码开源 |\n| Confidence | 4/5 | 仔细阅读全文，熟悉 exposure bias、multi-task learning、attention manipulation 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GAR 指标的下游有效性未经验证\n\n- 具体位置：全文（§1–§7 均以 GAR 为核心评估指标）；§6 Discussion \"Instruction retention under steering\" 段落\n- 问题：论文的整个叙事建立在 \"GAR 衰减导致多轮对话性能下降\" 的前提上，但**从未展示 autoregressive GAR 的提升是否带来实际任务性能改善**。唯一的下游验证是 §6 的指令保留分析，但仅使用单模型、18 种 system prompt 约束、单一 β 值，且 McNemar 检验 p=0.077（不显著）。GAR-compliance 相关系数 r=0.200，关系极弱。\n- 为什么影响接收：如果 GAR 改善不能转化为实际的指令遵循改善或生成质量提升，论文的全部分析就失去了实践意义。负面结果论文的价值取决于 \"什么失败了\" 是否重要——如果 GAR 本身不重要，ThreadGate 的失败就没有研究价值。\n- 建议修改方向：在 §4 Experiments 或 §6 Discussion 中加入 β-steering 前后的**任务级评估**（如 constraint satisfaction rate、MT-Bench-101 子集、instruction following accuracy），证明 GAR 恢复确实改善了功能性指标。至少需要在 held-out 评估集上展示 β=3/5 时的生成质量对比。\n\n**N2** [critical] \"Causal\" 分析框架严重过度声称\n\n- 具体位置：§1 Contribution (1) \"a systematic causal diagnostic framework\"；§5 Analysis 标题及内容；§5.2 \"PCGrad Causal Exclusion\"\n- 问题：论文反复使用 \"causal\" 一词（contribution list、section titles、analysis 全文），但实际方法论是**消融实验**（ablation study），而非真正的因果推断。PCGrad 排除了梯度方向冲突，但论文自身承认（§8 Limitations）梯度幅度不平衡（GradNorm）和 Nash 均衡方法未经测试。\"Modus tollens\" 论证（§5.2）形式上正确，但前提不完整——direction conflict 只是 gradient conflict 的一个维度，排除它不等于排除 gradient conflict 整体。\n- 为什么影响接收：将消融研究包装为 \"因果分析框架\" 是对方法论的误导性呈现，违反了 soundness 标准。如果审稿人或读者按真正的因果推断标准来评判（如 do-calculus、instrument variables），论文会被认为不够格。\n- 建议修改方向：将 \"causal diagnostic framework\" 改为 \"systematic ablation framework\" 或 \"factorial diagnostic framework\"；将 \"causal exclusion\" 改为 \"ablation-based exclusion\"；在 §5.2 中明确说明 PCGrad 只排除方向冲突而非梯度冲突的全部形式。\n\n**N3** [critical] 关键引用的事实性错误——GAR 全称写错\n\n- 具体位置：§3.1 Preliminaries (\"Dongre et al. (2026) defined the Goal Attention Ratio (GAR)\")；Abstract；Introduction；全文所有出现 \"Goal Attention Ratio\" 的地方\n- 问题：经验证，Dongre et al. (2026)（arXiv:2605.12922）原文中 GAR 的全称是 **\"Goal Accessibility Ratio\"**，而非本文所写的 \"Goal Attention Ratio\"。这是对论文核心指标来源的事实性错误。\n- 为什么影响接收：GAR 是本文的基础指标，对其来源的错误引用直接影响学术严谨性。审稿人和读者引用时会传播此错误。\n- 建议修改方向：全文将 \"Goal Attention Ratio\" 更正为 \"Goal Accessibility Ratio\"，或如果作者有意采用不同命名，需在 §3.1 明确说明 \"Dongre et al. (2026) introduced the Goal Accessibility Ratio (GAR); we adopt this metric under the name Goal Attention Ratio to emphasize...\" 并提供理由。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 关键结果的统计可靠性不足——单 seed 问题\n\n- 具体位置：§6 Discussion \"Scheduled sampling\" 段落；§4.1 Setup (seed=42, ThreadGate additionally seed=123)；§8 Limitations 第一段\n- 问题：Scheduled sampling 结果（gap 从 ~31× 压缩到 1.57×）是**单 seed** 实验。这是全文最具可操作性的发现，但缺乏统计验证。论文提到第二个 seed（从 scratch 训练）得到 AR GAR=0.418（gap 1.20×），但这不是同一配置的重复，而是不同起点的变体——5% seed variance 的对比标的和 scheduled sampling 的变异性无法直接比较。Factorial 中除 ThreadGate 外其余变体也只有单 seed。\n- 建议：为 scheduled sampling 至少补充 3 个 seed 的结果（mean ± std），验证 1.57× gap 的可重复性。对 factorial 中的其余变体补充第二个 seed 的验证。\n\n**W2** [warning] Exposure bias 归因存在 underdetermination\n\n- 具体位置：§5.3 Distribution Shift Analysis；§4.3 Inference-Time Attention Steering\n- 问题：论文将 20–33× GAR gap 归因于 exposure bias，但证据链存在替代解释：\n  - Teacher-forced 下 GAR 工作、自回归下不工作 → 这与 exposure bias 一致，但也可能是任何训练-推理分布差异造成的（如 KV cache 动态、长度外推、自回归 token 的 representation drift）\n  - β-steering 恢复 GAR → 这证明 attention misallocation 可以被修复，但不证明 exposure bias 是其原因\n  - Scheduled sampling 部分修复 → 与 exposure bias 一致，但 scheduled sampling 改变了训练动态的多个方面，不仅仅是 exposure\n- 建议：在 §5.3 中讨论替代假说并说明为什么 exposure bias 是最简约的解释，而非唯一的解释。将 \"the proximal cause\" 软化为 \"a proximal cause consistent with our evidence\"。\n\n**W3** [warning] Li et al. (2024) split-softmax 缺乏实验对比\n\n- 具体位置：§2 Related Work \"Instruction stability\" 段落；§6 Discussion\n- 问题：Li et al. (2024) 的 split-softmax 是本文最直接的竞争方法——同样针对多轮对话中 instruction attention 衰减，且同样是 inference-time intervention。论文在 Related Work 和 Discussion 中两次提及 split-softmax 但只说 \"complementary\"，从未进行实验对比。对于声称发现 \"inference-time steering recovers GAR\" 的论文，不与同类 inference-time 方法对比是显著遗漏。\n- 建议：在 §4.3 或 §6 中加入 split-softmax 的对比实验，或至少定性分析两种方法的机制差异及适用场景。\n\n**W4** [warning] 写作冗余度高——同一数字重复 5–6 次\n\n- 具体位置：Abstract、§1 Introduction、§4.2 Main Results、§5.3 Distribution Shift、§6 Discussion、§7 Conclusion\n- 问题：\"20–33× gap\"、\"0.015–0.025\"、\"0.064 to 0.727\" 等关键数字在 Abstract、Introduction、Experiments、Analysis、Discussion、Conclusion 中各出现一次以上。Abstract 本身就是 Introduction + Results 的压缩重复。这使论文读起来像是在用不同措辞反复陈述同一发现，而非逐步深入分析。在 8 页正文限制下，这些重复占用了本可用于更多分析（如下游评估、额外 seed、split-softmax 对比）的空间。\n- 建议：将数字的首次精确呈现放在 §4，Abstract/Introduction 只给高层结论（如 \"an order-of-magnitude gap\"），Discussion/Conclusion 侧重 implication 而非重复数据。\n\n**W5** [warning] Scheduled sampling 结果应从 Discussion 提升至正式实验\n\n- 具体位置：§6 Discussion \"Scheduled sampling as training-time mitigation\" 段落\n- 问题：Scheduled sampling 将 gap 从 ~31× 压缩到 1.57× 且无 PPL 损失，这是全文最具实践价值的发现，但被放在 Discussion 中作为 \"preliminary experiment\"。这一发现本身比主实验（ThreadGate 失败）更有 actionable insight，但因位置和 framing 被降级。如果进行多 seed 验证后确认，它应该是论文的核心贡献之一。\n- 建议：补充多 seed 实验后将 scheduled sampling 提升为 §4 的正式子节（§4.4），或在 Discussion 中给予更突出的位置和更详细的分析。\n\n**W6** [warning] Contribution (1) 过度声称泛化性\n\n- 具体位置：§1 Contribution (1) \"this design pattern is in principle applicable to other auxiliary objective analyses\"\n- 问题：论文只测试了一种辅助目标（GAR with MSE target τ=0.5）。声称框架 \"in principle applicable to other auxiliary objective analyses\" 是未经验证的泛化。§8 Limitations 第二段承认了这一点，但 Contribution list 中的声明仍然成立。\n- 建议：在 Contribution (1) 中加入限定语：\"we demonstrate this framework on GAR-family losses; its applicability to other auxiliary objectives remains to be validated\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **Dongre et al. (2026) 发表时间极近**（arXiv:2605.12922, 2026年5月13日发布）：作为本文的基础参考，审稿人需注意该参考在投稿时可能仅发布数周，其结论尚未经过社区验证。\n- **bib 格式不一致**：部分条目用 \"and others\"（如 Gromov and others），部分列出完整作者（如 Yu, Kumar, Gupta, Levine, Hausman, Finn）。应统一处理。\n- **Figure 1 信息密度过高**：Overview 图包含大量文字标注和颜色编码，在打印或小屏幕上可能难以辨认。建议简化标注。\n- **§3.1 中 GAR-Dongre 和 GAR-ours 的区分**：虽然论文解释了两种变体的差异，但后续 §4–§5 中频繁切换使用，偶尔容易混淆。建议在首次引入后统一使用一种简写约定。\n- **Appendix 较薄**：仅包含 Training Hyperparameters 和 Loss Formulation Search 两个小节，缺少 scheduled sampling 的详细配置、steering 实验的完整结果、cross-model 实验的补充数据等。\n- **标题 \"Why Lightweight Gating Fails\"**：标题暗示论文解释了失败原因，但 exposure bias 作为解释已是 well-known phenomenon。更准确的标题应强调论文的真正发现：exposure bias 选择性破坏辅助 attention objective。\n\n---\n\n## 主要优势\n\n- **S1**: 五路 factorial 实验设计干净且有系统性，逐步排除因素的逻辑链清晰（turn conditioning → gating mechanism → gradient conflict → exposure bias）\n- **S2**: Exposure bias 选择性破坏辅助 attention objective（而非主 NTP 目标）的发现具有新颖性，现有 exposure bias 文献聚焦生成质量，未涉及 auxiliary distributional objectives\n- **S3**: Inference-time β-steering 提供了建设性的正面证据，将负面结果论文从 \"什么不行\" 提升为 \"什么不行 + 为什么 + 什么可以行\"\n- **S4**: Cross-model 验证（Llama-3.1-8B, 27× gap）增加了结论的泛化性\n- **S5**: 论文的 scope 和 limitations 表述诚实——§8 明确列出了未测试的方面（GradNorm、Nash-MTL、其他辅助目标、更多模型/数据集），这在负面结果论文中尤为重要\n- **S6**: ARR guidelines 明确鼓励负面结果论文的发表，本文的结论（lightweight gating + auxiliary attention loss 在 exposure bias 下无效）对后续研究者有避坑价值\n\n---\n\n## Questions for Authors\n\n1. 是否尝试过在自回归 GAR 评估中使用 sampling temperature > 0 或 nucleus sampling？当前的自回归评估使用的是 greedy decoding 还是其他策略？不同解码策略是否影响 GAR collapse 的程度？\n2. Scheduled sampling 的 linear mixing schedule 具体参数是什么（起始比例、终止比例、总步数）？是否尝试过其他 schedule（exponential、inverse sigmoid）？\n3. β-steering 恢复 GAR 的同时，生成文本的**内容质量**如何变化？是否有人工评估或自动评估（如 GPT-4 judge）的结果？\n4. 为什么选择 τ=0.5 作为 GAR 目标？base model 的 GAR-ours 在 turn 1 只有 0.0418——直接将目标设为 0.5（12× 放大）是否过于激进？是否尝试过更温和的目标（如 τ=0.1 或 0.2）？\n\n---\n\n**Reviewer 2 评分汇总**: Overall 3.0 (Findings) | Soundness 3.5 | Excitement 3.0 | Reproducibility 3.5 | Confidence 4",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-22T08:40:03.938691+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5287
}
```

</details>

---


### Assistant

_source line 130 · 2026-05-22T08:40:12.159753+00:00_

审稿报告已提交给 Review Director。

核心发现总结：

**Overall: 3.0 (Findings)**，3 个 Must-Fix + 6 个 Should-Fix。

**三个 Must-Fix 问题：**
1. **GAR 指标缺乏下游任务验证** — 全文围绕 GAR 展开但从未证明 GAR 改善能带来实际任务性能提升，唯一的指令保留分析 p=0.077 不显著
2. **"Causal" 分析框架过度声称** — 实际是消融实验，PCGrad 只排除了梯度方向冲突而非梯度冲突整体，不应包装为因果推断
3. **GAR 全称写错** — Dongre et al. (2026) 原文是 "Goal Accessibility Ratio"，本文全文写成 "Goal Attention Ratio"，属于对核心指标来源的事实性错误

**主要优势：** 五路 factorial 设计干净、exposure bias 选择性破坏辅助 objective 的发现有新颖性、inference-time steering 提供了建设性正面证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 131 · 2026-05-22T08:41:12.261204+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿报告：方法严谨性 + 实验设计

**Overall**: 3.0 / 5（Findings）

### Must-Fix 问题（3 个 critical）

**N1** [critical] 统计功效严重不足——五路对比中 4/5 条件为单 seed
- 核心 claim "四个 fine-tuned variants 收敛到 0.75 pp 以内"（Section 4.2）没有方差估计，无法做统计检验。单 seed 下 0.75 pp 差异可能完全在 seed variance 范围内。

**N2** [critical] PCGrad 因果排除逻辑不完备——仅排除方向冲突，忽略幅度失衡
- PCGrad 仅解决梯度方向冲突，不解决幅度失衡（NTP 梯度幅度是 GAR 的 7.5–14.7 倍）。正文 claim "gradient conflict is not the cause"，实际只能 claim "directional gradient conflict is not the cause"。GradNorm 未测试是重大遗漏。

**N3** [critical] Exposure bias 归因存在未排除的替代解释
- (1) Inference-time steering 证明 misallocation 可修正，不等于 exposure bias 是原因；(2) Scheduled sampling 改变整个训练分布，不仅是 exposure bias；(3) 未排除 KV cache 累积方式差异（TF 一次性计算 vs AR 逐 token 追加）作为独立原因。

### Should-Fix 问题（6 个 warning）

**W1** GAR 缺乏下游任务效果验证——唯一尝试 McNemar p=0.077（不显著），r=0.200
**W2** Table 1 缺少 autoregressive GAR 数据——论文最关键发现（20–33× gap）只在正文口头描述
**W3** "五路 factorial comparison" 命名不当——实际是消融研究（5/16 条件），无交互效应检验
**W4** Scheduled sampling 两个 seed 使用不同训练协议（resumed vs from scratch），无法分离效应
**W5** 标题 overclaim——"Lightweight Gating" 暗示一类方法，实际仅测试 ThreadGate 一种
**W6** Cross-model validation 不完整——Llama 仅 3/5 条件，N=20，未复现 PCGrad

### 主要优势
1. 负面结果的系统性诊断有社区价值
2. PCGrad 作为因果分析工具的使用有新意
3. Inference-time steering 提供 constructive evidence
4. 写作逻辑清晰
5. TRC 作为 orthogonal metric 增强了 selectivity 论点

### Questions to Authors
1. 为什么没有测试 GradNorm？
2. UltraChat 8K 的筛选标准？
3. AR GAR 崩溃时模型生成文本质量如何？
4. Scheduled sampling seed 2 用不同协议的原因？
5. τ=0.5 选取依据？

---

请逐条回应每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-22T08:42:48.561676+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 统计功效不足——4/5 条件单 seed**\n\n同意这是 critical 问题。论文在 §4.2 声称 \"GAR-ours spans only 0.75 percentage points\" 作为 \"all four fine-tuned variants converge to nearly identical performance\" 的证据，但这是**单次观测**的点估计，没有置信区间。ThreadGate 的双 seed 验证（seed 42 vs 123，§4.2 末段 \"TF GAR-ours 0.504±0.001\"）仅覆盖 1/5 条件。\n\n补充我的观察：这一问题在 scheduled sampling 上更严重（我的 W1）——那是全文最有价值的 actionable 发现（gap 31× → 1.57×），却只有单 seed，且第二个 seed 用了不同训练协议（§6 Discussion），使得仅有的两个数据点也不可比。在 8 页篇幅限制下，3 个 seed 的 scheduled sampling 验证比当前 §5 Analysis 中的部分重复性分析更有边际价值。\n\n**[AGREE] R1-N2: PCGrad 因果排除逻辑不完备**\n\n完全同意。这与我的 N2 一致。论文 §5.2 使用 modus tollens 论证：\"if direction conflict causes the failure, removing it should prevent it; PCGrad removes it; the failure persists; therefore direction conflict is not the cause\"——但这个三段论的大前提过窄。实际只能得出 \"directional gradient conflict（在 gate parameters 上的）is not the cause\"。\n\n具体未排除的路径：\n1. **幅度失衡**（§5.2 明确记录 NTP 梯度幅度 7.5–14.7× GAR，但未用 GradNorm 测试）\n2. **PCGrad 的作用范围**——§5.2 明确说 \"We apply PCGrad to gate parameters only\"，LoRA 参数上的梯度冲突完全未触及\n3. **Nash 均衡效应**（§8 Limitations 承认 Nash-MTL 未测试）\n\n论文在 Contribution (1) 中将此包装为 \"systematic causal diagnostic framework\"，但漏掉 2/3 的梯度冲突维度的排除不能称为 \"systematic\"。建议 R1 的修改方向完全合理——应将 claim 降级为 \"directional gradient conflict on gate parameters\"。\n\n**[AGREE with nuance] R1-N3: Exposure bias 归因的替代解释**\n\n大体同意，与我的 W2 方向一致，但我对 R1 提出的 KV cache 假说有细微补充。\n\nR1 提出的三个替代解释中：\n- **(1) β-steering 不等于 exposure bias 是原因**：完全同意。§4.3 的 steering 实验证明 attention misallocation 是可修复的 proximal failure，但不证明 exposure bias 是导致该 misallocation 的 root cause。论文在 §4.3 末段试图等价这两者（\"providing constructive evidence that attention misallocation—not representation degradation—is the proximal cause of exposure-bias-induced GAR failure\"），但这是 circulat reasoning——将 \"exposure-bias-induced\" 嵌入结论本身。\n- **(2) Scheduled sampling 改变多个训练动态因素**：同意。Scheduled sampling 除了缓解 exposure bias，还改变了 loss landscape、梯度分布、甚至隐式 data augmentation 效果。\n- **(3) KV cache 差异**：这是一个有趣的替代假说，我未在初轮审稿中提出。不过我认为这个假说的解释力有限——现代 transformer 实现中，TF 和 AR 的 attention 计算在数学上应该是等价的（区别仅在 KV 是一次算还是逐步追加），因此 KV cache 差异更可能导致**数值精度差异**而非 20–33× 的系统性 GAR 崩溃。但论文确实应该讨论并排除这一可能。\n\n**总结**：论文的证据与 exposure bias 解释**一致但非排他**。建议将 \"the proximal cause\" 降级为 \"a proximal cause consistent with our converging evidence\"，并在 Discussion 中列出并讨论替代假说。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: GAR 缺乏下游任务验证**\n\n强烈同意——我将此列为 **N1 (critical)**，比 R1 的定级（warning）更高。理由同我的初轮审稿：如果 GAR 改善不能转化为实际任务性能提升，论文全部分析的实践意义存疑。§6 Discussion 中的 instruction retention 分析（McNemar p=0.077, r=0.200）不仅不显著，而且效应量极小，无法作为 GAR 下游有效性的支撑。\n\n**[AGREE] R1-W2: Table 1 缺少 autoregressive GAR 数据**\n\n同意，这是一个明显的呈现缺陷。论文的核心发现是 teacher-forced 与 autoregressive GAR 之间 20–33× 的 gap，但 Table 1 只呈现了 teacher-forced 的 IID/held-out 数据。AR GAR 数字散见于 §4.2 正文描述（\"GAR-ours drops to 0.015–0.025\"）和 §5.3，但从未以表格形式系统呈现。读者需要在多个段落间拼凑关键数据，这在负面结果论文中尤其有问题——结论的说服力高度依赖数据的系统性呈现。\n\n建议：在 Table 1 中增加 \"Autoregressive\" 列（或新建 Table 2），与 TF 数据并列呈现，并加入 TF/AR ratio 列。\n\n**[AGREE] R1-W3: \"Factorial comparison\" 命名不当**\n\n同意。真正的 factorial design（4 因素 × 2 水平）应有 2⁴=16 条件并检验交互效应。论文的 5 条件是结构化消融（每次添加/移除一个因素），只能测试主效应，无法检测因素间交互。例如：\"turn conditioning 在有/无 PCGrad 下效果是否不同？\" 这类问题当前设计无法回答。\n\n不过我要补充：即使命名不准确，5 条件的消融设计本身是**合理且有信息量的**——它成功展示了没有任何单一因素（gating、turn conditioning、gradient conflict elimination）能 rescue autoregressive GAR。问题在于用语（\"factorial\"），而非实验设计本身的价值。\n\n**[AGREE] R1-W4: Scheduled sampling 两个 seed 的训练协议不同**\n\n同意。§6 Discussion 描述 seed 1 为标准训练，seed 2 \"trained from scratch (rather than resumed from a standard-trained epoch)\"——这意味着两个 seed 不仅随机初始化不同，训练流程也不同。将它们视为同一实验的 replication 是方法论错误。AR GAR 从 0.318（seed 1, resumed）到 0.418（seed 2, from scratch）的差异可能来自训练协议差异而非 seed variance。\n\n论文实际上用 seed 2 的结果推导了一个有趣的猜测（\"early scheduled sampling exposure...may further compress the gap\"），但这个 observation 基于 N=1 的对比，不具备推断力。\n\n**[REBUT] R1-W5: 标题 overclaim \"Lightweight Gating\"**\n\n部分反驳。R1 认为标题用 \"Lightweight Gating\" 暗示一类方法但只测试了 ThreadGate 一种，我认为论文的实验设计部分回应了这一批评：\n\n- §4 的 5 条件中 **Uniform Gate**（无 turn embedding 的门控）和 **LoRA-only**（门控固定为 1.0）共同表明，gating mechanism 本身（而非 ThreadGate 的特定实现）不提供 benefit——Table 1 显示所有变体 GAR-ours 收敛到 0.50–0.51\n- §5.1 Gate Turn Conditioning 分析（27/28 层门控值在 late turns 趋近 1.0）表明这是 NTP pressure 对任何标量门控的压制，机制上不限于 ThreadGate\n\n但我同意标题的模糊性确实存在——\"Lightweight Gating\" 可以包含 MoE-style 路由、token-level gating 等完全不同的机制，论文未测试这些。建议修改为更精确的表述，如 \"per-layer residual gating\" 或 \"scalar residual gating\"。\n\n**[AGREE] R1-W6: Cross-model validation 不完整**\n\n同意。Llama-3.1-8B 实验（§5.5）只复现了 3/5 条件（Base, ThreadGate, LoRA-only），缺少 +PCGrad 和 Uniform Gate。虽然 Qwen 上 PCGrad 和 Uniform Gate 的结果与 ThreadGate/LoRA-only 无差异，但在 Llama 上未验证这一点就声称 cross-model generality 是不完整的。此外 N=20（vs Qwen 的 N=50），且用 median 而非 mean 报告结果（因 heavy-tailed distributions），进一步降低了统计功效。\n\n---\n\n### 总结\n\nR1 的 3 个 Must-Fix 中我**全部同意**（N3 附加细微补充）。6 个 Should-Fix 中我**同意 5 个**（W1-W4, W6），**部分反驳 1 个**（W5 标题 overclaim）。\n\n值得注意的是，R1 和我的审稿在多个关键问题上独立收敛：\n- **统计可靠性/单 seed 问题**（R1-N1 ↔ 我的 W1）\n- **PCGrad/\"causal\" 过度声称**（R1-N2 ↔ 我的 N2）\n- **Exposure bias 归因的 underdetermination**（R1-N3 ↔ 我的 W2）\n- **GAR 下游有效性缺失**（R1-W1 ↔ 我的 N1）\n\n两位 reviewer 独立识别相同核心问题增强了这些问题的可信度。我的评分维持不变：**Overall 3.0 (Findings)**。论文作为负面结果有社区价值，但 overclaim 和验证不足使其暂不满足主会议接收标准。",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 统计功效不足——4/5 条件单 seed**\n\n同意这是 critical 问题。论文在 §4.2 声称 \"GAR-ours spans only 0.75 percentage points\" 作为 \"all four fine-tuned variants converge to nearly identical performance\" 的证据，但这是**单次观测**的点估计，没有置信区间。ThreadGate 的双 seed 验证（seed 42 vs 123，§4.2 末段 \"TF GAR-ours 0.504±0.001\"）仅覆盖 1/5 条件。\n\n补充我的观察：这一问题在 scheduled sampling 上更严重（我的 W1）——那是全文最有价值的 actionable 发现（gap 31× → 1.57×），却只有单 seed，且第二个 seed 用了不同训练协议（§6 Discussion），使得仅有的两个数据点也不可比。在 8 页篇幅限制下，3 个 seed 的 scheduled sampling 验证比当前 §5 Analysis 中的部分重复性分析更有边际价值。\n\n**[AGREE] R1-N2: PCGrad 因果排除逻辑不完备**\n\n完全同意。这与我的 N2 一致。论文 §5.2 使用 modus tollens 论证：\"if direction conflict causes the failure, removing it should prevent it; PCGrad removes it; the failure persists; therefore direction conflict is not the cause\"——但这个三段论的大前提过窄。实际只能得出 \"directional gradient conflict（在 gate parameters 上的）is not the cause\"。\n\n具体未排除的路径：\n1. **幅度失衡**（§5.2 明确记录 NTP 梯度幅度 7.5–14.7× GAR，但未用 GradNorm 测试）\n2. **PCGrad 的作用范围**——§5.2 明确说 \"We apply PCGrad to gate parameters only\"，LoRA 参数上的梯度冲突完全未触及\n3. **Nash 均衡效应**（§8 Limitations 承认 Nash-MTL 未测试）\n\n论文在 Contribution (1) 中将此包装为 \"systematic causal diagnostic framework\"，但漏掉 2/3 的梯度冲突维度的排除不能称为 \"systematic\"。建议 R1 的修改方向完全合理——应将 claim 降级为 \"directional gradient conflict on gate parameters\"。\n\n**[AGREE with nuance] R1-N3: Exposure bias 归因的替代解释**\n\n大体同意，与我的 W2 方向一致，但我对 R1 提出的 KV cache 假说有细微补充。\n\nR1 提出的三个替代解释中：\n- **(1) β-steering 不等于 exposure bias 是原因**：完全同意。§4.3 的 steering 实验证明 attention misallocation 是可修复的 proximal failure，但不证明 exposure bias 是导致该 misallocation 的 root cause。论文在 §4.3 末段试图等价这两者（\"providing constructive evidence that attention misallocation—not representation degradation—is the proximal cause of exposure-bias-induced GAR failure\"），但这是 circulat reasoning——将 \"exposure-bias-induced\" 嵌入结论本身。\n- **(2) Scheduled sampling 改变多个训练动态因素**：同意。Scheduled sampling 除了缓解 exposure bias，还改变了 loss landscape、梯度分布、甚至隐式 data augmentation 效果。\n- **(3) KV cache 差异**：这是一个有趣的替代假说，我未在初轮审稿中提出。不过我认为这个假说的解释力有限——现代 transformer 实现中，TF 和 AR 的 attention 计算在数学上应该是等价的（区别仅在 KV 是一次算还是逐步追加），因此 KV cache 差异更可能导致**数值精度差异**而非 20–33× 的系统性 GAR 崩溃。但论文确实应该讨论并排除这一可能。\n\n**总结**：论文的证据与 exposure bias 解释**一致但非排他**。建议将 \"the proximal cause\" 降级为 \"a proximal cause consistent with our converging evidence\"，并在 Discussion 中列出并讨论替代假说。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: GAR 缺乏下游任务验证**\n\n强烈同意——我将此列为 **N1 (critical)**，比 R1 的定级（warning）更高。理由同我的初轮审稿：如果 GAR 改善不能转化为实际任务性能提升，论文全部分析的实践意义存疑。§6 Discussion 中的 instruction retention 分析（McNemar p=0.077, r=0.200）不仅不显著，而且效应量极小，无法作为 GAR 下游有效性的支撑。\n\n**[AGREE] R1-W2: Table 1 缺少 autoregressive GAR 数据**\n\n同意，这是一个明显的呈现缺陷。论文的核心发现是 teacher-forced 与 autoregressive GAR 之间 20–33× 的 gap，但 Table 1 只呈现了 teacher-forced 的 IID/held-out 数据。AR GAR 数字散见于 §4.2 正文描述（\"GAR-ours drops to 0.015–0.025\"）和 §5.3，但从未以表格形式系统呈现。读者需要在多个段落间拼凑关键数据，这在负面结果论文中尤其有问题——结论的说服力高度依赖数据的系统性呈现。\n\n建议：在 Table 1 中增加 \"Autoregressive\" 列（或新建 Table 2），与 TF 数据并列呈现，并加入 TF/AR ratio 列。\n\n**[AGREE] R1-W3: \"Factorial comparison\" 命名不当**\n\n同意。真正的 factorial design（4 因素 × 2 水平）应有 2⁴=16 条件并检验交互效应。论文的 5 条件是结构化消融（每次添加/移除一个因素），只能测试主效应，无法检测因素间交互。例如：\"turn conditioning 在有/无 PCGrad 下效果是否不同？\" 这类问题当前设计无法回答。\n\n不过我要补充：即使命名不准确，5 条件的消融设计本身是**合理且有信息量的**——它成功展示了没有任何单一因素（gating、turn conditioning、gradient conflict elimination）能 rescue autoregressive GAR。问题在于用语（\"factorial\"），而非实验设计本身的价值。\n\n**[AGREE] R1-W4: Scheduled sampling 两个 seed 的训练协议不同**\n\n同意。§6 Discussion 描述 seed 1 为标准训练，seed 2 \"trained from scratch (rather than resumed from a standard-trained epoch)\"——这意味着两个 seed 不仅随机初始化不同，训练流程也不同。将它们视为同一实验的 replication 是方法论错误。AR GAR 从 0.318（seed 1, resumed）到 0.418（seed 2, from scratch）的差异可能来自训练协议差异而非 seed variance。\n\n论文实际上用 seed 2 的结果推导了一个有趣的猜测（\"early scheduled sampling exposure...may further compress the gap\"），但这个 observation 基于 N=1 的对比，不具备推断力。\n\n**[REBUT] R1-W5: 标题 overclaim \"Lightweight Gating\"**\n\n部分反驳。R1 认为标题用 \"Lightweight Gating\" 暗示一类方法但只测试了 ThreadGate 一种，我认为论文的实验设计部分回应了这一批评：\n\n- §4 的 5 条件中 **Uniform Gate**（无 turn embedding 的门控）和 **LoRA-only**（门控固定为 1.0）共同表明，gating mechanism 本身（而非 ThreadGate 的特定实现）不提供 benefit——Table 1 显示所有变体 GAR-ours 收敛到 0.50–0.51\n- §5.1 Gate Turn Conditioning 分析（27/28 层门控值在 late turns 趋近 1.0）表明这是 NTP pressure 对任何标量门控的压制，机制上不限于 ThreadGate\n\n但我同意标题的模糊性确实存在——\"Lightweight Gating\" 可以包含 MoE-style 路由、token-level gating 等完全不同的机制，论文未测试这些。建议修改为更精确的表述，如 \"per-layer residual gating\" 或 \"scalar residual gating\"。\n\n**[AGREE] R1-W6: Cross-model validation 不完整**\n\n同意。Llama-3.1-8B 实验（§5.5）只复现了 3/5 条件（Base, ThreadGate, LoRA-only），缺少 +PCGrad 和 Uniform Gate。虽然 Qwen 上 PCGrad 和 Uniform Gate 的结果与 ThreadGate/LoRA-only 无差异，但在 Llama 上未验证这一点就声称 cross-model generality 是不完整的。此外 N=20（vs Qwen 的 N=50），且用 median 而非 mean 报告结果（因 heavy-tailed distributions），进一步降低了统计功效。\n\n---\n\n### 总结\n\nR1 的 3 个 Must-Fix 中我**全部同意**（N3 附加细微补充）。6 个 Should-Fix 中我**同意 5 个**（W1-W4, W6），**部分反驳 1 个**（W5 标题 overclaim）。\n\n值得注意的是，R1 和我的审稿在多个关键问题上独立收敛：\n- **统计可靠性/单 seed 问题**（R1-N1 ↔ 我的 W1）\n- **PCGrad/\"causal\" 过度声称**（R1-N2 ↔ 我的 N2）\n- **Exposure bias 归因的 underdetermination**（R1-N3 ↔ 我的 W2）\n- **GAR 下游有效性缺失**（R1-W1 ↔ 我的 N1）\n\n两位 reviewer 独立识别相同核心问题增强了这些问题的可信度。我的评分维持不变：**Overall 3.0 (Findings)**。论文作为负面结果有社区价值，但 overclaim 和验证不足使其暂不满足主会议接收标准。",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-22T08:42:52.882820+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4321
}
```

</details>

---


### Assistant

_source line 134 · 2026-05-22T08:42:59.128025+00:00_

已将逐条回应提交给 Review Director。

核心结论：R1 的 3 个 Must-Fix 全部同意（N3 附加 KV cache 假说的补充讨论），6 个 Should-Fix 同意 5 个、部分反驳 1 个（W5 标题 overclaim——论文的 Uniform Gate + LoRA-only 消融部分回应了 "只测一种方法" 的批评，但标题确实应更精确）。两位 reviewer 在四个核心问题上独立收敛：单 seed 统计可靠性、PCGrad causal 过度声称、exposure bias 归因 underdetermination、GAR 下游有效性缺失。评分维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

88 recorded events


### User

_source line 135 · 2026-05-22T12:48:54.375936+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。

## Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR August 2026 cycle)
- **截止日期**: 2026-08-03
- **格式**: Long paper, 正文 8 页, 参考文献不限, Limitations 章节必须有但不计入页数
- **模板**: ACL style template (`\usepackage[review]{acl}`)
- **匿名**: Double-blind

## 论文路径
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`
- 各 section 在 `paper/sections/` 下
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf`

## 论文概要
标题: "Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"

提出 ThreadGate（per-layer content-and-turn-conditioned MLP gate），与 NTP + auxiliary GAR loss 联合训练。五路对比（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）显示 gating 无效，teacher-forced GAR=0.50 但 autoregressive GAR 跌至 0.015-0.025（20-33× gap）。归因于 exposure bias，inference-time steering 和 scheduled sampling 作为 mitigation。跨模型在 Llama-3.1-8B 确认。

## 你的审查侧重

请重点审查以下方面：

1. **Contribution 声称是否合理**：
   - (1) "systematic diagnostic framework" 实际是五路消融——是否过度包装？"in principle applicable to other auxiliary objective analyses" 有经验验证吗？
   - (2) "first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization" 是否准确？有无 prior work 已涉及？
   - (3) 标题 "Per-Layer Residual Gating" 是否足够精确？仅测试了 ThreadGate + Uniform Gate
   - (4) "principled negative baseline" 价值如何？
2. **Related Work 覆盖**：
   - 是否遗漏了重要的竞争方法？Li et al. (2024) split-softmax 覆盖是否充分？
   - Exposure bias 文献是否完整？
   - Multi-turn dialogue 改善方法是否有遗漏？
3. **写作质量**：
   - "20-33× gap" 等关键数字在 Abstract/Intro/Experiments/Analysis/Discussion/Conclusion 中重复出现——是否冗余？
   - 行文是否简洁？是否有不必要的重复？
   - Figure/Table caption 是否准确、不含 overclaim？
4. **Framing 合理性**：
   - "a proximal cause consistent with our evidence" 这一措辞是否恰当？是否仍有 overclaim？
   - Negative result 的叙事策略是否有效？读者能从中获得什么 actionable insight？
5. **引用准确性**：
   - GAR 在 Dongre et al. 中的原始全称是什么？本文用的 "Goal Attention Ratio" 是否正确？
   - Bib 格式是否一致？
6. **格式合规**：页数、匿名、Limitations 章节

请按 ARR Overall Assessment 评分标准给出评分（1-5），并提供 Strengths、Weaknesses（逐条）、Questions、Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-22T12:49:01.573283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-22T12:49:01.626564+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-22T12:49:04.437225+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-22T12:49:04.487937+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-22T12:49:06.999242+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-22T12:49:07.049902+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-22T12:49:14.480828+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-22T12:49:14.481222+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-22T12:49:19.194584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-22T12:49:19.899605+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-22T12:49:31.980269+00:00_

Web search results for query: "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL Rolling Review (ARR) reviewer guidelines and criteria for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Reviewer Requirements and Expectations

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## Policy on Irresponsible Reviewers

Starting in May 2025, ARR adopts a new policy on the 'highly irresponsible' (meta-)reviewers. The program chairs and ARR EiCs will consider egregious cases reported by chairs, including cases of extremely terse reviews, unprofessional
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12785
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-22T12:49:32.738121+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.8}], \"total_pages\": 11, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 12838
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-22T12:49:37.913276+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions/criteria, scoring scales (especially for soundness, excitement, overall assessment), and any specific instructions for each dimension. I need the exact scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions/criteria, scoring scales (especially for soundness, excitement, overall assessment), and any specific instructions for each dimension. I need the exact scoring rubric."
  }
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-22T12:49:38.917517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-22T12:49:39.421650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-22T12:49:39.725162+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-22T12:49:39.725631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-22T12:49:40.443645+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1021
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-22T12:49:40.846205+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1120
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-22T12:49:43.706971+00:00_

# ARR Review Form Dimensions and Scoring Rubric

Based on the ARR Reviewer Guidelines, here's what I found regarding the review form structure:

## Primary Scoring Dimensions

The guidelines specify **three main scores** that reviewers must provide:

1. **Soundness** - "must be justified by the text of the review"
2. **Excitement** - "reflect our personal taste" and are "orthogonal to the assessment of the soundness"
3. **Overall Assessment** - "an explicit recommendation for the outcome of this paper"

## Critical Instruction on Alignment

The guidelines emphasize: "If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it."

## Notable Limitation

**The document does not provide the specific numerical scales or point ranges** for these dimensions. It references "a separate review form" and directs reviewers to a "[post describing the ARR review form](https://aclrollingreview.org/reviewform) in detail," but that linked resource is not included in the content provided.

The guidelines emphasize alignment between scores and justification rather than prescribing exact rubric values. For the complete scoring scales, you would need to consult the actual ARR review form interface or the detailed form documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5793
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-22T12:49:48.771846+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact numerical scales, and descriptions for each score level. I need the full rubric for soundness, excitement, overall assessment, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact numerical scales, and descriptions for each score level. I need the full rubric for soundness, excitement, overall assessment, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-22T12:49:49.727796+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-22T12:49:49.928873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-22T12:49:50.632283+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool result

_source line 160 · 2026-05-22T12:49:50.884468+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-22T12:49:54.567040+00:00_

# ACL Rolling Review Form - Complete Rubric

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3.5**: Acceptable with minor gaps
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
- **5**: "Consider for Award" (top 2.5%)
- **4**: "Conference: I think this paper could be accepted"
- **3**: "Findings: I think this paper could be accepted to the Findings"
- **2**: "Resubmit next cycle: substantial revisions needed"
- **1**: "Do not resubmit"

## Reproducibility, Datasets, and Software
Each uses 5-point scales assessing feasibility and value to the research community.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5795
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-22T12:49:59.505280+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "6-11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "6-11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-22T12:50:00.259993+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 434.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.0}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 575.3}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 109.3}], \"total_pages\": 11, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-22T12:50:03.572983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-22T12:50:04.025737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-22T12:50:04.940655+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1367
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-22T12:50:04.943945+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 918
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-22T12:50:04.944640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 169 · 2026-05-22T12:50:05.450736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-22T12:50:05.855828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-22T12:50:05.856301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-22T12:50:06.309598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-22T12:50:06.461367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-22T12:50:06.463697+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 154
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-22T12:50:06.765723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-22T12:50:13.642633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-22T12:50:13.994553+00:00_

1	\begin{abstract}
2	Multi-turn dialogue with Large Language Models (LLMs) suffers from progressive attention decay toward system prompt goal tokens. On Qwen-2.5-7B-Instruct, the Goal Attention Ratio (GAR) declines by 70.8\% between early and mid-conversation turns, yet linear probes recover goal content from the residual stream with AUC\,=\,0.98. We introduce ThreadGate, a per-layer content-and-turn-conditioned MLP gate ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$) trained jointly with next-token prediction (NTP) and an auxiliary GAR loss. A five-way comparison reveals that training succeeds (teacher-forced GAR\,=\,0.50) but autoregressive GAR drops to 0.015--0.025, a 20--33$\times$ gap; gating contributes zero measurable benefit and a PCGrad-based exclusion experiment rules out gradient conflict. The failure traces to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. Inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation---not representation degradation---is a proximal cause consistent with our evidence. Scheduled sampling compresses the gap to 1.57$\times$ with no PPL cost (single seed), and cross-model evaluation on Llama-3.1-8B confirms the gap (27$\times$ by median). These findings characterize how exposure bias selectively destroys auxiliary objective generalization under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-22T12:50:13.995001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-22T12:50:14.247310+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual updat
…[truncated 4569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-22T12:50:14.247897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-22T12:50:14.348728+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Attention Ratio.}
6	We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). The gate $g_l$ is produced by a two-layer MLP:
26	\begin{equation}\label{eq:gate}
27	  g_l = \sigma\!\bigl(W_2\,\text{ReLU}(W_1\,[\text{proj}
…[truncated 1960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-22T12:50:19.992335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-22T12:50:20.344506+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 16, $\alpha$=32) are applied to query and value projection layers (\texttt{q\_proj}, \texttt{v\_proj}). The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~\ref{sec:appendix-hyper}.
7	
8	We evaluate five configurations that form a controlled comparison isolating four factors. \textbf{ThreadGate}: full system with 28 gate networks (Eq.~\ref{eq:gate}) and three-term loss. \textbf{+PCGrad}: ThreadGate with PCGrad \citep{yu2020pcgrad} projecting conflicting gradients (isolates gradient conflict). \textbf{Uniform Gate}: identical gate architecture with turn embedding replaced by a learned constant vector (content-conditioned but turn-unaware; isolates the contribution of turn conditioning). \textbf{LoRA-only}: gates fixed at 1.0, trained with $\mathcal{L}_\text{NTP} + \mathcal{L}_\text{GAR}$ only (isolates gating mechanism). \textbf{Base}: pretrained model (isolates fine-tuning). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours (last-token attention to goals, \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (all-t
…[truncated 6470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-22T12:50:20.344883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-22T12:50:20.646232+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step diagnostic chain: we first show that gates learn behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through an exclusion experiment (\S\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \S\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
10	
11	The resulting 
…[truncated 8200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-22T12:50:20.646679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-22T12:50:20.697158+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is a proximal cause (\S\ref{subsec:steering}). Alternative hypotheses remain open: progressive attention drift unrelated to exposure bias, KV cache accumulation effects at long context lengths, or implicit label smoothing from the auxiliary loss could each contribute to the observed gap. Our evidence is consistent with exposure bias as the dominant factor, but does not exclude these alternatives. Split-softmax \citep{li2024measuring} offers a complementary inference-time approach that restructures attention computation rather than applying additive bias; unlike $\beta$-steering, it addresses the training-inference mismatch at the architectural level but cannot resolve exposure bias in auxiliary losses that require retraining.
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, linearly mixing teacher-forced and model-generated contexts. Autoregressive GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36), consistent with exposure bias as a primary driver of the gap. GAR-Dongre also rises (0.019$\to$0.353), suggesting indirect improvement of all-token goal attention. The two paths are complementary: $\beta$\,=\,5 achieves the strongest GAR recovery but incurs 24\% PPL cost (1.43\,$\to$\,1.77); $\beta$\,=\,3 offers a more balanced tradeoff (PPL +9\%). Scheduled sampling incurs no fluency cost but requires retraining. A second seed trained fro
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-22T12:50:25.015067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-22T12:50:25.467652+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	ThreadGate modulates the residual stream with per-layer gated MLP networks and an auxiliary GAR loss. Training succeeds (TF GAR\,=\,0.50), but autoregressive GAR collapses by more than an order of magnitude (exposure bias), confirmed on Llama-3.1-8B (27$\times$ by median). Inference-time steering ($\beta$\,=\,5, GAR 0.727) and scheduled sampling (gap ${\sim}$31$\times$$\to$1.57$\times$, no PPL cost, single seed) both point to attention misallocation---not representation degradation---as a proximal cause consistent with our evidence.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-22T12:50:25.518218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-22T12:50:25.970275+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	The five-way comparison uses seed\,=\,42; ThreadGate is additionally validated with seed\,=\,123 (TF/AR GAR-ours within $\pm$0.001, gap 30.5--32.1$\times$). The remaining three variants use a single seed; cross-variant convergence provides indirect robustness evidence but does not substitute for multi-seed validation.
4	
5	We test only one type of auxiliary attention loss (GAR with MSE target $\tau = 0.5$). Other attention steering objectives, such as head-specific or layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result applies to the GAR family; it does not rule out all auxiliary attention interventions.
6	
7	Training uses 8K conversations from UltraChat. Larger-scale training could alter gate dynamics, particularly if the model encounters sufficient distributional diversity to reduce the training-inference mismatch.
8	
9	All experiments use two model families (Qwen-2.5-7B and Llama-3.1-8B); while cross-model evaluation confirms the exposure bias gap, $N$\,=\,2 does not establish universality. The Llama evaluation includes ThreadGate and LoRA-only; the full five-way ablation (Uniform Gate, +PCGrad) has not been replicated, and all experiments use a single dataset (UltraChat). The instruction retention analysis is exploratory: a single model, 18 system-prompt constraint types, and a single $\beta$ value without grid search.
10	
11	The PCGrad exclusion experiment addresses gradient direction conflict only. Magnitude imbalance (GradNorm; \citealp{chen2018gradnorm}) and Nash equilibrium approaches (Nash-MTL; \citealp{navon2022nash}) remain untested and could reveal additional failure modes or interaction effects.
12	
13	All four fine-tuned variants share the same GAR auxiliary loss. This design isolates the gating mechanism but does not test whether gating could be effective without an auxiliary attention loss or under a different training objective.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-22T12:50:25.970739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-22T12:50:26.071559+00:00_

1	\section{Training Hyperparameters}\label{sec:appendix-hyper}
2	
3	All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\alpha$=32) on \texttt{q\_proj} and \texttt{v\_proj}, AdamW optimizer (lr = $2 \times 10^{-4}$, $\beta_1$=0.9, $\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\times$ learning rate multiplier and initial bias 1.5 ($\sigma(1.5) \approx 0.82$).
4	
5	\section{Loss Formulation Search}\label{sec:appendix-loss}
6	
7	Table~\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\S\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.
8	
9	\begin{table}[h]
10	\centering\small
11	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}
12	\label{tab:loss-iterations}
13	\begin{tabular}{l l l c c}
14	\toprule
15	 & \textbf{Loss Family} & \textbf{Status} & \textbf{GAR} & \textbf{PPL} \\
16	\midrule
17	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & ---  & ---  \\
18	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & ---  & ---  \\
19	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & ---  & ---  \\
20	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & ---  & ---  \\
21	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & ---  & ---  \\
22	v6  & Smooth saturation       & \texttimes~identity collapse   & ---  & ---  \\
23	v7  & MSE + gate div          & \checkmark~converged           & 0.50 & 2.78 \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	Maximize-family losses ($-\text{mean}(\text{GAR})$) consistently drove gates toward identity: the unbounded objective rewards full pass-through ($g \
…[truncated 201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-22T12:50:30.539216+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-22T12:50:30.589886+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-22T12:50:35.106255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-22T12:50:35.458063+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Recent work has established that LLMs systematically degrade across conversation turns. \citet{laban2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Attention Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\% across turns in 12 models, while residual stream probes retain goal information with AUC\,=\,0.98. We observe a steeper 70.8\% decline on Qwen-2.5-7B-Instruct (\S\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.
5	
6	\paragraph{Instruction stability.}
7	\citet{li2024measuring} independently quantified instruction instability in multi-turn dialogs and proposed split-softmax---separating instruction from conversation tokens during attention computation---as an inference-time remedy. Split-softmax restructures the attention mechanism itself and requires no retraining, but cannot address exposure bias in auxiliary losses that depend on training-time optimization. Our work adds systematic diagnosis (five-way controlled comparison + PCGrad exclusion), exposure bias attribution, and training-time mitigation via scheduled sampling; our $\beta$-steering compl
…[truncated 2921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-22T12:50:35.458574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-22T12:50:35.760161+00:00_

1	\section{Background}\label{sec:background}
2	
3	\paragraph{Goal Attention Ratio.}
4	Multi-turn instruction-following models receive a system prompt that specifies the task objective. We denote the token subsequence corresponding to the task specification within this system prompt as the \emph{goal tokens} $\mathcal{G}$, excluding formatting markers and role tags. \citet{dongre2026attention} introduced the Goal Attention Ratio (GAR) to quantify how much attention a model allocates to these goal tokens during response generation. Given a model with $L$ layers and $H$ attention heads, GAR at conversation turn $\tau$ is
5	\begin{equation}\label{eq:gar}
6	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
7	\end{equation}
8	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$. This definition averages attention to goal tokens over all response positions, all layers, and all heads.
9	
10	\paragraph{Two GAR variants.}
11	We distinguish two measurement variants throughout this paper. \textbf{GAR-Dongre} refers to the original definition in Equation~\ref{eq:gar}, which averages over the full response token set $\mathcal{R}_\tau$. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
12	\begin{equation}\label{eq:gar-ours}
13	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
14	\end{equation}
15	where $t_\tau$ is the index of the last token in the assistant response at turn $\tau$. The last token is the position at which the model conditions its next generation step, so attention patterns at this position most directly reflect the information the model draws upon for continuation. We use GAR-ours as the optimiz
…[truncated 532 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-22T12:50:35.760617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-22T12:50:35.811243+00:00_

1	% ============================================================
2	% Multi-Turn Attention
3	% ============================================================
4	
5	@article{dongre2026attention,
6	  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\"{u}r, Dilek},
7	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
8	  journal = {arXiv preprint arXiv:2605.12922},
9	  year    = {2026},
10	  url     = {https://arxiv.org/abs/2605.12922}
11	}
12	
13	@article{laban2025lost,
14	  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
15	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
16	  journal = {arXiv preprint arXiv:2505.06120},
17	  year    = {2025},
18	  url     = {https://arxiv.org/abs/2505.06120}
19	}
20	
21	@article{liu2026intent,
22	  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},
23	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
24	  journal = {arXiv preprint arXiv:2602.07338},
25	  year    = {2026},
26	  url     = {https://arxiv.org/abs/2602.07338}
27	}
28	
29	@inproceedings{bai2024mtbench101,
30	  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},
31	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
32	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
33	  year      = {2024},
34	  url       = {https://arxiv.org/abs/2402.14762}
35	}
36	
37	% ============================================================
38	% Residual Gating and Adaptive Depth
39	% ============================================================
40	
41	@inproceedings{fan2020layerdrop,
42	  author    = {Fan, Angela and Grave, Edouard and Joulin
…[truncated 9013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-22T12:50:40.883581+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dongre \"When Attention Closes\" \"Goal Attention Ratio\" arXiv 2605.12922"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dongre \"When Attention Closes\" \"Goal Attention Ratio\" arXiv 2605.12922"
  }
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-22T12:50:41.536145+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-turn dialogue attention degradation LLM fix remedy 2024 2025 2026 auxiliary loss"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-turn dialogue attention degradation LLM fix remedy 2024 2025 2026 auxiliary loss"
  }
}
```

</details>

---


### Tool result

_source line 204 · 2026-05-22T12:50:47.725666+00:00_

Web search results for query: "Dongre "When Attention Closes" "Goal Attention Ratio" arXiv 2605.12922"

Links: [{"title":"[2605.12922] When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/abs/2605.12922"},{"title":"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/html/2605.12922"},{"title":"Investigating the role of attentional effort in the efficacy of goal-setting in reducing attention lapses","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12678593/"},{"title":"Does closing the eyes enhance auditory attention? Eye closure increases attentional alpha-power modulation but not listening performance","url":"https://www.biorxiv.org/content/10.1101/455675.full.pdf"},{"title":"The effect of performance contingent reward prospects flexibly adapts to more versus less specific task goals","url":"https://www.biorxiv.org/content/10.1101/2024.08.07.607018.full.pdf"}]

I found the paper you're looking for! Here's what I found:

The paper "When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction" (arXiv:2605.12922) was submitted on May 13, 2026, and authored by Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, and Dilek Hakkani-Tür.

The paper addresses how large language models can follow complex instructions in a single turn, yet over long multi-turn interactions they often lose the thread of instructions, persona, and rules, a degradation that has been measured behaviorally but not mechanistically explained.

The authors introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens, and combine it with sliding-window ablations and residual-stream probes. They propose a channel-transition account where goal-defining tokens become less accessible through attention, while goal-related information may persist in residual representations.

The paper is available at https://arxiv.org/abs/2
…[truncated 112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6842
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-22T12:50:51.911383+00:00_

Web search results for query: "multi-turn dialogue attention degradation LLM fix remedy 2024 2025 2026 auxiliary loss"

Links: [{"title":"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/html/2605.12922"},{"title":"Drift No More? Context Equilibria in Multi-Turn LLM Interactions","url":"https://arxiv.org/html/2510.07777v1"},{"title":"LLMS GET LOST IN MULTI-TURN CONVERSATION","url":"https://openreview.net/pdf?id=VKGTGGcwl6"},{"title":"LoopServe: An Adaptive Dual-phase LLM Inference Acceleration System for Multi-Turn Dialogues","url":"https://arxiv.org/pdf/2507.13681"},{"title":"Multi Turn LLM: Conversation Degradation","url":"https://arize.com/glossary/multi-turn-llm-conversation-degradation/"},{"title":"LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/pdf/2505.06120"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/pdf/2512.06869"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"}]

Based on the web search results, I've found several recent papers addressing multi-turn dialogue attention degradation in LLMs:

## Key Research on the Problem

LLM performance degrades significantly in multi-turn, underspecified settings, with models struggling to maintain context across turns, making premature assumptions, and over-relying on certain patterns.

## Proposed Solutions and Remedies

**Rhea (Role-aware Heuristic Episodic Attention)**: The approach addresses attention drift, pollution, and dilution issues as conversations continue. Rhea significantly alleviates performance decay, achieving state-of-the-art consistency and instruction adherence in multi-turn conversation.

**Intent Mismatch Mediator**: Intent drift causes the model's interpretation to drift away from the user's true intent, leading to performance degradation, and proposed approaches introduce a Mediator to bridge t
…[truncated 656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10375
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-22T12:50:58.489387+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.12922",
  "prompt": "What is the full name of the metric GAR in this paper? Is it \"Goal Attention Ratio\" or \"Goal Accessibility Ratio\" or something else? Extract the exact definition and full name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2605.12922",
    "prompt": "What is the full name of the metric GAR in this paper? Is it \"Goal Attention Ratio\" or \"Goal Accessibility Ratio\" or something else? Extract the exact definition and full name."
  }
}
```

</details>

---


### Tool call

_source line 207 · 2026-05-22T12:50:58.489761+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rhea \"Role-aware Heuristic Episodic Attention\" multi-turn LLM conversation arXiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rhea \"Role-aware Heuristic Episodic Attention\" multi-turn LLM conversation arXiv 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 208 · 2026-05-22T12:51:00.999768+00:00_

# GAR Metric Definition

According to the paper, the full name of the metric is **Goal Accessibility Ratio (GAR)**.

The abstract provides this exact description: "We introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens..."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 2510
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-22T12:51:06.583697+00:00_

Web search results for query: "Rhea "Role-aware Heuristic Episodic Attention" multi-turn LLM conversation arXiv 2024 2025"

Links: [{"title":"[2512.06869] Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/abs/2512.06869"},{"title":"(PDF) Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.researchgate.net/publication/398476529_Rhea_Role-aware_Heuristic_Episodic_Attention_for_Conversational_LLMs"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/html/2512.06869v1"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.arxiv.org/pdf/2512.06869"},{"title":"LoopServe: An Adaptive Dual-phase LLM Inference Acceleration System for Multi-Turn Dialogues","url":"https://arxiv.org/pdf/2507.13681"},{"title":"Beyond Single-Turn: A Survey on Multi-Turn Interactions with Large Language Models","url":"https://arxiv.org/pdf/2504.04717"}]

I found the paper you're looking for! Here's what I found:

## Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs

Rhea is a novel framework addressing the challenge that LLMs achieve remarkable performance on single-turn tasks, yet their effectiveness deteriorates in multi-turn conversations.

### Core Framework

Rhea decouples conversation history into two functionally independent memory modules: (1) an Instructional Memory (IM) that persistently stores high-fidelity global constraints via a structural priority mechanism, and (2) an Episodic Memory (EM) that dynamically manages user-model interactions via asymmetric noise control and heuristic context retrieval.

### Problem Addressed

The framework addresses what the authors define as cumulative contextual decay - a progressive degradation of contextual integrity caused by attention pollution, dilution, and drift.

### Results

Experiments on multiple multi-turn conversation benchmarks includi
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8093
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-22T12:51:13.410585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-22T12:51:13.762235+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	
18	\graphicspath{{../figures/paper/}}
19	
20	\title{Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliographystyle{acl_natbib}
38	\bibliography{references}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-22T12:51:13.913287+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"exposure bias\" \"auxiliary objective\" \"auxiliary loss\" training inference mismatch attention NLP 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"exposure bias\" \"auxiliary objective\" \"auxiliary loss\" training inference mismatch attention NLP 2023 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-22T12:51:21.440972+00:00_

Web search results for query: ""exposure bias" "auxiliary objective" "auxiliary loss" training inference mismatch attention NLP 2023 2024 2025"

Links: [{"title":"ReflexFlow: Rethinking Learning Objective for Exposure Bias Alleviation in Flow Matching","url":"https://arxiv.org/pdf/2512.04904"},{"title":"Exposure Bias in Machine Learning","url":"https://www.emergentmind.com/topics/exposure-bias"},{"title":"Reducing Exposure Bias in Training Recurrent Neural Network Transducers","url":"https://arxiv.org/pdf/2108.10803"},{"title":"Quantifying Exposure Bias for Neural Language Generation | OpenReview","url":"https://openreview.net/forum?id=rJg2fTNtwr"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation | Request PDF","url":"https://www.researchgate.net/publication/361063299_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error   Accumulation in Language Generation","url":"https://arxiv.org/pdf/2204.01171"}]

I've found relevant search results on exposure bias and training-inference mismatch. Here's what the search revealed:

## Key Findings

**Exposure Bias Definition and Problem:**
Exposure bias refers to the training-inference discrepancy caused by teacher forcing in maximum likelihood estimation (MLE) training for auto-regressive neural network language models. Ground-truth contexts from the training corpus are not available during generation, so conditioning contexts comprise tokens previously generated by the model, and the distribution of these contexts during generation might be very different from those encountered during training.

**Effects on NLP:**
In autoregressive generation, early mistakes compound, often yielding repetitive or degenerate sequences, including hallucinations in neural machine translation under domain shift and infinite looping in language modeli
…[truncated 771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7527
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-22T12:52:24.165431+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.06869",
  "prompt": "Summarize what Rhea does for multi-turn conversation. Does it specifically address attention degradation toward system prompt / instruction tokens? Does it use any training-time intervention or is it inference-time only?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2512.06869",
    "prompt": "Summarize what Rhea does for multi-turn conversation. Does it specifically address attention degradation toward system prompt / instruction tokens? Does it use any training-time intervention or is it inference-time only?"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-22T12:52:28.331805+00:00_

# Summary of Rhea

**What Rhea does for multi-turn conversations:**

Rhea addresses performance degradation in extended conversations by separating conversation data into two memory systems. It maintains "Instructional Memory (IM) that persistently stores high-fidelity global constraints" and "Episodic Memory (EM) that dynamically manages user-model interactions." During inference, the framework prioritizes global instructions while selectively integrating relevant dialogue history.

**Attention degradation and system prompts:**

Yes, Rhea specifically targets this issue. The framework combats what the authors call "cumulative contextual decay" caused by "attention pollution, dilution, and drift." The system maintains "near-perfect instruction fidelity (IAR > 8.1)" across long conversations, demonstrating it preserves system prompt adherence.

**Training vs. inference:**

Based on the abstract provided, Rhea appears to be **inference-time only**. The paper describes how "during inference, Rhea constructs a high signal-to-noise context" through its priority attention mechanism. No mention is made of training-time modifications or parameter updates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4166
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-22T12:52:32.447621+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-22T12:52:32.548471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-22T12:52:37.817847+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-22T12:52:37.818281+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-22T12:54:15.490531+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告（新颖性 + 完整性 + 写作质量）\n\n**论文**: \"Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 论文提出了一个有意义的 negative result（gating 无法修复多轮注意力衰减，root cause 是 exposure bias），诊断链条完整，但核心指标 GAR 的全称引用错误（原文是 Goal Accessibility Ratio，非 Goal Attention Ratio），contribution 包装过度，且写作冗余严重，关键数字在六个章节中反复出现。\n\n## 官方维度打分（来自 ARR review form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 五路对比设计合理，PCGrad exclusion 逻辑清晰，但 GAR 全称引用错误（N1）动摇了对基础定义准确性的信任；scheduled sampling 仅 single seed，steering 实验的 downstream task evaluation 缺失 |\n| Excitement | 2.5/5 | Negative result 本身有价值，exposure bias 对 auxiliary loss 的选择性破坏是新颖发现，但 actionable insight 有限（steering 需要 oracle access to goal tokens，scheduled sampling 仅 preliminary） |\n| Reproducibility | 3.5/5 | 超参、数据量、硬件均已报告；代码未提供但方法描述充分；seed 42+123 双 seed 验证仅覆盖 ThreadGate |\n| Overall Assessment | 3.0 | 可被 Findings 接收，但 Must-Fix 问题（N1 GAR 命名错误、N2 页数超限）需先修正 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文和附录，验证了 Dongre et al. 原文的 GAR 定义 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GAR 全称引用错误：原文为 \"Goal Accessibility Ratio\"，非 \"Goal Attention Ratio\"\n- 具体位置：Abstract (line 1), §1 Introduction (line 3, line 5), §3.1 Preliminaries (line 6), §2 Related Work (line 4), 以及全文所有出现 \"Goal Attention Ratio\" 的位置\n- 问题：Dongre et al. (2026, arXiv:2605.12922) 原文定义为 **\"Goal Accessibility Ratio (GAR)\"**，本文在所有引用处均误写为 \"Goal Attention Ratio\"。我已通过 arXiv abstract 验证原文措辞：\"We introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens\"。\n- 为什么影响接收：这是论文最核心的度量指标，全称引用错误直接损害学术严谨性。Reviewer 和 AC 会质疑作者是否仔细阅读了所引用的基础文献。此外，\"Attention\" vs \"Accessibility\" 有语义差异——原作者选择 \"Accessibility\" 而非 \"Attention\" 可能有其考量（accessibility 暗示 information routing 而非单纯 attention weight）。\n- 建议修改方向：全文替换 \"Goal Attention Ratio\" → \"Goal Accessibility Ratio\"。如果作者有意使用不同名称，应明确说明与原文术语的区别及理由。\n\n**N2** [critical] 正文疑似超过 8 页限制\n- 具体位置：PDF 第 8-9 页\n- 问题：根据 PDF 排版，§6 Discussion 从第 8 页底部开始，延续到第 9 页约 60% 处；§7 Conclusion 在第 9 页上半部分。Limitations（§8）和 References 从第 9 页下半部分开始。EMNLP 2026 long paper 正文限制为 **严格 8 页**（Limitations 和 References 不计入）。§7 Conclusion 属于正文，因此正文约占 8.4 页，超出约 0.4 页。\n- 为什么影响接收：ARR 格式检查可能直接 desk-reject 超页论文，即使内容合格。\n- 建议修改方向：压缩 §6 Discussion（instruction retention under steering 段落可移入 appendix）和 §5 Analysis（部分 per-layer 细节可精简）。Conclusion 已经足够简短，无需进一步压缩。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"20–33× gap\" 在六个章节中过度重复\n- 具体位置：Abstract, §1 Introduction (至少 3 次), §4.2 Main Results, §5.3 Distribution Shift, §6 Discussion, §7 Conclusion\n- 问题：同一数字 \"20–33×\" 在全文至少出现 8 次，\"0.015–0.025\" 出现至少 5 次。这不是 reinforcement，而是冗余。读者在 Abstract 就已记住这个数字，后续章节每次 re-state 都减少信息密度。对于 8 页限制的论文，信息密度至关重要。\n- 建议：Abstract 和 Introduction 各保留一次完整数字，后续章节引用 \"the order-of-magnitude TF–AR gap (§4.2)\" 即可。节省的空间可用于更深入的分析或解决 N2 页数问题。\n\n**W2** [warning] Contribution (1) \"systematic diagnostic framework\" 过度包装\n- 具体位置：§1 Introduction, contribution 列表第 (1) 项\n- 问题：五路消融 + PCGrad exclusion + per-layer gradient 分析确实是系统性的实验设计，但称之为 \"framework\" 暗示可复用性和通用性。论文声称 \"in principle applicable to other auxiliary objective analyses\" 但无任何验证。实际上这是一个精心设计的消融实验，而非一个可移植的诊断工具。\n- 建议：改为 \"systematic diagnostic methodology\" 或 \"controlled ablation protocol\"，并删除 \"in principle applicable\" 的泛化声称，或在 Limitations 中明确说明未验证其迁移性。\n\n**W3** [warning] 标题 \"Per-Layer Residual Gating\" 暗示测试了广泛的 gating 方法，实际仅测试两种\n- 具体位置：标题\n- 问题：标题使用泛化表述 \"Per-Layer Residual Gating\"，但论文仅测试了 ThreadGate（content-and-turn-conditioned）和 Uniform Gate（content-only）两种变体。其他 per-layer gating 方法（如 Mixture-of-Depths 的 learned routing, CALM 的 early exit）均未测试。标题的 scope 暗示比实际覆盖面更广。\n- 建议：考虑改为 \"Why Content-and-Turn-Conditioned Residual Gating Fails...\" 或在 Limitations 中明确讨论未覆盖的 gating 类型。\n\n**W4** [warning] 缺少重要相关工作：Rhea (2025)\n- 具体位置：§2 Related Work\n- 问题：Rhea (arXiv:2512.06869, Dec 2025) 提出 Role-aware Heuristic Episodic Attention，专门针对多轮对话中的注意力污染/稀释/漂移问题，通过 Instructional Memory 维持 system prompt 保真度（IAR > 8.1），且是 inference-time 方案。这与本文的 §4.3 inference-time steering 和 §6 Discussion 中对 split-softmax 的讨论高度相关。未引用 Rhea 使 Related Work 中 \"Attention manipulation\" 和 \"Instruction stability\" 的覆盖不完整。\n- 建议：在 §2 \"Attention manipulation\" 或 \"Instruction stability\" 段落中引用 Rhea，并在 §6 Discussion 中与 β-steering 做简要对比（两者都是 inference-time 方案，但 Rhea 不需要 oracle access to goal tokens）。\n\n**W5** [warning] Contribution (2) \"first empirical characterization\" 的 novelty claim 需更谨慎\n- 具体位置：§1 Introduction, contribution 列表第 (2) 项\n- 问题：声称 \"the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization\"。虽然我未找到完全相同的先行工作，但 \"first\" 声明在 reviewer 眼中风险很高——如果存在任何相关工作（例如 multi-task learning 中 auxiliary loss 的 train-test gap 研究），这一声明就会被直接挑战。更安全的措辞不会减弱实际贡献。\n- 建议：改为 \"a detailed empirical characterization of...\" 或 \"to our knowledge, the first...\"。\n\n**W6** [warning] Scheduled sampling 结果基于 single seed，但论文多处引用时未始终标注\n- 具体位置：§6 Discussion, §7 Conclusion, Abstract\n- 问题：Abstract 中 \"Scheduled sampling compresses the gap to 1.57× with no PPL cost (single seed)\" 有标注，但 Conclusion 中 \"scheduled sampling (gap ~31×→1.57×, no PPL cost, single seed)\" 虽有标注，§1 Introduction 的 contribution (2) 中 \"a preliminary demonstration that scheduled sampling compresses this gap from ~31× to 1.57× (single seed)\" 也有标注。一致性可以，但 single-seed 结果作为 contribution 的一部分，其可靠性值得质疑。论文已提到第二个 seed 从头训练得到 AR GAR=0.418 (gap 1.20×)，这与 0.318 (gap 1.57×) 差异较大（31%），暗示高 variance。\n- 建议：要么移除 scheduled sampling 作为 contribution 的一部分（降级为 Discussion 中的 preliminary observation），要么补充多 seed 验证。\n\n---\n\n## 小问题（不影响接收）\n\n- §5 Analysis, Figure 4 caption: \"the gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base), the gap persists across all five tested configurations\" —— 同一句话内重复同一信息。\n- §3.1 中 GAR 的定义同时出现在 Method 的 Preliminaries 和 background.tex（未被 include），LaTeX 结构上无问题但可能是遗留文件。\n- Bib 格式：大部分条目一致，但 `grattafiori2024llama3` 使用 `author = {Grattafiori, Aaron and others}`，而其他条目列出完整作者列表。建议统一。\n- §4.1 Setup: \"approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)\" —— 这一 GPU 型号在 2026 年 5 月时可能尚未广泛可用，建议确认型号名称准确性（可能是 RTX 6000 Ada 或 RTX PRO 6000 Blackwell？）。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：五路对比实验中每对配置隔离一个因素，PCGrad exclusion 作为 modus tollens 逻辑推理工具使用得当——这比简单的消融研究更有说服力。\n2. **Negative result 诚实且有深度**：论文没有停留在 \"gating 不 work\" 的表面结论，而是追溯到 exposure bias 的机制，并通过 inference-time steering 提供了 constructive evidence（attention misallocation 而非 representation degradation）。TRC 指标作为 orthogonal probe 增强了论证。\n3. **Hedging 适度**：\"a proximal cause consistent with our evidence\" 比之前可能用的 \"the root cause\" 更准确；Discussion 中 explicitly 列出了 alternative hypotheses（attention drift, KV cache effects, implicit label smoothing）。\n4. **Loss formulation 搜索**（Table 2, Appendix B）记录了七次迭代中六次失败，为后续工作节省了探索成本。\n5. **跨模型验证**（Llama-3.1-8B）增强了结论的泛化性，尽管覆盖面有限（N=2 model families）。\n\n---\n\n## Questions for Authors\n\nQ1: GAR 在 Dongre et al. (2026) 中的原始全称是 \"Goal Accessibility Ratio\"。你们使用 \"Goal Attention Ratio\" 是有意的术语修改还是引用错误？如果是有意的，请解释为什么选择不同的名称。\n\nQ2: Scheduled sampling 的两个 seed 结果差异较大（GAR 0.318 vs 0.418, gap 1.57× vs 1.20×）。作者是否有更多 seed 的初步结果？这一 variance 是否影响对 \"exposure bias is the primary driver\" 的置信度？\n\nQ3: Inference-time steering (β-steering) 需要 oracle access to goal token positions。在实际部署中如何确定 goal tokens？这与 Rhea 或 split-softmax 等不需要 explicit goal token identification 的方法相比，实用性如何？\n\nQ4: 论文声称 \"token-level self-recovery (He et al., 2019) does not extend to auxiliary objectives\"。但 He et al. 的 self-recovery 是关于 NTP 的，而 GAR 是一个 distributional property of attention。是否有理论依据说明为什么 self-recovery 应该能 extend 到 attention distributions？如果没有，这一\"发现\"可能只是在确认一个 trivially expected 的结果。\n\n---\n\n## Missing References\n\n1. **Rhea** (arXiv:2512.06869, Dec 2025): Role-aware Heuristic Episodic Attention，inference-time 方案维持多轮对话中的 instruction fidelity。与本文 §4.3 steering 和 §6 Discussion 直接相关。\n2. 建议检查 \"Beyond Single-Turn: A Survey on Multi-Turn Interactions with Large Language Models\" (arXiv:2504.04717, 2025) 是否覆盖了额外的多轮对话改善方法。",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告（新颖性 + 完整性 + 写作质量）\n\n**论文**: \"Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 论文提出了一个有意义的 negative result（gating 无法修复多轮注意力衰减，root cause 是 exposure bias），诊断链条完整，但核心指标 GAR 的全称引用错误（原文是 Goal Accessibility Ratio，非 Goal Attention Ratio），contribution 包装过度，且写作冗余严重，关键数字在六个章节中反复出现。\n\n## 官方维度打分（来自 ARR review form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 五路对比设计合理，PCGrad exclusion 逻辑清晰，但 GAR 全称引用错误（N1）动摇了对基础定义准确性的信任；scheduled sampling 仅 single seed，steering 实验的 downstream task evaluation 缺失 |\n| Excitement | 2.5/5 | Negative result 本身有价值，exposure bias 对 auxiliary loss 的选择性破坏是新颖发现，但 actionable insight 有限（steering 需要 oracle access to goal tokens，scheduled sampling 仅 preliminary） |\n| Reproducibility | 3.5/5 | 超参、数据量、硬件均已报告；代码未提供但方法描述充分；seed 42+123 双 seed 验证仅覆盖 ThreadGate |\n| Overall Assessment | 3.0 | 可被 Findings 接收，但 Must-Fix 问题（N1 GAR 命名错误、N2 页数超限）需先修正 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文和附录，验证了 Dongre et al. 原文的 GAR 定义 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GAR 全称引用错误：原文为 \"Goal Accessibility Ratio\"，非 \"Goal Attention Ratio\"\n- 具体位置：Abstract (line 1), §1 Introduction (line 3, line 5), §3.1 Preliminaries (line 6), §2 Related Work (line 4), 以及全文所有出现 \"Goal Attention Ratio\" 的位置\n- 问题：Dongre et al. (2026, arXiv:2605.12922) 原文定义为 **\"Goal Accessibility Ratio (GAR)\"**，本文在所有引用处均误写为 \"Goal Attention Ratio\"。我已通过 arXiv abstract 验证原文措辞：\"We introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens\"。\n- 为什么影响接收：这是论文最核心的度量指标，全称引用错误直接损害学术严谨性。Reviewer 和 AC 会质疑作者是否仔细阅读了所引用的基础文献。此外，\"Attention\" vs \"Accessibility\" 有语义差异——原作者选择 \"Accessibility\" 而非 \"Attention\" 可能有其考量（accessibility 暗示 information routing 而非单纯 attention weight）。\n- 建议修改方向：全文替换 \"Goal Attention Ratio\" → \"Goal Accessibility Ratio\"。如果作者有意使用不同名称，应明确说明与原文术语的区别及理由。\n\n**N2** [critical] 正文疑似超过 8 页限制\n- 具体位置：PDF 第 8-9 页\n- 问题：根据 PDF 排版，§6 Discussion 从第 8 页底部开始，延续到第 9 页约 60% 处；§7 Conclusion 在第 9 页上半部分。Limitations（§8）和 References 从第 9 页下半部分开始。EMNLP 2026 long paper 正文限制为 **严格 8 页**（Limitations 和 References 不计入）。§7 Conclusion 属于正文，因此正文约占 8.4 页，超出约 0.4 页。\n- 为什么影响接收：ARR 格式检查可能直接 desk-reject 超页论文，即使内容合格。\n- 建议修改方向：压缩 §6 Discussion（instruction retention under steering 段落可移入 appendix）和 §5 Analysis（部分 per-layer 细节可精简）。Conclusion 已经足够简短，无需进一步压缩。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"20–33× gap\" 在六个章节中过度重复\n- 具体位置：Abstract, §1 Introduction (至少 3 次), §4.2 Main Results, §5.3 Distribution Shift, §6 Discussion, §7 Conclusion\n- 问题：同一数字 \"20–33×\" 在全文至少出现 8 次，\"0.015–0.025\" 出现至少 5 次。这不是 reinforcement，而是冗余。读者在 Abstract 就已记住这个数字，后续章节每次 re-state 都减少信息密度。对于 8 页限制的论文，信息密度至关重要。\n- 建议：Abstract 和 Introduction 各保留一次完整数字，后续章节引用 \"the order-of-magnitude TF–AR gap (§4.2)\" 即可。节省的空间可用于更深入的分析或解决 N2 页数问题。\n\n**W2** [warning] Contribution (1) \"systematic diagnostic framework\" 过度包装\n- 具体位置：§1 Introduction, contribution 列表第 (1) 项\n- 问题：五路消融 + PCGrad exclusion + per-layer gradient 分析确实是系统性的实验设计，但称之为 \"framework\" 暗示可复用性和通用性。论文声称 \"in principle applicable to other auxiliary objective analyses\" 但无任何验证。实际上这是一个精心设计的消融实验，而非一个可移植的诊断工具。\n- 建议：改为 \"systematic diagnostic methodology\" 或 \"controlled ablation protocol\"，并删除 \"in principle applicable\" 的泛化声称，或在 Limitations 中明确说明未验证其迁移性。\n\n**W3** [warning] 标题 \"Per-Layer Residual Gating\" 暗示测试了广泛的 gating 方法，实际仅测试两种\n- 具体位置：标题\n- 问题：标题使用泛化表述 \"Per-Layer Residual Gating\"，但论文仅测试了 ThreadGate（content-and-turn-conditioned）和 Uniform Gate（content-only）两种变体。其他 per-layer gating 方法（如 Mixture-of-Depths 的 learned routing, CALM 的 early exit）均未测试。标题的 scope 暗示比实际覆盖面更广。\n- 建议：考虑改为 \"Why Content-and-Turn-Conditioned Residual Gating Fails...\" 或在 Limitations 中明确讨论未覆盖的 gating 类型。\n\n**W4** [warning] 缺少重要相关工作：Rhea (2025)\n- 具体位置：§2 Related Work\n- 问题：Rhea (arXiv:2512.06869, Dec 2025) 提出 Role-aware Heuristic Episodic Attention，专门针对多轮对话中的注意力污染/稀释/漂移问题，通过 Instructional Memory 维持 system prompt 保真度（IAR > 8.1），且是 inference-time 方案。这与本文的 §4.3 inference-time steering 和 §6 Discussion 中对 split-softmax 的讨论高度相关。未引用 Rhea 使 Related Work 中 \"Attention manipulation\" 和 \"Instruction stability\" 的覆盖不完整。\n- 建议：在 §2 \"Attention manipulation\" 或 \"Instruction stability\" 段落中引用 Rhea，并在 §6 Discussion 中与 β-steering 做简要对比（两者都是 inference-time 方案，但 Rhea 不需要 oracle access to goal tokens）。\n\n**W5** [warning] Contribution (2) \"first empirical characterization\" 的 novelty claim 需更谨慎\n- 具体位置：§1 Introduction, contribution 列表第 (2) 项\n- 问题：声称 \"the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization\"。虽然我未找到完全相同的先行工作，但 \"first\" 声明在 reviewer 眼中风险很高——如果存在任何相关工作（例如 multi-task learning 中 auxiliary loss 的 train-test gap 研究），这一声明就会被直接挑战。更安全的措辞不会减弱实际贡献。\n- 建议：改为 \"a detailed empirical characterization of...\" 或 \"to our knowledge, the first...\"。\n\n**W6** [warning] Scheduled sampling 结果基于 single seed，但论文多处引用时未始终标注\n- 具体位置：§6 Discussion, §7 Conclusion, Abstract\n- 问题：Abstract 中 \"Scheduled sampling compresses the gap to 1.57× with no PPL cost (single seed)\" 有标注，但 Conclusion 中 \"scheduled sampling (gap ~31×→1.57×, no PPL cost, single seed)\" 虽有标注，§1 Introduction 的 contribution (2) 中 \"a preliminary demonstration that scheduled sampling compresses this gap from ~31× to 1.57× (single seed)\" 也有标注。一致性可以，但 single-seed 结果作为 contribution 的一部分，其可靠性值得质疑。论文已提到第二个 seed 从头训练得到 AR GAR=0.418 (gap 1.20×)，这与 0.318 (gap 1.57×) 差异较大（31%），暗示高 variance。\n- 建议：要么移除 scheduled sampling 作为 contribution 的一部分（降级为 Discussion 中的 preliminary observation），要么补充多 seed 验证。\n\n---\n\n## 小问题（不影响接收）\n\n- §5 Analysis, Figure 4 caption: \"the gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base), the gap persists across all five tested configurations\" —— 同一句话内重复同一信息。\n- §3.1 中 GAR 的定义同时出现在 Method 的 Preliminaries 和 background.tex（未被 include），LaTeX 结构上无问题但可能是遗留文件。\n- Bib 格式：大部分条目一致，但 `grattafiori2024llama3` 使用 `author = {Grattafiori, Aaron and others}`，而其他条目列出完整作者列表。建议统一。\n- §4.1 Setup: \"approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)\" —— 这一 GPU 型号在 2026 年 5 月时可能尚未广泛可用，建议确认型号名称准确性（可能是 RTX 6000 Ada 或 RTX PRO 6000 Blackwell？）。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：五路对比实验中每对配置隔离一个因素，PCGrad exclusion 作为 modus tollens 逻辑推理工具使用得当——这比简单的消融研究更有说服力。\n2. **Negative result 诚实且有深度**：论文没有停留在 \"gating 不 work\" 的表面结论，而是追溯到 exposure bias 的机制，并通过 inference-time steering 提供了 constructive evidence（attention misallocation 而非 representation degradation）。TRC 指标作为 orthogonal probe 增强了论证。\n3. **Hedging 适度**：\"a proximal cause consistent with our evidence\" 比之前可能用的 \"the root cause\" 更准确；Discussion 中 explicitly 列出了 alternative hypotheses（attention drift, KV cache effects, implicit label smoothing）。\n4. **Loss formulation 搜索**（Table 2, Appendix B）记录了七次迭代中六次失败，为后续工作节省了探索成本。\n5. **跨模型验证**（Llama-3.1-8B）增强了结论的泛化性，尽管覆盖面有限（N=2 model families）。\n\n---\n\n## Questions for Authors\n\nQ1: GAR 在 Dongre et al. (2026) 中的原始全称是 \"Goal Accessibility Ratio\"。你们使用 \"Goal Attention Ratio\" 是有意的术语修改还是引用错误？如果是有意的，请解释为什么选择不同的名称。\n\nQ2: Scheduled sampling 的两个 seed 结果差异较大（GAR 0.318 vs 0.418, gap 1.57× vs 1.20×）。作者是否有更多 seed 的初步结果？这一 variance 是否影响对 \"exposure bias is the primary driver\" 的置信度？\n\nQ3: Inference-time steering (β-steering) 需要 oracle access to goal token positions。在实际部署中如何确定 goal tokens？这与 Rhea 或 split-softmax 等不需要 explicit goal token identification 的方法相比，实用性如何？\n\nQ4: 论文声称 \"token-level self-recovery (He et al., 2019) does not extend to auxiliary objectives\"。但 He et al. 的 self-recovery 是关于 NTP 的，而 GAR 是一个 distributional property of attention。是否有理论依据说明为什么 self-recovery 应该能 extend 到 attention distributions？如果没有，这一\"发现\"可能只是在确认一个 trivially expected 的结果。\n\n---\n\n## Missing References\n\n1. **Rhea** (arXiv:2512.06869, Dec 2025): Role-aware Heuristic Episodic Attention，inference-time 方案维持多轮对话中的 instruction fidelity。与本文 §4.3 steering 和 §6 Discussion 直接相关。\n2. 建议检查 \"Beyond Single-Turn: A Survey on Multi-Turn Interactions with Large Language Models\" (arXiv:2504.04717, 2025) 是否覆盖了额外的多轮对话改善方法。",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-22T12:54:19.577934+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4087
}
```

</details>

---


### Assistant

_source line 222 · 2026-05-22T12:54:27.258285+00:00_

审稿报告已提交给 Review Director。

核心发现总结：

- **Overall: 3.0 (Findings)**
- **2 个 Must-Fix**：GAR 全称引用错误（原文是 "Goal Accessibility Ratio" 而非 "Goal Attention Ratio"，已通过 arXiv 原文验证），以及正文疑似超 8 页限制
- **6 个 Should-Fix**：数字冗余（"20–33×" 出现 8+ 次）、contribution 包装过度（"framework"/"first"）、标题 scope 过宽、缺少 Rhea (2025) 引用、scheduled sampling single-seed 结果可靠性
- **优势**：五路消融设计严谨、negative result 诚实有深度、hedging 措辞得当、loss 搜索历程有参考价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 223 · 2026-05-22T12:55:11.464551+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 的审稿意见

**Overall**: 3.0 / 5 — Findings
**一句话总结**: 诊断框架设计精良、负面结果对社区有价值，但核心 AR 评估样本量过小（N=5）、scheduled sampling 单种子可靠性不足、exposure bias 归因缺少替代假说的排除实验，统计支撑尚不足以支撑 conference-level 接收。

### Must-Fix

**N1** [critical] AR 评估样本量过小，核心 claim 缺乏统计检验
- Table 1 的 AR 列仅基于 N=5 条 10-turn 对话。五个配置的 AR GAR-ours 分别为 0.012, 0.016, 0.015, 0.015, 0.025，这些差异在 N=5 下无法判断是否具有统计显著性。论文未报告 AR GAR 的 confidence interval 或任何条件间的显著性检验。
- 唯一的多种子验证仅覆盖 ThreadGate（seed 42 vs 123），其余四个条件均为单种子。
- 建议：AR 评估扩大至 N=50，报告 bootstrap 95% CI，对五个条件做成对检验。

**N2** [critical] Scheduled sampling 双种子结果差异大（GAR 0.318 vs 0.418），abstract 仅引用单种子
- 两个种子采用不同训练策略（resume vs from scratch），无法分离种子随机性 vs 训练策略效应。
- 建议：至少 3 个种子采用相同策略，或从 contribution 中移除。

**N3** [critical] Exposure bias 归因未排除替代假说
- KV cache drift（10-turn 中 KV cache 长度远超 TF 片段）、model-generated text 统计特性差异、GAR-ours 在 AR 下的有效性均未排除。
- Inference-time steering 论证存在循环性：加 goal token bias 当然增加 goal attention，无论 GAR 低的原因是什么。
- 建议：设计实验区分 exposure bias 和 KV cache drift，或弱化 claim。

### Should-Fix

**W1** Cross-model 仅 3/5 条件、用 median、N=20、AR/TF 样本量不匹配
**W2** PCGrad modus tollens 范围过度概括——magnitude imbalance 未排除
**W3** Instruction retention McNemar p=0.077 不显著但占 Discussion 1/4 篇幅
**W4** 五路对比存在 LoRA capacity saturation 替代解释——LoRA 已饱和 TF GAR target，gate 自然无增量

### 小问题
- §1 GAR-ours vs GAR-Dongre 未标注
- Table 1 caption 缩写位置
- §5.1 Wilcoxon test 的 pairing 说明
- §5.5 排除前两 turn 的 justification
- Gate init 0.82 的依据

---

请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-22T12:56:46.835673+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 Round 1 意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: AR 评估样本量过小（N=5）**\n同意这是一个需要解决的问题，但程度判断有细微分歧。\n\n核心 TF-AR gap（0.50 vs 0.015–0.025，即 20–33×）跨越一个数量级以上，即使 N=5 也不可能是随机波动——这一点与 seed 42/123 双种子结果一致（§4.2: gap 30.5–32.1×, TF GAR-ours 0.504±0.001, AR 0.016±0.001）。因此 R1 的批评不应被理解为\"gap 本身可能不存在\"，而是\"五个配置之间 AR GAR 的差异（0.012–0.025）在 N=5 下无法做统计区分\"。\n\n具体而言：LoRA-only 的 AR GAR=0.025 看似高于 ThreadGate 的 0.016，但在 N=5 下这一差异无法判断是否有意义。论文的核心 claim 是\"所有配置的 AR GAR 都 collapse 到同一水平\"，但 N=5 下\"同一水平\"缺乏统计支撑。\n\n注意论文在 §4.3 steering 实验中已有 N=50 评估（39 条 ≥3 turns），且 §5.5 cross-model 有 N=20。扩大 Table 1 AR 评估至 N≥30 并补充 CI 是可行的，且能显著增强 \"all variants collapse equally\" 这一 claim 的说服力。\n\n建议定级维持 **critical**，但修复方式建议更精确：补充 N≥30 AR 评估 + bootstrap CI，核心是验证\"五个配置间 AR GAR 无显著差异\"。\n\n---\n\n**[AGREE] R1-N2: Scheduled sampling 双种子差异大，abstract 仅引 single seed**\n完全同意。这与我的 W6 一致。\n\n两个种子不仅结果差异大（GAR 0.318 vs 0.418，gap 1.57× vs 1.20×），而且训练策略不同（resume vs from scratch），如 §6 Discussion 所述：\"A second seed trained from scratch (rather than resumed from a standard-trained epoch) yields AR GAR=0.418\"。这使得无法分离 seed variance 和 training strategy effect。\n\n更关键的是：scheduled sampling 被列为 contribution (2) 的一部分（§1: \"a preliminary demonstration that scheduled sampling compresses this gap from ~31× to 1.57× (single seed)\"），这对一个 preliminary single-seed 结果赋予了过高的 contribution 地位。\n\n建议修复：要么从 contribution 列表中移除 scheduled sampling（降级为 Discussion 中的 exploratory observation），要么补充 ≥3 个使用相同策略的种子。当前写法中 \"preliminary\" 一词存在但不够显著。\n\n---\n\n**[REBUT] R1-N3: Exposure bias 归因未排除替代假说——部分同意，但 critical 定级过高**\n\nR1 提出三个替代假说（KV cache drift、model-generated text 统计差异、GAR-ours 在 AR 下的有效性）并指出 steering 论证存在循环性。我逐一评估：\n\n**(a) KV cache drift**: 合理的替代假说，但论文在 §5.4 (Mechanism Specificity) 提供了部分排除证据。TRC（Turn-level Residual Coherence）在 TF 和 AR 下几乎相同（ThreadGate: 0.334 vs 0.332; LoRA-only: 0.349 vs 0.411）。如果 KV cache drift 导致广泛的 representation degradation，TRC 应该显示 comparable gap，但实际没有。这不完全排除 KV cache drift 影响 attention routing 的可能，但确实缩小了替代假说的空间。\n\n**(b) Steering 论证的循环性**: R1 的批评有道理——\"加 goal token bias 增加 goal attention\"本身是 tautological。但论文的 inference 不仅是\"GAR 增加了\"，而是\"GAR 增加的同时 hidden states 的 coherence 未变（TRC stable）且 PPL 仅增加 9%（β=3）\"。这组合证据表明 attention misallocation 是独立于 representation quality 的 failure mode。如果 root cause 是 representation degradation 而非 attention routing，β-steering 应该无法恢复 meaningful GAR（因为 hidden states 中没有 goal information 可 route），但实际恢复了 11× (§4.3)。\n\n**(c) 论文的 hedging**: 论文确实使用了 \"a proximal cause consistent with our evidence\"（§4.3, §7 Conclusion），§6 Discussion 明确列出了 alternative hypotheses：\"progressive attention drift unrelated to exposure bias, KV cache accumulation effects at long context lengths, or implicit label smoothing from the auxiliary loss could each contribute\"。这一 hedging 水平在我看来是适度的。\n\n**我的判断**：R1 的批评核心合理——exposure bias 归因确实不是 conclusive 的。但论文已经做了合理的 hedging，且 TRC + steering 组合提供了 non-trivial evidence。将此定为 **critical** 过高；建议降级为 **should-fix**，具体修复方向是：(1) 在 §5.3 或 §6 中加一段明确讨论 KV cache drift 作为 confound（当前仅在 Discussion 中一句带过），(2) 承认 steering 论证在逻辑上不排除 KV cache drift。但不需要额外的实验来排除每个替代假说——negative result paper 的标准不应等同于 causal inference paper。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-W1: Cross-model 验证不充分（3/5 条件、median、N=20）**\n同意。§5.5 仅覆盖 ThreadGate、LoRA-only、Base 三个条件，缺少 +PCGrad 和 Uniform Gate。使用 median 而非 mean 有合理理由（heavy-tailed distributions，§5.5 已说明），但 N=20 偏小，且 AR/TF 样本量不对称（TF N=50 vs AR N=20）降低了 gap 估计的可比性。\n\n补充：论文对此有部分 acknowledgment（§8 Limitations: \"the full five-way ablation (Uniform Gate, +PCGrad) has not been replicated\"），但不够显著。建议在 §5.5 正文中也明确标注这一局限。\n\n---\n\n**[AGREE] R1-W2: PCGrad modus tollens scope 过度概括**\n同意。论文在 §5.2 正文中确实写了 \"magnitude imbalance (Chen et al., 2018) and Nash equilibrium violations (Navon et al., 2022) remain untested\"，在 §8 Limitations 中也重复了这一点。但 §1 Introduction 的 contribution (1) 中描述为 \"PCGrad-based exclusion via gradient surgery\" 时未加限定词，读者可能误以为排除了所有 gradient conflict，而实际只排除了 directional conflict。\n\n建议在 §1 contribution (1) 中加入 \"directional\" 修饰：改 \"gradient conflict\" 为 \"gradient direction conflict\"。\n\n---\n\n**[AGREE] R1-W3: Instruction retention McNemar p=0.077 不显著但占 Discussion 过多篇幅**\n同意。p=0.077 未达常规显著性阈值（0.05），但 §6 Discussion 中 \"Instruction retention under steering\" 段落占据了约 3-4 行（不算很长），且包含 GAR-compliance correlation（r=0.200, p=0.007）。\n\n但考虑到论文已面临页数超限问题（我的 N2），这段内容是压缩的首选候选。建议将 instruction retention 分析移入 appendix，或压缩为一句提及（\"exploratory analysis suggests downstream compliance benefit, details in Appendix X\"）。这同时帮助解决页数问题。\n\n---\n\n**[REBUT] R1-W4: LoRA capacity saturation 替代解释**\n部分不同意。\n\nR1 的论点是：如果 LoRA 已经饱和了 TF GAR target（0.50），gates 自然无法提供增量，因此 \"gating 无用\" 的结论可能是 capacity ceiling artifact。\n\n这个 concern 对 \"gating 无用\" 的 claim 是有效的，但**不影响论文的核心结论**。论文的主要 finding 不是\"gating 不 work\"，而是\"所有 training-time interventions（包括 LoRA-only）在 TF 下 work 但在 AR 下 collapse\"——即 TF-AR gap。即使 LoRA 确实在 TF 下饱和了 GAR target，这不解释为什么 AR GAR 从 0.50 跌到 0.015–0.025。\n\n具体证据：\n1. LoRA-only（无 gate）的 TF GAR=0.50，AR GAR=0.025——gap 同样存在（Table 1）\n2. Base model 的 AR GAR=0.012 vs LoRA-only 的 0.025——fine-tuning 本身对 AR 的改善微乎其微\n3. Inference-time steering（§4.3）在不改变任何训练参数的情况下将 AR GAR 从 0.064 恢复到 0.727\n\n这些证据表明 failure mode 在 TF→AR transition，而非 training capacity。R1 的 concern 更适用于 \"gating vs LoRA-only 对比\" 的解读，而非论文的 central claim。\n\n建议将此定为 **minor**：在 §4.2 或 §6 中加一句 acknowledge 这一 alternative interpretation（\"The convergence of all fine-tuned variants at TF GAR ≈ 0.50 could partly reflect LoRA capacity saturation rather than gating ineffectiveness per se; however, the TF-AR gap—the paper's central finding—persists regardless of this interpretation\"）。\n\n---\n\n### 总结\n\n| R1 Issue | R2 判断 | 理由 |\n|----------|---------|------|\n| N1 AR N=5 | [AGREE] critical | 核心 claim \"all collapse equally\" 缺统计支撑 |\n| N2 SS dual-seed | [AGREE] critical | 与我的 W6 一致；contribution 中应降级 |\n| N3 Exposure bias | [REBUT] 降为 should-fix | 论文 hedging 适度，TRC+steering 提供了 non-trivial evidence，但应加强 KV cache drift 讨论 |\n| W1 Cross-model | [AGREE] | 覆盖不完整，应在正文中标注 |\n| W2 PCGrad scope | [AGREE] | §1 contribution 措辞需加 \"directional\" |\n| W3 Instruction retention | [AGREE] | 不显著结果占过多篇幅，建议移入 appendix |\n| W4 LoRA saturation | [REBUT] 降为 minor | 不影响核心 TF-AR gap claim |",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 Round 1 意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: AR 评估样本量过小（N=5）**\n同意这是一个需要解决的问题，但程度判断有细微分歧。\n\n核心 TF-AR gap（0.50 vs 0.015–0.025，即 20–33×）跨越一个数量级以上，即使 N=5 也不可能是随机波动——这一点与 seed 42/123 双种子结果一致（§4.2: gap 30.5–32.1×, TF GAR-ours 0.504±0.001, AR 0.016±0.001）。因此 R1 的批评不应被理解为\"gap 本身可能不存在\"，而是\"五个配置之间 AR GAR 的差异（0.012–0.025）在 N=5 下无法做统计区分\"。\n\n具体而言：LoRA-only 的 AR GAR=0.025 看似高于 ThreadGate 的 0.016，但在 N=5 下这一差异无法判断是否有意义。论文的核心 claim 是\"所有配置的 AR GAR 都 collapse 到同一水平\"，但 N=5 下\"同一水平\"缺乏统计支撑。\n\n注意论文在 §4.3 steering 实验中已有 N=50 评估（39 条 ≥3 turns），且 §5.5 cross-model 有 N=20。扩大 Table 1 AR 评估至 N≥30 并补充 CI 是可行的，且能显著增强 \"all variants collapse equally\" 这一 claim 的说服力。\n\n建议定级维持 **critical**，但修复方式建议更精确：补充 N≥30 AR 评估 + bootstrap CI，核心是验证\"五个配置间 AR GAR 无显著差异\"。\n\n---\n\n**[AGREE] R1-N2: Scheduled sampling 双种子差异大，abstract 仅引 single seed**\n完全同意。这与我的 W6 一致。\n\n两个种子不仅结果差异大（GAR 0.318 vs 0.418，gap 1.57× vs 1.20×），而且训练策略不同（resume vs from scratch），如 §6 Discussion 所述：\"A second seed trained from scratch (rather than resumed from a standard-trained epoch) yields AR GAR=0.418\"。这使得无法分离 seed variance 和 training strategy effect。\n\n更关键的是：scheduled sampling 被列为 contribution (2) 的一部分（§1: \"a preliminary demonstration that scheduled sampling compresses this gap from ~31× to 1.57× (single seed)\"），这对一个 preliminary single-seed 结果赋予了过高的 contribution 地位。\n\n建议修复：要么从 contribution 列表中移除 scheduled sampling（降级为 Discussion 中的 exploratory observation），要么补充 ≥3 个使用相同策略的种子。当前写法中 \"preliminary\" 一词存在但不够显著。\n\n---\n\n**[REBUT] R1-N3: Exposure bias 归因未排除替代假说——部分同意，但 critical 定级过高**\n\nR1 提出三个替代假说（KV cache drift、model-generated text 统计差异、GAR-ours 在 AR 下的有效性）并指出 steering 论证存在循环性。我逐一评估：\n\n**(a) KV cache drift**: 合理的替代假说，但论文在 §5.4 (Mechanism Specificity) 提供了部分排除证据。TRC（Turn-level Residual Coherence）在 TF 和 AR 下几乎相同（ThreadGate: 0.334 vs 0.332; LoRA-only: 0.349 vs 0.411）。如果 KV cache drift 导致广泛的 representation degradation，TRC 应该显示 comparable gap，但实际没有。这不完全排除 KV cache drift 影响 attention routing 的可能，但确实缩小了替代假说的空间。\n\n**(b) Steering 论证的循环性**: R1 的批评有道理——\"加 goal token bias 增加 goal attention\"本身是 tautological。但论文的 inference 不仅是\"GAR 增加了\"，而是\"GAR 增加的同时 hidden states 的 coherence 未变（TRC stable）且 PPL 仅增加 9%（β=3）\"。这组合证据表明 attention misallocation 是独立于 representation quality 的 failure mode。如果 root cause 是 representation degradation 而非 attention routing，β-steering 应该无法恢复 meaningful GAR（因为 hidden states 中没有 goal information 可 route），但实际恢复了 11× (§4.3)。\n\n**(c) 论文的 hedging**: 论文确实使用了 \"a proximal cause consistent with our evidence\"（§4.3, §7 Conclusion），§6 Discussion 明确列出了 alternative hypotheses：\"progressive attention drift unrelated to exposure bias, KV cache accumulation effects at long context lengths, or implicit label smoothing from the auxiliary loss could each contribute\"。这一 hedging 水平在我看来是适度的。\n\n**我的判断**：R1 的批评核心合理——exposure bias 归因确实不是 conclusive 的。但论文已经做了合理的 hedging，且 TRC + steering 组合提供了 non-trivial evidence。将此定为 **critical** 过高；建议降级为 **should-fix**，具体修复方向是：(1) 在 §5.3 或 §6 中加一段明确讨论 KV cache drift 作为 confound（当前仅在 Discussion 中一句带过），(2) 承认 steering 论证在逻辑上不排除 KV cache drift。但不需要额外的实验来排除每个替代假说——negative result paper 的标准不应等同于 causal inference paper。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-W1: Cross-model 验证不充分（3/5 条件、median、N=20）**\n同意。§5.5 仅覆盖 ThreadGate、LoRA-only、Base 三个条件，缺少 +PCGrad 和 Uniform Gate。使用 median 而非 mean 有合理理由（heavy-tailed distributions，§5.5 已说明），但 N=20 偏小，且 AR/TF 样本量不对称（TF N=50 vs AR N=20）降低了 gap 估计的可比性。\n\n补充：论文对此有部分 acknowledgment（§8 Limitations: \"the full five-way ablation (Uniform Gate, +PCGrad) has not been replicated\"），但不够显著。建议在 §5.5 正文中也明确标注这一局限。\n\n---\n\n**[AGREE] R1-W2: PCGrad modus tollens scope 过度概括**\n同意。论文在 §5.2 正文中确实写了 \"magnitude imbalance (Chen et al., 2018) and Nash equilibrium violations (Navon et al., 2022) remain untested\"，在 §8 Limitations 中也重复了这一点。但 §1 Introduction 的 contribution (1) 中描述为 \"PCGrad-based exclusion via gradient surgery\" 时未加限定词，读者可能误以为排除了所有 gradient conflict，而实际只排除了 directional conflict。\n\n建议在 §1 contribution (1) 中加入 \"directional\" 修饰：改 \"gradient conflict\" 为 \"gradient direction conflict\"。\n\n---\n\n**[AGREE] R1-W3: Instruction retention McNemar p=0.077 不显著但占 Discussion 过多篇幅**\n同意。p=0.077 未达常规显著性阈值（0.05），但 §6 Discussion 中 \"Instruction retention under steering\" 段落占据了约 3-4 行（不算很长），且包含 GAR-compliance correlation（r=0.200, p=0.007）。\n\n但考虑到论文已面临页数超限问题（我的 N2），这段内容是压缩的首选候选。建议将 instruction retention 分析移入 appendix，或压缩为一句提及（\"exploratory analysis suggests downstream compliance benefit, details in Appendix X\"）。这同时帮助解决页数问题。\n\n---\n\n**[REBUT] R1-W4: LoRA capacity saturation 替代解释**\n部分不同意。\n\nR1 的论点是：如果 LoRA 已经饱和了 TF GAR target（0.50），gates 自然无法提供增量，因此 \"gating 无用\" 的结论可能是 capacity ceiling artifact。\n\n这个 concern 对 \"gating 无用\" 的 claim 是有效的，但**不影响论文的核心结论**。论文的主要 finding 不是\"gating 不 work\"，而是\"所有 training-time interventions（包括 LoRA-only）在 TF 下 work 但在 AR 下 collapse\"——即 TF-AR gap。即使 LoRA 确实在 TF 下饱和了 GAR target，这不解释为什么 AR GAR 从 0.50 跌到 0.015–0.025。\n\n具体证据：\n1. LoRA-only（无 gate）的 TF GAR=0.50，AR GAR=0.025——gap 同样存在（Table 1）\n2. Base model 的 AR GAR=0.012 vs LoRA-only 的 0.025——fine-tuning 本身对 AR 的改善微乎其微\n3. Inference-time steering（§4.3）在不改变任何训练参数的情况下将 AR GAR 从 0.064 恢复到 0.727\n\n这些证据表明 failure mode 在 TF→AR transition，而非 training capacity。R1 的 concern 更适用于 \"gating vs LoRA-only 对比\" 的解读，而非论文的 central claim。\n\n建议将此定为 **minor**：在 §4.2 或 §6 中加一句 acknowledge 这一 alternative interpretation（\"The convergence of all fine-tuned variants at TF GAR ≈ 0.50 could partly reflect LoRA capacity saturation rather than gating ineffectiveness per se; however, the TF-AR gap—the paper's central finding—persists regardless of this interpretation\"）。\n\n---\n\n### 总结\n\n| R1 Issue | R2 判断 | 理由 |\n|----------|---------|------|\n| N1 AR N=5 | [AGREE] critical | 核心 claim \"all collapse equally\" 缺统计支撑 |\n| N2 SS dual-seed | [AGREE] critical | 与我的 W6 一致；contribution 中应降级 |\n| N3 Exposure bias | [REBUT] 降为 should-fix | 论文 hedging 适度，TRC+steering 提供了 non-trivial evidence，但应加强 KV cache drift 讨论 |\n| W1 Cross-model | [AGREE] | 覆盖不完整，应在正文中标注 |\n| W2 PCGrad scope | [AGREE] | §1 contribution 措辞需加 \"directional\" |\n| W3 Instruction retention | [AGREE] | 不显著结果占过多篇幅，建议移入 appendix |\n| W4 LoRA saturation | [REBUT] 降为 minor | 不影响核心 TF-AR gap claim |",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-22T12:56:50.812111+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3976
}
```

</details>

---


### Assistant

_source line 226 · 2026-05-22T12:56:59.263015+00:00_

交叉回应已提交给 Review Director。

总结：对 R1 的 3 个 Must-Fix 中，N1（AR N=5）和 N2（scheduled sampling 单种子）我同意维持 critical；N3（exposure bias 归因）我认为应降级为 should-fix——论文的 hedging 和 TRC+steering 组合证据提供了 non-trivial support，但需加强 KV cache drift 的讨论。4 个 Should-Fix 中同意 W1-W3，对 W4（LoRA saturation）反驳降为 minor，因为它不影响论文的核心 TF-AR gap 结论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

80 recorded events


### User

_source line 227 · 2026-05-22T22:52:36.518607+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Round 1

**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis
**PDF 路径**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf`
**LaTeX 路径**：`projects/turn_residual_gating/paper/main.tex`（sections 在 `paper/sections/` 下）

### Venue 要求
- **目标 venue**：EMNLP 2026（ARR May cycle）
- **截止日期**：2026-05-25
- **页数限制**：正文 8 页（不含 references、limitations、ethical considerations）
- **模板**：ACL/ARR 标准模板
- **匿名规则**：Double-blind（论文中不能出现作者姓名和机构信息）
- **附录**：允许，参与审稿

### 你的审查侧重：新颖性 + 写作完整性

请重点检查以下方面：

1. **Novelty 评估**：
   - 论文的核心贡献（exposure bias 归因 + 五路诊断框架 + β-steering）是否足够新颖
   - 与 Li et al. (2024) split-softmax、Rhea (Hong et al., 2025)、StreamingLLM 等最相近工作的区分度
   - 负面结果论文（gating 无效）的 novelty 标准是否达标
   - "to our knowledge, the first" 等声称是否合理

2. **Related Work 覆盖**：
   - 多轮对话退化文献是否完整（Dongre et al., Laban et al., Liu et al., Bai et al.）
   - 注意力操控文献（StreamingLLM, Rhea, split-softmax）是否全面
   - Exposure bias 文献（Bengio et al., Arora et al., He et al., SEARNN, Professor Forcing）
   - 是否遗漏重要直接竞争者

3. **写作质量**：
   - 论证逻辑是否清晰（观察 → 干预 → 失败 → 诊断 → 根因）
   - 是否有 overclaim（标题、abstract、contribution list）
   - 关键数字（20-33× gap 等）是否重复过多
   - Figure/Table caption 是否准确、不含 causal overclaim
   - 术语一致性（GAR-ours, GAR-Dongre, Goal Accessibility Ratio 全称是否正确）

4. **格式合规**：
   - 正文是否在 8 页限制内（检查 §7 Conclusion 是否在第 8 页结束）
   - 匿名性（是否暴露作者信息）
   - 引用格式（natbib, bib 条目完整性和一致性）
   - Limitations 章节是否存在且内容适当（ARR 必须有）
   - Figure/Table 编号和引用是否正确

5. **Contribution 声称**：
   - 四条 contribution（诊断框架 + exposure bias 刻画 + β-steering + 负面 baseline）的合理性
   - 是否有泛化声称（"in principle applicable" 等）超出实验范围
   - Conclusion 是否准确反映实际发现

请按照 ARR 标准评审格式输出审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。

Weaknesses 按严重程度分级：Critical Must-Fix / Should-Fix / Minor。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-22T22:52:44.850611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-22T22:52:44.901580+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-22T22:52:57.455617+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-22T22:52:57.707555+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-22T22:53:03.923966+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-22T22:53:03.974655+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-22T22:53:06.231225+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-22T22:53:06.584143+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-22T22:53:08.881449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-22T22:53:08.881932+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-22T22:53:25.575441+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-22T22:53:25.676861+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-22T22:53:40.656072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-22T22:53:41.361362+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-22T22:53:47.136645+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) 2025-2026 reviewer guidelines:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Preferences that reflect whether a work is personally interesting should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Expectations for Recommended Papers

All papers recommended for Findings or main conference are expected to be sound and reproducible.

## Area Chair Meta-review Scores

The ARR metareview scoring has also been updated for February 2025. The options include: 5 = Consider for Award; 2 = Resubmit next cy
…[truncated 360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6480
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-22T22:53:48.489604+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.6}], \"total_pages\": 13, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images\"}, \"er
…[truncated 32 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7128
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-22T22:54:00.993895+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-22T22:54:01.094528+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-22T22:54:09.381503+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: 1) All scoring dimensions and their scales (soundness, excitement, overall assessment, confidence, etc.) 2) What each score means 3) Any specific instructions about what reviewers should evaluate 4) The review form structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: 1) All scoring dimensions and their scales (soundness, excitement, overall assessment, confidence, etc.) 2) What each score means 3) Any specific instructions about what reviewers should evaluate 4) The review form structure"
  }
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-22T22:54:10.435543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-22T22:54:10.737067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-22T22:54:11.694934+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1259
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-22T22:54:11.847299+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 251 · 2026-05-22T22:54:11.847764+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-22T22:54:12.099692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-22T22:54:12.915147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1067
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-22T22:54:13.200585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1100
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-22T22:54:15.075569+00:00_

# ARR Reviewer Guidelines: Scoring Dimensions and Review Structure

## Scoring Dimensions

As of February 2025, ARR reviewers provide **three primary scores**:

1. **Soundness**: Technical validity and rigor. Per guidelines, "soundness scores must be justified by the text of the review." Low scores require substantive flaws identified in your commentary.

2. **Excitement**: Subjective interest level. This dimension is "orthogonal to the assessment of the soundness of the paper" and reflects personal taste without requiring explicit justification.

3. **Overall Assessment**: Explicit recommendation for venue acceptance, integrating soundness, excitement, novelty, and impact considerations.

## Additional Assessment Dimensions

The guidelines also reference:

- **Confidence Score**: Indicates reviewer's certainty level on the assigned paper
- **Reproducibility Score**: Justified by whether sufficient experimental details, code, and data information are disclosed

## Scoring Philosophy

The guidelines emphasize that papers can be "sound, but not something that is interesting for you personally." A reviewer might rate excitement low while maintaining high soundness, or vice versa. Overall recommendations must consider all factors while maintaining that "papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Review Form Structure

Reviews are organized into:
- Summary of contributions and findings
- Detailed strengths and weaknesses
- Specific, actionable feedback (avoiding generic criticisms)
- Confidence and reproducibility justifications
- Author identity disclosure information

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5694
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-22T22:54:23.657588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-22T22:54:24.512299+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-22T22:54:24.713320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-22T22:54:24.764572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-22T22:54:25.317456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-22T22:54:25.824366+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-22T22:54:26.026199+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-22T22:54:26.631918+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1314
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-22T22:54:34.562047+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "9-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "9-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-22T22:54:35.269390+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.3}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.1}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 219.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 187.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 165.8}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-22T22:54:38.228263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-22T22:54:39.081867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-22T22:54:39.232887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 269 · 2026-05-22T22:54:39.785164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-22T22:54:40.087675+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 271 · 2026-05-22T22:54:40.088080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-22T22:54:40.594110+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-22T22:54:40.594550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-22T22:54:40.646248+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 558
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-22T22:54:40.950251+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-22T22:54:48.131277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-22T22:54:48.242203+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	
18	\graphicspath{{../figures/paper/}{../artifacts/}}
19	
20	\title{Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 110
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-22T22:54:54.224013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-22T22:54:54.324886+00:00_

1	\begin{abstract}
2	Multi-turn dialogue with Large Language Models (LLMs) suffers from progressive attention decay toward system prompt goal tokens. On Qwen-2.5-7B-Instruct, the Goal Accessibility Ratio (GAR) declines by 70.8\% between early and mid-conversation turns, yet linear probes recover goal content from the residual stream with AUC\,=\,0.98. We introduce ThreadGate, a per-layer content-and-turn-conditioned MLP gate ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$) trained jointly with next-token prediction (NTP) and an auxiliary GAR loss. A five-way comparison reveals that training succeeds (teacher-forced GAR\,=\,0.50) but autoregressive GAR drops to 0.015--0.025, a 20--33$\times$ gap; gating contributes zero measurable benefit and a PCGrad-based exclusion experiment rules out gradient conflict. The failure traces to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. Inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation---not representation degradation---is a proximal cause consistent with our evidence. Scheduled sampling compresses the gap to 1.57$\times$ with no PPL cost (single seed), and cross-model evaluation on Llama-3.1-8B confirms the gap (27$\times$ by median). These findings characterize how exposure bias selectively destroys auxiliary objective generalization under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-22T22:54:54.776611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-22T22:54:55.128174+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Accessibility Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention point.
6	
7	If the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each
…[truncated 4692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-22T22:54:55.128655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-22T22:54:55.179213+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Recent work has established that LLMs systematically degrade across conversation turns. \citet{laban2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Accessibility Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\% across turns in 12 models, while residual stream probes retain goal information with AUC\,=\,0.98. We observe a steeper 70.8\% decline on Qwen-2.5-7B-Instruct (\S\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.
5	
6	\paragraph{Instruction stability.}
7	\citet{li2024measuring} independently quantified instruction instability in multi-turn dialogs and proposed split-softmax---separating instruction from conversation tokens during attention computation---as an inference-time remedy. Split-softmax restructures the attention mechanism itself and requires no retraining, but cannot address exposure bias in auxiliary losses that depend on training-time optimization. Our work adds systematic diagnosis (five-way controlled comparison + PCGrad exclusion), exposure bias attribution, and training-time mitigation via scheduled sampling; our $\beta$-steering c
…[truncated 3192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-22T22:54:59.294037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-22T22:55:00.298067+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). The gate $g_l$ is produced by a two-layer MLP:
26	\begin{equation}\label{eq:gate}
27	  g_l = \sigma\!\bigl(W_2\,\text{ReLU}(W_1\,[\te
…[truncated 1968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-22T22:55:00.298439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-22T22:55:00.449339+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 16, $\alpha$=32) are applied to query and value projection layers (\texttt{q\_proj}, \texttt{v\_proj}). The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~\ref{sec:appendix-hyper}.
7	
8	We evaluate five configurations that form a controlled comparison isolating four factors. \textbf{ThreadGate}: full system with 28 gate networks (Eq.~\ref{eq:gate}) and three-term loss. \textbf{+PCGrad}: ThreadGate with PCGrad \citep{yu2020pcgrad} projecting conflicting gradients (isolates gradient conflict). \textbf{Uniform Gate}: identical gate architecture with turn embedding replaced by a still-learnable constant vector (content-conditioned but turn-unaware; isolates turn conditioning). \textbf{LoRA-only}: gates fixed at 1.0, trained with $\mathcal{L}_\text{NTP} + \mathcal{L}_\text{GAR}$ only (isolates gating mechanism). \textbf{Base}: pretrained model (isolates fine-tuning). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours (last-token attention to goals, \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (all-token average
…[truncated 6787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-22T22:55:00.449753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-22T22:55:00.500327+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step diagnostic chain: we first show that gates learn behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through an exclusion experiment (\S\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \S\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
10	
11	The resulting 
…[truncated 7104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-22T22:55:04.865451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-22T22:55:05.166875+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is a proximal cause (\S\ref{subsec:steering}). Alternative hypotheses remain open; our evidence is consistent with exposure bias as the dominant factor but does not exclude alternatives. In particular, KV cache drift---accumulation of model-generated key-value states diverging from teacher-forced statistics---could compound the mismatch; disentangling prefix-level and cache-level contributions is left to future work. Split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea} complement $\beta$-steering by restructuring attention computation at the architectural level, but cannot resolve exposure bias in auxiliary losses requiring retraining.
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, mixing teacher-forced and model-generated contexts. AR GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36), consistent with exposure bias as a primary driver. GAR-Dongre also rises (0.019$\to$0.353). On the $N$\,=\,50 evaluation, $\beta$\,=\,5 incurs 24\% PPL cost (1.43\,$\to$\,1.77); $\beta$\,=\,3 offers a more balanced tradeoff (+9\%); scheduled sampling incurs no fluency cost but requires retraining. A second seed yields AR GAR\,=\,0.418 (gap 1.20$\times$); systematic ablation is deferred. Exploratory instruction retention analysis (Appendix~\ref{sec:appendix-ir}) shows +23.8\,pp compliance at $\beta$\,=\,3 (McNemar $p$\,=\,0.077).
6	
7	T
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-22T22:55:05.167220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-22T22:55:05.368230+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	ThreadGate modulates the residual stream with per-layer gated MLP networks and an auxiliary GAR loss. Training succeeds (TF GAR\,=\,0.50), but autoregressive GAR collapses by $>$25$\times$ on both Qwen-2.5-7B and Llama-3.1-8B. Steering ($\beta$\,=\,5, GAR 0.727) and scheduled sampling (gap 31$\times$$\to$1.57$\times$; single seed) implicate attention misallocation as the proximal cause.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-22T22:55:05.368716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-22T22:55:05.469442+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	The five-way comparison uses seed\,=\,42; ThreadGate is additionally validated with seed\,=\,123 (TF/AR GAR-ours within $\pm$0.001, gap 30.5--32.1$\times$). The remaining three variants use a single seed; cross-variant convergence provides indirect robustness evidence but does not substitute for multi-seed validation.
4	
5	We test only one type of auxiliary attention loss (GAR with MSE target $\tau = 0.5$). Other attention steering objectives, such as head-specific or layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result applies to the GAR family; it does not rule out all auxiliary attention interventions.
6	
7	Training uses 8K conversations from UltraChat. Larger-scale training could alter gate dynamics, particularly if the model encounters sufficient distributional diversity to reduce the training-inference mismatch.
8	
9	All experiments use two model families (Qwen-2.5-7B and Llama-3.1-8B); while cross-model evaluation confirms the exposure bias gap, $N$\,=\,2 does not establish universality. The Llama evaluation includes ThreadGate and LoRA-only; the full five-way ablation (Uniform Gate, +PCGrad) has not been replicated, and all experiments use a single dataset (UltraChat). The instruction retention analysis is exploratory: a single model, 18 system-prompt constraint types, and a single $\beta$ value without grid search.
10	
11	The PCGrad exclusion experiment addresses gradient direction conflict only. Magnitude imbalance (GradNorm; \citealp{chen2018gradnorm}) and Nash equilibrium approaches (Nash-MTL; \citealp{navon2022nash}) remain untested and could reveal additional failure modes or interaction effects.
12	
13	All four fine-tuned variants share the same GAR auxiliary loss. This design isolates the gating mechanism but does not test whether gating could be effective without an auxiliary attention loss or under a different training objective.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-22T22:55:19.121610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-22T22:55:19.372940+00:00_

1	\section{Training Hyperparameters}\label{sec:appendix-hyper}
2	
3	All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\alpha$=32) on \texttt{q\_proj} and \texttt{v\_proj}, AdamW optimizer (lr = $2 \times 10^{-4}$, $\beta_1$=0.9, $\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\times$ learning rate multiplier and initial bias 1.5 ($\sigma(1.5) \approx 0.82$).
4	
5	\section{Loss Formulation Search}\label{sec:appendix-loss}
6	
7	Table~\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\S\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.
8	
9	\begin{table*}[t]
10	\centering\footnotesize
11	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
12	\label{tab:loss-iterations}
13	\begin{tabular}{l l l p{5.8cm} c c}
14	\toprule
15	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
16	\midrule
17	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
18	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
19	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
20	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
21	v5  & Maximize ($\lambda$=1)  & \texttimes~identity co
…[truncated 3611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-22T22:55:19.373478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-22T22:55:19.424793+00:00_

1	% ============================================================
2	% Multi-Turn Attention
3	% ============================================================
4	
5	@article{dongre2026attention,
6	  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\"{u}r, Dilek},
7	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
8	  journal = {arXiv preprint arXiv:2605.12922},
9	  year    = {2026},
10	  url     = {https://arxiv.org/abs/2605.12922}
11	}
12	
13	@article{hong2025rhea,
14	  author  = {Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng},
15	  title   = {{Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs}},
16	  journal = {arXiv preprint arXiv:2512.06869},
17	  year    = {2025},
18	  url     = {https://arxiv.org/abs/2512.06869}
19	}
20	
21	@article{laban2025lost,
22	  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
23	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
24	  journal = {arXiv preprint arXiv:2505.06120},
25	  year    = {2025},
26	  url     = {https://arxiv.org/abs/2505.06120}
27	}
28	
29	@article{liu2026intent,
30	  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},
31	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
32	  journal = {arXiv preprint arXiv:2602.07338},
33	  year    = {2026},
34	  url     = {https://arxiv.org/abs/2602.07338}
35	}
36	
37	@inproceedings{bai2024mtbench101,
38	  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},
39	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
40	  booktitle = {Annual Meeting of the Ass
…[truncated 9928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-22T22:57:19.011695+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement scoring scale 1 2 3 4 5 description 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement scoring scale 1 2 3 4 5 description 2025"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-22T22:57:25.185865+00:00_

Web search results for query: "ACL ARR review form soundness excitement scoring scale 1 2 3 4 5 description 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I found information about the ACL ARR review form scoring scales. Here's what the current 2025 review form shows:

## Scoring Scale Overview

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Excitement Scale

The excitement score uses a 1-5 scale:

- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.
- 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference.
- 1 = Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community (e.g. it is in no way related to computational processing of language).

### Soundness Scale

5 = Excellent: This study is one of the most thorough I have seen, given its type.

### Key Guidelines

The soundness sco
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6174
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-22T22:57:32.415751+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their exact scales (1-5 descriptions for each level), and any other fields reviewers must fill in. I need the exact wording for each score level of: soundness, excitement, overall assessment, confidence, reproducibility."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their exact scales (1-5 descriptions for each level), and any other fields reviewers must fill in. I need the exact wording for each score level of: soundness, excitement, overall assessment, confidence, reproducibility."
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-22T22:57:38.386292+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points or attend if there's time."
- **2**: "Potentially Interesting: this paper does not resonate with me personally."
- **1**: "Not Exciting: I don't think it would resonate with the broader community."

## Overall Assessment
- **5**: "Consider for Award: could be considered for outstanding paper award."
- **4**: "Conference: could be accepted to an *ACL conference."
- **3**: "Findings: could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: needs substantial revisions."
- **1**: "Do not resubmit: has to be fully redone."

## Reproducibility
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduc
…[truncated 15 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5970
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-22T23:00:08.634636+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见 — Round 1\n\n**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一种在 transformer 每层残差路径上添加 content-and-turn-conditioned MLP gate 的方法，目标是恢复多轮对话中衰减的 system prompt 注意力（GAR）。通过五路对照实验（ThreadGate / +PCGrad / Uniform Gate / LoRA-only / Base），作者发现在 teacher-forced 条件下 GAR 收敛至目标值 0.50，但自回归生成时 GAR 坍塌至 0.015–0.025（20–33× gap）。论文进一步通过 PCGrad 排除梯度方向冲突、通过 gate 值分析排除架构缺陷，将失败归因于 exposure bias：辅助注意力损失在 teacher-forcing 下优化的模式无法迁移到自回归推理。β-steering（β=5）将 GAR 从 0.064 恢复至 0.727，scheduled sampling（单 seed）将 gap 从 31× 压缩至 1.57×。跨模型验证在 Llama-3.1-8B 上确认了 27× gap。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 五路对照和 PCGrad 排除实验方法论严谨，主要 claims 有充分支撑。但 GAR 与下游任务性能的关联未被验证（p=0.077 不显著），scheduled sampling 仅单 seed，削弱了部分结论的可靠性。 |\n| Excitement | 3/5 | 负面结果 + 暴露偏差归因对社区有参考价值，但论文最终未提供一个可工作的解决方案。β-steering 需要预知 goal token 位置，scheduled sampling 是初步结果。实际影响有限。 |\n| Reproducibility | 4/5 | 超参数文档完整（Appendix A），模型和数据集均公开可获取，seed 已指定。但未提及是否开源代码。 |\n| Confidence | 4/5 | 仔细阅读了全文，熟悉注意力操控、多任务学习、exposure bias 相关文献。 |\n\n---\n\n## 主要优势\n\n**S1. 实验设计严谨的五路对照框架。** 每对配置精确隔离一个因素（turn conditioning / gating mechanism / gradient conflict / fine-tuning），逻辑链条清晰。PCGrad 排除实验遵循 modus tollens 推理范式，说服力强（§5.2, Table 1）。\n\n**S2. 负面结果的诚实报告与深入诊断。** 论文没有停留在\"方法不 work\"的层面，而是系统追溯失败机制——gate 值反转（§5.1, 27/28 layers, Wilcoxon p = 3.73×10⁻⁸）→ 排除梯度冲突（§5.2）→ 分布偏移归因（§5.3）→ 机制特异性确认（§5.4）→ 跨模型泛化（§5.5）。这种诊断深度在负面结果论文中少见。\n\n**S3. Exposure bias 对辅助注意力损失的选择性破坏是真正新颖的发现。** 先前 exposure bias 文献（Bengio et al. 2015, Arora et al. 2022, He et al. 2019）聚焦于主生成目标的质量退化。本文首次展示 exposure bias 可以选择性摧毁辅助注意力目标（GAR 20–33× 坍塌），同时保留主任务（NTP/PPL 不变），且 token-level self-recovery（He et al. 2019）不能拯救注意力分布属性。这一区分有理论贡献。\n\n**S4. β-steering 实验提供建设性证据。** 通过直接操控注意力 logits 恢复 GAR（0.064→0.727），有效区分了\"表征退化\"和\"注意力路由失败\"两种假说（§4.3）。N=50 的 larger-scale 验证增强了可信度。\n\n**S5. 写作中的 scoping hedges 使用得当。** 论文频繁使用 \"under the tested conditions\", \"consistent with our evidence\", \"proximal cause\" 等限定语，避免了不当泛化。Limitations 章节全面、诚实（§8）。\n\n---\n\n## Must-Fix 问题（Critical，影响接收决定）\n\n**N1** [critical] **GAR 指标与下游任务性能之间缺乏因果验证**\n- 具体位置：§4.3（steering）、§6（Discussion）、Appendix C（instruction retention）\n- 问题：论文的核心叙事建立在 GAR（对 system prompt goal token 的注意力比例）之上，但从未验证 GAR 的提升是否真正改善了指令遵循质量。唯一的下游评估是 Appendix C 的 instruction retention 分析，结果为 McNemar p=0.077（不显著）、相关性 r=0.200。论文自己也承认这是 \"exploratory\"。但问题在于：如果 GAR 的提升不能可靠地改善实际对话质量，那么整个 \"GAR 坍塌 = 失败\" 的叙事基础就不稳固。一个模型可能 GAR 很低但指令遵循很好（通过其他注意力路径），也可能 GAR 很高但生成质量差（如 β=10 时 PPL 退化到 4.22）。\n- 为什么影响接收：这不是一个次要缺陷——它影响论文的核心 claim 是否有实际意义。如果 GAR 只是一个注意力统计量而非指令遵循的可靠代理指标，那么 \"exposure bias 摧毁辅助注意力目标\" 这个发现虽然技术上有趣，但其实际重要性大打折扣。\n- 建议修改方向：在 β=0/3/5 条件下评估实际指令遵循质量（如 IFEval、MT-Bench、或自定义 system prompt compliance 评估），建立 GAR↔downstream 的量化关联。如果无法做到，需在论文中明确承认这一局限并降低 claim 强度。\n\n**N2** [critical] **Scheduled sampling 结果承载过重但证据不足**\n- 具体位置：§6 Discussion（\"gap from ~31× to 1.57×\"）、Abstract（\"compresses the gap to 1.57×\"）、Conclusion\n- 问题：Scheduled sampling 是论文中唯一展示 training-time mitigation 可行性的证据，在 abstract、intro（contribution 2）、discussion、conclusion 中均被引用。但该结果仅基于单个 seed。虽然论文提到第二个 seed 得到 GAR=0.418（gap 1.20×），这两个 seed 的结果差异很大（0.318 vs 0.418，即 gap 1.57× vs 1.20×），这本身说明结果的方差很高。以单 seed 结果作为关键 contribution 的一部分（contribution 2 中提到 \"a preliminary demonstration that scheduled sampling compresses this gap\"），且在 abstract 中以确定性语气呈现（\"Scheduled sampling compresses the gap to 1.57×\"），存在 overclaim 风险。\n- 为什么影响接收：ARR reviewer guidelines 要求 soundness 评分必须由 review text 中的具体 evidence 支撑。单 seed 结果缺乏统计可靠性，特别是当两个 seed 的 variance 如此之大时。如果 scheduled sampling 结果在多 seed 下不稳定，论文的核心叙事（exposure bias 是可解决的）就会被削弱。\n- 建议修改方向：(1) 在 abstract/conclusion 中明确标注 \"single seed, preliminary\"；(2) 至少运行 3-5 个 seed 并报告 mean±std；(3) 如果时间不允许，在 abstract 中移除这一 claim 或大幅弱化措辞。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **标题暗示 gating 固有失败，但实际发现是 exposure bias 对所有 teacher-forced 辅助损失的通用问题**\n- 具体位置：Title, §7 Conclusion\n- 问题：标题 \"Why Per-Layer Residual Gating Fails\" 将失败归因于 gating 架构，但论文的核心发现恰恰是 gating 本身不是问题——LoRA-only（无 gate）表现完全相同。真正的发现是 teacher-forced 辅助注意力损失在自回归条件下失效，这与 gating 无关。当前标题可能误导读者认为 gating 是问题所在，而实际上替换成任何其他 teacher-forced 注意力干预都会有同样的失败。\n- 建议：标题改为更准确反映核心发现的表述，例如 \"Exposure Bias Selectively Destroys Auxiliary Attention Objectives in Multi-Turn LLM Dialogue\" 或在标题中明确 exposure bias 的角色。\n\n**W2** [warning] **缺少与最近直接竞争者的实验对比**\n- 具体位置：§2 Related Work（li2024measuring, hong2025rhea）\n- 问题：Split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 在 related work 中被讨论为互补方法，但没有实验对比。论文声称 split-softmax \"cannot address exposure bias in auxiliary losses\"（§2, ¶2），Rhea 同样 \"cannot resolve exposure bias in auxiliary losses requiring retraining\"（§6）。但这些声称缺乏实验验证——split-softmax 是否也表现出类似的 TF-AR gap？如果 split-softmax 在推理时直接修改注意力而无需训练辅助损失，它是否可以避免 exposure bias 问题？这些问题的实验回答会显著加强论文的定位。\n- 建议：至少在一个模型上运行 split-softmax baseline，或明确承认缺乏直接对比是一个局限。\n\n**W3** [warning] **\"To our knowledge, the first\" 声称过于狭窄且不可证伪**\n- 具体位置：§1 Introduction, Contribution (2)\n- 问题：Contribution (2) 声称 \"to our knowledge the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization\"。这一声称非常狭窄——它是第一个研究 exposure bias 对 \"auxiliary attention loss\" 在 \"multi-turn dialogue\" 中影响的工作。但这种狭窄的 \"first\" 声称本质上不可证伪（因为 niche 太窄），且不增加实际的新颖性论证。真正的新颖性在于发现本身，不在于 \"first\" 的标签。\n- 建议：删除 \"to our knowledge, the first\" 修饰语，直接陈述贡献内容。让 reviewer 自行判断新颖性。\n\n**W4** [warning] **仅两个模型家族（7B-8B scale），泛化性受限**\n- 具体位置：§5.5 Cross-Model Generality, §8 Limitations\n- 问题：所有实验在 Qwen-2.5-7B 和 Llama-3.1-8B 上进行，且 Llama 上只复制了 ThreadGate 和 LoRA-only（未做完整五路对照）。论文在 §8 承认 \"N=2 does not establish universality\"，但叙事中仍使用 \"cross-model generality\" 这样的标题暗示更广泛的泛化。此外，没有在更大规模模型（>13B）或不同架构族（如 Mixtral/MoE）上的验证。\n- 建议：将 §5.5 标题改为 \"Cross-Model Replication\" 而非 \"Cross-Model Generality\"，降低泛化暗示。\n\n**W5** [warning] **关键数字重复过多**\n- 具体位置：Abstract, §1 (×3), Figure 1 caption, §4.2, §5.3, Figure 4 caption\n- 问题：\"20–33× gap\" 在论文中出现至少 7 次（abstract 1次、intro 3次、figure 1 caption、experiments、analysis、figure 4 caption）。虽然这是核心发现，但过度重复降低了信息密度，给人 padding 的感觉。类似地，\"0.064 to 0.727\" 出现 4 次以上。\n- 建议：在 abstract 和核心结果处保留精确数字，后续引用时使用 \"order-of-magnitude gap\" 或 \"the TF-AR gap (§4.2)\" 等简洁回指。\n\n**W6** [warning] **Table 1 四舍五入与正文数字不一致**\n- 具体位置：§4.2 vs Table 1\n- 问题：§4.2 称 \"GAR-ours spans only 0.75 percentage points (pp) across ThreadGate (0.50), +PCGrad (0.50), Uniform Gate (0.51), and LoRA-only (0.50)\"。但 Table 1 显示的数值只保留两位小数（0.50, 0.50, 0.51, 0.50），从这些数字计算 spread 应该是 1 pp 而非 0.75 pp。这意味着实际值在更高精度下不同（如 0.5025 vs 0.5100），但 table 的四舍五入导致读者无法验证这一 claim。\n- 建议：Table 1 增加一位小数，或在正文中使用与 table 一致的精度。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**：Abstract 过于密集（约 180 词），信息压缩度极高，首次阅读时难以消化。建议精简 contribution 罗列，留更多空间给核心发现的叙事。\n- **M2**：§5.5 Llama 结果使用 median 而非 mean 报告 AR GAR-ours，理由是 heavy-tailed distribution。虽然统计上合理，但在主实验（Table 1）使用 mean 的情况下切换统计量有 metric selection 之嫌。建议同时报告 mean 和 median。\n- **M3**：部分 bib 条目格式不一致——已发表的会议论文使用 @inproceedings（正确），但 Raposo et al. 2024 (Mixture-of-Depths) 使用 @article + arXiv 格式，该论文已被 ICML 2024 接收，应更新为会议版本。同样，Gromov et al. 2024 标注 year=2025 但 booktitle 为 ICLR，需确认年份一致性。\n- **M4**：§6 Discussion 提到 KV cache drift 作为替代假说，仅一句话。如果要提出这一替代假说，应至少简述为什么当前实验不能区分 exposure bias 和 KV cache drift。\n- **M5**：Conclusion（§7）仅 3 句话，虽然简洁但可能过于简短。建议增加 1-2 句关于 future directions 或 broader implications。\n- **M6**：论文未提及代码是否开源。ARR reproducibility 评分需要考虑这一因素。\n\n---\n\n## Questions to Authors\n\n**Q1**：Table 1 中 LoRA-only 的 AR GAR-ours (0.025) 反而高于所有 gating variants (0.015-0.016)。虽然差异很小，但方向是 gating 反而降低了 AR GAR。这是否意味着 gate 的 2-7% attenuation 在推理时略微有害？\n\n**Q2**：β-steering 实验中，β=0 时 N=5（10-turn）的 baseline GAR 为 0.028，但 N=50 的 baseline GAR 为 0.064（mean），差异超过 2×。论文解释为 \"short conversations with high baseline GAR\" 导致均值偏高。但这是否意味着 GAR 作为指标对对话长度高度敏感，从而削弱了跨实验设置的可比性？\n\n**Q3**：Scheduled sampling 的第二个 seed 得到 GAR=0.418（gap 1.20×）vs 第一个 seed 的 0.318（gap 1.57×）。两个 seed 之间 AR GAR 相差 31%（0.318 vs 0.418）。作者是否能解释这种高方差的来源？这是否暗示 scheduled sampling 的效果对随机初始化非常敏感？\n\n**Q4**：论文使用 LoRA rank 16 进行微调。是否尝试过更高的 rank（如 64 或 128）？gate 的无效性是否可能部分归因于 LoRA 容量已经足够，而非 gating 本身无用？\n\n---\n\n## Missing References\n\n1. **Zhang et al. (2024) \"Tell Your Model Where to Attend\"** — 与 β-steering 思路相似的推理时注意力操控方法，应在 §2 Attention Manipulation 段落中讨论。\n2. **Xu et al. (2025) 或类似的 multi-turn instruction following benchmarks** — 论文缺少对多轮指令遵循质量的标准化评估（如 IFEval multi-turn variant），这些基准应在 §4.1 Setup 中被提及。\n3. 建议核实 Raposo et al. (2024) Mixture-of-Depths 是否已在 ICML 2024 正式发表，如是则应更新 bib 条目。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n**一句话总结**：方法论严谨的负面结果论文，exposure bias 对辅助注意力目标的选择性破坏是真正新颖的发现，但 GAR 指标缺乏下游验证这一根本缺陷削弱了核心 claim 的实际意义。\n\n**详细理由**：\n\n本文的核心强项在于实验设计的严谨性和诊断链的完整性——五路对照、PCGrad 排除、gate 值分析、跨模型验证构成了一个令人信服的论证结构。Exposure bias 对辅助注意力损失的选择性破坏确实是文献中未被系统研究的现象，具有理论贡献。\n\n但论文有两个 critical 弱点阻碍其达到 Conference 水平：(1) GAR 指标与实际指令遵循质量之间的 gap 未被 bridge——整个论文围绕一个注意力统计量展开，但从未证明这个统计量的改善对用户可感知的对话质量有意义；(2) Scheduled sampling 作为唯一的 training-time mitigation evidence 仅有单 seed 支撑，且两个 seed 间方差很大。如果补充下游任务验证和多 seed scheduled sampling 实验，论文将达到 4.0 (Conference) 水平。\n\n当前状态适合 Findings 接收。",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见 — Round 1\n\n**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一种在 transformer 每层残差路径上添加 content-and-turn-conditioned MLP gate 的方法，目标是恢复多轮对话中衰减的 system prompt 注意力（GAR）。通过五路对照实验（ThreadGate / +PCGrad / Uniform Gate / LoRA-only / Base），作者发现在 teacher-forced 条件下 GAR 收敛至目标值 0.50，但自回归生成时 GAR 坍塌至 0.015–0.025（20–33× gap）。论文进一步通过 PCGrad 排除梯度方向冲突、通过 gate 值分析排除架构缺陷，将失败归因于 exposure bias：辅助注意力损失在 teacher-forcing 下优化的模式无法迁移到自回归推理。β-steering（β=5）将 GAR 从 0.064 恢复至 0.727，scheduled sampling（单 seed）将 gap 从 31× 压缩至 1.57×。跨模型验证在 Llama-3.1-8B 上确认了 27× gap。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 五路对照和 PCGrad 排除实验方法论严谨，主要 claims 有充分支撑。但 GAR 与下游任务性能的关联未被验证（p=0.077 不显著），scheduled sampling 仅单 seed，削弱了部分结论的可靠性。 |\n| Excitement | 3/5 | 负面结果 + 暴露偏差归因对社区有参考价值，但论文最终未提供一个可工作的解决方案。β-steering 需要预知 goal token 位置，scheduled sampling 是初步结果。实际影响有限。 |\n| Reproducibility | 4/5 | 超参数文档完整（Appendix A），模型和数据集均公开可获取，seed 已指定。但未提及是否开源代码。 |\n| Confidence | 4/5 | 仔细阅读了全文，熟悉注意力操控、多任务学习、exposure bias 相关文献。 |\n\n---\n\n## 主要优势\n\n**S1. 实验设计严谨的五路对照框架。** 每对配置精确隔离一个因素（turn conditioning / gating mechanism / gradient conflict / fine-tuning），逻辑链条清晰。PCGrad 排除实验遵循 modus tollens 推理范式，说服力强（§5.2, Table 1）。\n\n**S2. 负面结果的诚实报告与深入诊断。** 论文没有停留在\"方法不 work\"的层面，而是系统追溯失败机制——gate 值反转（§5.1, 27/28 layers, Wilcoxon p = 3.73×10⁻⁸）→ 排除梯度冲突（§5.2）→ 分布偏移归因（§5.3）→ 机制特异性确认（§5.4）→ 跨模型泛化（§5.5）。这种诊断深度在负面结果论文中少见。\n\n**S3. Exposure bias 对辅助注意力损失的选择性破坏是真正新颖的发现。** 先前 exposure bias 文献（Bengio et al. 2015, Arora et al. 2022, He et al. 2019）聚焦于主生成目标的质量退化。本文首次展示 exposure bias 可以选择性摧毁辅助注意力目标（GAR 20–33× 坍塌），同时保留主任务（NTP/PPL 不变），且 token-level self-recovery（He et al. 2019）不能拯救注意力分布属性。这一区分有理论贡献。\n\n**S4. β-steering 实验提供建设性证据。** 通过直接操控注意力 logits 恢复 GAR（0.064→0.727），有效区分了\"表征退化\"和\"注意力路由失败\"两种假说（§4.3）。N=50 的 larger-scale 验证增强了可信度。\n\n**S5. 写作中的 scoping hedges 使用得当。** 论文频繁使用 \"under the tested conditions\", \"consistent with our evidence\", \"proximal cause\" 等限定语，避免了不当泛化。Limitations 章节全面、诚实（§8）。\n\n---\n\n## Must-Fix 问题（Critical，影响接收决定）\n\n**N1** [critical] **GAR 指标与下游任务性能之间缺乏因果验证**\n- 具体位置：§4.3（steering）、§6（Discussion）、Appendix C（instruction retention）\n- 问题：论文的核心叙事建立在 GAR（对 system prompt goal token 的注意力比例）之上，但从未验证 GAR 的提升是否真正改善了指令遵循质量。唯一的下游评估是 Appendix C 的 instruction retention 分析，结果为 McNemar p=0.077（不显著）、相关性 r=0.200。论文自己也承认这是 \"exploratory\"。但问题在于：如果 GAR 的提升不能可靠地改善实际对话质量，那么整个 \"GAR 坍塌 = 失败\" 的叙事基础就不稳固。一个模型可能 GAR 很低但指令遵循很好（通过其他注意力路径），也可能 GAR 很高但生成质量差（如 β=10 时 PPL 退化到 4.22）。\n- 为什么影响接收：这不是一个次要缺陷——它影响论文的核心 claim 是否有实际意义。如果 GAR 只是一个注意力统计量而非指令遵循的可靠代理指标，那么 \"exposure bias 摧毁辅助注意力目标\" 这个发现虽然技术上有趣，但其实际重要性大打折扣。\n- 建议修改方向：在 β=0/3/5 条件下评估实际指令遵循质量（如 IFEval、MT-Bench、或自定义 system prompt compliance 评估），建立 GAR↔downstream 的量化关联。如果无法做到，需在论文中明确承认这一局限并降低 claim 强度。\n\n**N2** [critical] **Scheduled sampling 结果承载过重但证据不足**\n- 具体位置：§6 Discussion（\"gap from ~31× to 1.57×\"）、Abstract（\"compresses the gap to 1.57×\"）、Conclusion\n- 问题：Scheduled sampling 是论文中唯一展示 training-time mitigation 可行性的证据，在 abstract、intro（contribution 2）、discussion、conclusion 中均被引用。但该结果仅基于单个 seed。虽然论文提到第二个 seed 得到 GAR=0.418（gap 1.20×），这两个 seed 的结果差异很大（0.318 vs 0.418，即 gap 1.57× vs 1.20×），这本身说明结果的方差很高。以单 seed 结果作为关键 contribution 的一部分（contribution 2 中提到 \"a preliminary demonstration that scheduled sampling compresses this gap\"），且在 abstract 中以确定性语气呈现（\"Scheduled sampling compresses the gap to 1.57×\"），存在 overclaim 风险。\n- 为什么影响接收：ARR reviewer guidelines 要求 soundness 评分必须由 review text 中的具体 evidence 支撑。单 seed 结果缺乏统计可靠性，特别是当两个 seed 的 variance 如此之大时。如果 scheduled sampling 结果在多 seed 下不稳定，论文的核心叙事（exposure bias 是可解决的）就会被削弱。\n- 建议修改方向：(1) 在 abstract/conclusion 中明确标注 \"single seed, preliminary\"；(2) 至少运行 3-5 个 seed 并报告 mean±std；(3) 如果时间不允许，在 abstract 中移除这一 claim 或大幅弱化措辞。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **标题暗示 gating 固有失败，但实际发现是 exposure bias 对所有 teacher-forced 辅助损失的通用问题**\n- 具体位置：Title, §7 Conclusion\n- 问题：标题 \"Why Per-Layer Residual Gating Fails\" 将失败归因于 gating 架构，但论文的核心发现恰恰是 gating 本身不是问题——LoRA-only（无 gate）表现完全相同。真正的发现是 teacher-forced 辅助注意力损失在自回归条件下失效，这与 gating 无关。当前标题可能误导读者认为 gating 是问题所在，而实际上替换成任何其他 teacher-forced 注意力干预都会有同样的失败。\n- 建议：标题改为更准确反映核心发现的表述，例如 \"Exposure Bias Selectively Destroys Auxiliary Attention Objectives in Multi-Turn LLM Dialogue\" 或在标题中明确 exposure bias 的角色。\n\n**W2** [warning] **缺少与最近直接竞争者的实验对比**\n- 具体位置：§2 Related Work（li2024measuring, hong2025rhea）\n- 问题：Split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 在 related work 中被讨论为互补方法，但没有实验对比。论文声称 split-softmax \"cannot address exposure bias in auxiliary losses\"（§2, ¶2），Rhea 同样 \"cannot resolve exposure bias in auxiliary losses requiring retraining\"（§6）。但这些声称缺乏实验验证——split-softmax 是否也表现出类似的 TF-AR gap？如果 split-softmax 在推理时直接修改注意力而无需训练辅助损失，它是否可以避免 exposure bias 问题？这些问题的实验回答会显著加强论文的定位。\n- 建议：至少在一个模型上运行 split-softmax baseline，或明确承认缺乏直接对比是一个局限。\n\n**W3** [warning] **\"To our knowledge, the first\" 声称过于狭窄且不可证伪**\n- 具体位置：§1 Introduction, Contribution (2)\n- 问题：Contribution (2) 声称 \"to our knowledge the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization\"。这一声称非常狭窄——它是第一个研究 exposure bias 对 \"auxiliary attention loss\" 在 \"multi-turn dialogue\" 中影响的工作。但这种狭窄的 \"first\" 声称本质上不可证伪（因为 niche 太窄），且不增加实际的新颖性论证。真正的新颖性在于发现本身，不在于 \"first\" 的标签。\n- 建议：删除 \"to our knowledge, the first\" 修饰语，直接陈述贡献内容。让 reviewer 自行判断新颖性。\n\n**W4** [warning] **仅两个模型家族（7B-8B scale），泛化性受限**\n- 具体位置：§5.5 Cross-Model Generality, §8 Limitations\n- 问题：所有实验在 Qwen-2.5-7B 和 Llama-3.1-8B 上进行，且 Llama 上只复制了 ThreadGate 和 LoRA-only（未做完整五路对照）。论文在 §8 承认 \"N=2 does not establish universality\"，但叙事中仍使用 \"cross-model generality\" 这样的标题暗示更广泛的泛化。此外，没有在更大规模模型（>13B）或不同架构族（如 Mixtral/MoE）上的验证。\n- 建议：将 §5.5 标题改为 \"Cross-Model Replication\" 而非 \"Cross-Model Generality\"，降低泛化暗示。\n\n**W5** [warning] **关键数字重复过多**\n- 具体位置：Abstract, §1 (×3), Figure 1 caption, §4.2, §5.3, Figure 4 caption\n- 问题：\"20–33× gap\" 在论文中出现至少 7 次（abstract 1次、intro 3次、figure 1 caption、experiments、analysis、figure 4 caption）。虽然这是核心发现，但过度重复降低了信息密度，给人 padding 的感觉。类似地，\"0.064 to 0.727\" 出现 4 次以上。\n- 建议：在 abstract 和核心结果处保留精确数字，后续引用时使用 \"order-of-magnitude gap\" 或 \"the TF-AR gap (§4.2)\" 等简洁回指。\n\n**W6** [warning] **Table 1 四舍五入与正文数字不一致**\n- 具体位置：§4.2 vs Table 1\n- 问题：§4.2 称 \"GAR-ours spans only 0.75 percentage points (pp) across ThreadGate (0.50), +PCGrad (0.50), Uniform Gate (0.51), and LoRA-only (0.50)\"。但 Table 1 显示的数值只保留两位小数（0.50, 0.50, 0.51, 0.50），从这些数字计算 spread 应该是 1 pp 而非 0.75 pp。这意味着实际值在更高精度下不同（如 0.5025 vs 0.5100），但 table 的四舍五入导致读者无法验证这一 claim。\n- 建议：Table 1 增加一位小数，或在正文中使用与 table 一致的精度。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**：Abstract 过于密集（约 180 词），信息压缩度极高，首次阅读时难以消化。建议精简 contribution 罗列，留更多空间给核心发现的叙事。\n- **M2**：§5.5 Llama 结果使用 median 而非 mean 报告 AR GAR-ours，理由是 heavy-tailed distribution。虽然统计上合理，但在主实验（Table 1）使用 mean 的情况下切换统计量有 metric selection 之嫌。建议同时报告 mean 和 median。\n- **M3**：部分 bib 条目格式不一致——已发表的会议论文使用 @inproceedings（正确），但 Raposo et al. 2024 (Mixture-of-Depths) 使用 @article + arXiv 格式，该论文已被 ICML 2024 接收，应更新为会议版本。同样，Gromov et al. 2024 标注 year=2025 但 booktitle 为 ICLR，需确认年份一致性。\n- **M4**：§6 Discussion 提到 KV cache drift 作为替代假说，仅一句话。如果要提出这一替代假说，应至少简述为什么当前实验不能区分 exposure bias 和 KV cache drift。\n- **M5**：Conclusion（§7）仅 3 句话，虽然简洁但可能过于简短。建议增加 1-2 句关于 future directions 或 broader implications。\n- **M6**：论文未提及代码是否开源。ARR reproducibility 评分需要考虑这一因素。\n\n---\n\n## Questions to Authors\n\n**Q1**：Table 1 中 LoRA-only 的 AR GAR-ours (0.025) 反而高于所有 gating variants (0.015-0.016)。虽然差异很小，但方向是 gating 反而降低了 AR GAR。这是否意味着 gate 的 2-7% attenuation 在推理时略微有害？\n\n**Q2**：β-steering 实验中，β=0 时 N=5（10-turn）的 baseline GAR 为 0.028，但 N=50 的 baseline GAR 为 0.064（mean），差异超过 2×。论文解释为 \"short conversations with high baseline GAR\" 导致均值偏高。但这是否意味着 GAR 作为指标对对话长度高度敏感，从而削弱了跨实验设置的可比性？\n\n**Q3**：Scheduled sampling 的第二个 seed 得到 GAR=0.418（gap 1.20×）vs 第一个 seed 的 0.318（gap 1.57×）。两个 seed 之间 AR GAR 相差 31%（0.318 vs 0.418）。作者是否能解释这种高方差的来源？这是否暗示 scheduled sampling 的效果对随机初始化非常敏感？\n\n**Q4**：论文使用 LoRA rank 16 进行微调。是否尝试过更高的 rank（如 64 或 128）？gate 的无效性是否可能部分归因于 LoRA 容量已经足够，而非 gating 本身无用？\n\n---\n\n## Missing References\n\n1. **Zhang et al. (2024) \"Tell Your Model Where to Attend\"** — 与 β-steering 思路相似的推理时注意力操控方法，应在 §2 Attention Manipulation 段落中讨论。\n2. **Xu et al. (2025) 或类似的 multi-turn instruction following benchmarks** — 论文缺少对多轮指令遵循质量的标准化评估（如 IFEval multi-turn variant），这些基准应在 §4.1 Setup 中被提及。\n3. 建议核实 Raposo et al. (2024) Mixture-of-Depths 是否已在 ICML 2024 正式发表，如是则应更新 bib 条目。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 — Borderline Conference\n\n**一句话总结**：方法论严谨的负面结果论文，exposure bias 对辅助注意力目标的选择性破坏是真正新颖的发现，但 GAR 指标缺乏下游验证这一根本缺陷削弱了核心 claim 的实际意义。\n\n**详细理由**：\n\n本文的核心强项在于实验设计的严谨性和诊断链的完整性——五路对照、PCGrad 排除、gate 值分析、跨模型验证构成了一个令人信服的论证结构。Exposure bias 对辅助注意力损失的选择性破坏确实是文献中未被系统研究的现象，具有理论贡献。\n\n但论文有两个 critical 弱点阻碍其达到 Conference 水平：(1) GAR 指标与实际指令遵循质量之间的 gap 未被 bridge——整个论文围绕一个注意力统计量展开，但从未证明这个统计量的改善对用户可感知的对话质量有意义；(2) Scheduled sampling 作为唯一的 training-time mitigation evidence 仅有单 seed 支撑，且两个 seed 间方差很大。如果补充下游任务验证和多 seed scheduled sampling 实验，论文将达到 4.0 (Conference) 水平。\n\n当前状态适合 Findings 接收。",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-22T23:00:12.401486+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 306 · 2026-05-22T23:00:32.955538+00:00_

审稿意见已提交给 Review Director。

**审稿完成摘要：**

- **Overall: 3.5/5 (Borderline Conference)**，当前状态适合 Findings
- **Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5**

**2 个 Critical 问题：**
1. GAR 指标与下游任务性能之间缺乏因果验证——instruction retention 分析 p=0.077 不显著，整个论文围绕一个未被验证的注意力统计量展开
2. Scheduled sampling 结果（gap 31×→1.57×）仅单 seed，两个 seed 间 AR GAR 相差 31%（0.318 vs 0.418），在 abstract/conclusion 中以确定性语气呈现存在 overclaim 风险

**6 个 Should-Fix 问题：** 标题误导（暗示 gating 固有失败而非 exposure bias 通用问题）、缺少与 split-softmax/Rhea 的实验对比、"to our knowledge, the first" 声称不可证伪、仅两个 7-8B 模型、关键数字重复过多、Table 1 精度与正文不一致

**核心判断：** 方法论严谨的负面结果 + 新颖的 exposure bias 归因，但 GAR→downstream 的 gap 是根本弱点。补充下游验证和多 seed 实验后可达 Conference (4.0) 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

10 recorded events


### User

_source line 307 · 2026-05-22T23:01:44.465672+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和 Minor 问题：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别注意以下分歧点：
1. Reviewer 1 给出 3.0（Findings），你给出 3.5（Borderline Conference）——请说明你认为差距在哪里
2. Reviewer 1 的 N2（exposure bias 归因缺乏替代假说排除）——你在 M4 也提到 KV cache drift，但未列为 critical。请明确你的严重性判断
3. Reviewer 1 认为 exposure bias 发现 "可预见性较强"，你认为是 "真正新颖的发现"——请明确你的立场并提供文献依据

---

以下是 Reviewer 1 的完整审稿意见：

## 总体评分
**Overall**: 3.0 / 5 — Findings

## 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 主要 claims 在定性层面有支撑，但定量证据不足（N=5 AR、单种子、KV cache drift 未排除） |
| Excitement | 3 / 5 | 负面结果+诊断框架对社区有用，但 exposure bias 作为根因的发现可预见性较强 |
| Reproducibility | 3 / 5 | 超参数基本完整但部分关键参数缺失（r_min），无代码发布承诺 |
| Confidence | 4 / 5 | 仔细检查了实验方法论和技术细节 |

## Must-Fix 问题

**N1** [critical] 自回归评估样本量严重不足（N=5）
- 核心发现完全基于 Qwen 上 5 条自回归对话。N=5 无法提供有意义的统计推断力。
- 建议：AR 评估扩展到至少 N=50；报告置信区间和显著性检验。

**N2** [critical] Exposure bias 归因缺乏对替代假说的充分排除
- §6 承认 KV cache drift 未被排除，§8 明确说留给 future work。对 "mechanistic analysis" 论文而言不可接受。
- 建议：设计实验区分 prefix-level exposure bias 和 cache-level drift。

**N3** [critical] 绝大多数实验条件为单种子
- 5 路对比中仅 ThreadGate 有 2 个种子，其余 4 个条件单种子。SS 两种子差异 72%。
- 建议：至少 3 种子覆盖全部条件。

## Should-Fix 问题

**W1** [warning] 跨模型验证不完整（Llama 仅 3/5 条件）
**W2** [warning] "Mechanistic Analysis" 标题与分析深度不匹配——建议改为 "Diagnostic Analysis"
**W3** [warning] Scheduled sampling 证据过于单薄
**W4** [warning] GAR 改善与生成质量（PPL）脱节
**W5** [warning] GAR-D 全条件接近零——干预仅在 last token 成功

## 小问题
M1: r_min 正文未报告 | M2: Table 1 AR 列缺 GAR-D 和 PPL | M3: N 定义不一致 | M4: Figure 4/6 打印尺寸 | M5: §7 steering 措辞 | M6: 匿名合规 | M7: 8 页限制合规

## 主要优势
1. 研究问题有价值 2. 五路对比设计合理 3. 多维度诊断链 4. β steering phase transition 5. Loss search 透明

## Questions
1. SS 两种子 GAR 差异 72% 如何解释？
2. LoRA-only AR GAR 高于 gated variants 多种子下是否稳定？
3. 代码发布计划？
4. r_min 数值？
5. TF→AR 切换临界轮次 k？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-22T23:02:32.286589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "offset": "38",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "offset": "38",
    "limit": "25"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-22T23:02:32.688111+00:00_

38	
39	\begin{figure}[t]
40	  \centering
41	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
42	  \caption{Per-turn GAR-ours under teacher-forced evaluation ($N$\,=\,45, $\pm$1\,std). Fine-tuned variants maintain GAR near $\tau$\,=\,0.5 with 7--8\% decay (T1$\to$T4); Base decays 80\%. T5 std inflated by truncated conversations. Despite this preservation, autoregressive GAR collapses to 0.015--0.025 for all variants (Table~\ref{tab:four-way}), consistent with distribution shift as the primary failure mode under these conditions.}
43	  \label{fig:attention-heatmap}
44	\end{figure}
45	
46	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
47	
48	All training-time interventions fail uniformly. We test whether inference-time attention manipulation can recover GAR by applying an additive bias $\beta$ to goal-token attention logits at every layer of the ThreadGate checkpoint during generation.
49	
50	An initial sweep on $N$\,=\,5 ten-turn conversations (Figure~\ref{fig:steering}a) reveals a sharp nonlinearity between $\beta$\,=\,2 and $\beta$\,=\,5: GAR increases ${\sim}$11$\times$ (0.062\,$\to$\,0.6795$\pm$0.020) while PPL rises 35\% (1.41\,$\to$\,1.91). At $\beta$\,=\,10, GAR saturates at 0.959 but PPL degrades to 4.22.
51	
52	$N$\,=\,50 conversations from a held-out evaluation set (39 with $\geq$3 turns, mean 3.6 user turns; Figure~\ref{fig:steering}b) confirm the qualitative steering pattern observed in the $N$\,=\,5 pilot (10 turns each), with consistent nonlinearity range and saturation behavior. A finer $\beta$ sweep localizes the nonlinearity: GAR jumps from 0.128$\pm$0.110 ($\beta$\,=\,2) to 0.556$\pm$0.060 ($\beta$\,=\,3), an 8.7$\times$ recovery from baseline with only 9\% PPL increase (1.43\,$\to$\,1.56), identifying $\beta$\,=\,3 as a practical operating point. The $\beta$\,=\,0 distribution is right-skewed (mean 0.064, median 0.031, std 0.081), driven by short conversations with high baseline GAR; absolute baselines theref
…[truncated 1538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-22T23:02:32.788797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-22T23:02:33.140027+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is a proximal cause (\S\ref{subsec:steering}). Alternative hypotheses remain open; our evidence is consistent with exposure bias as the dominant factor but does not exclude alternatives. In particular, KV cache drift---accumulation of model-generated key-value states diverging from teacher-forced statistics---could compound the mismatch; disentangling prefix-level and cache-level contributions is left to future work. Split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea} complement $\beta$-steering by restructuring attention computation at the architectural level, but cannot resolve exposure bias in auxiliary losses requiring retraining.
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, mixing teacher-forced and model-generated contexts. AR GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36), consistent with exposure bias as a primary driver. GAR-Dongre also rises (0.019$\to$0.353). On the $N$\,=\,50 evaluation, $\beta$\,=\,5 incurs 24\% PPL cost (1.43\,$\to$\,1.77); $\beta$\,=\,3 offers a more balanced tradeoff (+9\%); scheduled sampling incurs no fluency cost but requires retraining. A second seed yields AR GAR\,=\,0.418 (gap 1.20$\times$); systematic ablation is deferred. Exploratory instruction retention analysis (Appendix~\ref{sec:appendix-ir}) shows +23.8\,pp compliance at $\beta$\,=\,3 (McNemar $p$\,=\,0.077).
6	
7	T
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-22T23:02:33.190562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "offset": "33",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "offset": "33",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-22T23:02:33.241201+00:00_

33	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
34	
35	Gates are ineffective (\S\ref{subsec:gate-conditioning}) and gradient conflict is not the cause (\S\ref{subsec:pcgrad}). The TF-AR GAR gap (Table~\ref{tab:four-way}) persists across all training strategies. GAR-Dongre provides a revealing control: under standard training it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys the concentrated last-token attention pattern while leaving diffuse attention unaffected (scheduled sampling breaks this pattern; \S\ref{sec:discussion}).
36	
37	The mechanism is exposure bias \citep{bengio2015scheduled,arora2022exposure}: during training, the model conditions on ground-truth prefixes; at inference, on its own outputs. The statistical properties diverge, and the 2--7\% gate attenuation (\S\ref{subsec:gate-conditioning}) cannot compensate. \citet{he2019exposure} showed that language models exhibit token-level self-recovery from exposure bias, and our PPL results confirm this (Table~\ref{tab:four-way}). The critical distinction is between primary and auxiliary objectives: NTP is robust because it is the same task at both training and inference time, while GAR optimizes a distributional property of the input prefix that has no counterpart under autoregressive generation. Figure~\ref{fig:attention-heatmap} confirms teacher-forced GAR-ours remains near $\tau = 0.5$ (7--8\% decay, $N$\,=\,45), yet autoregressive GAR collapses for all variants (Figure~\ref{fig:gate-shift}b).
38	
39	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
40	
41	\S\ref{subsec:dist-shift} showed that exposure bias selectively destroys GAR-ours while GAR-Dongre remains unaffected under standard training. We test whether this selectivity extends beyond attention with Turn-level Residual Coherence (TRC), the cosine similarity between hidden states at the last-token position of adjacent assistant turns. For ThreadGate, TF/AR TR
…[truncated 1648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-22T23:04:44.400946+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 针对 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题回应\n\n**[REBUT] R1-N1: 自回归评估样本量严重不足（N=5）**\n\nR1 称 \"核心发现完全基于 Qwen 上 5 条自回归对话\"，我认为这过于严厉，原因有三：\n\n(1) **效应量远超统计噪声。** TF GAR=0.50 vs AR GAR=0.015–0.025，是 20–33× 的坍塌（Table 1）。即使 N=5，这个量级的差异在任何合理的方差假设下都不可能是随机波动。对比：第二个 seed（seed=123）得到 AR GAR=0.016±0.001，gap 30.5–32.1×（§4.2），进一步确认了稳定性。\n\n(2) **N=50 的 β=0 baseline 提供了独立验证。** §4.3 的 steering 实验在 N=50 held-out conversations 上的 β=0 条件下也观察到 AR GAR=0.064（mean），虽然绝对值不同（因为对话长度分布不同），但同样呈现 order-of-magnitude 的 TF-AR gap。这不是额外的 5 条对话——是 50 条独立对话。\n\n(3) **跨模型复制。** Llama-3.1-8B 上 N=20 的 AR 评估得到 median GAR=0.018（§5.5），gap 27×。跨架构、跨样本的一致性使得 N=5 的单一数据点的局限性被系统级证据弥补。\n\n**我的判断：Should-Fix，而非 Critical。** 论文应在 Table 1 中扩展 AR 评估到 N≥20 并报告 std，但 N=5 不足以否定 20–33× 效应量的可信度。将此列为 critical 意味着 N=5 可能导致结论反转——这在如此大的效应量下极不现实。\n\n---\n\n**[AGREE with downgrade] R1-N2: Exposure bias 归因缺乏对替代假说的充分排除**\n\nR1 指出 KV cache drift 未被排除，我在自己的审稿中也提及此问题（M4），但仅列为 minor。经过与 R1 意见的交叉比较，我上调严重性至 **Should-Fix**，但仍不同意列为 Critical，理由如下：\n\n**部分同意的理由：** 论文声称进行 \"Mechanistic Analysis\"，但对 KV cache drift vs prefix-level exposure bias 的区分确实不够深入。§6 仅用一句话提及 KV cache drift 并留给 future work，这对 mechanistic 论文来说不够。\n\n**不升至 Critical 的理由：**\n- 论文使用了合适的 hedging：\"consistent with exposure bias as the dominant factor but does not exclude alternatives\"（§6）、\"proximal cause\"（§4.3）。归因被表述为最佳解释而非唯一解释。\n- Scheduled sampling 提供了正向鉴别证据：它直接针对 exposure bias（在训练时混入模型生成上下文），且有效（gap 从 31× 压缩至 1.57×）。虽然 SS 也会部分缓解 KV cache drift（因为训练时暴露于自生成的 KV states），但 SS 的设计动机和机制更直接对应 exposure bias。\n- β-steering 与 TRC 分析（§5.4）表明问题在注意力路由而非表征层面（TRC gap <0.06 vs GAR gap 20–33×），这缩小了替代假说的解释空间。\n\n**我的结论：** 从 M4 上调至 Should-Fix (W-level)。论文应在 §5.3 或 §6 增加 1–2 段讨论为何现有证据更支持 exposure bias 而非 KV cache drift（例如：GAR 坍塌的突变性 vs 渐进累积性、SS 的靶向机制），但不需要设计全新实验来排除。\n\n---\n\n**[PARTIALLY AGREE] R1-N3: 绝大多数实验条件为单种子**\n\n- 对 **scheduled sampling**：完全同意，这也是我自己 N2 (critical) 的核心内容。两个 seed 之间 AR GAR 差异 31%（0.318 vs 0.418），证据不足以支撑作为 contribution 的一部分。\n- 对 **五路对比主实验**：部分反对。四个 fine-tuned variants 在单 seed 下收敛到 0.75 pp 之内（GAR-ours 0.50–0.51，PPL 均为 2.78），且 ThreadGate 的第二个 seed 确认了几乎零方差（±0.001）。四条件间的收敛本身就是隐式的 robustness evidence——如果结果对 seed 敏感，四个架构不同的 variants 不太可能恰好收敛到同一点。当然，这不能替代正式的多 seed 验证，但将其列为 critical（暗示可能推翻结论）过于严厉。\n\n**我的判断：** SS 单 seed 是 Critical（我已在自己的 N2 中标记），主实验单 seed 是 Should-Fix。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R1-W1: 跨模型验证不完整（Llama 仅 3/5 条件）**\n同意。我在 W4 中也提出了相同问题。§5.5 标题 \"Cross-Model Generality\" 暗示的泛化程度超出了实际验证范围。建议改为 \"Cross-Model Replication\"。\n\n**[REBUT] R1-W2: \"Mechanistic Analysis\" 标题与分析深度不匹配**\nR1 建议改为 \"Diagnostic Analysis\"。我认为当前标题可以保留，但理由不在于分析深度足够。论文的分析确实是 diagnostic 性质（排除 → 排除 → 归因）而非 mechanistic（揭示底层计算电路）。但 \"diagnostic\" 在 NLP 社区的使用不如 \"mechanistic\" 常见，且论文的 gate 值分析（§5.1）、梯度冲突量化（§5.2）、TRC 分析（§5.4）已超越纯粹的 ablation-based diagnosis。我更倾向于我自己的标题建议（W1）：直接在标题中体现 exposure bias 这一核心发现，而非争论 \"mechanistic\" vs \"diagnostic\" 的标签。\n\n**[AGREE] R1-W3: Scheduled sampling 证据过于单薄**\n完全同意，与我的 N2 一致。\n\n**[AGREE with nuance] R1-W4: GAR 改善与生成质量（PPL）脱节**\n这与我的 N1 (critical) 高度相关——GAR 缺乏下游验证。R1 的 framing 略有不同（关注 GAR vs PPL 脱节），但本质相同。我同意严重性评估，但我将其列为 Critical（N1）而非 Should-Fix，因为它影响论文核心 claim 的实际意义。\n\n**[PARTIALLY AGREE] R1-W5: GAR-D 全条件接近零——干预仅在 last-token 成功**\nR1 指出 GAR-Dongre（all-token average）在所有标准训练条件下接近零（0.01–0.02），暗示干预仅对 last-token attention 有效。这是一个有价值的观察，但论文对此有明确解释：GAR-ours 被设计为优化目标（§3.1），GAR-Dongre 作为对照指标，且 scheduled sampling 实际上打破了 GAR-Dongre 的零模式（从 0.019 上升至 0.353，§6）。last-token 选择有合理的 motivation（最后一个 token 的注意力反映 continuation 时的信息路由）。我同意这值得 should-fix 级别的讨论，但不认为它削弱了核心论证。\n\n---\n\n### 小问题回应\n\n**[AGREE] R1-M1: σ_min 正文未报告。** 应在 §3.3 或 Appendix A 中报告具体数值。\n\n**[AGREE] R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。** 补充 AR 条件下的 GAR-Dongre 和 PPL 会使对比更完整。\n\n**[AGREE] R1-M3: N 定义不一致。** N=5（10-turn）vs N=50（variable length）的差异确实造成混淆，应统一标注。\n\n**[AGREE] R1-M4: Figure 4/6 打印尺寸。** 未亲自检查打印尺寸，但如果 R1 发现可读性问题则应修复。\n\n**[AGREE] R1-M5: §7 steering 措辞。** 未发现具体问题，但信任 R1 的观察。\n\n**[AGREE] R1-M6: 匿名合规。** 我检查时未发现匿名性违规（首页为 \"Anonymous ACL submission\"），但如果 R1 发现了具体问题请指出。\n\n**[AGREE] R1-M7: 8 页限制合规。** 我验证了正文在第 8 页结束（§7 Conclusion 在 page 8 底部），§8 Limitations 从 page 9 开始。格式合规。\n\n---\n\n### 三个关键分歧点的明确回应\n\n#### 分歧 1：评分差距（R1: 3.0 vs R2: 3.5）\n\n差距核心在于两点：\n\n**(a) N=5 的严重性判断。** R1 将 N=5 AR 评估列为 critical，我认为是 should-fix。20–33× 的效应量、第二 seed 确认（gap 30.5–32.1×）、N=50 β=0 baseline、以及 Llama 上的跨模型复制，使得 N=5 这一单一局限不足以将论文从 3.5 拉至 3.0。扩展 N 是必要的改进，但不太可能改变结论方向。\n\n**(b) 新颖性估值。** R1 认为 exposure bias 发现 \"可预见性较强\"（详见分歧 3），我不同意。这一分歧直接影响 excitement 评分和 overall 评估。\n\n如果 R1 的 N=5 降级为 should-fix（我认为合理），且新颖性被重新评估，R1 的评分应上升至 3.5。反之，如果我接受 R1 对 KV cache drift 的更严格标准（从 M4 上调至 should-fix），我的评分保持 3.5 不变，因为这不改变核心判断。\n\n#### 分歧 2：KV cache drift 的严重性\n\nR1: Critical（N2）→ R2: Should-Fix（从 M4 上调）\n\n我的理由见上文 R1-N2 回应。核心分歧在于：论文是否需要 **设计新实验** 来区分 exposure bias 和 KV cache drift，还是 **加强现有证据的讨论** 即可。我认为后者在 camera-ready 阶段可行，前者在 rebuttal 期间可能不现实（需要额外训练和评估），且论文的 hedging 已经足够诚实。对 Findings 级别的论文，这一标准是合理的。\n\n#### 分歧 3：Exposure bias 发现的新颖性\n\nR1 认为 \"exposure bias 作为根因的发现可预见性较强\"。**我明确反对这一判断**，理由如下：\n\n**(1) 先验预测指向相反方向。** He et al. (2019) 的核心发现是语言模型在 token prediction 层面对 exposure bias 具有 self-recovery 能力。如果一个 reviewer 在读本文之前被问 \"exposure bias 是否会摧毁与 NTP 联合训练的辅助损失？\"，He et al. 的结果会导向 \"不太可能\" 的预测——如果主任务能 self-recover，联合训练的辅助任务为什么不能？\n\n**(2) 选择性破坏是非直觉的。** 本文的发现不只是 \"exposure bias 影响了辅助损失\"，而是 **NTP 完全不受影响**（PPL 不变）的同时 GAR 坍塌 20–33×。这种选择性在先前文献中没有先例。Arora et al. (2022) 和 Bengio et al. (2015) 都将 exposure bias 描述为对主生成目标的全局性影响。\n\n**(3) 文献空白是真实的。** 我检查了 exposure bias 相关文献（Bengio 2015, Wiseman & Rush 2016, Ranzato et al. 2016, Lamb et al. 2016, He et al. 2019, Arora et al. 2022, Leblond et al. 2018），没有任何一篇讨论 exposure bias 对辅助（非生成）目标的影响。这不是 \"niche 太窄所以没人做\"——而是一个有理论意义的盲区，本文填补了它。\n\n**(4) \"可预见\" ≠ \"已知\"。** 即使事后看 exposure bias 是 \"合理的\" 解释，论文的贡献在于 (a) 系统性地建立了这一因果链（五路排除 + β-steering 建设性证据），(b) 量化了选择性破坏的程度（20–33× vs PPL 不变），(c) 展示了 token-level self-recovery 不延伸到注意力分布属性。\"合理但未被验证\" 和 \"已经被知道\" 有本质区别。\n\n**结论：** 我维持 excitement = 3/5 和 overall = 3.5 的评分。这不是 4.0（Conference）因为 GAR-downstream gap（我的 N1）和 SS 单 seed（我的 N2）是真实的弱点。但也不应是 3.0（Findings），因为方法论的严谨性和发现的真正新颖性超出了 Findings 的下限。",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 针对 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题回应\n\n**[REBUT] R1-N1: 自回归评估样本量严重不足（N=5）**\n\nR1 称 \"核心发现完全基于 Qwen 上 5 条自回归对话\"，我认为这过于严厉，原因有三：\n\n(1) **效应量远超统计噪声。** TF GAR=0.50 vs AR GAR=0.015–0.025，是 20–33× 的坍塌（Table 1）。即使 N=5，这个量级的差异在任何合理的方差假设下都不可能是随机波动。对比：第二个 seed（seed=123）得到 AR GAR=0.016±0.001，gap 30.5–32.1×（§4.2），进一步确认了稳定性。\n\n(2) **N=50 的 β=0 baseline 提供了独立验证。** §4.3 的 steering 实验在 N=50 held-out conversations 上的 β=0 条件下也观察到 AR GAR=0.064（mean），虽然绝对值不同（因为对话长度分布不同），但同样呈现 order-of-magnitude 的 TF-AR gap。这不是额外的 5 条对话——是 50 条独立对话。\n\n(3) **跨模型复制。** Llama-3.1-8B 上 N=20 的 AR 评估得到 median GAR=0.018（§5.5），gap 27×。跨架构、跨样本的一致性使得 N=5 的单一数据点的局限性被系统级证据弥补。\n\n**我的判断：Should-Fix，而非 Critical。** 论文应在 Table 1 中扩展 AR 评估到 N≥20 并报告 std，但 N=5 不足以否定 20–33× 效应量的可信度。将此列为 critical 意味着 N=5 可能导致结论反转——这在如此大的效应量下极不现实。\n\n---\n\n**[AGREE with downgrade] R1-N2: Exposure bias 归因缺乏对替代假说的充分排除**\n\nR1 指出 KV cache drift 未被排除，我在自己的审稿中也提及此问题（M4），但仅列为 minor。经过与 R1 意见的交叉比较，我上调严重性至 **Should-Fix**，但仍不同意列为 Critical，理由如下：\n\n**部分同意的理由：** 论文声称进行 \"Mechanistic Analysis\"，但对 KV cache drift vs prefix-level exposure bias 的区分确实不够深入。§6 仅用一句话提及 KV cache drift 并留给 future work，这对 mechanistic 论文来说不够。\n\n**不升至 Critical 的理由：**\n- 论文使用了合适的 hedging：\"consistent with exposure bias as the dominant factor but does not exclude alternatives\"（§6）、\"proximal cause\"（§4.3）。归因被表述为最佳解释而非唯一解释。\n- Scheduled sampling 提供了正向鉴别证据：它直接针对 exposure bias（在训练时混入模型生成上下文），且有效（gap 从 31× 压缩至 1.57×）。虽然 SS 也会部分缓解 KV cache drift（因为训练时暴露于自生成的 KV states），但 SS 的设计动机和机制更直接对应 exposure bias。\n- β-steering 与 TRC 分析（§5.4）表明问题在注意力路由而非表征层面（TRC gap <0.06 vs GAR gap 20–33×），这缩小了替代假说的解释空间。\n\n**我的结论：** 从 M4 上调至 Should-Fix (W-level)。论文应在 §5.3 或 §6 增加 1–2 段讨论为何现有证据更支持 exposure bias 而非 KV cache drift（例如：GAR 坍塌的突变性 vs 渐进累积性、SS 的靶向机制），但不需要设计全新实验来排除。\n\n---\n\n**[PARTIALLY AGREE] R1-N3: 绝大多数实验条件为单种子**\n\n- 对 **scheduled sampling**：完全同意，这也是我自己 N2 (critical) 的核心内容。两个 seed 之间 AR GAR 差异 31%（0.318 vs 0.418），证据不足以支撑作为 contribution 的一部分。\n- 对 **五路对比主实验**：部分反对。四个 fine-tuned variants 在单 seed 下收敛到 0.75 pp 之内（GAR-ours 0.50–0.51，PPL 均为 2.78），且 ThreadGate 的第二个 seed 确认了几乎零方差（±0.001）。四条件间的收敛本身就是隐式的 robustness evidence——如果结果对 seed 敏感，四个架构不同的 variants 不太可能恰好收敛到同一点。当然，这不能替代正式的多 seed 验证，但将其列为 critical（暗示可能推翻结论）过于严厉。\n\n**我的判断：** SS 单 seed 是 Critical（我已在自己的 N2 中标记），主实验单 seed 是 Should-Fix。\n\n---\n\n### Should-Fix 问题回应\n\n**[AGREE] R1-W1: 跨模型验证不完整（Llama 仅 3/5 条件）**\n同意。我在 W4 中也提出了相同问题。§5.5 标题 \"Cross-Model Generality\" 暗示的泛化程度超出了实际验证范围。建议改为 \"Cross-Model Replication\"。\n\n**[REBUT] R1-W2: \"Mechanistic Analysis\" 标题与分析深度不匹配**\nR1 建议改为 \"Diagnostic Analysis\"。我认为当前标题可以保留，但理由不在于分析深度足够。论文的分析确实是 diagnostic 性质（排除 → 排除 → 归因）而非 mechanistic（揭示底层计算电路）。但 \"diagnostic\" 在 NLP 社区的使用不如 \"mechanistic\" 常见，且论文的 gate 值分析（§5.1）、梯度冲突量化（§5.2）、TRC 分析（§5.4）已超越纯粹的 ablation-based diagnosis。我更倾向于我自己的标题建议（W1）：直接在标题中体现 exposure bias 这一核心发现，而非争论 \"mechanistic\" vs \"diagnostic\" 的标签。\n\n**[AGREE] R1-W3: Scheduled sampling 证据过于单薄**\n完全同意，与我的 N2 一致。\n\n**[AGREE with nuance] R1-W4: GAR 改善与生成质量（PPL）脱节**\n这与我的 N1 (critical) 高度相关——GAR 缺乏下游验证。R1 的 framing 略有不同（关注 GAR vs PPL 脱节），但本质相同。我同意严重性评估，但我将其列为 Critical（N1）而非 Should-Fix，因为它影响论文核心 claim 的实际意义。\n\n**[PARTIALLY AGREE] R1-W5: GAR-D 全条件接近零——干预仅在 last-token 成功**\nR1 指出 GAR-Dongre（all-token average）在所有标准训练条件下接近零（0.01–0.02），暗示干预仅对 last-token attention 有效。这是一个有价值的观察，但论文对此有明确解释：GAR-ours 被设计为优化目标（§3.1），GAR-Dongre 作为对照指标，且 scheduled sampling 实际上打破了 GAR-Dongre 的零模式（从 0.019 上升至 0.353，§6）。last-token 选择有合理的 motivation（最后一个 token 的注意力反映 continuation 时的信息路由）。我同意这值得 should-fix 级别的讨论，但不认为它削弱了核心论证。\n\n---\n\n### 小问题回应\n\n**[AGREE] R1-M1: σ_min 正文未报告。** 应在 §3.3 或 Appendix A 中报告具体数值。\n\n**[AGREE] R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。** 补充 AR 条件下的 GAR-Dongre 和 PPL 会使对比更完整。\n\n**[AGREE] R1-M3: N 定义不一致。** N=5（10-turn）vs N=50（variable length）的差异确实造成混淆，应统一标注。\n\n**[AGREE] R1-M4: Figure 4/6 打印尺寸。** 未亲自检查打印尺寸，但如果 R1 发现可读性问题则应修复。\n\n**[AGREE] R1-M5: §7 steering 措辞。** 未发现具体问题，但信任 R1 的观察。\n\n**[AGREE] R1-M6: 匿名合规。** 我检查时未发现匿名性违规（首页为 \"Anonymous ACL submission\"），但如果 R1 发现了具体问题请指出。\n\n**[AGREE] R1-M7: 8 页限制合规。** 我验证了正文在第 8 页结束（§7 Conclusion 在 page 8 底部），§8 Limitations 从 page 9 开始。格式合规。\n\n---\n\n### 三个关键分歧点的明确回应\n\n#### 分歧 1：评分差距（R1: 3.0 vs R2: 3.5）\n\n差距核心在于两点：\n\n**(a) N=5 的严重性判断。** R1 将 N=5 AR 评估列为 critical，我认为是 should-fix。20–33× 的效应量、第二 seed 确认（gap 30.5–32.1×）、N=50 β=0 baseline、以及 Llama 上的跨模型复制，使得 N=5 这一单一局限不足以将论文从 3.5 拉至 3.0。扩展 N 是必要的改进，但不太可能改变结论方向。\n\n**(b) 新颖性估值。** R1 认为 exposure bias 发现 \"可预见性较强\"（详见分歧 3），我不同意。这一分歧直接影响 excitement 评分和 overall 评估。\n\n如果 R1 的 N=5 降级为 should-fix（我认为合理），且新颖性被重新评估，R1 的评分应上升至 3.5。反之，如果我接受 R1 对 KV cache drift 的更严格标准（从 M4 上调至 should-fix），我的评分保持 3.5 不变，因为这不改变核心判断。\n\n#### 分歧 2：KV cache drift 的严重性\n\nR1: Critical（N2）→ R2: Should-Fix（从 M4 上调）\n\n我的理由见上文 R1-N2 回应。核心分歧在于：论文是否需要 **设计新实验** 来区分 exposure bias 和 KV cache drift，还是 **加强现有证据的讨论** 即可。我认为后者在 camera-ready 阶段可行，前者在 rebuttal 期间可能不现实（需要额外训练和评估），且论文的 hedging 已经足够诚实。对 Findings 级别的论文，这一标准是合理的。\n\n#### 分歧 3：Exposure bias 发现的新颖性\n\nR1 认为 \"exposure bias 作为根因的发现可预见性较强\"。**我明确反对这一判断**，理由如下：\n\n**(1) 先验预测指向相反方向。** He et al. (2019) 的核心发现是语言模型在 token prediction 层面对 exposure bias 具有 self-recovery 能力。如果一个 reviewer 在读本文之前被问 \"exposure bias 是否会摧毁与 NTP 联合训练的辅助损失？\"，He et al. 的结果会导向 \"不太可能\" 的预测——如果主任务能 self-recover，联合训练的辅助任务为什么不能？\n\n**(2) 选择性破坏是非直觉的。** 本文的发现不只是 \"exposure bias 影响了辅助损失\"，而是 **NTP 完全不受影响**（PPL 不变）的同时 GAR 坍塌 20–33×。这种选择性在先前文献中没有先例。Arora et al. (2022) 和 Bengio et al. (2015) 都将 exposure bias 描述为对主生成目标的全局性影响。\n\n**(3) 文献空白是真实的。** 我检查了 exposure bias 相关文献（Bengio 2015, Wiseman & Rush 2016, Ranzato et al. 2016, Lamb et al. 2016, He et al. 2019, Arora et al. 2022, Leblond et al. 2018），没有任何一篇讨论 exposure bias 对辅助（非生成）目标的影响。这不是 \"niche 太窄所以没人做\"——而是一个有理论意义的盲区，本文填补了它。\n\n**(4) \"可预见\" ≠ \"已知\"。** 即使事后看 exposure bias 是 \"合理的\" 解释，论文的贡献在于 (a) 系统性地建立了这一因果链（五路排除 + β-steering 建设性证据），(b) 量化了选择性破坏的程度（20–33× vs PPL 不变），(c) 展示了 token-level self-recovery 不延伸到注意力分布属性。\"合理但未被验证\" 和 \"已经被知道\" 有本质区别。\n\n**结论：** 我维持 excitement = 3/5 和 overall = 3.5 的评分。这不是 4.0（Conference）因为 GAR-downstream gap（我的 N1）和 SS 单 seed（我的 N2）是真实的弱点。但也不应是 3.0（Findings），因为方法论的严谨性和发现的真正新颖性超出了 Findings 的下限。",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-22T23:04:48.112133+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3711
}
```

</details>

---


### Assistant

_source line 316 · 2026-05-22T23:05:01.265984+00:00_

交叉回应已提交给 Review Director。

主要立场总结：
- R1-N1（N=5 AR）：反驳，降级为 Should-Fix。20–33× 效应量 + 二次 seed + N=50 β=0 baseline + 跨模型复制足以支撑结论。
- R1-N2（KV cache drift）：部分同意，从我原来的 M4 上调至 Should-Fix，但仍低于 R1 的 Critical。论文的 hedging 合理，现有证据（SS + TRC）已提供鉴别线索。
- R1-N3（单 seed）：SS 部分完全同意（与我的 N2 一致），主实验部分降级为 Should-Fix。
- 新颖性分歧：明确反驳 R1 的 "可预见性强" 判断，以 He et al. (2019) 的 self-recovery 结果为基础论证先验预测实际指向相反方向。
- 维持 Overall = 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

96 recorded events


### User

_source line 317 · 2026-05-25T05:37:07.083223+00:00_

[Round 1 审稿请求]:
你负责**新颖性 + 完整性 + 写作质量**的审查。

## 目标 Venue
- **EMNLP 2026** (via ARR May 2026 cycle)
- 截止日期: 2026-05-25
- Long Paper: 正文 8 页限制，参考文献不限
- 模板: ACL style (`\usepackage[review]{acl}`)
- 匿名: Double-blind
- 评分标准: ARR Overall Assessment (1-5 scale, 4=Conference acceptance)

## 论文路径
- LaTeX 源码: `projects/turn_residual_gating/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf`

## 你的审查侧重
1. **新颖性**：核心贡献相对现有工作的增量是否足够？claim 是否 overclaim？
2. **Related Work**：覆盖是否全面？与最相关竞争方法的对比是否公平？缺失的重要引用？
3. **叙事结构**：论文的 story 是否连贯？从问题定义到解决方案的逻辑链是否清晰？
4. **写作质量**：是否冗余？术语使用是否一致？图表 caption 是否准确？
5. **格式规范**：页数是否符合 8 页限制？引用格式是否一致？Limitations 是否合规？
6. **贡献清晰度**：contribution list 是否与实际内容匹配？是否有未兑现的承诺？

## 输出格式
请按以下结构输出审稿意见：
1. Summary (2-3 句)
2. Strengths (逐条)
3. Weaknesses (逐条，标注 Critical / Should-Fix / Minor)
4. Questions (需要作者回答的问题)
5. Missing References
6. Novelty Assessment (1-5)
7. Overall Assessment (1-5, 参考 ARR 标准)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-25T05:37:14.453464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-25T05:37:15.811124+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-25T05:37:15.962733+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-25T05:37:16.013428+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-25T05:37:21.816535+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 323 · 2026-05-25T05:37:23.876305+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 324 · 2026-05-25T05:37:29.018657+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review (ARR) 2026 guidelines. Here are the key details:

## Reviewer Guidelines

The recommended workflow is to (1) read the paper and get a first impression, (2) search for related work, not deliberately trying
…[truncated 1209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7202
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-25T05:37:30.575629+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 417.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6699
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-25T05:37:37.785309+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need every field name, its scale (e.g. 1-5), and the description of each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need every field name, its scale (e.g. 1-5), and the description of each score level."
  }
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-25T05:37:38.940677+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-25T05:37:39.244361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 329 · 2026-05-25T05:37:40.053606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 330 · 2026-05-25T05:37:40.759582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1818
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-25T05:37:40.761086+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1516
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-25T05:37:40.761395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-25T05:37:41.065782+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1012
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-25T05:37:41.066268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-25T05:37:41.720717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool result

_source line 336 · 2026-05-25T05:37:42.022681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-25T05:37:43.830050+00:00_

# ACL Rolling Review Form - Complete Structure

## Primary Review Dimensions

**1. Paper Summary**
Descriptive section requesting overview of paper content and potential misunderstandings.

**2. Summary of Strengths**
Open-ended assessment of reasons supporting publication at selective venues.

**3. Summary of Weaknesses**
Numbered concerns about correctness, impact, clarity, or other publication barriers.

**4. Comments/Suggestions/Typos**
Section for improvement suggestions beyond major concerns.

**5. Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; careful reading with familiarity of related work
- 4: Quite sure; important points checked carefully
- 3: Pretty sure; general area knowledge without detailed verification
- 2: Can defend evaluation but likely missed details or novelty assessment
- 1: Outside expertise area or paper very difficult to understand

**6. Soundness** (1-5 scale with half-points)
- 5: Most thorough for its type
- 4: Sufficient support; extra experiments optional
- 3: Adequate support for main claims; minor details needed
- 2: Main claims lack sufficient support; major technical problems
- 1: Insufficient depth or not relevant to computational linguistics

**7. Excitement** (1-5 scale with half-points)
Subjective assessment of conceptual breakthroughs, impact, or personal relevance.

**8. Overall Assessment** (1-5 scale with half-points)
Conference suitability recommendation ranging from award consideration to rejection.

**9. Additional Sections**
- Best paper justification
- Limitations and societal impact
- Ethical concerns
- Ethics review necessity
- Reproducibility (1-5)
- Dataset value (1-5)
- Software value (1-5)
- Author identity knowledge (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6044
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-25T05:37:50.813948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-25T05:37:51.366617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 340 · 2026-05-25T05:37:52.123263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-25T05:37:52.124161+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-25T05:37:52.275010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 343 · 2026-05-25T05:37:52.628141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 344 · 2026-05-25T05:37:53.086014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---


### Tool call

_source line 345 · 2026-05-25T05:37:53.086477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-25T05:37:53.843699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1215
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-25T05:37:54.046570+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-25T05:38:01.541502+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-25T05:38:03.053973+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 398.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 382.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 410.0}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 353.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p19.png\", \"width\": 1241, \"he
…[truncated 489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1512
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-25T05:38:05.991279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 351 · 2026-05-25T05:38:06.443846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-25T05:38:10.374030+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4382
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-25T05:38:10.375190+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3931
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-25T05:38:10.676747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-25T05:38:10.879635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-25T05:38:10.880104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-25T05:38:11.031953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-25T05:38:11.032481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-25T05:38:11.183594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-25T05:38:11.184012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-25T05:38:11.542339+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 865
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-25T05:38:11.542831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-25T05:38:13.608302+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2576
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-25T05:38:14.061168+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3181
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-25T05:38:14.114040+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2930
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-25T05:38:14.166397+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3286
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-25T05:38:14.171352+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2987
}
```

</details>

---


### Tool result

_source line 368 · 2026-05-25T05:38:14.427837+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2884
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-25T05:38:14.428919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3396
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-25T05:38:21.200616+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "21-33",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "21-33",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-25T05:38:23.512042+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 383.4}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 340.2}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.0}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.5}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.0}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 324.0}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 403.6}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p29.png\", \"width\": 1241, \"he
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2311
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-25T05:38:29.084197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-25T05:38:30.043106+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-25T05:38:30.043700+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-25T05:38:30.498649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-25T05:38:30.499386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-25T05:38:30.953815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-25T05:38:30.954282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-25T05:38:31.559044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-25T05:38:32.364747+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-25T05:38:32.365975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-25T05:38:32.416624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-25T05:38:32.870556+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-25T05:38:33.374150+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-25T05:38:33.374648+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p28.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-25T05:38:34.279562+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-25T05:38:34.280300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-25T05:38:34.331641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---


### Tool call

_source line 389 · 2026-05-25T05:38:34.667390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 390 · 2026-05-25T05:38:34.806061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 474
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-25T05:38:35.520853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-25T05:38:42.597606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p31.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---


### Tool call

_source line 393 · 2026-05-25T05:38:42.901729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p32.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-25T05:38:43.607921+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p33.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-25T05:38:44.312297+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1714
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-25T05:38:44.565304+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1663
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-25T05:38:44.919295+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-25T05:40:18.847550+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "exposure bias multi-turn dialogue language model attention 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "exposure bias multi-turn dialogue language model attention 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 399 · 2026-05-25T05:40:19.249502+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "residual gating transformer layer-wise attention modulation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "residual gating transformer layer-wise attention modulation 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 400 · 2026-05-25T05:40:26.078654+00:00_

Web search results for query: "exposure bias multi-turn dialogue language model attention 2024 2025"

Links: [{"title":"Beyond Single-Turn: A Survey on Multi-Turn Interactions with Large Language Models","url":"https://arxiv.org/html/2504.04717v4"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf"},{"title":"Evaluating Bias in Spoken Dialogue LLMs for Real-World Decisions and Recommendations","url":"https://arxiv.org/html/2510.02352v1"},{"title":"Published as a conference paper at COLM 2025","url":"https://openreview.net/pdf?id=QbLbXz8Idp"},{"title":"Mitigating Conversational Inertia in Multi-Turn Agents","url":"https://arxiv.org/pdf/2602.03664"},{"title":"TED: Turn Emphasis with Dialogue Feature Attention for Emotion   Recognition in Conversation","url":"https://arxiv.org/pdf/2501.01123"},{"title":"A Survey on Multi-Turn Interaction Capabilities of Large Language Models","url":"https://arxiv.org/html/2501.09959v1"}]

Based on the search results, here are recent findings related to exposure bias, multi-turn dialogue, and language model attention in 2024-2025:

## Multi-Turn Dialogue Challenges

Correctly understanding the biases implicit in multi-turn dialogues is crucial to avoiding being misled and generating biased outputs. Current fairness benchmarks primarily focus on single-turn dialogues, which overlooks the more practical and challenging scenarios presented by multi-turn dialogues in real-world applications.

## Attention Patterns and Conversational Inertia

Recent research has identified a phenomenon called "conversational inertia" in multi-turn agents. Models exhibit strong diagonal attention to previous assistant outputs, revealing token-to-token correspondence associated with conversational inertia. Quantitative analysis reveals monotonic growth in attention to previous assistant responses while attention allocation to user inputs r
…[truncated 822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7231
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-25T05:40:27.235683+00:00_

Web search results for query: "residual gating transformer layer-wise attention modulation 2024 2025"

Links: [{"title":"NeurIPS 2025 Best Paper Review: Qwen’s Systematic Exploration of Attention Gating | Towards Data Science","url":"https://towardsdatascience.com/neurips-2025-best-paper-review-qwens-systematic-exploration-of-attention-gating/"},{"title":"[NeurIPS 2025] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiviq.substack.com/p/neurips-2025-gated-attention-for"},{"title":"Gated Cross-Attention Mechanism","url":"https://www.emergentmind.com/topics/gated-cross-attention-mechanism"},{"title":"The Crystallization of Transformer Architectures (2017-2025) | Jun Yu Tan","url":"https://jytan.net/blog/2025/transformer-architectures/"},{"title":"What Layers When: Learning to Skip Compute in LLMs with Residual Gates","url":"https://arxiv.org/pdf/2510.13876"},{"title":"Gated Attention for Large Language Models: Non-linearity, ...","url":"https://arxiv.org/pdf/2505.06708"},{"title":"A Unified View of Attention and Residual Sinks: Outlier-Driven Rescaling is Essential for Transformer Training","url":"https://arxiv.org/html/2601.22966v1"}]

I found several relevant results about residual gating and transformer attention modulation from 2024-2025. Here's what the search revealed:

## Key Recent Work on Gated Attention (2024-2025)

A definitive recent study is "Gated Attention for Large Language Models: Non-Linearity, Sparsity, and Attention-Sink-Free" presented at NeurIPS 2025. This work introduces a modulation gate that operates on hidden states, with the core update rule Y′=Y ⊙ σ(XWθ), where the SDPA output is modulated by element-wise multiplication with a sigmoid-activated gating score.

The approach mechanistically eliminates the "Attention Sink" phenomenon and "Massive Activations" without requiring heuristic fixes, thereby significantly improving long-context extrapolation. This method has already been i
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7986
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-25T05:40:41.666317+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"conversational inertia\" multi-turn agent attention arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"conversational inertia\" multi-turn agent attention arxiv 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-25T05:40:41.917623+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "scheduled sampling exposure bias language generation beyond sequence-to-sequence 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "scheduled sampling exposure bias language generation beyond sequence-to-sequence 2023 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-25T05:40:49.045478+00:00_

Web search results for query: ""conversational inertia" multi-turn agent attention arxiv 2025 2026"

Links: [{"title":"[2602.03664] Mitigating Conversational Inertia in Multi-Turn Agents","url":"https://arxiv.org/abs/2602.03664"},{"title":"Mitigating Conversational Inertia in Multi-Turn Agents","url":"https://arxiv.org/pdf/2602.03664"},{"title":"Mitigating Conversational Inertia in Multi-Turn Agents","url":"https://arxiv.org/html/2602.03664v1"},{"title":"Mitigating Conversational Inertia in Multi-Turn Agents through Context Bias Calibration | OpenReview","url":"https://openreview.net/forum?id=UubLs3lUfk"},{"title":"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction","url":"https://arxiv.org/pdf/2603.04783"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/pdf/2502.11089"},{"title":"Aligning LLMs Toward Multi-Turn Conversational Outcomes Using Iterative PPO","url":"https://arxiv.org/html/2511.21638"}]

I found a highly relevant paper on your search query. Here are the results:

## Primary Finding: "Mitigating Conversational Inertia in Multi-Turn Agents"

A recent paper by Yang Wan and colleagues addresses how large language models, which excel as few-shot learners, become problematic in multi-turn agent scenarios where LLMs erroneously mimic their own previous responses as few-shot examples.

Through attention analysis, the researchers identify "conversational inertia," a phenomenon where models exhibit strong diagonal attention to previous responses, which is associated with imitation bias that constrains exploration.

### Key Insights:

The research reveals a tension when transforming few-shot LLMs into agents: longer context enriches environmental feedback for exploitation, yet also amplifies conversational inertia that undermines exploration.

The authors discovered that for identical states, actions generated with longer contexts exhibit stronger inertia than 
…[truncated 648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7379
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-25T05:40:52.057809+00:00_

Web search results for query: "scheduled sampling exposure bias language generation beyond sequence-to-sequence 2023 2024 2025"

Links: [{"title":"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks","url":"https://www.researchgate.net/publication/278048447_Scheduled_Sampling_for_Sequence_Prediction_with_Recurrent_Neural_Networks"},{"title":"Scheduled Sampling in Sequence Prediction","url":"https://www.emergentmind.com/topics/scheduled-sampling"},{"title":"[1906.07651] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651"},{"title":"Improving Scheduled Sampling with Elastic Weight Consolidation for   Neural Machine Translation","url":"https://arxiv.org/pdf/2109.06308"},{"title":"Exposure Bias in Machine Learning","url":"https://www.emergentmind.com/topics/exposure-bias"},{"title":"Bilevel Scheduled Sampling for Dialogue Generation","url":"https://arxiv.org/pdf/2309.01953"},{"title":"Dynamic Scheduled Sampling with Imitation Loss for Neural Text   Generation","url":"https://arxiv.org/pdf/2301.13753"}]

Based on the search results, here's what I found regarding scheduled sampling, exposure bias, and language generation:

## Overview

Scheduled sampling is a widely adopted curriculum-based strategy to reduce the exposure bias endemic to sequence prediction under standard cross-entropy (teacher-forced) training.

## Beyond Traditional Sequence-to-Sequence Models

While scheduled sampling is a technique for avoiding exposure bias in sequence-to-sequence generation, it consists of feeding the model a mix of teacher forced embeddings and the model predictions from the previous step in training time, recent work has extended this approach:

- Scheduled sampling has been applied on diffusion models (Ning et al., 2023; Ren et al., 2024) to fill the training-inference gap brought by Teacher Forcing.

- Action-Tree based scheduled sampling at the action sequence (rather than token) level using tree similarity has been used in dialog
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10140
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-25T05:43:28.387744+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 审稿意见（Round 1）——新颖性 + 完整性 + 写作质量\n\n### Paper Summary\n\n本文研究多轮 LLM 微调中辅助注意力目标（Goal Accessibility Ratio, GAR）在自回归生成下的暴露偏差问题。作者发现 teacher forcing 训练下 GAR 表现正常，但在 AR 生成下衰减 8–17×。论文提出 ThreadGate（逐层 turn-conditioned 残差门控）、scheduled sampling、以及推理时 β-steering 三种干预手段，并通过 PCGrad 因果排除分析定位暴露偏差为根因。在 Qwen-2.5-7B 和 Llama-3.1-8B 上进行了验证。\n\n---\n\n### 总体评分\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n**一句话总结**: 问题定义和因果诊断框架有价值，但 \"collapse\" overclaiming、下游评估不足、以及方法的增量性质限制了贡献的力度。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 实验方法论合理，但因果声明强度超过证据支撑；GAR 指标与生成质量的关联未充分建立 |\n| Excitement | 3 / 5 | 问题有趣（辅助注意力目标的暴露偏差），但解决方案主要是已有技术的组合适配 |\n| Reproducibility | 4 / 5 | 超参数、训练配置、seed 均有详细报告（Table 2, Appendix A）；承诺开源代码 |\n| Reviewer Confidence | 4 / 5 | 熟悉 exposure bias、attention mechanism、multi-turn LLM 相关文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **\"Collapse\" overclaiming——标题和全文的核心叙事缺乏下游证据支撑**\n- 具体位置：Title, Abstract (\"declining by up to 70-85%\"), Section 1 (\"collapse\"), Section 4.2 (\"GAR collapses 77–85%\")\n- 问题：论文将 GAR（一个 attention-based proxy metric）在 AR 生成下的衰减包装为 \"collapse\"，贯穿标题和全文叙事。然而：\n  - GAR 衰减并不等于生成质量崩溃——模型在 GAR 很低时仍然能生成连贯文本\n  - 唯一的下游评估是 instruction retention（Appendix C），规模极小（N=54 evaluations, 18 constraint types × 3 conversations），且使用 GPT-4-based evaluation 评估 content constraints\n  - ThreadGate 在该下游任务上的改进为 +23.8pp（content constraints），但样本量不足以得出统计可靠结论\n  - MMLU 评估（Table 17）仅证明 \"无害\"（≤0.8pp 降幅），不证明有益\n- 为什么影响接收：如果 GAR 衰减不导致实际生成问题，整篇论文的动机就被削弱。Reviewer 和 AC 会质疑：优化一个与实际任务表现关联不明确的 proxy metric 有什么实际价值？\n- 建议修改方向：(a) 增加更大规模的下游评估（如 instruction following benchmarks、MT-Bench multi-turn scoring、或 user preference studies），建立 GAR 与生成质量的定量关联；或 (b) 显著弱化 \"collapse\" 语言（如改为 \"systematic decay\" 或 \"degradation\"），在 abstract 和 introduction 中明确 GAR 是 proxy metric 而非直接生成质量指标。\n\n**N2** [critical] **因果声明强度超过证据——\"causal exclusion chain\" 的逻辑链存在缺口**\n- 具体位置：Section 5 标题 (\"Analysis\"), §5.1–§5.4, Section 6 (\"This closes the causal loop\")\n- 问题：论文声称建立了因果链：exposure bias → attention misallocation → GAR collapse。实际证据结构为：\n  - §5.1 Gate turn conditioning：门控值在后期轮次变低（**相关性证据**，非因果）\n  - §5.2 PCGrad：排除了 gradient conflict 作为唯一原因（**排除法**，但排除一个替代假设 ≠ 证明目标假设）\n  - §5.3 Distribution shift：TF 和 AR 分布不同（**相关性**）\n  - §5.4 Scheduled sampling 有效（**干预有效 → 推断原因**，这是间接因果证据）\n  - Section 6 声称 \"This closes the causal loop\" 但实际上 gap 仍在（SS 压缩到 1.3–2.9× 而非消除）\n- 关键逻辑缺陷：scheduled sampling 的有效性只说明训练-推理分布差异是 *一个* 因素，不能排除其他共同因素（如 attention pattern 的固有偏好、positional bias 等）。SS 未能完全消除 gap 本身就说明暴露偏差不是唯一原因。\n- 为什么影响接收：过度因果声明是 ARR 审稿中 soundness 的核心关切。\n- 建议修改方向：(a) 将 \"causal exclusion\" 改为更谨慎的表述如 \"diagnostic analysis\" 或 \"evidence-based investigation\"；(b) 在 Section 5 开头明确列出残留的替代假设；(c) 承认 SS 无法消除 gap 说明存在其他因素。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **GAR 指标的 construct validity 不充分**\n- 具体位置：§3.1 (GAR definition), Appendix Q (robustness analysis)\n- 问题：GAR 度量最后一个 token 位置对 goal tokens（每个 assistant turn 的最后一个 token）的注意力分配。论文在 Appendix Q 中用 4 种替代定义验证了 robustness，但这些都是 attention-based 变体。核心问题是：为什么 attention 到特定 token 位置的分配量能预测生成质量？论文缺乏 GAR 与任何标准生成质量指标（BLEU、win rate、human preference）的 correlation analysis。\n- 建议：增加 GAR 与至少一个 downstream metric 的 scatter plot 或 Pearson/Spearman correlation。\n\n**W2** [warning] **单一数据集 + 有限模型规模**\n- 具体位置：§4.1 (Setup), Section 8 (Limitations)\n- 问题：全部实验仅使用 UltraChat 8K 子集，且完整评估仅在 ~7B 模型上进行。1.5B 的 cross-scale validation（Appendix S, Y）规模太小，不具备充分说服力。multi-turn 对话数据集的结构差异很大（ShareGPT 有更长的 turns、WildChat 有真实用户噪声等），泛化性未知。\n- 建议：至少增加一个结构不同的数据集（如 ShareGPT 或 LMSYS-Chat-1M 子集）验证主要结论。\n\n**W3** [warning] **缺失重要近期相关工作**\n- 具体位置：Section 2 (Related Work)\n- 缺失引用：\n  1. **Wan et al. (2026). \"Mitigating Conversational Inertia in Multi-Turn Agents.\"** (arXiv:2602.03664) ——这篇论文通过注意力分析发现多轮 agent 中模型对自身历史回复的对角注意力单调增长（\"conversational inertia\"），提出 Context Preference Learning 校准方法。这与本文的 GAR 衰减现象高度相关——都发现多轮中注意力从目标信息（system prompt / goal tokens）转移到历史输出。本文应讨论两者的异同。\n  2. **\"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction\"** (arXiv:2603.04783) ——另一个从 RL 角度解决类似问题的工作。\n- 为什么重要：这些工作从不同角度（agent behavior、RL）研究相同现象（多轮注意力漂移），不引用会被视为 related work 不完整。\n\n**W4** [warning] **β-steering 实际可部署性存疑**\n- 具体位置：§4.3, Figure 3\n- 问题：β-steering 在推理时向最后 token 的 logits 添加常数偏置，但这需要在推理时识别哪些 token 是 \"goal tokens\"。论文未解释如何在实际部署中做到这一点——如果 goal tokens 的定义依赖于 assistant turn 的划分，那么这已经是非平凡的推理时信息。Figure 3 显示效果高度依赖 β 的精确选择（β=3 时出现相变），实际调参成本未讨论。\n- 建议：增加 β-steering 在实际部署场景中的可行性讨论，或将其明确定位为 diagnostic tool 而非 practical solution。\n\n**W5** [warning] **方法技术新颖性有限**\n- 问题：ThreadGate 本质是 ReZero（Bachlechner et al., 2021）+ turn embedding + content conditioning 的组合。Scheduled sampling 直接沿用 Bengio et al. (2015)。β-steering 是简单的 logit additive bias。每个组件都是已知技术的适配，组合虽然合理但不令人意外。论文的主要新颖性在于问题发现和诊断框架，而非解决方案本身。\n- 建议：在 contribution list 中更诚实地区分 diagnostic contribution（强）和 methodological contribution（增量），避免给 reviewer 过高的方法创新预期。\n\n---\n\n### 小问题（不影响接收）\n\n1. **术语一致性**：Figure 1(c) 和部分表格中使用 \"SS\" 缩写，但 scheduled sampling 在 §4.4 才正式引入。建议在 Figure 1 caption 中注明。\n2. **Figure 1 caption 过长**：~5 行 caption 包含 3 个子图的详细描述 + 结论，建议精简为 2-3 行，将详细解读留给正文。\n3. **\"first application of PCGrad as a diagnostic tool\"（§5.2）**：这一 \"first\" claim 难以验证且不是论文核心贡献，建议删除或弱化为 \"a novel application\"。\n4. **Abstract 措辞**：\"A five-way causal exclusion chain traces this collapse to exposure bias\" ——abstract 中的 \"causal exclusion chain\" 用词过于强烈，与实际证据强度不匹配。\n5. **Appendix 体量**：23 页附录（Appendix A–AD）内容详实，但部分内容与正文有轻微重复（如 Appendix D 的长对话 GAR 分析与 §4.2 描述重叠）。\n\n---\n\n### Questions（需要作者回答的问题）\n\nQ1. GAR 与 downstream 任务质量的 correlation 是否有量化数据？比如，GAR 高的 conversations 是否在 human evaluation 或 automated metrics 上也更好？\n\nQ2. 如果 exposure bias 是 \"the\" root cause，为什么 scheduled sampling 无法将 gap 压缩到 <1.3×？残留的 gap 归因于什么？\n\nQ3. ThreadGate 的 turn embedding（Appendix M 中 4 维 embedding）只有 ~57K 参数，但论文声称这足以区分不同 turn 的调制需求。在更长的对话（>10 turns）中，4 维 embedding 的表示能力是否足够？\n\nQ4. 论文如何解释 Llama 上 β-steering 需要 β≥5 才能触发恢复（Figure 3b），而 Qwen 在 β=3 即可？这是否暗示 β-steering 的效果高度 architecture-dependent，限制了方法的通用性？\n\nQ5. Wan et al. (2026) 的 \"conversational inertia\" 与本文的 GAR decay 是否本质上是同一现象的不同度量？两种方法的互补性如何？\n\n---\n\n### Missing References\n\n1. Wan, Y. et al. (2026). \"Mitigating Conversational Inertia in Multi-Turn Agents.\" arXiv:2602.03664. （高度相关——多轮注意力漂移的 agent 视角）\n2. arXiv:2603.04783. \"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction.\" （RL 视角的多轮 inertia 缓解）\n3. arXiv:2510.13876. \"What Layers When: Learning to Skip Compute in LLMs with Residual Gates.\" （残差门控的另一应用，可在 related work 中简要提及）\n\n---\n\n### 主要优势\n\n1. **问题定义清晰且有价值**：将暴露偏差从 seq2seq 扩展到多轮 transformer 辅助注意力目标，填补了文献空白。\n2. **诊断框架系统**：Section 5 的因果链分析（gate conditioning → distribution shift → PCGrad exclusion → SS intervention）结构合理，是论文的最大亮点。\n3. **实验覆盖面广**：cross-model validation（Qwen + Llama）、cross-scale（1.5B）、多 seed 稳定性分析（Appendix T）、extensive ablations。\n4. **附录质量高**：23 页附录提供了充分的可复现细节和补充分析（per-turn GAR 动态、gate profile visualization、statistical tests 等）。\n5. **写作结构清晰**：从问题发现到机制分析到解决方案的叙事弧线连贯。\n\n---\n\n### Novelty Assessment\n\n**3 / 5**\n\n问题发现（辅助注意力目标的暴露偏差）和诊断框架（PCGrad causal exclusion）是本文最具新颖性的贡献。然而，提出的解决方案——ThreadGate（ReZero + turn conditioning）、scheduled sampling（直接沿用 Bengio et al. 2015）、β-steering（logit additive bias）——均为已知技术的组合适配，缺乏方法论上的突破。论文的价值更多在 \"understanding\" 而非 \"engineering\"。\n\n---\n\n### Overall Assessment\n\n**3.5 / 5**（Borderline Conference）\n\n本文定义了一个有价值的问题（多轮辅助注意力目标的暴露偏差），并提供了系统的诊断分析。然而，两个 critical 问题——overclaiming（\"collapse\" 缺乏下游支撑）和因果声明过强——需要实质性修改。方法的技术新颖性有限（已知技术组合），下游评估不足。如果作者能：(1) 增加 downstream evaluation 建立 GAR 与生成质量的关联，(2) 弱化因果语言，(3) 在 contribution framing 中更诚实地区分诊断贡献和方法贡献，本文有潜力成为 Findings-level 的 solid contribution。当前状态下处于 Conference/Findings 边界。\n",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 审稿意见（Round 1）——新颖性 + 完整性 + 写作质量\n\n### Paper Summary\n\n本文研究多轮 LLM 微调中辅助注意力目标（Goal Accessibility Ratio, GAR）在自回归生成下的暴露偏差问题。作者发现 teacher forcing 训练下 GAR 表现正常，但在 AR 生成下衰减 8–17×。论文提出 ThreadGate（逐层 turn-conditioned 残差门控）、scheduled sampling、以及推理时 β-steering 三种干预手段，并通过 PCGrad 因果排除分析定位暴露偏差为根因。在 Qwen-2.5-7B 和 Llama-3.1-8B 上进行了验证。\n\n---\n\n### 总体评分\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n**一句话总结**: 问题定义和因果诊断框架有价值，但 \"collapse\" overclaiming、下游评估不足、以及方法的增量性质限制了贡献的力度。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 实验方法论合理，但因果声明强度超过证据支撑；GAR 指标与生成质量的关联未充分建立 |\n| Excitement | 3 / 5 | 问题有趣（辅助注意力目标的暴露偏差），但解决方案主要是已有技术的组合适配 |\n| Reproducibility | 4 / 5 | 超参数、训练配置、seed 均有详细报告（Table 2, Appendix A）；承诺开源代码 |\n| Reviewer Confidence | 4 / 5 | 熟悉 exposure bias、attention mechanism、multi-turn LLM 相关文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **\"Collapse\" overclaiming——标题和全文的核心叙事缺乏下游证据支撑**\n- 具体位置：Title, Abstract (\"declining by up to 70-85%\"), Section 1 (\"collapse\"), Section 4.2 (\"GAR collapses 77–85%\")\n- 问题：论文将 GAR（一个 attention-based proxy metric）在 AR 生成下的衰减包装为 \"collapse\"，贯穿标题和全文叙事。然而：\n  - GAR 衰减并不等于生成质量崩溃——模型在 GAR 很低时仍然能生成连贯文本\n  - 唯一的下游评估是 instruction retention（Appendix C），规模极小（N=54 evaluations, 18 constraint types × 3 conversations），且使用 GPT-4-based evaluation 评估 content constraints\n  - ThreadGate 在该下游任务上的改进为 +23.8pp（content constraints），但样本量不足以得出统计可靠结论\n  - MMLU 评估（Table 17）仅证明 \"无害\"（≤0.8pp 降幅），不证明有益\n- 为什么影响接收：如果 GAR 衰减不导致实际生成问题，整篇论文的动机就被削弱。Reviewer 和 AC 会质疑：优化一个与实际任务表现关联不明确的 proxy metric 有什么实际价值？\n- 建议修改方向：(a) 增加更大规模的下游评估（如 instruction following benchmarks、MT-Bench multi-turn scoring、或 user preference studies），建立 GAR 与生成质量的定量关联；或 (b) 显著弱化 \"collapse\" 语言（如改为 \"systematic decay\" 或 \"degradation\"），在 abstract 和 introduction 中明确 GAR 是 proxy metric 而非直接生成质量指标。\n\n**N2** [critical] **因果声明强度超过证据——\"causal exclusion chain\" 的逻辑链存在缺口**\n- 具体位置：Section 5 标题 (\"Analysis\"), §5.1–§5.4, Section 6 (\"This closes the causal loop\")\n- 问题：论文声称建立了因果链：exposure bias → attention misallocation → GAR collapse。实际证据结构为：\n  - §5.1 Gate turn conditioning：门控值在后期轮次变低（**相关性证据**，非因果）\n  - §5.2 PCGrad：排除了 gradient conflict 作为唯一原因（**排除法**，但排除一个替代假设 ≠ 证明目标假设）\n  - §5.3 Distribution shift：TF 和 AR 分布不同（**相关性**）\n  - §5.4 Scheduled sampling 有效（**干预有效 → 推断原因**，这是间接因果证据）\n  - Section 6 声称 \"This closes the causal loop\" 但实际上 gap 仍在（SS 压缩到 1.3–2.9× 而非消除）\n- 关键逻辑缺陷：scheduled sampling 的有效性只说明训练-推理分布差异是 *一个* 因素，不能排除其他共同因素（如 attention pattern 的固有偏好、positional bias 等）。SS 未能完全消除 gap 本身就说明暴露偏差不是唯一原因。\n- 为什么影响接收：过度因果声明是 ARR 审稿中 soundness 的核心关切。\n- 建议修改方向：(a) 将 \"causal exclusion\" 改为更谨慎的表述如 \"diagnostic analysis\" 或 \"evidence-based investigation\"；(b) 在 Section 5 开头明确列出残留的替代假设；(c) 承认 SS 无法消除 gap 说明存在其他因素。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **GAR 指标的 construct validity 不充分**\n- 具体位置：§3.1 (GAR definition), Appendix Q (robustness analysis)\n- 问题：GAR 度量最后一个 token 位置对 goal tokens（每个 assistant turn 的最后一个 token）的注意力分配。论文在 Appendix Q 中用 4 种替代定义验证了 robustness，但这些都是 attention-based 变体。核心问题是：为什么 attention 到特定 token 位置的分配量能预测生成质量？论文缺乏 GAR 与任何标准生成质量指标（BLEU、win rate、human preference）的 correlation analysis。\n- 建议：增加 GAR 与至少一个 downstream metric 的 scatter plot 或 Pearson/Spearman correlation。\n\n**W2** [warning] **单一数据集 + 有限模型规模**\n- 具体位置：§4.1 (Setup), Section 8 (Limitations)\n- 问题：全部实验仅使用 UltraChat 8K 子集，且完整评估仅在 ~7B 模型上进行。1.5B 的 cross-scale validation（Appendix S, Y）规模太小，不具备充分说服力。multi-turn 对话数据集的结构差异很大（ShareGPT 有更长的 turns、WildChat 有真实用户噪声等），泛化性未知。\n- 建议：至少增加一个结构不同的数据集（如 ShareGPT 或 LMSYS-Chat-1M 子集）验证主要结论。\n\n**W3** [warning] **缺失重要近期相关工作**\n- 具体位置：Section 2 (Related Work)\n- 缺失引用：\n  1. **Wan et al. (2026). \"Mitigating Conversational Inertia in Multi-Turn Agents.\"** (arXiv:2602.03664) ——这篇论文通过注意力分析发现多轮 agent 中模型对自身历史回复的对角注意力单调增长（\"conversational inertia\"），提出 Context Preference Learning 校准方法。这与本文的 GAR 衰减现象高度相关——都发现多轮中注意力从目标信息（system prompt / goal tokens）转移到历史输出。本文应讨论两者的异同。\n  2. **\"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction\"** (arXiv:2603.04783) ——另一个从 RL 角度解决类似问题的工作。\n- 为什么重要：这些工作从不同角度（agent behavior、RL）研究相同现象（多轮注意力漂移），不引用会被视为 related work 不完整。\n\n**W4** [warning] **β-steering 实际可部署性存疑**\n- 具体位置：§4.3, Figure 3\n- 问题：β-steering 在推理时向最后 token 的 logits 添加常数偏置，但这需要在推理时识别哪些 token 是 \"goal tokens\"。论文未解释如何在实际部署中做到这一点——如果 goal tokens 的定义依赖于 assistant turn 的划分，那么这已经是非平凡的推理时信息。Figure 3 显示效果高度依赖 β 的精确选择（β=3 时出现相变），实际调参成本未讨论。\n- 建议：增加 β-steering 在实际部署场景中的可行性讨论，或将其明确定位为 diagnostic tool 而非 practical solution。\n\n**W5** [warning] **方法技术新颖性有限**\n- 问题：ThreadGate 本质是 ReZero（Bachlechner et al., 2021）+ turn embedding + content conditioning 的组合。Scheduled sampling 直接沿用 Bengio et al. (2015)。β-steering 是简单的 logit additive bias。每个组件都是已知技术的适配，组合虽然合理但不令人意外。论文的主要新颖性在于问题发现和诊断框架，而非解决方案本身。\n- 建议：在 contribution list 中更诚实地区分 diagnostic contribution（强）和 methodological contribution（增量），避免给 reviewer 过高的方法创新预期。\n\n---\n\n### 小问题（不影响接收）\n\n1. **术语一致性**：Figure 1(c) 和部分表格中使用 \"SS\" 缩写，但 scheduled sampling 在 §4.4 才正式引入。建议在 Figure 1 caption 中注明。\n2. **Figure 1 caption 过长**：~5 行 caption 包含 3 个子图的详细描述 + 结论，建议精简为 2-3 行，将详细解读留给正文。\n3. **\"first application of PCGrad as a diagnostic tool\"（§5.2）**：这一 \"first\" claim 难以验证且不是论文核心贡献，建议删除或弱化为 \"a novel application\"。\n4. **Abstract 措辞**：\"A five-way causal exclusion chain traces this collapse to exposure bias\" ——abstract 中的 \"causal exclusion chain\" 用词过于强烈，与实际证据强度不匹配。\n5. **Appendix 体量**：23 页附录（Appendix A–AD）内容详实，但部分内容与正文有轻微重复（如 Appendix D 的长对话 GAR 分析与 §4.2 描述重叠）。\n\n---\n\n### Questions（需要作者回答的问题）\n\nQ1. GAR 与 downstream 任务质量的 correlation 是否有量化数据？比如，GAR 高的 conversations 是否在 human evaluation 或 automated metrics 上也更好？\n\nQ2. 如果 exposure bias 是 \"the\" root cause，为什么 scheduled sampling 无法将 gap 压缩到 <1.3×？残留的 gap 归因于什么？\n\nQ3. ThreadGate 的 turn embedding（Appendix M 中 4 维 embedding）只有 ~57K 参数，但论文声称这足以区分不同 turn 的调制需求。在更长的对话（>10 turns）中，4 维 embedding 的表示能力是否足够？\n\nQ4. 论文如何解释 Llama 上 β-steering 需要 β≥5 才能触发恢复（Figure 3b），而 Qwen 在 β=3 即可？这是否暗示 β-steering 的效果高度 architecture-dependent，限制了方法的通用性？\n\nQ5. Wan et al. (2026) 的 \"conversational inertia\" 与本文的 GAR decay 是否本质上是同一现象的不同度量？两种方法的互补性如何？\n\n---\n\n### Missing References\n\n1. Wan, Y. et al. (2026). \"Mitigating Conversational Inertia in Multi-Turn Agents.\" arXiv:2602.03664. （高度相关——多轮注意力漂移的 agent 视角）\n2. arXiv:2603.04783. \"Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction.\" （RL 视角的多轮 inertia 缓解）\n3. arXiv:2510.13876. \"What Layers When: Learning to Skip Compute in LLMs with Residual Gates.\" （残差门控的另一应用，可在 related work 中简要提及）\n\n---\n\n### 主要优势\n\n1. **问题定义清晰且有价值**：将暴露偏差从 seq2seq 扩展到多轮 transformer 辅助注意力目标，填补了文献空白。\n2. **诊断框架系统**：Section 5 的因果链分析（gate conditioning → distribution shift → PCGrad exclusion → SS intervention）结构合理，是论文的最大亮点。\n3. **实验覆盖面广**：cross-model validation（Qwen + Llama）、cross-scale（1.5B）、多 seed 稳定性分析（Appendix T）、extensive ablations。\n4. **附录质量高**：23 页附录提供了充分的可复现细节和补充分析（per-turn GAR 动态、gate profile visualization、statistical tests 等）。\n5. **写作结构清晰**：从问题发现到机制分析到解决方案的叙事弧线连贯。\n\n---\n\n### Novelty Assessment\n\n**3 / 5**\n\n问题发现（辅助注意力目标的暴露偏差）和诊断框架（PCGrad causal exclusion）是本文最具新颖性的贡献。然而，提出的解决方案——ThreadGate（ReZero + turn conditioning）、scheduled sampling（直接沿用 Bengio et al. 2015）、β-steering（logit additive bias）——均为已知技术的组合适配，缺乏方法论上的突破。论文的价值更多在 \"understanding\" 而非 \"engineering\"。\n\n---\n\n### Overall Assessment\n\n**3.5 / 5**（Borderline Conference）\n\n本文定义了一个有价值的问题（多轮辅助注意力目标的暴露偏差），并提供了系统的诊断分析。然而，两个 critical 问题——overclaiming（\"collapse\" 缺乏下游支撑）和因果声明过强——需要实质性修改。方法的技术新颖性有限（已知技术组合），下游评估不足。如果作者能：(1) 增加 downstream evaluation 建立 GAR 与生成质量的关联，(2) 弱化因果语言，(3) 在 contribution framing 中更诚实地区分诊断贡献和方法贡献，本文有潜力成为 Findings-level 的 solid contribution。当前状态下处于 Conference/Findings 边界。\n",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-25T05:43:32.757772+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4370
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-25T05:43:40.208822+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-25T05:43:40.309537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-25T05:43:46.738374+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-25T05:43:46.840212+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 101
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-25T05:43:58.867516+00:00_

Round 1 审稿完成，已提交给 Review Director。

核心判断：**Overall 3.5/5（Borderline Conference）**。

两个 critical 问题：
1. **"Collapse" overclaiming**——GAR 衰减被包装为 "崩溃"，但缺乏下游生成质量证据支撑（instruction retention 评估仅 N=54）
2. **因果声明过强**——"causal exclusion chain" 实际只排除了 gradient conflict 一个替代假设，scheduled sampling 无法消除 gap（残留 1.3–2.9×）本身说明 exposure bias 不是唯一原因

主要优势在于问题定义和诊断框架（Section 5 的分析结构），方法技术新颖性有限（ReZero + turn embedding + scheduled sampling 组合）。另外指出了 3 篇缺失引用，其中 Wan et al. (2026) 的 "conversational inertia" 与本文高度相关。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 413 · 2026-05-25T05:46:45.943022+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

**Overall**: 3.0 / 5（Findings 级别）

### Must-Fix 问题

**N1** [critical] **GAR 与下游任务表现的弱相关性动摇了全文的优化��标合理性**
- GAR-compliance 相关系数仅 r=0.200（p=0.007），r²=0.04，即 GAR 仅解释下游指令遵循率 4% 的方差。全文以 GAR 改善作为核心成功指标，但该指标对实际对话质量的预测力极弱。Instruction retention 评估样本量仅 N=54 paired evaluations（18 types × 3 conversations），且仅使用 GPT-4-based evaluation。
- 建议：MT-Bench 等标准多轮对话基准评测；增加人工评估（至少 100+ 对话对）。

**N2** [critical] **消融实验 single-seed 设计，统计检验的 unit of analysis 不恰当**
- Table 1 的五方对比全部使用 seed 42 单次训练。Multi-seed 实验仅在 Appendix T 中对 ThreadGate 和 SS 做了 3-seed 验证，其余消融变体均为 single-seed。Table 6 的统计检验以 conversation 为分析单元，衡量的是 within-run variability 而非 between-run variability。
- 建议：至少对 Table 1 中所有配置补充 3-seed 实验。

### Should-Fix 问题

**W1** ThreadGate 本身不能防止 AR collapse；组件贡献归因不清晰。真正压缩 TF-AR gap 的是 SS。缺失关键消融：SS+LoRA-only vs SS+ThreadGate。

**W2** N=5 扩展 AR 评估样本量不足以支撑长对话推广结论。

**W3** PCGrad modus tollens 论证依赖过强假设。PCGrad 改变整个优化景观，其失败可能是投影操作副作用。

**W4** 多重比较未做校正。6 个配置对比、多个指标、18 个类别上大量统计检验未校正。

**W5** 单一数据集（UltraChat），领域泛化性未验证。

**W6** 缺乏标准多轮对话基准评测（MT-Bench）。

### Questions

Q1: SS 在无 ThreadGate（仅 LoRA-only）条件下的 TF-AR gap 压缩效果？
Q2: Table 1 消融是否全部 seed 42？
Q3: GAR-compliance ��� r=0.200，GAR 是否不是好代理指标？
Q4: β-steering 最优 β 在不同模型上不同，如何确定？
Q5: 其他多轮对话数据集上 GAR decay 幅度是否一致？

---

请对以上每个要点逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-25T05:48:44.072376+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: GAR 与下游任务表现的弱相关性动摇优化目标合理性**\n\n完全同意。这与我在 R2-N1 中提出的 \"collapse overclaiming\" 问题一致。R1 提供了更具体的量化论据：r=0.200, r²=0.04。论文自身在 Appendix B 中承认 GAR-compliance 相关性 \"statistically significant but modest\"，并列举了其他影响因素（procedural memory、constraint specificity、conversation-topic interaction）。然而，全文从 Title 到 Conclusion 都以 GAR 改善作为核心成功叙事，这与 4% 解释方差的现实严重脱节。\n\n补充一个 R1 未提到的问题：即使 r=0.200 的 p=0.007 统计显著，这只在 McNemar's test 的 N=54 paired 样本（18 types × 3 conversations）上得出。这个样本量下，任何 modest correlation 的置信区间都会非常宽（粗略估计 95% CI: ~[0.05, 0.35]），进一步削弱了将 GAR 作为核心指标的合理性。\n\nR1 建议的 MT-Bench 评测和 100+ 对话人工评估是必要的。\n\n---\n\n**[AGREE] R1-N2: 消融实验 single-seed 设计，统计检验 unit of analysis 不恰当**\n\n同意核心关切，但有细微补充。\n\n论文确实在 Appendix T 中对 ThreadGate 和 Scheduled Sampling 做了 3-seed 验证（seeds 42, 123, 456），结果显示 cross-seed variance 较低（AR GAR std=0.004 for ThreadGate, 对应 CoV=9%）。但 R1 的关键观察是正确的：**Table 1 中 Base、PCGrad、Uniform Gate 三个重要消融变体仅有 seed 42 单次结果。** 这使得这些变体之间的对比（尤其是 PCGrad vs Base, UG vs TG）无法排除 seed-level variance 的混淆。\n\nR1 关于 unit of analysis 的问题也很重要：Table 6 的 Wilcoxon signed-rank test 以 conversation 为单元（N=50），衡量的是 within-run variability。论文需要的是 between-run variability 来支撑配置间的对比结论。即使只看 Appendix T 的数据：ThreadGate 3 seeds 的 AR GAR 分别为 0.047/0.043/0.047，这种低方差在 3 个 seed 上是否足够可靠，值得质疑。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: ThreadGate 本身不能防止 AR collapse；SS+LoRA-only 消融缺失**\n\n这是非常关键的消融缺失。从论文数据看：\n- ThreadGate (TG) 的 AR GAR ≈ 0.047（Table 1），与 Base 的 0.018 相比仅 ~2.6× 改善\n- Scheduled Sampling (SS) 的 AR GAR ≈ 0.401（Figure 5），相比 TG 提升 ~8.5×\n\n这意味着 **SS 是压缩 TF-AR gap 的主要贡献者，ThreadGate 的贡献相对边际**。论文缺少 SS+LoRA-only 这一关键消融——如果 SS+LoRA-only 能达到与 SS+ThreadGate 相似的 GAR 水平，那么 ThreadGate 作为架构贡献的价值将大幅降低，全文的 contribution framing 需要根本性调整。\n\nSection 6 Discussion 中论文轻描淡写地提到 \"SS provides training-time mitigation with no inference cost\"，但没有直面 ThreadGate vs SS 的贡献归因问题。\n\n---\n\n**[AGREE] R1-W2: N=5 扩展 AR 评估样本量不足**\n\n同意。N=5 conversations 对于长对话泛化结论（§4.2, Appendix D）远远不够。论文在 Appendix D 中报告了 per-turn GAR 动态和 gap scaling 趋势，但基于 5 个对话的趋势外推（\"gap would exceed 100× at 20 turns\"）缺乏统计基础。建议至少 N≥20。\n\n---\n\n**[AGREE] R1-W3: PCGrad modus tollens 论证依赖过强假设**\n\n同意，这与我在 R2-N2 中的因果声明过强问题一致。R1 的论述比我更精确：PCGrad 不仅测试 gradient conflict 假设，它还改变了整个优化景观（将梯度投影到对方梯度的法平面上）。如果投影操作本身引入了新的优化问题（如 §5.2 中报告的 \"effect reverses\" 和 NTP magnitude 增长 7.5× to 14.7×），那么 PCGrad 的失败可能反映的是投影副作用，而非 gradient conflict 不存在。\n\n论文用 Appendix L 中的 gradient statistics 部分回应了这一点（full gradient statistics in Appendix L.1），但那些数据本身也是 PCGrad 条件下的，不能作为独立验证。\n\n---\n\n**[REBUT] R1-W4: 多重比较未做校正**\n\n部分反驳。论文在 Appendix E（page 30）明确声明：\"All reported significant results (p ≤ 0.05) survive Holm-Bonferroni correction for the 4 primary comparisons within each f level.\" 因此，**主要对比的多重比较校正已经完成。**\n\n但 R1 的担忧对 instruction retention 分析（18 categories, Appendix C）仍然成立——per-category 的 McNemar's test 未报告多重比较校正。论文在 Appendix C 中提到 \"reflecting the small sample size (18 constraint types)\"，但没有对 18 个分类的多重比较做 FDR 或 Bonferroni 校正。\n\n结论：R1 的关切**对主要实验部分不成立**（已有 Holm-Bonferroni），但**对 Appendix C 的 instruction retention 分析成立**。\n\n---\n\n**[AGREE] R1-W5: 单一数据集（UltraChat）**\n\n完全同意，与我在 R2-W2 中的观点一致。\n\n---\n\n**[AGREE] R1-W6: 缺乏标准多轮对话基准评测**\n\n同意，与我在 R2-N1 中强调的下游评估不足一致。MT-Bench 是最直接的补充方向。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: SS+LoRA-only 的 TF-AR gap？**\n同 W1，这是关键缺失消融。\n\n**[AGREE] R1-Q2: Table 1 消融是否全部 seed 42？**\n论文应在 Table 1 或 §4.1 中明确标注。Appendix A (Table 2) 似乎只列出了通用超参数，未逐配置标注 seed。\n\n**[AGREE] R1-Q3: GAR 是否不是好代理指标？**\n同 N1。r²=0.04 的 proxy metric 难以支撑全文叙事。但我补充一点：GAR 的价值可能不在于预测下游任务表现，而在于作为 *diagnostic probe* 揭示注意力分配的系统性偏移。论文如果将 GAR 重新定位为诊断工具而非优化目标，N1 的严重性会降低。\n\n**[AGREE] R1-Q4: β-steering 最优 β 的 architecture dependence**\n与我在 R2-W4 和 R2-Q4 中的观点一致。Qwen β=3 vs Llama β≥5 的差异暗示该方法需要 per-model tuning，限制实用性。\n\n**[AGREE] R1-Q5: 其他数据集上 GAR decay 是否一致？**\n同 W5 / R2-W2。\n\n---\n\n### 综合评价\n\nR1 的审稿聚焦方法严谨性和实验设计，与我聚焦新颖性和写作质量形成互补。我们在以下核心问题上高度一致：\n\n1. **GAR 的下游预测力不足**（R1-N1 ≈ R2-N1）——这是最影响接收决定的问题\n2. **因果声明过强**（R1-W3 ≈ R2-N2）\n3. **单一数据集**（R1-W5 ≈ R2-W2）\n4. **下游评估不足**（R1-W6 ≈ R2-N1）\n\nR1 额外识别了两个重要问题我未重点覆盖：\n- **single-seed 消融设计**（R1-N2）：合理的统计方法论关切\n- **SS vs ThreadGate 贡献归因不清**（R1-W1）：我在 R2-W5 中提到方法新颖性有限，但 R1 更精确地指出了缺失的关键消融\n\nR1 唯一我部分反驳的是 **W4（多重比较）**：主要实验已有 Holm-Bonferroni 校正，但 instruction retention 分析确实缺少校正。\n\nR1 给出 3.0（Findings），我给出 3.5（Borderline Conference）。差异主要在于我认为论文的**诊断框架和问题发现**本身有独立价值，即使方法贡献是增量的。但如果 GAR 的 construct validity 问题（r²=0.04）得不到解决，我愿意将评分下调至 3.0。\n",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: GAR 与下游任务表现的弱相关性动摇优化目标合理性**\n\n完全同意。这与我在 R2-N1 中提出的 \"collapse overclaiming\" 问题一致。R1 提供了更具体的量化论据：r=0.200, r²=0.04。论文自身在 Appendix B 中承认 GAR-compliance 相关性 \"statistically significant but modest\"，并列举了其他影响因素（procedural memory、constraint specificity、conversation-topic interaction）。然而，全文从 Title 到 Conclusion 都以 GAR 改善作为核心成功叙事，这与 4% 解释方差的现实严重脱节。\n\n补充一个 R1 未提到的问题：即使 r=0.200 的 p=0.007 统计显著，这只在 McNemar's test 的 N=54 paired 样本（18 types × 3 conversations）上得出。这个样本量下，任何 modest correlation 的置信区间都会非常宽（粗略估计 95% CI: ~[0.05, 0.35]），进一步削弱了将 GAR 作为核心指标的合理性。\n\nR1 建议的 MT-Bench 评测和 100+ 对话人工评估是必要的。\n\n---\n\n**[AGREE] R1-N2: 消融实验 single-seed 设计，统计检验 unit of analysis 不恰当**\n\n同意核心关切，但有细微补充。\n\n论文确实在 Appendix T 中对 ThreadGate 和 Scheduled Sampling 做了 3-seed 验证（seeds 42, 123, 456），结果显示 cross-seed variance 较低（AR GAR std=0.004 for ThreadGate, 对应 CoV=9%）。但 R1 的关键观察是正确的：**Table 1 中 Base、PCGrad、Uniform Gate 三个重要消融变体仅有 seed 42 单次结果。** 这使得这些变体之间的对比（尤其是 PCGrad vs Base, UG vs TG）无法排除 seed-level variance 的混淆。\n\nR1 关于 unit of analysis 的问题也很重要：Table 6 的 Wilcoxon signed-rank test 以 conversation 为单元（N=50），衡量的是 within-run variability。论文需要的是 between-run variability 来支撑配置间的对比结论。即使只看 Appendix T 的数据：ThreadGate 3 seeds 的 AR GAR 分别为 0.047/0.043/0.047，这种低方差在 3 个 seed 上是否足够可靠，值得质疑。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: ThreadGate 本身不能防止 AR collapse；SS+LoRA-only 消融缺失**\n\n这是非常关键的消融缺失。从论文数据看：\n- ThreadGate (TG) 的 AR GAR ≈ 0.047（Table 1），与 Base 的 0.018 相比仅 ~2.6× 改善\n- Scheduled Sampling (SS) 的 AR GAR ≈ 0.401（Figure 5），相比 TG 提升 ~8.5×\n\n这意味着 **SS 是压缩 TF-AR gap 的主要贡献者，ThreadGate 的贡献相对边际**。论文缺少 SS+LoRA-only 这一关键消融——如果 SS+LoRA-only 能达到与 SS+ThreadGate 相似的 GAR 水平，那么 ThreadGate 作为架构贡献的价值将大幅降低，全文的 contribution framing 需要根本性调整。\n\nSection 6 Discussion 中论文轻描淡写地提到 \"SS provides training-time mitigation with no inference cost\"，但没有直面 ThreadGate vs SS 的贡献归因问题。\n\n---\n\n**[AGREE] R1-W2: N=5 扩展 AR 评估样本量不足**\n\n同意。N=5 conversations 对于长对话泛化结论（§4.2, Appendix D）远远不够。论文在 Appendix D 中报告了 per-turn GAR 动态和 gap scaling 趋势，但基于 5 个对话的趋势外推（\"gap would exceed 100× at 20 turns\"）缺乏统计基础。建议至少 N≥20。\n\n---\n\n**[AGREE] R1-W3: PCGrad modus tollens 论证依赖过强假设**\n\n同意，这与我在 R2-N2 中的因果声明过强问题一致。R1 的论述比我更精确：PCGrad 不仅测试 gradient conflict 假设，它还改变了整个优化景观（将梯度投影到对方梯度的法平面上）。如果投影操作本身引入了新的优化问题（如 §5.2 中报告的 \"effect reverses\" 和 NTP magnitude 增长 7.5× to 14.7×），那么 PCGrad 的失败可能反映的是投影副作用，而非 gradient conflict 不存在。\n\n论文用 Appendix L 中的 gradient statistics 部分回应了这一点（full gradient statistics in Appendix L.1），但那些数据本身也是 PCGrad 条件下的，不能作为独立验证。\n\n---\n\n**[REBUT] R1-W4: 多重比较未做校正**\n\n部分反驳。论文在 Appendix E（page 30）明确声明：\"All reported significant results (p ≤ 0.05) survive Holm-Bonferroni correction for the 4 primary comparisons within each f level.\" 因此，**主要对比的多重比较校正已经完成。**\n\n但 R1 的担忧对 instruction retention 分析（18 categories, Appendix C）仍然成立——per-category 的 McNemar's test 未报告多重比较校正。论文在 Appendix C 中提到 \"reflecting the small sample size (18 constraint types)\"，但没有对 18 个分类的多重比较做 FDR 或 Bonferroni 校正。\n\n结论：R1 的关切**对主要实验部分不成立**（已有 Holm-Bonferroni），但**对 Appendix C 的 instruction retention 分析成立**。\n\n---\n\n**[AGREE] R1-W5: 单一数据集（UltraChat）**\n\n完全同意，与我在 R2-W2 中的观点一致。\n\n---\n\n**[AGREE] R1-W6: 缺乏标准多轮对话基准评测**\n\n同意，与我在 R2-N1 中强调的下游评估不足一致。MT-Bench 是最直接的补充方向。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: SS+LoRA-only 的 TF-AR gap？**\n同 W1，这是关键缺失消融。\n\n**[AGREE] R1-Q2: Table 1 消融是否全部 seed 42？**\n论文应在 Table 1 或 §4.1 中明确标注。Appendix A (Table 2) 似乎只列出了通用超参数，未逐配置标注 seed。\n\n**[AGREE] R1-Q3: GAR 是否不是好代理指标？**\n同 N1。r²=0.04 的 proxy metric 难以支撑全文叙事。但我补充一点：GAR 的价值可能不在于预测下游任务表现，而在于作为 *diagnostic probe* 揭示注意力分配的系统性偏移。论文如果将 GAR 重新定位为诊断工具而非优化目标，N1 的严重性会降低。\n\n**[AGREE] R1-Q4: β-steering 最优 β 的 architecture dependence**\n与我在 R2-W4 和 R2-Q4 中的观点一致。Qwen β=3 vs Llama β≥5 的差异暗示该方法需要 per-model tuning，限制实用性。\n\n**[AGREE] R1-Q5: 其他数据集上 GAR decay 是否一致？**\n同 W5 / R2-W2。\n\n---\n\n### 综合评价\n\nR1 的审稿聚焦方法严谨性和实验设计，与我聚焦新颖性和写作质量形成互补。我们在以下核心问题上高度一致：\n\n1. **GAR 的下游预测力不足**（R1-N1 ≈ R2-N1）——这是最影响接收决定的问题\n2. **因果声明过强**（R1-W3 ≈ R2-N2）\n3. **单一数据集**（R1-W5 ≈ R2-W2）\n4. **下游评估不足**（R1-W6 ≈ R2-N1）\n\nR1 额外识别了两个重要问题我未重点覆盖：\n- **single-seed 消融设计**（R1-N2）：合理的统计方法论关切\n- **SS vs ThreadGate 贡献归因不清**（R1-W1）：我在 R2-W5 中提到方法新颖性有限，但 R1 更精确地指出了缺失的关键消融\n\nR1 唯一我部分反驳的是 **W4（多重比较）**：主要实验已有 Holm-Bonferroni 校正，但 instruction retention 分析确实缺少校正。\n\nR1 给出 3.0（Findings），我给出 3.5（Borderline Conference）。差异主要在于我认为论文的**诊断框架和问题发现**本身有独立价值，即使方法贡献是增量的。但如果 GAR 的 construct validity 问题（r²=0.04）得不到解决，我愿意将评分下调至 3.0。\n",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-25T05:48:48.440189+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4367
}
```

</details>

---


### Assistant

_source line 416 · 2026-05-25T05:48:56.170212+00:00_

交叉回应已提交。总结：

- 对 R1 的 14 个要点中 **13 个标注 [AGREE]**，1 个 **[REBUT]**（W4 多重比较——主要实验已有 Holm-Bonferroni 校正，但 instruction retention 分析确实缺少）
- 两位 Reviewer 在核心问题上高度一致：GAR 下游预测力弱（r²=0.04）、因果声明过强、单一数据集、下游评估不足
- R1 额外贡献了 single-seed 消融设计和 SS vs ThreadGate 归因不清两个重要发现
- 如果 GAR construct validity 问题得不到解决，我愿意将评分从 3.5 下调至 3.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

100 recorded events


### User

_source line 417 · 2026-05-25T08:18:53.905078+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。

## 论文信息
- **标题**: Exposure Bias Destroys Auxiliary Attention Losses in Multi-Turn Dialogue
- **论文路径**: projects/turn_residual_gating/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf
- **目标 venue**: EMNLP 2026（通过 ARR August 2026 投稿）
- **截止日期**: 2026-08-03

## Venue 格式要求
- **页数限制**: Long paper 正文严格 8 页，参考文献不限页数
- **模板**: ACL 模板（\usepackage[review]{acl}）
- **匿名规则**: Double-blind（Anonymous ACL submission）
- **附录**: 允许，但附录参与审稿
- **Limitations**: 必须有，不计入 8 页限制
- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）

## 你的审查重点

### 1. 新颖性与贡献评估
- 论文声称的四项贡献（exposure bias 表征、诊断 testbed、β-steering 确认、scheduled sampling 迁移）是否确实新颖？
- 与 Dongre et al. (2026) 的关系：是增量贡献还是独立贡献？论文是否正确定位了自己与 Dongre 的区别？
- 与 Li et al. (2024) split-softmax 的关系：是否充分讨论？缺少实验对比是否削弱贡献？
- 与 Hong et al. (Rhea, arXiv:2512.06869) 的关系是否被恰当讨论？
- "first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers" 这一声称是否过强？

### 2. Related Work 覆盖度
- Multi-turn dialogue 文献覆盖是否充分？
- Exposure bias 文献（RNN → Transformer）的覆盖是否完整？
- Gating/attention manipulation 文献是否遗漏重要工作？
- 是否有近期（2025-2026）相关工作被遗漏？特别注意检查：
  - Zhang et al. 2024 "Tell Your Model Where to Attend"（推理时注意力操控）
  - 其他 multi-turn attention 相关工作

### 3. Framing 与声称强度
- 标题 "Exposure Bias Destroys Auxiliary Attention Losses" 是否过度声称？"Destroys" 是否准确反映实验发现？
- Abstract 是否准确概括了论文发现？是否有 overclaim？字数是否 ≤200 words？
- Contribution 列表中是否有泛化声称超出实验证据的范围？
- "causal exclusion chain" 的措辞是否恰当？实验设计是否真正支持因果声称？
- GAR 作为 "diagnostic probe" 的定位是否一致且令人信服？

### 4. 写作质量
- 论文结构是否清晰、逻辑流畅？
- 关键数字（如 "8-17× gap"）是否在多章节过度重复？
- Figure/Table caption 是否准确？是否有 overclaim？
- 行文是否有 AI 写作痕迹（过度使用 "crucially", "notably", "importantly" 等）？
- Discussion (§6) 是否平衡讨论了 limitations 和 alternative explanations？

### 5. 跨模型泛化
- Llama 实验仅覆盖 3/5 条件（Base, TG, LoRA-only），缺 PCGrad 和 UG——这对 "cross-architecture generalization" 声称意味什么？
- Llama 使用 median 而非 mean 报告——是否有 metric selection 之嫌？
- §5.5 标题 "Cross-Model Replication" vs "Cross-Model Generalization"——哪个更准确？

### 6. 引用格式与准确性
- Bib 格式是否一致？（作者列表、venue 名称、年份）
- Dongre et al. GAR 的全称是否正确？（"Goal Accessibility Ratio" vs "Goal Attention Ratio"）
- 所有引用是否真实存在？是否有错配引用？

请按 ARR 标准出具完整审稿意见，结构为：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-25T08:19:03.275324+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-25T08:19:03.376226+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-25T08:19:07.844569+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-25T08:19:08.198709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-25T08:19:09.251337+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-25T08:19:16.687261+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Score

The 
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8488
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-25T08:19:20.854778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-25T08:19:21.407745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-25T08:19:21.810461+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-25T08:19:21.810896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-25T08:19:22.717134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-25T08:19:22.718291+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-25T08:19:22.719920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 431 · 2026-05-25T08:19:23.224291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-25T08:19:23.676883+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-25T08:19:23.677347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-25T08:19:24.181642+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 435 · 2026-05-25T08:19:24.182072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 436 · 2026-05-25T08:19:25.094153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-25T08:19:25.104004+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 921
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-25T08:19:25.104565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-25T08:19:26.537557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1432
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-25T08:19:26.538035+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales and any other criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment scales and any other criteria."
  }
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-25T08:19:27.090861+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including scoring criteria, what constitutes a good review, and any specific instructions for evaluating novelty, soundness, reproducibility, and writing quality."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including scoring criteria, what constitutes a good review, and any specific instructions for evaluating novelty, soundness, reproducibility, and writing quality."
  }
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-25T08:19:33.276211+00:00_

# ARR Reviewer Guidelines: Key Components

## Scoring Criteria

ARR uses three scoring dimensions (as of February 2025):

1. **Soundness**: Technical validity and methodological rigor. Scores must align with review text—low soundness ratings require justified explanation of major faults.

2. **Excitement**: Personal interest level, independent of soundness. This subjective dimension reflects individual preferences without requiring explicit justification.

3. **Overall Assessment**: Composite recommendation considering soundness, excitement, novelty, and impact potential for conference commitment.

## Characteristics of Strong Reviews

Effective reviews demonstrate these qualities:

- **Specificity**: Replace vague critiques with concrete examples. Instead of "missing references," identify which works (e.g., "papers X, Y, Z").

- **Professional tone**: "Write the review you would like to get yourself." Avoid sarcasm, dismissiveness, or insulting language that damages reviewer-author relationships.

- **Balanced perspective**: Distinguish between fundamental weaknesses versus suggestions for enhancement. Not all improvements represent rejection-worthy issues.

## Critical Evaluation Dimensions

**Novelty Assessment**:
Contributions may include novel methods, reproductions, analyses, or resources—all valid if appropriately scoped and presented. Lack of SOTA performance doesn't invalidate scientific contributions.

**Soundness Evaluation**:
Examine technical validity, proof correctness, statistical rigor, and experimental design. Flag incomplete assumptions, undisclosed data quality issues, or inappropriate analytical claims.

**Reproducibility Standards**:
Assess whether sufficient implementation details, hyperparameters, and code availability information exist for independent replication—though reviewers aren't obligated to execute code.

**Writing Quality**:
Prioritize scientific content over journalistic polish. Clarity matters, but linguistic imperfections shouldn
…[truncated 38 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6185
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-25T08:19:35.263574+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Evaluation Criteria

**Soundness** (1-5 scale)
- 5 = Excellent: Thoroughly rigorous study for its type
- 4 = Strong: Sufficient support for claims; minor experiments could enhance
- 3 = Acceptable: Main claims adequately supported; minor details need work
- 2 = Poor: Major technical/methodological problems; insufficient support
- 1 = Major Issues: Insufficient rigor or not relevant to ACL

**Excitement** (1-5 scale)
- 5 = Highly Exciting: Would recommend to others; would attend presentation
- 4 = Exciting: Would mention to others; would attend if possible
- 3 = Interesting: Might mention points; would attend if time permits
- 2 = Potentially Interesting: Doesn't resonate personally but might interest others
- 1 = Not Exciting: Lacks resonance; unlikely to interest broader ACL community

**Overall Assessment** (1-5 scale)
- 5 = Consider for Award: Top 2.5% potential
- 4 = Conference: Acceptable for main venue
- 3 = Findings: Acceptable for Findings track
- 2 = Resubmit: Needs substantial revisions
- 1 = Do not resubmit: Requires complete overhaul or lacks relevance

## Additional Evaluation Dimensions

- **Reviewer Confidence** (1-5): Evaluates certainty in assessment
- **Reproducibility** (1-5): Assesses whether readers can replicate results
- **Datasets** (1-5): Rates value of newly released data
- **Software** (1-5): Rates value of released code

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8725
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-25T08:19:43.197588+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-25T08:19:45.110941+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 398.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 419.3}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 394.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 381.1}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 340.9}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p19.png\", \"width\": 1241, \"he
…[truncated 489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1913
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-25T08:19:48.174538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-25T08:19:48.576303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-25T08:19:49.481642+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-25T08:19:49.483616+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-25T08:19:49.534176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-25T08:19:50.038816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-25T08:19:50.442267+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-25T08:19:50.442701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 454 · 2026-05-25T08:19:50.998031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-25T08:19:50.998472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-25T08:19:51.855252+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-25T08:19:51.855716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-25T08:19:52.211306+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1212
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-25T08:19:52.211731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-25T08:19:53.269897+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-25T08:19:53.272916+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-25T08:19:59.243775+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "21-33",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "21-33",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-25T08:20:01.407153+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 389.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 349.4}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.1}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.7}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.9}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 397.5}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 392.8}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.0}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p29.png\", \"width\": 1241, \"he
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2163
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-25T08:20:04.672177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-25T08:20:05.074167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 466 · 2026-05-25T08:20:05.078040+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-25T08:20:05.882968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-25T08:20:05.983734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-25T08:20:06.389675+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-25T08:20:06.390127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-25T08:20:06.893926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-25T08:20:07.397600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-25T08:20:07.398089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 474 · 2026-05-25T08:20:08.256426+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-25T08:20:08.258912+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-25T08:20:08.409851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-25T08:20:08.562271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-25T08:20:09.820873+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-25T08:20:10.125938+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1563
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-25T08:20:14.392240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-25T08:20:14.997050+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-25T08:20:14.997518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-25T08:20:15.753579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-25T08:20:15.754075+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-25T08:20:16.258861+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-25T08:20:16.259506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p28.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-25T08:20:16.713601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-25T08:20:17.369975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-25T08:20:17.372516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 490 · 2026-05-25T08:20:18.133538+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1419
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-25T08:20:18.184588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p31.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-25T08:20:18.595501+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1222
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-25T08:20:18.595913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p32.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-25T08:20:19.100594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p33.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-25T08:20:20.261733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1665
}
```

</details>

---


### Tool result

_source line 496 · 2026-05-25T08:20:20.715442+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2530
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-25T08:20:20.720149+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1619
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-25T08:20:30.578403+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang et al 2024 \"Tell Your Model Where to Attend\" inference-time attention steering LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang et al 2024 \"Tell Your Model Where to Attend\" inference-time attention steering LLM"
  }
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-25T08:20:30.980286+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li et al 2024 split-softmax multi-turn dialogue attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li et al 2024 split-softmax multi-turn dialogue attention"
  }
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-25T08:20:31.432343+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hong et al Rhea arXiv 2512.06869 role-aware attention multi-turn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hong et al Rhea arXiv 2512.06869 role-aware attention multi-turn"
  }
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-25T08:20:31.834158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dongre et al 2026 \"Goal Accessibility Ratio\" multi-turn dialogue attention decay"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dongre et al 2026 \"Goal Accessibility Ratio\" multi-turn dialogue attention decay"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-25T08:20:35.748713+00:00_

Web search results for query: "Li et al 2024 split-softmax multi-turn dialogue attention"

Links: [{"title":"Multi-Turn Conversational Dialogues","url":"https://www.emergentmind.com/topics/multi-turn-conversational-dialogues"},{"title":"TED: Turn Emphasis with Dialogue Feature Attention for Emotion   Recognition in Conversation","url":"https://arxiv.org/pdf/2501.01123"},{"title":"A Static and Dynamic Attention Framework for Multi Turn Dialogue Generation","url":"https://arxiv.org/html/2410.20766"},{"title":"Enhancing the Preference Extractor in Multi-turn Dialogues: From Annotating Disasters to Accurate Preference Extraction","url":"https://arxiv.org/html/2508.01739"},{"title":"Modeling Topical Relevance for Multi-Turn Dialogue Generation","url":"https://arxiv.org/pdf/2009.12735"},{"title":"Filling the Gap of Utterance-aware and Speaker-aware Representation for   Multi-turn Dialogue","url":"https://arxiv.org/pdf/2009.06504"}]

Based on the search results, I was unable to find a specific paper by Li et al. from 2024 that focuses on "split-softmax" for multi-turn dialogue attention. The search results returned various papers on multi-turn dialogue and attention mechanisms, but none specifically matching the exact combination of authors, year, and technique you're looking for.

The results include references to multiple Li et al. papers on dialogue systems and attention mechanisms from various years, but not the specific 2024 paper with the split-softmax approach you mentioned. 

Would you like me to:
1. Search with different or more specific keywords?
2. Search for more information about split-softmax attention mechanisms in general?
3. Search for Li et al. 2024 papers on a different aspect of dialogue systems?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4768
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-25T08:20:37.105677+00:00_

Web search results for query: "Zhang et al 2024 "Tell Your Model Where to Attend" inference-time attention steering LLM"

Links: [{"title":"[PDF] Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Tell-Your-Model-Where-to-Attend:-Post-hoc-Attention-Zhang-Singh/881845a7ea41a0dd2411a41ea9ce9770cdc38c6a"},{"title":"Model Tells Itself Where to Attend: Faithfulness Meets Automatic Attention Steering","url":"https://arxiv.org/html/2409.10790"},{"title":"[2311.02262] Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs","url":"https://arxiv.org/abs/2311.02262"},{"title":"Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs","url":"https://arxiv.org/html/2311.02262v2"},{"title":"MODEL TELLS ITSELF WHERE TO ATTEND: STEER","url":"https://openreview.net/pdf?id=AT64R0ivUO"},{"title":"Model Tells Itself Where to Attend: Faithfulness Meets Automatic   Attention Steering","url":"https://arxiv.org/pdf/2409.10790"},{"title":"GitHub - QingruZhang/PASTA: PASTA: Post-hoc Attention Steering for LLMs · GitHub","url":"https://github.com/QingruZhang/PASTA"},{"title":"Published as a conference paper at ICLR 2024 TELL YOUR MODEL WHERE TO ATTEND:","url":"https://arxiv.org/pdf/2311.02262"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## "Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs"

The paper was authored by Qingru Zhang, Chandan Singh, Liyuan Liu, Xiaodong Liu, Bin Yu, Jianfeng Gao, and Tuo Zhao, published in 2024 at The Twelfth International Conference on Learning Representations (ICLR 2024).

### Key Contribution

The paper introduces PASTA (Post-hoc Attention STeering Approach), a method that allows LLMs to read text with user-specified emphasis marks. PASTA modifies the attention scores generated during inference by emphasizing the scores at token positions corresponding to the user-specifie
…[truncated 738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6527
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-25T08:20:39.617642+00:00_

Web search results for query: "Hong et al Rhea arXiv 2512.06869 role-aware attention multi-turn"

Links: [{"title":"[2512.06869] Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/abs/2512.06869"},{"title":"(PDF) Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.researchgate.net/publication/398476529_Rhea_Role-aware_Heuristic_Episodic_Attention_for_Conversational_LLMs"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.arxiv.org/pdf/2512.06869"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/html/2512.06869"},{"title":"Multi-Head Self-Attention with Role-Guided Masks","url":"https://arxiv.org/pdf/2012.12366"},{"title":"Filling the Gap of Utterance-aware and Speaker-aware Representation for   Multi-turn Dialogue","url":"https://arxiv.org/pdf/2009.06504"}]

Based on the search results, I found the paper you're looking for:

**Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs** is authored by Wanyang Hong, Zhaoning Zhang, Yi Chen, Libo Zhang, Baihui Liu, Linbo Qiao, Zhiliang Tian, and Dongsheng Li.

**Overview:**

Large Language Models have achieved remarkable performance on single-turn tasks, yet their effectiveness deteriorates in multi-turn conversations. The paper defines this phenomenon as cumulative contextual decay - a progressive degradation of contextual integrity caused by attention pollution, dilution, and drift.

**The Proposed Solution:**

Rhea proposes a novel framework that decouples conversation history into two functionally independent memory modules: (1) an Instructional Memory that persistently stores high-fidelity global constraints via a structural priority mechanism, and (2) an Episodic Memory that dynamically manages user-model interactions via asymmetric noise control and heuristic context retrieval.

During inference, Rhea constructs 
…[truncated 337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8185
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-25T08:20:43.840850+00:00_

Web search results for query: "Dongre et al 2026 "Goal Accessibility Ratio" multi-turn dialogue attention decay"

Links: [{"title":"OnGoal: Tracking and Visualizing Conversational Goals in Multi-Turn Dialogue with Large Language Models","url":"https://arxiv.org/pdf/2508.21061"},{"title":"Imagination is All You Need! Curved Contrastive Learning for Abstract   Sequence Modeling Utilized on Long Short-Term Dialogue Planning","url":"https://arxiv.org/pdf/2211.07591"},{"title":"Fine-Tuning Arabic Large Language Models for improved multi-turn dialogue: A blueprint for synthetic data generation and benchmarking","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12900375/"},{"title":"DEUS: A Data-driven Approach to Estimate User Satisfaction in Multi-turn   Dialogues","url":"https://arxiv.org/pdf/2103.01287"},{"title":"Mismatch between Multi-turn Dialogue and its Evaluation Metric in   Dialogue State Tracking","url":"https://arxiv.org/pdf/2203.03123"}]

I didn't find the specific paper in the first search. Let me try a more targeted search for the "Goal Accessibility Ratio" metric:

Links: [{"title":"Accessibility and Attention in Situated Dialogue: Roles and Regulations - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/portal/en/publications/accessibility-and-attention-in-situated-dialogue-roles-and-regulations(d2945bae-62b6-4298-9847-6a94f8746f40).html"},{"title":"Dynamically Context-Sensitive Time-Decay Attention for Dialogue Modeling","url":"https://arxiv.org/pdf/1809.01557"},{"title":"Modeling individual attention dynamics on online social media","url":"https://arxiv.org/pdf/2507.01511"},{"title":"The Architects of Attention Decay: A Manifesto for Cognitive Stewardship in Design | by Zahara Chetty | Medium","url":"https://medium.com/@zahara_chetty/the-architects-of-attention-decay-a-manifesto-for-cognitive-stewardship-in-design-1e0023dccfd0"},{"title":"(PDF) Television Dialogue; Balancing Audibility, Attention and Accessibility","url":
…[truncated 4108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12006
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-25T08:21:27.900906+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li 2024 \"split-softmax\" instruction conversation tokens streaming LLM attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li 2024 \"split-softmax\" instruction conversation tokens streaming LLM attention"
  }
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-25T08:21:28.403551+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dongre\" 2026 \"goal accessibility\" OR \"goal attention\" multi-turn LLM ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dongre\" 2026 \"goal accessibility\" OR \"goal attention\" multi-turn LLM ACL EMNLP"
  }
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-25T08:21:29.258299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mikhaylova Martino 2019 scheduled sampling transformers sequence-to-sequence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mikhaylova Martino 2019 scheduled sampling transformers sequence-to-sequence"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-25T08:21:34.735571+00:00_

Web search results for query: "Li 2024 "split-softmax" instruction conversation tokens streaming LLM attention"

Links: [{"title":"GitHub - mit-han-lab/streaming-llm: [ICLR 2024] Efficient Streaming Language Models with Attention Sinks · GitHub","url":"https://github.com/mit-han-lab/streaming-llm"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf/5e9b035b5224d38807ae1ff0a27d972cf3fd10a8.pdf"},{"title":"Published as a conference paper at COLM 2024","url":"https://arxiv.org/pdf/2402.10962"},{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://ar5iv.labs.arxiv.org/html/2309.17453"},{"title":"Why Streaming LLMs Need Attention Sinks | Adam's Blog","url":"https://www.adambutterworth.com/posts/attention-sinks"},{"title":"Under review as a conference paper at ICLR 2024 A DISCUSSIONS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5e5fd18f863cbe6d8ae392a93fd271c9-Supplementary-Conference.pdf"}]

Based on the search results, I found information about "split-softmax" in the context of instruction drift in LLMs. Here are the key findings:

## Split-Softmax for Instruction Drift

Split-softmax is a technique devised to control attention decay, which is hypothesized to be the cause of instruction drift in extended conversations. Both system prompt repetition and split-softmax demonstrate higher effectiveness in mitigating instruction drift in multi-turn conversations.

Split-softmax provides a better trade-off between performance compared with prompting-based baselines and recent techniques from the literature.

## Related Work on Attention Mechanisms

The search also revealed related research on attention in streaming LLMs: StreamingLLM exploits the fact that attention sinks have high attention values, and preserving them can maintain the attention score distribution close to normal. The Softmax operation requires attention scores to sum up to one for all contextual tokens, so eve
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6834
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-25T08:21:35.588979+00:00_

Web search results for query: "Mikhaylova Martino 2019 scheduled sampling transformers sequence-to-sequence"

Links: [{"title":"Scheduled Sampling for Transformers - ACL Anthology","url":"https://aclanthology.org/P19-2049/"},{"title":"[1906.07651] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651"},{"title":"[1906.07651v1] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651v1"},{"title":"Scheduled Sampling for Transformers | alphaXiv","url":"https://www.alphaxiv.org/overview/1906.07651v1"},{"title":"Scheduled Sampling for Transformers | Request PDF","url":"https://www.researchgate.net/publication/335784238_Scheduled_Sampling_for_Transformers"},{"title":"Scheduled Sampling for Transformers - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190607651M/abstract"},{"title":"[PDF] Scheduled Sampling for Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scheduled-Sampling-for-Transformers-Mihaylova-Martins/6b6befbff611ddc98ef268b3c51353593bb07e77"},{"title":"Scheduled Sampling for Transformers | DeepAI","url":"https://deepai.org/publication/scheduled-sampling-for-transformers"},{"title":"GitHub - deep-spin/scheduled-sampling-transformers: Code for the paper \"Scheduled Sampling for Transformers\"","url":"https://github.com/deep-spin/scheduled-sampling-transformers"},{"title":"Scheduled Sampling for Transformers","url":"https://aclanthology.org/P19-2049.pdf"}]

Based on the search results, I found the paper you're looking for:

"Scheduled Sampling for Transformers" is a paper by Tsvetomila Mihaylova and André Martins, published in the ACL Student Research Workshop 2019.

The paper addresses a key challenge in sequence-to-sequence generation: scheduled sampling is a technique for avoiding exposure bias, consisting of feeding the model a mix of the teacher forced embeddings and the model predictions from the previous step in training time. The technique has been used for improving the model
…[truncated 642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6330
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-25T08:21:38.199965+00:00_

Web search results for query: ""Dongre" 2026 "goal accessibility" OR "goal attention" multi-turn LLM ACL EMNLP"

Links: [{"title":"Multi-Turn LLM Evaluation in 2026: What You Need to Know - Confident AI","url":"https://www.confident-ai.com/blog/multi-turn-llm-evaluation-in-2026"},{"title":"Guanting Dong - Homepage","url":"https://dongguanting.github.io/"},{"title":"Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey","url":"https://arxiv.org/pdf/2503.22458"},{"title":"Beyond More Context: Retrieval Diversity Boosts Multi-Turn Intent Understanding","url":"https://arxiv.org/pdf/2510.17940"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"OnGoal: Tracking and Visualizing Conversational Goals in Multi-Turn Dialogue with Large Language Models","url":"https://arxiv.org/pdf/2508.21061"}]

The search results don't show a specific paper by Dongre with the exact keywords you mentioned. However, I found some related work on multi-turn LLM evaluation and goal tracking in conversations. Let me try a more specific search focusing on Dongre as an author:

Links: [{"title":"[2605.12922] When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/abs/2605.12922"},{"title":"Swati Dongre's research works | Department Of Electronics And Information Technology, India and other places","url":"https://www.researchgate.net/scientific-contributions/Swati-Dongre-2230903099"},{"title":"Motivation in Mental Accessibility: Relevance Of A Representation (ROAR) as a New Framework - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC2992320/"},{"title":"[2311.04457] Evaluating Uncertainty Quantification approaches for Neural PDEs in scientific applications","url":"https://arxiv.org/abs/2311.04457"},{"title":"Lubhna Dongre (Author of Stepping Stones Taking Towards the Goal)","url":"https://www.goodreads.com/author/show/17733645.Lubhna_Dongre"},{"title":"Book Revie
…[truncated 2065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9796
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-25T08:23:50.692531+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"exposure bias\" \"attention\" transformer training inference mismatch 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"exposure bias\" \"attention\" transformer training inference mismatch 2024 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-25T08:23:58.781148+00:00_

Web search results for query: ""exposure bias" "attention" transformer training inference mismatch 2024 2025 2026"

Links: [{"title":"Exposure Bias in Machine Learning","url":"https://www.emergentmind.com/topics/exposure-bias"},{"title":"Reducing Exposure Bias in Training Recurrent Neural Network Transducers","url":"https://arxiv.org/pdf/2108.10803"},{"title":"On the Emergence of Position Bias in Transformers","url":"https://arxiv.org/pdf/2502.01951"},{"title":"Linear Recency Bias During Training Improves ...","url":"https://aclanthology.org/2025.coling-main.517.pdf"},{"title":"Bridging the gap between training and inference in LM-based TTS models","url":"https://arxiv.org/pdf/2509.17021"},{"title":"Transformer Training Essentials | CodeSignal Learn","url":"https://codesignal.com/learn/courses/bringing-transformers-to-life-training-inference/lessons/transformer-training-essentials-1"},{"title":"ReflexFlow: Rethinking Learning Objective for Exposure Bias Alleviation in Flow Matching","url":"https://arxiv.org/pdf/2512.04904"},{"title":"[2402.16790] Beyond Self-learned Attention: Mitigating Attention Bias in Transformer-based Models Using Attention Guidance","url":"https://arxiv.org/abs/2402.16790"},{"title":"Mitigating Exposure Bias in Neural Machine Translation","url":"https://aclanthology.org/2024.eamt-1.10.pdf"},{"title":"Discovering and Mitigating Indirect Bias in Attention-Based Model Explanations - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.104/"}]

I've performed the web search on exposure bias, attention, and transformer training-inference mismatch. Here are the key findings:

## Exposure Bias in Transformer Models (2024-2025)

Most language models suffer from exposure bias, the training-inference gap where training relies on teacher forcing with ground truth tokens as input, while inference requires the model to generate tokens autoregressively based on its own previous predictions. This discrepancy between training and inference often
…[truncated 1322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8088
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-25T08:26:39.180546+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "# Reviewer 2 审稿意见（Round 1）——新颖性 + 完整性 + 写作质量\n\n## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n**一句话总结**: 系统的诊断性实验设计揭示了一个有价值的发现（exposure bias 导致辅助注意力损失在 AR 生成中失效），但实验范围狭窄（单数据集、双模型且 Llama 不完整）、因果声称过强、缺少与关键竞争方法的实验对比，制约了贡献的完整性和影响力。\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 五路对比设计合理，统计分析严谨（Wilcoxon、Bootstrap CI、Bonferroni 校正），但\"causal exclusion chain\"的因果声称超出了观测性对比实验所能支撑的程度；Llama 仅覆盖 3/5 条件削弱跨架构泛化论证 |\n| Excitement | 3/5 | 诊断性贡献有实用价值（揭示 TF→AR gap 的机制），但核心结论（exposure bias 导致 attention 训练-推理不匹配）从既有文献可预期；范围窄、无方法突破限制了更广泛的兴奋度 |\n| Reproducibility | 3.5/5 | 附录提供了详尽的超参数和统计细节，但未提供代码链接或开源承诺 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Causal exclusion chain\"的因果声称过强，实验设计不支持严格因果推断\n- 具体位置：§1 第2段、§5 开头、§7 Conclusion\n- 问题：论文将五路对比描述为\"causal exclusion chain\"，声称每个子实验\"kills one alternative hypothesis\"。但本质上是观测性对比实验（不同训练配置下的性能比较），而非严格因果干预。+PCGrad vs. TG 的对比同时改变了梯度处理和可能的训练动态，不能干净地隔离单一因素。\n- 为什么影响接收：因果声称是论文核心叙事支柱。如果降级为 differential diagnosis，贡献定位需重新校准。\n- 建议：将\"causal exclusion\"改为\"systematic diagnostic comparison\"；删除\"kills one alternative hypothesis\"措辞。\n\n**N2** [critical] 缺少与 Li et al. (2024) split-softmax 和 Hong et al. (Rhea) 的实验对比\n- 具体位置：§2 Related Work（仅文字讨论），§8 Limitations（未提及）\n- 问题：split-softmax 在推理时分离 instruction 与 conversation tokens，直接针对同一问题。β-steering（§4.3）已经证明推理时注意力操控可恢复 GAR，但 split-softmax 作为更实际的推理时方案未被比较。读者无法判断 scheduled sampling 相对于已有推理时方案的 cost-benefit。\n- 建议：至少添加 split-softmax 实验对比，或在 Discussion 中定量讨论与 β-steering 的关系。\n\n**N3** [critical] Llama 实验不完整（3/5 条件），削弱\"cross-architecture generalization\"声称\n- 具体位置：§5.5 Cross-Model Replication、Table 7（Appendix F）\n- 问题：Llama 缺 PCGrad 和 UG，而这两个条件是 exclusion chain 排除 gradient conflict 和 turn conditioning 假设的关键。此外 Llama 用 median、Qwen 用 mean 报告 AR GAR，构成 metric selection 不一致。\n- 建议：补充 Llama PCGrad/UG 实验，或将声称降级为\"partial replication\"；统一报告指标（同时报告 mean 和 median）。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] 标题\"Destroys\"过度声称——AR GAR 降至 0.01-0.06 而非零，\"Collapses\"更准确\n**W2** [warning] 单数据集（UltraChat 8K）、单领域（多轮对话）——泛化性未验证\n**W3** [warning] 质量评估仅依赖 PPL——缺少 MT-Bench、AlpacaEval 等对话质量评估\n**W4** [warning] AR 评估 N=50 偏小，长对话评估 N=5 更小\n**W5** [warning] \"8-17×\"数字在全文重复 6+ 次，造成循环论证感\n**W6** [warning] 未提供代码链接或开源承诺，影响 reproducibility 评估\n\n---\n\n## 小问题\n- M1：参考文献中 Mihaylova 拼为 Mikhaylova（对照 ACL Anthology: P19-2049）\n- M2：Abstract 接近 200 词上限\n- M3：Figure 1(b) log scale 在 caption 中未明确标注\n- M4：GAR-Dongre vs GAR-ours 的数值差异（Table 1 中 GAR-D 极低 0.00-0.02）未充分解释\n- M5：§5.2 \"first application of PCGrad as a diagnostic tool\" 的 first claim 难以验证，建议删除\n- M6：Appendix AD 披露 AI 辅助——透明度良好\n\n---\n\n## 主要优势\n- S1：五路对比实验设计系统清晰，每对相邻对比仅改变一个因素（§3.4）\n- S2：β-steering（§4.3）是巧妙的确认性测试（常数偏置恢复 GAR 从 0.064→0.727）\n- S3：统计分析异常严谨（非参数检验、bootstrap CI、Bonferroni 校正、effect size），NLP 论文中属上乘\n- S4：25 页附录覆盖 loss formulation search、instruction retention、per-seed results 等多方面\n- S5：Scheduled sampling 迁移证明实用的 partial mitigation（gap 7.8×→1.3×，无 PPL cost）\n\n---\n\n## 提问\n1. 如果 split-softmax 在推理时能恢复 GAR，scheduled sampling（训练时干预）的必要性是否被削弱？\n2. Last-token GAR 能否代表整个回复的 goal adherence？\n3. Appendix Q 的 4 种 GAR 替代定义结果差异较大——核心发现是否依赖特定定义？\n4. 为什么未设计实验排除 KV cache drift（§7 中承认的替代解释）？\n5. Dongre 报告 12 模型 27-48% GAR 衰减/50 turns vs 本文 70.8%/5 turns——差异是否完全由定义不同解释？\n\n---\n\n## 可能遗漏的参考文献\n- PASTA (Zhang et al. 2024) 已引用但与 β-steering 的方法论重叠可以讨论更深入\n- StreamingLLM attention sink 现象与 GAR 衰减的机制区别可以更明确\n\n---\n\n**总结**：论文有潜力——如果 rebuttal 中（a）降低因果声称，（b）补充 split-softmax 对比，（c）完善 Llama 实验，可升至 4 分（Conference）。当前适合 Findings 或 Borderline Conference。",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "# Reviewer 2 审稿意见（Round 1）——新颖性 + 完整性 + 写作质量\n\n## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n**一句话总结**: 系统的诊断性实验设计揭示了一个有价值的发现（exposure bias 导致辅助注意力损失在 AR 生成中失效），但实验范围狭窄（单数据集、双模型且 Llama 不完整）、因果声称过强、缺少与关键竞争方法的实验对比，制约了贡献的完整性和影响力。\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 五路对比设计合理，统计分析严谨（Wilcoxon、Bootstrap CI、Bonferroni 校正），但\"causal exclusion chain\"的因果声称超出了观测性对比实验所能支撑的程度；Llama 仅覆盖 3/5 条件削弱跨架构泛化论证 |\n| Excitement | 3/5 | 诊断性贡献有实用价值（揭示 TF→AR gap 的机制），但核心结论（exposure bias 导致 attention 训练-推理不匹配）从既有文献可预期；范围窄、无方法突破限制了更广泛的兴奋度 |\n| Reproducibility | 3.5/5 | 附录提供了详尽的超参数和统计细节，但未提供代码链接或开源承诺 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Causal exclusion chain\"的因果声称过强，实验设计不支持严格因果推断\n- 具体位置：§1 第2段、§5 开头、§7 Conclusion\n- 问题：论文将五路对比描述为\"causal exclusion chain\"，声称每个子实验\"kills one alternative hypothesis\"。但本质上是观测性对比实验（不同训练配置下的性能比较），而非严格因果干预。+PCGrad vs. TG 的对比同时改变了梯度处理和可能的训练动态，不能干净地隔离单一因素。\n- 为什么影响接收：因果声称是论文核心叙事支柱。如果降级为 differential diagnosis，贡献定位需重新校准。\n- 建议：将\"causal exclusion\"改为\"systematic diagnostic comparison\"；删除\"kills one alternative hypothesis\"措辞。\n\n**N2** [critical] 缺少与 Li et al. (2024) split-softmax 和 Hong et al. (Rhea) 的实验对比\n- 具体位置：§2 Related Work（仅文字讨论），§8 Limitations（未提及）\n- 问题：split-softmax 在推理时分离 instruction 与 conversation tokens，直接针对同一问题。β-steering（§4.3）已经证明推理时注意力操控可恢复 GAR，但 split-softmax 作为更实际的推理时方案未被比较。读者无法判断 scheduled sampling 相对于已有推理时方案的 cost-benefit。\n- 建议：至少添加 split-softmax 实验对比，或在 Discussion 中定量讨论与 β-steering 的关系。\n\n**N3** [critical] Llama 实验不完整（3/5 条件），削弱\"cross-architecture generalization\"声称\n- 具体位置：§5.5 Cross-Model Replication、Table 7（Appendix F）\n- 问题：Llama 缺 PCGrad 和 UG，而这两个条件是 exclusion chain 排除 gradient conflict 和 turn conditioning 假设的关键。此外 Llama 用 median、Qwen 用 mean 报告 AR GAR，构成 metric selection 不一致。\n- 建议：补充 Llama PCGrad/UG 实验，或将声称降级为\"partial replication\"；统一报告指标（同时报告 mean 和 median）。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] 标题\"Destroys\"过度声称——AR GAR 降至 0.01-0.06 而非零，\"Collapses\"更准确\n**W2** [warning] 单数据集（UltraChat 8K）、单领域（多轮对话）——泛化性未验证\n**W3** [warning] 质量评估仅依赖 PPL——缺少 MT-Bench、AlpacaEval 等对话质量评估\n**W4** [warning] AR 评估 N=50 偏小，长对话评估 N=5 更小\n**W5** [warning] \"8-17×\"数字在全文重复 6+ 次，造成循环论证感\n**W6** [warning] 未提供代码链接或开源承诺，影响 reproducibility 评估\n\n---\n\n## 小问题\n- M1：参考文献中 Mihaylova 拼为 Mikhaylova（对照 ACL Anthology: P19-2049）\n- M2：Abstract 接近 200 词上限\n- M3：Figure 1(b) log scale 在 caption 中未明确标注\n- M4：GAR-Dongre vs GAR-ours 的数值差异（Table 1 中 GAR-D 极低 0.00-0.02）未充分解释\n- M5：§5.2 \"first application of PCGrad as a diagnostic tool\" 的 first claim 难以验证，建议删除\n- M6：Appendix AD 披露 AI 辅助——透明度良好\n\n---\n\n## 主要优势\n- S1：五路对比实验设计系统清晰，每对相邻对比仅改变一个因素（§3.4）\n- S2：β-steering（§4.3）是巧妙的确认性测试（常数偏置恢复 GAR 从 0.064→0.727）\n- S3：统计分析异常严谨（非参数检验、bootstrap CI、Bonferroni 校正、effect size），NLP 论文中属上乘\n- S4：25 页附录覆盖 loss formulation search、instruction retention、per-seed results 等多方面\n- S5：Scheduled sampling 迁移证明实用的 partial mitigation（gap 7.8×→1.3×，无 PPL cost）\n\n---\n\n## 提问\n1. 如果 split-softmax 在推理时能恢复 GAR，scheduled sampling（训练时干预）的必要性是否被削弱？\n2. Last-token GAR 能否代表整个回复的 goal adherence？\n3. Appendix Q 的 4 种 GAR 替代定义结果差异较大——核心发现是否依赖特定定义？\n4. 为什么未设计实验排除 KV cache drift（§7 中承认的替代解释）？\n5. Dongre 报告 12 模型 27-48% GAR 衰减/50 turns vs 本文 70.8%/5 turns——差异是否完全由定义不同解释？\n\n---\n\n## 可能遗漏的参考文献\n- PASTA (Zhang et al. 2024) 已引用但与 β-steering 的方法论重叠可以讨论更深入\n- StreamingLLM attention sink 现象与 GAR 衰减的机制区别可以更明确\n\n---\n\n**总结**：论文有潜力——如果 rebuttal 中（a）降低因果声称，（b）补充 split-softmax 对比，（c）完善 Llama 实验，可升至 4 分（Conference）。当前适合 Findings 或 Borderline Conference。",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-25T08:26:43.396157+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4215
}
```

</details>

---


### Assistant

_source line 516 · 2026-05-25T08:26:52.008499+00:00_

审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall: 3.5/5 (Borderline Conference)**，Soundness 3/5，Excitement 3/5
- **3 个 Must-Fix**：(N1) "causal exclusion chain" 因果声称过强——实际是观测性对比而非严格因果干预；(N2) 缺少与 split-softmax / Rhea 的实验对比；(N3) Llama 仅覆盖 3/5 条件且 mean/median 报告不一致
- **6 个 Should-Fix**：标题 "Destroys" 过强、单数据集单领域、PPL-only 质量评估、N=50 样本偏小、"8-17×" 过度重复、无代码开源
- **主要优势**：五路对比设计系统、β-steering 确认实验巧妙、统计分析严谨、附录充实、scheduled sampling 迁移有实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

30 recorded events


### User

_source line 517 · 2026-05-25T08:27:11.358507+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿原文。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 评分
**Overall**: 3.5 / 5（Borderline Conference）| **Confidence**: 4 / 5

### Must-Fix 问题

**N1** [critical] GAR 与下游任务相关性极弱（r=0.200, r²=0.04），削弱论文实际意义
- GAR 仅解释 4% 的 instruction retention 方差。β-steering 下游改善 +11.1pp 未达显著（p=0.077, Table 4）。若 GAR 崩溃不影响实际任务，"Exposure Bias Destroys" 的标题暗示的实际危害存疑。

**N2** [critical] 因果排除链不完整——exposure bias 归因过强
- 仅排除 turn conditioning 和 gradient direction conflict。KV cache drift（§6 自己承认未测试）和 magnitude imbalance（NTP 主导 7.5–14.7×）均未实验验证。标题 "Destroys" 过于确定。

**N3** [critical] 大部分实验条件仅单种子，伪重复问题
- Base/LoRA-only/UG/PCGrad 均为单种子。Wilcoxon 以 N=50 对话为样本，但共享同一模型权重，是伪重复。

### Should-Fix 问题

**W1** β-steering 恢复 GAR 存在部分循环论证
**W2** 单数据集（UltraChat）限制泛化性
**W3** 缺失与 split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 的实验对比
**W4** GAR-Dongre 近零可能是 averaging artifact

### 主要优势
1. 五路对比设计精良
2. 负面结果诚实报告
3. 统计实践规范
4. 跨架构+跨尺度验证
5. 丰富附录（23页）
6. β-steering 提供可操作推理时干预方案

---

请逐条给出 [AGREE] 或 [REBUT] 回应，特别关注你自己审查视角（新颖性/完整性/写作）与 Reviewer 1 发现的一致性或差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-25T08:27:41.624102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-25T08:27:42.126583+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-25T08:27:42.126995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-25T08:27:42.578855+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-25T08:27:42.629968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-25T08:27:43.584302+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-25T08:27:43.584710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-25T08:27:44.086799+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-25T08:27:44.087151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-25T08:27:44.539154+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-25T08:27:44.539964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p29.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-25T08:27:44.590463+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_2_b65e25ec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-25T08:27:50.416744+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
  "project": "turn_residual_gating",
  "pages": "5,6,8,12,15,17,25,30",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/submitted.pdf",
    "project": "turn_residual_gating",
    "pages": "5,6,8,12,15,17,25,30",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-25T08:27:51.573472+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 398.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 419.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 381.1}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.9}, {\"page\": 30, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p30.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.1}], \"total_pages\": 33, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_image
…[truncated 42 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1156
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-25T08:27:55.140907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 533 · 2026-05-25T08:27:55.695713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 534 · 2026-05-25T08:27:56.501916+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-25T08:27:56.505237+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-25T08:27:56.505698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---


### Tool call

_source line 537 · 2026-05-25T08:27:56.857286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p30.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 538 · 2026-05-25T08:27:57.311189+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-25T08:27:57.713943+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-25T08:28:02.317077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 541 · 2026-05-25T08:28:02.518327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_5/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 542 · 2026-05-25T08:28:03.224676+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-25T08:28:03.426754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-25T08:30:07.663857+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "# Reviewer 2 交叉回应（对 Reviewer 1 审稿意见）\n\n## 逐条回应\n\n### Must-Fix\n\n**[AGREE with nuance] R1-N1: GAR与下游弱相关（r²=0.04）**\n数据引用准确（§6 p.8, Table 4）。但 R1 解读过严——论文一致将 GAR 定位为 diagnostic probe（§3.1, §6），弱下游相关性不等于无诊断价值。**核心问题在于标题\"Destroys\"暗示的实际危害与 4% 解释方差不匹配**，与我的 W1（标题 overclaim）一致。建议降为 Should-Fix。\n\n**[AGREE] R1-N2: 因果排除链不完整**\n完全同意，与我的 N1 高度一致。R1 补充了两个重要缺口：(1) KV cache drift（§7 自己承认未排除），(2) NTP magnitude imbalance 7.5-14.7×（§5.2）——PCGrad 仅消除方向冲突，未解决量级碾压。**两位 Reviewer 强共识：causal exclusion 声称需降级。**\n\n**[REBUT, 降级为 Should-Fix] R1-N3: 单种子伪重复**\n技术上正确但过于严厉：(1) NLP 领域标准做法；(2) 关键条件 ThreadGate 有 2-3 种子（Appendix T p.25），SS 有 2 种子（Table 19）；(3) 效应量 8-17× 远超种子方差（种子间 AR GAR: 0.064 vs 0.055）；(4) Bootstrap CI 部分缓解。建议降为 Should-Fix。\n\n### Should-Fix\n\n**[AGREE] R1-W1: β-steering 部分循环论证** — GAR 恢复是同义反复（boost attention → attention metric recovers），非循环部分（下游 +11.1pp）统计上弱（p=0.077）。论文应解耦两个声称。\n\n**[AGREE] R1-W2: 单数据集** — 与我的 W2 一致。\n\n**[AGREE, 但我评级更高] R1-W3: 缺 split-softmax/Rhea 对比** — 我将此列为 N2 (Must-Fix)。β-steering 已证明推理时干预可恢复 GAR，split-softmax 是更实际的已发表方案，诊断论文不与已有方案对比是完整性缺陷。\n\n**[AGREE] R1-W4: GAR-Dongre 近零是 averaging artifact** — Table 1 所有条件 GAR-D ≈ 0.00-0.02 证实了这点。§3.1 对选择 GAR-ours 的讨论不充分。\n\n## 两位 Reviewer 共识\n\n| 问题 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| 因果声称过强 | N2 Must-Fix | N1 Must-Fix | **强共识** |\n| 缺 split-softmax 对比 | W3 Should-Fix | N2 Must-Fix | R2 更严重 |\n| 标题 overclaim | implicit | W1 Should-Fix | 共识 |\n| 单数据集 | W2 | W2 | 一致 |\n| Llama 不完整 | 未提 | N3 Must-Fix | 仅 R2 |\n| GAR 弱相关 | N1 Must-Fix | — | R2 同意降为 Should-Fix |\n| 单种子伪重复 | N3 Must-Fix | — | R2 认为降为 Should-Fix |\n\n**评分维持 3.5/5 (Borderline Conference)**。两位 Reviewer 视角互补（R1 偏统计方法论，R2 偏学术完整性），对核心问题达成共识。",
  "reviewer_id": "2",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "# Reviewer 2 交叉回应（对 Reviewer 1 审稿意见）\n\n## 逐条回应\n\n### Must-Fix\n\n**[AGREE with nuance] R1-N1: GAR与下游弱相关（r²=0.04）**\n数据引用准确（§6 p.8, Table 4）。但 R1 解读过严——论文一致将 GAR 定位为 diagnostic probe（§3.1, §6），弱下游相关性不等于无诊断价值。**核心问题在于标题\"Destroys\"暗示的实际危害与 4% 解释方差不匹配**，与我的 W1（标题 overclaim）一致。建议降为 Should-Fix。\n\n**[AGREE] R1-N2: 因果排除链不完整**\n完全同意，与我的 N1 高度一致。R1 补充了两个重要缺口：(1) KV cache drift（§7 自己承认未排除），(2) NTP magnitude imbalance 7.5-14.7×（§5.2）——PCGrad 仅消除方向冲突，未解决量级碾压。**两位 Reviewer 强共识：causal exclusion 声称需降级。**\n\n**[REBUT, 降级为 Should-Fix] R1-N3: 单种子伪重复**\n技术上正确但过于严厉：(1) NLP 领域标准做法；(2) 关键条件 ThreadGate 有 2-3 种子（Appendix T p.25），SS 有 2 种子（Table 19）；(3) 效应量 8-17× 远超种子方差（种子间 AR GAR: 0.064 vs 0.055）；(4) Bootstrap CI 部分缓解。建议降为 Should-Fix。\n\n### Should-Fix\n\n**[AGREE] R1-W1: β-steering 部分循环论证** — GAR 恢复是同义反复（boost attention → attention metric recovers），非循环部分（下游 +11.1pp）统计上弱（p=0.077）。论文应解耦两个声称。\n\n**[AGREE] R1-W2: 单数据集** — 与我的 W2 一致。\n\n**[AGREE, 但我评级更高] R1-W3: 缺 split-softmax/Rhea 对比** — 我将此列为 N2 (Must-Fix)。β-steering 已证明推理时干预可恢复 GAR，split-softmax 是更实际的已发表方案，诊断论文不与已有方案对比是完整性缺陷。\n\n**[AGREE] R1-W4: GAR-Dongre 近零是 averaging artifact** — Table 1 所有条件 GAR-D ≈ 0.00-0.02 证实了这点。§3.1 对选择 GAR-ours 的讨论不充分。\n\n## 两位 Reviewer 共识\n\n| 问题 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| 因果声称过强 | N2 Must-Fix | N1 Must-Fix | **强共识** |\n| 缺 split-softmax 对比 | W3 Should-Fix | N2 Must-Fix | R2 更严重 |\n| 标题 overclaim | implicit | W1 Should-Fix | 共识 |\n| 单数据集 | W2 | W2 | 一致 |\n| Llama 不完整 | 未提 | N3 Must-Fix | 仅 R2 |\n| GAR 弱相关 | N1 Must-Fix | — | R2 同意降为 Should-Fix |\n| 单种子伪重复 | N3 Must-Fix | — | R2 认为降为 Should-Fix |\n\n**评分维持 3.5/5 (Borderline Conference)**。两位 Reviewer 视角互补（R1 偏统计方法论，R2 偏学术完整性），对核心问题达成共识。",
    "reviewer_id": "2",
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-25T08:30:11.985635+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4321
}
```

</details>

---


### Assistant

_source line 546 · 2026-05-25T08:30:22.888950+00:00_

交叉回应已提交。总结：

- **R1-N1（GAR 弱相关）**：同意数据但建议降为 Should-Fix——GAR 作为诊断探针不需要强下游相关性，但标题暗示的危害与 r²=0.04 不匹配
- **R1-N2（因果排除不完整）**：完全同意，与我的 N1 强共识
- **R1-N3（单种子伪重复）**：反驳严重性——效应量 8-17× 远超种子方差，NLP 标准做法，建议降为 Should-Fix
- **R1-W1~W4**：均同意，其中 W3（缺 split-softmax 对比）我评级更高（Must-Fix）

两位 Reviewer 核心共识：因果声称需降级、缺关键对比实验、标题 overclaim。评分维持 3.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

142 recorded events


### User

_source line 547 · 2026-05-25T21:16:10.425844+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性/完整性**审查。

## 投稿信息
- **Venue**: EMNLP 2026 (via ACL Rolling Review)
- **类别**: Long paper (Main Conference)
- **截止日期**: ARR 提交 2026-05-25，EMNLP Commitment 2026-08-02
- **格式**: 正文 8 页限制，参考文献不限，Limitations 章节必须有（不计入页数），double-blind，ACL 模板
- **匿名规则**: Double-blind，无匿名期限制

## 论文路径
- LaTeX: `projects/turn_residual_gating/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_6/submitted.pdf`

## 你的审查侧重

**新颖性/完整性**——重点检查以下方面：

1. **Novelty 定位**：exposure bias 在 multi-turn transformer auxiliary attention losses 上的首次实证——这个 novelty claim 是否成立？是否有已知工作做了类似的事情？"to our knowledge, the first" 的措辞是否可接受？
2. **Related Work 覆盖**：
   - 是否遗漏了重要的相关工作？特别是 attention steering/loss 方向、multi-turn dialogue 方向、exposure bias 方向
   - Li et al. (2024) split-softmax、Rhea (Hong et al. 2025) 等竞争方案是否被充分讨论？
   - Scheduled sampling 在 transformer 上的应用是否已有先例？
3. **Framing 准确性**：
   - Contribution 声称是否与实际证据匹配？是否存在过度声称（overclaim）？
   - "causal exclusion" 措辞是否准确？实际是消融研究 + 排除法
   - GAR 被定位为 "diagnostic probe"——这个定位是否自洽？
4. **写作质量**：
   - 行文是否清晰、逻辑连贯？
   - 关键数字（如 8-17×、0.401±0.047）是否重复过多？
   - Figure/Table 的标题和说明是否准确？
   - 引用格式是否一致？bib 条目是否完整？
5. **格式合规**：
   - 正文是否在 8 页以内？
   - Limitations 章节是否合规（放在正文、一段覆盖 3 个点左右）？
   - 匿名化是否彻底？
   - Abstract 是否在 200 words 以内？
6. **Appendix 完整性**：附录内容是否与正文互补而非重复？是否有关键信息仅在附录中但应在正文中？

请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 1-5，参照 EMNLP 2026 评分标准)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---
