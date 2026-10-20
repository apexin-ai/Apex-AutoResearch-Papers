# paper table7 update m004

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_paper_table7_update_m004_20260518T122421.log`
- **Structured JSON:** [`71914a2492e4ab8b71eb.json`](../../sessions/71/71914a2492e4ab8b71eb.json)

## Before a recorded user message

52 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "45b544d9-3c6d-4ffe-ade2-9b8b28019551",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1779124800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "405459f4-4f16-4215-a109-ab5e5724e584",
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13"
}
```

---

### Assistant

_source line 4_

I'll start by reading the relevant files on the remote server to understand the current state before making changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "85be3f8f-345d-480d-a0cc-70c77a5ed0fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQJcmcMBXdGVUWuyQa2qMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13800,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13800
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014XbAhNfozavp81JisRfcBN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "03c34343-efcf-4935-b238-43d1159f7237",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQJcmcMBXdGVUWuyQa2qMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13800,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13800
      },
      "output_tokens": 9,
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

_source line 6 · 2026-05-18T12:24:32.369Z_

<details><summary>↩ Tool result · `toolu_014XbAhNfozavp81JisRfcBN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "f12487e8-1abb-4b9c-bc60-b142831b31a1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant files on the remote server to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "b169f362-2d9a-4c68-b7a3-88e12ae021aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016P4unPpEQEo6eoaAbNMmF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 25641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

### Assistant

_source line 8_

Reading the three files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "f9617732-d060-47c8-af3b-bd4d85805abc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016P4unPpEQEo6eoaAbNMmF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 25641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013ZwovXiKWSMTN1cizPeaP3`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat -n /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "5f7f03c2-a16a-49b8-bbe2-3e5c4a8ff149",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016P4unPpEQEo6eoaAbNMmF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 25641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011Ffm7kdpiqSGN8AR6BVX6E`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat -n /root/autodl-tmp/distrib_canary_collapse/docs/paper/discussion.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "ab2d6bc2-fbf4-4202-b000-0e409fd2da46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016P4unPpEQEo6eoaAbNMmF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 25641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VjEeHwpQPvHEEEp1e6egJy`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat -n /root/autodl-tmp/distrib_canary_collapse/docs/paper/conclusion.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "a05d2ba6-6fbf-487d-92ea-46fab5e749b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016P4unPpEQEo6eoaAbNMmF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 25641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
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

_source line 12 · 2026-05-18T12:24:40.192Z_

