# code spectral metric comparison

**collapse aware mixing** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_code_spectral-metric-comparison_20260513T081946.log`
- **Structured JSON:** [`f10d7f86ad2a9109ce20.json`](../../sessions/f1/f10d7f86ad2a9109ce20.json)

## Before a recorded user message

21 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code",
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
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
    "mcp__agent-ml-research__allocate_and_submit",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__approve_worker",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__backup_project_to_s3",
    "mcp__agent-ml-research__cancel_worker",
    "mcp__agent-ml-research__check_job_status",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
    "mcp__agent-ml-research__get_gpu_health",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_matrix_value",
    "mcp__agent-ml-research__get_project_resource_usage",
    "mcp__agent-ml-research__get_tum_config",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__impact_analysis",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_available_gpus",
    "mcp__agent-ml-research__list_constraints",
    "mcp__agent-ml-research__list_s3_backups",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__main_agent_post_to_director",
    "mcp__agent-ml-research__matrix_gap_analysis",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__poll_cron",
    "mcp__agent-ml-research__poll_secret_request",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_matrix",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__reconcile_crons",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__register_cron",
    "mcp__agent-ml-research__request_secret",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__submit_on_allocated",
    "mcp__agent-ml-research__submit_training_job",
    "mcp__agent-ml-research__sync_matrix_status",
    "mcp__agent-ml-research__tail_training_logs",
    "mcp__agent-ml-research__update_baseline",
    "mcp__agent-ml-research__update_matrix",
    "mcp__agent-ml-research__update_registry",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "f2a8b419-cfb7-4196-bbf4-e05bdf5cb424",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-collapse-aware-mixing-artifacts-code/memory/"
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
    "resetsAt": 1778677800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "167becf8-7b28-441f-9dfe-f6d104530505",
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me create the `evaluate_spectral_metrics.py` script based on the detailed requirements. I'll first check what existing code is in the artifacts/code directory for reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "3e33d58b-5c84-44a2-87b3-e961358ebafe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jiFqf3FtHAuBnAXUxVSM1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13489,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13489
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

### Assistant

_source line 5_

Let me check the existing code for reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "988bf88f-9b4c-49e9-8b60-70dff12d63ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jiFqf3FtHAuBnAXUxVSM1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13489,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13489
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Glob · `toolu_014kFYuYwMnXxNHsoSH6RM6L`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "d5225df4-03bf-4103-a212-4d42a3942cf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jiFqf3FtHAuBnAXUxVSM1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13489,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13489
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

_source line 7 · 2026-05-13T08:19:56.878Z_

<details><summary>↩ Tool result · `toolu_014kFYuYwMnXxNHsoSH6RM6L`</summary>

```text
generate.py
metrics.py
controller.py
test_controller.py
main_experiment.py
baselines/golden_ratio_baseline.py
train.py
pilot_pipeline.py
config.py
data_utils.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "d4e0e5af-d01d-4463-ad02-83b9143421e4",
  "tool_use_result": {
    "filenames": [
      "generate.py",
      "metrics.py",
      "controller.py",
      "test_controller.py",
      "main_experiment.py",
      "baselines/golden_ratio_baseline.py",
      "train.py",
      "pilot_pipeline.py",
      "config.py",
      "data_utils.py"
    ],
    "durationMs": 10,
    "numFiles": 10,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Cji1B71s2i1fqH9nfPZfuW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "eccd0e36-1a09-417f-84ff-1f16138cfb41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vzjF8tgo52ummDCfJqDYi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 232,
      "cache_read_input_tokens": 25330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 232
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

_source line 9 · 2026-05-13T08:19:59.724Z_

<details><summary>↩ Tool result · `toolu_01Cji1B71s2i1fqH9nfPZfuW`</summary>

```text
1	"""Collapse-detection metrics for the pilot experiment.
2	
3	Six metrics computed at each training checkpoint:
4	1. Spectral effective rank (core hypothesis)
5	2. Token-level prediction entropy variance
6	3. N-gram entropy (uni/bi/trigram)
7	4. Vocabulary coverage
8	5. Perplexity on held-out real data
9	6. Inter-generational KL divergence (unigram approximation)
10	"""
11	
12	import math
13	import logging
14	from collections import Counter
15	from typing import Dict, List, Optional
16	
17	import numpy as np
18	import torch
19	import torch.nn.functional as F
20	from torch.utils.data import DataLoader
21	from tqdm import tqdm
22	
23	logger = logging.getLogger(__name__)
24	
25	
26	# ---------------------------------------------------------------------------
27	# 1. Spectral effective rank
28	# ---------------------------------------------------------------------------
29	
30	def compute_spectral_effective_rank(
31	    model: torch.nn.Module,
32	    dataloader: DataLoader,
33	    num_samples: int = 50_000,
34	    device: str = "cuda",
35	) -> Dict[str, float]:
36	    """RankMe-style effective rank from final-layer hidden states.
37	
38	    Collects mean-pooled hidden states E (N x d), computes singular values,
39	    normalises to a distribution p, and returns exp(H(p)).
40	    """
41	    model.eval()
42	    hidden_list = []
43	    collected = 0
44	
45	    with torch.no_grad():
46	        for batch in tqdm(dataloader, desc="spectral-rank", leave=False):
47	            if collected >= num_samples:
48	                break
49	            input_ids = batch["input_ids"].to(device)
50	            attn_mask = batch["attention_mask"].to(device)
51	
52	            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)
53	            # final-layer hidden: (B, L, D)
54	            h = out.hidden_states[-1].float()
55	
56	            # mean-pool over sequence (mask-aware)
57	            mask = attn_mask.unsqueeze(-1).float()
58	            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)
59	            hidden_list.append(pooled.cpu())
60	            collected += pooled.shape[0]
61	
62	    E = torch.cat(hidden_list, dim=0)[:num_samples]  # (N, D)
63	    sigma = torch.linalg.svdvals(E)                   # descending
64	
65	    # normalise to probability distribution
66	    sigma_pos = sigma[sigma > 0]
67	    p = sigma_pos / sigma_pos.sum()
68	    entropy = -(p * p.log()).sum().item()
69	    eff_rank = math.exp(entropy)
70	
71	    return {
72	        "spectral_effective_rank": eff_rank,
73	        "spectral_entropy": entropy,
74	        "top_singular_value": sigma[0].item(),
75	        "sigma_ratio_top_bottom": (sigma[0] / sigma_pos[-1]).item(),
76	        "spectral_num_samples": int(E.shape[0]),
77	    }
78	
79	
80	# ---------------------------------------------------------------------------
81	# 2. Token-level prediction entropy variance
82	# ---------------------------------------------------------------------------
83	
84	def compute_token_entropy_variance(
85	    model: torch.nn.Module,
86	    dataloader: DataLoader,
87	    num_samples: int = 10_000,
88	    device: str = "cuda",
89	) -> Dict[str, float]:
90	    """Per-token next-token entropy, report mean and variance across all tokens."""
91	    model.eval()
92	    entropies = []
93	    seen = 0
94	
95	    with torch.no_grad():
96	        for batch in tqdm(dataloader, desc="token-entropy", leave=False):
97	            if seen >= num_samples:
98	                break
99	            input_ids = batch["input_ids"].to(device)
100	            attn_mask = batch["attention_mask"].to(device)
101	
102	            logits = model(input_ids=input_ids, attention_mask=attn_mask).logits
103	            # shift: predict position t+1 from position t
104	            logits = logits[:, :-1, :]
105	            mask = attn_mask[:, 1:].bool()
106	
107	            log_p = F.log_softmax(logits, dim=-1)
108	            p = log_p.exp()
109	            ent = -(p * log_p).sum(dim=-1)  # (B, L-1)
110	
111	            for i in range(ent.shape[0]):
112	                entropies.append(ent[i][mask[i]].cpu())
113	            seen += input_ids.shape[0]
114	
115	    all_ent = torch.cat(entropies).float()
116	    return {
117	        "token_entropy_mean": all_ent.mean().item(),
118	        "token_entropy_var": all_ent.var().item(),
119	        "token_entropy_std": all_ent.std().item(),
120	        "token_entropy_num_tokens": int(all_ent.shape[0]),
121	    }
122	
123	
124	# ---------------------------------------------------------------------------
125	# 3. N-gram entropy
126	# ---------------------------------------------------------------------------
127	
128	def compute_ngram_entropy(token_ids: List[int], max_n: int = 3) -> Dict[str, float]:
129	    """Shannon entropy of unigram / bigram / trigram distributions."""
130	    label = {1: "unigram", 2: "bigram", 3: "trigram"}
131	    results: Dict[str, float] = {}
132	    for n in range(1, max_n + 1):
133	        counter: Counter = Counter()
134	        for i in range(len(token_ids) - n + 1):
135	            counter[tuple(token_ids[i : i + n])] += 1
136	        total = sum(counter.values())
137	        entropy = -sum((c / total) * math.log(c / total) for c in counter.values())
138	        results[f"{label[n]}_entropy"] = entropy
139	        results[f"{label[n]}_unique"] = len(counter)
140	    return results
141	
142	
143	# ---------------------------------------------------------------------------
144	# 4. Vocabulary coverage
145	# ---------------------------------------------------------------------------
146	
147	def compute_vocab_coverage(token_ids: List[int], vocab_size: int) -> Dict[str, float]:
148	    unique = len(set(token_ids))
149	    return {
150	        "vocab_coverage": unique / vocab_size,
151	        "unique_tokens": unique,
152	        "total_tokens": len(token_ids),
153	    }
154	
155	
156	# ---------------------------------------------------------------------------
157	# 5. Perplexity
158	# ---------------------------------------------------------------------------
159	
160	def compute_perplexity(
161	    model: torch.nn.Module,
162	    dataloader: DataLoader,
163	    num_samples: int = 5_000,
164	    device: str = "cuda",
165	) -> Dict[str, float]:
166	    """Standard perplexity on held-out data."""
167	    model.eval()
168	    total_loss = 0.0
169	    total_tokens = 0
170	    seen = 0
171	
172	    with torch.no_grad():
173	        for batch in tqdm(dataloader, desc="perplexity", leave=False):
174	            if seen >= num_samples:
175	                break
176	            input_ids = batch["input_ids"].to(device)
177	            attn_mask = batch["attention_mask"].to(device)
178	            labels = input_ids.clone()
179	            labels[attn_mask == 0] = -100
180	
181	            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss
182	            n_tok = (labels[:, 1:] != -100).sum().item()
183	            total_loss += loss.item() * n_tok
184	            total_tokens += n_tok
185	            seen += input_ids.shape[0]
186	
187	    avg_loss = total_loss / max(total_tokens, 1)
188	    return {
189	        "perplexity": math.exp(avg_loss),
190	        "avg_loss": avg_loss,
191	        "ppl_num_tokens": total_tokens,
192	    }
193	
194	
195	# ---------------------------------------------------------------------------
196	# 6. Inter-generational KL divergence (full distribution report)
197	# ---------------------------------------------------------------------------
198	
199	def _unigram_dist(ids: np.ndarray, vocab_size: int, smoothing: float = 1e-8) -> np.ndarray:
200	    c = np.bincount(ids, minlength=vocab_size).astype(np.float64)
201	    c += smoothing
202	    return c / c.sum()
203	
204	
205	def _bigram_kl(ids_a: List[int], ids_b: List[int], smoothing: float = 1e-8) -> float:
206	    """KL(P_a || P_b) over bigram distributions (sparse, observed-support only)."""
207	    ca: Counter = Counter(zip(ids_a[:-1], ids_a[1:]))
208	    cb: Counter = Counter(zip(ids_b[:-1], ids_b[1:]))
209	    all_bg = set(ca) | set(cb)
210	    n_bg = len(all_bg)
211	    total_a = sum(ca.values()) + smoothing * n_bg
212	    total_b = sum(cb.values()) + smoothing * n_bg
213	    kl = 0.0
214	    for bg in all_bg:
215	        pa = (ca.get(bg, 0) + smoothing) / total_a
216	        pb = (cb.get(bg, 0) + smoothing) / total_b
217	        kl += pa * math.log(pa / pb)
218	    return kl
219	
220	
221	def compute_kl_divergence(
222	    ids_a: List[int],
223	    ids_b: List[int],
224	    vocab_size: int,
225	    smoothing: float = 1e-8,
226	    n_bootstrap: int = 1000,
227	    ci_level: float = 0.95,
228	) -> Dict[str, float]:
229	    """Full KL divergence report.
230	
231	    Returns unigram KL, bigram KL, frequency-binned KL contributions
232	    (high/mid/low-freq tokens), and bootstrap 95% CI on unigram KL.
233	    """
234	    arr_a = np.array(ids_a, dtype=np.int64)
235	    arr_b = np.array(ids_b, dtype=np.int64)
236	
237	    # --- Unigram KL ---
238	    p = _unigram_dist(arr_a, vocab_size, smoothing)
239	    q = _unigram_dist(arr_b, vocab_size, smoothing)
240	    per_token_kl = p * np.log(p / q)
241	    kl_unigram = float(per_token_kl.sum())
242	    kl_reverse = float((q * np.log(q / p)).sum())
243	    js = 0.5 * (kl_unigram + kl_reverse)
244	
245	    # --- Bigram KL ---
246	    kl_bigram = _bigram_kl(ids_a, ids_b, smoothing)
247	
248	    # --- Frequency-binned KL (based on reference corpus ids_a) ---
249	    counts_a = np.bincount(arr_a, minlength=vocab_size)
250	    ranked = np.argsort(-counts_a)
251	    n_nonzero = int((counts_a[ranked] > 0).sum())
252	    cut_high = max(1, n_nonzero // 100)         # top 1% of token types
253	    cut_mid = max(cut_high + 1, n_nonzero // 5)  # top 20%
254	
255	    kl_freq_high = float(per_token_kl[ranked[:cut_high]].sum())
256	    kl_freq_mid = float(per_token_kl[ranked[cut_high:cut_mid]].sum())
257	    kl_freq_low = float(per_token_kl[ranked[cut_mid:]].sum())
258	
259	    # --- Bootstrap CI on unigram KL ---
260	    rng = np.random.default_rng(42)
261	    sub_n = min(1_000_000, len(arr_a), len(arr_b))
262	    boot_kls = np.empty(n_bootstrap)
263	    for i in range(n_bootstrap):
264	        sa = rng.choice(arr_a, size=sub_n, replace=True)
265	        sb = rng.choice(arr_b, size=sub_n, replace=True)
266	        bp = np.bincount(sa, minlength=vocab_size).astype(np.float64) + smoothing
267	        bq = np.bincount(sb, minlength=vocab_size).astype(np.float64) + smoothing
268	        bp /= bp.sum()
269	        bq /= bq.sum()
270	        boot_kls[i] = (bp * np.log(bp / bq)).sum()
271	
272	    alpha = (1 - ci_level) / 2
273	    ci_lo = float(np.percentile(boot_kls, alpha * 100))
274	    ci_hi = float(np.percentile(boot_kls, (1 - alpha) * 100))
275	
276	    return {
277	        "kl_unigram": kl_unigram,
278	        "kl_unigram_reverse": kl_reverse,
279	        "js_divergence": js,
280	        "kl_bigram": kl_bigram,
281	        "kl_freq_high": kl_freq_high,
282	        "kl_freq_mid": kl_freq_mid,
283	        "kl_freq_low": kl_freq_low,
284	        "kl_ci_lower_95": ci_lo,
285	        "kl_ci_upper_95": ci_hi,
286	        "kl_bootstrap_mean": float(boot_kls.mean()),
287	        "kl_bootstrap_std": float(boot_kls.std()),
288	        "kl_freq_high_ntypes": int(cut_high),
289	        "kl_freq_mid_ntypes": int(cut_mid - cut_high),
290	        "kl_freq_low_ntypes": int(max(0, n_nonzero - cut_mid)),
291	        "kl_ci_note": "token-level i.i.d. bootstrap; CI may be anti-conservative due to sequential dependence",
292	    }
293	
294	
295	# ---------------------------------------------------------------------------
296	# Orchestrator: all metrics for one checkpoint
297	# ---------------------------------------------------------------------------
298	
299	def compute_checkpoint_metrics(
300	    model: torch.nn.Module,
301	    holdout_loader: DataLoader,
302	    gen_token_ids: List[int],
303	    prev_gen_token_ids: Optional[List[int]],
304	    vocab_size: int,
305	    config,
306	    device: str = "cuda",
307	) -> Dict[str, float]:
308	    """Compute all six metric groups for a single checkpoint."""
309	    results: Dict[str, float] = {}
310	
311	    logger.info("Computing spectral effective rank ...")
312	    results.update(compute_spectral_effective_rank(
313	        model, holdout_loader, num_samples=config.spectral_num_samples, device=device
314	    ))
315	
316	    logger.info("Computing token entropy variance ...")
317	    results.update(compute_token_entropy_variance(
318	        model, holdout_loader, num_samples=config.ppl_num_samples, device=device
319	    ))
320	
321	    logger.info("Computing perplexity ...")
322	    results.update(compute_perplexity(
323	        model, holdout_loader, num_samples=config.ppl_num_samples, device=device
324	    ))
325	
326	    logger.info("Computing n-gram entropy & vocab coverage ...")
327	    results.update(compute_ngram_entropy(gen_token_ids))
328	    results.update(compute_vocab_coverage(gen_token_ids, vocab_size))
329	
330	    if prev_gen_token_ids is not None:
331	        logger.info("Computing KL divergence (full report) ...")
332	        results.update(compute_kl_divergence(prev_gen_token_ids, gen_token_ids, vocab_size))
333	
334	    return results
335	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "3a215991-b5d7-43e2-8cb1-9937e7498946",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py",
      "content": "\"\"\"Collapse-detection metrics for the pilot experiment.\n\nSix metrics computed at each training checkpoint:\n1. Spectral effective rank (core hypothesis)\n2. Token-level prediction entropy variance\n3. N-gram entropy (uni/bi/trigram)\n4. Vocabulary coverage\n5. Perplexity on held-out real data\n6. Inter-generational KL divergence (unigram approximation)\n\"\"\"\n\nimport math\nimport logging\nfrom collections import Counter\nfrom typing import Dict, List, Optional\n\nimport numpy as np\nimport torch\nimport torch.nn.functional as F\nfrom torch.utils.data import DataLoader\nfrom tqdm import tqdm\n\nlogger = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# 1. Spectral effective rank\n# ---------------------------------------------------------------------------\n\ndef compute_spectral_effective_rank(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int = 50_000,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"RankMe-style effective rank from final-layer hidden states.\n\n    Collects mean-pooled hidden states E (N x d), computes singular values,\n    normalises to a distribution p, and returns exp(H(p)).\n    \"\"\"\n    model.eval()\n    hidden_list = []\n    collected = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"spectral-rank\", leave=False):\n            if collected >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n\n            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)\n            # final-layer hidden: (B, L, D)\n            h = out.hidden_states[-1].float()\n\n            # mean-pool over sequence (mask-aware)\n            mask = attn_mask.unsqueeze(-1).float()\n            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)\n            hidden_list.append(pooled.cpu())\n            collected += pooled.shape[0]\n\n    E = torch.cat(hidden_list, dim=0)[:num_samples]  # (N, D)\n    sigma = torch.linalg.svdvals(E)                   # descending\n\n    # normalise to probability distribution\n    sigma_pos = sigma[sigma > 0]\n    p = sigma_pos / sigma_pos.sum()\n    entropy = -(p * p.log()).sum().item()\n    eff_rank = math.exp(entropy)\n\n    return {\n        \"spectral_effective_rank\": eff_rank,\n        \"spectral_entropy\": entropy,\n        \"top_singular_value\": sigma[0].item(),\n        \"sigma_ratio_top_bottom\": (sigma[0] / sigma_pos[-1]).item(),\n        \"spectral_num_samples\": int(E.shape[0]),\n    }\n\n\n# ---------------------------------------------------------------------------\n# 2. Token-level prediction entropy variance\n# ---------------------------------------------------------------------------\n\ndef compute_token_entropy_variance(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int = 10_000,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Per-token next-token entropy, report mean and variance across all tokens.\"\"\"\n    model.eval()\n    entropies = []\n    seen = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"token-entropy\", leave=False):\n            if seen >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n\n            logits = model(input_ids=input_ids, attention_mask=attn_mask).logits\n            # shift: predict position t+1 from position t\n            logits = logits[:, :-1, :]\n            mask = attn_mask[:, 1:].bool()\n\n            log_p = F.log_softmax(logits, dim=-1)\n            p = log_p.exp()\n            ent = -(p * log_p).sum(dim=-1)  # (B, L-1)\n\n            for i in range(ent.shape[0]):\n                entropies.append(ent[i][mask[i]].cpu())\n            seen += input_ids.shape[0]\n\n    all_ent = torch.cat(entropies).float()\n    return {\n        \"token_entropy_mean\": all_ent.mean().item(),\n        \"token_entropy_var\": all_ent.var().item(),\n        \"token_entropy_std\": all_ent.std().item(),\n        \"token_entropy_num_tokens\": int(all_ent.shape[0]),\n    }\n\n\n# ---------------------------------------------------------------------------\n# 3. N-gram entropy\n# ---------------------------------------------------------------------------\n\ndef compute_ngram_entropy(token_ids: List[int], max_n: int = 3) -> Dict[str, float]:\n    \"\"\"Shannon entropy of unigram / bigram / trigram distributions.\"\"\"\n    label = {1: \"unigram\", 2: \"bigram\", 3: \"trigram\"}\n    results: Dict[str, float] = {}\n    for n in range(1, max_n + 1):\n        counter: Counter = Counter()\n        for i in range(len(token_ids) - n + 1):\n            counter[tuple(token_ids[i : i + n])] += 1\n        total = sum(counter.values())\n        entropy = -sum((c / total) * math.log(c / total) for c in counter.values())\n        results[f\"{label[n]}_entropy\"] = entropy\n        results[f\"{label[n]}_unique\"] = len(counter)\n    return results\n\n\n# ---------------------------------------------------------------------------\n# 4. Vocabulary coverage\n# ---------------------------------------------------------------------------\n\ndef compute_vocab_coverage(token_ids: List[int], vocab_size: int) -> Dict[str, float]:\n    unique = len(set(token_ids))\n    return {\n        \"vocab_coverage\": unique / vocab_size,\n        \"unique_tokens\": unique,\n        \"total_tokens\": len(token_ids),\n    }\n\n\n# ---------------------------------------------------------------------------\n# 5. Perplexity\n# ---------------------------------------------------------------------------\n\ndef compute_perplexity(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int = 5_000,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Standard perplexity on held-out data.\"\"\"\n    model.eval()\n    total_loss = 0.0\n    total_tokens = 0\n    seen = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"perplexity\", leave=False):\n            if seen >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n            labels = input_ids.clone()\n            labels[attn_mask == 0] = -100\n\n            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss\n            n_tok = (labels[:, 1:] != -100).sum().item()\n            total_loss += loss.item() * n_tok\n            total_tokens += n_tok\n            seen += input_ids.shape[0]\n\n    avg_loss = total_loss / max(total_tokens, 1)\n    return {\n        \"perplexity\": math.exp(avg_loss),\n        \"avg_loss\": avg_loss,\n        \"ppl_num_tokens\": total_tokens,\n    }\n\n\n# ---------------------------------------------------------------------------\n# 6. Inter-generational KL divergence (full distribution report)\n# ---------------------------------------------------------------------------\n\ndef _unigram_dist(ids: np.ndarray, vocab_size: int, smoothing: float = 1e-8) -> np.ndarray:\n    c = np.bincount(ids, minlength=vocab_size).astype(np.float64)\n    c += smoothing\n    return c / c.sum()\n\n\ndef _bigram_kl(ids_a: List[int], ids_b: List[int], smoothing: float = 1e-8) -> float:\n    \"\"\"KL(P_a || P_b) over bigram distributions (sparse, observed-support only).\"\"\"\n    ca: Counter = Counter(zip(ids_a[:-1], ids_a[1:]))\n    cb: Counter = Counter(zip(ids_b[:-1], ids_b[1:]))\n    all_bg = set(ca) | set(cb)\n    n_bg = len(all_bg)\n    total_a = sum(ca.values()) + smoothing * n_bg\n    total_b = sum(cb.values()) + smoothing * n_bg\n    kl = 0.0\n    for bg in all_bg:\n        pa = (ca.get(bg, 0) + smoothing) / total_a\n        pb = (cb.get(bg, 0) + smoothing) / total_b\n        kl += pa * math.log(pa / pb)\n    return kl\n\n\ndef compute_kl_divergence(\n    ids_a: List[int],\n    ids_b: List[int],\n    vocab_size: int,\n    smoothing: float = 1e-8,\n    n_bootstrap: int = 1000,\n    ci_level: float = 0.95,\n) -> Dict[str, float]:\n    \"\"\"Full KL divergence report.\n\n    Returns unigram KL, bigram KL, frequency-binned KL contributions\n    (high/mid/low-freq tokens), and bootstrap 95% CI on unigram KL.\n    \"\"\"\n    arr_a = np.array(ids_a, dtype=np.int64)\n    arr_b = np.array(ids_b, dtype=np.int64)\n\n    # --- Unigram KL ---\n    p = _unigram_dist(arr_a, vocab_size, smoothing)\n    q = _unigram_dist(arr_b, vocab_size, smoothing)\n    per_token_kl = p * np.log(p / q)\n    kl_unigram = float(per_token_kl.sum())\n    kl_reverse = float((q * np.log(q / p)).sum())\n    js = 0.5 * (kl_unigram + kl_reverse)\n\n    # --- Bigram KL ---\n    kl_bigram = _bigram_kl(ids_a, ids_b, smoothing)\n\n    # --- Frequency-binned KL (based on reference corpus ids_a) ---\n    counts_a = np.bincount(arr_a, minlength=vocab_size)\n    ranked = np.argsort(-counts_a)\n    n_nonzero = int((counts_a[ranked] > 0).sum())\n    cut_high = max(1, n_nonzero // 100)         # top 1% of token types\n    cut_mid = max(cut_high + 1, n_nonzero // 5)  # top 20%\n\n    kl_freq_high = float(per_token_kl[ranked[:cut_high]].sum())\n    kl_freq_mid = float(per_token_kl[ranked[cut_high:cut_mid]].sum())\n    kl_freq_low = float(per_token_kl[ranked[cut_mid:]].sum())\n\n    # --- Bootstrap CI on unigram KL ---\n    rng = np.random.default_rng(42)\n    sub_n = min(1_000_000, len(arr_a), len(arr_b))\n    boot_kls = np.empty(n_bootstrap)\n    for i in range(n_bootstrap):\n        sa = rng.choice(arr_a, size=sub_n, replace=True)\n        sb = rng.choice(arr_b, size=sub_n, replace=True)\n        bp = np.bincount(sa, minlength=vocab_size).astype(np.float64) + smoothing\n        bq = np.bincount(sb, minlength=vocab_size).astype(np.float64) + smoothing\n        bp /= bp.sum()\n        bq /= bq.sum()\n        boot_kls[i] = (bp * np.log(bp / bq)).sum()\n\n    alpha = (1 - ci_level) / 2\n    ci_lo = float(np.percentile(boot_kls, alpha * 100))\n    ci_hi = float(np.percentile(boot_kls, (1 - alpha) * 100))\n\n    return {\n        \"kl_unigram\": kl_unigram,\n        \"kl_unigram_reverse\": kl_reverse,\n        \"js_divergence\": js,\n        \"kl_bigram\": kl_bigram,\n        \"kl_freq_high\": kl_freq_high,\n        \"kl_freq_mid\": kl_freq_mid,\n        \"kl_freq_low\": kl_freq_low,\n        \"kl_ci_lower_95\": ci_lo,\n        \"kl_ci_upper_95\": ci_hi,\n        \"kl_bootstrap_mean\": float(boot_kls.mean()),\n        \"kl_bootstrap_std\": float(boot_kls.std()),\n        \"kl_freq_high_ntypes\": int(cut_high),\n        \"kl_freq_mid_ntypes\": int(cut_mid - cut_high),\n        \"kl_freq_low_ntypes\": int(max(0, n_nonzero - cut_mid)),\n        \"kl_ci_note\": \"token-level i.i.d. bootstrap; CI may be anti-conservative due to sequential dependence\",\n    }\n\n\n# ---------------------------------------------------------------------------\n# Orchestrator: all metrics for one checkpoint\n# ---------------------------------------------------------------------------\n\ndef compute_checkpoint_metrics(\n    model: torch.nn.Module,\n    holdout_loader: DataLoader,\n    gen_token_ids: List[int],\n    prev_gen_token_ids: Optional[List[int]],\n    vocab_size: int,\n    config,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Compute all six metric groups for a single checkpoint.\"\"\"\n    results: Dict[str, float] = {}\n\n    logger.info(\"Computing spectral effective rank ...\")\n    results.update(compute_spectral_effective_rank(\n        model, holdout_loader, num_samples=config.spectral_num_samples, device=device\n    ))\n\n    logger.info(\"Computing token entropy variance ...\")\n    results.update(compute_token_entropy_variance(\n        model, holdout_loader, num_samples=config.ppl_num_samples, device=device\n    ))\n\n    logger.info(\"Computing perplexity ...\")\n    results.update(compute_perplexity(\n        model, holdout_loader, num_samples=config.ppl_num_samples, device=device\n    ))\n\n    logger.info(\"Computing n-gram entropy & vocab coverage ...\")\n    results.update(compute_ngram_entropy(gen_token_ids))\n    results.update(compute_vocab_coverage(gen_token_ids, vocab_size))\n\n    if prev_gen_token_ids is not None:\n        logger.info(\"Computing KL divergence (full report) ...\")\n        results.update(compute_kl_divergence(prev_gen_token_ids, gen_token_ids, vocab_size))\n\n    return results\n",
      "numLines": 335,
      "startLine": 1,
      "totalLines": 335
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01Dd9CrzzN3juA12PwZP45sp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "baa60d17-42e9-4e3c-a9b5-812c4a360c77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vzjF8tgo52ummDCfJqDYi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 232,
      "cache_read_input_tokens": 25330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 232
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

_source line 11 · 2026-05-13T08:20:00.188Z_

<details><summary>↩ Tool result · `toolu_01Dd9CrzzN3juA12PwZP45sp`</summary>

```text
1	"""Data loading, tokenization, and preprocessing for pilot experiments."""
2	
3	import os
4	import logging
5	import random
6	from typing import Tuple, List, Optional
7	from itertools import chain
8	
9	import torch
10	from torch.utils.data import Dataset as TorchDataset, DataLoader
11	from datasets import load_dataset, Dataset, load_from_disk
12	from transformers import PreTrainedTokenizer
13	
14	logger = logging.getLogger(__name__)
15	
16	
17	class PackedDataset(TorchDataset):
18	    """Pre-tokenized, fixed-length sequences for causal LM training."""
19	
20	    def __init__(self, input_ids: List[List[int]]):
21	        self.input_ids = input_ids
22	
23	    def __len__(self):
24	        return len(self.input_ids)
25	
26	    def __getitem__(self, idx):
27	        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)
28	        return {"input_ids": ids, "attention_mask": torch.ones_like(ids), "labels": ids.clone()}
29	
30	
31	def prepare_real_data(
32	    config, tokenizer: PreTrainedTokenizer
33	) -> Tuple[PackedDataset, PackedDataset]:
34	    """Load real data, tokenize, pack, split into train/holdout."""
35	    cache_path = os.path.join(config.output_dir, "real_data_cache")
36	
37	    if os.path.exists(cache_path):
38	        logger.info("Loading cached tokenized data from %s", cache_path)
39	        ds = load_from_disk(cache_path)
40	    else:
41	        num_train_seqs = config.tokens_per_generation // config.max_seq_length + 1
42	        num_total_seqs = num_train_seqs + config.holdout_size + 2000
43	
44	        dataset_config = getattr(config, "real_dataset_config", None)
45	        logger.info("Loading from %s (config=%s) ...", config.real_dataset, dataset_config)
46	        raw = load_dataset(
47	            config.real_dataset,
48	            dataset_config,
49	            split="train",
50	        )
51	
52	        logger.info("Tokenizing ...")
53	        tokenized = raw.map(
54	            lambda ex: tokenizer(ex["text"], truncation=False, add_special_tokens=False),
55	            batched=True,
56	            remove_columns=raw.column_names,
57	            num_proc=4,
58	            desc="Tokenizing",
59	        )
60	
61	        logger.info("Packing into %d-token sequences ...", config.max_seq_length)
62	
63	        def pack_fn(examples):
64	            flat = list(chain(*examples["input_ids"]))
65	            n = (len(flat) // config.max_seq_length) * config.max_seq_length
66	            return {
67	                "input_ids": [
68	                    flat[i : i + config.max_seq_length]
69	                    for i in range(0, n, config.max_seq_length)
70	                ]
71	            }
72	
73	        ds = tokenized.map(
74	            pack_fn, batched=True, remove_columns=tokenized.column_names, num_proc=1
75	        )
76	
77	        os.makedirs(cache_path, exist_ok=True)
78	        ds.save_to_disk(cache_path)
79	        logger.info("Cached %d packed sequences to %s", len(ds), cache_path)
80	
81	    num_train = config.tokens_per_generation // config.max_seq_length
82	    available = len(ds) - config.holdout_size
83	    if num_train > available:
84	        logger.warning(
85	            "Requested %d train seqs but only %d available (dataset=%d, holdout=%d). Clamping.",
86	            num_train, available, len(ds), config.holdout_size,
87	        )
88	        num_train = available
89	    num_holdout = min(config.holdout_size, len(ds) - num_train)
90	
91	    train_ids = ds.select(range(num_train))["input_ids"]
92	    holdout_ids = ds.select(range(num_train, num_train + num_holdout))["input_ids"]
93	
94	    logger.info(
95	        "Train: %d seqs (%.1fM tokens) | Holdout: %d seqs",
96	        len(train_ids),
97	        len(train_ids) * config.max_seq_length / 1e6,
98	        len(holdout_ids),
99	    )
100	    return PackedDataset(train_ids), PackedDataset(holdout_ids)
101	
102	
103	def prepare_synthetic_data(
104	    data_path: str, config, tokenizer: PreTrainedTokenizer
105	) -> PackedDataset:
106	    """Load generated synthetic data and wrap as PackedDataset."""
107	    logger.info("Loading synthetic data from %s", data_path)
108	    ds = load_from_disk(data_path)
109	    num_seqs = min(len(ds), config.tokens_per_generation // config.max_seq_length)
110	
111	    input_ids = []
112	    for i in range(num_seqs):
113	        seq = ds[i]["input_ids"]
114	        if len(seq) >= config.max_seq_length:
115	            input_ids.append(seq[: config.max_seq_length])
116	        else:
117	            # pad short sequences with eos_token_id
118	            pad_id = tokenizer.eos_token_id or 0
119	            input_ids.append(seq + [pad_id] * (config.max_seq_length - len(seq)))
120	
121	    logger.info("Loaded %d synthetic sequences", len(input_ids))
122	    return PackedDataset(input_ids)
123	
124	
125	def extract_token_ids(dataset: PackedDataset, max_tokens: Optional[int] = None) -> List[int]:
126	    """Flatten all sequences into a single token-id list for corpus-level metrics."""
127	    ids: List[int] = []
128	    for i in range(len(dataset)):
129	        ids.extend(dataset.input_ids[i])
130	        if max_tokens and len(ids) >= max_tokens:
131	            return ids[:max_tokens]
132	    return ids
133	
134	
135	def mix_datasets(
136	    real_dataset: PackedDataset,
137	    synth_dataset: PackedDataset,
138	    ratio: float,
139	    seed: int = 42,
140	) -> PackedDataset:
141	    """Mix real and synthetic data by ratio.
142	
143	    Args:
144	        real_dataset: PackedDataset of real (human) sequences.
145	        synth_dataset: PackedDataset of synthetic (model-generated) sequences.
146	        ratio: Fraction of real data in the mix. 1.0 = pure real, 0.0 = pure synthetic.
147	        seed: Random seed for reproducible sampling and shuffling.
148	
149	    Returns:
150	        A new PackedDataset with ratio * N real sequences and (1 - ratio) * N synthetic sequences,
151	        where N = min(len(real), len(synth)) to keep total dataset size consistent.
152	    """
153	    total = min(len(real_dataset), len(synth_dataset))
154	    n_real = int(ratio * total)
155	    n_synth = total - n_real
156	
157	    rng = random.Random(seed)
158	    real_indices = rng.sample(range(len(real_dataset)), min(n_real, len(real_dataset)))
159	    synth_indices = rng.sample(range(len(synth_dataset)), min(n_synth, len(synth_dataset)))
160	
161	    mixed = [real_dataset.input_ids[i] for i in real_indices] + \
162	            [synth_dataset.input_ids[i] for i in synth_indices]
163	    rng.shuffle(mixed)
164	
165	    logger.info(
166	        "Mixed dataset: %d real + %d synth = %d total (ratio=%.2f)",
167	        len(real_indices), len(synth_indices), len(mixed), ratio,
168	    )
169	    return PackedDataset(mixed)
170	
171	
172	def make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:
173	    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "503ba3fc-3e58-4ed0-b100-663f75fc844c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py",
      "content": "\"\"\"Data loading, tokenization, and preprocessing for pilot experiments.\"\"\"\n\nimport os\nimport logging\nimport random\nfrom typing import Tuple, List, Optional\nfrom itertools import chain\n\nimport torch\nfrom torch.utils.data import Dataset as TorchDataset, DataLoader\nfrom datasets import load_dataset, Dataset, load_from_disk\nfrom transformers import PreTrainedTokenizer\n\nlogger = logging.getLogger(__name__)\n\n\nclass PackedDataset(TorchDataset):\n    \"\"\"Pre-tokenized, fixed-length sequences for causal LM training.\"\"\"\n\n    def __init__(self, input_ids: List[List[int]]):\n        self.input_ids = input_ids\n\n    def __len__(self):\n        return len(self.input_ids)\n\n    def __getitem__(self, idx):\n        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)\n        return {\"input_ids\": ids, \"attention_mask\": torch.ones_like(ids), \"labels\": ids.clone()}\n\n\ndef prepare_real_data(\n    config, tokenizer: PreTrainedTokenizer\n) -> Tuple[PackedDataset, PackedDataset]:\n    \"\"\"Load real data, tokenize, pack, split into train/holdout.\"\"\"\n    cache_path = os.path.join(config.output_dir, \"real_data_cache\")\n\n    if os.path.exists(cache_path):\n        logger.info(\"Loading cached tokenized data from %s\", cache_path)\n        ds = load_from_disk(cache_path)\n    else:\n        num_train_seqs = config.tokens_per_generation // config.max_seq_length + 1\n        num_total_seqs = num_train_seqs + config.holdout_size + 2000\n\n        dataset_config = getattr(config, \"real_dataset_config\", None)\n        logger.info(\"Loading from %s (config=%s) ...\", config.real_dataset, dataset_config)\n        raw = load_dataset(\n            config.real_dataset,\n            dataset_config,\n            split=\"train\",\n        )\n\n        logger.info(\"Tokenizing ...\")\n        tokenized = raw.map(\n            lambda ex: tokenizer(ex[\"text\"], truncation=False, add_special_tokens=False),\n            batched=True,\n            remove_columns=raw.column_names,\n            num_proc=4,\n            desc=\"Tokenizing\",\n        )\n\n        logger.info(\"Packing into %d-token sequences ...\", config.max_seq_length)\n\n        def pack_fn(examples):\n            flat = list(chain(*examples[\"input_ids\"]))\n            n = (len(flat) // config.max_seq_length) * config.max_seq_length\n            return {\n                \"input_ids\": [\n                    flat[i : i + config.max_seq_length]\n                    for i in range(0, n, config.max_seq_length)\n                ]\n            }\n\n        ds = tokenized.map(\n            pack_fn, batched=True, remove_columns=tokenized.column_names, num_proc=1\n        )\n\n        os.makedirs(cache_path, exist_ok=True)\n        ds.save_to_disk(cache_path)\n        logger.info(\"Cached %d packed sequences to %s\", len(ds), cache_path)\n\n    num_train = config.tokens_per_generation // config.max_seq_length\n    available = len(ds) - config.holdout_size\n    if num_train > available:\n        logger.warning(\n            \"Requested %d train seqs but only %d available (dataset=%d, holdout=%d). Clamping.\",\n            num_train, available, len(ds), config.holdout_size,\n        )\n        num_train = available\n    num_holdout = min(config.holdout_size, len(ds) - num_train)\n\n    train_ids = ds.select(range(num_train))[\"input_ids\"]\n    holdout_ids = ds.select(range(num_train, num_train + num_holdout))[\"input_ids\"]\n\n    logger.info(\n        \"Train: %d seqs (%.1fM tokens) | Holdout: %d seqs\",\n        len(train_ids),\n        len(train_ids) * config.max_seq_length / 1e6,\n        len(holdout_ids),\n    )\n    return PackedDataset(train_ids), PackedDataset(holdout_ids)\n\n\ndef prepare_synthetic_data(\n    data_path: str, config, tokenizer: PreTrainedTokenizer\n) -> PackedDataset:\n    \"\"\"Load generated synthetic data and wrap as PackedDataset.\"\"\"\n    logger.info(\"Loading synthetic data from %s\", data_path)\n    ds = load_from_disk(data_path)\n    num_seqs = min(len(ds), config.tokens_per_generation // config.max_seq_length)\n\n    input_ids = []\n    for i in range(num_seqs):\n        seq = ds[i][\"input_ids\"]\n        if len(seq) >= config.max_seq_length:\n            input_ids.append(seq[: config.max_seq_length])\n        else:\n            # pad short sequences with eos_token_id\n            pad_id = tokenizer.eos_token_id or 0\n            input_ids.append(seq + [pad_id] * (config.max_seq_length - len(seq)))\n\n    logger.info(\"Loaded %d synthetic sequences\", len(input_ids))\n    return PackedDataset(input_ids)\n\n\ndef extract_token_ids(dataset: PackedDataset, max_tokens: Optional[int] = None) -> List[int]:\n    \"\"\"Flatten all sequences into a single token-id list for corpus-level metrics.\"\"\"\n    ids: List[int] = []\n    for i in range(len(dataset)):\n        ids.extend(dataset.input_ids[i])\n        if max_tokens and len(ids) >= max_tokens:\n            return ids[:max_tokens]\n    return ids\n\n\ndef mix_datasets(\n    real_dataset: PackedDataset,\n    synth_dataset: PackedDataset,\n    ratio: float,\n    seed: int = 42,\n) -> PackedDataset:\n    \"\"\"Mix real and synthetic data by ratio.\n\n    Args:\n        real_dataset: PackedDataset of real (human) sequences.\n        synth_dataset: PackedDataset of synthetic (model-generated) sequences.\n        ratio: Fraction of real data in the mix. 1.0 = pure real, 0.0 = pure synthetic.\n        seed: Random seed for reproducible sampling and shuffling.\n\n    Returns:\n        A new PackedDataset with ratio * N real sequences and (1 - ratio) * N synthetic sequences,\n        where N = min(len(real), len(synth)) to keep total dataset size consistent.\n    \"\"\"\n    total = min(len(real_dataset), len(synth_dataset))\n    n_real = int(ratio * total)\n    n_synth = total - n_real\n\n    rng = random.Random(seed)\n    real_indices = rng.sample(range(len(real_dataset)), min(n_real, len(real_dataset)))\n    synth_indices = rng.sample(range(len(synth_dataset)), min(n_synth, len(synth_dataset)))\n\n    mixed = [real_dataset.input_ids[i] for i in real_indices] + \\\n            [synth_dataset.input_ids[i] for i in synth_indices]\n    rng.shuffle(mixed)\n\n    logger.info(\n        \"Mixed dataset: %d real + %d synth = %d total (ratio=%.2f)\",\n        len(real_indices), len(synth_indices), len(mixed), ratio,\n    )\n    return PackedDataset(mixed)\n\n\ndef make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:\n    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)\n",
      "numLines": 174,
      "startLine": 1,
      "totalLines": 174
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01XQRcZhU8tyE4QfXDU33ERg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "c14bf37e-1d02-487e-b8fb-e7eb0050e852",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vzjF8tgo52ummDCfJqDYi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 232,
      "cache_read_input_tokens": 25330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 232
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

_source line 13 · 2026-05-13T08:20:00.496Z_

<details><summary>↩ Tool result · `toolu_01XQRcZhU8tyE4QfXDU33ERg`</summary>

```text
1	"""Pilot experiment configuration for collapse-aware-mixing MVP.
2	
3	Validates spectral effective rank as a leading indicator of model collapse
4	in iterative synthetic training (Pythia-1B, 3 generations x 500M tokens).
5	"""
6	
7	import os
8	from dataclasses import dataclass
9	
10	
11	@dataclass
12	class PilotConfig:
13	    # --- Model ---
14	    model_name: str = "EleutherAI/pythia-1b"
15	
16	    # --- Training ---
17	    num_generations: int = 3                    # G0 (real), G1 (synth from G0), G2 (synth from G1)
18	    tokens_per_generation: int = 100_000_000    # 100M tokens per generation
19	    checkpoint_interval_tokens: int = 10_000_000  # save + eval every 10M tokens
20	    max_seq_length: int = 2048
21	    per_device_batch_size: int = 8
22	    gradient_accumulation_steps: int = 4
23	    learning_rate: float = 2e-6
24	    warmup_ratio: float = 0.05
25	    weight_decay: float = 0.01
26	    seed: int = 42
27	    bf16: bool = True
28	    gradient_checkpointing: bool = True
29	
30	    # --- Synthetic data generation ---
31	    gen_temperature: float = 1.0
32	    gen_top_p: float = 0.95
33	    gen_batch_size: int = 32
34	    gen_max_new_tokens: int = 2048
35	
36	    # --- Metrics ---
37	    spectral_num_samples: int = 50_000          # sequences for spectral effective rank
38	    spectral_batch_size: int = 64
39	    metrics_gen_tokens: int = 500_000           # tokens to generate at each ckpt for n-gram/coverage
40	    ppl_num_samples: int = 5_000                # sequences for PPL evaluation
41	    ppl_batch_size: int = 16
42	
43	    # --- Data ---
44	    real_dataset: str = "wikitext"
45	    real_dataset_config: str = "wikitext-103-raw-v1"
46	    holdout_size: int = 10_000                  # sequences reserved for evaluation
47	    fixed_ratio: float | None = None            # real/synth mixing ratio: None=original, 0.0=pure synth, 1.0=pure real
48	
49	    # --- Paths ---
50	    output_dir: str = "./output"
51	
52	    # --- Logging ---
53	    use_wandb: bool = True
54	    wandb_project: str = "collapse-aware-mixing"
55	    wandb_run_prefix: str = "pilot"
56	
57	    # --- Derived properties ---
58	
59	    @property
60	    def effective_batch_size(self) -> int:
61	        return self.per_device_batch_size * self.gradient_accumulation_steps
62	
63	    @property
64	    def tokens_per_step(self) -> int:
65	        return self.max_seq_length * self.effective_batch_size
66	
67	    @property
68	    def save_steps(self) -> int:
69	        return self.checkpoint_interval_tokens // self.tokens_per_step
70	
71	    @property
72	    def max_steps(self) -> int:
73	        return self.tokens_per_generation // self.tokens_per_step
74	
75	    def gen_dir(self, g: int) -> str:
76	        return os.path.join(self.output_dir, f"G{g}")
77	
78	    def checkpoint_dir(self, g: int, step: int) -> str:
79	        return os.path.join(self.gen_dir(g), "training", f"checkpoint-{step}")
80	
81	    def synthetic_data_path(self, g: int) -> str:
82	        return os.path.join(self.gen_dir(g), "synthetic_data")
83	
84	    def metrics_path(self, g: int) -> str:
85	        return os.path.join(self.gen_dir(g), "metrics.jsonl")
86	
87	    def summary_path(self) -> str:
88	        return os.path.join(self.output_dir, "pilot_summary.json")
89	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "c1ac7970-c04b-404e-bdfa-4df091a924da",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py",
      "content": "\"\"\"Pilot experiment configuration for collapse-aware-mixing MVP.\n\nValidates spectral effective rank as a leading indicator of model collapse\nin iterative synthetic training (Pythia-1B, 3 generations x 500M tokens).\n\"\"\"\n\nimport os\nfrom dataclasses import dataclass\n\n\n@dataclass\nclass PilotConfig:\n    # --- Model ---\n    model_name: str = \"EleutherAI/pythia-1b\"\n\n    # --- Training ---\n    num_generations: int = 3                    # G0 (real), G1 (synth from G0), G2 (synth from G1)\n    tokens_per_generation: int = 100_000_000    # 100M tokens per generation\n    checkpoint_interval_tokens: int = 10_000_000  # save + eval every 10M tokens\n    max_seq_length: int = 2048\n    per_device_batch_size: int = 8\n    gradient_accumulation_steps: int = 4\n    learning_rate: float = 2e-6\n    warmup_ratio: float = 0.05\n    weight_decay: float = 0.01\n    seed: int = 42\n    bf16: bool = True\n    gradient_checkpointing: bool = True\n\n    # --- Synthetic data generation ---\n    gen_temperature: float = 1.0\n    gen_top_p: float = 0.95\n    gen_batch_size: int = 32\n    gen_max_new_tokens: int = 2048\n\n    # --- Metrics ---\n    spectral_num_samples: int = 50_000          # sequences for spectral effective rank\n    spectral_batch_size: int = 64\n    metrics_gen_tokens: int = 500_000           # tokens to generate at each ckpt for n-gram/coverage\n    ppl_num_samples: int = 5_000                # sequences for PPL evaluation\n    ppl_batch_size: int = 16\n\n    # --- Data ---\n    real_dataset: str = \"wikitext\"\n    real_dataset_config: str = \"wikitext-103-raw-v1\"\n    holdout_size: int = 10_000                  # sequences reserved for evaluation\n    fixed_ratio: float | None = None            # real/synth mixing ratio: None=original, 0.0=pure synth, 1.0=pure real\n\n    # --- Paths ---\n    output_dir: str = \"./output\"\n\n    # --- Logging ---\n    use_wandb: bool = True\n    wandb_project: str = \"collapse-aware-mixing\"\n    wandb_run_prefix: str = \"pilot\"\n\n    # --- Derived properties ---\n\n    @property\n    def effective_batch_size(self) -> int:\n        return self.per_device_batch_size * self.gradient_accumulation_steps\n\n    @property\n    def tokens_per_step(self) -> int:\n        return self.max_seq_length * self.effective_batch_size\n\n    @property\n    def save_steps(self) -> int:\n        return self.checkpoint_interval_tokens // self.tokens_per_step\n\n    @property\n    def max_steps(self) -> int:\n        return self.tokens_per_generation // self.tokens_per_step\n\n    def gen_dir(self, g: int) -> str:\n        return os.path.join(self.output_dir, f\"G{g}\")\n\n    def checkpoint_dir(self, g: int, step: int) -> str:\n        return os.path.join(self.gen_dir(g), \"training\", f\"checkpoint-{step}\")\n\n    def synthetic_data_path(self, g: int) -> str:\n        return os.path.join(self.gen_dir(g), \"synthetic_data\")\n\n    def metrics_path(self, g: int) -> str:\n        return os.path.join(self.gen_dir(g), \"metrics.jsonl\")\n\n    def summary_path(self) -> str:\n        return os.path.join(self.output_dir, \"pilot_summary.json\")\n",
      "numLines": 89,
      "startLine": 1,
      "totalLines": 89
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the existing codebase. Let me create the `evaluate_spectral_metrics.py` script. Key observations:

1. `metrics.py` has `compute_spectral_effective_rank` that collects hidden states and computes SVD - I need to refactor to separate hidden state collection from metric computation
2. `data_utils.py` has `PackedDataset` and `make_dataloader` 
3. `config.py` has `PilotConfig` with relevant settings

Let me write the script now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "48ce03f6-77b7-4160-a2f4-e2383052686a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtmH4NPPoeACYSSof2k5R8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8478,
      "cache_read_input_tokens": 25562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8478
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

Now I have the full picture. Writing the evaluation script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "72b195a0-7ff0-4e1f-85d9-923ceefb83c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtmH4NPPoeACYSSof2k5R8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8478,
      "cache_read_input_tokens": 25562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8478
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

<details open><summary>🔧 Tool call — Write · `toolu_01HTcrJFtphHKSwNRzLjLqeL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/evaluate_spectral_metrics.py",
  "content": "\"\"\"Spectral metric comparison across checkpoints for collapse detection.\n\nComputes 4 spectral indicators (effective rank, condition number, trace norm,\nspectral gap) + perplexity on each checkpoint found under an output directory,\nthen ranks which metric first detects collapse (leading indicator analysis).\n\nInput:  --output-dir with G0/G1/G2 subdirectories containing training checkpoints\nOutput: stdout table + spectral_comparison.json in output-dir\n\nDependencies: torch, transformers, datasets, tqdm\n\"\"\"\n\nimport argparse\nimport glob\nimport json\nimport logging\nimport math\nimport os\nimport re\nimport sys\nfrom dataclasses import dataclass\nfrom itertools import chain\nfrom typing import Dict, List, Optional, Tuple\n\nimport torch\nimport torch.nn.functional as F\nfrom torch.utils.data import DataLoader, Dataset as TorchDataset\nfrom tqdm import tqdm\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogger = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data\n# ---------------------------------------------------------------------------\n\nclass PackedDataset(TorchDataset):\n    def __init__(self, input_ids: List[List[int]]):\n        self.input_ids = input_ids\n\n    def __len__(self):\n        return len(self.input_ids)\n\n    def __getitem__(self, idx):\n        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)\n        return {\"input_ids\": ids, \"attention_mask\": torch.ones_like(ids), \"labels\": ids.clone()}\n\n\ndef make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:\n    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)\n\n\ndef prepare_holdout(tokenizer, max_seq_length: int = 2048) -> PackedDataset:\n    from datasets import load_dataset\n\n    raw = load_dataset(\"wikitext\", \"wikitext-103-raw-v1\", split=\"test\")\n    tokenized = raw.map(\n        lambda ex: tokenizer(ex[\"text\"], truncation=False, add_special_tokens=False),\n        batched=True,\n        remove_columns=raw.column_names,\n        num_proc=4,\n        desc=\"Tokenizing holdout\",\n    )\n    flat = list(chain(*tokenized[\"input_ids\"]))\n    n = (len(flat) // max_seq_length) * max_seq_length\n    sequences = [flat[i : i + max_seq_length] for i in range(0, n, max_seq_length)]\n    logger.info(\"Holdout: %d sequences (%d tokens)\", len(sequences), n)\n    return PackedDataset(sequences)\n\n\n# ---------------------------------------------------------------------------\n# Core spectral functions\n# ---------------------------------------------------------------------------\n\ndef collect_hidden_states(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int,\n    device: str = \"cuda\",\n) -> torch.Tensor:\n    \"\"\"Collect mean-pooled final-layer hidden states E (N, D).\n\n    Same logic as metrics.py compute_spectral_effective_rank but returns\n    the raw matrix instead of computed metrics.\n    \"\"\"\n    model.eval()\n    hidden_list = []\n    collected = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"collecting hidden states\", leave=False):\n            if collected >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n\n            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)\n            h = out.hidden_states[-1].float()  # (B, L, D)\n\n            mask = attn_mask.unsqueeze(-1).float()\n            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)\n            hidden_list.append(pooled.cpu())\n            collected += pooled.shape[0]\n\n    return torch.cat(hidden_list, dim=0)[:num_samples]\n\n\ndef compute_all_spectral_metrics(E: torch.Tensor) -> dict:\n    \"\"\"Compute 4 spectral indicators from hidden states matrix.\n\n    Given E of shape (N, D), computes SVD and derives:\n      - eff_rank: exp(H(p)) where p_i = sigma_i / sum(sigma), Shannon entropy-based\n      - condition_number: sigma_max / sigma_min\n      - trace_norm: sum(sigma), i.e. nuclear norm\n      - spectral_gap: sigma_1 - sigma_2\n\n    Returns dict with all metrics plus auxiliary values.\n    \"\"\"\n    sigma = torch.linalg.svdvals(E)  # descending\n    sigma_pos = sigma[sigma > 0]\n\n    # Effective rank\n    p = sigma_pos / sigma_pos.sum()\n    entropy = -(p * p.log()).sum().item()\n    eff_rank = math.exp(entropy)\n\n    # Condition number\n    condition_number = (sigma_pos[0] / sigma_pos[-1]).item()\n\n    # Trace norm (nuclear norm)\n    trace_norm = sigma_pos.sum().item()\n\n    # Spectral gap\n    spectral_gap = (sigma_pos[0] - sigma_pos[1]).item() if len(sigma_pos) >= 2 else 0.0\n\n    return {\n        \"eff_rank\": eff_rank,\n        \"condition_number\": condition_number,\n        \"trace_norm\": trace_norm,\n        \"spectral_gap\": spectral_gap,\n        \"top_singular_value\": sigma_pos[0].item(),\n        \"num_singular_values\": int(len(sigma_pos)),\n    }\n\n\ndef compute_perplexity(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int = 5000,\n    device: str = \"cuda\",\n) -> float:\n    model.eval()\n    total_loss = 0.0\n    total_tokens = 0\n    seen = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"perplexity\", leave=False):\n            if seen >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n            labels = input_ids.clone()\n            labels[attn_mask == 0] = -100\n\n            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss\n            n_tok = (labels[:, 1:] != -100).sum().item()\n            total_loss += loss.item() * n_tok\n            total_tokens += n_tok\n            seen += input_ids.shape[0]\n\n    avg_loss = total_loss / max(total_tokens, 1)\n    return math.exp(avg_loss)\n\n\n# ---------------------------------------------------------------------------\n# Checkpoint evaluation\n# ---------------------------------------------------------------------------\n\ndef evaluate_checkpoint(\n    checkpoint_path: str,\n    holdout_data: PackedDataset,\n    num_samples: int = 50_000,\n    spectral_batch_size: int = 64,\n    ppl_batch_size: int = 16,\n    device: str = \"cuda\",\n) -> dict:\n    \"\"\"Load a checkpoint, compute all spectral metrics + PPL.\"\"\"\n    logger.info(\"Evaluating %s\", checkpoint_path)\n\n    model = AutoModelForCausalLM.from_pretrained(\n        checkpoint_path, torch_dtype=torch.bfloat16\n    ).to(device)\n    model.eval()\n\n    spectral_loader = make_dataloader(holdout_data, batch_size=spectral_batch_size)\n    E = collect_hidden_states(model, spectral_loader, num_samples=num_samples, device=device)\n    metrics = compute_all_spectral_metrics(E)\n\n    ppl_loader = make_dataloader(holdout_data, batch_size=ppl_batch_size)\n    metrics[\"ppl\"] = compute_perplexity(model, ppl_loader, num_samples=5000, device=device)\n\n    del model\n    torch.cuda.empty_cache()\n\n    return metrics\n\n\n# ---------------------------------------------------------------------------\n# Leading indicator analysis\n# ---------------------------------------------------------------------------\n\ndef compute_leading_indicator_ranking(results: List[dict], baseline: dict) -> dict:\n    \"\"\"Rank which spectral metric first detects collapse.\n\n    For each metric, estimates sigma from the baseline checkpoint(s) (first entry)\n    and finds the earliest checkpoint index where the metric deviates by more than\n    2 sigma from the baseline value.\n\n    Args:\n        results: list of dicts, each with keys eff_rank, condition_number,\n                 trace_norm, spectral_gap, ppl. Ordered chronologically.\n        baseline: dict with the same keys, representing the reference (G0-final).\n\n    Returns:\n        dict with 'ranking' (sorted list of {metric, first_deviation_idx, ...})\n        and 'details' per metric.\n    \"\"\"\n    metric_keys = [\"eff_rank\", \"condition_number\", \"trace_norm\", \"spectral_gap\"]\n\n    # Estimate sigma from variance across all checkpoints in the baseline generation.\n    # If only one baseline point, use 1% of baseline value as a fallback sigma.\n    baseline_vals = {k: baseline[k] for k in metric_keys}\n\n    details = {}\n    for key in metric_keys:\n        bv = baseline_vals[key]\n        # Fallback sigma: 1% of baseline value (minimum floor to avoid div-by-zero)\n        sigma_est = max(abs(bv) * 0.01, 1e-8)\n\n        first_idx = None\n        first_delta = None\n        first_sigma_multiple = None\n\n        for i, r in enumerate(results):\n            delta = r[key] - bv\n            n_sigma = abs(delta) / sigma_est\n            if n_sigma >= 2.0:\n                first_idx = i\n                first_delta = delta\n                first_sigma_multiple = n_sigma\n                break\n\n        details[key] = {\n            \"baseline_value\": bv,\n            \"sigma_estimate\": sigma_est,\n            \"first_deviation_idx\": first_idx,\n            \"first_deviation_delta\": first_delta,\n            \"first_deviation_sigma\": first_sigma_multiple,\n        }\n\n    # Sort: earliest deviation first; ties broken by larger sigma multiple\n    ranking = sorted(\n        details.items(),\n        key=lambda kv: (\n            kv[1][\"first_deviation_idx\"] if kv[1][\"first_deviation_idx\"] is not None else len(results) + 1,\n            -(kv[1][\"first_deviation_sigma\"] or 0),\n        ),\n    )\n\n    return {\n        \"ranking\": [\n            {\"metric\": k, **v, \"rank\": i + 1}\n            for i, (k, v) in enumerate(ranking)\n        ],\n        \"details\": details,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpoint discovery\n# ---------------------------------------------------------------------------\n\ndef discover_checkpoints(output_dir: str) -> List[Tuple[str, str]]:\n    \"\"\"Scan output_dir for G*/training/checkpoint-* and G*/final_model/.\n\n    Returns list of (label, path) sorted by generation then step.\n    \"\"\"\n    entries = []\n\n    for gen_dir in sorted(glob.glob(os.path.join(output_dir, \"G*\"))):\n        gen_name = os.path.basename(gen_dir)\n\n        # training checkpoints\n        ckpt_pattern = os.path.join(gen_dir, \"training\", \"checkpoint-*\")\n        ckpts = sorted(glob.glob(ckpt_pattern), key=lambda p: int(re.search(r\"checkpoint-(\\d+)\", p).group(1)))\n        for i, cp in enumerate(ckpts, 1):\n            step = re.search(r\"checkpoint-(\\d+)\", cp).group(1)\n            entries.append((f\"{gen_name}-ckpt{i}(s{step})\", cp))\n\n        # final model\n        final = os.path.join(gen_dir, \"final_model\")\n        if os.path.isdir(final):\n            entries.append((f\"{gen_name}-final\", final))\n\n    return entries\n\n\n# ---------------------------------------------------------------------------\n# Display\n# ---------------------------------------------------------------------------\n\ndef print_table(labels: List[str], results: List[dict]):\n    metric_rows = [\n        (\"eff_rank\", \"eff_rank\"),\n        (\"cond_num\", \"condition_number\"),\n        (\"trace_nm\", \"trace_norm\"),\n        (\"spec_gap\", \"spectral_gap\"),\n        (\"ppl\", \"ppl\"),\n    ]\n\n    col_width = max(10, max(len(l) for l in labels) + 2)\n    header = \"         | \" + \" | \".join(l.center(col_width) for l in labels)\n    sep = \"=\" * len(header)\n\n    print(\"\\nMetric Comparison Across Checkpoints\")\n    print(sep)\n    print(header)\n    print(sep)\n\n    for display_name, key in metric_rows:\n        vals = []\n        for r in results:\n            v = r.get(key)\n            if v is None:\n                vals.append(\"N/A\".center(col_width))\n            elif abs(v) >= 1000:\n                vals.append(f\"{v:.1f}\".center(col_width))\n            elif abs(v) >= 10:\n                vals.append(f\"{v:.1f}\".center(col_width))\n            else:\n                vals.append(f\"{v:.3f}\".center(col_width))\n        print(f\"{display_name:>8s} | \" + \" | \".join(vals))\n\n    print(sep)\n\n\ndef print_ranking(ranking_info: dict, labels: List[str]):\n    print(\"\\nLeading Indicator Ranking:\")\n    for entry in ranking_info[\"ranking\"]:\n        idx = entry[\"first_deviation_idx\"]\n        if idx is not None:\n            delta = entry[\"first_deviation_delta\"]\n            sigma = entry[\"first_deviation_sigma\"]\n            sign = \"+\" if delta > 0 else \"\"\n            label = labels[idx] if idx < len(labels) else f\"idx={idx}\"\n            print(f\"  {entry['rank']}. {entry['metric']:<18s} — first deviation at {label} \"\n                  f\"(Δ={sign}{delta:.2f}, {sigma:.1f}σ)\")\n        else:\n            print(f\"  {entry['rank']}. {entry['metric']:<18s} — no significant deviation detected\")\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Spectral metric comparison for collapse detection\")\n    parser.add_argument(\"--output-dir\", required=True, help=\"Root output dir with G0/G1/G2 subdirs\")\n    parser.add_argument(\"--model-name\", default=\"EleutherAI/pythia-1b\", help=\"Base model name for tokenizer\")\n    parser.add_argument(\"--num-samples\", type=int, default=50_000, help=\"Hidden state samples for spectral metrics\")\n    parser.add_argument(\"--spectral-batch-size\", type=int, default=64)\n    parser.add_argument(\"--ppl-batch-size\", type=int, default=16)\n    parser.add_argument(\"--max-seq-length\", type=int, default=2048)\n    parser.add_argument(\"--device\", default=\"cuda\")\n    parser.add_argument(\"--json-output\", default=None, help=\"JSON output path (default: output-dir/spectral_comparison.json)\")\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\n\n    checkpoints = discover_checkpoints(args.output_dir)\n    if not checkpoints:\n        print(f\"No checkpoints found under {args.output_dir}/G*/\", file=sys.stderr)\n        sys.exit(1)\n\n    labels = [label for label, _ in checkpoints]\n    paths = [path for _, path in checkpoints]\n    logger.info(\"Found %d checkpoints: %s\", len(checkpoints), \", \".join(labels))\n\n    # Prepare holdout data\n    logger.info(\"Preparing holdout data from wikitext-103-raw-v1 test split...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_name)\n    holdout = prepare_holdout(tokenizer, max_seq_length=args.max_seq_length)\n\n    # Evaluate each checkpoint\n    all_results = []\n    for label, path in checkpoints:\n        logger.info(\"--- %s ---\", label)\n        metrics = evaluate_checkpoint(\n            path, holdout,\n            num_samples=args.num_samples,\n            spectral_batch_size=args.spectral_batch_size,\n            ppl_batch_size=args.ppl_batch_size,\n            device=args.device,\n        )\n        metrics[\"label\"] = label\n        metrics[\"path\"] = path\n        all_results.append(metrics)\n        logger.info(\"  eff_rank=%.1f  cond=%.1f  trace=%.1f  gap=%.2f  ppl=%.2f\",\n                     metrics[\"eff_rank\"], metrics[\"condition_number\"],\n                     metrics[\"trace_norm\"], metrics[\"spectral_gap\"], metrics[\"ppl\"])\n\n    # Use first checkpoint (G0 earliest) as baseline\n    baseline = all_results[0]\n\n    # Leading indicator analysis (skip baseline itself)\n    ranking_info = compute_leading_indicator_ranking(all_results[1:], baseline)\n\n    # Display\n    print_table(labels, all_results)\n    # Shift labels for ranking display (skipped baseline)\n    print_ranking(ranking_info, labels[1:])\n\n    # Save JSON\n    json_path = args.json_output or os.path.join(args.output_dir, \"spectral_comparison.json\")\n    report = {\n        \"checkpoints\": [\n            {**r, \"path\": str(r[\"path\"])} for r in all_results\n        ],\n        \"baseline_label\": labels[0],\n        \"leading_indicator_ranking\": ranking_info,\n    }\n    os.makedirs(os.path.dirname(json_path) or \".\", exist_ok=True)\n    with open(json_path, \"w\") as f:\n        json.dump(report, f, indent=2)\n    print(f\"\\nJSON report saved to {json_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "e73c8aeb-592d-4813-ba0d-58e21e87a634",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtmH4NPPoeACYSSof2k5R8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8478,
      "cache_read_input_tokens": 25562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8478
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

_source line 17 · 2026-05-13T08:21:19.800Z_

<details><summary>↩ Tool result · `toolu_01HTcrJFtphHKSwNRzLjLqeL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/evaluate_spectral_metrics.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "cd148460-fd8e-41b1-9aae-6a0529d8d4c3",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/evaluate_spectral_metrics.py",
    "content": "\"\"\"Spectral metric comparison across checkpoints for collapse detection.\n\nComputes 4 spectral indicators (effective rank, condition number, trace norm,\nspectral gap) + perplexity on each checkpoint found under an output directory,\nthen ranks which metric first detects collapse (leading indicator analysis).\n\nInput:  --output-dir with G0/G1/G2 subdirectories containing training checkpoints\nOutput: stdout table + spectral_comparison.json in output-dir\n\nDependencies: torch, transformers, datasets, tqdm\n\"\"\"\n\nimport argparse\nimport glob\nimport json\nimport logging\nimport math\nimport os\nimport re\nimport sys\nfrom dataclasses import dataclass\nfrom itertools import chain\nfrom typing import Dict, List, Optional, Tuple\n\nimport torch\nimport torch.nn.functional as F\nfrom torch.utils.data import DataLoader, Dataset as TorchDataset\nfrom tqdm import tqdm\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogger = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data\n# ---------------------------------------------------------------------------\n\nclass PackedDataset(TorchDataset):\n    def __init__(self, input_ids: List[List[int]]):\n        self.input_ids = input_ids\n\n    def __len__(self):\n        return len(self.input_ids)\n\n    def __getitem__(self, idx):\n        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)\n        return {\"input_ids\": ids, \"attention_mask\": torch.ones_like(ids), \"labels\": ids.clone()}\n\n\ndef make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:\n    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)\n\n\ndef prepare_holdout(tokenizer, max_seq_length: int = 2048) -> PackedDataset:\n    from datasets import load_dataset\n\n    raw = load_dataset(\"wikitext\", \"wikitext-103-raw-v1\", split=\"test\")\n    tokenized = raw.map(\n        lambda ex: tokenizer(ex[\"text\"], truncation=False, add_special_tokens=False),\n        batched=True,\n        remove_columns=raw.column_names,\n        num_proc=4,\n        desc=\"Tokenizing holdout\",\n    )\n    flat = list(chain(*tokenized[\"input_ids\"]))\n    n = (len(flat) // max_seq_length) * max_seq_length\n    sequences = [flat[i : i + max_seq_length] for i in range(0, n, max_seq_length)]\n    logger.info(\"Holdout: %d sequences (%d tokens)\", len(sequences), n)\n    return PackedDataset(sequences)\n\n\n# ---------------------------------------------------------------------------\n# Core spectral functions\n# ---------------------------------------------------------------------------\n\ndef collect_hidden_states(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int,\n    device: str = \"cuda\",\n) -> torch.Tensor:\n    \"\"\"Collect mean-pooled final-layer hidden states E (N, D).\n\n    Same logic as metrics.py compute_spectral_effective_rank but returns\n    the raw matrix instead of computed metrics.\n    \"\"\"\n    model.eval()\n    hidden_list = []\n    collected = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"collecting hidden states\", leave=False):\n            if collected >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n\n            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)\n            h = out.hidden_states[-1].float()  # (B, L, D)\n\n            mask = attn_mask.unsqueeze(-1).float()\n            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)\n            hidden_list.append(pooled.cpu())\n            collected += pooled.shape[0]\n\n    return torch.cat(hidden_list, dim=0)[:num_samples]\n\n\ndef compute_all_spectral_metrics(E: torch.Tensor) -> dict:\n    \"\"\"Compute 4 spectral indicators from hidden states matrix.\n\n    Given E of shape (N, D), computes SVD and derives:\n      - eff_rank: exp(H(p)) where p_i = sigma_i / sum(sigma), Shannon entropy-based\n      - condition_number: sigma_max / sigma_min\n      - trace_norm: sum(sigma), i.e. nuclear norm\n      - spectral_gap: sigma_1 - sigma_2\n\n    Returns dict with all metrics plus auxiliary values.\n    \"\"\"\n    sigma = torch.linalg.svdvals(E)  # descending\n    sigma_pos = sigma[sigma > 0]\n\n    # Effective rank\n    p = sigma_pos / sigma_pos.sum()\n    entropy = -(p * p.log()).sum().item()\n    eff_rank = math.exp(entropy)\n\n    # Condition number\n    condition_number = (sigma_pos[0] / sigma_pos[-1]).item()\n\n    # Trace norm (nuclear norm)\n    trace_norm = sigma_pos.sum().item()\n\n    # Spectral gap\n    spectral_gap = (sigma_pos[0] - sigma_pos[1]).item() if len(sigma_pos) >= 2 else 0.0\n\n    return {\n        \"eff_rank\": eff_rank,\n        \"condition_number\": condition_number,\n        \"trace_norm\": trace_norm,\n        \"spectral_gap\": spectral_gap,\n        \"top_singular_value\": sigma_pos[0].item(),\n        \"num_singular_values\": int(len(sigma_pos)),\n    }\n\n\ndef compute_perplexity(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int = 5000,\n    device: str = \"cuda\",\n) -> float:\n    model.eval()\n    total_loss = 0.0\n    total_tokens = 0\n    seen = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"perplexity\", leave=False):\n            if seen >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n            labels = input_ids.clone()\n            labels[attn_mask == 0] = -100\n\n            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss\n            n_tok = (labels[:, 1:] != -100).sum().item()\n            total_loss += loss.item() * n_tok\n            total_tokens += n_tok\n            seen += input_ids.shape[0]\n\n    avg_loss = total_loss / max(total_tokens, 1)\n    return math.exp(avg_loss)\n\n\n# ---------------------------------------------------------------------------\n# Checkpoint evaluation\n# ---------------------------------------------------------------------------\n\ndef evaluate_checkpoint(\n    checkpoint_path: str,\n    holdout_data: PackedDataset,\n    num_samples: int = 50_000,\n    spectral_batch_size: int = 64,\n    ppl_batch_size: int = 16,\n    device: str = \"cuda\",\n) -> dict:\n    \"\"\"Load a checkpoint, compute all spectral metrics + PPL.\"\"\"\n    logger.info(\"Evaluating %s\", checkpoint_path)\n\n    model = AutoModelForCausalLM.from_pretrained(\n        checkpoint_path, torch_dtype=torch.bfloat16\n    ).to(device)\n    model.eval()\n\n    spectral_loader = make_dataloader(holdout_data, batch_size=spectral_batch_size)\n    E = collect_hidden_states(model, spectral_loader, num_samples=num_samples, device=device)\n    metrics = compute_all_spectral_metrics(E)\n\n    ppl_loader = make_dataloader(holdout_data, batch_size=ppl_batch_size)\n    metrics[\"ppl\"] = compute_perplexity(model, ppl_loader, num_samples=5000, device=device)\n\n    del model\n    torch.cuda.empty_cache()\n\n    return metrics\n\n\n# ---------------------------------------------------------------------------\n# Leading indicator analysis\n# ---------------------------------------------------------------------------\n\ndef compute_leading_indicator_ranking(results: List[dict], baseline: dict) -> dict:\n    \"\"\"Rank which spectral metric first detects collapse.\n\n    For each metric, estimates sigma from the baseline checkpoint(s) (first entry)\n    and finds the earliest checkpoint index where the metric deviates by more than\n    2 sigma from the baseline value.\n\n    Args:\n        results: list of dicts, each with keys eff_rank, condition_number,\n                 trace_norm, spectral_gap, ppl. Ordered chronologically.\n        baseline: dict with the same keys, representing the reference (G0-final).\n\n    Returns:\n        dict with 'ranking' (sorted list of {metric, first_deviation_idx, ...})\n        and 'details' per metric.\n    \"\"\"\n    metric_keys = [\"eff_rank\", \"condition_number\", \"trace_norm\", \"spectral_gap\"]\n\n    # Estimate sigma from variance across all checkpoints in the baseline generation.\n    # If only one baseline point, use 1% of baseline value as a fallback sigma.\n    baseline_vals = {k: baseline[k] for k in metric_keys}\n\n    details = {}\n    for key in metric_keys:\n        bv = baseline_vals[key]\n        # Fallback sigma: 1% of baseline value (minimum floor to avoid div-by-zero)\n        sigma_est = max(abs(bv) * 0.01, 1e-8)\n\n        first_idx = None\n        first_delta = None\n        first_sigma_multiple = None\n\n        for i, r in enumerate(results):\n            delta = r[key] - bv\n            n_sigma = abs(delta) / sigma_est\n            if n_sigma >= 2.0:\n                first_idx = i\n                first_delta = delta\n                first_sigma_multiple = n_sigma\n                break\n\n        details[key] = {\n            \"baseline_value\": bv,\n            \"sigma_estimate\": sigma_est,\n            \"first_deviation_idx\": first_idx,\n            \"first_deviation_delta\": first_delta,\n            \"first_deviation_sigma\": first_sigma_multiple,\n        }\n\n    # Sort: earliest deviation first; ties broken by larger sigma multiple\n    ranking = sorted(\n        details.items(),\n        key=lambda kv: (\n            kv[1][\"first_deviation_idx\"] if kv[1][\"first_deviation_idx\"] is not None else len(results) + 1,\n            -(kv[1][\"first_deviation_sigma\"] or 0),\n        ),\n    )\n\n    return {\n        \"ranking\": [\n            {\"metric\": k, **v, \"rank\": i + 1}\n            for i, (k, v) in enumerate(ranking)\n        ],\n        \"details\": details,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpoint discovery\n# ---------------------------------------------------------------------------\n\ndef discover_checkpoints(output_dir: str) -> List[Tuple[str, str]]:\n    \"\"\"Scan output_dir for G*/training/checkpoint-* and G*/final_model/.\n\n    Returns list of (label, path) sorted by generation then step.\n    \"\"\"\n    entries = []\n\n    for gen_dir in sorted(glob.glob(os.path.join(output_dir, \"G*\"))):\n        gen_name = os.path.basename(gen_dir)\n\n        # training checkpoints\n        ckpt_pattern = os.path.join(gen_dir, \"training\", \"checkpoint-*\")\n        ckpts = sorted(glob.glob(ckpt_pattern), key=lambda p: int(re.search(r\"checkpoint-(\\d+)\", p).group(1)))\n        for i, cp in enumerate(ckpts, 1):\n            step = re.search(r\"checkpoint-(\\d+)\", cp).group(1)\n            entries.append((f\"{gen_name}-ckpt{i}(s{step})\", cp))\n\n        # final model\n        final = os.path.join(gen_dir, \"final_model\")\n        if os.path.isdir(final):\n            entries.append((f\"{gen_name}-final\", final))\n\n    return entries\n\n\n# ---------------------------------------------------------------------------\n# Display\n# ---------------------------------------------------------------------------\n\ndef print_table(labels: List[str], results: List[dict]):\n    metric_rows = [\n        (\"eff_rank\", \"eff_rank\"),\n        (\"cond_num\", \"condition_number\"),\n        (\"trace_nm\", \"trace_norm\"),\n        (\"spec_gap\", \"spectral_gap\"),\n        (\"ppl\", \"ppl\"),\n    ]\n\n    col_width = max(10, max(len(l) for l in labels) + 2)\n    header = \"         | \" + \" | \".join(l.center(col_width) for l in labels)\n    sep = \"=\" * len(header)\n\n    print(\"\\nMetric Comparison Across Checkpoints\")\n    print(sep)\n    print(header)\n    print(sep)\n\n    for display_name, key in metric_rows:\n        vals = []\n        for r in results:\n            v = r.get(key)\n            if v is None:\n                vals.append(\"N/A\".center(col_width))\n            elif abs(v) >= 1000:\n                vals.append(f\"{v:.1f}\".center(col_width))\n            elif abs(v) >= 10:\n                vals.append(f\"{v:.1f}\".center(col_width))\n            else:\n                vals.append(f\"{v:.3f}\".center(col_width))\n        print(f\"{display_name:>8s} | \" + \" | \".join(vals))\n\n    print(sep)\n\n\ndef print_ranking(ranking_info: dict, labels: List[str]):\n    print(\"\\nLeading Indicator Ranking:\")\n    for entry in ranking_info[\"ranking\"]:\n        idx = entry[\"first_deviation_idx\"]\n        if idx is not None:\n            delta = entry[\"first_deviation_delta\"]\n            sigma = entry[\"first_deviation_sigma\"]\n            sign = \"+\" if delta > 0 else \"\"\n            label = labels[idx] if idx < len(labels) else f\"idx={idx}\"\n            print(f\"  {entry['rank']}. {entry['metric']:<18s} — first deviation at {label} \"\n                  f\"(Δ={sign}{delta:.2f}, {sigma:.1f}σ)\")\n        else:\n            print(f\"  {entry['rank']}. {entry['metric']:<18s} — no significant deviation detected\")\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Spectral metric comparison for collapse detection\")\n    parser.add_argument(\"--output-dir\", required=True, help=\"Root output dir with G0/G1/G2 subdirs\")\n    parser.add_argument(\"--model-name\", default=\"EleutherAI/pythia-1b\", help=\"Base model name for tokenizer\")\n    parser.add_argument(\"--num-samples\", type=int, default=50_000, help=\"Hidden state samples for spectral metrics\")\n    parser.add_argument(\"--spectral-batch-size\", type=int, default=64)\n    parser.add_argument(\"--ppl-batch-size\", type=int, default=16)\n    parser.add_argument(\"--max-seq-length\", type=int, default=2048)\n    parser.add_argument(\"--device\", default=\"cuda\")\n    parser.add_argument(\"--json-output\", default=None, help=\"JSON output path (default: output-dir/spectral_comparison.json)\")\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\n\n    checkpoints = discover_checkpoints(args.output_dir)\n    if not checkpoints:\n        print(f\"No checkpoints found under {args.output_dir}/G*/\", file=sys.stderr)\n        sys.exit(1)\n\n    labels = [label for label, _ in checkpoints]\n    paths = [path for _, path in checkpoints]\n    logger.info(\"Found %d checkpoints: %s\", len(checkpoints), \", \".join(labels))\n\n    # Prepare holdout data\n    logger.info(\"Preparing holdout data from wikitext-103-raw-v1 test split...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_name)\n    holdout = prepare_holdout(tokenizer, max_seq_length=args.max_seq_length)\n\n    # Evaluate each checkpoint\n    all_results = []\n    for label, path in checkpoints:\n        logger.info(\"--- %s ---\", label)\n        metrics = evaluate_checkpoint(\n            path, holdout,\n            num_samples=args.num_samples,\n            spectral_batch_size=args.spectral_batch_size,\n            ppl_batch_size=args.ppl_batch_size,\n            device=args.device,\n        )\n        metrics[\"label\"] = label\n        metrics[\"path\"] = path\n        all_results.append(metrics)\n        logger.info(\"  eff_rank=%.1f  cond=%.1f  trace=%.1f  gap=%.2f  ppl=%.2f\",\n                     metrics[\"eff_rank\"], metrics[\"condition_number\"],\n                     metrics[\"trace_norm\"], metrics[\"spectral_gap\"], metrics[\"ppl\"])\n\n    # Use first checkpoint (G0 earliest) as baseline\n    baseline = all_results[0]\n\n    # Leading indicator analysis (skip baseline itself)\n    ranking_info = compute_leading_indicator_ranking(all_results[1:], baseline)\n\n    # Display\n    print_table(labels, all_results)\n    # Shift labels for ranking display (skipped baseline)\n    print_ranking(ranking_info, labels[1:])\n\n    # Save JSON\n    json_path = args.json_output or os.path.join(args.output_dir, \"spectral_comparison.json\")\n    report = {\n        \"checkpoints\": [\n            {**r, \"path\": str(r[\"path\"])} for r in all_results\n        ],\n        \"baseline_label\": labels[0],\n        \"leading_indicator_ranking\": ranking_info,\n    }\n    os.makedirs(os.path.dirname(json_path) or \".\", exist_ok=True)\n    with open(json_path, \"w\") as f:\n        json.dump(report, f, indent=2)\n    print(f\"\\nJSON report saved to {json_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01JbC3pSBemEtqxzrdekCWBE`</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('evaluate_spectral_metrics.py').read()); print('OK')\"",
  "description": "Verify syntax of the new script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "5f33532d-82cc-4fc6-a323-5b86af9ac957",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFuYNVEQ5Z9NjFm8mwc8Qw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4991,
      "cache_read_input_tokens": 34040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4991
      },
      "output_tokens": 66,
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

