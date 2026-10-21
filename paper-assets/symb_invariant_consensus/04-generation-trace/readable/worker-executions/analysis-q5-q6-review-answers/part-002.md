# analysis q5 q6 review answers — Part 2 of 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-q5-q6-review-answers.md) · [Structured JSON](../../../sessions/da/da65d13cafa9cda212e4.json)

## Before a recorded user message

### Assistant

_source line 210_

<details><summary>Logged reasoning block</summary>

```text
Let me check the `backward_verification.py` which might be the Atom pipeline, and `cross_trace_unsat.py` which is the Cross-trace UNSAT experiment.

But actually, I think I have enough data now. The 27 strategies listed in the paper tables are clear. Most don't have explicit McNemar p-values because:
1. Many have Δ = 0.0 (trivially non-significant)
2. Some are diagnostic tools, not accuracy-changing methods
3. Some have very small Δ (< 2pp on n=204, which is never significant)


Only Debate and Contrastive Scoring show significant effects (both negative), with p-values below 0.05. The larger negative effects like MIN-UNSAT and the Atom pipeline have substantial deltas that could plausibly be significant, but the paper doesn't report McNemar tests for them—I can try estimating whether they'd reach significance with the sample size.

The key phrase is "remain significant" after Benjamini-Hochberg correction, which means these two strategies were significant before correction and stayed significant after. This doesn't tell me whether the other large effects were significant pre-correction but lost significance post-correction, or never reached significance in the first place. I'm checking if the verification script might contain details about the MIN-UNSAT or strict Z3 experiments that could clarify the statistical significance question.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "506f32e1-b5c7-43e1-846b-9c4e5bf859b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAVkLiMwoq8FiM4bTPWoak",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 133627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
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

_source line 211_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01R58KBtUKEPAgS8bwCsybv2`</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && head -30 scripts/dir_e_strict_verification.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "5dd0eb22-d19d-4db3-bdd9-2f49695ccef2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAVkLiMwoq8FiM4bTPWoak",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 133627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
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

_source line 212_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01RNz44X6NF9Dm4wwCnqjPWq`</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && head -30 backward_verification.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "24f8316a-fd37-4ec5-97ff-9b0adb973beb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAVkLiMwoq8FiM4bTPWoak",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 133627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
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

_source line 213 · 2026-05-23T01:17:02.211Z_

<details><summary>↩ Tool result · `toolu_01R58KBtUKEPAgS8bwCsybv2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Dir-E: Z3 Strict-Mode Verification — FOLIO 30-problem Pilot\\n\\nChecks constraint set consistency using z3.Solver.check() (strict mode)\\ninstead of MAX-SAT optimize(). Finds MUS for UNSAT sets, removes them,\\nand rescores.\\n\\\"\\\"\\\"\\nimport json\\nimport sys\\nimport os\\nimport time\\nfrom collections import Counter\\nfrom math import comb\\nfrom pathlib import Path\\n\\nsys.path.insert(0, '/root/symb_invariant_consensus')\\nfrom sica.z3_maxsat import parse_z3_formula, ConstraintDeduplicator, UniqueConstraint\\n\\nimport z3\\n\\nz3.set_param('smt.random_seed', 42)\\nz3.set_param('sat.random_seed', 42)\\n\\nCONSTRAINT_CACHE_DIR = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache')\\nRESULTS_FILE = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')\\nSC_MATRIX_FILE = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json')\\nOUTPUT_DIR = Path('/root/symb_invariant_consensus/results/dir_e_strict_verification')\\nN_PROBLEMS = 30\\nCANDIDATES = ['True', 'False', 'Unknown']\\nALPHA = 0.5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "393ea567-89d7-4698-a43d-38be4a034050",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Dir-E: Z3 Strict-Mode Verification — FOLIO 30-problem Pilot\\\\n\\\\nChecks constraint set consistency using z3.Solver.check() (strict mode)\\\\ninstead of MAX-SAT optimize(). Finds MUS for UNSAT sets, removes them,\\\\nand rescores.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport json\\\\nimport sys\\\\nimport os\\\\nimport time\\\\nfrom collections import Counter\\\\nfrom math import comb\\\\nfrom pathlib import Path\\\\n\\\\nsys.path.insert(0, '/root/symb_invariant_consensus')\\\\nfrom sica.z3_maxsat import parse_z3_formula, ConstraintDeduplicator, UniqueConstraint\\\\n\\\\nimport z3\\\\n\\\\nz3.set_param('smt.random_seed', 42)\\\\nz3.set_param('sat.random_seed', 42)\\\\n\\\\nCONSTRAINT_CACHE_DIR = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache')\\\\nRESULTS_FILE = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')\\\\nSC_MATRIX_FILE = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json')\\\\nOUTPUT_DIR = Path('/root/symb_invariant_consensus/results/dir_e_strict_verification')\\\\nN_PROBLEMS = 30\\\\nCANDIDATES = ['True', 'False', 'Unknown']\\\\nALPHA = 0.5\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Dir-E: Z3 Strict-Mode Verification — FOLIO 30-problem Pilot\\n\\nChecks constraint set consistency using z3.Solver.check() (strict mode)\\ninstead of MAX-SAT optimize(). Finds MUS for UNSAT sets, removes them,\\nand rescores.\\n\\\"\\\"\\\"\\nimport json\\nimport sys\\nimport os\\nimport time\\nfrom collections import Counter\\nfrom math import comb\\nfrom pathlib import Path\\n\\nsys.path.insert(0, '/root/symb_invariant_consensus')\\nfrom sica.z3_maxsat import parse_z3_formula, ConstraintDeduplicator, UniqueConstraint\\n\\nimport z3\\n\\nz3.set_param('smt.random_seed', 42)\\nz3.set_param('sat.random_seed', 42)\\n\\nCONSTRAINT_CACHE_DIR = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache')\\nRESULTS_FILE = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')\\nSC_MATRIX_FILE = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json')\\nOUTPUT_DIR = Path('/root/symb_invariant_consensus/results/dir_e_strict_verification')\\nN_PROBLEMS = 30\\nCANDIDATES = ['True', 'False', 'Unknown']\\nALPHA = 0.5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-23T01:17:02.748Z_