<details><summary>↩ Tool result · `toolu_013ZwovXiKWSMTN1cizPeaP3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Experiments}\\n     2\\t\\\\label{sec:experiments}\\n     3\\t\\n     4\\t\\\\subsection{Experimental Setup}\\n     5\\t\\\\label{sec:setup}\\n     6\\t\\n     7\\tWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\n     8\\tPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\n     9\\tCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\S\\\\ref{sec:method_sensitivity}, \\\\S\\\\ref{sec:regime}, and \\\\S\\\\ref{sec:discussion}.\\n    10\\tTraining data is drawn from WikiText-103 \\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\n    11\\t\\n    12\\tOur protocol follows the replace paradigm of \\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\alpha{<}1.0$.\\n    13\\tEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\alpha$ fraction synthetic data and $(1{-}\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\n    14\\tWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$.\\n    15\\tThe $\\\\alpha{=}1.0$ condition uses four random seeds $\\\\{42, 43, 44, 45\\\\}$; $\\\\alpha{=}0.00$, $\\\\alpha{=}0.25$, and $\\\\alpha{=}0.75$ each use three seeds $\\\\{42, 43, 44\\\\}$; $\\\\alpha{=}0.50$ uses three seeds $\\\\{42, 43, 44\\\\}$.\\n    16\\t\\n    17\\tWe track two \\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\cite{scheffer2009early}) and three \\\\emph{downstream metrics}.\\n    18\\tCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\n    19\\tDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\n    20\\tToken entropy is the mean next-token prediction entropy $H(p_\\\\theta | \\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\n    21\\tWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\S\\\\ref{sec:case_study}).\\n    22\\tResults for distinct-3 are reported in Appendix~\\\\ref{app:distinct3}.\\n    23\\tCode and data will be released upon publication.\\n    24\\t\\n    25\\tEach canary-downstream pair is independently tested for directional predictive improvement.\\n    26\\tPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\n    27\\tIndividual method significance is assessed at $\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\% false positive rate under the null (Table~\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\n    28\\tCross-correlation analysis uses a maximum lag of 5 generations.\\n    29\\tTable~\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\n    30\\t\\n    31\\t\\\\begin{\\n\\n... [截断: 输出过长，省略 33983 字符] ...\\n\\nle~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\n   363\\tAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\n   364\\tToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n   365\\t\\n   366\\tMethod-level variation across architectures is informative.\\n   367\\tThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\n   368\\tToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\n   369\\tDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n   370\\t\\n   371\\t\\\\paragraph{Scale generalization.}\\n   372\\tScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\n   373\\tOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\n   374\\tThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\n   375\\tThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\n   376\\tToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\n   377\\tThe consensus framework absorbs this single-method failure by design.\\n   378\\t\\n   379\\t\\\\paragraph{Domain generalization.}\\n   380\\tReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\n   381\\tWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\n   382\\tInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n   383\\t\\n   384\\tTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\n   385\\tPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\n   386\\tECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\n   387\\tTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.84}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "248d5369-cec6-4db2-a572-fdb3bd012d28",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"     1\\\\t\\\\\\\\section{Experiments}\\\\n     2\\\\t\\\\\\\\label{sec:experiments}\\\\n     3\\\\t\\\\n     4\\\\t\\\\\\\\subsection{Experimental Setup}\\\\n     5\\\\t\\\\\\\\label{sec:setup}\\\\n     6\\\\t\\\\n     7\\\\tWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\\\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\\\n     8\\\\tPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\\\n     9\\\\tCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}, \\\\\\\\S\\\\\\\\ref{sec:regime}, and \\\\\\\\S\\\\\\\\ref{sec:discussion}.\\\\n    10\\\\tTraining data is drawn from WikiText-103 \\\\\\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\\\n    11\\\\t\\\\n    12\\\\tOur protocol follows the replace paradigm of \\\\\\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\\\\\alpha{<}1.0$.\\\\n    13\\\\tEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\\\\\alpha$ fraction synthetic data and $(1{-}\\\\\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\\\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\\\n    14\\\\tWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\\\\\alpha \\\\\\\\in \\\\\\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\\\\\}$.\\\\n    15\\\\tThe $\\\\\\\\alpha{=}1.0$ condition uses four random seeds $\\\\\\\\{42, 43, 44, 45\\\\\\\\}$; $\\\\\\\\alpha{=}0.00$, $\\\\\\\\alpha{=}0.25$, and $\\\\\\\\alpha{=}0.75$ each use three seeds $\\\\\\\\{42, 43, 44\\\\\\\\}$; $\\\\\\\\alpha{=}0.50$ uses three seeds $\\\\\\\\{42, 43, 44\\\\\\\\}$.\\\\n    16\\\\t\\\\n    17\\\\tWe track two \\\\\\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\\\\\cite{scheffer2009early}) and three \\\\\\\\emph{downstream metrics}.\\\\n    18\\\\tCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\\\n    19\\\\tDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\\\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\\\n    20\\\\tToken entropy is the mean next-token prediction entropy $H(p_\\\\\\\\theta | \\\\\\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\\\n    21\\\\tWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\\\\\S\\\\\\\\ref{sec:case_study}).\\\\n    22\\\\tResults for distinct-3 are reported in Appendix~\\\\\\\\ref{app:distinct3}.\\\\n    23\\\\tCode and data will be released upon publication.\\\\n    24\\\\t\\\\n    25\\\\tEach canary-downstream pair is independently tested for directional predictive improvement.\\\\n    26\\\\tPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\\\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\\\n    27\\\\tIndividual method significance is assessed at $\\\\\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\\\\\% false positive rate under the null (Table~\\\\\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\\\n    28\\\\tCross-correlation analysis uses a maximum lag of 5 generations.\\\\n    29\\\\tTable~\\\\\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\\\n    30\\\\t\\\\n    31\\\\t\\\\\\\\begin{\\\\n\\\\n... [截断: 输出过长，省略 33983 字符] ...\\\\n\\\\nle~\\\\\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\\\n   363\\\\tAll models reach Tier~3 consensus ($K{\\\\\\\\geq}4/5$) with 6/8 canary$\\\\\\\\to$diversity pairs confirmed.\\\\n   364\\\\tToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\\\n   365\\\\t\\\\n   366\\\\tMethod-level variation across architectures is informative.\\\\n   367\\\\tThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\\\n   368\\\\tToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\n   369\\\\tDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\\\\\geq}4/5$.\\\\n   370\\\\t\\\\n   371\\\\t\\\\\\\\paragraph{Scale generalization.}\\\\n   372\\\\tScaling from 410M to 1.4B parameters (3.4$\\\\\\\\times$) preserves majority consensus ($K{\\\\\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\\\n   373\\\\tOf the three non-consensus pairs, two target perplexity (token\\\\\\\\_entropy$\\\\\\\\to$perplexity, $K{=}1$; ECE$\\\\\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).\\\\n   374\\\\tThe sole scale-specific miss is token\\\\\\\\_entropy$\\\\\\\\to$distinct\\\\\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\\\n   375\\\\tThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\\\n   376\\\\tToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\n   377\\\\tThe consensus framework absorbs this single-method failure by design.\\\\n   378\\\\t\\\\n   379\\\\t\\\\\\\\paragraph{Domain generalization.}\\\\n   380\\\\tReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\\\n   381\\\\tWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\\\n   382\\\\tInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\\\n   383\\\\t\\\\n   384\\\\tTable~\\\\\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\\\n   385\\\\tPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\\\n   386\\\\tECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\\\n   387\\\\tTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\\\\\alpha{=}1.0$.\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.84}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Experiments}\\n     2\\t\\\\label{sec:experiments}\\n     3\\t\\n     4\\t\\\\subsection{Experimental Setup}\\n     5\\t\\\\label{sec:setup}\\n     6\\t\\n     7\\tWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\n     8\\tPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\n     9\\tCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\S\\\\ref{sec:method_sensitivity}, \\\\S\\\\ref{sec:regime}, and \\\\S\\\\ref{sec:discussion}.\\n    10\\tTraining data is drawn from WikiText-103 \\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\n    11\\t\\n    12\\tOur protocol follows the replace paradigm of \\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\alpha{<}1.0$.\\n    13\\tEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\alpha$ fraction synthetic data and $(1{-}\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\n    14\\tWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$.\\n    15\\tThe $\\\\alpha{=}1.0$ condition uses four random seeds $\\\\{42, 43, 44, 45\\\\}$; $\\\\alpha{=}0.00$, $\\\\alpha{=}0.25$, and $\\\\alpha{=}0.75$ each use three seeds $\\\\{42, 43, 44\\\\}$; $\\\\alpha{=}0.50$ uses three seeds $\\\\{42, 43, 44\\\\}$.\\n    16\\t\\n    17\\tWe track two \\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\cite{scheffer2009early}) and three \\\\emph{downstream metrics}.\\n    18\\tCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\n    19\\tDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\n    20\\tToken entropy is the mean next-token prediction entropy $H(p_\\\\theta | \\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\n    21\\tWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\S\\\\ref{sec:case_study}).\\n    22\\tResults for distinct-3 are reported in Appendix~\\\\ref{app:distinct3}.\\n    23\\tCode and data will be released upon publication.\\n    24\\t\\n    25\\tEach canary-downstream pair is independently tested for directional predictive improvement.\\n    26\\tPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\n    27\\tIndividual method significance is assessed at $\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\% false positive rate under the null (Table~\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\n    28\\tCross-correlation analysis uses a maximum lag of 5 generations.\\n    29\\tTable~\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\n    30\\t\\n    31\\t\\\\begin{\\n\\n... [截断: 输出过长，省略 33983 字符] ...\\n\\nle~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\n   363\\tAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\n   364\\tToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n   365\\t\\n   366\\tMethod-level variation across architectures is informative.\\n   367\\tThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\n   368\\tToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\n   369\\tDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n   370\\t\\n   371\\t\\\\paragraph{Scale generalization.}\\n   372\\tScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\n   373\\tOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\n   374\\tThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\n   375\\tThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\n   376\\tToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\n   377\\tThe consensus framework absorbs this single-method failure by design.\\n   378\\t\\n   379\\t\\\\paragraph{Domain generalization.}\\n   380\\tReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\n   381\\tWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\n   382\\tInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n   383\\t\\n   384\\tTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\n   385\\tPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\n   386\\tECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\n   387\\tTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.84}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T12:24:42.910Z_

<details><summary>↩ Tool result · `toolu_011Ffm7kdpiqSGN8AR6BVX6E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Discussion}\\\\label{sec:discussion}\\n     2\\t\\n     3\\t\\\\paragraph{Granger precedence is not causation.}\\n     4\\tGranger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\\\\cite{granger1969investigating,shojaie2022granger}.\\n     5\\tBivariate Granger tests cannot exclude confounders: an unobserved process (such as a latent distributional shift in the training data) could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.\\n     6\\tOur multi-method consensus framework inherits this limitation in full.\\n     7\\tThroughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.\\n     8\\tThis distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \\\\emph{causes} diversity collapse.\\n     9\\t\\n    10\\t\\\\paragraph{Calibration scope and generalization.}\\n    11\\tAll FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\\\\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\\\\alpha \\\\in \\\\{0.0, 0.25, 0.50, 0.75, 1.0\\\\}$).\\n    12\\tGeneralization to other model architectures, datasets, or training protocols requires independent validation.\\n    13\\tThe consensus framework's structure (multi-method agreement combined with multi-seed replication) is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\\\\geq}4/5$ methods, $S{\\\\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.\\n    14\\tFor instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.\\n    15\\tPreliminary cross-architecture validation on GPT-2-medium (single seed, $\\\\alpha{=}1.0$) suggests the entropy-leads-diversity pattern transfers at Tier~3 consensus: all 6 canary$\\\\to$diversity pairs reach $K{\\\\geq}4/5$ method agreement (permutation Granger $p_{\\\\text{perm}}{<}0.005$), with 0/6 reverse-direction pairs significant.\\n    16\\tFull-panel inter-method agreement remains low (Fleiss' $\\\\kappa{=}0.091$) but rises to $\\\\kappa{=}0.667$ among the three informative methods (\\\\S\\\\ref{sec:method_sensitivity}), confirming that the consensus framework's structure transfers across architectures even if operating thresholds require architecture-specific calibration.\\n    17\\tIn preliminary $\\\\alpha{=}0.25$ experiments, GPT-2-medium yields 1/8 pairs at Tier~3 consensus ($K{\\\\geq}4/5$) and 7/8 at Tier~2 ($K{\\\\geq}3/5$), placing it in the same null/low-detectability regime as Pythia (0/8 Tier~3) and confirming that the detectability boundary is consistent across two transformer decoder-only model families of similar scale.\\n    18\\tThe full GPT-2-medium drift profile at $\\\\alpha{=}0.25$ is: entropy $-32.8\\\\%$, ECE $+422\\\\%$, perplexity $-44.5\\\\%$, distinct-1 $-23.5\\\\%$, distinct-2 $-31.6\\\\%$, distinct-3 $-30.2\\\\%$, MAUVE $0.0315 \\\\to 0.0282$ ($-10.5\\\\%$).\\n    19\\tCompared to Pythia ($-4.7{\\\\pm}0.5\\\\%$ entropy, $-40.3{\\\\pm}0.3\\\\%$ distinct-1), GPT-2-medium shows substantially stronger canary drift but milder diversity decline, likely due to its $8\\\\times$ larger batch size exposing more data per step.\\n    20\\tThe stronger canary signal approaches detectability (permutation Granger $F{=}64.09$, $p{=}0.081$ for entropy$\\\\to$distinct-1, compared to $p{>}0.5$ in Pythia), suggesting that the regime boundary may shift with increased effective sample size, but single-seed $T{=}10$ power remains insufficient for Confirmatory claims.\\n    21\\tToda--Yamamoto Granger finds 1/8 pairs significant, consistent with its known instability at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\n    22\\t\\n    23\\t\\\\paragraph{Why $K{=}4\\n\\n... [截断: 输出过长，省略 10225 字符] ...\\n\\n the same underlying distributional contraction.\\n    80\\tThus, the perplexity channel being ``spurious'' is not trivially expected from the mathematical relationship, but rather a substantive finding about collapse dynamics: the generation-evaluation divergence breaks the entropy--perplexity coupling in a temporally informative way.\\n    81\\t\\n    82\\t\\n    83\\t\\\\paragraph{Canary quality hierarchy: token entropy vs.\\\\ ECE.}\\n    84\\tToken entropy is the preferred canary indicator: it maintains perfect unidirectional precedence (reverse 0/4) across all experimental conditions, including architecture variants, domain transfer, and scale changes.\\n    85\\tECE is effective but secondary: forward signal is strong (6/8 to 8/8 across conditions), yet reverse leakage is condition-dependent in magnitude. In the Baseline and OPT-1.3B conditions, ECE reverse effects are borderline ($p\\\\approx 0.03$) and do not survive BH FDR correction, while in C4, three of four ECE pairs show stronger reverse coupling ($p<0.005$, BH-significant at $\\\\alpha{=}0.05$). This gradient reinforces the canary quality hierarchy: token entropy provides unconditionally unidirectional signal, whereas ECE coupling strength varies with the training domain.\\n    86\\tThe underlying mechanism is calibration-diversity feedback: ECE reflects both model quality and output diversity and is therefore susceptible to reverse influence from diversity collapse, whereas token entropy captures model quality degradation alone.\\n    87\\tFor monitoring applications, token entropy should serve as the primary canary, with ECE as supplementary confirmation.\\n    88\\t\\n    89\\t\\\\paragraph{NLP-specific constraints on lead-lag analysis.}\\n    90\\tOur application of Granger-type methods to iterative training faces constraints absent in their original econometric settings.\\n    91\\tFirst, observation length: typical econometric applications use $T{=}100$--$1000$ time points, whereas iterative training studies are limited to $T{=}5$--$20$ generations due to computational cost.\\n    92\\tThis severely constrains degrees of freedom for VAR-based methods and explains the Toda--Yamamoto procedure's poor power in our setting.\\n    93\\tSecond, non-stationarity is by design: each generation's training data differs from the previous generation's, making the underlying process non-stationary by construction rather than as an incidental property.\\n    94\\tStandard stationarity tests (ADF, KPSS) may yield misleading results when applied to processes with deterministic degradation trajectories rather than stochastic unit roots.\\n    95\\tThird, the sample-size bottleneck limits the power of individual statistical tests: with only 8--32 pairs per regime, traditional per-hypothesis corrections operate on small multiplicity, motivating our consensus-based approach to multiplicity control.\\n    96\\tThese constraints motivate our multi-method consensus approach as a complement to, rather than replacement for, traditional significance testing.\\n    97\\t\\n    98\\t\\\\paragraph{Future work.}\\n    99\\tSeveral directions extend this work.\\n   100\\tMultivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.\\n   101\\tCross-architecture validation beyond our single-seed GPT-2-medium validation requires multi-seed replication; evaluation on larger-scale models would further test generalizability.\\n   102\\tOnline monitoring, where canary metrics are computed within training pipelines for real-time collapse detection, is a natural applied extension.\\n   103\\tAccumulate-mode experiments~\\\\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.\\n   104\\tFinally, connecting the empirically observed onset boundary at $\\\\alpha{\\\\approx}0.25$--$0.50$ to theoretical phase transition analysis~\\\\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "00a0941c-ba80-4647-aace-761b8da497d4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"     1\\\\t\\\\\\\\section{Discussion}\\\\\\\\label{sec:discussion}\\\\n     2\\\\t\\\\n     3\\\\t\\\\\\\\paragraph{Granger precedence is not causation.}\\\\n     4\\\\tGranger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\\\\\\\\cite{granger1969investigating,shojaie2022granger}.\\\\n     5\\\\tBivariate Granger tests cannot exclude confounders: an unobserved process (such as a latent distributional shift in the training data) could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.\\\\n     6\\\\tOur multi-method consensus framework inherits this limitation in full.\\\\n     7\\\\tThroughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.\\\\n     8\\\\tThis distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \\\\\\\\emph{causes} diversity collapse.\\\\n     9\\\\t\\\\n    10\\\\t\\\\\\\\paragraph{Calibration scope and generalization.}\\\\n    11\\\\tAll FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\\\\\\\\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\\\\\\\\alpha \\\\\\\\in \\\\\\\\{0.0, 0.25, 0.50, 0.75, 1.0\\\\\\\\}$).\\\\n    12\\\\tGeneralization to other model architectures, datasets, or training protocols requires independent validation.\\\\n    13\\\\tThe consensus framework's structure (multi-method agreement combined with multi-seed replication) is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\\\\\\\\geq}4/5$ methods, $S{\\\\\\\\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.\\\\n    14\\\\tFor instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.\\\\n    15\\\\tPreliminary cross-architecture validation on GPT-2-medium (single seed, $\\\\\\\\alpha{=}1.0$) suggests the entropy-leads-diversity pattern transfers at Tier~3 consensus: all 6 canary$\\\\\\\\to$diversity pairs reach $K{\\\\\\\\geq}4/5$ method agreement (permutation Granger $p_{\\\\\\\\text{perm}}{<}0.005$), with 0/6 reverse-direction pairs significant.\\\\n    16\\\\tFull-panel inter-method agreement remains low (Fleiss' $\\\\\\\\kappa{=}0.091$) but rises to $\\\\\\\\kappa{=}0.667$ among the three informative methods (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}), confirming that the consensus framework's structure transfers across architectures even if operating thresholds require architecture-specific calibration.\\\\n    17\\\\tIn preliminary $\\\\\\\\alpha{=}0.25$ experiments, GPT-2-medium yields 1/8 pairs at Tier~3 consensus ($K{\\\\\\\\geq}4/5$) and 7/8 at Tier~2 ($K{\\\\\\\\geq}3/5$), placing it in the same null/low-detectability regime as Pythia (0/8 Tier~3) and confirming that the detectability boundary is consistent across two transformer decoder-only model families of similar scale.\\\\n    18\\\\tThe full GPT-2-medium drift profile at $\\\\\\\\alpha{=}0.25$ is: entropy $-32.8\\\\\\\\%$, ECE $+422\\\\\\\\%$, perplexity $-44.5\\\\\\\\%$, distinct-1 $-23.5\\\\\\\\%$, distinct-2 $-31.6\\\\\\\\%$, distinct-3 $-30.2\\\\\\\\%$, MAUVE $0.0315 \\\\\\\\to 0.0282$ ($-10.5\\\\\\\\%$).\\\\n    19\\\\tCompared to Pythia ($-4.7{\\\\\\\\pm}0.5\\\\\\\\%$ entropy, $-40.3{\\\\\\\\pm}0.3\\\\\\\\%$ distinct-1), GPT-2-medium shows substantially stronger canary drift but milder diversity decline, likely due to its $8\\\\\\\\times$ larger batch size exposing more data per step.\\\\n    20\\\\tThe stronger canary signal approaches detectability (permutation Granger $F{=}64.09$, $p{=}0.081$ for entropy$\\\\\\\\to$distinct-1, compared to $p{>}0.5$ in Pythia), suggesting that the regime boundary may shift with increased effective sample size, but single-seed $T{=}10$ power remains insufficient for Confirmatory claims.\\\\n    21\\\\tToda--Yamamoto Granger finds 1/8 pairs significant, consistent with its known instability at short series lengths (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\n    22\\\\t\\\\n    23\\\\t\\\\\\\\paragraph{Why $K{=}4\\\\n\\\\n... [截断: 输出过长，省略 10225 字符] ...\\\\n\\\\n the same underlying distributional contraction.\\\\n    80\\\\tThus, the perplexity channel being ``spurious'' is not trivially expected from the mathematical relationship, but rather a substantive finding about collapse dynamics: the generation-evaluation divergence breaks the entropy--perplexity coupling in a temporally informative way.\\\\n    81\\\\t\\\\n    82\\\\t\\\\n    83\\\\t\\\\\\\\paragraph{Canary quality hierarchy: token entropy vs.\\\\\\\\ ECE.}\\\\n    84\\\\tToken entropy is the preferred canary indicator: it maintains perfect unidirectional precedence (reverse 0/4) across all experimental conditions, including architecture variants, domain transfer, and scale changes.\\\\n    85\\\\tECE is effective but secondary: forward signal is strong (6/8 to 8/8 across conditions), yet reverse leakage is condition-dependent in magnitude. In the Baseline and OPT-1.3B conditions, ECE reverse effects are borderline ($p\\\\\\\\approx 0.03$) and do not survive BH FDR correction, while in C4, three of four ECE pairs show stronger reverse coupling ($p<0.005$, BH-significant at $\\\\\\\\alpha{=}0.05$). This gradient reinforces the canary quality hierarchy: token entropy provides unconditionally unidirectional signal, whereas ECE coupling strength varies with the training domain.\\\\n    86\\\\tThe underlying mechanism is calibration-diversity feedback: ECE reflects both model quality and output diversity and is therefore susceptible to reverse influence from diversity collapse, whereas token entropy captures model quality degradation alone.\\\\n    87\\\\tFor monitoring applications, token entropy should serve as the primary canary, with ECE as supplementary confirmation.\\\\n    88\\\\t\\\\n    89\\\\t\\\\\\\\paragraph{NLP-specific constraints on lead-lag analysis.}\\\\n    90\\\\tOur application of Granger-type methods to iterative training faces constraints absent in their original econometric settings.\\\\n    91\\\\tFirst, observation length: typical econometric applications use $T{=}100$--$1000$ time points, whereas iterative training studies are limited to $T{=}5$--$20$ generations due to computational cost.\\\\n    92\\\\tThis severely constrains degrees of freedom for VAR-based methods and explains the Toda--Yamamoto procedure's poor power in our setting.\\\\n    93\\\\tSecond, non-stationarity is by design: each generation's training data differs from the previous generation's, making the underlying process non-stationary by construction rather than as an incidental property.\\\\n    94\\\\tStandard stationarity tests (ADF, KPSS) may yield misleading results when applied to processes with deterministic degradation trajectories rather than stochastic unit roots.\\\\n    95\\\\tThird, the sample-size bottleneck limits the power of individual statistical tests: with only 8--32 pairs per regime, traditional per-hypothesis corrections operate on small multiplicity, motivating our consensus-based approach to multiplicity control.\\\\n    96\\\\tThese constraints motivate our multi-method consensus approach as a complement to, rather than replacement for, traditional significance testing.\\\\n    97\\\\t\\\\n    98\\\\t\\\\\\\\paragraph{Future work.}\\\\n    99\\\\tSeveral directions extend this work.\\\\n   100\\\\tMultivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.\\\\n   101\\\\tCross-architecture validation beyond our single-seed GPT-2-medium validation requires multi-seed replication; evaluation on larger-scale models would further test generalizability.\\\\n   102\\\\tOnline monitoring, where canary metrics are computed within training pipelines for real-time collapse detection, is a natural applied extension.\\\\n   103\\\\tAccumulate-mode experiments~\\\\\\\\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.\\\\n   104\\\\tFinally, connecting the empirically observed onset boundary at $\\\\\\\\alpha{\\\\\\\\approx}0.25$--$0.50$ to theoretical phase transition analysis~\\\\\\\\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Discussion}\\\\label{sec:discussion}\\n     2\\t\\n     3\\t\\\\paragraph{Granger precedence is not causation.}\\n     4\\tGranger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\\\\cite{granger1969investigating,shojaie2022granger}.\\n     5\\tBivariate Granger tests cannot exclude confounders: an unobserved process (such as a latent distributional shift in the training data) could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.\\n     6\\tOur multi-method consensus framework inherits this limitation in full.\\n     7\\tThroughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.\\n     8\\tThis distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \\\\emph{causes} diversity collapse.\\n     9\\t\\n    10\\t\\\\paragraph{Calibration scope and generalization.}\\n    11\\tAll FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\\\\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\\\\alpha \\\\in \\\\{0.0, 0.25, 0.50, 0.75, 1.0\\\\}$).\\n    12\\tGeneralization to other model architectures, datasets, or training protocols requires independent validation.\\n    13\\tThe consensus framework's structure (multi-method agreement combined with multi-seed replication) is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\\\\geq}4/5$ methods, $S{\\\\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.\\n    14\\tFor instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.\\n    15\\tPreliminary cross-architecture validation on GPT-2-medium (single seed, $\\\\alpha{=}1.0$) suggests the entropy-leads-diversity pattern transfers at Tier~3 consensus: all 6 canary$\\\\to$diversity pairs reach $K{\\\\geq}4/5$ method agreement (permutation Granger $p_{\\\\text{perm}}{<}0.005$), with 0/6 reverse-direction pairs significant.\\n    16\\tFull-panel inter-method agreement remains low (Fleiss' $\\\\kappa{=}0.091$) but rises to $\\\\kappa{=}0.667$ among the three informative methods (\\\\S\\\\ref{sec:method_sensitivity}), confirming that the consensus framework's structure transfers across architectures even if operating thresholds require architecture-specific calibration.\\n    17\\tIn preliminary $\\\\alpha{=}0.25$ experiments, GPT-2-medium yields 1/8 pairs at Tier~3 consensus ($K{\\\\geq}4/5$) and 7/8 at Tier~2 ($K{\\\\geq}3/5$), placing it in the same null/low-detectability regime as Pythia (0/8 Tier~3) and confirming that the detectability boundary is consistent across two transformer decoder-only model families of similar scale.\\n    18\\tThe full GPT-2-medium drift profile at $\\\\alpha{=}0.25$ is: entropy $-32.8\\\\%$, ECE $+422\\\\%$, perplexity $-44.5\\\\%$, distinct-1 $-23.5\\\\%$, distinct-2 $-31.6\\\\%$, distinct-3 $-30.2\\\\%$, MAUVE $0.0315 \\\\to 0.0282$ ($-10.5\\\\%$).\\n    19\\tCompared to Pythia ($-4.7{\\\\pm}0.5\\\\%$ entropy, $-40.3{\\\\pm}0.3\\\\%$ distinct-1), GPT-2-medium shows substantially stronger canary drift but milder diversity decline, likely due to its $8\\\\times$ larger batch size exposing more data per step.\\n    20\\tThe stronger canary signal approaches detectability (permutation Granger $F{=}64.09$, $p{=}0.081$ for entropy$\\\\to$distinct-1, compared to $p{>}0.5$ in Pythia), suggesting that the regime boundary may shift with increased effective sample size, but single-seed $T{=}10$ power remains insufficient for Confirmatory claims.\\n    21\\tToda--Yamamoto Granger finds 1/8 pairs significant, consistent with its known instability at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\n    22\\t\\n    23\\t\\\\paragraph{Why $K{=}4\\n\\n... [截断: 输出过长，省略 10225 字符] ...\\n\\n the same underlying distributional contraction.\\n    80\\tThus, the perplexity channel being ``spurious'' is not trivially expected from the mathematical relationship, but rather a substantive finding about collapse dynamics: the generation-evaluation divergence breaks the entropy--perplexity coupling in a temporally informative way.\\n    81\\t\\n    82\\t\\n    83\\t\\\\paragraph{Canary quality hierarchy: token entropy vs.\\\\ ECE.}\\n    84\\tToken entropy is the preferred canary indicator: it maintains perfect unidirectional precedence (reverse 0/4) across all experimental conditions, including architecture variants, domain transfer, and scale changes.\\n    85\\tECE is effective but secondary: forward signal is strong (6/8 to 8/8 across conditions), yet reverse leakage is condition-dependent in magnitude. In the Baseline and OPT-1.3B conditions, ECE reverse effects are borderline ($p\\\\approx 0.03$) and do not survive BH FDR correction, while in C4, three of four ECE pairs show stronger reverse coupling ($p<0.005$, BH-significant at $\\\\alpha{=}0.05$). This gradient reinforces the canary quality hierarchy: token entropy provides unconditionally unidirectional signal, whereas ECE coupling strength varies with the training domain.\\n    86\\tThe underlying mechanism is calibration-diversity feedback: ECE reflects both model quality and output diversity and is therefore susceptible to reverse influence from diversity collapse, whereas token entropy captures model quality degradation alone.\\n    87\\tFor monitoring applications, token entropy should serve as the primary canary, with ECE as supplementary confirmation.\\n    88\\t\\n    89\\t\\\\paragraph{NLP-specific constraints on lead-lag analysis.}\\n    90\\tOur application of Granger-type methods to iterative training faces constraints absent in their original econometric settings.\\n    91\\tFirst, observation length: typical econometric applications use $T{=}100$--$1000$ time points, whereas iterative training studies are limited to $T{=}5$--$20$ generations due to computational cost.\\n    92\\tThis severely constrains degrees of freedom for VAR-based methods and explains the Toda--Yamamoto procedure's poor power in our setting.\\n    93\\tSecond, non-stationarity is by design: each generation's training data differs from the previous generation's, making the underlying process non-stationary by construction rather than as an incidental property.\\n    94\\tStandard stationarity tests (ADF, KPSS) may yield misleading results when applied to processes with deterministic degradation trajectories rather than stochastic unit roots.\\n    95\\tThird, the sample-size bottleneck limits the power of individual statistical tests: with only 8--32 pairs per regime, traditional per-hypothesis corrections operate on small multiplicity, motivating our consensus-based approach to multiplicity control.\\n    96\\tThese constraints motivate our multi-method consensus approach as a complement to, rather than replacement for, traditional significance testing.\\n    97\\t\\n    98\\t\\\\paragraph{Future work.}\\n    99\\tSeveral directions extend this work.\\n   100\\tMultivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.\\n   101\\tCross-architecture validation beyond our single-seed GPT-2-medium validation requires multi-seed replication; evaluation on larger-scale models would further test generalizability.\\n   102\\tOnline monitoring, where canary metrics are computed within training pipelines for real-time collapse detection, is a natural applied extension.\\n   103\\tAccumulate-mode experiments~\\\\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.\\n   104\\tFinally, connecting the empirically observed onset boundary at $\\\\alpha{\\\\approx}0.25$--$0.50$ to theoretical phase transition analysis~\\\\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.71}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T12:24:45.268Z_

