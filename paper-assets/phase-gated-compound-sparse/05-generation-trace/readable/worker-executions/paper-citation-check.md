# paper citation check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_paper_citation-check_20260514T132110.log`
- **Structured JSON:** [`a7113cb192b9fb0ce52c.json`](../../sessions/a7/a7113cb192b9fb0ce52c.json)

## Before a recorded user message

46 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "ba775a38-f922-40a1-b989-735ae9d8cd1f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778775000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4a1234ad-ca2d-42b7-9706-078762ac1487",
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me check the paper directory and extract citation keys from tex files and bib entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "260e4116-a7de-4789-ad23-1316cc481531",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bx4F2t12NFSUqUMucwttqb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11544
      },
      "output_tokens": 20,
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

_source line 5_

<details open><summary>🔧 Tool call — Glob · `toolu_01Ervv21bNPTt17ukHRvtg81`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "70303f7e-e22a-44ec-a008-aa9c99a479fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bx4F2t12NFSUqUMucwttqb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11544
      },
      "output_tokens": 20,
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

_source line 6 · 2026-05-14T13:21:21.361Z_

<details><summary>↩ Tool result · `toolu_01Ervv21bNPTt17ukHRvtg81`</summary>

```text
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "78eb9610-432e-4cde-a3cc-8ea6efb1565c",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/appendix_results.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/appendix_disc_analysis.tex",
      "artifacts/_project/paper/appendix.tex",
      "artifacts/_project/paper/results.tex"
    ],
    "durationMs": 13,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01BV8pr1c9mhjpPhMEtYfqM9`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "3303c3ef-b92b-4d04-80b8-d73126ef0c23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bx4F2t12NFSUqUMucwttqb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11544
      },
      "output_tokens": 20,
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

_source line 8 · 2026-05-14T13:21:21.644Z_

<details><summary>↩ Tool result · `toolu_01BV8pr1c9mhjpPhMEtYfqM9`</summary>

```text
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "71eec3b0-829d-482c-9008-08426fb837b2",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 14,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Grep · `toolu_01TgD69HPLLcVR5oENdinn3t`</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "6415b966-d496-42c0-8a10-b9a68b95ea5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qS76tLg8gHJnejMSEg2HR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 22991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
      },
      "output_tokens": 37,
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

_source line 10 · 2026-05-14T13:21:25.400Z_

<details><summary>↩ Tool result · `toolu_01TgD69HPLLcVR5oENdinn3t`</summary>

```text
artifacts/_project/paper/related_work.tex:6:\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
artifacts/_project/paper/related_work.tex:7:\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
artifacts/_project/paper/related_work.tex:8:\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
artifacts/_project/paper/related_work.tex:9:GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
artifacts/_project/paper/related_work.tex:14:Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
artifacts/_project/paper/related_work.tex:15:\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
artifacts/_project/paper/related_work.tex:16:RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
artifacts/_project/paper/related_work.tex:20:ThinKV~\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.
artifacts/_project/paper/related_work.tex:21:\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\ ``decisive'' representation phases.
artifacts/_project/paper/related_work.tex:22:\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.
artifacts/_project/paper/methodology.tex:6:[Omitted long matching line]
artifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
artifacts/_project/paper/methodology.tex:22:All confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\cite{efron-1993}. Paired bootstrap controls for problem-level variance. All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.\footnote{Experiments on 4$\times$ NVIDIA RTX PRO 6000 Blackwell 96\,GB GPUs.}
artifacts/_project/paper/background.tex:12:[Omitted long matching line]
artifacts/_project/paper/background.tex:33:Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\ref{app:formulation-details}.
artifacts/_project/paper/appendix.tex:5:Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
artifacts/_project/paper/appendix.tex:22:where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
artifacts/_project/paper/appendix.tex:25:Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
artifacts/_project/paper/introduction.tex:4:Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
artifacts/_project/paper/introduction.tex:5:Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}.
artifacts/_project/paper/introduction.tex:7:Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}.
artifacts/_project/paper/introduction.tex:8:This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "c0af0d10-0790-4875-ad74-43ae86cef66a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:6:\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\cite{slim-icml2025} formalize compound error for quantization and sparsity.\nartifacts/_project/paper/related_work.tex:7:\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.\nartifacts/_project/paper/related_work.tex:8:\\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.\nartifacts/_project/paper/related_work.tex:9:GRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.\nartifacts/_project/paper/related_work.tex:14:Ada-KV~\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\cite{snapkv-neurips2024} compresses from a fixed observation window; \\cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\\times}$ higher than expected under standard aggregation.\nartifacts/_project/paper/related_work.tex:15:\\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.\nartifacts/_project/paper/related_work.tex:16:RetentiveKV~\\cite{retentivekv-2026} identifies deferred importance, and \\cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.\nartifacts/_project/paper/related_work.tex:20:ThinKV~\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.\nartifacts/_project/paper/related_work.tex:21:\\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\\ ``decisive'' representation phases.\nartifacts/_project/paper/related_work.tex:22:\\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.\nartifacts/_project/paper/methodology.tex:6:[Omitted long matching line]\nartifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\nartifacts/_project/paper/methodology.tex:22:All confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\cite{efron-1993}. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.\\footnote{Experiments on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\,GB GPUs.}\nartifacts/_project/paper/background.tex:12:[Omitted long matching line]\nartifacts/_project/paper/background.tex:33:Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\\ref{app:formulation-details}.\nartifacts/_project/paper/appendix.tex:5:Heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\nartifacts/_project/paper/appendix.tex:22:where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\nartifacts/_project/paper/appendix.tex:25:Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\nartifacts/_project/paper/introduction.tex:4:Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\cite{kwon-sosp2023, pope-mlsys2023}.\nartifacts/_project/paper/introduction.tex:5:Two complementary responses---\\emph{attention head pruning} \\cite{voita-acl2019, michel-neurips2019} and \\emph{KV cache eviction} \\cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\cite{spark-aaai2026, slim-icml2025}.\nartifacts/_project/paper/introduction.tex:7:Prior work treats compound interaction magnitude as roughly constant across generation \\cite{spark-aaai2026, unicomp-2026}.\nartifacts/_project/paper/introduction.tex:8:This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.",
    "numLines": 22
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_014CnptuzyWTMDSJVhnbf8Wj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "c34a9693-7540-4b83-8107-6a47e182dbff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qS76tLg8gHJnejMSEg2HR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 22991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
      },
      "output_tokens": 37,
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

_source line 12 · 2026-05-14T13:21:25.695Z_

<details><summary>↩ Tool result · `toolu_014CnptuzyWTMDSJVhnbf8Wj`</summary>

