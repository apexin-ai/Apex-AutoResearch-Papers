# code caclr training framework

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_code_caclr_training_framework_20260520T214641.log`
- **Structured JSON:** [`d221d010f46ab49ca162.json`](../../sessions/d2/d221d010f46ab49ca162.json)

## Before a recorded user message

18 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
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
  "uuid": "64128eaf-5f93-456b-8356-56bda55e2833",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/memory/"
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
    "resetsAt": 1779325800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fab18f98-8fa3-49ac-b92f-14afe75265b7",
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the two referenced files to understand the existing code structure and ensure compatibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "184976fc-f118-43bd-bb98-ee16ec95e48f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CSyz7Z7vgWXJMDFPB1ebX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13249,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13249
      },
      "output_tokens": 25,
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

_source line 5_

读取现有代码了解上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "9771771b-a6a5-4288-9334-4ca87d8f2c93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CSyz7Z7vgWXJMDFPB1ebX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13249,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13249
      },
      "output_tokens": 25,
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_018P1BjjBhKqKNzk3sjr5zu6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/train_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "61a74582-c531-4cfe-a66a-9e4e8e439ec2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CSyz7Z7vgWXJMDFPB1ebX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13249,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13249
      },
      "output_tokens": 25,
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

_source line 7 · 2026-05-20T21:46:50.926Z_

<details><summary>↩ Tool result · `toolu_018P1BjjBhKqKNzk3sjr5zu6`</summary>

```text
1	"""
2	Train per-layer correctness probes (logistic regression) on English activations.
3	
4	For each layer, trains an L2-regularized LogisticRegression on 80% of the
5	English data and evaluates on the held-out 20%. Reports AUROC, ECE, Brier score.
6	
7	Input:  .pt files from extract_activations.py  (e.g. activations/layer8_en.pt)
8	Output: probe pickle files + train_metrics.csv
9	
10	Usage:
11	  python train_probe.py \
12	    --activations_dir ./activations \
13	    --output_dir ./probes \
14	    --layers 0,4,8,12,16,20,24,28,31
15	"""
16	
17	import argparse
18	import os
19	import pickle
20	
21	import numpy as np
22	import torch
23	from sklearn.linear_model import LogisticRegression
24	from sklearn.model_selection import train_test_split
25	from sklearn.preprocessing import StandardScaler
26	from sklearn.metrics import roc_auc_score, brier_score_loss
27	
28	
29	def parse_args():
30	    p = argparse.ArgumentParser()
31	    p.add_argument("--activations_dir", default="./activations")
32	    p.add_argument("--output_dir", default="./probes")
33	    p.add_argument("--layers", default=None,
34	                   help="Comma-separated layer indices. Default: auto-detect from activations_dir")
35	    p.add_argument("--test_size", type=float, default=0.2)
36	    p.add_argument("--seed", type=int, default=42)
37	    p.add_argument("--C", type=float, default=1.0, help="Inverse regularization strength")
38	    p.add_argument("--max_iter", type=int, default=2000)
39	    return p.parse_args()
40	
41	
42	def compute_ece(probs, labels, n_bins=10):
43	    """Histogram-based Expected Calibration Error (10 equal-width bins)."""
44	    bin_edges = np.linspace(0, 1, n_bins + 1)
45	    ece = 0.0
46	    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
47	        mask = (probs > lo) & (probs <= hi)
48	        if lo == 0.0:
49	            mask = (probs >= lo) & (probs <= hi)
50	        n_in_bin = mask.sum()
51	        if n_in_bin == 0:
52	            continue
53	        avg_conf = probs[mask].mean()
54	        avg_acc = labels[mask].mean()
55	        ece += (n_in_bin / len(probs)) * abs(avg_acc - avg_conf)
56	    return ece
57	
58	
59	def main():
60	    args = parse_args()
61	    if args.layers is None:
62	        import glob
63	        available = sorted(set(
64	            int(os.path.basename(f).split('_')[0].replace('layer', ''))
65	            for f in glob.glob(os.path.join(args.activations_dir, 'layer*_en.pt'))
66	        ))
67	        if not available:
68	            raise RuntimeError(f"No layer*_en.pt files found in {args.activations_dir}")
69	        print(f"Auto-detected layers: {available}")
70	        layer_indices = available
71	    else:
72	        layer_indices = sorted(int(x) for x in args.layers.split(","))
73	    os.makedirs(args.output_dir, exist_ok=True)
74	
75	    results = []
76	    print(f"{'Layer':>5s} {'N_train':>7s} {'N_test':>6s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s}")
77	    print("-" * 46)
78	
79	    for li in layer_indices:
80	        pt_path = os.path.join(args.activations_dir, f"layer{li}_en.pt")
81	        if not os.path.exists(pt_path):
82	            print(f"  [SKIP] {pt_path} not found")
83	            continue
84	
85	        data = torch.load(pt_path, weights_only=True)
86	        X = data["activations"].numpy()
87	        y = data["labels"].numpy()
88	
89	        if len(np.unique(y)) < 2:
90	            print(f"  [SKIP] Layer {li}: only one class present (all correct or all wrong)")
91	            continue
92	
93	        X_train, X_test, y_train, y_test = train_test_split(
94	            X, y, test_size=args.test_size, random_state=args.seed, stratify=y,
95	        )
96	
97	        scaler = StandardScaler()
98	        X_train_s = scaler.fit_transform(X_train)
99	        X_test_s = scaler.transform(X_test)
100	
101	        clf = LogisticRegression(
102	            C=args.C, penalty="l2", solver="lbfgs", max_iter=args.max_iter, random_state=args.seed,
103	        )
104	        clf.fit(X_train_s, y_train)
105	
106	        probs = clf.predict_proba(X_test_s)[:, 1]
107	        auroc = roc_auc_score(y_test, probs)
108	        ece = compute_ece(probs, y_test)
109	        brier = brier_score_loss(y_test, probs)
110	
111	        print(f"{li:>5d} {len(y_train):>7d} {len(y_test):>6d} {auroc:>7.4f} {ece:>7.4f} {brier:>7.4f}")
112	
113	        probe_path = os.path.join(args.output_dir, f"probe_layer{li}.pkl")
114	        with open(probe_path, "wb") as f:
115	            pickle.dump({"scaler": scaler, "model": clf}, f)
116	
117	        results.append({
118	            "layer": li,
119	            "n_train": len(y_train),
120	            "n_test": len(y_test),
121	            "auroc": auroc,
122	            "ece": ece,
123	            "brier": brier,
124	            "probe_path": probe_path,
125	        })
126	
127	    csv_path = os.path.join(args.output_dir, "train_metrics.csv")
128	    with open(csv_path, "w") as f:
129	        f.write("layer,n_train,n_test,auroc,ece,brier\n")
130	        for r in results:
131	            f.write(f"{r['layer']},{r['n_train']},{r['n_test']},{r['auroc']:.6f},{r['ece']:.6f},{r['brier']:.6f}\n")
132	    print(f"\nMetrics saved to {csv_path}")
133	    print(f"Probes saved to {args.output_dir}/")
134	
135	
136	if __name__ == "__main__":
137	    main()
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "40d3f6ae-efe6-4bf2-89bf-d4f13d6bc430",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/train_probe.py",
      "content": "\"\"\"\nTrain per-layer correctness probes (logistic regression) on English activations.\n\nFor each layer, trains an L2-regularized LogisticRegression on 80% of the\nEnglish data and evaluates on the held-out 20%. Reports AUROC, ECE, Brier score.\n\nInput:  .pt files from extract_activations.py  (e.g. activations/layer8_en.pt)\nOutput: probe pickle files + train_metrics.csv\n\nUsage:\n  python train_probe.py \\\n    --activations_dir ./activations \\\n    --output_dir ./probes \\\n    --layers 0,4,8,12,16,20,24,28,31\n\"\"\"\n\nimport argparse\nimport os\nimport pickle\n\nimport numpy as np\nimport torch\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import roc_auc_score, brier_score_loss\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--activations_dir\", default=\"./activations\")\n    p.add_argument(\"--output_dir\", default=\"./probes\")\n    p.add_argument(\"--layers\", default=None,\n                   help=\"Comma-separated layer indices. Default: auto-detect from activations_dir\")\n    p.add_argument(\"--test_size\", type=float, default=0.2)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--C\", type=float, default=1.0, help=\"Inverse regularization strength\")\n    p.add_argument(\"--max_iter\", type=int, default=2000)\n    return p.parse_args()\n\n\ndef compute_ece(probs, labels, n_bins=10):\n    \"\"\"Histogram-based Expected Calibration Error (10 equal-width bins).\"\"\"\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):\n        mask = (probs > lo) & (probs <= hi)\n        if lo == 0.0:\n            mask = (probs >= lo) & (probs <= hi)\n        n_in_bin = mask.sum()\n        if n_in_bin == 0:\n            continue\n        avg_conf = probs[mask].mean()\n        avg_acc = labels[mask].mean()\n        ece += (n_in_bin / len(probs)) * abs(avg_acc - avg_conf)\n    return ece\n\n\ndef main():\n    args = parse_args()\n    if args.layers is None:\n        import glob\n        available = sorted(set(\n            int(os.path.basename(f).split('_')[0].replace('layer', ''))\n            for f in glob.glob(os.path.join(args.activations_dir, 'layer*_en.pt'))\n        ))\n        if not available:\n            raise RuntimeError(f\"No layer*_en.pt files found in {args.activations_dir}\")\n        print(f\"Auto-detected layers: {available}\")\n        layer_indices = available\n    else:\n        layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    results = []\n    print(f\"{'Layer':>5s} {'N_train':>7s} {'N_test':>6s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s}\")\n    print(\"-\" * 46)\n\n    for li in layer_indices:\n        pt_path = os.path.join(args.activations_dir, f\"layer{li}_en.pt\")\n        if not os.path.exists(pt_path):\n            print(f\"  [SKIP] {pt_path} not found\")\n            continue\n\n        data = torch.load(pt_path, weights_only=True)\n        X = data[\"activations\"].numpy()\n        y = data[\"labels\"].numpy()\n\n        if len(np.unique(y)) < 2:\n            print(f\"  [SKIP] Layer {li}: only one class present (all correct or all wrong)\")\n            continue\n\n        X_train, X_test, y_train, y_test = train_test_split(\n            X, y, test_size=args.test_size, random_state=args.seed, stratify=y,\n        )\n\n        scaler = StandardScaler()\n        X_train_s = scaler.fit_transform(X_train)\n        X_test_s = scaler.transform(X_test)\n\n        clf = LogisticRegression(\n            C=args.C, penalty=\"l2\", solver=\"lbfgs\", max_iter=args.max_iter, random_state=args.seed,\n        )\n        clf.fit(X_train_s, y_train)\n\n        probs = clf.predict_proba(X_test_s)[:, 1]\n        auroc = roc_auc_score(y_test, probs)\n        ece = compute_ece(probs, y_test)\n        brier = brier_score_loss(y_test, probs)\n\n        print(f\"{li:>5d} {len(y_train):>7d} {len(y_test):>6d} {auroc:>7.4f} {ece:>7.4f} {brier:>7.4f}\")\n\n        probe_path = os.path.join(args.output_dir, f\"probe_layer{li}.pkl\")\n        with open(probe_path, \"wb\") as f:\n            pickle.dump({\"scaler\": scaler, \"model\": clf}, f)\n\n        results.append({\n            \"layer\": li,\n            \"n_train\": len(y_train),\n            \"n_test\": len(y_test),\n            \"auroc\": auroc,\n            \"ece\": ece,\n            \"brier\": brier,\n            \"probe_path\": probe_path,\n        })\n\n    csv_path = os.path.join(args.output_dir, \"train_metrics.csv\")\n    with open(csv_path, \"w\") as f:\n        f.write(\"layer,n_train,n_test,auroc,ece,brier\\n\")\n        for r in results:\n            f.write(f\"{r['layer']},{r['n_train']},{r['n_test']},{r['auroc']:.6f},{r['ece']:.6f},{r['brier']:.6f}\\n\")\n    print(f\"\\nMetrics saved to {csv_path}\")\n    print(f\"Probes saved to {args.output_dir}/\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 138,
      "startLine": 1,
      "totalLines": 138
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01XEz5z8jEsVQEJANTY2CtAk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/transfer_eval.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "fb892352-112c-45d6-b8f8-bdaa616e5fe3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CSyz7Z7vgWXJMDFPB1ebX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13249,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13249
      },
      "output_tokens": 25,
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