<details><summary>↩ Tool result · `toolu_01VjEeHwpQPvHEEEp1e6egJy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Conclusion}\\n     2\\t\\\\label{sec:conclusion}\\n     3\\t\\n     4\\tLead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.\\n     5\\tMethod choice alone inflates spurious-signal rates to at least 62.5\\\\%, first-differencing exposes canary$\\\\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.\\n     6\\tThese pitfalls establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.\\n     7\\t\\n     8\\tOur multi-method consensus framework addresses this fragility by requiring convergent evidence across multiple independent methods and random seeds.\\n     9\\tCalibrated on effect-size reference pairs with a non-circular 4-method panel, the framework achieves FPR${=}$0\\\\% (0/24, three null-control seeds) and FNR${=}$0\\\\% with permutation Granger power${=}1.0$, and provides four tiers of practical guidance from exploratory screening to publication-grade claims.\\n    10\\t\\n    11\\tThe framework generalizes across three decoder-only transformer families (Pythia-410M, GPT-2 Medium, OPT-1.3B), all reaching Tier~3 consensus ($K{\\\\geq}4/5$) on WikiText-103, with dominant forward directionality (token entropy: reverse 0 across all conditions; ECE: marginal reverse in 3/4 verified conditions).\\n    12\\tDomain transfer from WikiText to C4 (Pythia-1B) yields even stronger consensus (7/8 at $K{\\\\geq}4/5$), confirming the canary quality hierarchy: token entropy maintains strict unidirectionality (reverse 0/4) across all conditions, while ECE shows marginal reverse leakage in some conditions ($p\\\\approx 0.03$), an inherent property of calibration metrics rather than a domain-specific phenomenon.\\n    13\\tThis diagnostic distinction, visible only through the multi-method design, would be missed by any single-test analysis.\\n    14\\t\\n    15\\tDose-response experiments across five contamination levels ($\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$) with three seeds each show a monotonic progression from null (0/24 significant) to confirmatory (${\\\\sim}$8/8 consensus); the detectability boundary lies at $\\\\alpha{=}0.75$, where directional asymmetry is confirmed (19/24 forward, 0/24 reverse) but method consensus remains transitional (Tier~2--3).\\n    16\\tAt $\\\\alpha{=}1.0$, token entropy exhibits robust Granger-precedence over diversity collapse (${\\\\geq}4/5$ method consensus, Tier~3 across 4~seeds) with complete unidirectional precedence (token entropy: 0/12 reverse pairs across 4 seeds; ECE: marginal reverse $p\\\\approx 0.03$, consistent with a canary quality hierarchy) and a consistent one-generation lead.\\n    17\\tThis finding is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.\\n    18\\t\\n    19\\tThe methodological pitfalls we expose arise from generic properties of short, non-stationary time series, and the consensus framework's successful generalization across architectures and data domains supports its transfer to other iterative training settings where multiple detection methods can be applied in parallel.\\n    20\\tLimitations are detailed in \\\\S\\\\ref{sec:limitations}; future directions are discussed in \\\\S\\\\ref{sec:discussion}.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "0e0754ea-070d-4c52-b689-748583978dc7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"     1\\\\t\\\\\\\\section{Conclusion}\\\\n     2\\\\t\\\\\\\\label{sec:conclusion}\\\\n     3\\\\t\\\\n     4\\\\tLead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.\\\\n     5\\\\tMethod choice alone inflates spurious-signal rates to at least 62.5\\\\\\\\%, first-differencing exposes canary$\\\\\\\\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.\\\\n     6\\\\tThese pitfalls establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.\\\\n     7\\\\t\\\\n     8\\\\tOur multi-method consensus framework addresses this fragility by requiring convergent evidence across multiple independent methods and random seeds.\\\\n     9\\\\tCalibrated on effect-size reference pairs with a non-circular 4-method panel, the framework achieves FPR${=}$0\\\\\\\\% (0/24, three null-control seeds) and FNR${=}$0\\\\\\\\% with permutation Granger power${=}1.0$, and provides four tiers of practical guidance from exploratory screening to publication-grade claims.\\\\n    10\\\\t\\\\n    11\\\\tThe framework generalizes across three decoder-only transformer families (Pythia-410M, GPT-2 Medium, OPT-1.3B), all reaching Tier~3 consensus ($K{\\\\\\\\geq}4/5$) on WikiText-103, with dominant forward directionality (token entropy: reverse 0 across all conditions; ECE: marginal reverse in 3/4 verified conditions).\\\\n    12\\\\tDomain transfer from WikiText to C4 (Pythia-1B) yields even stronger consensus (7/8 at $K{\\\\\\\\geq}4/5$), confirming the canary quality hierarchy: token entropy maintains strict unidirectionality (reverse 0/4) across all conditions, while ECE shows marginal reverse leakage in some conditions ($p\\\\\\\\approx 0.03$), an inherent property of calibration metrics rather than a domain-specific phenomenon.\\\\n    13\\\\tThis diagnostic distinction, visible only through the multi-method design, would be missed by any single-test analysis.\\\\n    14\\\\t\\\\n    15\\\\tDose-response experiments across five contamination levels ($\\\\\\\\alpha \\\\\\\\in \\\\\\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\\\\\}$) with three seeds each show a monotonic progression from null (0/24 significant) to confirmatory (${\\\\\\\\sim}$8/8 consensus); the detectability boundary lies at $\\\\\\\\alpha{=}0.75$, where directional asymmetry is confirmed (19/24 forward, 0/24 reverse) but method consensus remains transitional (Tier~2--3).\\\\n    16\\\\tAt $\\\\\\\\alpha{=}1.0$, token entropy exhibits robust Granger-precedence over diversity collapse (${\\\\\\\\geq}4/5$ method consensus, Tier~3 across 4~seeds) with complete unidirectional precedence (token entropy: 0/12 reverse pairs across 4 seeds; ECE: marginal reverse $p\\\\\\\\approx 0.03$, consistent with a canary quality hierarchy) and a consistent one-generation lead.\\\\n    17\\\\tThis finding is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.\\\\n    18\\\\t\\\\n    19\\\\tThe methodological pitfalls we expose arise from generic properties of short, non-stationary time series, and the consensus framework's successful generalization across architectures and data domains supports its transfer to other iterative training settings where multiple detection methods can be applied in parallel.\\\\n    20\\\\tLimitations are detailed in \\\\\\\\S\\\\\\\\ref{sec:limitations}; future directions are discussed in \\\\\\\\S\\\\\\\\ref{sec:discussion}.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Conclusion}\\n     2\\t\\\\label{sec:conclusion}\\n     3\\t\\n     4\\tLead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.\\n     5\\tMethod choice alone inflates spurious-signal rates to at least 62.5\\\\%, first-differencing exposes canary$\\\\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.\\n     6\\tThese pitfalls establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.\\n     7\\t\\n     8\\tOur multi-method consensus framework addresses this fragility by requiring convergent evidence across multiple independent methods and random seeds.\\n     9\\tCalibrated on effect-size reference pairs with a non-circular 4-method panel, the framework achieves FPR${=}$0\\\\% (0/24, three null-control seeds) and FNR${=}$0\\\\% with permutation Granger power${=}1.0$, and provides four tiers of practical guidance from exploratory screening to publication-grade claims.\\n    10\\t\\n    11\\tThe framework generalizes across three decoder-only transformer families (Pythia-410M, GPT-2 Medium, OPT-1.3B), all reaching Tier~3 consensus ($K{\\\\geq}4/5$) on WikiText-103, with dominant forward directionality (token entropy: reverse 0 across all conditions; ECE: marginal reverse in 3/4 verified conditions).\\n    12\\tDomain transfer from WikiText to C4 (Pythia-1B) yields even stronger consensus (7/8 at $K{\\\\geq}4/5$), confirming the canary quality hierarchy: token entropy maintains strict unidirectionality (reverse 0/4) across all conditions, while ECE shows marginal reverse leakage in some conditions ($p\\\\approx 0.03$), an inherent property of calibration metrics rather than a domain-specific phenomenon.\\n    13\\tThis diagnostic distinction, visible only through the multi-method design, would be missed by any single-test analysis.\\n    14\\t\\n    15\\tDose-response experiments across five contamination levels ($\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$) with three seeds each show a monotonic progression from null (0/24 significant) to confirmatory (${\\\\sim}$8/8 consensus); the detectability boundary lies at $\\\\alpha{=}0.75$, where directional asymmetry is confirmed (19/24 forward, 0/24 reverse) but method consensus remains transitional (Tier~2--3).\\n    16\\tAt $\\\\alpha{=}1.0$, token entropy exhibits robust Granger-precedence over diversity collapse (${\\\\geq}4/5$ method consensus, Tier~3 across 4~seeds) with complete unidirectional precedence (token entropy: 0/12 reverse pairs across 4 seeds; ECE: marginal reverse $p\\\\approx 0.03$, consistent with a canary quality hierarchy) and a consistent one-generation lead.\\n    17\\tThis finding is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.\\n    18\\t\\n    19\\tThe methodological pitfalls we expose arise from generic properties of short, non-stationary time series, and the consensus framework's successful generalization across architectures and data domains supports its transfer to other iterative training settings where multiple detection methods can be applied in parallel.\\n    20\\tLimitations are detailed in \\\\S\\\\ref{sec:limitations}; future directions are discussed in \\\\S\\\\ref{sec:discussion}.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.35}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
The experiments.tex output was truncated. I need to find Table 7 specifically. Let me search for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "eeb55e21-ef4b-4140-b587-cd58bf100cec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HG6DYBUv5shTa8vuJHA6gq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6600,
      "cache_read_input_tokens": 26334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6600
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

_source line 16_

Output was truncated for experiments.tex. Let me find Table 7 specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "dff8b96e-d211-4b52-9ba2-43b7cb804e09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HG6DYBUv5shTa8vuJHA6gq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6600,
      "cache_read_input_tokens": 26334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6600
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

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018jcppKet7uTQobFe5fLvQb`</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"tab:generalization\\|begin{table\\|end{table\\|Naive\\|Diff\\|Thresh\\|PG.*fwd\\|PG.*rev\\|TY\\|K.*4\\|Baseline\\|GPT\\|OPT\\|Scale\\|Domain\\|C4\\|caption\\|footnote\\|nperm\\|n_perm\\|n.*perm\\|5000\\|1000\\|Preliminary\\|preliminary\\|dagger\\|TBD\\|tbd\" /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "81c56528-ff11-4312-8d0d-3575342f1037",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HG6DYBUv5shTa8vuJHA6gq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6600,
      "cache_read_input_tokens": 26334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6600
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