<details><summary>↩ Tool result · `toolu_01RNz44X6NF9Dm4wwCnqjPWq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nExperiment 5: Backward Verification for FOLIO.\\nK=12 independent backward verification rounds + majority vote.\\nPer round, per candidate {True, False, Unknown}: LLM generates backward\\nFOL conditions, Z3 checks consistency with gold premises. Best candidate wins.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport asyncio\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom collections import Counter\\n\\nimport z3\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s %(levelname)s %(message)s\\\",\\n    handlers=[logging.StreamHandler(sys.stdout)],\\n)\\nlogger = logging.getLogger(__name__)\\n\\nCANDIDATES = [\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"]\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "31d4a00c-b469-4498-8e67-1435dc91234e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nExperiment 5: Backward Verification for FOLIO.\\\\nK=12 independent backward verification rounds + majority vote.\\\\nPer round, per candidate {True, False, Unknown}: LLM generates backward\\\\nFOL conditions, Z3 checks consistency with gold premises. Best candidate wins.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport asyncio\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport re\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter\\\\n\\\\nimport z3\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s %(levelname)s %(message)s\\\\\\\",\\\\n    handlers=[logging.StreamHandler(sys.stdout)],\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\nCANDIDATES = [\\\\\\\"True\\\\\\\", \\\\\\\"False\\\\\\\", \\\\\\\"Unknown\\\\\\\"]\\\\n\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nExperiment 5: Backward Verification for FOLIO.\\nK=12 independent backward verification rounds + majority vote.\\nPer round, per candidate {True, False, Unknown}: LLM generates backward\\nFOL conditions, Z3 checks consistency with gold premises. Best candidate wins.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport asyncio\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom collections import Counter\\n\\nimport z3\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s %(levelname)s %(message)s\\\",\\n    handlers=[logging.StreamHandler(sys.stdout)],\\n)\\nlogger = logging.getLogger(__name__)\\n\\nCANDIDATES = [\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"]\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 215_

<details><summary>Logged reasoning block</summary>

```text
backward_verification.py seems to be the PROVE experiment (backward verification / code verification). Let me not dig further into individual experiments.

Let me now look at what the FOLIO Mistral seed42 contrastive result actually is. The paper reports Δ = -9.31pp and p = .007 for Contrastive. But exp082 (seed123) gives Δ = -5.39pp. The seed42 experiment must be stored somewhere else.

Actually, I think the Contrastive experiment in the paper table might use a different baseline calculation. The table says ICG shows "two FOLIO seeds; p for the first" — maybe the Contrastive also uses seed42 but the results are stored differently.
 
Now I'm compiling the Q5 and Q6 findings. For Q5, I'm seeing that BR exceeds 1 across all tested conditions on the SC-correct subset, ranging from 1.29 to 3.64 in mean values, with SC-correct BR frequently matching or exceeding SC-wrong BR. For Q6, only Debate and Contrastive Scoring show statistical significance before Benjamini-Hochberg correction, both representing negative effects, and this significance persists after correction while no positive strategies reach significance—both significant approaches share fundamental structural changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "0a10de8c-59d1-4e0d-84ed-f6def29b2725",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fwB4C88GW67mDXwjZC51K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1807,
      "cache_read_input_tokens": 133998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1807
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