_source line 9 · 2026-05-20T21:46:51.070Z_

<details><summary>↩ Tool result · `toolu_01XEz5z8jEsVQEJANTY2CtAk`</summary>

```text
1	"""
2	Evaluate cross-lingual transfer of English correctness probes.
3	
4	Two transfer conditions:
5	  (a) Zero-shot: apply English probe directly to target-language activations
6	  (b) Mean-shift: shift target activations by (mean_en - mean_tgt) before probing
7	
8	Input:  English probes (.pkl) + per-language activations (.pt)
9	Output: transfer_results.csv with AUROC / ECE / Brier per (layer, language, method)
10	
11	Usage:
12	  python transfer_eval.py \
13	    --activations_dir ./activations \
14	    --probes_dir ./probes \
15	    --output_dir ./results \
16	    --layers 0,4,8,12,16,20,24,28,31 \
17	    --languages zh ar hi sw ko
18	"""
19	
20	import argparse
21	import os
22	import pickle
23	
24	import numpy as np
25	import torch
26	from sklearn.metrics import roc_auc_score, brier_score_loss
27	
28	
29	def parse_args():
30	    p = argparse.ArgumentParser()
31	    p.add_argument("--activations_dir", default="./activations")
32	    p.add_argument("--probes_dir", default="./probes")
33	    p.add_argument("--output_dir", default="./results")
34	    p.add_argument("--layers", default=None,
35	                   help="Comma-separated layer indices. Default: auto-detect from activations_dir")
36	    p.add_argument("--languages", nargs="+", default=["zh", "ar", "hi", "sw", "ko"])
37	    p.add_argument("--n_perm", type=int, default=1000,
38	                   help="Number of permutations for significance test")
39	    return p.parse_args()
40	
41	
42	def compute_ece(probs, labels, n_bins=10):
43	    """Histogram-based ECE."""
44	    bin_edges = np.linspace(0, 1, n_bins + 1)
45	    ece = 0.0
46	    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
47	        mask = (probs > lo) & (probs <= hi)
48	        if lo == 0.0:
49	            mask = (probs >= lo) & (probs <= hi)
50	        n_in_bin = mask.sum()
51	        if n_in_bin == 0:
52	            continue
53	        ece += (n_in_bin / len(probs)) * abs(labels[mask].mean() - probs[mask].mean())
54	    return ece
55	
56	
57	def permutation_test_auroc(y_true, y_score, n_perm=1000, seed=42):
58	    """One-sided permutation test: is AUROC significantly above chance?"""
59	    rng = np.random.RandomState(seed)
60	    real_auroc = roc_auc_score(y_true, y_score)
61	    count_ge = 0
62	    for _ in range(n_perm):
63	        perm_auroc = roc_auc_score(rng.permutation(y_true), y_score)
64	        if perm_auroc >= real_auroc:
65	            count_ge += 1
66	    return (count_ge + 1) / (n_perm + 1)
67	
68	
69	def evaluate_probe(probe, scaler, X, y, n_perm=1000):
70	    """Apply probe and compute metrics. Returns (auroc, ece, brier, p_value, probs)."""
71	    X_s = scaler.transform(X)
72	    probs = probe.predict_proba(X_s)[:, 1]
73	    logits = probe.decision_function(X_s)
74	
75	    if len(np.unique(y)) < 2:
76	        return None, None, None, None, probs
77	
78	    auroc = roc_auc_score(y, logits)
79	    ece = compute_ece(probs, y)
80	    brier = brier_score_loss(y, probs)
81	    p_value = permutation_test_auroc(y, logits, n_perm=n_perm)
82	    return auroc, ece, brier, p_value, probs
83	
84	
85	def main():
86	    args = parse_args()
87	    if args.layers is None:
88	        import glob
89	        available = sorted(set(
90	            int(os.path.basename(f).split('_')[0].replace('layer', ''))
91	            for f in glob.glob(os.path.join(args.activations_dir, 'layer*_en.pt'))
92	        ))
93	        if not available:
94	            raise RuntimeError(f"No layer*_en.pt files found in {args.activations_dir}")
95	        print(f"Auto-detected layers: {available}")
96	        layer_indices = available
97	    else:
98	        layer_indices = sorted(int(x) for x in args.layers.split(","))
99	    os.makedirs(args.output_dir, exist_ok=True)
100	
101	    results = []
102	
103	    def _fmt(v):
104	        return f"{v:.4f}" if v is not None else "  N/A "
105	
106	    print(f"{'Layer':>5s} {'Lang':>4s} {'Method':>10s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s} {'p':>7s} {'N':>6s}")
107	    print("-" * 60)
108	
109	    for li in layer_indices:
110	        probe_path = os.path.join(args.probes_dir, f"probe_layer{li}.pkl")
111	        if not os.path.exists(probe_path):
112	            print(f"  [SKIP] No probe for layer {li}")
113	            continue
114	
115	        with open(probe_path, "rb") as f:
116	            saved = pickle.load(f)
117	        probe = saved["model"]
118	        scaler = saved["scaler"]
119	
120	        en_pt = os.path.join(args.activations_dir, f"layer{li}_en.pt")
121	        if not os.path.exists(en_pt):
122	            print(f"  [SKIP] No English activations for layer {li}")
123	            continue
124	        en_data = torch.load(en_pt, weights_only=True)
125	        en_mean = en_data["activations"].numpy().mean(axis=0)
126	
127	        for lang in args.languages:
128	            tgt_pt = os.path.join(args.activations_dir, f"layer{li}_{lang}.pt")
129	            if not os.path.exists(tgt_pt):
130	                print(f"  [SKIP] No activations for layer {li}, lang {lang}")
131	                continue
132	
133	            tgt_data = torch.load(tgt_pt, weights_only=True)
134	            X_tgt = tgt_data["activations"].numpy()
135	            y_tgt = tgt_data["labels"].numpy()
136	            n_samples = len(y_tgt)
137	
138	            # (a) Zero-shot
139	            auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_tgt, y_tgt, n_perm=args.n_perm)
140	            row = {"layer": li, "language": lang, "method": "zero_shot",
141	                   "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_samples}
142	            results.append(row)
143	            print(f"{li:>5d} {lang:>4s} {'zero_shot':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}")
144	
145	            # (b) Mean-shift: X_shifted = X_tgt - (mean_tgt - mean_en)
146	            tgt_mean = X_tgt.mean(axis=0)
147	            X_shifted = X_tgt - (tgt_mean - en_mean)
148	            auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_shifted, y_tgt, n_perm=args.n_perm)
149	            row = {"layer": li, "language": lang, "method": "mean_shift",
150	                   "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_samples}
151	            results.append(row)
152	            print(f"{li:>5d} {lang:>4s} {'mean_shift':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}")
153	
154	    csv_path = os.path.join(args.output_dir, "transfer_results.csv")
155	    with open(csv_path, "w") as f:
156	        f.write("layer,language,method,auroc,ece,brier,p_value,n\n")
157	        for r in results:
158	            vals = []
159	            for k in ["auroc", "ece", "brier", "p_value"]:
160	                vals.append(f"{r[k]:.6f}" if r[k] is not None else "")
161	            f.write(f"{r['layer']},{r['language']},{r['method']},{','.join(vals)},{r['n']}\n")
162	
163	    print(f"\nResults saved to {csv_path}")
164	
165	
166	if __name__ == "__main__":
167	    main()
168	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "09226e54-f0f0-4d27-a025-40fa0785381d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/transfer_eval.py",
      "content": "\"\"\"\nEvaluate cross-lingual transfer of English correctness probes.\n\nTwo transfer conditions:\n  (a) Zero-shot: apply English probe directly to target-language activations\n  (b) Mean-shift: shift target activations by (mean_en - mean_tgt) before probing\n\nInput:  English probes (.pkl) + per-language activations (.pt)\nOutput: transfer_results.csv with AUROC / ECE / Brier per (layer, language, method)\n\nUsage:\n  python transfer_eval.py \\\n    --activations_dir ./activations \\\n    --probes_dir ./probes \\\n    --output_dir ./results \\\n    --layers 0,4,8,12,16,20,24,28,31 \\\n    --languages zh ar hi sw ko\n\"\"\"\n\nimport argparse\nimport os\nimport pickle\n\nimport numpy as np\nimport torch\nfrom sklearn.metrics import roc_auc_score, brier_score_loss\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--activations_dir\", default=\"./activations\")\n    p.add_argument(\"--probes_dir\", default=\"./probes\")\n    p.add_argument(\"--output_dir\", default=\"./results\")\n    p.add_argument(\"--layers\", default=None,\n                   help=\"Comma-separated layer indices. Default: auto-detect from activations_dir\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"zh\", \"ar\", \"hi\", \"sw\", \"ko\"])\n    p.add_argument(\"--n_perm\", type=int, default=1000,\n                   help=\"Number of permutations for significance test\")\n    return p.parse_args()\n\n\ndef compute_ece(probs, labels, n_bins=10):\n    \"\"\"Histogram-based ECE.\"\"\"\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):\n        mask = (probs > lo) & (probs <= hi)\n        if lo == 0.0:\n            mask = (probs >= lo) & (probs <= hi)\n        n_in_bin = mask.sum()\n        if n_in_bin == 0:\n            continue\n        ece += (n_in_bin / len(probs)) * abs(labels[mask].mean() - probs[mask].mean())\n    return ece\n\n\ndef permutation_test_auroc(y_true, y_score, n_perm=1000, seed=42):\n    \"\"\"One-sided permutation test: is AUROC significantly above chance?\"\"\"\n    rng = np.random.RandomState(seed)\n    real_auroc = roc_auc_score(y_true, y_score)\n    count_ge = 0\n    for _ in range(n_perm):\n        perm_auroc = roc_auc_score(rng.permutation(y_true), y_score)\n        if perm_auroc >= real_auroc:\n            count_ge += 1\n    return (count_ge + 1) / (n_perm + 1)\n\n\ndef evaluate_probe(probe, scaler, X, y, n_perm=1000):\n    \"\"\"Apply probe and compute metrics. Returns (auroc, ece, brier, p_value, probs).\"\"\"\n    X_s = scaler.transform(X)\n    probs = probe.predict_proba(X_s)[:, 1]\n    logits = probe.decision_function(X_s)\n\n    if len(np.unique(y)) < 2:\n        return None, None, None, None, probs\n\n    auroc = roc_auc_score(y, logits)\n    ece = compute_ece(probs, y)\n    brier = brier_score_loss(y, probs)\n    p_value = permutation_test_auroc(y, logits, n_perm=n_perm)\n    return auroc, ece, brier, p_value, probs\n\n\ndef main():\n    args = parse_args()\n    if args.layers is None:\n        import glob\n        available = sorted(set(\n            int(os.path.basename(f).split('_')[0].replace('layer', ''))\n            for f in glob.glob(os.path.join(args.activations_dir, 'layer*_en.pt'))\n        ))\n        if not available:\n            raise RuntimeError(f\"No layer*_en.pt files found in {args.activations_dir}\")\n        print(f\"Auto-detected layers: {available}\")\n        layer_indices = available\n    else:\n        layer_indices = sorted(int(x) for x in args.layers.split(\",\"))\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    results = []\n\n    def _fmt(v):\n        return f\"{v:.4f}\" if v is not None else \"  N/A \"\n\n    print(f\"{'Layer':>5s} {'Lang':>4s} {'Method':>10s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s} {'p':>7s} {'N':>6s}\")\n    print(\"-\" * 60)\n\n    for li in layer_indices:\n        probe_path = os.path.join(args.probes_dir, f\"probe_layer{li}.pkl\")\n        if not os.path.exists(probe_path):\n            print(f\"  [SKIP] No probe for layer {li}\")\n            continue\n\n        with open(probe_path, \"rb\") as f:\n            saved = pickle.load(f)\n        probe = saved[\"model\"]\n        scaler = saved[\"scaler\"]\n\n        en_pt = os.path.join(args.activations_dir, f\"layer{li}_en.pt\")\n        if not os.path.exists(en_pt):\n            print(f\"  [SKIP] No English activations for layer {li}\")\n            continue\n        en_data = torch.load(en_pt, weights_only=True)\n        en_mean = en_data[\"activations\"].numpy().mean(axis=0)\n\n        for lang in args.languages:\n            tgt_pt = os.path.join(args.activations_dir, f\"layer{li}_{lang}.pt\")\n            if not os.path.exists(tgt_pt):\n                print(f\"  [SKIP] No activations for layer {li}, lang {lang}\")\n                continue\n\n            tgt_data = torch.load(tgt_pt, weights_only=True)\n            X_tgt = tgt_data[\"activations\"].numpy()\n            y_tgt = tgt_data[\"labels\"].numpy()\n            n_samples = len(y_tgt)\n\n            # (a) Zero-shot\n            auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_tgt, y_tgt, n_perm=args.n_perm)\n            row = {\"layer\": li, \"language\": lang, \"method\": \"zero_shot\",\n                   \"auroc\": auroc, \"ece\": ece, \"brier\": brier, \"p_value\": pval, \"n\": n_samples}\n            results.append(row)\n            print(f\"{li:>5d} {lang:>4s} {'zero_shot':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}\")\n\n            # (b) Mean-shift: X_shifted = X_tgt - (mean_tgt - mean_en)\n            tgt_mean = X_tgt.mean(axis=0)\n            X_shifted = X_tgt - (tgt_mean - en_mean)\n            auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_shifted, y_tgt, n_perm=args.n_perm)\n            row = {\"layer\": li, \"language\": lang, \"method\": \"mean_shift\",\n                   \"auroc\": auroc, \"ece\": ece, \"brier\": brier, \"p_value\": pval, \"n\": n_samples}\n            results.append(row)\n            print(f\"{li:>5d} {lang:>4s} {'mean_shift':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}\")\n\n    csv_path = os.path.join(args.output_dir, \"transfer_results.csv\")\n    with open(csv_path, \"w\") as f:\n        f.write(\"layer,language,method,auroc,ece,brier,p_value,n\\n\")\n        for r in results:\n            vals = []\n            for k in [\"auroc\", \"ece\", \"brier\", \"p_value\"]:\n                vals.append(f\"{r[k]:.6f}\" if r[k] is not None else \"\")\n            f.write(f\"{r['layer']},{r['language']},{r['method']},{','.join(vals)},{r['n']}\\n\")\n\n    print(f\"\\nResults saved to {csv_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 168,
      "startLine": 1,
      "totalLines": 168
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of:

1. `train_probe.py` - saves probes as `{"scaler": scaler, "model": clf}` pickle files. The model is sklearn LogisticRegression.
2. `transfer_eval.py` - loads probes, uses `probe.predict_proba(X_s)[:, 1]` and `probe.decision_function(X_s)` for evaluation.

Key compatibility requirements:
- CaCLRProbe needs `predict_proba()` returning a 2D array (columns for class 0 and class 1)


- CaCLRProbe also needs `decision_function()` returning logits
- Save format: `{"scaler": scaler, "model": probe}`
- Activations are loaded as `.pt` files with `{"activations": tensor, "labels": tensor}`

Writing train_caclr.py...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "ef993390-3ac8-4012-80cb-fc7d720cc630",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTzhSRD6Qn9tXndqWhB9Ps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5005,
      "cache_read_input_tokens": 25090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5005
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

_source line 11_

关键兼容性要点：
- probe pickle 格式：`{"scaler": scaler, "model": clf}`
- `evaluate_probe` 调用 `probe.predict_proba(X_s)[:, 1]`（需返回 2D array）和 `probe.decision_function(X_s)`
- activations `.pt` 格式：`{"activations": tensor, "labels": tensor}`

开始编写 `train_caclr.py`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "bcd12d49-5875-423d-8a97-6f88924c0474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTzhSRD6Qn9tXndqWhB9Ps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5005,
      "cache_read_input_tokens": 25090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5005
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

_source line 12_

<details open><summary>🔧 Tool call — Write · `toolu_013YvqX6k26RSknmE6SfZpWM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/train_caclr.py",
  "content": "\"\"\"\nCaCLR: Calibration-aware Cross-Lingual Regularization.\n\nTrain a linear probe with two additional regularization terms beyond BCE:\n  Loss = L_BCE + α · L_SB-ECE + β · L_consistency(MMD)\n\n  - L_SB-ECE: differentiable soft-binning ECE (calibration regularizer)\n  - L_consistency: MMD with Gaussian RBF kernel (cross-lingual consistency)\n\nInput:  per-language activation .pt files from extract_activations.py\n        (each file has {\"activations\": Tensor, \"labels\": Tensor})\nOutput: trained probe .pkl compatible with transfer_eval.py\n        (pickle dict with {\"model\": CaCLRProbe, \"scaler\": StandardScaler, ...})\n\nUsage:\n  # Single run\n  python train_caclr.py \\\n    --activations_dir ./activations --output_dir ./probes_caclr \\\n    --layer 16 --languages zh ar hi sw ko --alpha 1.0 --beta 0.1\n\n  # Sweep over α × β\n  python train_caclr.py \\\n    --activations_dir ./activations --output_dir ./probes_caclr \\\n    --layer 16 --languages zh ar hi sw ko \\\n    --alpha_sweep 0.01,0.1,0.5,1.0,2.0,5.0,10.0 \\\n    --beta_sweep 0.001,0.01,0.05,0.1,0.5,1.0\n\"\"\"\n\nimport argparse\nimport os\nimport pickle\nfrom itertools import product\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import roc_auc_score, brier_score_loss\n\n\n# ---------------------------------------------------------------------------\n# Loss components\n# ---------------------------------------------------------------------------\n\ndef bce_loss(logits, labels):\n    \"\"\"Standard binary cross-entropy on probe logits.\"\"\"\n    return F.binary_cross_entropy_with_logits(logits, labels)\n\n\ndef sb_ece_loss(probs, labels, n_bins=10, temperature=0.05):\n    \"\"\"Differentiable soft-binning ECE approximation.\n\n    Hard-histogram ECE is non-differentiable. We replace indicator-based bin\n    assignment with Gaussian soft assignment:\n      bin centers c_k = (k + 0.5) / n_bins,  k = 0, ..., n_bins-1\n      weights  w_{ik} = softmax( -|p_i - c_k|^2 / temperature )\n\n    Per-bin calibration error:\n      CE_k = | Σ_i w_{ik} * (label_i - p_i) | / (Σ_i w_{ik} + ε)\n\n    SB-ECE = Σ_k (Σ_i w_{ik} / N) * CE_k\n    \"\"\"\n    centers = torch.linspace(0.5 / n_bins, 1.0 - 0.5 / n_bins, n_bins,\n                             device=probs.device)                          # (K,)\n    # Pairwise distances: (N, K)\n    dists = (probs.unsqueeze(1) - centers.unsqueeze(0)) ** 2               # (N, K)\n    weights = F.softmax(-dists / temperature, dim=1)                       # (N, K)\n\n    bin_counts = weights.sum(dim=0)                                        # (K,)\n    # Weighted calibration gap per bin\n    gap = labels.unsqueeze(1) - probs.unsqueeze(1)                         # (N, K) broadcast\n    weighted_gap = (weights * gap).sum(dim=0)                              # (K,)\n    per_bin_ce = weighted_gap.abs() / (bin_counts + 1e-8)\n\n    ece = (bin_counts / probs.shape[0] * per_bin_ce).sum()\n    return ece\n\n\ndef gaussian_rbf_kernel(x, y, bandwidth=None):\n    \"\"\"Gaussian RBF kernel matrix.\n\n    k(x, y) = exp( -||x - y||^2 / (2 * bandwidth^2) )\n\n    If bandwidth is None, uses the median heuristic:\n      bandwidth = sqrt( median(||x_i - y_j||^2) / 2 )\n    \"\"\"\n    xx = torch.cdist(x, x) ** 2    # (N, N)\n    yy = torch.cdist(y, y) ** 2    # (M, M)\n    xy = torch.cdist(x, y) ** 2    # (N, M)\n\n    if bandwidth is None:\n        # Median heuristic over cross-distances\n        all_dists = xy.detach().reshape(-1)\n        median_dist = all_dists.median()\n        bandwidth = torch.sqrt(median_dist / 2.0).clamp(min=1e-5)\n\n    gamma = 1.0 / (2.0 * bandwidth ** 2)\n    K_xx = torch.exp(-gamma * xx)\n    K_yy = torch.exp(-gamma * yy)\n    K_xy = torch.exp(-gamma * xy)\n    return K_xx, K_yy, K_xy, bandwidth\n\n\ndef mmd_loss(x_en, x_tgt, bandwidth=None):\n    \"\"\"Unbiased estimate of MMD^2 between English and target representations.\n\n    MMD^2 = E[k(x,x')] + E[k(y,y')] - 2·E[k(x,y)]\n\n    where k is a Gaussian RBF kernel with median heuristic bandwidth.\n    \"\"\"\n    K_xx, K_yy, K_xy, bw = gaussian_rbf_kernel(x_en, x_tgt, bandwidth)\n    n = K_xx.shape[0]\n    m = K_yy.shape[0]\n\n    # Unbiased: zero out diagonal for self-terms\n    sum_xx = (K_xx.sum() - K_xx.diagonal().sum()) / (n * (n - 1)) if n > 1 else K_xx.mean()\n    sum_yy = (K_yy.sum() - K_yy.diagonal().sum()) / (m * (m - 1)) if m > 1 else K_yy.mean()\n    sum_xy = K_xy.mean()\n\n    return sum_xx + sum_yy - 2.0 * sum_xy\n\n\n# ---------------------------------------------------------------------------\n# CaCLR Probe model\n# ---------------------------------------------------------------------------\n\nclass CaCLRProbe(nn.Module):\n    \"\"\"Linear probe with CaCLR regularization.\n\n    Functionally equivalent to sklearn LogisticRegression (single Linear layer),\n    but trained with gradient descent plus L_SB-ECE and L_MMD regularizers.\n\n    Exposes predict_proba() and decision_function() for compatibility with\n    transfer_eval.py's evaluate_probe().\n    \"\"\"\n\n    def __init__(self, input_dim, l2_weight=1.0):\n        super().__init__()\n        self.linear = nn.Linear(input_dim, 1)\n        self.l2_weight = l2_weight\n\n    def forward(self, x):\n        \"\"\"Return raw logits (N,).\"\"\"\n        return self.linear(x).squeeze(-1)\n\n    def predict_proba(self, x):\n        \"\"\"Return (N, 2) numpy array of [P(class=0), P(class=1)].\n\n        Accepts numpy array or torch Tensor. Returns numpy for sklearn compat.\n        \"\"\"\n        if isinstance(x, np.ndarray):\n            x = torch.from_numpy(x).float().to(self.linear.weight.device)\n        with torch.no_grad():\n            p1 = torch.sigmoid(self.forward(x)).cpu().numpy()\n        return np.column_stack([1 - p1, p1])\n\n    def decision_function(self, x):\n        \"\"\"Return logits as 1-D numpy array (sklearn compat).\"\"\"\n        if isinstance(x, np.ndarray):\n            x = torch.from_numpy(x).float().to(self.linear.weight.device)\n        with torch.no_grad():\n            return self.forward(x).cpu().numpy()\n\n    def l2_reg(self):\n        \"\"\"L2 penalty on weights (not bias), matching sklearn C = 1/l2_weight.\"\"\"\n        return self.l2_weight * (self.linear.weight ** 2).sum()\n\n    @classmethod\n    def from_sklearn(cls, sklearn_probe, scaler, l2_weight=1.0):\n        \"\"\"Initialize from a trained sklearn LogisticRegression + StandardScaler.\n\n        Copies weight and bias so CaCLR starts from the converged LR solution.\n        The scaler is applied externally (same as sklearn pipeline), so we only\n        need the LR parameters here.\n        \"\"\"\n        input_dim = sklearn_probe.coef_.shape[1]\n        model = cls(input_dim, l2_weight=l2_weight)\n        with torch.no_grad():\n            model.linear.weight.copy_(torch.from_numpy(sklearn_probe.coef_).float())\n            model.linear.bias.copy_(torch.from_numpy(sklearn_probe.intercept_).float())\n        return model\n\n\n# ---------------------------------------------------------------------------\n# Training loop\n# ---------------------------------------------------------------------------\n\ndef train_caclr(\n    X_en, y_en,\n    X_tgt_dict,\n    alpha=1.0,\n    beta=0.1,\n    lr=1e-3,\n    epochs=100,\n    l2_weight=1.0,\n    init_from_sklearn=True,\n    seed=42,\n    verbose=True,\n):\n    \"\"\"Train CaCLR probe.\n\n    Steps:\n      1. Fit StandardScaler on English data.\n      2. Train standard LogisticRegression on English (sklearn).\n      3. Initialize CaCLRProbe from LR weights.\n      4. Fine-tune with L_BCE + α·L_SB-ECE + β·L_MMD.\n\n    Args:\n        X_en: (N_en, D) numpy array of English activations.\n        y_en: (N_en,) numpy array of binary labels.\n        X_tgt_dict: {lang: (X_tgt, y_tgt)} numpy arrays for target languages.\n        alpha: weight on SB-ECE calibration loss.\n        beta: weight on MMD consistency loss.\n        lr: learning rate for Adam optimizer.\n        epochs: number of training epochs.\n        l2_weight: L2 regularization weight (sklearn C = 1/l2_weight).\n        init_from_sklearn: if True, warm-start from sklearn LR solution.\n        seed: random seed.\n        verbose: print training progress.\n\n    Returns:\n        probe: trained CaCLRProbe (on CPU).\n        scaler: fitted StandardScaler.\n        history: dict with keys \"total\", \"bce\", \"sb_ece\", \"mmd\" (lists of per-epoch losses).\n    \"\"\"\n    torch.manual_seed(seed)\n    np.random.seed(seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n\n    # 1. Fit scaler on English data\n    scaler = StandardScaler()\n    X_en_s = scaler.fit_transform(X_en)\n\n    # 2. Train sklearn LR as initialization\n    sklearn_C = 1.0 / l2_weight if l2_weight > 0 else 1e6\n    sklearn_lr = LogisticRegression(\n        C=sklearn_C, penalty=\"l2\", solver=\"lbfgs\", max_iter=2000, random_state=seed,\n    )\n    sklearn_lr.fit(X_en_s, y_en)\n\n    # 3. Initialize CaCLRProbe\n    if init_from_sklearn:\n        probe = CaCLRProbe.from_sklearn(sklearn_lr, scaler, l2_weight=l2_weight)\n    else:\n        probe = CaCLRProbe(X_en_s.shape[1], l2_weight=l2_weight)\n    probe = probe.to(device)\n\n    # Convert data to tensors\n    X_en_t = torch.from_numpy(X_en_s).float().to(device)\n    y_en_t = torch.from_numpy(y_en.astype(np.float32)).to(device)\n\n    tgt_tensors = {}\n    for lang, (X_tgt, y_tgt) in X_tgt_dict.items():\n        X_tgt_s = scaler.transform(X_tgt)\n        tgt_tensors[lang] = (\n            torch.from_numpy(X_tgt_s).float().to(device),\n            torch.from_numpy(y_tgt.astype(np.float32)).to(device),\n        )\n\n    # 4. Fine-tune with CaCLR loss\n    optimizer = torch.optim.Adam(probe.parameters(), lr=lr)\n    history = {\"total\": [], \"bce\": [], \"sb_ece\": [], \"mmd\": [], \"l2\": []}\n\n    for epoch in range(epochs):\n        probe.train()\n        optimizer.zero_grad()\n\n        logits_en = probe(X_en_t)\n        probs_en = torch.sigmoid(logits_en)\n\n        loss_bce = bce_loss(logits_en, y_en_t)\n        loss_sb_ece = sb_ece_loss(probs_en, y_en_t)\n        loss_l2 = probe.l2_reg()\n\n        # MMD: average over all target languages\n        loss_mmd = torch.tensor(0.0, device=device)\n        if beta > 0 and len(tgt_tensors) > 0:\n            # Use hidden representation (pre-sigmoid) for MMD\n            # Since it's a single linear layer, the representation IS the input,\n            # so we compare scaled activations directly.\n            mmd_terms = []\n            for lang, (X_tgt_t, _) in tgt_tensors.items():\n                # Subsample for efficiency if datasets are large\n                n_sub = min(512, X_en_t.shape[0], X_tgt_t.shape[0])\n                idx_en = torch.randperm(X_en_t.shape[0], device=device)[:n_sub]\n                idx_tgt = torch.randperm(X_tgt_t.shape[0], device=device)[:n_sub]\n                mmd_terms.append(mmd_loss(X_en_t[idx_en], X_tgt_t[idx_tgt]))\n            loss_mmd = torch.stack(mmd_terms).mean()\n\n        total = loss_bce + alpha * loss_sb_ece + beta * loss_mmd + loss_l2\n        total.backward()\n        optimizer.step()\n\n        history[\"total\"].append(total.item())\n        history[\"bce\"].append(loss_bce.item())\n        history[\"sb_ece\"].append(loss_sb_ece.item())\n        history[\"mmd\"].append(loss_mmd.item())\n        history[\"l2\"].append(loss_l2.item())\n\n        if verbose and (epoch + 1) % max(1, epochs // 10) == 0:\n            print(f\"  epoch {epoch+1:>4d}/{epochs}  \"\n                  f\"total={total.item():.4f}  bce={loss_bce.item():.4f}  \"\n                  f\"sb_ece={loss_sb_ece.item():.4f}  mmd={loss_mmd.item():.4f}\")\n\n    probe = probe.cpu().eval()\n    return probe, scaler, history\n\n\n# ---------------------------------------------------------------------------\n# Evaluation helper (quick validation during sweep)\n# ---------------------------------------------------------------------------\n\ndef compute_ece(probs, labels, n_bins=10):\n    \"\"\"Histogram-based ECE (numpy, matches train_probe.py).\"\"\"\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):\n        mask = (probs > lo) & (probs <= hi)\n        if lo == 0.0:\n            mask = (probs >= lo) & (probs <= hi)\n        n_in_bin = mask.sum()\n        if n_in_bin == 0:\n            continue\n        ece += (n_in_bin / len(probs)) * abs(labels[mask].mean() - probs[mask].mean())\n    return ece\n\n\ndef quick_eval(probe, scaler, X, y):\n    \"\"\"AUROC + ECE + Brier on held-out data.\"\"\"\n    X_s = scaler.transform(X)\n    probs = probe.predict_proba(X_s)[:, 1]\n    logits = probe.decision_function(X_s)\n    if len(np.unique(y)) < 2:\n        return None, None, None\n    return roc_auc_score(y, logits), compute_ece(probs, y), brier_score_loss(y, probs)\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"CaCLR probe training\")\n    p.add_argument(\"--activations_dir\", default=\"./activations\")\n    p.add_argument(\"--output_dir\", default=\"./probes_caclr\")\n    p.add_argument(\"--layer\", type=int, required=True,\n                   help=\"Layer index to train on\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"zh\", \"ar\", \"hi\", \"sw\", \"ko\"],\n                   help=\"Target languages for MMD consistency loss\")\n    p.add_argument(\"--alpha\", type=float, default=1.0,\n                   help=\"SB-ECE calibration loss weight\")\n    p.add_argument(\"--beta\", type=float, default=0.1,\n                   help=\"MMD consistency loss weight\")\n    p.add_argument(\"--alpha_sweep\", type=str, default=None,\n                   help=\"Comma-separated alpha values for grid search \"\n                        \"(e.g., '0.01,0.1,1.0,10.0')\")\n    p.add_argument(\"--beta_sweep\", type=str, default=None,\n                   help=\"Comma-separated beta values for grid search\")\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--epochs\", type=int, default=100)\n    p.add_argument(\"--l2_weight\", type=float, default=1.0)\n    p.add_argument(\"--test_size\", type=float, default=0.2,\n                   help=\"English held-out fraction for sweep selection\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    # Load English activations\n    en_path = os.path.join(args.activations_dir, f\"layer{args.layer}_en.pt\")\n    en_data = torch.load(en_path, weights_only=True)\n    X_en = en_data[\"activations\"].numpy()\n    y_en = en_data[\"labels\"].numpy()\n    print(f\"English data: {X_en.shape[0]} samples, dim={X_en.shape[1]}\")\n\n    # Load target language activations\n    X_tgt_dict = {}\n    for lang in args.languages:\n        tgt_path = os.path.join(args.activations_dir, f\"layer{args.layer}_{lang}.pt\")\n        if not os.path.exists(tgt_path):\n            print(f\"  [SKIP] {tgt_path} not found\")\n            continue\n        tgt_data = torch.load(tgt_path, weights_only=True)\n        X_tgt_dict[lang] = (tgt_data[\"activations\"].numpy(), tgt_data[\"labels\"].numpy())\n        print(f\"  {lang}: {X_tgt_dict[lang][0].shape[0]} samples\")\n\n    # Determine if sweep mode\n    sweep_mode = args.alpha_sweep is not None or args.beta_sweep is not None\n    alphas = [float(v) for v in args.alpha_sweep.split(\",\")] if args.alpha_sweep else [args.alpha]\n    betas = [float(v) for v in args.beta_sweep.split(\",\")] if args.beta_sweep else [args.beta]\n\n    if sweep_mode:\n        # Hold out English validation set for selecting best (alpha, beta)\n        X_train, X_val, y_train, y_val = train_test_split(\n            X_en, y_en, test_size=args.test_size, random_state=args.seed, stratify=y_en,\n        )\n        print(f\"\\nSweep mode: {len(alphas)} alphas × {len(betas)} betas = {len(alphas)*len(betas)} runs\")\n        print(f\"Train: {len(y_train)}, Val: {len(y_val)}\")\n        print(f\"{'alpha':>8s} {'beta':>8s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s}\")\n        print(\"-\" * 42)\n\n        best_score = -float(\"inf\")\n        best_result = None\n\n        for a, b in product(alphas, betas):\n            probe, scaler, history = train_caclr(\n                X_train, y_train, X_tgt_dict,\n                alpha=a, beta=b, lr=args.lr, epochs=args.epochs,\n                l2_weight=args.l2_weight, seed=args.seed, verbose=False,\n            )\n            auroc, ece, brier = quick_eval(probe, scaler, X_val, y_val)\n            # Selection criterion: maximize AUROC, break ties by lower ECE\n            score = (auroc or 0.0) - 0.1 * (ece or 1.0)\n            print(f\"{a:>8.3f} {b:>8.4f} {auroc or 0:>7.4f} {ece or 0:>7.4f} {brier or 0:>7.4f}\"\n                  f\"{'  *' if score > best_score else ''}\")\n\n            if score > best_score:\n                best_score = score\n                best_result = {\n                    \"probe\": probe, \"scaler\": scaler, \"alpha\": a, \"beta\": b,\n                    \"history\": history, \"val_auroc\": auroc, \"val_ece\": ece, \"val_brier\": brier,\n                }\n\n        # Retrain best on full English data\n        print(f\"\\nBest: alpha={best_result['alpha']}, beta={best_result['beta']} \"\n              f\"(val AUROC={best_result['val_auroc']:.4f}, ECE={best_result['val_ece']:.4f})\")\n        print(\"Retraining on full English data...\")\n        probe, scaler, history = train_caclr(\n            X_en, y_en, X_tgt_dict,\n            alpha=best_result[\"alpha\"], beta=best_result[\"beta\"],\n            lr=args.lr, epochs=args.epochs, l2_weight=args.l2_weight,\n            seed=args.seed, verbose=True,\n        )\n        save_dict = {\n            \"model\": probe, \"scaler\": scaler,\n            \"alpha\": best_result[\"alpha\"], \"beta\": best_result[\"beta\"],\n            \"history\": history,\n            \"sweep_best\": {\"val_auroc\": best_result[\"val_auroc\"],\n                           \"val_ece\": best_result[\"val_ece\"],\n                           \"val_brier\": best_result[\"val_brier\"]},\n        }\n    else:\n        # Single run\n        probe, scaler, history = train_caclr(\n            X_en, y_en, X_tgt_dict,\n            alpha=args.alpha, beta=args.beta, lr=args.lr, epochs=args.epochs,\n            l2_weight=args.l2_weight, seed=args.seed, verbose=True,\n        )\n        save_dict = {\n            \"model\": probe, \"scaler\": scaler,\n            \"alpha\": args.alpha, \"beta\": args.beta,\n            \"history\": history,\n        }\n\n    # Save probe (compatible with transfer_eval.py)\n    out_path = os.path.join(args.output_dir, f\"probe_layer{args.layer}.pkl\")\n    with open(out_path, \"wb\") as f:\n        pickle.dump(save_dict, f)\n    print(f\"\\nProbe saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "c1b2c20d-35b8-433f-b489-1fa486a9e05e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTzhSRD6Qn9tXndqWhB9Ps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5005,
      "cache_read_input_tokens": 25090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5005
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