_source line 18 · 2026-05-18T12:26:20.138Z_

<details><summary>↩ Tool result · `toolu_018jcppKet7uTQobFe5fLvQb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "c7b9ac62-8c8c-45bc-813b-b4a9b0aae8aa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LR3mRxK5nHipWHGxUzFv3F`</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"tab:generalization\" /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "787f931e-d7ce-40ce-8549-2f94040765ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XiG4JddnWa8ca4Wq7h8eS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 32934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 403
      },
      "output_tokens": 69,
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

_source line 20 · 2026-05-18T12:26:24.936Z_

<details><summary>↩ Tool result · `toolu_01LR3mRxK5nHipWHGxUzFv3F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"343:\\\\label{tab:generalization}\\n362:Table~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\n384:Table~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.83}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "f7b8ea14-9b34-4d8d-b3bd-7fac922bc906",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"343:\\\\\\\\label{tab:generalization}\\\\n362:Table~\\\\\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\\\n384:Table~\\\\\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.83}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"343:\\\\label{tab:generalization}\\n362:Table~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\n384:Table~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.83}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013kvtaAzqXWLMMcvz75iaij`</summary>

```json
{
  "server": "westd-19828",
  "command": "sed -n '320,360p' /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "c2912bd2-bca3-4304-9368-5e6ab988199c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BgEW6EzgBEs6B66HkUfm5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 325,
      "cache_read_input_tokens": 33337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 325
      },
      "output_tokens": 67,
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

_source line 22 · 2026-05-18T12:26:29.045Z_

<details><summary>↩ Tool result · `toolu_013kvtaAzqXWLMMcvz75iaij`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "d1927302-0b16-4b27-8708-ffe1449c13ed",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CrSnzeckWAL3Hvhdszgs1F`</summary>

```json
{
  "server": "westd-19828",
  "command": "head -n 360 /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "6c19ca16-f1f8-44a0-915c-1949e9ca0225",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rGWuskvtkxQtbnE6vbPoN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 329,
      "cache_read_input_tokens": 33662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 329
      },
      "output_tokens": 65,
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

_source line 24 · 2026-05-18T12:26:33.092Z_

<details><summary>↩ Tool result · `toolu_01CrSnzeckWAL3Hvhdszgs1F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\\\label{sec:experiments}\\n\\n\\\\subsection{Experimental Setup}\\n\\\\label{sec:setup}\\n\\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\S\\\\ref{sec:method_sensitivity}, \\\\S\\\\ref{sec:regime}, and \\\\S\\\\ref{sec:discussion}.\\nTraining data is drawn from WikiText-103 \\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\n\\nOur protocol follows the replace paradigm of \\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\alpha{<}1.0$.\\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\alpha$ fraction synthetic data and $(1{-}\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$.\\nThe $\\\\alpha{=}1.0$ condition uses four random seeds $\\\\{42, 43, 44, 45\\\\}$; $\\\\alpha{=}0.00$, $\\\\alpha{=}0.25$, and $\\\\alpha{=}0.75$ each use three seeds $\\\\{42, 43, 44\\\\}$; $\\\\alpha{=}0.50$ uses three seeds $\\\\{42, 43, 44\\\\}$.\\n\\nWe track two \\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\cite{scheffer2009early}) and three \\\\emph{downstream metrics}.\\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\nToken entropy is the mean next-token prediction entropy $H(p_\\\\theta | \\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\S\\\\ref{sec:case_study}).\\nResults for distinct-3 are reported in Appendix~\\\\ref{app:distinct3}.\\nCode and data will be released upon publication.\\n\\nEach canary-downstream pair is independently tested for directional predictive improvement.\\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\nIndividual method significance is assessed at $\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\% false positive rate under the null (Table~\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\nCross-correlation analysis uses a maximum lag of 5 generations.\\nTable~\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Metric drift (\\\\%, generation~0$\\\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\\\alpha$ levels, with the strongest decline at moderate contami\\n\\n... [截断: 输出过长，省略 27405 字符] ...\\n\\ne in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\\\\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\\\\beta{=}0.3$).\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\\\\geq}4/5$ achieves FPR${=}$0\\\\% and FNR${=}$0\\\\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration. FPR: $\\\\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\\\\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds).}\\n\\\\label{tab:fpr_fnr}\\n\\\\begin{tabular}{lcc}\\n\\\\toprule\\nCriterion & FPR ($\\\\alpha{=}0.0$) & FNR ($\\\\alpha{=}1.0$) \\\\\\\\\\n\\\\midrule\\nNaive XCorr              & 100\\\\%              & 0\\\\%  \\\\\\\\\\nDifferenced XCorr        & 37.5\\\\%             & 0\\\\%  \\\\\\\\\\nThreshold Onset          & 20.8\\\\% (12.5--37.5) & 0\\\\%  \\\\\\\\\\nPermutation Granger      & 0\\\\%                & 0\\\\%  \\\\\\\\\\nToda--Yamamoto           & 4.2\\\\% (0--12.5)    & 33.3\\\\% \\\\\\\\\\n\\\\midrule\\nConsensus ($K{\\\\geq}4/5$)              & 0\\\\%    & 0\\\\%  \\\\\\\\\\nConsensus ($K{\\\\geq}4/5$, $S{\\\\geq}3/4$) & 0\\\\%    & 0\\\\%  \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}\\n\\\\label{sec:generalization}\\n\\nThe methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\nAll conditions use $\\\\alpha{=}1.0$ and a single seed.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\n\\\\label{tab:generalization}\\n\\\\begin{tabular}{llccccccc}\\n\\\\toprule\\nVariation & Model / Dataset & \\\\rotatebox{70}{Naive} & \\\\rotatebox{70}{Diff.\\\\ XCorr} & \\\\rotatebox{70}{Threshold} & \\\\rotatebox{70}{PermG (fwd)} & \\\\rotatebox{70}{PermG (rev)} & \\\\rotatebox{70}{TY} & \\\\rotatebox{70}{$K{\\\\geq}4/5$} \\\\\\\\\\n\\\\midrule\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\textit{pending} \\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\nScale ($3.4\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\dagger$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\vspace{2pt}\\n{\\\\footnotesize $^\\\\dagger$C4 domain (s42): token\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\_entropy$\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\rightarrow$diversity reverse significance ($p\\\\approx 0.03$); token\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\nCanary$\\\\to$perplexity pairs do not reach $K{\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\S\\\\ref{sec:method_sensitivity}).}\\n\\\\end{table}\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "f1cc2e1d-4327-4f81-a8dc-3e5e65300730",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Experiments}\\\\n\\\\\\\\label{sec:experiments}\\\\n\\\\n\\\\\\\\subsection{Experimental Setup}\\\\n\\\\\\\\label{sec:setup}\\\\n\\\\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\\\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\\\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\\\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}, \\\\\\\\S\\\\\\\\ref{sec:regime}, and \\\\\\\\S\\\\\\\\ref{sec:discussion}.\\\\nTraining data is drawn from WikiText-103 \\\\\\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\\\n\\\\nOur protocol follows the replace paradigm of \\\\\\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\\\\\alpha{<}1.0$.\\\\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\\\\\alpha$ fraction synthetic data and $(1{-}\\\\\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\\\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\\\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\\\\\alpha \\\\\\\\in \\\\\\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\\\\\}$.\\\\nThe $\\\\\\\\alpha{=}1.0$ condition uses four random seeds $\\\\\\\\{42, 43, 44, 45\\\\\\\\}$; $\\\\\\\\alpha{=}0.00$, $\\\\\\\\alpha{=}0.25$, and $\\\\\\\\alpha{=}0.75$ each use three seeds $\\\\\\\\{42, 43, 44\\\\\\\\}$; $\\\\\\\\alpha{=}0.50$ uses three seeds $\\\\\\\\{42, 43, 44\\\\\\\\}$.\\\\n\\\\nWe track two \\\\\\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\\\\\cite{scheffer2009early}) and three \\\\\\\\emph{downstream metrics}.\\\\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\\\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\\\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\\\nToken entropy is the mean next-token prediction entropy $H(p_\\\\\\\\theta | \\\\\\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\\\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\\\\\S\\\\\\\\ref{sec:case_study}).\\\\nResults for distinct-3 are reported in Appendix~\\\\\\\\ref{app:distinct3}.\\\\nCode and data will be released upon publication.\\\\n\\\\nEach canary-downstream pair is independently tested for directional predictive improvement.\\\\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\\\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\\\nIndividual method significance is assessed at $\\\\\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\\\\\% false positive rate under the null (Table~\\\\\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\\\nCross-correlation analysis uses a maximum lag of 5 generations.\\\\nTable~\\\\\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Metric drift (\\\\\\\\%, generation~0$\\\\\\\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\\\\\\\alpha$ levels, with the strongest decline at moderate contami\\\\n\\\\n... [截断: 输出过长，省略 27405 字符] ...\\\\n\\\\ne in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\\\\\\\\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\\\\\\\\beta{=}0.3$).\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\\\\\\\\geq}4/5$ achieves FPR${=}$0\\\\\\\\% and FNR${=}$0\\\\\\\\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration. FPR: $\\\\\\\\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\\\\\\\\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds).}\\\\n\\\\\\\\label{tab:fpr_fnr}\\\\n\\\\\\\\begin{tabular}{lcc}\\\\n\\\\\\\\toprule\\\\nCriterion & FPR ($\\\\\\\\alpha{=}0.0$) & FNR ($\\\\\\\\alpha{=}1.0$) \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nNaive XCorr              & 100\\\\\\\\%              & 0\\\\\\\\%  \\\\\\\\\\\\\\\\\\\\nDifferenced XCorr        & 37.5\\\\\\\\%             & 0\\\\\\\\%  \\\\\\\\\\\\\\\\\\\\nThreshold Onset          & 20.8\\\\\\\\% (12.5--37.5) & 0\\\\\\\\%  \\\\\\\\\\\\\\\\\\\\nPermutation Granger      & 0\\\\\\\\%                & 0\\\\\\\\%  \\\\\\\\\\\\\\\\\\\\nToda--Yamamoto           & 4.2\\\\\\\\% (0--12.5)    & 33.3\\\\\\\\% \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nConsensus ($K{\\\\\\\\geq}4/5$)              & 0\\\\\\\\%    & 0\\\\\\\\%  \\\\\\\\\\\\\\\\\\\\nConsensus ($K{\\\\\\\\geq}4/5$, $S{\\\\\\\\geq}3/4$) & 0\\\\\\\\%    & 0\\\\\\\\%  \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\n\\\\\\\\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}\\\\n\\\\\\\\label{sec:generalization}\\\\n\\\\nThe methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\\\\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\\\nAll conditions use $\\\\\\\\alpha{=}1.0$ and a single seed.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\\\n\\\\\\\\label{tab:generalization}\\\\n\\\\\\\\begin{tabular}{llccccccc}\\\\n\\\\\\\\toprule\\\\nVariation & Model / Dataset & \\\\\\\\rotatebox{70}{Naive} & \\\\\\\\rotatebox{70}{Diff.\\\\\\\\ XCorr} & \\\\\\\\rotatebox{70}{Threshold} & \\\\\\\\rotatebox{70}{PermG (fwd)} & \\\\\\\\rotatebox{70}{PermG (rev)} & \\\\\\\\rotatebox{70}{TY} & \\\\\\\\rotatebox{70}{$K{\\\\\\\\geq}4/5$} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\\\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\\\\\textit{pending} \\\\\\\\\\\\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\\\\\\\\\\\nScale ($3.4\\\\\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\\\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\\\\\dagger$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\vspace{2pt}\\\\n{\\\\\\\\footnotesize $^\\\\\\\\dagger$C4 domain (s42): token\\\\\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\\\\\_entropy$\\\\\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\\\\\rightarrow$diversity reverse significance ($p\\\\\\\\approx 0.03$); token\\\\\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\\\\\\\\\\\nCanary$\\\\\\\\to$perplexity pairs do not reach $K{\\\\\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.93}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\\\label{sec:experiments}\\n\\n\\\\subsection{Experimental Setup}\\n\\\\label{sec:setup}\\n\\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\S\\\\ref{sec:method_sensitivity}, \\\\S\\\\ref{sec:regime}, and \\\\S\\\\ref{sec:discussion}.\\nTraining data is drawn from WikiText-103 \\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\n\\nOur protocol follows the replace paradigm of \\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\alpha{<}1.0$.\\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\alpha$ fraction synthetic data and $(1{-}\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$.\\nThe $\\\\alpha{=}1.0$ condition uses four random seeds $\\\\{42, 43, 44, 45\\\\}$; $\\\\alpha{=}0.00$, $\\\\alpha{=}0.25$, and $\\\\alpha{=}0.75$ each use three seeds $\\\\{42, 43, 44\\\\}$; $\\\\alpha{=}0.50$ uses three seeds $\\\\{42, 43, 44\\\\}$.\\n\\nWe track two \\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\cite{scheffer2009early}) and three \\\\emph{downstream metrics}.\\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\nToken entropy is the mean next-token prediction entropy $H(p_\\\\theta | \\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\S\\\\ref{sec:case_study}).\\nResults for distinct-3 are reported in Appendix~\\\\ref{app:distinct3}.\\nCode and data will be released upon publication.\\n\\nEach canary-downstream pair is independently tested for directional predictive improvement.\\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\nIndividual method significance is assessed at $\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\% false positive rate under the null (Table~\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\nCross-correlation analysis uses a maximum lag of 5 generations.\\nTable~\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Metric drift (\\\\%, generation~0$\\\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\\\alpha$ levels, with the strongest decline at moderate contami\\n\\n... [截断: 输出过长，省略 27405 字符] ...\\n\\ne in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\\\\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\\\\beta{=}0.3$).\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\\\\geq}4/5$ achieves FPR${=}$0\\\\% and FNR${=}$0\\\\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration. FPR: $\\\\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\\\\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds).}\\n\\\\label{tab:fpr_fnr}\\n\\\\begin{tabular}{lcc}\\n\\\\toprule\\nCriterion & FPR ($\\\\alpha{=}0.0$) & FNR ($\\\\alpha{=}1.0$) \\\\\\\\\\n\\\\midrule\\nNaive XCorr              & 100\\\\%              & 0\\\\%  \\\\\\\\\\nDifferenced XCorr        & 37.5\\\\%             & 0\\\\%  \\\\\\\\\\nThreshold Onset          & 20.8\\\\% (12.5--37.5) & 0\\\\%  \\\\\\\\\\nPermutation Granger      & 0\\\\%                & 0\\\\%  \\\\\\\\\\nToda--Yamamoto           & 4.2\\\\% (0--12.5)    & 33.3\\\\% \\\\\\\\\\n\\\\midrule\\nConsensus ($K{\\\\geq}4/5$)              & 0\\\\%    & 0\\\\%  \\\\\\\\\\nConsensus ($K{\\\\geq}4/5$, $S{\\\\geq}3/4$) & 0\\\\%    & 0\\\\%  \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\n\\\\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}\\n\\\\label{sec:generalization}\\n\\nThe methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\nAll conditions use $\\\\alpha{=}1.0$ and a single seed.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\n\\\\label{tab:generalization}\\n\\\\begin{tabular}{llccccccc}\\n\\\\toprule\\nVariation & Model / Dataset & \\\\rotatebox{70}{Naive} & \\\\rotatebox{70}{Diff.\\\\ XCorr} & \\\\rotatebox{70}{Threshold} & \\\\rotatebox{70}{PermG (fwd)} & \\\\rotatebox{70}{PermG (rev)} & \\\\rotatebox{70}{TY} & \\\\rotatebox{70}{$K{\\\\geq}4/5$} \\\\\\\\\\n\\\\midrule\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\textit{pending} \\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\nScale ($3.4\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\dagger$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\vspace{2pt}\\n{\\\\footnotesize $^\\\\dagger$C4 domain (s42): token\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\_entropy$\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\rightarrow$diversity reverse significance ($p\\\\approx 0.03$); token\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\nCanary$\\\\to$perplexity pairs do not reach $K{\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\S\\\\ref{sec:method_sensitivity}).}\\n\\\\end{table}\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

````text
Now I have the full Table 7 (tab:generalization). Let me understand the current state:

Current Table 7:
```
Baseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\
Architecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \textit{pending} \\


```

Now I'm filling in the rest of the generalization table with results from different model architectures and scales. I see the OPT-1.3B variant, the larger Pythia-1.4B model showing some degradation in certain columns, and the domain shift experiment with Pythia-1B trained on C4 data.

Generating markdown table... I need to update several rows in the table with corrected values, add two new rows for C4 s43 and Scale 1.4B s43, verify the permutation count in Table 7's caption, and replace the "pending" marker for GPT-2m with something else.

Now I'm checking the surrounding text for mentions of these models and reviewing the caption more carefully. The caption references permutation testing at p<0.05 and cross-method consensus as a multiplicity control, but I need to confirm the actual n_perm value used and make sure it's documented properly. I'm checking the table caption for mentions of n_perm and noticing it's missing — the main text specifies 5,000 permutations, so I should add that to the caption. I also need to update the "single seed per condition" claim since the new rows for C4 and Scale add additional seeds, and I'm verifying the GPT-2-medium pair count since the task indicates it should be 8/8, not 6. I need to update the caption since the task shows GPT-2-medium now has 8 pairs with the /8 denominator, not the original 6 pairs that MAUVE excluded. Let me just follow what the task specifies rather than second-guessing the data. For the caption, I need to add n_perm=5000 since it's not currently mentioned. Looking at the footnote for C4, I should check if it needs updating given the new rows being added, but the task only explicitly asks for the n_perm addition and removing "Preliminary" markers, so I'll stick to those changes and keep the footnote as is unless the data actually contradicts it. Generating the table data... Generating the results table... I'm realizing I need to add seed labels to disambiguate between the s42 and s43 runs—the current C4 row should be marked as (s42) now that I'm adding a (s43) variant. I should also update the caption since we're no longer using a single seed per condition, and I need to revise the dagger footnote to reflect the changes to both seed versions. Since C4 s42 is shifting to 6/8, the footnote's reference to "the single non-consensus pair" is now outdated and needs adjustment to reflect multiple non-consensus pairs instead. I'm reviewing the specific metric changes across Diff, Thresh, PG_fwd, and PG_rev to determine how substantially the footnote content should be revised, though I want to be careful not to over-edit beyond what's necessary for consistency. not be necessary anymore, so I'll remove the dagger from the C4 rows and convert the footnote into a general table note instead. I'm planning to write a Python script to handle all these edits systematically—reading the file, identifying the exact lines that need changing, and applying them via ssh_execute.

Now I need to pinpoint the exact line numbers where the table starts so I can make the targeted changes.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "1aa28e01-27e2-4625-b8e8-d9771015529b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FEdxVndmCWcBe6aqHE21d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3275,
      "cache_read_input_tokens": 33991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3275
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

_source line 26_

Let me get the exact line numbers of Table 7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "225e8621-737a-410c-91c4-ef34d13d521f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FEdxVndmCWcBe6aqHE21d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3275,
      "cache_read_input_tokens": 33991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3275
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Sbsy96BuHGqgb96BHBDECP`</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"tab:generalization\\|Baseline.*Pythia.*Wiki\\|GPT-2-medium.*Wiki\\|OPT-1.3B.*Wiki\\|Pythia-1.4B.*Wiki\\|Pythia-1B.*C4\\|bottomrule\\|footnotesize\\|pending\\|dagger\\|single seed\" /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "3d29f35c-0bdd-4f9a-ae48-0467aac47ece",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FEdxVndmCWcBe6aqHE21d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3275,
      "cache_read_input_tokens": 33991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3275
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

_source line 28 · 2026-05-18T12:27:45.136Z_

<details><summary>↩ Tool result · `toolu_01Sbsy96BuHGqgb96BHBDECP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "d17dc60a-ba85-4f62-8e62-bb836210416b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0182vdEWfYg8eyhKBRWxTiHJ`</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"tab:generalization\" /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "429dc49d-94ea-418e-9491-38b25154007a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aZYyQQYspzV2wdcBKAPtL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 37266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4903
      },
      "output_tokens": 69,
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

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017ZBQTTJVSkYwyERFf7Aqqv`</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"pending\" /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "f079e1c0-f071-4295-8ae9-89a687402df8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aZYyQQYspzV2wdcBKAPtL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 37266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4903
      },
      "output_tokens": 69,
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

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015CFFYVqWBy6sDBCpTU8hdc`</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"bottomrule\" /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "b36c5710-ee74-441f-a1d7-4ef2c24b9421",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aZYyQQYspzV2wdcBKAPtL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 37266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4903
      },
      "output_tokens": 69,
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