```text
1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{compression-ordering-2025,
13	    title   = {A Systematic Study of Compression Ordering for Large Language Models},
14	    author  = {Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna},
15	    journal = {arXiv preprint arXiv:2511.19495},
16	    year    = {2025},
17	    url     = {https://arxiv.org/abs/2511.19495},
18	}
19	
20	@article{decision-repr-transition-2026,
21	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
22	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
23	    journal = {arXiv preprint arXiv:2605.07271},
24	    year    = {2026},
25	    url     = {https://arxiv.org/abs/2605.07271},
26	}
27	
28	@article{deepseek-r1-2025,
29	    title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},
30	    author  = {{DeepSeek-AI}},
31	    journal = {Nature},
32	    volume  = {645},
33	    pages   = {633--638},
34	    year    = {2025},
35	    doi     = {10.1038/s41586-025-08636-z},
36	}
37	
38	@inproceedings{defensivekv-iclr2026,
39	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
40	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
41	    booktitle = {International Conference on Learning Representations},
42	    year      = {2026},
43	    url       = {https://arxiv.org/abs/2510.13334},
44	}
45	
46	@article{doing-more-with-less-2026,
47	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
48	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
49	    journal = {arXiv preprint arXiv:2604.25098},
50	    year    = {2026},
51	    url     = {https://arxiv.org/abs/2604.25098},
52	}
53	
54	@book{efron-1993,
55	    title     = {An Introduction to the Bootstrap},
56	    author    = {Efron, Bradley and Tibshirani, Robert J.},
57	    publisher = {Chapman \& Hall/CRC},
58	    year      = {1993},
59	}
60	
61	@inproceedings{graspune-acl2026,
62	    title     = {{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},
63	    author    = {Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
64	    booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},
65	    year      = {2026},
66	    url       = {https://arxiv.org/abs/2604.19398},
67	}
68	
69	@article{greedy-bias-kvcache-2026,
70	    title   = {More Than a Quick Glance: Overcoming the Greedy Bias in {KV}-Cache Compression},
71	    author  = {Sood, Aryan and Sharma, Tanvi and Agrawal, Vansh},
72	    journal = {arXiv preprint arXiv:2602.02199},
73	    year    = {2026},
74	    url     = {https://arxiv.org/abs/2602.02199},
75	}
76	
77	@inproceedings{h2o-neurips2023,
78	    title     = {{H\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
79	    author    = {Zhang, Zhenyu and Sheng, Ying and Zhou, Tianyi and Chen, Tianlong and Zheng, Lianmin and Cai, Ruisi and Song, Zhao and Tian, Yuandong and R{\'e}, Christopher and Barrett, Clark and Wang, Zhangyang and Chen, Beidi},
80	    booktitle = {Advances in Neural Information Processing Systems},
81	    year      = {2023},
82	    url       = {https://arxiv.org/abs/2306.14048},
83	}
84	
85	@inproceedings{kwon-sosp2023,
86	    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
87	    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},
88	    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},
89	    year      = {2023},
90	    url       = {https://arxiv.org/abs/2309.06180},
91	}
92	
93	@inproceedings{math500-neurips2021,
94	    title     = {Measuring Mathematical Problem Solving With the {MATH} Dataset},
95	    author    = {Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob},
96	    booktitle = {Advances in Neural Information Processing Systems},
97	    year      = {2021},
98	    url       = {https://arxiv.org/abs/2103.03874},
99	}
100	
101	@inproceedings{michel-neurips2019,
102	    title     = {Are Sixteen Heads Really Better than One?},
103	    author    = {Michel, Paul and Levy, Omer and Neubig, Graham},
104	    booktitle = {Advances in Neural Information Processing Systems},
105	    year      = {2019},
106	    url       = {https://arxiv.org/abs/1905.10650},
107	}
108	
109	@inproceedings{mustafar-neurips2025,
110	    title     = {Mustafar: Promoting Unstructured Sparsity for {KV} Cache Pruning in {LLM} Inference},
111	    author    = {Joo, Donghyeon and Hosseini, Helya and Hadidi, Ramyad and Asgari, Bahar},
112	    booktitle = {Advances in Neural Information Processing Systems},
113	    year      = {2025},
114	    url       = {https://arxiv.org/abs/2505.22913},
115	}
116	
117	@inproceedings{nacl-acl2024,
118	    title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},
119	    author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},
120	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
121	    year      = {2024},
122	    url       = {https://arxiv.org/abs/2408.03675},
123	}
124	
125	@article{obcache-2025,
126	    title   = {{OBCache}: Optimal Brain {KV} Cache Pruning for Efficient Long-Context {LLM} Inference},
127	    author  = {Gu, Yuzhe and Liang, Xiyu and Zhao, Jiaojiao and Diao, Enmao},
128	    journal = {arXiv preprint arXiv:2510.07651},
129	    year    = {2025},
130	    url     = {https://arxiv.org/abs/2510.07651},
131	}
132	
133	@inproceedings{pagedeviction-eacl2026,
134	    title     = {{PagedEviction}: Structured Block-wise {KV} Cache Pruning for Efficient Large Language Model Inference},
135	    author    = {Chitty-Venkata, Krishna Teja and Ye, Jie and Sun, Xian-He and Kougkas, Anthony and Emani, Murali and Vishwanath, Venkatram and Nicolae, Bogdan},
136	    booktitle = {Findings of the European Chapter of the Association for Computational Linguistics},
137	    year      = {2026},
138	    url       = {https://arxiv.org/abs/2509.04377},
139	}
140	
141	@article{phase-transition-compression-2026,
142	    title   = {Phase transitions in large language model compression},
143	    author  = {Ma, Ziyang and Li, Zuchao and Zhang, Lefei and Xia, Gui-Song and Du, Bo and Zhang, Liangpei and Tao, Dacheng},
144	    journal = {npj Artificial Intelligence},
145	    volume  = {2},
146	    number  = {21},
147	    year    = {2026},
148	    url     = {https://www.nature.com/articles/s44387-026-00072-8},
149	}
150	
151	@inproceedings{pope-mlsys2023,
152	    title     = {Efficiently Scaling Transformer Inference},
153	    author    = {Pope, Reiner and Douglas, Sholto and Chowdhery, Aakanksha and Devlin, Jacob and Bradbury, James and Heek, Jonathan and Xiao, Kefan and Agrawal, Shivani and Dean, Jeff},
154	    booktitle = {Proceedings of Machine Learning and Systems},
155	    year      = {2023},
156	    url       = {https://arxiv.org/abs/2211.05102},
157	}
158	
159	@article{pyramidkv-2024,
160	    title   = {{PyramidKV}: Dynamic {KV} Cache Compression based on Pyramidal Information Funneling},
161	    author  = {Cai, Zefan and Zhang, Yichi and Gao, Bofei and Liu, Yuliang and Liu, Tianyu and Lu, Keming and Xiong, Wayne and Dong, Yue and Chang, Baobao and Hu, Junjie and Xiao, Wen},
162	    journal = {arXiv preprint arXiv:2406.02069},
163	    year    = {2024},
164	    url     = {https://arxiv.org/abs/2406.02069},
165	}
166	
167	@article{qwen25-2024,
168	    title   = {{Qwen2.5} Technical Report},
169	    author  = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Wei, Haoran and others},
170	    journal = {arXiv preprint arXiv:2412.15115},
171	    year    = {2024},
172	    url     = {https://arxiv.org/abs/2412.15115},
173	}
174	
175	@inproceedings{raas-acl2025,
176	    title     = {{RaaS}: Reasoning-Aware Attention Sparsity for Efficient {LLM} Reasoning},
177	    author    = {Hu, Junhao and Huang, Wenrui and Wang, Weidong and Li, Zhenwen and Hu, Tiancheng and Liu, Zhixia and Chen, Xusheng and Xie, Tao and Shan, Yizhou},
178	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
179	    year      = {2025},
180	    url       = {https://arxiv.org/abs/2502.11147},
181	}
182	
183	@article{retentivekv-2026,
184	    title   = {{RetentiveKV}: State-Space Memory for Uncertainty-Aware Multimodal {KV} Cache Eviction},
185	    author  = {Liu, Sihao and Xiong, YuFan and Jiang, Zhonghua and Wang, Zhaode and Lv, Chengfei and Zhang, Shengyu},
186	    journal = {arXiv preprint arXiv:2605.04075},
187	    year    = {2026},
188	    url     = {https://arxiv.org/abs/2605.04075},
189	}
190	
191	@inproceedings{slim-icml2025,
192	    title     = {{SLiM}: One-shot Quantization and Sparsity with Low-rank Approximation for {LLM} Weight Compression},
193	    author    = {Mozaffari, Mohammad and Yazdanbakhsh, Amir and Dehnavi, Maryam Mehri},
194	    booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
195	    year      = {2025},
196	    url       = {https://arxiv.org/abs/2410.09615},
197	}
198	
199	@inproceedings{snapkv-neurips2024,
200	    title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},
201	    author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},
202	    booktitle = {Advances in Neural Information Processing Systems},
203	    year      = {2024},
204	    url       = {https://arxiv.org/abs/2404.14469},
205	}
206	
207	
208	@inproceedings{spark-aaai2026,
209	    title     = {{SparK}: Query-Aware Unstructured Sparsity with Recoverable {KV} Cache Channel Pruning},
210	    author    = {Liao, Huanxuan and Xu, Yixing and He, Shizhu and Li, Guanchen and Yin, Xuanwu and Li, Dong and Barsoum, Emad and Zhao, Jun and Liu, Kang},
211	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
212	    year      = {2026},
213	    url       = {https://arxiv.org/abs/2508.15212},
214	}
215	
216	@article{sparse-frontier-2025,
217	    title   = {The Sparse Frontier: Sparse Attention Trade-offs in Transformer {LLMs}},
218	    author  = {Nawrot, Piotr and Li, Robert and Huang, Renjie and Ruder, Sebastian and Marchisio, Kelly and Ponti, Edoardo M.},
219	    journal = {arXiv preprint arXiv:2504.17768},
220	    year    = {2025},
221	    url     = {https://arxiv.org/abs/2504.17768},
222	}
223	
224	@inproceedings{thinkv-iclr2026,
225	    title     = {{ThinKV}: Thought-Adaptive {KV} Cache Compression for Efficient Reasoning Models},
226	    author    = {Ramachandran, Akshat and Neseem, Marina and Sakr, Charbel and Venkatesan, Rangharajan and Khailany, Brucek and Krishna, Tushar},
227	    booktitle = {International Conference on Learning Representations},
228	    year      = {2026},
229	    url       = {https://arxiv.org/abs/2510.01290},
230	}
231	
232	@article{unicomp-2026,
233	    title   = {{UniComp}: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation},
234	    author  = {von Rad, Jonathan and Cao, Yong and Geiger, Andreas},
235	    journal = {arXiv preprint arXiv:2602.09130},
236	    year    = {2026},
237	    url     = {https://arxiv.org/abs/2602.09130},
238	}
239	
240	@inproceedings{voita-acl2019,
241	    title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
242	    author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},
243	    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
244	    year      = {2019},
245	    url       = {https://arxiv.org/abs/1905.09418},
246	}
247	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "d0f4c85b-e0b1-4be7-9027-1c3543e6e29f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
      "content": "% References for Phase-Gated Compound Sparse paper\n% Generated 2026-05-14; all entries verified via web search\n\n@inproceedings{adakv-neurips2025,\n    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},\n    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2407.11550},\n}\n\n@article{compression-ordering-2025,\n    title   = {A Systematic Study of Compression Ordering for Large Language Models},\n    author  = {Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna},\n    journal = {arXiv preprint arXiv:2511.19495},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2511.19495},\n}\n\n@article{decision-repr-transition-2026,\n    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},\n    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},\n    journal = {arXiv preprint arXiv:2605.07271},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2605.07271},\n}\n\n@article{deepseek-r1-2025,\n    title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n    author  = {{DeepSeek-AI}},\n    journal = {Nature},\n    volume  = {645},\n    pages   = {633--638},\n    year    = {2025},\n    doi     = {10.1038/s41586-025-08636-z},\n}\n\n@inproceedings{defensivekv-iclr2026,\n    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},\n    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2510.13334},\n}\n\n@article{doing-more-with-less-2026,\n    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n    journal = {arXiv preprint arXiv:2604.25098},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2604.25098},\n}\n\n@book{efron-1993,\n    title     = {An Introduction to the Bootstrap},\n    author    = {Efron, Bradley and Tibshirani, Robert J.},\n    publisher = {Chapman \\& Hall/CRC},\n    year      = {1993},\n}\n\n@inproceedings{graspune-acl2026,\n    title     = {{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},\n    author    = {Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n    booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2604.19398},\n}\n\n@article{greedy-bias-kvcache-2026,\n    title   = {More Than a Quick Glance: Overcoming the Greedy Bias in {KV}-Cache Compression},\n    author  = {Sood, Aryan and Sharma, Tanvi and Agrawal, Vansh},\n    journal = {arXiv preprint arXiv:2602.02199},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2602.02199},\n}\n\n@inproceedings{h2o-neurips2023,\n    title     = {{H\\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n    author    = {Zhang, Zhenyu and Sheng, Ying and Zhou, Tianyi and Chen, Tianlong and Zheng, Lianmin and Cai, Ruisi and Song, Zhao and Tian, Yuandong and R{\\'e}, Christopher and Barrett, Clark and Wang, Zhangyang and Chen, Beidi},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2306.14048},\n}\n\n@inproceedings{kwon-sosp2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2309.06180},\n}\n\n@inproceedings{math500-neurips2021,\n    title     = {Measuring Mathematical Problem Solving With the {MATH} Dataset},\n    author    = {Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2021},\n    url       = {https://arxiv.org/abs/2103.03874},\n}\n\n@inproceedings{michel-neurips2019,\n    title     = {Are Sixteen Heads Really Better than One?},\n    author    = {Michel, Paul and Levy, Omer and Neubig, Graham},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1905.10650},\n}\n\n@inproceedings{mustafar-neurips2025,\n    title     = {Mustafar: Promoting Unstructured Sparsity for {KV} Cache Pruning in {LLM} Inference},\n    author    = {Joo, Donghyeon and Hosseini, Helya and Hadidi, Ramyad and Asgari, Bahar},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.22913},\n}\n\n@inproceedings{nacl-acl2024,\n    title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},\n    author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2408.03675},\n}\n\n@article{obcache-2025,\n    title   = {{OBCache}: Optimal Brain {KV} Cache Pruning for Efficient Long-Context {LLM} Inference},\n    author  = {Gu, Yuzhe and Liang, Xiyu and Zhao, Jiaojiao and Diao, Enmao},\n    journal = {arXiv preprint arXiv:2510.07651},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.07651},\n}\n\n@inproceedings{pagedeviction-eacl2026,\n    title     = {{PagedEviction}: Structured Block-wise {KV} Cache Pruning for Efficient Large Language Model Inference},\n    author    = {Chitty-Venkata, Krishna Teja and Ye, Jie and Sun, Xian-He and Kougkas, Anthony and Emani, Murali and Vishwanath, Venkatram and Nicolae, Bogdan},\n    booktitle = {Findings of the European Chapter of the Association for Computational Linguistics},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2509.04377},\n}\n\n@article{phase-transition-compression-2026,\n    title   = {Phase transitions in large language model compression},\n    author  = {Ma, Ziyang and Li, Zuchao and Zhang, Lefei and Xia, Gui-Song and Du, Bo and Zhang, Liangpei and Tao, Dacheng},\n    journal = {npj Artificial Intelligence},\n    volume  = {2},\n    number  = {21},\n    year    = {2026},\n    url     = {https://www.nature.com/articles/s44387-026-00072-8},\n}\n\n@inproceedings{pope-mlsys2023,\n    title     = {Efficiently Scaling Transformer Inference},\n    author    = {Pope, Reiner and Douglas, Sholto and Chowdhery, Aakanksha and Devlin, Jacob and Bradbury, James and Heek, Jonathan and Xiao, Kefan and Agrawal, Shivani and Dean, Jeff},\n    booktitle = {Proceedings of Machine Learning and Systems},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2211.05102},\n}\n\n@article{pyramidkv-2024,\n    title   = {{PyramidKV}: Dynamic {KV} Cache Compression based on Pyramidal Information Funneling},\n    author  = {Cai, Zefan and Zhang, Yichi and Gao, Bofei and Liu, Yuliang and Liu, Tianyu and Lu, Keming and Xiong, Wayne and Dong, Yue and Chang, Baobao and Hu, Junjie and Xiao, Wen},\n    journal = {arXiv preprint arXiv:2406.02069},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2406.02069},\n}\n\n@article{qwen25-2024,\n    title   = {{Qwen2.5} Technical Report},\n    author  = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Wei, Haoran and others},\n    journal = {arXiv preprint arXiv:2412.15115},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2412.15115},\n}\n\n@inproceedings{raas-acl2025,\n    title     = {{RaaS}: Reasoning-Aware Attention Sparsity for Efficient {LLM} Reasoning},\n    author    = {Hu, Junhao and Huang, Wenrui and Wang, Weidong and Li, Zhenwen and Hu, Tiancheng and Liu, Zhixia and Chen, Xusheng and Xie, Tao and Shan, Yizhou},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2502.11147},\n}\n\n@article{retentivekv-2026,\n    title   = {{RetentiveKV}: State-Space Memory for Uncertainty-Aware Multimodal {KV} Cache Eviction},\n    author  = {Liu, Sihao and Xiong, YuFan and Jiang, Zhonghua and Wang, Zhaode and Lv, Chengfei and Zhang, Shengyu},\n    journal = {arXiv preprint arXiv:2605.04075},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2605.04075},\n}\n\n@inproceedings{slim-icml2025,\n    title     = {{SLiM}: One-shot Quantization and Sparsity with Low-rank Approximation for {LLM} Weight Compression},\n    author    = {Mozaffari, Mohammad and Yazdanbakhsh, Amir and Dehnavi, Maryam Mehri},\n    booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2410.09615},\n}\n\n@inproceedings{snapkv-neurips2024,\n    title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},\n    author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2404.14469},\n}\n\n\n@inproceedings{spark-aaai2026,\n    title     = {{SparK}: Query-Aware Unstructured Sparsity with Recoverable {KV} Cache Channel Pruning},\n    author    = {Liao, Huanxuan and Xu, Yixing and He, Shizhu and Li, Guanchen and Yin, Xuanwu and Li, Dong and Barsoum, Emad and Zhao, Jun and Liu, Kang},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.15212},\n}\n\n@article{sparse-frontier-2025,\n    title   = {The Sparse Frontier: Sparse Attention Trade-offs in Transformer {LLMs}},\n    author  = {Nawrot, Piotr and Li, Robert and Huang, Renjie and Ruder, Sebastian and Marchisio, Kelly and Ponti, Edoardo M.},\n    journal = {arXiv preprint arXiv:2504.17768},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2504.17768},\n}\n\n@inproceedings{thinkv-iclr2026,\n    title     = {{ThinKV}: Thought-Adaptive {KV} Cache Compression for Efficient Reasoning Models},\n    author    = {Ramachandran, Akshat and Neseem, Marina and Sakr, Charbel and Venkatesan, Rangharajan and Khailany, Brucek and Krishna, Tushar},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2510.01290},\n}\n\n@article{unicomp-2026,\n    title   = {{UniComp}: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation},\n    author  = {von Rad, Jonathan and Cao, Yong and Geiger, Andreas},\n    journal = {arXiv preprint arXiv:2602.09130},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2602.09130},\n}\n\n@inproceedings{voita-acl2019,\n    title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n    author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1905.09418},\n}\n",
      "numLines": 247,
      "startLine": 1,
      "totalLines": 247
    }
  }
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778775000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "33f17cb8-3583-44b7-999f-98a28a870adf",
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368"
}
```

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Let me extract the citation keys from the tex files and the bib keys, then compare.