_source line 19 · 2026-05-13T08:21:23.605Z_

<details><summary>↩ Tool result · `toolu_01JbC3pSBemEtqxzrdekCWBE`</summary>

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
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "62fd9703-b12a-4dab-ba59-e205604453d6",
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

_source line 20_

语法验证通过。`evaluate_spectral_metrics.py` 已写入 `artifacts/code/`。

脚本结构：
- `collect_hidden_states` — 收集 final-layer mean-pooled hidden states，返回 (N, D) 矩阵
- `compute_all_spectral_metrics` — 从 E 矩阵计算 4 种谱指标（eff_rank / condition_number / trace_norm / spectral_gap）
- `evaluate_checkpoint` — 加载单个 checkpoint，计算谱指标 + PPL
- `compute_leading_indicator_ranking` — 以首个 checkpoint 为 baseline，找各指标最早超过 2σ 偏离的位置，输出排名
- `discover_checkpoints` — 自动扫描 G*/training/checkpoint-* 和 G*/final_model/
- holdout 数据用 wikitext-103-raw-v1 test split tokenize + pack

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "uuid": "a69ad339-f990-4447-9121-b6722d4cda1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFTFSxkSUCr4JcEnVN5vNF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 119,
      "cache_read_input_tokens": 39031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 119
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