_source line 32 · 2026-05-18T12:27:51.193Z_

<details><summary>↩ Tool result · `toolu_0182vdEWfYg8eyhKBRWxTiHJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"343:\\\\label{tab:generalization}\\n362:Table~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\n384:Table~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.14}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "9810ace8-4143-400c-a1e7-eafd5b4af3a9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"343:\\\\\\\\label{tab:generalization}\\\\n362:Table~\\\\\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\\\n384:Table~\\\\\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.14}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"343:\\\\label{tab:generalization}\\n362:Table~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\n384:Table~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.14}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TLYxLc4e7JaqynR9LBjZmn`</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"dagger\" /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "0d1f523b-8f55-4e83-af37-275826c0bc2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aZYyQQYspzV2wdcBKAPtL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4903,
      "cache_read_input_tokens": 37266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4903
      },
      "output_tokens": 69,
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

_source line 34 · 2026-05-18T12:27:53.904Z_

<details><summary>↩ Tool result · `toolu_017ZBQTTJVSkYwyERFf7Aqqv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"211:Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\\\max}$.\\n307:Toda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\\\\max}$), confirming its poor sensitivity at $T{=}10$.\\n349:Architecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\textit{pending} \\\\\\\\\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "5bf9555f-ecdb-44f4-952e-1b6c3d1194b6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"211:Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\\\\\\\max}$.\\\\n307:Toda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\\\\\\\\max}$), confirming its poor sensitivity at $T{=}10$.\\\\n349:Architecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\\\\\textit{pending} \\\\\\\\\\\\\\\\\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.7}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"211:Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\\\max}$.\\n307:Toda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\\\\max}$), confirming its poor sensitivity at $T{=}10$.\\n349:Architecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\textit{pending} \\\\\\\\\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T12:27:54.833Z_

<details><summary>↩ Tool result · `toolu_015CFFYVqWBy6sDBCpTU8hdc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"45:\\\\bottomrule\\n119:\\\\bottomrule\\n171:\\\\bottomrule\\n297:\\\\bottomrule\\n327:\\\\bottomrule\\n353:\\\\bottomrule\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "c640c6df-cb94-4d09-99ed-b542fdc2448b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"45:\\\\\\\\bottomrule\\\\n119:\\\\\\\\bottomrule\\\\n171:\\\\\\\\bottomrule\\\\n297:\\\\\\\\bottomrule\\\\n327:\\\\\\\\bottomrule\\\\n353:\\\\\\\\bottomrule\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.92}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"45:\\\\bottomrule\\n119:\\\\bottomrule\\n171:\\\\bottomrule\\n297:\\\\bottomrule\\n327:\\\\bottomrule\\n353:\\\\bottomrule\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T12:27:56.779Z_

<details><summary>↩ Tool result · `toolu_01TLYxLc4e7JaqynR9LBjZmn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"108:\\\\caption{Significance rates (\\\\%) for five lead-lag methods across contamination levels (Pythia-410M). Method choice swings significance from 100\\\\% (naive cross-correlation) to 0\\\\% (permutation Granger) at $\\\\alpha{\\\\leq}0.25$, with seed-dependent onset at $\\\\alpha{=}0.50$, demonstrating that single-method conclusions are unreliable. Each cell reports the fraction of 8 canary$\\\\to$downstream pairs (token entropy and ECE $\\\\times$ 4 downstream metrics) reaching significance ($p{<}0.05$), excluding failed candidates (\\\\S\\\\ref{sec:case_study}). Seed coverage: $\\\\alpha{=}1.0$: 4 seeds (32 pairs); $\\\\alpha{=}0.00$, $\\\\alpha{=}0.75$: 3 seeds (24 pairs); $\\\\alpha{=}0.25$ Toda--Yamamoto: 3 seeds (24 pairs), other methods single seed; $\\\\alpha{=}0.50$: 3~seeds for permutation Granger (range shown), single seed for other methods. $^\\\\dagger$Seed-dependent onset: s42${=}$0/8, s43${=}$6/8, s44${=}$3/8 (median 3/8).}\\n117:Perm.\\\\ Granger  & 0     & 0    & 0--75$^\\\\dagger$  & 79.2  & 75    & 0    \\\\\\\\\\n352:Domain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\dagger$ \\\\\\\\\\n356:{\\\\footnotesize $^\\\\dagger$C4 domain (s42): token\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\_entropy$\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.94}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "c37ff304-7f36-45c5-ad6a-da0d9e2a9e93",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"108:\\\\\\\\caption{Significance rates (\\\\\\\\%) for five lead-lag methods across contamination levels (Pythia-410M). Method choice swings significance from 100\\\\\\\\% (naive cross-correlation) to 0\\\\\\\\% (permutation Granger) at $\\\\\\\\alpha{\\\\\\\\leq}0.25$, with seed-dependent onset at $\\\\\\\\alpha{=}0.50$, demonstrating that single-method conclusions are unreliable. Each cell reports the fraction of 8 canary$\\\\\\\\to$downstream pairs (token entropy and ECE $\\\\\\\\times$ 4 downstream metrics) reaching significance ($p{<}0.05$), excluding failed candidates (\\\\\\\\S\\\\\\\\ref{sec:case_study}). Seed coverage: $\\\\\\\\alpha{=}1.0$: 4 seeds (32 pairs); $\\\\\\\\alpha{=}0.00$, $\\\\\\\\alpha{=}0.75$: 3 seeds (24 pairs); $\\\\\\\\alpha{=}0.25$ Toda--Yamamoto: 3 seeds (24 pairs), other methods single seed; $\\\\\\\\alpha{=}0.50$: 3~seeds for permutation Granger (range shown), single seed for other methods. $^\\\\\\\\dagger$Seed-dependent onset: s42${=}$0/8, s43${=}$6/8, s44${=}$3/8 (median 3/8).}\\\\n117:Perm.\\\\\\\\ Granger  & 0     & 0    & 0--75$^\\\\\\\\dagger$  & 79.2  & 75    & 0    \\\\\\\\\\\\\\\\\\\\n352:Domain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\\\\\dagger$ \\\\\\\\\\\\\\\\\\\\n356:{\\\\\\\\footnotesize $^\\\\\\\\dagger$C4 domain (s42): token\\\\\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\\\\\_entropy$\\\\\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\\\\\\\\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.94}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"108:\\\\caption{Significance rates (\\\\%) for five lead-lag methods across contamination levels (Pythia-410M). Method choice swings significance from 100\\\\% (naive cross-correlation) to 0\\\\% (permutation Granger) at $\\\\alpha{\\\\leq}0.25$, with seed-dependent onset at $\\\\alpha{=}0.50$, demonstrating that single-method conclusions are unreliable. Each cell reports the fraction of 8 canary$\\\\to$downstream pairs (token entropy and ECE $\\\\times$ 4 downstream metrics) reaching significance ($p{<}0.05$), excluding failed candidates (\\\\S\\\\ref{sec:case_study}). Seed coverage: $\\\\alpha{=}1.0$: 4 seeds (32 pairs); $\\\\alpha{=}0.00$, $\\\\alpha{=}0.75$: 3 seeds (24 pairs); $\\\\alpha{=}0.25$ Toda--Yamamoto: 3 seeds (24 pairs), other methods single seed; $\\\\alpha{=}0.50$: 3~seeds for permutation Granger (range shown), single seed for other methods. $^\\\\dagger$Seed-dependent onset: s42${=}$0/8, s43${=}$6/8, s44${=}$3/8 (median 3/8).}\\n117:Perm.\\\\ Granger  & 0     & 0    & 0--75$^\\\\dagger$  & 79.2  & 75    & 0    \\\\\\\\\\n352:Domain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\dagger$ \\\\\\\\\\n356:{\\\\footnotesize $^\\\\dagger$C4 domain (s42): token\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\_entropy$\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.94}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now I have the line numbers. Let me read lines 335-360 to get the full table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "dd2877ed-03aa-452d-a7a8-6d7a3151eb11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NghaYkUCy2us4WQvQVCzHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1759,
      "cache_read_input_tokens": 42169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1759
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

_source line 38_

Now let me read the exact table lines (335-360).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "6bda74b0-e76d-43f9-8e65-932422ac68b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NghaYkUCy2us4WQvQVCzHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1759,
      "cache_read_input_tokens": 42169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1759
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

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CUutZRdNsMVccMA8G2KZSz`</summary>

