# analysis edcr diagnostic

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_analysis_edcr_diagnostic_20260515T234346.jsonl`
- **Structured JSON:** [`80a943cbb7134955b255.json`](../../sessions/80/80a943cbb7134955b255.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-15T23:45:39.190624+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T23:45:39.191174+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T23:45:39.191524+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/scripts/edcr_diagnostic.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/scripts/edcr_diagnostic.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T23:45:39.191787+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/freige/eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/freige/eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T23:45:39.192311+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Cross-method EDCR diagnostic analysis.\\n\\nInput:\\n  --methods NAME:PRED_PATH [NAME:PRED_PATH ...]\\n    Each entry is method_name:path_to_predictions.json\\n    predictions.json format: list of {doc_id, parsed_triples, gold_triples}\\n    where each triple has {head, relation, tail, evidence}\\n\\n  OR --auto-discover (scan /root/autodl-tmp/eval_results/*/predictions.json)\\n\\n  --gold PATH  DocRED dev.json for gold (only needed if predictions.json lacks gold_triples)\\n  --output-dir PATH  Where to write results (default: /root/autodl-tmp/eval_results/)\\n\\nOutput (in output_dir):\\n  edcr_diagnostic.json  — per-method: overall EDCR, per-relation-type EDCR, per-document EDCR stats\\n  edcr_diagnostic.tex   — LaTeX table ready for paper\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport statistics\\nimport sys\\nfrom collections import defaultdict\\nfrom pathlib import Path\\n\\n# Allow importing freige when run from /root/autodl-tmp/\\nsys.path.insert(0, str(Path(__file__).resolve().parents[1]))\\n\\nfrom eval.evaluator import DocREDEvaluator, _triple_key\\n\\n\\n# --------------------------------------------------------------------------\\n# Default method configs for --auto-discover\\n# --------------------------------------------------------------------------\\nAUTO_METHODS = [\\n    (\\\"SFT baseline (quant)\\\", \\\"/root/autodl-tmp/sft_baseline_eval_results/predictions.json\\\"),\\n    (\\\"SFT baseline (noquant)\\\", \\\"/root/autodl-tmp/eval_results/sft_baseline_noquant/predictions.json\\\"),\\n    (\\\"RSFT-CED s42\\\", \\\"/root/autodl-tmp/eval_results/rsft_r1/predictions.json\\\"),\\n    (\\\"RSFT-CED s43\\\", \\\"/root/autodl-tmp/eval_results/rsft_s43/predictions.json\\\"),\\n    (\\\"RSFT-CED s44\\\", \\\"/root/autodl-tmp/eval_results/rsft_s44/predictions.json\\\"),\\n    (\\\"RSFT-CED r2a\\\", \\\"/root/autodl-tmp/eval_results/rsft_r2a/predictions.json\\\"),\\n    (\\\"RS
…[truncated 7482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:45:39.192625+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/freige/eval_results/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:45:39.192960+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T23:45:39.193256+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 704\\ndrwxr-xr-x 43 root root   4096 May 16 07:39 .\\ndrwxr-xr-x 75 root root   4096 May 16 07:08 ..\\n-rw-r--r--  1 root root   1583 May 15 19:59 3seed_summary.json\\ndrwxr-xr-x  2 root root      6 May 16 03:54 bf16_g8_step30\\ndrwxr-xr-x  2 root root      6 May 16 03:57 bf16_g8_step50\\ndrwxr-xr-x  2 root root    127 May 15 17:52 ced_reranker_dryrun\\ndrwxr-xr-x  2 root root     95 May 15 22:44 ced_reranker_poc\\ndrwxr-xr-x  2 root root     95 May 15 16:02 ced_reranker_poc_dryrun\\n-rw-r--r--  1 root root   3364 May 16 03:59 cross_method_table.json\\ndrwxr-xr-x  2 root root     82 May 16 05:22 dpo_ced_1ep\\ndrwxr-xr-x  2 root root     62 May 16 07:35 dpo_ced_1ep_fixed\\ndrwxr-xr-x  2 root root      6 May 16 03:33 dpo_ced_ckpt400\\n-rw-r--r--  1 root root   9342 May 15 19:59 edcr_analysis.json\\n-rw-r--r--  1 root root  24773 May 15 19:57 edcr_analysis_r2b.md\\n-rw-r--r--  1 root root 622694 May 16 05:11 edcr_diagnostic.json\\n-rw-r--r--  1 root root   2700 May 16 05:11 edcr_diagnostic.tex\\n-rw-r--r--  1 root root   6834 May 16 07:22 edcr_diagnostic_v2.json\\n-rw-r--r--  1 root root   1672 May 16 07:22 edcr_diagnostic_v2.tex\\n-rw-r--r--  1 root root   1662 May 15 21:19 evi_f1_joint_comparison.json\\ndrwxr-xr-x  9 root root   4096 May 15 05:05 grpo_ced_kl001\\ndrwxr-xr-x  3 root root     60 May 15 03:35 grpo_ced_kl001_step100\\ndrwxr-xr-x  4 root root     84 May 15 05:30 grpo_ced_lr5e6\\ndrwxr-xr-x  2 root root     62 May 15 08:05 grpo_ced_lr5e6_ckpt60\\ndrwxr-xr-x  3 root root     59 May 15 06:06 grpo_ced_lr5e6_rp\\ndrwxr-xr-x  2 root root      6 May 16 03:55 grpo_extract_r4_step10\\ndrwxr-xr-x  4 root root     60 May 16 03:57 grpo_flatnli_r3\\ndrwxr-xr-x  5 root root    110 May 15 23:45 grpo_g8_bf16\\ndrwxr-xr-x  2 root root     62 May 15 23:40 grpo_g8_bf16_ckpt100\\ndrwxr-xr-x  3 root root     36 May 15 07:39 lr5e6_r1_ckpt100\\ndrwxr-xr-x  3 root root     59 May 15 07:08 lr5e6_r1_ckpt40\\ndrwxr-xr-x 
…[truncated 1645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:45:39.193519+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/sft_baseline_eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/sft_baseline_eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T23:45:39.193838+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7664\\ndrwxr-xr-x  2 root root      62 May 15 07:35 .\\ndrwxr-xr-x 75 root root    4096 May 16 07:08 ..\\n-rw-r--r--  1 root root    1260 May 15 07:35 metrics.json\\n-rw-r--r--  1 root root 7839031 May 15 07:35 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T23:45:39.194145+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python scripts/edcr_diagnostic.py --auto-discover",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python scripts/edcr_diagnostic.py --auto-discover",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T23:45:39.194555+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Analyzing: SFT baseline (quant)\\nAnalyzing: SFT baseline (noquant)\\nAnalyzing: RSFT-CED s42\\nAnalyzing: RSFT-CED s43\\nAnalyzing: RSFT-CED s44\\nAnalyzing: RSFT-CED r2a\\nAnalyzing: RSFT-CED r2b\\nAnalyzing: RSFT-flatNLI s42\\nAnalyzing: SFT no-evidence\\nAnalyzing: GRPO bf16 ckpt100\\nAnalyzing: GRPO QLoRA kl001 ckpt100\\nAnalyzing: GRPO QLoRA lr5e6 ckpt100\\nAnalyzing: DPO-CED 1ep\\nAnalyzing: RSFT-flatNLI s43\\n\\nJSON -> /root/autodl-tmp/eval_results/edcr_diagnostic.json\\nLaTeX -> /root/autodl-tmp/eval_results/edcr_diagnostic.tex\\n\\nMethod                        rel_f1  evi_f1    EDCR     med     std  n_doc\\n------------------------------------------------------------------------------\\nSFT baseline (quant)          0.4057  0.7979  0.7118  0.6838  0.2879    982\\nSFT baseline (noquant)        0.4106  0.8013  0.7039  0.6667  0.2927    983\\nRSFT-CED s42                  0.4449  0.8187  0.6565  0.6000  0.2936    985\\nRSFT-CED s43                  0.4683  0.8156  0.6388  0.5818  0.2902    985\\nRSFT-CED s44                  0.4655  0.8087  0.6350  0.5714  0.2894    985\\nRSFT-CED r2a                  0.4494  0.8108  0.6641  0.6190  0.2844    985\\nRSFT-CED r2b                  0.4493  0.8128  0.6609  0.6111  0.2866    983\\nRSFT-flatNLI s42              0.4539  0.8043  0.6431  0.6000  0.2935    985\\nSFT no-evidence               0.4893  0.0000  0.0000  0.0000  0.0000      0\\nGRPO bf16 ckpt100             0.4549  0.8086  0.6318  0.5909  0.2743    985\\nGRPO QLoRA kl001 ckpt100      0.2167  0.5746  0.8539  0.9231  0.1787    985\\nGRPO QLoRA lr5e6 ckpt100      0.0147  0.8502  0.9869  1.0000  0.0562    984\\nDPO-CED 1ep                   0.0022  0.7500  0.9982  1.0000  0.0137    981\\nRSFT-flatNLI s43              0.0022  0.8533  0.9982  1.0000  0.0125    981\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T23:45:39.194875+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/edcr_diagnostic.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/edcr_diagnostic.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T23:45:39.195133+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/edcr_diagnostic.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/edcr_diagnostic.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T23:45:39.195713+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"method\\\": \\\"SFT baseline (quant)\\\",\\n    \\\"rel_f1\\\": 0.4057,\\n    \\\"evi_f1\\\": 0.7979,\\n    \\\"edcr\\\": 0.7118,\\n    \\\"n_distractor_citations\\\": 21796,\\n    \\\"n_total_citations\\\": 30622,\\n    \\\"n_predictions\\\": 18815,\\n    \\\"per_relation_edcr\\\": {\\n      \\\"country\\\": {\\n        \\\"edcr\\\": 0.6565,\\n        \\\"n_distractor\\\": 4642,\\n        \\\"n_total\\\": 7071,\\n        \\\"n_triples\\\": 3930\\n      },\\n      \\\"located in the administrative territorial entity\\\": {\\n        \\\"edcr\\\": 0.7317,\\n        \\\"n_distractor\\\": 1934,\\n        \\\"n_total\\\": 2643,\\n        \\\"n_triples\\\": 1749\\n      },\\n      \\\"contains administrative territorial entity\\\": {\\n        \\\"edcr\\\": 0.8341,\\n        \\\"n_distractor\\\": 1734,\\n        \\\"n_total\\\": 2079,\\n        \\\"n_triples\\\": 1274\\n      },\\n      \\\"country of citizenship\\\": {\\n        \\\"edcr\\\": 0.6104,\\n        \\\"n_distractor\\\": 1308,\\n        \\\"n_total\\\": 2143,\\n        \\\"n_triples\\\": 1258\\n      },\\n      \\\"record label\\\": {\\n        \\\"edcr\\\": 0.6816,\\n        \\\"n_distractor\\\": 976,\\n        \\\"n_total\\\": 1432,\\n        \\\"n_triples\\\": 796\\n      },\\n      \\\"has part\\\": {\\n        \\\"edcr\\\": 0.7306,\\n        \\\"n_distractor\\\": 499,\\n        \\\"n_total\\\": 683,\\n        \\\"n_triples\\\": 463\\n      },\\n      \\\"head of government\\\": {\\n        \\\"edcr\\\": 0.9766,\\n        \\\"n_distractor\\\": 752,\\n        \\\"n_total\\\": 770,\\n        \\\"n_triples\\\": 458\\n      },\\n      \\\"country of origin\\\": {\\n        \\\"edcr\\\": 0.8331,\\n        \\\"n_distractor\\\": 639,\\n        \\\"n_total\\\": 767,\\n        \\\"n_triples\\\": 389\\n      },\\n      \\\"date of birth\\\": {\\n        \\\"edcr\\\": 0.217,\\n        \\\"n_distractor\\\": 87,\\n        \\\"n_total\\\": 401,\\
…[truncated 8642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T23:45:39.196070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"% Auto-generated by edcr_diagnostic.py\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{EDCR Cross-Method Diagnostic}\\n\\\\label{tab:edcr-diagnostic}\\n\\\\begin{tabular}{l ccc cc}\\n\\\\toprule\\nMethod & Rel-F1 & Evi-F1 & EDCR & EDCR$_\\\\text{med}$ & EDCR$_\\\\text{std}$ \\\\\\\\\\n\\\\midrule\\n  SFT baseline (quant) & 0.4057 & 0.7979 & 0.7118 & 0.6838 & 0.2879 \\\\\\\\\\n  SFT baseline (noquant) & 0.4106 & 0.8013 & 0.7039 & 0.6667 & 0.2927 \\\\\\\\\\n  RSFT-CED s42 & 0.4449 & 0.8187 & 0.6565 & 0.6000 & 0.2936 \\\\\\\\\\n  RSFT-CED s43 & 0.4683 & 0.8156 & 0.6388 & 0.5818 & 0.2902 \\\\\\\\\\n  RSFT-CED s44 & 0.4655 & 0.8087 & 0.6350 & 0.5714 & 0.2894 \\\\\\\\\\n  RSFT-CED r2a & 0.4494 & 0.8108 & 0.6641 & 0.6190 & 0.2844 \\\\\\\\\\n  RSFT-CED r2b & 0.4493 & 0.8128 & 0.6609 & 0.6111 & 0.2866 \\\\\\\\\\n  RSFT-flatNLI s42 & 0.4539 & 0.8043 & 0.6431 & 0.6000 & 0.2935 \\\\\\\\\\n  SFT no-evidence & 0.4893 & 0.0000 & 0.0000 & 0.0000 & 0.0000 \\\\\\\\\\n  GRPO bf16 ckpt100 & 0.4549 & 0.8086 & 0.6318 & 0.5909 & 0.2743 \\\\\\\\\\n  GRPO QLoRA kl001 ckpt100 & 0.2167 & 0.5746 & 0.8539 & 0.9231 & 0.1787 \\\\\\\\\\n  GRPO QLoRA lr5e6 ckpt100 & 0.0147 & 0.8502 & 0.9869 & 1.0000 & 0.0562 \\\\\\\\\\n  DPO-CED 1ep & 0.0022 & 0.7500 & 0.9982 & 1.0000 & 0.0137 \\\\\\\\\\n  RSFT-flatNLI s43 & 0.0022 & 0.8533 & 0.9982 & 1.0000 & 0.0125 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Per-Relation-Type EDCR (top-10 relations by frequency)}\\n\\\\label{tab:edcr-per-relation}\\n\\\\begin{tabular}{l c c c c c c c c c c c c c c}\\n\\\\toprule\\nRelation & SFT baseline & SFT baseline & RSFT-CED s42 & RSFT-CED s43 & RSFT-CED s44 & RSFT-CED r2a & RSFT-CED r2b & RSFT-flatNLI & SFT no-evide & GRPO bf16 ck & GRPO QLoRA k & GRPO QLoRA l & DPO-CED 1ep & RSFT-flatNLI \\\\\\\\\\n\\\\midrule\\n  country & 0.656 & 0.623 & 0.579 & 0.550 & 0.522 & 0.
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T23:45:39.196426+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "EDCR Cross-Method Diagnostic Table",
  "type": "report",
  "description": "Cross-method EDCR diagnostic: 14 methods analyzed. Best EDCR among viable methods (rel_f1>0.4): GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350). Includes per-relation and per-document breakdowns.",
  "project": "faith-evidence-ie",
  "exp_id": "plan_003_edcr_diagnostic",
  "content_filename": "edcr_diagnostic_summary.md",
  "content": "# EDCR Cross-Method Diagnostic (2026-05-16)\n\n## Summary Table\n\n| Method | rel_f1 | evi_f1 | EDCR | median | std | n_doc |\n|---|---|---|---|---|---|---|\n| SFT baseline (quant) | 0.4057 | 0.7979 | 0.7118 | 0.6838 | 0.2879 | 982 |\n| SFT baseline (noquant) | 0.4106 | 0.8013 | 0.7039 | 0.6667 | 0.2927 | 983 |\n| RSFT-CED s42 | 0.4449 | 0.8187 | 0.6565 | 0.6000 | 0.2936 | 985 |\n| RSFT-CED s43 | 0.4683 | 0.8156 | 0.6388 | 0.5818 | 0.2902 | 985 |\n| RSFT-CED s44 | 0.4655 | 0.8087 | 0.6350 | 0.5714 | 0.2894 | 985 |\n| RSFT-CED r2a | 0.4494 | 0.8108 | 0.6641 | 0.6190 | 0.2844 | 985 |\n| RSFT-CED r2b | 0.4493 | 0.8128 | 0.6609 | 0.6111 | 0.2866 | 983 |\n| RSFT-flatNLI s42 | 0.4539 | 0.8043 | 0.6431 | 0.6000 | 0.2935 | 985 |\n| SFT no-evidence | 0.4893 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 |\n| GRPO bf16 ckpt100 | 0.4549 | 0.8086 | 0.6318 | 0.5909 | 0.2743 | 985 |\n| GRPO QLoRA kl001 ckpt100 | 0.2167 | 0.5746 | 0.8539 | 0.9231 | 0.1787 | 985 |\n| GRPO QLoRA lr5e6 ckpt100 | 0.0147 | 0.8502 | 0.9869 | 1.0000 | 0.0562 | 984 |\n| DPO-CED 1ep | 0.0022 | 0.7500 | 0.9982 | 1.0000 | 0.0137 | 981 |\n| RSFT-flatNLI s43 | 0.0022 | 0.8533 | 0.9982 | 1.0000 | 0.0125 | 981 |\n\n## Key Observations\n- **Best EDCR (viable methods, rel_f1>0.4):** GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350)\n- **SFT no-evidence:** EDCR=0 (no evidence produced, as expected)\n- **Degenerate models** (DPO-CED 1ep, RSFT-flatNLI s43, GRPO QLoRA lr5e6): EDCR≈1.0 but rel_f1<0.02 — nearly all citations are distractors because the model barely extracts correct triples\n- **GRPO bf16 has lowest EDCR AND lowest std (0.2743)** among viable methods — most consistent evidence quality\n\n## Files\n- JSON: `/root/autodl-tmp/eval_results/edcr_diagnostic.json`\n- LaTeX: `/root/autodl-tmp/eval_results/edcr_diagnostic.tex`\n",
  "tags": "['edcr', 'diagnostic', 'cross-method', 'evidence-quality']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "EDCR Cross-Method Diagnostic Table",
    "type": "report",
    "description": "Cross-method EDCR diagnostic: 14 methods analyzed. Best EDCR among viable methods (rel_f1>0.4): GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350). Includes per-relation and per-document breakdowns.",
    "project": "faith-evidence-ie",
    "exp_id": "plan_003_edcr_diagnostic",
    "content_filename": "edcr_diagnostic_summary.md",
    "content": "# EDCR Cross-Method Diagnostic (2026-05-16)\n\n## Summary Table\n\n| Method | rel_f1 | evi_f1 | EDCR | median | std | n_doc |\n|---|---|---|---|---|---|---|\n| SFT baseline (quant) | 0.4057 | 0.7979 | 0.7118 | 0.6838 | 0.2879 | 982 |\n| SFT baseline (noquant) | 0.4106 | 0.8013 | 0.7039 | 0.6667 | 0.2927 | 983 |\n| RSFT-CED s42 | 0.4449 | 0.8187 | 0.6565 | 0.6000 | 0.2936 | 985 |\n| RSFT-CED s43 | 0.4683 | 0.8156 | 0.6388 | 0.5818 | 0.2902 | 985 |\n| RSFT-CED s44 | 0.4655 | 0.8087 | 0.6350 | 0.5714 | 0.2894 | 985 |\n| RSFT-CED r2a | 0.4494 | 0.8108 | 0.6641 | 0.6190 | 0.2844 | 985 |\n| RSFT-CED r2b | 0.4493 | 0.8128 | 0.6609 | 0.6111 | 0.2866 | 983 |\n| RSFT-flatNLI s42 | 0.4539 | 0.8043 | 0.6431 | 0.6000 | 0.2935 | 985 |\n| SFT no-evidence | 0.4893 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 |\n| GRPO bf16 ckpt100 | 0.4549 | 0.8086 | 0.6318 | 0.5909 | 0.2743 | 985 |\n| GRPO QLoRA kl001 ckpt100 | 0.2167 | 0.5746 | 0.8539 | 0.9231 | 0.1787 | 985 |\n| GRPO QLoRA lr5e6 ckpt100 | 0.0147 | 0.8502 | 0.9869 | 1.0000 | 0.0562 | 984 |\n| DPO-CED 1ep | 0.0022 | 0.7500 | 0.9982 | 1.0000 | 0.0137 | 981 |\n| RSFT-flatNLI s43 | 0.0022 | 0.8533 | 0.9982 | 1.0000 | 0.0125 | 981 |\n\n## Key Observations\n- **Best EDCR (viable methods, rel_f1>0.4):** GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350)\n- **SFT no-evidence:** EDCR=0 (no evidence produced, as expected)\n- **Degenerate models** (DPO-CED 1ep, RSFT-flatNLI s43, GRPO QLoRA lr5e6): EDCR≈1.0 but rel_f1<0.02 — nearly all citations are distractors because the model barely extracts correct triples\n- **GRPO bf16 has lowest EDCR AND lowest std (0.2743)** among viable methods — most consistent evidence quality\n\n## Files\n- JSON: `/root/autodl-tmp/eval_results/edcr_diagnostic.json`\n- LaTeX: `/root/autodl-tmp/eval_results/edcr_diagnostic.tex`\n",
    "tags": "['edcr', 'diagnostic', 'cross-method', 'evidence-quality']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T23:45:39.196734+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_b9319a\", \"name\": \"EDCR Cross-Method Diagnostic Table\", \"type\": \"report\", \"description\": \"Cross-method EDCR diagnostic: 14 methods analyzed. Best EDCR among viable methods (rel_f1>0.4): GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350). Includes per-relation and per-document breakdowns.\", \"path\": \"projects/faith-evidence-ie/artifacts/plan_003_edcr_diagnostic/report/edcr_diagnostic_summary.md\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": \"plan_003_edcr_diagnostic\", \"skill\": \"\", \"created_at\": \"2026-05-15T23:44:53.624871+00:00\", \"tags\": [\"edcr\", \"diagnostic\", \"cross-method\", \"evidence-quality\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T23:45:39.196962+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "status",
  "value": "done",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "status",
    "value": "done",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T23:45:39.197181+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid state 'done'. Valid: ['ALLOCATED', 'ANALYZING', 'DEPLOYED', 'DEPLOYING', 'DONE', 'PENDING', 'PREPARING', 'QUEUED', 'RUNNING']\", \"metadata\": {\"elapsed_seconds\": 1.7229}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T23:45:39.197431+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "status",
  "value": "DONE",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T23:45:39.197639+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.4339}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T23:45:39.197842+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "conclusion",
  "value": "14 methods analyzed. Best EDCR among viable methods (rel_f1>0.4): GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350). GRPO bf16 also has lowest per-doc std (0.2743). Degenerate models (DPO-CED, RSFT-flatNLI s43) have EDCR≈1.0 due to near-zero rel_f1.",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "conclusion",
    "value": "14 methods analyzed. Best EDCR among viable methods (rel_f1>0.4): GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350). GRPO bf16 also has lowest per-doc std (0.2743). Degenerate models (DPO-CED, RSFT-flatNLI s43) have EDCR≈1.0 due to near-zero rel_f1.",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T23:45:39.198059+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion '14 methods analyzed. Best EDCR among viable methods (rel_f1>0.4): GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350). GRPO bf16 also has lowest per-doc std (0.2743). Degenerate models (DPO-CED, RSFT-flatNLI s43) have EDCR≈1.0 due to near-zero rel_f1.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.6455}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T23:45:39.198286+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "conclusion",
  "value": "success",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T23:45:39.198525+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_003_edcr_diagnostic\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:40.174Z\", \"updated_at\": \"2026-05-15T23:45:09.365Z\", \"hypothesis\": \"EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。\", \"server\": \"rtx5090-4x\", \"gpu\": null, \"account\": \"root\", \"spec\": {\"gpu\": null, \"server\": \"rtx5090-4x\", \"notes\": \"CPU-only task, GPU allocation removed to free cuda:3\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0675}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T23:45:39.198749+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "status",
  "value": "DONE",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T23:45:39.198951+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path', 'log_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.9341}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T23:45:39.199147+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "metrics",
  "value": "{'n_methods': 14, 'best_edcr_viable': {'method': 'GRPO bf16 ckpt100', 'edcr': 0.6318, 'rel_f1': 0.4549}, 'runner_up': {'method': 'RSFT-CED s44', 'edcr': 0.635, 'rel_f1': 0.4655}, 'sft_baseline_edcr': 0.7118}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "metrics",
    "value": "{'n_methods': 14, 'best_edcr_viable': {'method': 'GRPO bf16 ckpt100', 'edcr': 0.6318, 'rel_f1': 0.4549}, 'runner_up': {'method': 'RSFT-CED s44', 'edcr': 0.635, 'rel_f1': 0.4655}, 'sft_baseline_edcr': 0.7118}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T23:45:39.199419+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_003_edcr_diagnostic\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:40.174Z\", \"updated_at\": \"2026-05-15T23:45:16.688Z\", \"hypothesis\": \"EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。\", \"server\": \"rtx5090-4x\", \"gpu\": null, \"account\": \"root\", \"spec\": {\"gpu\": null, \"server\": \"rtx5090-4x\", \"notes\": \"CPU-only task, GPU allocation removed to free cuda:3\"}, \"conclusion\": \"success\", \"metrics\": {\"n_methods\": 14, \"best_edcr_viable\": {\"method\": \"GRPO bf16 ckpt100\", \"edcr\": 0.6318, \"rel_f1\": 0.4549}, \"runner_up\": {\"method\": \"RSFT-CED s44\", \"edcr\": 0.635, \"rel_f1\": 0.4655}, \"sft_baseline_edcr\": 0.7118}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1691}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T23:45:39.199880+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/eval_results/edcr_diagnostic.json",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/eval_results/edcr_diagnostic.json",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T23:45:39.200137+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_003_edcr_diagnostic\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:40.174Z\", \"updated_at\": \"2026-05-15T23:45:21.038Z\", \"hypothesis\": \"EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。\", \"server\": \"rtx5090-4x\", \"gpu\": null, \"account\": \"root\", \"spec\": {\"gpu\": null, \"server\": \"rtx5090-4x\", \"notes\": \"CPU-only task, GPU allocation removed to free cuda:3\"}, \"conclusion\": \"success\", \"metrics\": {\"n_methods\": 14, \"best_edcr_viable\": {\"method\": \"GRPO bf16 ckpt100\", \"edcr\": 0.6318, \"rel_f1\": 0.4549}, \"runner_up\": {\"method\": \"RSFT-CED s44\", \"edcr\": 0.635, \"rel_f1\": 0.4655}, \"sft_baseline_edcr\": 0.7118}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.626}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T23:45:39.200395+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "log_path",
  "value": "/root/autodl-tmp/eval_results/edcr_diagnostic.tex",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "log_path",
    "value": "/root/autodl-tmp/eval_results/edcr_diagnostic.tex",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T23:45:39.200641+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_003_edcr_diagnostic\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:40.174Z\", \"updated_at\": \"2026-05-15T23:45:21.815Z\", \"hypothesis\": \"EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。\", \"server\": \"rtx5090-4x\", \"gpu\": null, \"account\": \"root\", \"spec\": {\"gpu\": null, \"server\": \"rtx5090-4x\", \"notes\": \"CPU-only task, GPU allocation removed to free cuda:3\"}, \"conclusion\": \"success\", \"metrics\": {\"n_methods\": 14, \"best_edcr_viable\": {\"method\": \"GRPO bf16 ckpt100\", \"edcr\": 0.6318, \"rel_f1\": 0.4549}, \"runner_up\": {\"method\": \"RSFT-CED s44\", \"edcr\": 0.635, \"rel_f1\": 0.4655}, \"sft_baseline_edcr\": 0.7118}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.json\", \"log_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.tex\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6487}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T23:45:39.200882+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_003_edcr_diagnostic",
  "field": "status",
  "value": "DONE",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_003_edcr_diagnostic",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T23:45:39.201145+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_003_edcr_diagnostic\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:40.174Z\", \"updated_at\": \"2026-05-15T23:45:26.064Z\", \"hypothesis\": \"EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。\", \"server\": \"rtx5090-4x\", \"gpu\": null, \"account\": \"root\", \"spec\": {\"gpu\": null, \"server\": \"rtx5090-4x\", \"notes\": \"CPU-only task, GPU allocation removed to free cuda:3\"}, \"conclusion\": \"success\", \"metrics\": {\"n_methods\": 14, \"best_edcr_viable\": {\"method\": \"GRPO bf16 ckpt100\", \"edcr\": 0.6318, \"rel_f1\": 0.4549}, \"runner_up\": {\"method\": \"RSFT-CED s44\", \"edcr\": 0.635, \"rel_f1\": 0.4655}, \"sft_baseline_edcr\": 0.7118}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.json\", \"log_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.tex\", \"completed_at\": \"2026-05-15T23:45:26.064Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4386}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T23:45:39.201472+00:00_

EDCR diagnostic 完成。14 个方法全部成功分析，registry 已更新为 DONE。

**结果摘要（viable methods, rel_f1>0.4）：**

| Method | rel_f1 | evi_f1 | EDCR |
|---|---|---|---|
| **GRPO bf16 ckpt100** | 0.4549 | 0.8086 | **0.6318** (最低) |
| RSFT-CED s44 | 0.4655 | 0.8087 | 0.6350 |
| RSFT-CED s43 | 0.4683 | 0.8156 | 0.6388 |
| RSFT-flatNLI s42 | 0.4539 | 0.8043 | 0.6431 |
| RSFT-CED s42 | 0.4449 | 0.8187 | 0.6565 |
| SFT baseline (quant) | 0.4057 | 0.7979 | 0.7118 (最高) |

GRPO bf16 ckpt100 的 EDCR 最低（0.6318）且 per-doc std 最小（0.2743），evidence 质量最稳定。SFT no-evidence 的 EDCR=0 符合预期（无 evidence 输出）。DPO-CED 1ep / RSFT-flatNLI s43 / GRPO QLoRA lr5e6 的 EDCR≈1.0 是因为 rel_f1<0.02，模型退化导致几乎所有 citation 都是 distractor。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_edcr_diagnostic_20260515T234346"
}
```

</details>

---