From the tex grep output, let me extract all citation keys:

From tex files:
- spark-aaai2026
- slim-icml2025
- unicomp-2026
- phase-transition-compression-2026
- graspune-acl2026
- adakv-neurips2025
- snapkv-neurips2024
- defensivekv-iclr2026
- nacl-acl2024
- retentivekv-2026
- greedy-bias-kvcache-2026


- thinkv-iclr2026
- decision-repr-transition-2026
- doing-more-with-less-2026
- sparse-frontier-2025
- math500-neurips2021
- efron-1993
- voita-acl2019
- michel-neurips2019
- kwon-sosp2023
- pope-mlsys2023

I should also check the methodology.tex and background.tex files directly to make sure I'm capturing all the citations, since some lines might have been cut off in the grep output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "aac43c19-8e5d-44c3-9940-b5872a56f100",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 15_

Some lines were omitted in the grep. Let me read the files with long lines to get complete citation coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "b7bd11f9-605b-462f-bba0-3834ecd7ac7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_018NApNg2k14VPicsyDQWNQV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "8a3a64a3-b55a-4511-8641-ac05ff09fe64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 17 · 2026-05-14T13:21:35.175Z_

<details><summary>↩ Tool result · `toolu_018NApNg2k14VPicsyDQWNQV`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\cite{efron-1993}. Paired bootstrap controls for problem-level variance. All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.\footnote{Experiments on 4$\times$ NVIDIA RTX PRO 6000 Blackwell 96\,GB GPUs.}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "9c99f6b7-541a-4639-a646-635fe911bd85",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\paragraph{Models.}\n\\label{sec:models}\nWe evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \\textbf{DeepSeek-R1-Distill-Qwen-7B}~\\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \\textbf{Qwen2.5-7B-Instruct}~\\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \\texttt{bfloat16} with eager attention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values; \\texttt{bfloat16} eliminated all occurrences.}\n\n\\paragraph{Dataset.}\n\\label{sec:dataset}\nWe use 50 problems stratified from MATH-500~\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\n\n\\paragraph{Sparsity configuration.}\n\\label{sec:sparsity-config}\nWe apply symmetric compound sparsity at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \\emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\\ref{eq:kv-importance}; BOS always retained) and \\emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.\n\n\\paragraph{Phase segmentation and metrics.}\n\\label{sec:phase-seg}\nEach sequence is segmented into three phases using the quantile-based method (\\S\\ref{sec:phase-segmentation}), with $\\texttt{min\\_phase\\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\\ref{eq:ii}), and $G$ (Eq.~\\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).\n\n\\paragraph{Statistical analysis.}\n\\label{sec:stats}\nAll confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\cite{efron-1993}. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.\\footnote{Experiments on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\,GB GPUs.}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01GqKKLSMfJFmDzA7wxugfuo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "4a191646-08c7-4026-bffe-fb87df12bed1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 19 · 2026-05-14T13:21:35.681Z_