_source line 13 · 2026-05-20T21:48:22.858Z_

<details><summary>↩ Tool result · `toolu_013YvqX6k26RSknmE6SfZpWM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/train_caclr.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "e98ec79c-bf7a-4fa0-aaf6-c96950e93713",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/train_caclr.py",
    "content": "\"\"\"\nCaCLR: Calibration-aware Cross-Lingual Regularization.\n\nTrain a linear probe with two additional regularization terms beyond BCE:\n  Loss = L_BCE + α · L_SB-ECE + β · L_consistency(MMD)\n\n  - L_SB-ECE: differentiable soft-binning ECE (calibration regularizer)\n  - L_consistency: MMD with Gaussian RBF kernel (cross-lingual consistency)\n\nInput:  per-language activation .pt files from extract_activations.py\n        (each file has {\"activations\": Tensor, \"labels\": Tensor})\nOutput: trained probe .pkl compatible with transfer_eval.py\n        (pickle dict with {\"model\": CaCLRProbe, \"scaler\": StandardScaler, ...})\n\nUsage:\n  # Single run\n  python train_caclr.py \\\n    --activations_dir ./activations --output_dir ./probes_caclr \\\n    --layer 16 --languages zh ar hi sw ko --alpha 1.0 --beta 0.1\n\n  # Sweep over α × β\n  python train_caclr.py \\\n    --activations_dir ./activations --output_dir ./probes_caclr \\\n    --layer 16 --languages zh ar hi sw ko \\\n    --alpha_sweep 0.01,0.1,0.5,1.0,2.0,5.0,10.0 \\\n    --beta_sweep 0.001,0.01,0.05,0.1,0.5,1.0\n\"\"\"\n\nimport argparse\nimport os\nimport pickle\nfrom itertools import product\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import roc_auc_score, brier_score_loss\n\n\n# ---------------------------------------------------------------------------\n# Loss components\n# ---------------------------------------------------------------------------\n\ndef bce_loss(logits, labels):\n    \"\"\"Standard binary cross-entropy on probe logits.\"\"\"\n    return F.binary_cross_entropy_with_logits(logits, labels)\n\n\ndef sb_ece_loss(probs, labels, n_bins=10, temperature=0.05):\n    \"\"\"Differentiable soft-binning ECE approximation.\n\n    Hard-histogram ECE is non-differentiable. We replace indicator-based bin\n    assignment with Gaussian soft assignment:\n      bin centers c_k = (k + 0.5) / n_bins,  k = 0, ..., n_bins-1\n      weights  w_{ik} = softmax( -|p_i - c_k|^2 / temperature )\n\n    Per-bin calibration error:\n      CE_k = | Σ_i w_{ik} * (label_i - p_i) | / (Σ_i w_{ik} + ε)\n\n    SB-ECE = Σ_k (Σ_i w_{ik} / N) * CE_k\n    \"\"\"\n    centers = torch.linspace(0.5 / n_bins, 1.0 - 0.5 / n_bins, n_bins,\n                             device=probs.device)                          # (K,)\n    # Pairwise distances: (N, K)\n    dists = (probs.unsqueeze(1) - centers.unsqueeze(0)) ** 2               # (N, K)\n    weights = F.softmax(-dists / temperature, dim=1)                       # (N, K)\n\n    bin_counts = weights.sum(dim=0)                                        # (K,)\n    # Weighted calibration gap per bin\n    gap = labels.unsqueeze(1) - probs.unsqueeze(1)                         # (N, K) broadcast\n    weighted_gap = (weights * gap).sum(dim=0)                              # (K,)\n    per_bin_ce = weighted_gap.abs() / (bin_counts + 1e-8)\n\n    ece = (bin_counts / probs.shape[0] * per_bin_ce).sum()\n    return ece\n\n\ndef gaussian_rbf_kernel(x, y, bandwidth=None):\n    \"\"\"Gaussian RBF kernel matrix.\n\n    k(x, y) = exp( -||x - y||^2 / (2 * bandwidth^2) )\n\n    If bandwidth is None, uses the median heuristic:\n      bandwidth = sqrt( median(||x_i - y_j||^2) / 2 )\n    \"\"\"\n    xx = torch.cdist(x, x) ** 2    # (N, N)\n    yy = torch.cdist(y, y) ** 2    # (M, M)\n    xy = torch.cdist(x, y) ** 2    # (N, M)\n\n    if bandwidth is None:\n        # Median heuristic over cross-distances\n        all_dists = xy.detach().reshape(-1)\n        median_dist = all_dists.median()\n        bandwidth = torch.sqrt(median_dist / 2.0).clamp(min=1e-5)\n\n    gamma = 1.0 / (2.0 * bandwidth ** 2)\n    K_xx = torch.exp(-gamma * xx)\n    K_yy = torch.exp(-gamma * yy)\n    K_xy = torch.exp(-gamma * xy)\n    return K_xx, K_yy, K_xy, bandwidth\n\n\ndef mmd_loss(x_en, x_tgt, bandwidth=None):\n    \"\"\"Unbiased estimate of MMD^2 between English and target representations.\n\n    MMD^2 = E[k(x,x')] + E[k(y,y')] - 2·E[k(x,y)]\n\n    where k is a Gaussian RBF kernel with median heuristic bandwidth.\n    \"\"\"\n    K_xx, K_yy, K_xy, bw = gaussian_rbf_kernel(x_en, x_tgt, bandwidth)\n    n = K_xx.shape[0]\n    m = K_yy.shape[0]\n\n    # Unbiased: zero out diagonal for self-terms\n    sum_xx = (K_xx.sum() - K_xx.diagonal().sum()) / (n * (n - 1)) if n > 1 else K_xx.mean()\n    sum_yy = (K_yy.sum() - K_yy.diagonal().sum()) / (m * (m - 1)) if m > 1 else K_yy.mean()\n    sum_xy = K_xy.mean()\n\n    return sum_xx + sum_yy - 2.0 * sum_xy\n\n\n# ---------------------------------------------------------------------------\n# CaCLR Probe model\n# ---------------------------------------------------------------------------\n\nclass CaCLRProbe(nn.Module):\n    \"\"\"Linear probe with CaCLR regularization.\n\n    Functionally equivalent to sklearn LogisticRegression (single Linear layer),\n    but trained with gradient descent plus L_SB-ECE and L_MMD regularizers.\n\n    Exposes predict_proba() and decision_function() for compatibility with\n    transfer_eval.py's evaluate_probe().\n    \"\"\"\n\n    def __init__(self, input_dim, l2_weight=1.0):\n        super().__init__()\n        self.linear = nn.Linear(input_dim, 1)\n        self.l2_weight = l2_weight\n\n    def forward(self, x):\n        \"\"\"Return raw logits (N,).\"\"\"\n        return self.linear(x).squeeze(-1)\n\n    def predict_proba(self, x):\n        \"\"\"Return (N, 2) numpy array of [P(class=0), P(class=1)].\n\n        Accepts numpy array or torch Tensor. Returns numpy for sklearn compat.\n        \"\"\"\n        if isinstance(x, np.ndarray):\n            x = torch.from_numpy(x).float().to(self.linear.weight.device)\n        with torch.no_grad():\n            p1 = torch.sigmoid(self.forward(x)).cpu().numpy()\n        return np.column_stack([1 - p1, p1])\n\n    def decision_function(self, x):\n        \"\"\"Return logits as 1-D numpy array (sklearn compat).\"\"\"\n        if isinstance(x, np.ndarray):\n            x = torch.from_numpy(x).float().to(self.linear.weight.device)\n        with torch.no_grad():\n            return self.forward(x).cpu().numpy()\n\n    def l2_reg(self):\n        \"\"\"L2 penalty on weights (not bias), matching sklearn C = 1/l2_weight.\"\"\"\n        return self.l2_weight * (self.linear.weight ** 2).sum()\n\n    @classmethod\n    def from_sklearn(cls, sklearn_probe, scaler, l2_weight=1.0):\n        \"\"\"Initialize from a trained sklearn LogisticRegression + StandardScaler.\n\n        Copies weight and bias so CaCLR starts from the converged LR solution.\n        The scaler is applied externally (same as sklearn pipeline), so we only\n        need the LR parameters here.\n        \"\"\"\n        input_dim = sklearn_probe.coef_.shape[1]\n        model = cls(input_dim, l2_weight=l2_weight)\n        with torch.no_grad():\n            model.linear.weight.copy_(torch.from_numpy(sklearn_probe.coef_).float())\n            model.linear.bias.copy_(torch.from_numpy(sklearn_probe.intercept_).float())\n        return model\n\n\n# ---------------------------------------------------------------------------\n# Training loop\n# ---------------------------------------------------------------------------\n\ndef train_caclr(\n    X_en, y_en,\n    X_tgt_dict,\n    alpha=1.0,\n    beta=0.1,\n    lr=1e-3,\n    epochs=100,\n    l2_weight=1.0,\n    init_from_sklearn=True,\n    seed=42,\n    verbose=True,\n):\n    \"\"\"Train CaCLR probe.\n\n    Steps:\n      1. Fit StandardScaler on English data.\n      2. Train standard LogisticRegression on English (sklearn).\n      3. Initialize CaCLRProbe from LR weights.\n      4. Fine-tune with L_BCE + α·L_SB-ECE + β·L_MMD.\n\n    Args:\n        X_en: (N_en, D) numpy array of English activations.\n        y_en: (N_en,) numpy array of binary labels.\n        X_tgt_dict: {lang: (X_tgt, y_tgt)} numpy arrays for target languages.\n        alpha: weight on SB-ECE calibration loss.\n        beta: weight on MMD consistency loss.\n        lr: learning rate for Adam optimizer.\n        epochs: number of training epochs.\n        l2_weight: L2 regularization weight (sklearn C = 1/l2_weight).\n        init_from_sklearn: if True, warm-start from sklearn LR solution.\n        seed: random seed.\n        verbose: print training progress.\n\n    Returns:\n        probe: trained CaCLRProbe (on CPU).\n        scaler: fitted StandardScaler.\n        history: dict with keys \"total\", \"bce\", \"sb_ece\", \"mmd\" (lists of per-epoch losses).\n    \"\"\"\n    torch.manual_seed(seed)\n    np.random.seed(seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n\n    # 1. Fit scaler on English data\n    scaler = StandardScaler()\n    X_en_s = scaler.fit_transform(X_en)\n\n    # 2. Train sklearn LR as initialization\n    sklearn_C = 1.0 / l2_weight if l2_weight > 0 else 1e6\n    sklearn_lr = LogisticRegression(\n        C=sklearn_C, penalty=\"l2\", solver=\"lbfgs\", max_iter=2000, random_state=seed,\n    )\n    sklearn_lr.fit(X_en_s, y_en)\n\n    # 3. Initialize CaCLRProbe\n    if init_from_sklearn:\n        probe = CaCLRProbe.from_sklearn(sklearn_lr, scaler, l2_weight=l2_weight)\n    else:\n        probe = CaCLRProbe(X_en_s.shape[1], l2_weight=l2_weight)\n    probe = probe.to(device)\n\n    # Convert data to tensors\n    X_en_t = torch.from_numpy(X_en_s).float().to(device)\n    y_en_t = torch.from_numpy(y_en.astype(np.float32)).to(device)\n\n    tgt_tensors = {}\n    for lang, (X_tgt, y_tgt) in X_tgt_dict.items():\n        X_tgt_s = scaler.transform(X_tgt)\n        tgt_tensors[lang] = (\n            torch.from_numpy(X_tgt_s).float().to(device),\n            torch.from_numpy(y_tgt.astype(np.float32)).to(device),\n        )\n\n    # 4. Fine-tune with CaCLR loss\n    optimizer = torch.optim.Adam(probe.parameters(), lr=lr)\n    history = {\"total\": [], \"bce\": [], \"sb_ece\": [], \"mmd\": [], \"l2\": []}\n\n    for epoch in range(epochs):\n        probe.train()\n        optimizer.zero_grad()\n\n        logits_en = probe(X_en_t)\n        probs_en = torch.sigmoid(logits_en)\n\n        loss_bce = bce_loss(logits_en, y_en_t)\n        loss_sb_ece = sb_ece_loss(probs_en, y_en_t)\n        loss_l2 = probe.l2_reg()\n\n        # MMD: average over all target languages\n        loss_mmd = torch.tensor(0.0, device=device)\n        if beta > 0 and len(tgt_tensors) > 0:\n            # Use hidden representation (pre-sigmoid) for MMD\n            # Since it's a single linear layer, the representation IS the input,\n            # so we compare scaled activations directly.\n            mmd_terms = []\n            for lang, (X_tgt_t, _) in tgt_tensors.items():\n                # Subsample for efficiency if datasets are large\n                n_sub = min(512, X_en_t.shape[0], X_tgt_t.shape[0])\n                idx_en = torch.randperm(X_en_t.shape[0], device=device)[:n_sub]\n                idx_tgt = torch.randperm(X_tgt_t.shape[0], device=device)[:n_sub]\n                mmd_terms.append(mmd_loss(X_en_t[idx_en], X_tgt_t[idx_tgt]))\n            loss_mmd = torch.stack(mmd_terms).mean()\n\n        total = loss_bce + alpha * loss_sb_ece + beta * loss_mmd + loss_l2\n        total.backward()\n        optimizer.step()\n\n        history[\"total\"].append(total.item())\n        history[\"bce\"].append(loss_bce.item())\n        history[\"sb_ece\"].append(loss_sb_ece.item())\n        history[\"mmd\"].append(loss_mmd.item())\n        history[\"l2\"].append(loss_l2.item())\n\n        if verbose and (epoch + 1) % max(1, epochs // 10) == 0:\n            print(f\"  epoch {epoch+1:>4d}/{epochs}  \"\n                  f\"total={total.item():.4f}  bce={loss_bce.item():.4f}  \"\n                  f\"sb_ece={loss_sb_ece.item():.4f}  mmd={loss_mmd.item():.4f}\")\n\n    probe = probe.cpu().eval()\n    return probe, scaler, history\n\n\n# ---------------------------------------------------------------------------\n# Evaluation helper (quick validation during sweep)\n# ---------------------------------------------------------------------------\n\ndef compute_ece(probs, labels, n_bins=10):\n    \"\"\"Histogram-based ECE (numpy, matches train_probe.py).\"\"\"\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):\n        mask = (probs > lo) & (probs <= hi)\n        if lo == 0.0:\n            mask = (probs >= lo) & (probs <= hi)\n        n_in_bin = mask.sum()\n        if n_in_bin == 0:\n            continue\n        ece += (n_in_bin / len(probs)) * abs(labels[mask].mean() - probs[mask].mean())\n    return ece\n\n\ndef quick_eval(probe, scaler, X, y):\n    \"\"\"AUROC + ECE + Brier on held-out data.\"\"\"\n    X_s = scaler.transform(X)\n    probs = probe.predict_proba(X_s)[:, 1]\n    logits = probe.decision_function(X_s)\n    if len(np.unique(y)) < 2:\n        return None, None, None\n    return roc_auc_score(y, logits), compute_ece(probs, y), brier_score_loss(y, probs)\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"CaCLR probe training\")\n    p.add_argument(\"--activations_dir\", default=\"./activations\")\n    p.add_argument(\"--output_dir\", default=\"./probes_caclr\")\n    p.add_argument(\"--layer\", type=int, required=True,\n                   help=\"Layer index to train on\")\n    p.add_argument(\"--languages\", nargs=\"+\", default=[\"zh\", \"ar\", \"hi\", \"sw\", \"ko\"],\n                   help=\"Target languages for MMD consistency loss\")\n    p.add_argument(\"--alpha\", type=float, default=1.0,\n                   help=\"SB-ECE calibration loss weight\")\n    p.add_argument(\"--beta\", type=float, default=0.1,\n                   help=\"MMD consistency loss weight\")\n    p.add_argument(\"--alpha_sweep\", type=str, default=None,\n                   help=\"Comma-separated alpha values for grid search \"\n                        \"(e.g., '0.01,0.1,1.0,10.0')\")\n    p.add_argument(\"--beta_sweep\", type=str, default=None,\n                   help=\"Comma-separated beta values for grid search\")\n    p.add_argument(\"--lr\", type=float, default=1e-3)\n    p.add_argument(\"--epochs\", type=int, default=100)\n    p.add_argument(\"--l2_weight\", type=float, default=1.0)\n    p.add_argument(\"--test_size\", type=float, default=0.2,\n                   help=\"English held-out fraction for sweep selection\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    # Load English activations\n    en_path = os.path.join(args.activations_dir, f\"layer{args.layer}_en.pt\")\n    en_data = torch.load(en_path, weights_only=True)\n    X_en = en_data[\"activations\"].numpy()\n    y_en = en_data[\"labels\"].numpy()\n    print(f\"English data: {X_en.shape[0]} samples, dim={X_en.shape[1]}\")\n\n    # Load target language activations\n    X_tgt_dict = {}\n    for lang in args.languages:\n        tgt_path = os.path.join(args.activations_dir, f\"layer{args.layer}_{lang}.pt\")\n        if not os.path.exists(tgt_path):\n            print(f\"  [SKIP] {tgt_path} not found\")\n            continue\n        tgt_data = torch.load(tgt_path, weights_only=True)\n        X_tgt_dict[lang] = (tgt_data[\"activations\"].numpy(), tgt_data[\"labels\"].numpy())\n        print(f\"  {lang}: {X_tgt_dict[lang][0].shape[0]} samples\")\n\n    # Determine if sweep mode\n    sweep_mode = args.alpha_sweep is not None or args.beta_sweep is not None\n    alphas = [float(v) for v in args.alpha_sweep.split(\",\")] if args.alpha_sweep else [args.alpha]\n    betas = [float(v) for v in args.beta_sweep.split(\",\")] if args.beta_sweep else [args.beta]\n\n    if sweep_mode:\n        # Hold out English validation set for selecting best (alpha, beta)\n        X_train, X_val, y_train, y_val = train_test_split(\n            X_en, y_en, test_size=args.test_size, random_state=args.seed, stratify=y_en,\n        )\n        print(f\"\\nSweep mode: {len(alphas)} alphas × {len(betas)} betas = {len(alphas)*len(betas)} runs\")\n        print(f\"Train: {len(y_train)}, Val: {len(y_val)}\")\n        print(f\"{'alpha':>8s} {'beta':>8s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s}\")\n        print(\"-\" * 42)\n\n        best_score = -float(\"inf\")\n        best_result = None\n\n        for a, b in product(alphas, betas):\n            probe, scaler, history = train_caclr(\n                X_train, y_train, X_tgt_dict,\n                alpha=a, beta=b, lr=args.lr, epochs=args.epochs,\n                l2_weight=args.l2_weight, seed=args.seed, verbose=False,\n            )\n            auroc, ece, brier = quick_eval(probe, scaler, X_val, y_val)\n            # Selection criterion: maximize AUROC, break ties by lower ECE\n            score = (auroc or 0.0) - 0.1 * (ece or 1.0)\n            print(f\"{a:>8.3f} {b:>8.4f} {auroc or 0:>7.4f} {ece or 0:>7.4f} {brier or 0:>7.4f}\"\n                  f\"{'  *' if score > best_score else ''}\")\n\n            if score > best_score:\n                best_score = score\n                best_result = {\n                    \"probe\": probe, \"scaler\": scaler, \"alpha\": a, \"beta\": b,\n                    \"history\": history, \"val_auroc\": auroc, \"val_ece\": ece, \"val_brier\": brier,\n                }\n\n        # Retrain best on full English data\n        print(f\"\\nBest: alpha={best_result['alpha']}, beta={best_result['beta']} \"\n              f\"(val AUROC={best_result['val_auroc']:.4f}, ECE={best_result['val_ece']:.4f})\")\n        print(\"Retraining on full English data...\")\n        probe, scaler, history = train_caclr(\n            X_en, y_en, X_tgt_dict,\n            alpha=best_result[\"alpha\"], beta=best_result[\"beta\"],\n            lr=args.lr, epochs=args.epochs, l2_weight=args.l2_weight,\n            seed=args.seed, verbose=True,\n        )\n        save_dict = {\n            \"model\": probe, \"scaler\": scaler,\n            \"alpha\": best_result[\"alpha\"], \"beta\": best_result[\"beta\"],\n            \"history\": history,\n            \"sweep_best\": {\"val_auroc\": best_result[\"val_auroc\"],\n                           \"val_ece\": best_result[\"val_ece\"],\n                           \"val_brier\": best_result[\"val_brier\"]},\n        }\n    else:\n        # Single run\n        probe, scaler, history = train_caclr(\n            X_en, y_en, X_tgt_dict,\n            alpha=args.alpha, beta=args.beta, lr=args.lr, epochs=args.epochs,\n            l2_weight=args.l2_weight, seed=args.seed, verbose=True,\n        )\n        save_dict = {\n            \"model\": probe, \"scaler\": scaler,\n            \"alpha\": args.alpha, \"beta\": args.beta,\n            \"history\": history,\n        }\n\n    # Save probe (compatible with transfer_eval.py)\n    out_path = os.path.join(args.output_dir, f\"probe_layer{args.layer}.pkl\")\n    with open(out_path, \"wb\") as f:\n        pickle.dump(save_dict, f)\n    print(f\"\\nProbe saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 14_

验证语法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "c4948641-a6a1-4b03-8e60-385dc43d32df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwL6rLrX4eJVdMx2J9xitk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6850,
      "cache_read_input_tokens": 30095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6850
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

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_011kDau3aiwuctbEv2R7epjM`</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/train_caclr.py').read()); print('OK')\"",
  "description": "Verify Python syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "787384a5-1e1a-4d9b-9235-d1e09298f2e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwL6rLrX4eJVdMx2J9xitk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6850,
      "cache_read_input_tokens": 30095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6850
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