_source line 21_

语法验证通过。`evaluate_spectral_metrics.py` 已写入 `artifacts/code/`。

脚本结构：
- `collect_hidden_states` — 收集 final-layer mean-pooled hidden states，返回 (N, D) 矩阵
- `compute_all_spectral_metrics` — 从 E 矩阵计算 4 种谱指标（eff_rank / condition_number / trace_norm / spectral_gap）
- `evaluate_checkpoint` — 加载单个 checkpoint，计算谱指标 + PPL
- `compute_leading_indicator_ranking` — 以首个 checkpoint 为 baseline，找各指标最早超过 2σ 偏离的位置，输出排名
- `discover_checkpoints` — 自动扫描 G*/training/checkpoint-* 和 G*/final_model/
- holdout 数据用 wikitext-103-raw-v1 test split tokenize + pack

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 96949,
  "duration_api_ms": 97744,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "b6cdcfd6-47ef-4476-9791-3c3ab3c5560a",
  "total_cost_usd": 0.38430824999999996,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 27309,
    "cache_read_input_tokens": 135804,
    "output_tokens": 5725,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27309,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 258,
        "cache_read_input_tokens": 39031,
        "cache_creation_input_tokens": 119,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 119
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2490,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002565,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 5725,
      "cacheReadInputTokens": 135804,
      "cacheCreationInputTokens": 27309,
      "webSearchRequests": 0,
      "costUSD": 0.38174325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0fbe504f-32ca-42cd-80b8-24c08e307f16"
}
```

</details>

---