<details><summary>↩ Tool result · `toolu_01GqKKLSMfJFmDzA7wxugfuo`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.
22	
23	\paragraph{Severity gradient.}
24	To capture phase variation:
25	\begin{equation}
26	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
27	    \label{eq:gradient}
28	\end{equation}
29	where $\widetilde{\mathrm{II}}_{\,\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \gg 1$ indicates phase-concentrated severity.
30	
31	\paragraph{Phase segmentation.}
32	\label{sec:phase-segmentation}
33	Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\ref{app:formulation-details}.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "0a283e0b-de4c-48b1-8751-f13ff6ed523c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Full formulation details in Appendix (app:formulation-details).\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\\ref{app:formulation-details}.\n\n\\paragraph{Compound sparsity.}\n\\label{sec:compound-sparsity}\nLet $s \\in (0,1)$ denote a unified sparsity budget. \\emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \\cite{voita-acl2019, michel-neurips2019}. \\emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \\emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\\ref{eq:kv-importance} in Appendix~\\ref{app:formulation-details}), and \\emph{random}, which evicts uniformly at random. Applying both simultaneously yields \\emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \\cite{spark-aaai2026}.\n\n\\paragraph{Interaction Index.}\n\\label{sec:interaction-index}\nFor a text segment, let $\\text{PPL}_c$ denote perplexity under condition $c \\in \\{d, a, k, b\\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \\text{PPL}_c / \\text{PPL}_d$, and:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.\n\n\\paragraph{Severity gradient.}\nTo capture phase variation:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \\gg 1$ indicates phase-concentrated severity.\n\n\\paragraph{Phase segmentation.}\n\\label{sec:phase-segmentation}\nEach generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\\ref{app:formulation-details}.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_013yWLkz7qjpwruYTcCzQwdp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "f207ecd9-2d98-4f69-8a68-9b90941eb0d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 21 · 2026-05-14T13:21:36.657Z_

<details><summary>↩ Tool result · `toolu_013yWLkz7qjpwruYTcCzQwdp`</summary>

```text
1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	\subsection{Discrimination Collapse}
5	\label{sec:discrimination-collapse}
6	
7	Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
8	
9	\begin{table}[t]
10	\centering
11	\caption{Discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
12	\label{tab:discrimination-metrics-full}
13	\small
14	\begin{tabular}{llrr}
15	\toprule
16	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
17	\midrule
18	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
19	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
20	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
21	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
22	\midrule
23	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
24	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
25	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
26	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
32	
33	\subsection{Entropy Redistribution}
34	\label{sec:entropy-redistribution}
35	
36	Beyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
37	\begin{equation}
38	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
39	    \label{eq:attn-entropy}
40	\end{equation}
41	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
42	
43	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.040, -0.047]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek
44	
45	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen
46	
47	We characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
48	
49	\begin{table}[t]
50	\centering
51	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
52	\label{tab:entropy-deltas}
53	\small
54	\begin{tabular}{llr}
55	\toprule
56	Model & $s$ & $\Delta\mathcal{H}$ \\
57	\midrule
58	DeepSeek & $0.15$ & $-0.040$ \\
59	DeepSeek & $0.20$ & $-0.047$ \\
60	DeepSeek & $0.25$ & $-0.045$ \\
61	DeepSeek & $0.30$ & $-0.044$ \\
62	\midrule
63	Qwen & $0.15$ & $-0.073$ \\
64	Qwen & $0.20$ & $-0.076$ \\
65	Qwen & $0.25$ & $+0.045$ \\
66	Qwen & $0.30$ & $-0.007$ \\
67	\bottomrule
68	\end{tabular}
69	\end{table}
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "13c62468-f420-48bc-95c3-4483ab5d58a0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{sec:analysis}\n\n\\subsection{Discrimination Collapse}\n\\label{sec:discrimination-collapse}\n\nHead pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\\times$ 4 sparsity levels $\\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse under importance-based eviction. $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\n\\label{tab:discrimination-metrics-full}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\\subsection{Entropy Redistribution}\n\\label{sec:entropy-redistribution}\n\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nand compute $\\Delta\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\n\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.040, -0.047]$; Table~\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\n\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\Delta\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\n\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\n\\label{tab:entropy-deltas}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nModel & $s$ & $\\Delta\\mathcal{H}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.040$ \\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.073$ \\\\\nQwen & $0.20$ & $-0.076$ \\\\\nQwen & $0.25$ & $+0.045$ \\\\\nQwen & $0.30$ & $-0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_018rHCCgWZqjUyDCbesPx3Z7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "fd3af72e-8edd-414f-aace-804ed0fcf702",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 23 · 2026-05-14T13:21:37.138Z_

<details><summary>↩ Tool result · `toolu_018rHCCgWZqjUyDCbesPx3Z7`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation.
9	
10	\paragraph{Cross-model robustness.}
11	The pattern replicates with perfect ordinal agreement across both models (Spearman $\rho{=}1.0$; gradient permutation $p{=}0.043$), though Qwen's magnitudes are ${\sim}1/5$ of DeepSeek's. The onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ ($d_z{=}0.44$), while Qwen's becomes significant only at $s \geq 0.20$ ($d_z{=}0.55$). We conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale. Discrimination collapse (Gini/CV reduction) is consistent across all conditions; the entropy redistribution component is model-dependent, with Qwen showing a sign reversal at $s{=}0.25$. We characterize discrimination collapse as the robust driver, with entropy redistribution as a secondary, model-specific amplifier. % exp_id: cross_model_correlation; mechanism_entropy_qwen; cohens_d_bf16.json, cohens_d_bf16_qwen.json
12	
13	\paragraph{Architecture generality.}
14	Discrimination collapse depends on: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~a sufficient number of pruned heads to degrade the importance distribution. Both are shared by major KV cache methods (H$_2$O, SnapKV, PyramidKV) and by any autoregressive transformer producing extended reasoning. The entropy redistribution component, while consistent in DeepSeek, appears model-dependent.
15	
16	\paragraph{Testable prediction.}
17	Any importance metric derived from attention mass should exhibit discrimination collapse under head pruning, with severity gradient scaling with pruning-induced Gini decrease. Metrics deriving importance from sources independent of attention---such as activation magnitude or gradient-based saliency---should produce flatter severity gradients.
18	
19	\paragraph{Future directions.}
20	A \emph{phase-gated controller} that monitors attention sparsity in real time and dynamically adjusts compound sparsity per phase could mitigate severity amplification while preserving compression gains where compound behavior is near-additive. Scaling to larger models and diverse reasoning tasks would establish generality. Extended discussion in Appendix~\ref{app:extended-discussion}.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "0894dc52-9670-461d-812b-0319ca183dd9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Quantitative surprise.}\nWhile the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \\approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\n\\paragraph{Implications for deployment.}\nApplying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \\emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \\gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation.\n\n\\paragraph{Cross-model robustness.}\nThe pattern replicates with perfect ordinal agreement across both models (Spearman $\\rho{=}1.0$; gradient permutation $p{=}0.043$), though Qwen's magnitudes are ${\\sim}1/5$ of DeepSeek's. The onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ ($d_z{=}0.44$), while Qwen's becomes significant only at $s \\geq 0.20$ ($d_z{=}0.55$). We conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale. Discrimination collapse (Gini/CV reduction) is consistent across all conditions; the entropy redistribution component is model-dependent, with Qwen showing a sign reversal at $s{=}0.25$. We characterize discrimination collapse as the robust driver, with entropy redistribution as a secondary, model-specific amplifier. % exp_id: cross_model_correlation; mechanism_entropy_qwen; cohens_d_bf16.json, cohens_d_bf16_qwen.json\n\n\\paragraph{Architecture generality.}\nDiscrimination collapse depends on: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~a sufficient number of pruned heads to degrade the importance distribution. Both are shared by major KV cache methods (H$_2$O, SnapKV, PyramidKV) and by any autoregressive transformer producing extended reasoning. The entropy redistribution component, while consistent in DeepSeek, appears model-dependent.\n\n\\paragraph{Testable prediction.}\nAny importance metric derived from attention mass should exhibit discrimination collapse under head pruning, with severity gradient scaling with pruning-induced Gini decrease. Metrics deriving importance from sources independent of attention---such as activation magnitude or gradient-based saliency---should produce flatter severity gradients.\n\n\\paragraph{Future directions.}\nA \\emph{phase-gated controller} that monitors attention sparsity in real time and dynamically adjusts compound sparsity per phase could mitigate severity amplification while preserving compression gains where compound behavior is near-additive. Scaling to larger models and diverse reasoning tasks would establish generality. Extended discussion in Appendix~\\ref{app:extended-discussion}.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01ND3izQCBhmW3U3r25XSQ8B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "189f7175-8fac-4306-bf30-09c9194c62ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 25 · 2026-05-14T13:21:37.617Z_

<details><summary>↩ Tool result · `toolu_01ND3izQCBhmW3U3r25XSQ8B`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{\times}$ at all sparsity levels. Figure~\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
30	
31	\begin{table*}[t]
32	\centering
33	\small
34	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
35	\label{tab:main-results}
36	\begin{tabular}{@{}llccccr@{}}
37	\toprule
38	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
39	\midrule
40	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
41	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
42	\addlinespace
43	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
44	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
45	\addlinespace
46	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
47	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
48	\addlinespace
49	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
50	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
51	\bottomrule
52	\end{tabular}
53	\end{table*}
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{fig1_dose_response.pdf}
58	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\times}$ to $274{\times}$; random eviction (dashed) remains flat near $1{\times}$. Shaded regions: 95\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030
59	\label{fig:hero}
60	\end{figure}
61	
62	
63	\subsection{Phase-Strategy Crossover}
64	\label{sec:crossover}
65	
66	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
67	
68	\begin{figure}[t]
69	\centering
70	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
71	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
72	\label{fig:crossover}
73	\end{figure}
74	
75	
76	\subsection{Cross-Model Replication}
77	\label{sec:cross-model}
78	
79	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
80	
81	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
82	
83	Qwen reproduces the monotonic severity gradient: $\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\sim}1/5$ the magnitude (Table~\ref{tab:cross-model}). Both models yield strictly increasing $d_z$ trajectories (Spearman $\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$). Per-problem concordance analysis appears in Appendix~\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
84	
85	\begin{table}[t]
86	\centering
87	\small
88	\caption{Cross-model comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
89	\label{tab:cross-model}
90	\begin{tabular}{@{}lcccc@{}}
91	\toprule
92	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
93	\midrule
94	DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030
95	Qwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\ % exp_id: bf16_qw_imp_s015..s030
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	
100	\begin{figure}[t]
101	\centering
102	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
103	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
104	\label{fig:cross-model}
105	\end{figure}
106	
107	
108	\subsection{Statistical Validation}
109	\label{sec:stat-validation}
110	
111	\paragraph{Distribution characterization.}
112	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen. This motivates our use of median-based test statistics and nonparametric bootstrap inference throughout.
113	
114	\paragraph{Permutation test.}
115	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons. The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
116	
117	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
118	
119	\begin{table}[t]
120	\centering
121	\small
122	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}
123	\label{tab:permutation}
124	\begin{tabular}{@{}rrcl@{}}
125	\toprule
126	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
127	\midrule
128	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015
129	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020
130	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025
131	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
139	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}
140	\label{fig:permtest-forest}
141	\end{figure}
142	
143	\paragraph{Effect sizes.}
144	Table~\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$). At higher sparsity ($s \geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance yielding larger standardized differences despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs ($B{=}10{,}000$).}
150	\label{tab:cohens-d}
151	\begin{tabular}{@{}lcccc@{}}
152	\toprule
153	$s$ & DS $d_z$ & $\widetilde{\Delta}$ [CI] & QW $d_z$ & $\widetilde{\Delta}$ [CI] \\
154	\midrule
155	0.15 & 0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05\; $[-0.01, 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015
156	0.20 & 0.52 & 1.15\; $[0.66, 1.26]$ & 0.55 & 0.21\; $[0.07, 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020
157	0.25 & 0.68 & 3.97\; $[2.83, 5.29]$ & 0.89 & 1.11\; $[0.61, 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025
158	0.30 & 0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030
159	\bottomrule
160	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.}
161	\end{tabular}
162	\end{table}
163	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "e7cb2abf-dfd6-40b7-9467-174466d7eb93",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity}\n\\label{sec:strategy-severity}\n\nTable~\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Phase-Modulated Amplification}\n\\label{sec:phase-amplification}\n\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\approx 0.9$--$1.7{\\times}$ at all sparsity levels. Figure~\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$; random eviction (dashed) remains flat near $1{\\times}$. Shaded regions: 95\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\n\n\\subsection{Phase-Strategy Crossover}\n\\label{sec:crossover}\n\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\ref{fig:crossover}): importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but \\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\S\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n\\label{fig:crossover}\n\\end{figure}\n\n\n\\subsection{Cross-Model Replication}\n\\label{sec:cross-model}\n\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek).\n\nQwen reproduces the monotonic severity gradient: $\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\sim}1/5$ the magnitude (Table~\\ref{tab:cross-model}). Both models yield strictly increasing $d_z$ trajectories (Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). Per-problem concordance analysis appears in Appendix~\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model comparison of median compound severity difference ($\\Delta$) under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\n\\paragraph{Distribution characterization.}\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen. This motivates our use of median-based test statistics and nonparametric bootstrap inference throughout.\n\n\\paragraph{Permutation test.}\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons. The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$); at $s \\geq 0.20$, no permutation exceeds the observed statistic.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\\paragraph{Effect sizes.}\nTable~\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). At higher sparsity ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance yielding larger standardized differences despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 163,
      "startLine": 1,
      "totalLines": 163
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01RTvBmwrsd9cJV4n82TP4vd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "728cf5b2-9096-4635-abea-d8ce85839c03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 27 · 2026-05-14T13:21:38.151Z_

<details><summary>↩ Tool result · `toolu_01RTvBmwrsd9cJV4n82TP4vd`</summary>

```text
1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\{\sigma_i\}$; segments shorter than 10 tokens are merged into adjacent phases.
34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\mathrm{II}_{\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$), while random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.
39	
40	% Bootstrap and permutation details moved to main text \S\ref{sec:stat-validation}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "6befd7bf-2ac6-457f-99c5-57008739c3b0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
      "content": "\\section{Compound Sparsity Formulation}\n\\label{app:formulation-details}\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\n\\begin{equation}\n    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n    \\label{eq:kv-importance}\n\\end{equation}\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\paragraph{Attention sparsity metric.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\n\n\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}\n\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\mathrm{II}_{\\times} = r_b - r_a \\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\mathrm{II}_{\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\times} = 58$--$241{\\times}$), while random eviction remains flat ($G_{\\times} \\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\n\n% Bootstrap and permutation details moved to main text \\S\\ref{sec:stat-validation}\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01RXQw9bj5LdVZpwVFM2VjoT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "9b1479ed-e4c3-4cc1-80e4-85a367946e2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 29 · 2026-05-14T13:21:39.165Z_

<details><summary>↩ Tool result · `toolu_01RXQw9bj5LdVZpwVFM2VjoT`</summary>

```text
1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "59681b9f-8c48-4ee8-8710-d649b9ac5ad2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
      "content": "% Appendix: supplementary results details\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01XbzAFUqMxR5RxSq2BZCYBv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "696c7195-409f-4a0c-bf85-44b460656123",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 31 · 2026-05-14T13:21:39.623Z_

<details><summary>↩ Tool result · `toolu_01XbzAFUqMxR5RxSq2BZCYBv`</summary>

```text
1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.
18	
19	
20	\section{Extended Limitations}
21	\label{app:limitations}
22	
23	\paragraph{Model scale.}
24	All experiments are conducted at the 7B parameter scale.
25	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
26	Larger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
27	% REVIEWER-ATTACK: "7B is too small to be relevant for production."
28	% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
29	
30	\paragraph{Architectural scope.}
31	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
32	The cross-model replication (\S\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.
33	The entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.
34	% REVIEWER-ATTACK: "Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM."
35	% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.
36	
37	\paragraph{Task coverage.}
38	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
39	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
40	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
41	% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
42	% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
43	
44	\paragraph{Statistical scope.}
45	Bootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
46	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
47	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]
48	
49	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
50	This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
51	
52	\paragraph{Sparsity range.}
53	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, a moderate range representative of practical deployment targets.
54	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
55	Conversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.
56	% REVIEWER-ATTACK: "Why not test higher sparsity? 0.30 is conservative."
57	% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
58	
59	\paragraph{No throughput evaluation.}
60	This work focuses on characterizing the \emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.
61	We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.
62	% REVIEWER-ATTACK: "No system evaluation. How do we know the severity amplification matters for real deployment?"
63	% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
64	
65	% Entropy redistribution analysis moved to main text \S\ref{sec:entropy-redistribution}
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "02692845-eb34-45ab-b843-6aae83be5a2e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\\section{Discrimination Collapse Details}\n\\label{app:discrimination-collapse-details}\n\nThis cross-model consistency (Table~\\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\n\n\\paragraph{Random masking as falsification control.}\nRandom eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n\n\\paragraph{Entropy mechanism boundary conditions.}\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.\nThe entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nThis work focuses on characterizing the \\emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.\nWe do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\n\n% Entropy redistribution analysis moved to main text \\S\\ref{sec:entropy-redistribution}\n",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01PdrR5aNt7q1cu557C2zPNE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "d9e70f31-c292-4462-9ee8-b647e94c4255",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ea82nxaB485S8DbMCdUYGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6729,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6729
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

_source line 33 · 2026-05-14T13:21:40.173Z_

<details><summary>↩ Tool result · `toolu_01PdrR5aNt7q1cu557C2zPNE`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) with attenuated magnitude. Discrimination collapse provides a robust mechanistic explanation confirmed across both models.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	
7	\section*{Limitations}
8	\label{sec:limitations}
9	
10	\paragraph{Model scale and architecture.}
11	All experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Both models share the Qwen2ForCausalLM architecture; while the cross-model replication (\S\ref{sec:cross-model}) confirms the findings are not artifacts of a single model's weights, empirical validation on architecturally distinct designs (e.g., LLaMA~3, Mistral, or multi-latent attention) is needed.
12	
13	\paragraph{Task coverage.}
14	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
15	
16	\paragraph{Mechanism.}
17	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
18	
19	\paragraph{Sparsity range.}
20	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "fb8c7432-2cbf-46c7-808c-b2a4a0cf6185",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\times}$ to $274{\\times}$ across sparsity levels ($d_z$: $0.44 \\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$) with attenuated magnitude. Discrimination collapse provides a robust mechanistic explanation confirmed across both models.\nThese findings motivate phase-aware sparsity allocation for reasoning model deployment.\n\n\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Model scale and architecture.}\nAll experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Both models share the Qwen2ForCausalLM architecture; while the cross-model replication (\\S\\ref{sec:cross-model}) confirms the findings are not artifacts of a single model's weights, empirical validation on architecturally distinct designs (e.g., LLaMA~3, Mistral, or multi-latent attention) is needed.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\n\n\\paragraph{Mechanism.}\nThe discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\ref{app:limitations}.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the remaining tex files for citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "d5c9f9e4-c728-4441-8603-f5b94b0e84a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTuXwfNN5NPynm7ruNFKtN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15575,
      "cache_read_input_tokens": 30162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15575
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