```json
{
  "server": "westd-19828",
  "command": "cat -n /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "a18c93cd-4ac3-499d-b675-4cf9e319197a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NghaYkUCy2us4WQvQVCzHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1759,
      "cache_read_input_tokens": 42169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1759
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

_source line 40 · 2026-05-18T12:28:04.127Z_

<details><summary>↩ Tool result · `toolu_01CUutZRdNsMVccMA8G2KZSz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Experiments}\\n     2\\t\\\\label{sec:experiments}\\n     3\\t\\n     4\\t\\\\subsection{Experimental Setup}\\n     5\\t\\\\label{sec:setup}\\n     6\\t\\n     7\\tWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\n     8\\tPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\n     9\\tCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\S\\\\ref{sec:method_sensitivity}, \\\\S\\\\ref{sec:regime}, and \\\\S\\\\ref{sec:discussion}.\\n    10\\tTraining data is drawn from WikiText-103 \\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\n    11\\t\\n    12\\tOur protocol follows the replace paradigm of \\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\alpha{<}1.0$.\\n    13\\tEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\alpha$ fraction synthetic data and $(1{-}\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\n    14\\tWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$.\\n    15\\tThe $\\\\alpha{=}1.0$ condition uses four random seeds $\\\\{42, 43, 44, 45\\\\}$; $\\\\alpha{=}0.00$, $\\\\alpha{=}0.25$, and $\\\\alpha{=}0.75$ each use three seeds $\\\\{42, 43, 44\\\\}$; $\\\\alpha{=}0.50$ uses three seeds $\\\\{42, 43, 44\\\\}$.\\n    16\\t\\n    17\\tWe track two \\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\cite{scheffer2009early}) and three \\\\emph{downstream metrics}.\\n    18\\tCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\n    19\\tDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\n    20\\tToken entropy is the mean next-token prediction entropy $H(p_\\\\theta | \\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\n    21\\tWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\S\\\\ref{sec:case_study}).\\n    22\\tResults for distinct-3 are reported in Appendix~\\\\ref{app:distinct3}.\\n    23\\tCode and data will be released upon publication.\\n    24\\t\\n    25\\tEach canary-downstream pair is independently tested for directional predictive improvement.\\n    26\\tPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\n    27\\tIndividual method significance is assessed at $\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\% false positive rate under the null (Table~\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\n    28\\tCross-correlation analysis uses a maximum lag of 5 generations.\\n    29\\tTable~\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\n    30\\t\\n    31\\t\\\\begin{\\n\\n... [截断: 输出过长，省略 33983 字符] ...\\n\\nle~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\n   363\\tAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\n   364\\tToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n   365\\t\\n   366\\tMethod-level variation across architectures is informative.\\n   367\\tThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\n   368\\tToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\n   369\\tDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n   370\\t\\n   371\\t\\\\paragraph{Scale generalization.}\\n   372\\tScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\n   373\\tOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\n   374\\tThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\n   375\\tThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\n   376\\tToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\n   377\\tThe consensus framework absorbs this single-method failure by design.\\n   378\\t\\n   379\\t\\\\paragraph{Domain generalization.}\\n   380\\tReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\n   381\\tWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\n   382\\tInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n   383\\t\\n   384\\tTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\n   385\\tPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\n   386\\tECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\n   387\\tTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.55}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "870b5eaf-f31f-4e83-8842-ff64e05e2133",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"     1\\\\t\\\\\\\\section{Experiments}\\\\n     2\\\\t\\\\\\\\label{sec:experiments}\\\\n     3\\\\t\\\\n     4\\\\t\\\\\\\\subsection{Experimental Setup}\\\\n     5\\\\t\\\\\\\\label{sec:setup}\\\\n     6\\\\t\\\\n     7\\\\tWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\\\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\\\n     8\\\\tPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\\\n     9\\\\tCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}, \\\\\\\\S\\\\\\\\ref{sec:regime}, and \\\\\\\\S\\\\\\\\ref{sec:discussion}.\\\\n    10\\\\tTraining data is drawn from WikiText-103 \\\\\\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\\\n    11\\\\t\\\\n    12\\\\tOur protocol follows the replace paradigm of \\\\\\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\\\\\alpha{<}1.0$.\\\\n    13\\\\tEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\\\\\alpha$ fraction synthetic data and $(1{-}\\\\\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\\\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\\\n    14\\\\tWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\\\\\alpha \\\\\\\\in \\\\\\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\\\\\}$.\\\\n    15\\\\tThe $\\\\\\\\alpha{=}1.0$ condition uses four random seeds $\\\\\\\\{42, 43, 44, 45\\\\\\\\}$; $\\\\\\\\alpha{=}0.00$, $\\\\\\\\alpha{=}0.25$, and $\\\\\\\\alpha{=}0.75$ each use three seeds $\\\\\\\\{42, 43, 44\\\\\\\\}$; $\\\\\\\\alpha{=}0.50$ uses three seeds $\\\\\\\\{42, 43, 44\\\\\\\\}$.\\\\n    16\\\\t\\\\n    17\\\\tWe track two \\\\\\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\\\\\cite{scheffer2009early}) and three \\\\\\\\emph{downstream metrics}.\\\\n    18\\\\tCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\\\n    19\\\\tDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\\\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\\\n    20\\\\tToken entropy is the mean next-token prediction entropy $H(p_\\\\\\\\theta | \\\\\\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\\\n    21\\\\tWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\\\\\S\\\\\\\\ref{sec:case_study}).\\\\n    22\\\\tResults for distinct-3 are reported in Appendix~\\\\\\\\ref{app:distinct3}.\\\\n    23\\\\tCode and data will be released upon publication.\\\\n    24\\\\t\\\\n    25\\\\tEach canary-downstream pair is independently tested for directional predictive improvement.\\\\n    26\\\\tPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\\\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\\\n    27\\\\tIndividual method significance is assessed at $\\\\\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\\\\\% false positive rate under the null (Table~\\\\\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\\\n    28\\\\tCross-correlation analysis uses a maximum lag of 5 generations.\\\\n    29\\\\tTable~\\\\\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\\\n    30\\\\t\\\\n    31\\\\t\\\\\\\\begin{\\\\n\\\\n... [截断: 输出过长，省略 33983 字符] ...\\\\n\\\\nle~\\\\\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\\\n   363\\\\tAll models reach Tier~3 consensus ($K{\\\\\\\\geq}4/5$) with 6/8 canary$\\\\\\\\to$diversity pairs confirmed.\\\\n   364\\\\tToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\\\n   365\\\\t\\\\n   366\\\\tMethod-level variation across architectures is informative.\\\\n   367\\\\tThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\\\n   368\\\\tToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\n   369\\\\tDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\\\\\geq}4/5$.\\\\n   370\\\\t\\\\n   371\\\\t\\\\\\\\paragraph{Scale generalization.}\\\\n   372\\\\tScaling from 410M to 1.4B parameters (3.4$\\\\\\\\times$) preserves majority consensus ($K{\\\\\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\\\n   373\\\\tOf the three non-consensus pairs, two target perplexity (token\\\\\\\\_entropy$\\\\\\\\to$perplexity, $K{=}1$; ECE$\\\\\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).\\\\n   374\\\\tThe sole scale-specific miss is token\\\\\\\\_entropy$\\\\\\\\to$distinct\\\\\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\\\n   375\\\\tThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\\\n   376\\\\tToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\n   377\\\\tThe consensus framework absorbs this single-method failure by design.\\\\n   378\\\\t\\\\n   379\\\\t\\\\\\\\paragraph{Domain generalization.}\\\\n   380\\\\tReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\\\n   381\\\\tWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\\\n   382\\\\tInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\\\n   383\\\\t\\\\n   384\\\\tTable~\\\\\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\\\n   385\\\\tPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\\\n   386\\\\tECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\\\n   387\\\\tTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\\\\\alpha{=}1.0$.\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.55}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\\section{Experiments}\\n     2\\t\\\\label{sec:experiments}\\n     3\\t\\n     4\\t\\\\subsection{Experimental Setup}\\n     5\\t\\\\label{sec:setup}\\n     6\\t\\n     7\\tWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\n     8\\tPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\n     9\\tCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\S\\\\ref{sec:method_sensitivity}, \\\\S\\\\ref{sec:regime}, and \\\\S\\\\ref{sec:discussion}.\\n    10\\tTraining data is drawn from WikiText-103 \\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\n    11\\t\\n    12\\tOur protocol follows the replace paradigm of \\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\alpha{<}1.0$.\\n    13\\tEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\alpha$ fraction synthetic data and $(1{-}\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\n    14\\tWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$.\\n    15\\tThe $\\\\alpha{=}1.0$ condition uses four random seeds $\\\\{42, 43, 44, 45\\\\}$; $\\\\alpha{=}0.00$, $\\\\alpha{=}0.25$, and $\\\\alpha{=}0.75$ each use three seeds $\\\\{42, 43, 44\\\\}$; $\\\\alpha{=}0.50$ uses three seeds $\\\\{42, 43, 44\\\\}$.\\n    16\\t\\n    17\\tWe track two \\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\cite{scheffer2009early}) and three \\\\emph{downstream metrics}.\\n    18\\tCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\n    19\\tDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\n    20\\tToken entropy is the mean next-token prediction entropy $H(p_\\\\theta | \\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\n    21\\tWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\S\\\\ref{sec:case_study}).\\n    22\\tResults for distinct-3 are reported in Appendix~\\\\ref{app:distinct3}.\\n    23\\tCode and data will be released upon publication.\\n    24\\t\\n    25\\tEach canary-downstream pair is independently tested for directional predictive improvement.\\n    26\\tPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\n    27\\tIndividual method significance is assessed at $\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\% false positive rate under the null (Table~\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\n    28\\tCross-correlation analysis uses a maximum lag of 5 generations.\\n    29\\tTable~\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\n    30\\t\\n    31\\t\\\\begin{\\n\\n... [截断: 输出过长，省略 33983 字符] ...\\n\\nle~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\n   363\\tAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\n   364\\tToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n   365\\t\\n   366\\tMethod-level variation across architectures is informative.\\n   367\\tThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\n   368\\tToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\n   369\\tDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n   370\\t\\n   371\\t\\\\paragraph{Scale generalization.}\\n   372\\tScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\n   373\\tOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\n   374\\tThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\n   375\\tThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\n   376\\tToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\n   377\\tThe consensus framework absorbs this single-method failure by design.\\n   378\\t\\n   379\\t\\\\paragraph{Domain generalization.}\\n   380\\tReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\n   381\\tWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\n   382\\tInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n   383\\t\\n   384\\tTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\n   385\\tPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\n   386\\tECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\n   387\\tTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.55}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
The output is truncated again. Let me specifically get lines 335-360.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "201f6fd9-e0cd-47bb-b900-a84fdf213af5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrCVyFZNqLKwgqzhNbMvTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2881,
      "cache_read_input_tokens": 43928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2881
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

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015tLcVZefMvmBqjkx4ifkVX`</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +335 /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "41106944-e97c-420a-8908-279b924f0209",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrCVyFZNqLKwgqzhNbMvTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2881,
      "cache_read_input_tokens": 43928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2881
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

_source line 43 · 2026-05-18T12:28:12.395Z_

<details><summary>↩ Tool result · `toolu_015tLcVZefMvmBqjkx4ifkVX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\nAll conditions use $\\\\alpha{=}1.0$ and a single seed.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\n\\\\label{tab:generalization}\\n\\\\begin{tabular}{llccccccc}\\n\\\\toprule\\nVariation & Model / Dataset & \\\\rotatebox{70}{Naive} & \\\\rotatebox{70}{Diff.\\\\ XCorr} & \\\\rotatebox{70}{Threshold} & \\\\rotatebox{70}{PermG (fwd)} & \\\\rotatebox{70}{PermG (rev)} & \\\\rotatebox{70}{TY} & \\\\rotatebox{70}{$K{\\\\geq}4/5$} \\\\\\\\\\n\\\\midrule\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\textit{pending} \\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\nScale ($3.4\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\dagger$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\vspace{2pt}\\n{\\\\footnotesize $^\\\\dagger$C4 domain (s42): token\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\_entropy$\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\rightarrow$diversity reverse significance ($p\\\\approx 0.03$); token\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\nCanary$\\\\to$perplexity pairs do not reach $K{\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\S\\\\ref{sec:method_sensitivity}).}\\n\\\\end{table}\\n\\n\\\\paragraph{Architecture generalization.}\\nTable~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\nAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n\\nMethod-level variation across architectures is informative.\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n\\n\\\\paragraph{Scale generalization.}\\nScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\nOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\nThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\nThe consensus framework absorbs this single-method failure by design.\\n\\n\\\\paragraph{Domain generalization.}\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n\\nTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "52768ef5-3557-43db-91f4-c1173429190c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\\\\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\\\nAll conditions use $\\\\\\\\alpha{=}1.0$ and a single seed.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\\\n\\\\\\\\label{tab:generalization}\\\\n\\\\\\\\begin{tabular}{llccccccc}\\\\n\\\\\\\\toprule\\\\nVariation & Model / Dataset & \\\\\\\\rotatebox{70}{Naive} & \\\\\\\\rotatebox{70}{Diff.\\\\\\\\ XCorr} & \\\\\\\\rotatebox{70}{Threshold} & \\\\\\\\rotatebox{70}{PermG (fwd)} & \\\\\\\\rotatebox{70}{PermG (rev)} & \\\\\\\\rotatebox{70}{TY} & \\\\\\\\rotatebox{70}{$K{\\\\\\\\geq}4/5$} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\\\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\\\\\textit{pending} \\\\\\\\\\\\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\\\\\\\\\\\nScale ($3.4\\\\\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\\\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\\\\\dagger$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\vspace{2pt}\\\\n{\\\\\\\\footnotesize $^\\\\\\\\dagger$C4 domain (s42): token\\\\\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\\\\\_entropy$\\\\\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\\\\\rightarrow$diversity reverse significance ($p\\\\\\\\approx 0.03$); token\\\\\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\\\\\\\\\\\nCanary$\\\\\\\\to$perplexity pairs do not reach $K{\\\\\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\paragraph{Architecture generalization.}\\\\nTable~\\\\\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\\\nAll models reach Tier~3 consensus ($K{\\\\\\\\geq}4/5$) with 6/8 canary$\\\\\\\\to$diversity pairs confirmed.\\\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\\\n\\\\nMethod-level variation across architectures is informative.\\\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\\\\\geq}4/5$.\\\\n\\\\n\\\\\\\\paragraph{Scale generalization.}\\\\nScaling from 410M to 1.4B parameters (3.4$\\\\\\\\times$) preserves majority consensus ($K{\\\\\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\\\nOf the three non-consensus pairs, two target perplexity (token\\\\\\\\_entropy$\\\\\\\\to$perplexity, $K{=}1$; ECE$\\\\\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).\\\\nThe sole scale-specific miss is token\\\\\\\\_entropy$\\\\\\\\to$distinct\\\\\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\nThe consensus framework absorbs this single-method failure by design.\\\\n\\\\n\\\\\\\\paragraph{Domain generalization.}\\\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\\\n\\\\nTable~\\\\\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\\\\\alpha{=}1.0$.\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\nAll conditions use $\\\\alpha{=}1.0$ and a single seed.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\n\\\\label{tab:generalization}\\n\\\\begin{tabular}{llccccccc}\\n\\\\toprule\\nVariation & Model / Dataset & \\\\rotatebox{70}{Naive} & \\\\rotatebox{70}{Diff.\\\\ XCorr} & \\\\rotatebox{70}{Threshold} & \\\\rotatebox{70}{PermG (fwd)} & \\\\rotatebox{70}{PermG (rev)} & \\\\rotatebox{70}{TY} & \\\\rotatebox{70}{$K{\\\\geq}4/5$} \\\\\\\\\\n\\\\midrule\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\textit{pending} \\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\nScale ($3.4\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\dagger$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\vspace{2pt}\\n{\\\\footnotesize $^\\\\dagger$C4 domain (s42): token\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\_entropy$\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\rightarrow$diversity reverse significance ($p\\\\approx 0.03$); token\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\nCanary$\\\\to$perplexity pairs do not reach $K{\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\S\\\\ref{sec:method_sensitivity}).}\\n\\\\end{table}\\n\\n\\\\paragraph{Architecture generalization.}\\nTable~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\nAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n\\nMethod-level variation across architectures is informative.\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n\\n\\\\paragraph{Scale generalization.}\\nScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\nOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\nThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\nThe consensus framework absorbs this single-method failure by design.\\n\\n\\\\paragraph{Domain generalization.}\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n\\nTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"
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
Now I have a clear picture. Let me also check the line numbers precisely. Based on my earlier grep results:
- Line 343: \label{tab:generalization}
- Line 349: GPT-2-medium / Wiki row with "pending"
- Line 352: C4 row with dagger
- Line 353: \bottomrule
- Line 356: footnote with dagger

Let me now get the exact line numbers for the table area. I need to count from the `tail -n +335` output:
- Line 335: "The methodological pitfalls..."
- Line 336: "To test whether..."


- Line 337: "All conditions use..."
- Line 338: (empty)
- Line 339: \begin{table}[t]
- Line 340: \centering
- Line 341: \small
- Line 342: \caption{...}
- Line 343: \label{tab:generalization}
- Line 344: \begin{tabular}{llccccccc}
- Line 345: \toprule
- Line 346: Variation & Model / Dataset ...
- Line 347: \midrule
- Line 348: Baseline & Pythia-410M / Wiki ...
- Line 349: Architecture & GPT-2-medium / Wiki ... & \textit{pending} \\
- Line 350: Architecture & OPT-1.3

So the table structure starts at line 339 with the table environment, then the tabular content begins at line 344 with the column specification, followed by the header row and data rows starting around line 346.

Looking at the next chunk, I can see the rest of the table rows continuing with different model variations and their corresponding results, ending with the table closing commands at lines 353-354. The footnote content appears at lines 356-358 before the table ends.

Now I'm ready to write a Python script that will make all the necessary edits to this table in one pass. I need to reorganize the table rows to group the Scale and Domain entries by their seed variants, inserting the new s43 rows right after their s42 counterparts rather than at the end.

For the caption, I'm noticing the GPT-2-medium note about "6~pairs (MAUVE excluded)" doesn't align with the task description showing 8/8 values across all methods. I should update this to reflect that GPT-2-medium actually has 8 pairs, and I'll also need to add the perm=5000 mention and adjust the language about seeds since some conditions now have multiple seeds rather than just one. The caption needs to be updated to just say "8 pairs per condition" since GPT-2-medium now includes MAUVE. For the footnote, I need to account for the fact that C4 s42 is now 6/8 instead of 7/8, which means there are two non-consensus pairs rather than one, so the dagger reference should be removed and the C4 note updated accordingly. I need to update the body text references too—C4 s42 dropping to 6/8 means line 384 needs revision, and the GPT-2-medium Toda-Yamamoto result changing from 0/6 to 5/8 contradicts line 368. The task description doesn't explicitly ask for these updates, so I should focus on what was requested: the table, discussion edits, and conclusion changes. I'm noticing several inconsistencies between the table values and the body text that need fixing. The GPT-2-medium Toda-Yamamoto result changed from 0/6 to 5/8, which significantly alters that comparison statement. Similarly, the Pythia-1B C4 result appears to have shifted from 7/8 to 6/8, so I need to update that claim about exceeding the Tier 3 threshold.

The Permutation Granger forward detection also needs correction—it's now 6/8 rather than 8/8. Since the task emphasizes keeping body text consistent with the table, I should systematically go through all numerical references in the results section and align them with the actual table values. I'm going to write a script that identifies and corrects each of these discrepancies across the document. Updating the table rows with corrected metrics and adding the s43 variant for the Pythia-1.4B scale experiment, then modifying the C4 domain row to include both s42 and s43 versions with adjusted values and removing the dagger notation. I'm revising the footnote to clarify the key findings about directional relationships and methodological details—token entropy pairs show consistent unidirectionality while the ECE-diversity relationship shows marginal reverse significance, and I'm noting that canary-perplexity pairs don't meet the threshold due to shared-trend artifacts that get filtered out in the sensitivity analysis. I also need to update the body text since the conditions now use multiple seeds rather than a single one. I need to clarify what the Toda-Yamamoto range actually represents across these architectures. Looking at the baseline conditions, I have Pythia-410M at 4/8, GPT-2-medium at 5/8, and OPT-1.3B at 6/8, so the range is indeed 4/8 to 6/8. The earlier "0/6" was likely a misinterpretation—probably conflating the number of pairs with the actual TY hits. Now that I have the correct GPT-2-medium value of 5/8, I can update the sentence to reflect this narrower, more accurate range.

For the Scale paragraph discussion, adding the s43 seed data (6/8) means I need to reconsider how to present the majority consensus statement. The current phrasing about "5/8 pairs" was specific to s42 alone, but now with both seeds included, I should acknowledge both values rather than rewriting the entire paragraph.

More critically, I'm catching errors in the claims about C4 results. The Pythia-1B on C4 line claims 7/8 consensus exceeding the baseline, but the actual data shows 6/8 for both seeds, which matches rather than exceeds the WikiText baseline. Similarly, the Permutation Granger forward detection claim of 8/8 is incorrect—it's actually 6/8 for C4 s42. These factual corrections need to be made directly in the text.

Rather than manually editing each line, I should write a script to handle these replacements systematically. I'm continuing through the table structure, seeing the rows for different model variations and their corresponding architectures and scales. The table includes footnotes about the C4 domain and canary metrics, then transitions into a paragraph discussing how the architecture generalization results confirm the findings across different model sizes.

Now I'm looking at the performance metrics across different detection methods—token entropy shows consistent results, while threshold onset detection performs well on larger models like OPT-1.3B, though the Toda-Yamamoto method shows more variability depending on the architecture. Moving into the scale generalization section, I'm examining how the methods perform as model size increases from 410M to 1.4B parameters, with threshold onset detection maintaining strong performance across scales while Toda-Yamamoto struggles consistently.

For domain generalization, I'm switching the evaluation dataset from WikiText-103 to C4 and using bounded diversity metrics instead of perplexity to assess how well the detection methods transfer across different text domains. The results show that Pythia-1B achieves strong detection rates on C4, with permutation Granger forward detection reaching perfect scores and ECE reverse leakage appearing in most verified conditions.

Now I'm working through the caption updates. For line 337, I need to clarify the seed structure—Architecture uses a single seed while Scale and Domain conditions each use two seeds for replication. For line 368, I'm revising how the Toda-Yamamoto range is described to be more precise about which models achieve which detection rates. Looking at the Scale paragraph with both seeds now, I need to balance updating the numbers while keeping the analysis grounded. Since s42 and s43 show different consensus levels and failure patterns, I should present both data points but avoid over-specifying individual pair failures that might not generalize. I'll be conservative with the rewrites and focus on what the task explicitly requires—Table 7 updates and removing the GPT-2m conditional phrasing—rather than extensively revising the body text.

Now I'm identifying the specific lines that contain factually incorrect numbers: the single seed reference, the GPT-2-medium TY value, the pair counts, and the detection rates that need updating for the new multi-seed results. I'll write a script to make these targeted replacements reliably.

Writing the update script... Updating the experiment results table... Updating the C4 domain rows with new seed labels and adjusted metrics, then replacing the footnote to reflect the corrected analysis for the C4 domain seed 42 results. I'm working on replacing the footnote text in the Python script, but the backslash escaping is getting complicated. Let me switch to a line-by-line file reading approach instead, which will be more reliable. I should also refine the figure caption to be more concise—right now it's explaining the methodology and pair counts, but I can compress that down to the essential details about what the figure shows and how significance is determined. I'm settling on a Python script approach to handle the multiline edits safely, since I have the line numbers pinned down from my earlier check—the caption is on line 342, and the table rows I need to modify are on lines 349-352. I'll read the file, make the targeted changes, and write it back out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "c2ef1c85-be71-4149-958d-f513c47cac2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wn3cocrnapXyo94KHXkAnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2524,
      "cache_read_input_tokens": 46809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2524
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

Now I have the full picture. Let me verify exact line numbers around Table 7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "d5af6187-fb9f-41da-be4f-be7f439cac71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wn3cocrnapXyo94KHXkAnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2524,
      "cache_read_input_tokens": 46809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2524
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

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RQEFDbt9Keyv14qqaejH1g`</summary>

```json
{
  "server": "westd-19828",
  "command": "head -n 390 /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "8444a1b2-2793-4c3d-ad96-d03d18536d4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wn3cocrnapXyo94KHXkAnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2524,
      "cache_read_input_tokens": 46809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2524
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

_source line 47 · 2026-05-18T12:30:16.241Z_

<details><summary>↩ Tool result · `toolu_01RQEFDbt9Keyv14qqaejH1g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\\\label{sec:experiments}\\n\\n\\\\subsection{Experimental Setup}\\n\\\\label{sec:setup}\\n\\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\S\\\\ref{sec:method_sensitivity}, \\\\S\\\\ref{sec:regime}, and \\\\S\\\\ref{sec:discussion}.\\nTraining data is drawn from WikiText-103 \\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\n\\nOur protocol follows the replace paradigm of \\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\alpha{<}1.0$.\\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\alpha$ fraction synthetic data and $(1{-}\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$.\\nThe $\\\\alpha{=}1.0$ condition uses four random seeds $\\\\{42, 43, 44, 45\\\\}$; $\\\\alpha{=}0.00$, $\\\\alpha{=}0.25$, and $\\\\alpha{=}0.75$ each use three seeds $\\\\{42, 43, 44\\\\}$; $\\\\alpha{=}0.50$ uses three seeds $\\\\{42, 43, 44\\\\}$.\\n\\nWe track two \\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\cite{scheffer2009early}) and three \\\\emph{downstream metrics}.\\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\nToken entropy is the mean next-token prediction entropy $H(p_\\\\theta | \\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\S\\\\ref{sec:case_study}).\\nResults for distinct-3 are reported in Appendix~\\\\ref{app:distinct3}.\\nCode and data will be released upon publication.\\n\\nEach canary-downstream pair is independently tested for directional predictive improvement.\\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\nIndividual method significance is assessed at $\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\% false positive rate under the null (Table~\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\nCross-correlation analysis uses a maximum lag of 5 generations.\\nTable~\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Metric drift (\\\\%, generation~0$\\\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\\\alpha$ levels, with the strongest decline at moderate contami\\n\\n... [截断: 输出过长，省略 31274 字符] ...\\n\\nn any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\S\\\\ref{sec:method_sensitivity}).}\\n\\\\end{table}\\n\\n\\\\paragraph{Architecture generalization.}\\nTable~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\nAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n\\nMethod-level variation across architectures is informative.\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n\\n\\\\paragraph{Scale generalization.}\\nScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\nOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\nThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\nThe consensus framework absorbs this single-method failure by design.\\n\\n\\\\paragraph{Domain generalization.}\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n\\nTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.59}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "fef73740-e415-4404-bd44-f6194ca16580",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\\section{Experiments}\\\\n\\\\\\\\label{sec:experiments}\\\\n\\\\n\\\\\\\\subsection{Experimental Setup}\\\\n\\\\\\\\label{sec:setup}\\\\n\\\\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\\\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\\\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\\\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}, \\\\\\\\S\\\\\\\\ref{sec:regime}, and \\\\\\\\S\\\\\\\\ref{sec:discussion}.\\\\nTraining data is drawn from WikiText-103 \\\\\\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\\\n\\\\nOur protocol follows the replace paradigm of \\\\\\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\\\\\alpha{<}1.0$.\\\\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\\\\\alpha$ fraction synthetic data and $(1{-}\\\\\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\\\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\\\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\\\\\alpha \\\\\\\\in \\\\\\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\\\\\}$.\\\\nThe $\\\\\\\\alpha{=}1.0$ condition uses four random seeds $\\\\\\\\{42, 43, 44, 45\\\\\\\\}$; $\\\\\\\\alpha{=}0.00$, $\\\\\\\\alpha{=}0.25$, and $\\\\\\\\alpha{=}0.75$ each use three seeds $\\\\\\\\{42, 43, 44\\\\\\\\}$; $\\\\\\\\alpha{=}0.50$ uses three seeds $\\\\\\\\{42, 43, 44\\\\\\\\}$.\\\\n\\\\nWe track two \\\\\\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\\\\\cite{scheffer2009early}) and three \\\\\\\\emph{downstream metrics}.\\\\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\\\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\\\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\\\nToken entropy is the mean next-token prediction entropy $H(p_\\\\\\\\theta | \\\\\\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\\\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\\\\\S\\\\\\\\ref{sec:case_study}).\\\\nResults for distinct-3 are reported in Appendix~\\\\\\\\ref{app:distinct3}.\\\\nCode and data will be released upon publication.\\\\n\\\\nEach canary-downstream pair is independently tested for directional predictive improvement.\\\\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\\\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\\\nIndividual method significance is assessed at $\\\\\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\\\\\% false positive rate under the null (Table~\\\\\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\\\nCross-correlation analysis uses a maximum lag of 5 generations.\\\\nTable~\\\\\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Metric drift (\\\\\\\\%, generation~0$\\\\\\\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\\\\\\\alpha$ levels, with the strongest decline at moderate contami\\\\n\\\\n... [截断: 输出过长，省略 31274 字符] ...\\\\n\\\\nn any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\paragraph{Architecture generalization.}\\\\nTable~\\\\\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\\\nAll models reach Tier~3 consensus ($K{\\\\\\\\geq}4/5$) with 6/8 canary$\\\\\\\\to$diversity pairs confirmed.\\\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\\\n\\\\nMethod-level variation across architectures is informative.\\\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\\\\\geq}4/5$.\\\\n\\\\n\\\\\\\\paragraph{Scale generalization.}\\\\nScaling from 410M to 1.4B parameters (3.4$\\\\\\\\times$) preserves majority consensus ($K{\\\\\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\\\nOf the three non-consensus pairs, two target perplexity (token\\\\\\\\_entropy$\\\\\\\\to$perplexity, $K{=}1$; ECE$\\\\\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).\\\\nThe sole scale-specific miss is token\\\\\\\\_entropy$\\\\\\\\to$distinct\\\\\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\nThe consensus framework absorbs this single-method failure by design.\\\\n\\\\n\\\\\\\\paragraph{Domain generalization.}\\\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\\\n\\\\nTable~\\\\\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\\\\\alpha{=}1.0$.\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.59}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\\\label{sec:experiments}\\n\\n\\\\subsection{Experimental Setup}\\n\\\\label{sec:setup}\\n\\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\\\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\\\S\\\\ref{sec:method_sensitivity}, \\\\S\\\\ref{sec:regime}, and \\\\S\\\\ref{sec:discussion}.\\nTraining data is drawn from WikiText-103 \\\\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\\n\\nOur protocol follows the replace paradigm of \\\\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\\\alpha{<}1.0$.\\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\\\alpha$ fraction synthetic data and $(1{-}\\\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\\\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\\\alpha \\\\in \\\\{0.00, 0.25, 0.50, 0.75, 1.00\\\\}$.\\nThe $\\\\alpha{=}1.0$ condition uses four random seeds $\\\\{42, 43, 44, 45\\\\}$; $\\\\alpha{=}0.00$, $\\\\alpha{=}0.25$, and $\\\\alpha{=}0.75$ each use three seeds $\\\\{42, 43, 44\\\\}$; $\\\\alpha{=}0.50$ uses three seeds $\\\\{42, 43, 44\\\\}$.\\n\\nWe track two \\\\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\\\cite{scheffer2009early}) and three \\\\emph{downstream metrics}.\\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\\\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\\nToken entropy is the mean next-token prediction entropy $H(p_\\\\theta | \\\\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\\\S\\\\ref{sec:case_study}).\\nResults for distinct-3 are reported in Appendix~\\\\ref{app:distinct3}.\\nCode and data will be released upon publication.\\n\\nEach canary-downstream pair is independently tested for directional predictive improvement.\\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\\\cite{shojaie2022granger} to obtain exact $p$-values; other methods employ nonparametric significance tests.\\nIndividual method significance is assessed at $\\\\alpha{=}0.05$ (permutation $p$-values for PermG, $n{=}5{,}000$; standard tests for others). Multiplicity across the eight causal pairs is controlled by the consensus threshold $K{\\\\geq}4/5$, which requires at least four of five independent methods to detect significance for a given pair. This empirically yields 0\\\\% false positive rate under the null (Table~\\\\ref{tab:fpr_fnr}), avoiding the over-conservatism of applying BH FDR to component tests within an already-stringent consensus filter.\\nCross-correlation analysis uses a maximum lag of 5 generations.\\nTable~\\\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Metric drift (\\\\%, generation~0$\\\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\\\alpha$ levels, with the strongest decline at moderate contami\\n\\n... [截断: 输出过长，省略 31274 字符] ...\\n\\nn any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\S\\\\ref{sec:method_sensitivity}).}\\n\\\\end{table}\\n\\n\\\\paragraph{Architecture generalization.}\\nTable~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\nAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n\\nMethod-level variation across architectures is informative.\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n\\n\\\\paragraph{Scale generalization.}\\nScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\nOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\nThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\nThe consensus framework absorbs this single-method failure by design.\\n\\n\\\\paragraph{Domain generalization.}\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n\\nTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.59}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
OK, the output is still getting truncated in the middle. Let me use a more targeted approach. Let me get lines 335-390 specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "cdbebff2-515b-472b-becd-5145bd3f3aee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNDv52EepxxPdsk8cGdRGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10970,
      "cache_read_input_tokens": 49333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10970
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

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VxPqUGEiiZEoZaWWtWa22W`</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "9a59bd10-8893-4819-b8aa-7daa1cf6a8a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNDv52EepxxPdsk8cGdRGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10970,
      "cache_read_input_tokens": 49333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10970
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

_source line 50 · 2026-05-18T12:30:22.768Z_

<details><summary>↩ Tool result · `toolu_01VxPqUGEiiZEoZaWWtWa22W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"386 /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "dafe8d2d-dff1-4051-8ac0-6632b8fecb2f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"386 /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"386 /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.47}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BzdBM9hxqq2mvWpRbyNGJF`</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n 52 /root/autodl-tmp/distrib_canary_collapse/docs/paper/experiments.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "70016c2a-f3d7-4687-a65a-060e9156125e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRzWRobcBT49vozU4Eb9xJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 60303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 275
      },
      "output_tokens": 63,
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

_source line 52 · 2026-05-18T12:30:26.849Z_

<details><summary>↩ Tool result · `toolu_01BzdBM9hxqq2mvWpRbyNGJF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\nAll conditions use $\\\\alpha{=}1.0$ and a single seed.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\n\\\\label{tab:generalization}\\n\\\\begin{tabular}{llccccccc}\\n\\\\toprule\\nVariation & Model / Dataset & \\\\rotatebox{70}{Naive} & \\\\rotatebox{70}{Diff.\\\\ XCorr} & \\\\rotatebox{70}{Threshold} & \\\\rotatebox{70}{PermG (fwd)} & \\\\rotatebox{70}{PermG (rev)} & \\\\rotatebox{70}{TY} & \\\\rotatebox{70}{$K{\\\\geq}4/5$} \\\\\\\\\\n\\\\midrule\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\textit{pending} \\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\nScale ($3.4\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\dagger$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\vspace{2pt}\\n{\\\\footnotesize $^\\\\dagger$C4 domain (s42): token\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\_entropy$\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\rightarrow$diversity reverse significance ($p\\\\approx 0.03$); token\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\nCanary$\\\\to$perplexity pairs do not reach $K{\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\S\\\\ref{sec:method_sensitivity}).}\\n\\\\end{table}\\n\\n\\\\paragraph{Architecture generalization.}\\nTable~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\nAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n\\nMethod-level variation across architectures is informative.\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n\\n\\\\paragraph{Scale generalization.}\\nScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\nOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\nThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\nThe consensus framework absorbs this single-method failure by design.\\n\\n\\\\paragraph{Domain generalization.}\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n\\nTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "43bde036-ddb7-4689-ae2f-5d919553cd13",
  "uuid": "8c942fbb-9a31-4f80-a38b-540b27b2de72",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\\\nAll conditions use $\\\\\\\\alpha{=}1.0$ and a single seed.\\\\n\\\\n\\\\\\\\begin{table}[t]\\\\n\\\\\\\\centering\\\\n\\\\\\\\small\\\\n\\\\\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\\\n\\\\\\\\label{tab:generalization}\\\\n\\\\\\\\begin{tabular}{llccccccc}\\\\n\\\\\\\\toprule\\\\nVariation & Model / Dataset & \\\\\\\\rotatebox{70}{Naive} & \\\\\\\\rotatebox{70}{Diff.\\\\\\\\ XCorr} & \\\\\\\\rotatebox{70}{Threshold} & \\\\\\\\rotatebox{70}{PermG (fwd)} & \\\\\\\\rotatebox{70}{PermG (rev)} & \\\\\\\\rotatebox{70}{TY} & \\\\\\\\rotatebox{70}{$K{\\\\\\\\geq}4/5$} \\\\\\\\\\\\\\\\\\\\n\\\\\\\\midrule\\\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\\\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\\\\\textit{pending} \\\\\\\\\\\\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\\\\\\\\\\\nScale ($3.4\\\\\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\\\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\\\\\dagger$ \\\\\\\\\\\\\\\\\\\\n\\\\\\\\bottomrule\\\\n\\\\\\\\end{tabular}\\\\n\\\\\\\\vspace{2pt}\\\\n{\\\\\\\\footnotesize $^\\\\\\\\dagger$C4 domain (s42): token\\\\\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\\\\\_entropy$\\\\\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\\\\\rightarrow$diversity reverse significance ($p\\\\\\\\approx 0.03$); token\\\\\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\\\\\\\\\\\nCanary$\\\\\\\\to$perplexity pairs do not reach $K{\\\\\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).}\\\\n\\\\\\\\end{table}\\\\n\\\\n\\\\\\\\paragraph{Architecture generalization.}\\\\nTable~\\\\\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\\\nAll models reach Tier~3 consensus ($K{\\\\\\\\geq}4/5$) with 6/8 canary$\\\\\\\\to$diversity pairs confirmed.\\\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\\\n\\\\nMethod-level variation across architectures is informative.\\\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\\\\\geq}4/5$.\\\\n\\\\n\\\\\\\\paragraph{Scale generalization.}\\\\nScaling from 410M to 1.4B parameters (3.4$\\\\\\\\times$) preserves majority consensus ($K{\\\\\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\\\nOf the three non-consensus pairs, two target perplexity (token\\\\\\\\_entropy$\\\\\\\\to$perplexity, $K{=}1$; ECE$\\\\\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\\\\\S\\\\\\\\ref{sec:method_sensitivity}).\\\\nThe sole scale-specific miss is token\\\\\\\\_entropy$\\\\\\\\to$distinct\\\\\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\\\\\S\\\\\\\\ref{sec:consensus_validation}).\\\\nThe consensus framework absorbs this single-method failure by design.\\\\n\\\\n\\\\\\\\paragraph{Domain generalization.}\\\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\\\n\\\\nTable~\\\\\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\\\\\alpha{=}1.0$.\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.12}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\\nAll conditions use $\\\\alpha{=}1.0$ and a single seed.\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\\\to$downstream pairs reaching significance. Significance at permutation $p{<}0.05$; cross-method consensus ($K{\\\\geq}4/5$) serves as multiplicity control (see Appendix~\\\\ref{sec:fdr_sensitivity} for sensitivity analysis). 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded).}\\n\\\\label{tab:generalization}\\n\\\\begin{tabular}{llccccccc}\\n\\\\toprule\\nVariation & Model / Dataset & \\\\rotatebox{70}{Naive} & \\\\rotatebox{70}{Diff.\\\\ XCorr} & \\\\rotatebox{70}{Threshold} & \\\\rotatebox{70}{PermG (fwd)} & \\\\rotatebox{70}{PermG (rev)} & \\\\rotatebox{70}{TY} & \\\\rotatebox{70}{$K{\\\\geq}4/5$} \\\\\\\\\\n\\\\midrule\\nBaseline      & Pythia-410M / Wiki    & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 \\\\\\\\\\nArchitecture  & GPT-2-medium / Wiki   & -- & -- & -- & -- & -- & -- & \\\\textit{pending} \\\\\\\\\\nArchitecture  & OPT-1.3B / Wiki       & 8/8 & 8/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 \\\\\\\\\\nScale ($3.4\\\\times$) & Pythia-1.4B / Wiki    & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 \\\\\\\\\\nDomain        & Pythia-1B / C4        & 8/8 & 8/8 & 6/8 & 8/8 & 4/8 & 4/8 & 7/8$^\\\\dagger$ \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\vspace{2pt}\\n{\\\\footnotesize $^\\\\dagger$C4 domain (s42): token\\\\_entropy pairs maintain strict unidirectionality (rev=0/4); ECE pairs show reverse significance (rev=4/4). The single non-consensus pair (token\\\\_entropy$\\\\to$mauve) reaches only 3/5 methods.\\\\\\\\\\nPG rev counts reflect marginal ECE$\\\\rightarrow$diversity reverse significance ($p\\\\approx 0.03$); token\\\\_entropy pairs maintain 0/4 reverse across all conditions.\\\\\\\\\\nCanary$\\\\to$perplexity pairs do not reach $K{\\\\geq}4$ in any condition; these are shared-trend artifacts eliminated by first-differencing (\\\\S\\\\ref{sec:method_sensitivity}).}\\n\\\\end{table}\\n\\n\\\\paragraph{Architecture generalization.}\\nTable~\\\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\\nAll models reach Tier~3 consensus ($K{\\\\geq}4/5$) with 6/8 canary$\\\\to$diversity pairs confirmed.\\nToken entropy maintains perfect unidirectional precedence across architectures (reverse 0/4 in each), while ECE exhibits marginal reverse leakage to diversity metrics in some conditions ($p\\\\approx 0.03$, non-significant after FDR), consistent with calibration-diversity feedback rather than true reverse causation.\\n\\nMethod-level variation across architectures is informative.\\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\\\to$1 discontinuity that cleanly exceeds the onset threshold.\\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\\\S\\\\ref{sec:consensus_validation}).\\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\\\geq}4/5$.\\n\\n\\\\paragraph{Scale generalization.}\\nScaling from 410M to 1.4B parameters (3.4$\\\\times$) preserves majority consensus ($K{\\\\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.\\nOf the three non-consensus pairs, two target perplexity (token\\\\_entropy$\\\\to$perplexity, $K{=}1$; ECE$\\\\to$perplexity, $K{=}2$), a channel that also fails to reach $K{\\\\geq}4$ in the 410M Baseline due to the shared-trend artifact identified by the first-differencing diagnostic (\\\\S\\\\ref{sec:method_sensitivity}).\\nThe sole scale-specific miss is token\\\\_entropy$\\\\to$distinct\\\\_3 ($K{=}3/5$), where permutation Granger forward significance falls just short of threshold ($p{=}0.053$); excluding perplexity pairs, Scale consensus reaches 5/6.\\nThreshold onset detection achieves 8/8 at this scale, and permutation Granger reverse significance is 0/8 (the only condition without ECE reverse leakage, likely because the larger model's reduced variance suppresses borderline reverse signals).\\nToda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration order estimates become unstable across conditions (token\\\\_entropy shifts from $I(0)$ to $I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom renders the procedure uninformative (\\\\S\\\\ref{sec:consensus_validation}).\\nThe consensus framework absorbs this single-method failure by design.\\n\\n\\\\paragraph{Domain generalization.}\\nReplacing WikiText-103 with C4 tests whether the lead-lag pattern depends on the training data distribution.\\nWe exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6$\\\\to$1682.6, ADF statistic $+1.07$) violates the stationarity assumption required by VAR-based Granger analysis.\\nInstead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\\n\\nTable~\\\\ref{tab:generalization} shows that Pythia-1B on C4 achieves 7/8 consensus at $K{\\\\geq}4/5$, exceeding the Tier~3 threshold established by the WikiText baseline (6/8).\\nPermutation Granger forward detection reaches 8/8, the strongest single-method score across all generalization conditions.\\nECE reverse leakage appears in 3 of 4 verified conditions: C4 domain (4/4 ECE pairs), WikiText baseline (3/4), and OPT-1.3B (2/4), while only the 1.4B scale condition shows no reverse leakage (0/4). This pattern reflects an inherent marginal property of ECE rather than a domain-specific phenomenon.\\nTogether with the architecture results, this establishes four independent validation lines (three architectures, one domain) converging on the same conclusion: token entropy Granger-precedes diversity collapse at $\\\\alpha{=}1.0$.\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"
    }
  }
}
```

</details>

---