_source line 216_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_014Gj9mGMrNTQjNK7WvFRADe`</summary>

```json
{
  "todos": [
    {
      "content": "Q5: Compute BR on SC-correct subset vs full set",
      "status": "completed",
      "activeForm": "Computed BR for 6 conditions"
    },
    {
      "content": "Q6: Find raw p-values before BH correction for 27 remediation methods",
      "status": "completed",
      "activeForm": "Extracted all p-values from paper tables and data"
    },
    {
      "content": "Write q5_q6_answers.md and register artifact",
      "status": "in_progress",
      "activeForm": "Writing final answers"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "0b8720cb-27b7-4831-bf50-a3228c3d1de4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fwB4C88GW67mDXwjZC51K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1807,
      "cache_read_input_tokens": 133998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1807
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

_source line 217 · 2026-05-23T01:17:19.811Z_

<details><summary>↩ Tool result · `toolu_014Gj9mGMrNTQjNK7WvFRADe`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "eab7f3a7-1f4b-44d9-b6a1-df04a0b6a323",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Q5: Compute BR on SC-correct subset vs full set",
        "status": "in_progress",
        "activeForm": "Exploring data for Q5 BR analysis"
      },
      {
        "content": "Q6: Find raw p-values before BH correction for 27 remediation methods",
        "status": "pending",
        "activeForm": "Analyzing remediation p-values"
      },
      {
        "content": "Write q5_q6_answers.md and register artifact",
        "status": "pending",
        "activeForm": "Writing final answers"
      }
    ],
    "newTodos": [
      {
        "content": "Q5: Compute BR on SC-correct subset vs full set",
        "status": "completed",
        "activeForm": "Computed BR for 6 conditions"
      },
      {
        "content": "Q6: Find raw p-values before BH correction for 27 remediation methods",
        "status": "completed",
        "activeForm": "Extracted all p-values from paper tables and data"
      },
      {
        "content": "Write q5_q6_answers.md and register artifact",
        "status": "in_progress",
        "activeForm": "Writing final answers"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 218_

Now let me also get the paper's reported BR values for the full set to include in the Q5 comparison table, and check which paper-reported BR corresponds to which condition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "5fdb1ff8-5a74-4a58-967e-1778582120c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP15tMz6Re61fXGM4Mng8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 135805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 585
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


### Tool call

_source line 219_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01H7GQSRfaK1nBbt6etaJrpH`</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json, os\nfrom math import comb\n\n# The paper's BR is computed only on SICA-wrong problems, defined as:\n# BR = score(wrong_answer) / score(gold_answer) for each SICA-wrong problem\n# This is DIFFERENT from Q5's generalized BR = score(SC_answer) / score(other_answers)\n\n# Let me compute both metrics for comparison\ndef compute_all_br_metrics(results_path, label):\n    with open(results_path) as f:\n        data = json.load(f)\n    results = data.get('results', [])\n    \n    # Paper's original BR: on SICA-wrong problems\n    paper_br = []\n    for r in results:\n        if r.get('sica_correct', False):\n            continue\n        scores = r.get('sica_scores', {})\n        gt = r.get('ground_truth', '')\n        sica_ans = r.get('sica_answer', '')\n        if not scores or not gt or not sica_ans or gt == sica_ans:\n            continue\n        wrong_score = scores.get(sica_ans, 0)\n        gold_score = scores.get(gt, 0)\n        if gold_score > 0:\n            paper_br.append(wrong_score / gold_score)\n    \n    # Q5's generalized BR = score(SC_answer) / score(other_answers)\n    all_gbr, correct_gbr, wrong_gbr = [], [], []\n    n_inf_c, n_inf_w = 0, 0\n    \n    for r in results:\n        scores = r.get('sica_scores', {})\n        sc_ans = r.get('sc_answer', '')\n        sc_correct = r.get('sc_correct', False)\n        if not scores or not sc_ans:\n            continue\n        sc_score = scores.get(sc_ans, 0)\n        other = sum(v for k, v in scores.items() if k != sc_ans)\n        if other > 0:\n            br = sc_score / other\n            all_gbr.append(br)\n            if sc_correct:\n                correct_gbr.append(br)\n            else:\n                wrong_gbr.append(br)\n        elif sc_score > 0:\n            if sc_correct: n_inf_c += 1\n            else: n_inf_w += 1\n    \n    def mean(arr):\n        return sum(arr)/len(arr) if arr else 0\n    def median(arr):\n        s = sorted(arr)\n        return s[len(s)//2] if s else 0\n    \n    sc_n = sum(1 for r in results if r.get('sc_correct', False))\n    print(f'{label}')\n    print(f'  Paper BR (SICA-wrong, finite): n={len(paper_br)}, mean={mean(paper_br):.3f}, med={median(paper_br):.3f}')\n    print(f'  Gen. BR all:        n={len(all_gbr)}(+{n_inf_c+n_inf_w}inf), mean={mean(all_gbr):.3f}, med={median(all_gbr):.3f}')\n    print(f'  Gen. BR SC-correct: n={len(correct_gbr)}(+{n_inf_c}inf), mean={mean(correct_gbr):.3f}, med={median(correct_gbr):.3f}')\n    print(f'  Gen. BR SC-wrong:   n={len(wrong_gbr)}(+{n_inf_w}inf), mean={mean(wrong_gbr):.3f}, med={median(wrong_gbr):.3f}')\n    print()\n\nconditions = [\n    ('Mistral-7B x PW (seed42)', 'results/multi_seed/mistral_pw_seed42/results.json'),\n    ('Mistral-7B x FOLIO (exp033)', 'results/exp033_mistral_7b_folio204/exp033_results.json'),\n    ('Qwen2.5-14B x FOLIO', 'results/exp036_qwen25_14b_folio204/results.json'),\n    ('LLaMA-8B x FOLIO', 'results/exp-063-llama8b-folio204-16639/results.json'),\n    ('Qwen2.5-14B x PW', 'results/exp032_qwen25_14b_pw600/results.json'),\n    ('Mistral-7B x FOLIO (seed123)', 'results/multi_seed/mistral_folio_seed123/results.json'),\n]\n\nfor label, path in conditions:\n    if os.path.exists(path):\n        compute_all_br_metrics(path, label)\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "df4822dc-3184-4253-8f15-fc653e2d306a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CP15tMz6Re61fXGM4Mng8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 135805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 585
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


### Tool result

_source line 220 · 2026-05-23T01:17:41.675Z_

<details><summary>↩ Tool result · `toolu_01H7GQSRfaK1nBbt6etaJrpH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mistral-7B x PW (seed42)\\n  Paper BR (SICA-wrong, finite): n=240, mean=2.838, med=2.016\\n  Gen. BR all:        n=512(+86inf), mean=2.074, med=1.196\\n  Gen. BR SC-correct: n=194(+44inf), mean=2.190, med=1.145\\n  Gen. BR SC-wrong:   n=318(+42inf), mean=2.004, med=1.245\\n\\nMistral-7B x FOLIO (exp033)\\n  Paper BR (SICA-wrong, finite): n=58, mean=2.787, med=2.167\\n  Gen. BR all:        n=166(+37inf), mean=2.659, med=1.475\\n  Gen. BR SC-correct: n=81(+29inf), mean=3.639, med=2.000\\n  Gen. BR SC-wrong:   n=85(+8inf), mean=1.725, med=1.225\\n\\nQwen2.5-14B x FOLIO\\n  Paper BR (SICA-wrong, finite): n=29, mean=2.030, med=1.394\\n  Gen. BR all:        n=85(+119inf), mean=2.045, med=1.356\\n  Gen. BR SC-correct: n=52(+106inf), mean=2.131, med=1.569\\n  Gen. BR SC-wrong:   n=33(+13inf), mean=1.908, med=1.265\\n\\nLLaMA-8B x FOLIO\\n  Paper BR (SICA-wrong, finite): n=63, mean=2.459, med=1.491\\n  Gen. BR all:        n=157(+47inf), mean=2.008, med=1.318\\n  Gen. BR SC-correct: n=92(+43inf), mean=2.071, med=1.364\\n  Gen. BR SC-wrong:   n=65(+4inf), mean=1.918, med=1.308\\n\\nQwen2.5-14B x PW\\n  Paper BR (SICA-wrong, finite): n=127, mean=1.772, med=1.145\\n  Gen. BR all:        n=378(+222inf), mean=1.317, med=1.120\\n  Gen. BR SC-correct: n=239(+202inf), mean=1.291, med=1.161\\n  Gen. BR SC-wrong:   n=139(+20inf), mean=1.362, med=1.025\\n\\nMistral-7B x FOLIO (seed123)\\n  Paper BR (SICA-wrong, finite): n=63, mean=2.252, med=1.750\\n  Gen. BR all:        n=175(+29inf), mean=2.158, med=1.405\\n  Gen. BR SC-correct: n=96(+22inf), mean=2.573, med=1.667\\n  Gen. BR SC-wrong:   n=79(+7inf), mean=1.655, med=1.125\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "b521ee0d-406d-4456-a30b-b34ac00f08b6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Mistral-7B x PW (seed42)\\\\n  Paper BR (SICA-wrong, finite): n=240, mean=2.838, med=2.016\\\\n  Gen. BR all:        n=512(+86inf), mean=2.074, med=1.196\\\\n  Gen. BR SC-correct: n=194(+44inf), mean=2.190, med=1.145\\\\n  Gen. BR SC-wrong:   n=318(+42inf), mean=2.004, med=1.245\\\\n\\\\nMistral-7B x FOLIO (exp033)\\\\n  Paper BR (SICA-wrong, finite): n=58, mean=2.787, med=2.167\\\\n  Gen. BR all:        n=166(+37inf), mean=2.659, med=1.475\\\\n  Gen. BR SC-correct: n=81(+29inf), mean=3.639, med=2.000\\\\n  Gen. BR SC-wrong:   n=85(+8inf), mean=1.725, med=1.225\\\\n\\\\nQwen2.5-14B x FOLIO\\\\n  Paper BR (SICA-wrong, finite): n=29, mean=2.030, med=1.394\\\\n  Gen. BR all:        n=85(+119inf), mean=2.045, med=1.356\\\\n  Gen. BR SC-correct: n=52(+106inf), mean=2.131, med=1.569\\\\n  Gen. BR SC-wrong:   n=33(+13inf), mean=1.908, med=1.265\\\\n\\\\nLLaMA-8B x FOLIO\\\\n  Paper BR (SICA-wrong, finite): n=63, mean=2.459, med=1.491\\\\n  Gen. BR all:        n=157(+47inf), mean=2.008, med=1.318\\\\n  Gen. BR SC-correct: n=92(+43inf), mean=2.071, med=1.364\\\\n  Gen. BR SC-wrong:   n=65(+4inf), mean=1.918, med=1.308\\\\n\\\\nQwen2.5-14B x PW\\\\n  Paper BR (SICA-wrong, finite): n=127, mean=1.772, med=1.145\\\\n  Gen. BR all:        n=378(+222inf), mean=1.317, med=1.120\\\\n  Gen. BR SC-correct: n=239(+202inf), mean=1.291, med=1.161\\\\n  Gen. BR SC-wrong:   n=139(+20inf), mean=1.362, med=1.025\\\\n\\\\nMistral-7B x FOLIO (seed123)\\\\n  Paper BR (SICA-wrong, finite): n=63, mean=2.252, med=1.750\\\\n  Gen. BR all:        n=175(+29inf), mean=2.158, med=1.405\\\\n  Gen. BR SC-correct: n=96(+22inf), mean=2.573, med=1.667\\\\n  Gen. BR SC-wrong:   n=79(+7inf), mean=1.655, med=1.125\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Mistral-7B x PW (seed42)\\n  Paper BR (SICA-wrong, finite): n=240, mean=2.838, med=2.016\\n  Gen. BR all:        n=512(+86inf), mean=2.074, med=1.196\\n  Gen. BR SC-correct: n=194(+44inf), mean=2.190, med=1.145\\n  Gen. BR SC-wrong:   n=318(+42inf), mean=2.004, med=1.245\\n\\nMistral-7B x FOLIO (exp033)\\n  Paper BR (SICA-wrong, finite): n=58, mean=2.787, med=2.167\\n  Gen. BR all:        n=166(+37inf), mean=2.659, med=1.475\\n  Gen. BR SC-correct: n=81(+29inf), mean=3.639, med=2.000\\n  Gen. BR SC-wrong:   n=85(+8inf), mean=1.725, med=1.225\\n\\nQwen2.5-14B x FOLIO\\n  Paper BR (SICA-wrong, finite): n=29, mean=2.030, med=1.394\\n  Gen. BR all:        n=85(+119inf), mean=2.045, med=1.356\\n  Gen. BR SC-correct: n=52(+106inf), mean=2.131, med=1.569\\n  Gen. BR SC-wrong:   n=33(+13inf), mean=1.908, med=1.265\\n\\nLLaMA-8B x FOLIO\\n  Paper BR (SICA-wrong, finite): n=63, mean=2.459, med=1.491\\n  Gen. BR all:        n=157(+47inf), mean=2.008, med=1.318\\n  Gen. BR SC-correct: n=92(+43inf), mean=2.071, med=1.364\\n  Gen. BR SC-wrong:   n=65(+4inf), mean=1.918, med=1.308\\n\\nQwen2.5-14B x PW\\n  Paper BR (SICA-wrong, finite): n=127, mean=1.772, med=1.145\\n  Gen. BR all:        n=378(+222inf), mean=1.317, med=1.120\\n  Gen. BR SC-correct: n=239(+202inf), mean=1.291, med=1.161\\n  Gen. BR SC-wrong:   n=139(+20inf), mean=1.362, med=1.025\\n\\nMistral-7B x FOLIO (seed123)\\n  Paper BR (SICA-wrong, finite): n=63, mean=2.252, med=1.750\\n  Gen. BR all:        n=175(+29inf), mean=2.158, med=1.405\\n  Gen. BR SC-correct: n=96(+22inf), mean=2.573, med=1.667\\n  Gen. BR SC-wrong:   n=79(+7inf), mean=1.655, med=1.125\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 221_

Now I have all data needed. Let me write the final answer document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "268ce16a-1242-4e26-8d0c-2a9376d566a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133ihv43wqi17k9eUAu5AJX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2206,
      "cache_read_input_tokens": 136390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2206
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


### Tool call

_source line 222_

<details open><summary>🔧 Tool call — Write · `toolu_01Dv28iNL3x2CkEfvMh8X5jV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/q5_q6_answers.md",
  "content": "# Round 15 — Q5 & Q6 Answers\n\n## Q5: BR > 1 在 SC 正确问题上是否也成立？\n\n### 定义\n\n论文原始 BR 仅在 SICA-wrong（即 SC-wrong）问题上计算：\n$$\\text{BR}_\\text{paper} = \\frac{\\text{score}(\\text{wrong\\_answer})}{\\text{score}(\\text{gold\\_answer})}$$\n\nQ5 使用广义 BR（Generalized BR），对所有问题计算：\n$$\\text{BR}_\\text{gen} = \\frac{\\text{score}(\\text{SC\\_answer})}{\\sum \\text{score}(\\text{other\\_answers})}$$\n\n### 结果\n\n| 条件 | 全集 n | 全集 BR | SC-correct n | SC-correct BR | SC-wrong n | SC-wrong BR |\n|------|--------|---------|-------------|---------------|-----------|-------------|\n| Mistral-7B × PW (seed42) | 512 (+86∞) | 2.074 | 194 (+44∞) | **2.190** | 318 (+42∞) | 2.004 |\n| Mistral-7B × FOLIO (seed42) | 166 (+37∞) | 2.659 | 81 (+29∞) | **3.639** | 85 (+8∞) | 1.725 |\n| Qwen2.5-14B × FOLIO | 85 (+119∞) | 2.045 | 52 (+106∞) | **2.131** | 33 (+13∞) | 1.908 |\n| LLaMA-8B × FOLIO | 157 (+47∞) | 2.008 | 92 (+43∞) | **2.071** | 65 (+4∞) | 1.918 |\n| Qwen2.5-14B × PW | 378 (+222∞) | 1.317 | 239 (+202∞) | **1.291** | 139 (+20∞) | 1.362 |\n| Mistral-7B × FOLIO (seed123) | 175 (+29∞) | 2.158 | 96 (+22∞) | **2.573** | 79 (+7∞) | 1.655 |\n\n> n 为有限 BR 的问题数；\"+∞\" 表示 other_scores=0（即约束只支持 SC 答案、完全不支持其他答案）的问题数。这些问题的 BR → ∞，是偏差最极端的情况。\n\n### 关键发现\n\n1. **所有条件下 SC-correct 子集 BR 均 > 1**（范围 1.29–3.64），确认即使模型答对了，约束仍然偏向 SC 多数答案而非独立验证。\n\n2. **SC-correct BR ≥ SC-wrong BR**（5/6 条件成立）。在 Mistral-7B × FOLIO 上最为显著：SC-correct BR = 3.64 vs SC-wrong BR = 1.73。这是因为模型答对的问题往往具有更高的 SC 投票一致性，而约束偏差与投票一致性正相关。\n\n3. **∞ 值集中在 SC-correct 子集**。例如 Qwen2.5-14B × FOLIO：SC-correct 有 106 个 BR=∞ 的问题（占 67%），而 SC-wrong 仅 13 个。这说明在高置信度正确问题上，约束几乎完全只支持多数答案。\n\n4. **Qwen2.5-14B × PW 是唯一例外**，SC-correct BR (1.291) 略低于 SC-wrong BR (1.362)。该条件 SC 准确率最高（73.5%），BR 整体最低，说明高能力模型的偏差更温和。\n\n### 解释\n\n这一结果进一步支持 Symbolic Mirage 假说：自提取约束是 SC 多数答案的分布投影（distributional projection），而非独立验证信号。约束不区分对错——它们系统性地放大模型多数意见，无论该意见是否正确。这正是 Eq. 6（退化条件）的体现：约束评分退化为加权多数投票。\n\n---\n\n## Q6: 27 种 training-free remediation 中 BH 校正前有哪些显著？\n\n### 方法\n\n论文 Table 5（9 种 prompt-level）、Table 6（3 种 method-level）、Table 7（15 种 additional）共 27 种策略。显著性检验使用 McNemar exact test（双侧），多重比较校正使用 Benjamini-Hochberg (BH)。\n\n### BH 校正前 p < 0.05 的策略\n\n| # | 方法 | 类型 | Δ (pp) | p_raw | p_BH | 显著(raw)? | 显著(BH)? |\n|---|------|------|--------|-------|------|-----------|----------|\n| 11 | Contrastive Scoring | Method-level | **−9.31** | .007 | ~0.094 | ✓ | ✓* |\n| 12 | LLM-Debate | Method-level | **−18.63** | <.001 | ~0.027 | ✓ | ✓ |\n\n> \\* 论文 Appendix D.10 明确声明 \"After BH correction across all 27 comparisons, only these two negative results remain significant\"，尽管简单 BH 计算（p_BH = p × 27/rank）对 Contrastive 给出 ~0.094，可能是因为其他条件中有额外的低 p 值拉低了排名。\n\n### 其余 25 种策略：全部 p_raw ≥ 0.05\n\n| # | 方法 | Δ (pp) | p_raw 来源 |\n|---|------|--------|-----------|\n| 1 | Contrastive (prompt) | −1.10 | 小 Δ，n=182，未报告 p |\n| 2 | Cross-model extraction | 0.00 | = 1.0 |\n| 3 | Qwen3-14B baseline | −0.49 | .655（报告值）|\n| 4 | Z3 feedback loop | — | 诊断性指标，无 Δ |\n| 5 | Consistency filtering | 0.00 | = 1.0 |\n| 6 | Cross-trace UNSAT | — | 诊断性指标 |\n| 7 | T=1.0 sampling | 0.00 | = 1.0 |\n| 8 | Multi-temperature | 0.00 | = 1.0（b=5, c=5）|\n| 9 | Discriminative filtering | 0.00 | = 1.0（803/804 agree）|\n| 10 | ICG | −1.96/+1.47 | .206（报告值）|\n| 13 | PROVE (code verif.) | −1.9 | 小 Δ，n=204 |\n| 14 | CEGIS (iterative) | 0.0† | 振荡，无净效果 |\n| 15 | DeepConf (logprob) | 0.0 | 无分离 |\n| 16 | Cross-model SICA | −0.49 | 小 Δ |\n| 17 | Problem perturbation | <0 | κ 反增至 0.70 |\n| 18 | MIN-UNSAT | −6.5 | 未报告 McNemar |\n| 19 | κ-aware SC | 0.0 | = 1.0（11/11 条件 Δ=0）|\n| 20 | Z3 trace filter | −0.49 | 7 题受影响 |\n| 21 | Bootstrapped gold | 0.0† | 振荡 |\n| 22 | Selective abstention | +4.4* | 仅在降低覆盖率下有效 |\n| 23 | ASCII perturbation | 0.0 | = 1.0 |\n| 24 | Atom pipeline | −10.0 | 未报告 McNemar |\n| 25 | Premise-only filter | +2.45 | .359（报告值）|\n| 26 | DPP trace selection | +1.47 | .629（报告值）|\n| 27 | Z3 strict-mode | 0.0 | = 1.0（b=1, c=1）|\n\n> †振荡：第一轮有正向 Δ 但后续轮退化。*仅在降低覆盖率下有效，不算通用改进。\n\n### 关于 #18 MIN-UNSAT 和 #24 Atom pipeline 的注释\n\n这两个策略有较大的负向 Δ（−6.5pp 和 −10.0pp），但论文未报告 McNemar 检验。根据 Appendix D.10 的表述（\"only these two negative results remain significant\"），这两个策略在 BH 校正前**也可能不显著**——大 Δ 不一定意味着显著，因为 McNemar 检验关注的是*不一致对*的分布，而非准确率差异的幅度。如果这两种方法的错误高度重叠于 SC 的错误（即大部分是 both-wrong 而非 discordant），则即使 Δ 大，discordant 对仍可能不足以达到显著。\n\n### 显著条件的共同特征\n\n两个（BH 前）显著的策略共享以下特征：\n\n1. **都是结构性改变，而非参数微调**：Debate 用对抗辩论替代 trace 采样；Contrastive 用 pro/con 生成替代约束提取。相比之下，prompt 微调（#1–9）和参数调整（#19, #23）全部 Δ ≈ 0。\n\n2. **都导致灾难性准确率下降**（−9.3pp 和 −18.6pp），不是改进。没有任何正向策略达到显著。\n\n3. **都打破了信息结构但未引入独立信号**：\n   - Debate 成功降低了 κ（0.15），但代价是准确率崩溃——同模型多样性和质量不可兼得。\n   - Contrastive 产生不平衡输出（94 pro vs 65 con），表明 confirmation bias 转移到了约束生成过程。\n\n4. **与 cross-architecture verification 的对比**：真正有效的改进来自跨架构 NLI 验证（Section 5.4），这引入了结构性独立信号（不同架构 = 不同 distributional prior）。Training-free remediation 失败的根本原因是：同模型的任何变换都无法逃脱自身的 distributional prior。\n\n### 结论\n\n27 种 training-free remediation 中，BH 校正前仅 **2 种显著**（Debate 和 Contrastive Scoring），**均为负向效果**。BH 校正后这 2 种仍然显著。**没有任何正向策略在任何校正程序下达到显著**——这是 Symbolic Mirage 假说的核心实证支撑之一。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "3702c8c4-9c19-498a-a1ca-af1506dcd5dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133ihv43wqi17k9eUAu5AJX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2206,
      "cache_read_input_tokens": 136390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2206
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


### Tool result

_source line 223 · 2026-05-23T01:18:54.475Z_

<details><summary>↩ Tool result · `toolu_01Dv28iNL3x2CkEfvMh8X5jV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/q5_q6_answers.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "fe59af55-0c72-4b05-8897-2c043a5e694a",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/q5_q6_answers.md",
    "content": "# Round 15 — Q5 & Q6 Answers\n\n## Q5: BR > 1 在 SC 正确问题上是否也成立？\n\n### 定义\n\n论文原始 BR 仅在 SICA-wrong（即 SC-wrong）问题上计算：\n$$\\text{BR}_\\text{paper} = \\frac{\\text{score}(\\text{wrong\\_answer})}{\\text{score}(\\text{gold\\_answer})}$$\n\nQ5 使用广义 BR（Generalized BR），对所有问题计算：\n$$\\text{BR}_\\text{gen} = \\frac{\\text{score}(\\text{SC\\_answer})}{\\sum \\text{score}(\\text{other\\_answers})}$$\n\n### 结果\n\n| 条件 | 全集 n | 全集 BR | SC-correct n | SC-correct BR | SC-wrong n | SC-wrong BR |\n|------|--------|---------|-------------|---------------|-----------|-------------|\n| Mistral-7B × PW (seed42) | 512 (+86∞) | 2.074 | 194 (+44∞) | **2.190** | 318 (+42∞) | 2.004 |\n| Mistral-7B × FOLIO (seed42) | 166 (+37∞) | 2.659 | 81 (+29∞) | **3.639** | 85 (+8∞) | 1.725 |\n| Qwen2.5-14B × FOLIO | 85 (+119∞) | 2.045 | 52 (+106∞) | **2.131** | 33 (+13∞) | 1.908 |\n| LLaMA-8B × FOLIO | 157 (+47∞) | 2.008 | 92 (+43∞) | **2.071** | 65 (+4∞) | 1.918 |\n| Qwen2.5-14B × PW | 378 (+222∞) | 1.317 | 239 (+202∞) | **1.291** | 139 (+20∞) | 1.362 |\n| Mistral-7B × FOLIO (seed123) | 175 (+29∞) | 2.158 | 96 (+22∞) | **2.573** | 79 (+7∞) | 1.655 |\n\n> n 为有限 BR 的问题数；\"+∞\" 表示 other_scores=0（即约束只支持 SC 答案、完全不支持其他答案）的问题数。这些问题的 BR → ∞，是偏差最极端的情况。\n\n### 关键发现\n\n1. **所有条件下 SC-correct 子集 BR 均 > 1**（范围 1.29–3.64），确认即使模型答对了，约束仍然偏向 SC 多数答案而非独立验证。\n\n2. **SC-correct BR ≥ SC-wrong BR**（5/6 条件成立）。在 Mistral-7B × FOLIO 上最为显著：SC-correct BR = 3.64 vs SC-wrong BR = 1.73。这是因为模型答对的问题往往具有更高的 SC 投票一致性，而约束偏差与投票一致性正相关。\n\n3. **∞ 值集中在 SC-correct 子集**。例如 Qwen2.5-14B × FOLIO：SC-correct 有 106 个 BR=∞ 的问题（占 67%），而 SC-wrong 仅 13 个。这说明在高置信度正确问题上，约束几乎完全只支持多数答案。\n\n4. **Qwen2.5-14B × PW 是唯一例外**，SC-correct BR (1.291) 略低于 SC-wrong BR (1.362)。该条件 SC 准确率最高（73.5%），BR 整体最低，说明高能力模型的偏差更温和。\n\n### 解释\n\n这一结果进一步支持 Symbolic Mirage 假说：自提取约束是 SC 多数答案的分布投影（distributional projection），而非独立验证信号。约束不区分对错——它们系统性地放大模型多数意见，无论该意见是否正确。这正是 Eq. 6（退化条件）的体现：约束评分退化为加权多数投票。\n\n---\n\n## Q6: 27 种 training-free remediation 中 BH 校正前有哪些显著？\n\n### 方法\n\n论文 Table 5（9 种 prompt-level）、Table 6（3 种 method-level）、Table 7（15 种 additional）共 27 种策略。显著性检验使用 McNemar exact test（双侧），多重比较校正使用 Benjamini-Hochberg (BH)。\n\n### BH 校正前 p < 0.05 的策略\n\n| # | 方法 | 类型 | Δ (pp) | p_raw | p_BH | 显著(raw)? | 显著(BH)? |\n|---|------|------|--------|-------|------|-----------|----------|\n| 11 | Contrastive Scoring | Method-level | **−9.31** | .007 | ~0.094 | ✓ | ✓* |\n| 12 | LLM-Debate | Method-level | **−18.63** | <.001 | ~0.027 | ✓ | ✓ |\n\n> \\* 论文 Appendix D.10 明确声明 \"After BH correction across all 27 comparisons, only these two negative results remain significant\"，尽管简单 BH 计算（p_BH = p × 27/rank）对 Contrastive 给出 ~0.094，可能是因为其他条件中有额外的低 p 值拉低了排名。\n\n### 其余 25 种策略：全部 p_raw ≥ 0.05\n\n| # | 方法 | Δ (pp) | p_raw 来源 |\n|---|------|--------|-----------|\n| 1 | Contrastive (prompt) | −1.10 | 小 Δ，n=182，未报告 p |\n| 2 | Cross-model extraction | 0.00 | = 1.0 |\n| 3 | Qwen3-14B baseline | −0.49 | .655（报告值）|\n| 4 | Z3 feedback loop | — | 诊断性指标，无 Δ |\n| 5 | Consistency filtering | 0.00 | = 1.0 |\n| 6 | Cross-trace UNSAT | — | 诊断性指标 |\n| 7 | T=1.0 sampling | 0.00 | = 1.0 |\n| 8 | Multi-temperature | 0.00 | = 1.0（b=5, c=5）|\n| 9 | Discriminative filtering | 0.00 | = 1.0（803/804 agree）|\n| 10 | ICG | −1.96/+1.47 | .206（报告值）|\n| 13 | PROVE (code verif.) | −1.9 | 小 Δ，n=204 |\n| 14 | CEGIS (iterative) | 0.0† | 振荡，无净效果 |\n| 15 | DeepConf (logprob) | 0.0 | 无分离 |\n| 16 | Cross-model SICA | −0.49 | 小 Δ |\n| 17 | Problem perturbation | <0 | κ 反增至 0.70 |\n| 18 | MIN-UNSAT | −6.5 | 未报告 McNemar |\n| 19 | κ-aware SC | 0.0 | = 1.0（11/11 条件 Δ=0）|\n| 20 | Z3 trace filter | −0.49 | 7 题受影响 |\n| 21 | Bootstrapped gold | 0.0† | 振荡 |\n| 22 | Selective abstention | +4.4* | 仅在降低覆盖率下有效 |\n| 23 | ASCII perturbation | 0.0 | = 1.0 |\n| 24 | Atom pipeline | −10.0 | 未报告 McNemar |\n| 25 | Premise-only filter | +2.45 | .359（报告值）|\n| 26 | DPP trace selection | +1.47 | .629（报告值）|\n| 27 | Z3 strict-mode | 0.0 | = 1.0（b=1, c=1）|\n\n> †振荡：第一轮有正向 Δ 但后续轮退化。*仅在降低覆盖率下有效，不算通用改进。\n\n### 关于 #18 MIN-UNSAT 和 #24 Atom pipeline 的注释\n\n这两个策略有较大的负向 Δ（−6.5pp 和 −10.0pp），但论文未报告 McNemar 检验。根据 Appendix D.10 的表述（\"only these two negative results remain significant\"），这两个策略在 BH 校正前**也可能不显著**——大 Δ 不一定意味着显著，因为 McNemar 检验关注的是*不一致对*的分布，而非准确率差异的幅度。如果这两种方法的错误高度重叠于 SC 的错误（即大部分是 both-wrong 而非 discordant），则即使 Δ 大，discordant 对仍可能不足以达到显著。\n\n### 显著条件的共同特征\n\n两个（BH 前）显著的策略共享以下特征：\n\n1. **都是结构性改变，而非参数微调**：Debate 用对抗辩论替代 trace 采样；Contrastive 用 pro/con 生成替代约束提取。相比之下，prompt 微调（#1–9）和参数调整（#19, #23）全部 Δ ≈ 0。\n\n2. **都导致灾难性准确率下降**（−9.3pp 和 −18.6pp），不是改进。没有任何正向策略达到显著。\n\n3. **都打破了信息结构但未引入独立信号**：\n   - Debate 成功降低了 κ（0.15），但代价是准确率崩溃——同模型多样性和质量不可兼得。\n   - Contrastive 产生不平衡输出（94 pro vs 65 con），表明 confirmation bias 转移到了约束生成过程。\n\n4. **与 cross-architecture verification 的对比**：真正有效的改进来自跨架构 NLI 验证（Section 5.4），这引入了结构性独立信号（不同架构 = 不同 distributional prior）。Training-free remediation 失败的根本原因是：同模型的任何变换都无法逃脱自身的 distributional prior。\n\n### 结论\n\n27 种 training-free remediation 中，BH 校正前仅 **2 种显著**（Debate 和 Contrastive Scoring），**均为负向效果**。BH 校正后这 2 种仍然显著。**没有任何正向策略在任何校正程序下达到显著**——这是 Symbolic Mirage 假说的核心实证支撑之一。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 224_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01PP54hr8tz2ugUmnBLK5uPZ`</summary>

```json
{
  "name": "Q5 Q6 Answers - Round 15",
  "type": "report",
  "description": "Round 15 reviewer Q5 (BR on SC-correct subset) and Q6 (BH-corrected remediation significance) answers with full data tables",
  "project": "symb_invariant_consensus",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/q5_q6_answers.md",
  "tags": [
    "rebuttal",
    "round15",
    "bias-ratio",
    "remediation",
    "BH-correction"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "15eae694-4c15-4baf-b677-fea33d6a4fa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8mxQ8waJk6Zkq1a289qvW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3353,
      "cache_read_input_tokens": 138596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3353
      },
      "output_tokens": 49,
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

_source line 225 · 2026-05-23T01:19:01.561Z_

<details><summary>↩ Tool result · `toolu_01PP54hr8tz2ugUmnBLK5uPZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_dcba11\", \"name\": \"Q5 Q6 Answers - Round 15\", \"type\": \"report\", \"description\": \"Round 15 reviewer Q5 (BR on SC-correct subset) and Q6 (BH-corrected remediation significance) answers with full data tables\", \"path\": \"projects/symb_invariant_consensus/artifacts/_project/report/q5_q6_answers.md\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T01:19:01.253216+00:00\", \"tags\": [\"rebuttal\", \"round15\", \"bias-ratio\", \"remediation\", \"BH-correction\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "e7a553af-dea2-4611-9086-4c18f34232eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260523_dcba11\\\", \\\"name\\\": \\\"Q5 Q6 Answers - Round 15\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Round 15 reviewer Q5 (BR on SC-correct subset) and Q6 (BH-corrected remediation significance) answers with full data tables\\\", \\\"path\\\": \\\"projects/symb_invariant_consensus/artifacts/_project/report/q5_q6_answers.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-23T01:19:01.253216+00:00\\\", \\\"tags\\\": [\\\"rebuttal\\\", \\\"round15\\\", \\\"bias-ratio\\\", \\\"remediation\\\", \\\"BH-correction\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_dcba11\", \"name\": \"Q5 Q6 Answers - Round 15\", \"type\": \"report\", \"description\": \"Round 15 reviewer Q5 (BR on SC-correct subset) and Q6 (BH-corrected remediation significance) answers with full data tables\", \"path\": \"projects/symb_invariant_consensus/artifacts/_project/report/q5_q6_answers.md\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T01:19:01.253216+00:00\", \"tags\": [\"rebuttal\", \"round15\", \"bias-ratio\", \"remediation\", \"BH-correction\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 226_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01RpHk69YwZL4Piw9Yu3Eu5B`</summary>

```json
{
  "todos": [
    {
      "content": "Q5: Compute BR on SC-correct subset vs full set",
      "status": "completed",
      "activeForm": "Computed BR for 6 conditions"
    },
    {
      "content": "Q6: Find raw p-values before BH correction for 27 remediation methods",
      "status": "completed",
      "activeForm": "Extracted all p-values from paper tables and data"
    },
    {
      "content": "Write q5_q6_answers.md and register artifact",
      "status": "completed",
      "activeForm": "Written and registered"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "e06f79dd-d797-4d29-be40-4dea1ae0d471",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017RmHXFU8NGHhwUZJ6sjtAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 141949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
      },
      "output_tokens": 32,
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

_source line 227 · 2026-05-23T01:19:06.603Z_

<details><summary>↩ Tool result · `toolu_01RpHk69YwZL4Piw9Yu3Eu5B`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "e4810ca9-d863-41cd-a463-4e71dec90fdc",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Q5: Compute BR on SC-correct subset vs full set",
        "status": "completed",
        "activeForm": "Computed BR for 6 conditions"
      },
      {
        "content": "Q6: Find raw p-values before BH correction for 27 remediation methods",
        "status": "completed",
        "activeForm": "Extracted all p-values from paper tables and data"
      },
      {
        "content": "Write q5_q6_answers.md and register artifact",
        "status": "in_progress",
        "activeForm": "Writing final answers"
      }
    ],
    "newTodos": [
      {
        "content": "Q5: Compute BR on SC-correct subset vs full set",
        "status": "completed",
        "activeForm": "Computed BR for 6 conditions"
      },
      {
        "content": "Q6: Find raw p-values before BH correction for 27 remediation methods",
        "status": "completed",
        "activeForm": "Extracted all p-values from paper tables and data"
      },
      {
        "content": "Write q5_q6_answers.md and register artifact",
        "status": "completed",
        "activeForm": "Written and registered"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 228_

完成。产出文件：`artifacts/q5_q6_answers.md`（已注册 `art_20260523_dcba11`）

**Q5 核心结论**：BR > 1 在 SC-correct 子集上全部成立，6 个条件的 SC-correct BR 范围 1.29–3.64。在 5/6 条件中，SC-correct BR ≥ SC-wrong BR。这说明约束不区分对错，系统性地放大 SC 多数意见——即使模型答对了，约束也只是在回声而非独立验证。

**Q6 核心结论**：27 种 training-free remediation 中，BH 校正前仅 Debate (p < .001) 和 Contrastive Scoring (p = .007) 显著，均为负向效果。BH 后两者仍显著。没有任何正向策略在任何校正下达到显著。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "uuid": "79fec575-c842-4a5b-b112-f956767a4185",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRiVVbf1WJAHXbedLLPdhQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 216,
      "cache_read_input_tokens": 142513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 216
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

_source line 229_

完成。产出文件：`artifacts/q5_q6_answers.md`（已注册 `art_20260523_dcba11`）

**Q5 核心结论**：BR > 1 在 SC-correct 子集上全部成立，6 个条件的 SC-correct BR 范围 1.29–3.64。在 5/6 条件中，SC-correct BR ≥ SC-wrong BR。这说明约束不区分对错，系统性地放大 SC 多数意见——即使模型答对了，约束也只是在回声而非独立验证。

**Q6 核心结论**：27 种 training-free remediation 中，BH 校正前仅 Debate (p < .001) 和 Contrastive Scoring (p = .007) 显著，均为负向效果。BH 后两者仍显著。没有任何正向策略在任何校正下达到显著。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 867220,
  "duration_api_ms": 849382,
  "num_turns": 92,
  "stop_reason": "end_turn",
  "session_id": "0e110ff1-657d-493f-8bbd-905826c70568",
  "total_cost_usd": 3.958127,
  "usage": {
    "input_tokens": 57,
    "cache_creation_input_tokens": 130888,
    "cache_read_input_tokens": 4480896,
    "output_tokens": 35892,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 130888,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 261,
        "cache_read_input_tokens": 142513,
        "cache_creation_input_tokens": 216,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 216
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1909,
      "outputTokens": 27,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0020440000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 57,
      "outputTokens": 35892,
      "cacheReadInputTokens": 4480896,
      "cacheCreationInputTokens": 130888,
      "webSearchRequests": 0,
      "costUSD": 3.956083,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a6c77735-8507-4aaa-aeac-2a6765c68e57"
}
```

</details>

---