_source line 35_

Now let me check the remaining files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "f04f6739-32dc-40ce-a71e-8ccf2e3c1e34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTuXwfNN5NPynm7ruNFKtN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15575,
      "cache_read_input_tokens": 30162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15575
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

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01JZroGF3VQ2CFDuaHNnFUTJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "51263a33-be0b-4e11-8361-d68925384237",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTuXwfNN5NPynm7ruNFKtN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15575,
      "cache_read_input_tokens": 30162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15575
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

_source line 37 · 2026-05-14T13:21:45.321Z_

<details><summary>↩ Tool result · `toolu_01JZroGF3VQ2CFDuaHNnFUTJ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
9	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
10	
11	We show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.
12	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.
13	On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).
14	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$).
15	Critically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.
16	
17	We propose \emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
18	Random eviction is immune because its decisions are independent of attention patterns.
19	Our contributions:
20	\begin{enumerate}[nosep,leftmargin=*]
21	    \item We identify a \textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:results}).
22	    \item We show this gradient \textbf{increases monotonically with sparsity} and replicates across two models with different training regimes (\S\ref{sec:results}).
23	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation (\S\ref{sec:discrimination-collapse}).
24	\end{enumerate}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "51484f39-0d03-4533-8948-30b1c9f82682",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses---\\emph{attention head pruning} \\cite{voita-acl2019, michel-neurips2019} and \\emph{KV cache eviction} \\cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work treats compound interaction magnitude as roughly constant across generation \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.\n\nWe show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.\nUnder importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.\nOn DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$).\nCritically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.\n\nWe propose \\emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nRandom eviction is immune because its decisions are independent of attention patterns.\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show this gradient \\textbf{increases monotonically with sparsity} and replicates across two models with different training regimes (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation (\\S\\ref{sec:discrimination-collapse}).\n\\end{enumerate}\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_018JeMfNP2w66LBmmMyfvzBz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "74a168ff-c400-42b2-9053-4bb6c70ca159",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTuXwfNN5NPynm7ruNFKtN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15575,
      "cache_read_input_tokens": 30162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15575
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

_source line 39 · 2026-05-14T13:21:45.860Z_

<details><summary>↩ Tool result · `toolu_018JeMfNP2w66LBmmMyfvzBz`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
11	
12	\paragraph{KV cache eviction.}
13	Most methods rely on importance scoring whose reliability is increasingly questioned.
14	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
15	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
16	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
17	These conditions are characterized in terms of aggregation or metric choice---not reasoning phase or interaction with head pruning.
18	
19	\paragraph{Phase-aware inference.}
20	ThinKV~\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.
21	\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\ ``decisive'' representation phases.
22	\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.
23	These works establish phase-dependent compression tolerance along single axes.
24	Our work bridges this by quantifying how compound severity varies across phases and eviction strategies.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "f836b68a-75b5-4568-a2b1-5198289adc7f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Compound compression.}\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\cite{slim-icml2025} formalize compound error for quantization and sparsity.\n\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.\n\\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.\nGRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.\nThese works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.\n\n\\paragraph{KV cache eviction.}\nMost methods rely on importance scoring whose reliability is increasingly questioned.\nAda-KV~\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\cite{snapkv-neurips2024} compresses from a fixed observation window; \\cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\\times}$ higher than expected under standard aggregation.\n\\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.\nRetentiveKV~\\cite{retentivekv-2026} identifies deferred importance, and \\cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.\nThese conditions are characterized in terms of aggregation or metric choice---not reasoning phase or interaction with head pruning.\n\n\\paragraph{Phase-aware inference.}\nThinKV~\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.\n\\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\\ ``decisive'' representation phases.\n\\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.\nThese works establish phase-dependent compression tolerance along single axes.\nOur work bridges this by quantifying how compound severity varies across phases and eviction strategies.\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01EbBPpqU6x2t2qZK443Yfwc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "ac4befda-ad3b-41d9-8fdb-7f1fdc8d5989",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTuXwfNN5NPynm7ruNFKtN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15575,
      "cache_read_input_tokens": 30162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15575
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

_source line 41 · 2026-05-14T13:21:46.340Z_

<details><summary>↩ Tool result · `toolu_01EbBPpqU6x2t2qZK443Yfwc`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).
11	
12	We propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
13	These findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.
14	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "5e34d664-494a-4f0c-83fa-efe384ae2942",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01HATn2UQjVXw5qM6LTZzHuG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "86968d03-773e-4753-98f8-5daa5c9fb845",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTuXwfNN5NPynm7ruNFKtN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15575,
      "cache_read_input_tokens": 30162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15575
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

_source line 43 · 2026-05-14T13:21:46.711Z_

<details><summary>↩ Tool result · `toolu_01HATn2UQjVXw5qM6LTZzHuG`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	\input{related_work}
33	\input{background}
34	\input{methodology}
35	\input{results}
36	\input{analysis}
37	\input{discussion}
38	\input{conclusion}
39	
40	\bibliography{references}
41	
42	\appendix
43	\input{appendix}
44	\input{appendix_results}
45	\input{appendix_disc_analysis}
46	
47	\end{document}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "dc9b508c-1dac-433c-b982-8a2da4631cc9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\n\\graphicspath{{figures/}}\n\n\\title{Phase-Modulated Compound Sparsity:\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\\input{appendix_results}\n\\input{appendix_disc_analysis}\n\n\\end{document}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me compile the results.

**Citations found in tex files:**

From introduction.tex:
- kwon-sosp2023
- pope-mlsys2023
- voita-acl2019
- michel-neurips2019
- snapkv-neurips2024
- adakv-neurips2025
- spark-aaai2026
- slim-icml2025
- unicomp-2026
- thinkv-iclr2026
- decision-repr-transition-2026


- spark-aaai2026
- slim-icml2025
- unicomp-2026
- phase-transition-compression-2026
- graspune-acl2026
- adakv-neurips2025
- snapkv-neurips2024
- defensivekv-iclr2026
- nacl-acl2024
- retentivekv-2026
- greedy-bias-kvcache-2026
- thinkv-iclr2026
- decision-repr-transition-2026
- doing-more-with-less-2026
- sparse-frontier-2025

From background.tex, I'm seeing the start of another citation list that appears to be cut off.

Now I'm compiling the full citation inventory across all sections. The methodology section pulls in some newer work like deepseek-r1-2025 and qwen25-2024, while the appendix consolidates several key references. I'm noticing that several sections—abstract, results, analysis, discussion, and conclusion—don't have any citations at all, which suggests the paper is still in development. I'm continuing to compile the bibliography entries, adding more recent papers on KV cache optimization and compression techniques, including some 2025 and 2026 publications that weren't in the previous list.

Now I'm checking which citations are actually used in the tex file versus what's in the bibliography — looks like there are 7 entries that made it into the bib but aren't cited anywhere in the document, so those could be removed to clean things up.

I'm also verifying that each bibliography entry has the essential fields like title, author, and year to ensure completeness. I'm continuing to verify the bibliography entries, checking off title, author, and year for each remaining paper through entry 20. kv-2024 — title ✓, author ✓, year ✓
21. qwen25-2024 — title ✓, author ✓, year ✓
22. raas-acl2025 — title ✓, author ✓, year ✓
23. retentivekv-2026 — title ✓, author ✓, year ✓
24. slim-icml2025 — title ✓, author ✓, year ✓
25. snapkv-neurips2024 — title ✓, author ✓, year ✓
26. spark-aaai2026 — title ✓, author ✓, year ✓
27. sparse-frontier-2025 — title ✓, author ✓, year ✓
28. thinkv-iclr2026 — title ✓, author ✓, year ✓
29. unicomp-2026 — title ✓, author ✓, year ✓
30. voita-acl2019 — title ✓, author ✓, year ✓

All entries verified and complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "982e425e-1ecf-4d98-bcde-56be50600160",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmPvCnN6GPsMJGNYb2iVNU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3032,
      "cache_read_input_tokens": 45737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3032
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

_source line 45_

## 引用完整性报告

### Critical: 缺失引用（tex 中引用但 bib 中无条目）

**无。** 全部 23 个引用 key 在 `references.bib` 中均有对应条目。

### Info: 未使用引用（bib 中有但 tex 中未引用）

7 条：
| Key | Title |
|-----|-------|
| `compression-ordering-2025` | A Systematic Study of Compression Ordering for LLMs |
| `h2o-neurips2023` | H₂O: Heavy-Hitter Oracle for Efficient Generative Inference |
| `mustafar-neurips2025` | Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning |
| `obcache-2025` | OBCache: Optimal Brain KV Cache Pruning |
| `pagedeviction-eacl2026` | PagedEviction: Structured Block-wise KV Cache Pruning |
| `pyramidkv-2024` | PyramidKV: Dynamic KV Cache Compression |
| `raas-acl2025` | RaaS: Reasoning-Aware Attention Sparsity |

注：`h2o-neurips2023` 和 `pyramidkv-2024` 在 `discussion.tex` 正文中以文字形式提及（"H₂O, SnapKV, PyramidKV"），但未用 `\cite{}` 引用。可考虑补上 `\cite`。

### Warning: 格式不完整的 bib 条目

**无。** 全部 30 条 bib 条目均包含 title、author、year 三个必需字段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "uuid": "9d648b25-e15c-409b-ac08-489b1ded7bbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmPvCnN6GPsMJGNYb2iVNU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3032,
      "cache_read_input_tokens": 45737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3032
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

### Task result

_source line 46_

## 引用完整性报告

### Critical: 缺失引用（tex 中引用但 bib 中无条目）

**无。** 全部 23 个引用 key 在 `references.bib` 中均有对应条目。

### Info: 未使用引用（bib 中有但 tex 中未引用）

7 条：
| Key | Title |
|-----|-------|
| `compression-ordering-2025` | A Systematic Study of Compression Ordering for LLMs |
| `h2o-neurips2023` | H₂O: Heavy-Hitter Oracle for Efficient Generative Inference |
| `mustafar-neurips2025` | Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning |
| `obcache-2025` | OBCache: Optimal Brain KV Cache Pruning |
| `pagedeviction-eacl2026` | PagedEviction: Structured Block-wise KV Cache Pruning |
| `pyramidkv-2024` | PyramidKV: Dynamic KV Cache Compression |
| `raas-acl2025` | RaaS: Reasoning-Aware Attention Sparsity |

注：`h2o-neurips2023` 和 `pyramidkv-2024` 在 `discussion.tex` 正文中以文字形式提及（"H₂O, SnapKV, PyramidKV"），但未用 `\cite{}` 引用。可考虑补上 `\cite`。

### Warning: 格式不完整的 bib 条目

**无。** 全部 30 条 bib 条目均包含 title、author、year 三个必需字段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 61704,
  "duration_api_ms": 62547,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "5881f369-bfaa-41ba-8896-cbac8a19f368",
  "total_cost_usd": 0.40884250000000005,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 37322,
    "cache_read_input_tokens": 133770,
    "output_tokens": 4304,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37322,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2461,
        "cache_read_input_tokens": 45737,
        "cache_creation_input_tokens": 3032,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3032
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 990,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00106,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 4304,
      "cacheReadInputTokens": 133770,
      "cacheCreationInputTokens": 37322,
      "webSearchRequests": 0,
      "costUSD": 0.40778250000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b7d2a2d4-afd4-40ec-a9f6-a497c5ef06b2"
}
```

</details>

---