_source line 16 · 2026-05-20T21:48:26.508Z_

<details><summary>↩ Tool result · `toolu_011kDau3aiwuctbEv2R7epjM`</summary>

```text
OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "7303e033-72a5-414a-8eb4-7b24c0df840d",
  "tool_use_result": {
    "stdout": "OK",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 17_

语法正确。文件已创建：

**`code/train_caclr.py`** — 代码结构：

| 部分 | 内容 |
|------|------|
| **Loss 组件** | `bce_loss` / `sb_ece_loss`（Gaussian soft-binning ECE）/ `gaussian_rbf_kernel`（median heuristic）/ `mmd_loss`（unbiased MMD²） |
| **模型** | `CaCLRProbe(nn.Module)` — 单层 Linear，暴露 `predict_proba()` 返回 (N,2) 和 `decision_function()` 返回 (N,)，与 `transfer_eval.py` 兼容；`from_sklearn()` 从 sklearn LR 热启动 |
| **训练循环** | `train_caclr()` — sklearn LR 初始化 → Adam fine-tune，MMD 子采样 512 样本提效 |
| **CLI** | `--alpha_sweep` / `--beta_sweep` 网格搜索模式（英文 held-out 选最优后全量重训）；单次训练模式 |
| **输出** | `{"model": probe, "scaler": scaler, ...}` pickle，可被 `transfer_eval.py` 直接加载评估 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "uuid": "be2f65dd-718b-4de5-be3c-83b5d76bb532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EyRnNcT4Ld11TnxHgEDdYk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 36945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 152
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

_source line 18_

语法正确。文件已创建：

**`code/train_caclr.py`** — 代码结构：

| 部分 | 内容 |
|------|------|
| **Loss 组件** | `bce_loss` / `sb_ece_loss`（Gaussian soft-binning ECE）/ `gaussian_rbf_kernel`（median heuristic）/ `mmd_loss`（unbiased MMD²） |
| **模型** | `CaCLRProbe(nn.Module)` — 单层 Linear，暴露 `predict_proba()` 返回 (N,2) 和 `decision_function()` 返回 (N,)，与 `transfer_eval.py` 兼容；`from_sklearn()` 从 sklearn LR 热启动 |
| **训练循环** | `train_caclr()` — sklearn LR 初始化 → Adam fine-tune，MMD 子采样 512 样本提效 |
| **CLI** | `--alpha_sweep` / `--beta_sweep` 网格搜索模式（英文 held-out 选最优后全量重训）；单次训练模式 |
| **输出** | `{"model": probe, "scaler": scaler, ...}` pickle，可被 `transfer_eval.py` 直接加载评估 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 109707,
  "duration_api_ms": 111296,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "de453e38-3487-4296-a6a6-a0e01d368331",
  "total_cost_usd": 0.40032249999999997,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 25256,
    "cache_read_input_tokens": 103971,
    "output_tokens": 7501,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25256,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 359,
        "cache_read_input_tokens": 36945,
        "cache_creation_input_tokens": 152,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 152
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2852,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0029319999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 7501,
      "cacheReadInputTokens": 103971,
      "cacheCreationInputTokens": 25256,
      "webSearchRequests": 0,
      "costUSD": 0.3973905,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "218778ef-e48b-4c66-bb1f-b5eda3a0deaf"
}
```

</details>

---
