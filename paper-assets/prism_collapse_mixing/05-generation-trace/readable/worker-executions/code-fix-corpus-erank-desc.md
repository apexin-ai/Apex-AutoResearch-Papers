# code fix corpus erank desc

**prism collapse mixing** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_code_fix_corpus_erank_desc_20260516T020037.log`
- **Structured JSON:** [`6f33413e3cbffed25624.json`](../../sessions/6f/6f33413e3cbffed25624.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/prism_collapse_mixing",
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "ea4f2173-fe6c-4c84-99a9-05e14b49adba",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-5-projects-prism-collapse-mixing/memory/"
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
    "resetsAt": 1778905200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "aa724324-cfab-4040-a573-cf35bbdc6e42",
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4"
}
```

---

### Assistant

_source line 4_

I'll read the actual code on the server and the current paper skeleton in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "97948e43-e534-4ad0-8e44-35c20bbaaff7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hsQMB7bPXGgXrGwZM9FQg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11701,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11701
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WfDdnWCjfTvqKArJZHYsJc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file",
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
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "5e7dd717-16d6-44ba-922c-c7cc89ef86af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hsQMB7bPXGgXrGwZM9FQg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11701,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11701
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-16T02:00:50.017Z_

<details><summary>↩ Tool result · `toolu_01WfDdnWCjfTvqKArJZHYsJc`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "feacec47-a241-4250-85b4-0c6cd6d0a0ba",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the code and the paper skeleton in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "c6f51d07-e097-4c5d-b23a-92ca8fa5f45f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2VwDpQYoNC9R15usYrmkU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 23542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 778
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017C8Z3NoxSjKYPyLVAR6CXH`</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "cat -n /root/prism_collapse_mixing/compute_signals.py",
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
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "2386a409-9b79-4522-abf5-367f3897644b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2VwDpQYoNC9R15usYrmkU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 23542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 778
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

<details open><summary>🔧 Tool call — Read · `toolu_01151oTtrXfnWZ2HER8X5fUY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/prism_collapse_mixing/artifacts/paper_skeleton.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "4d1b9e23-2db9-48f7-8262-3234fa5b6237",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2VwDpQYoNC9R15usYrmkU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 23542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 778
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

_source line 10 · 2026-05-16T02:01:01.636Z_

<details><summary>↩ Tool result · `toolu_017C8Z3NoxSjKYPyLVAR6CXH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\tcompute_signals.py — Compute per-example and corpus-level collapse signals.\\n     3\\tPer-example: loss, entropy, spectral_rank (5000-d vectors).\\n     4\\tCorpus-level: sigma_spectral_rank, distinct-n.\\n     5\\tPlus per-generation Spearman rho between per-example signals.\\n     6\\t\\\"\\\"\\\"\\n     7\\t\\n     8\\timport os\\n     9\\timport json\\n    10\\timport math\\n    11\\timport random\\n    12\\timport argparse\\n    13\\timport numpy as np\\n    14\\timport torch\\n    15\\tfrom torch.utils.data import Dataset, DataLoader\\n    16\\tfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n    17\\tfrom tqdm import tqdm\\n    18\\tfrom scipy.stats import spearmanr\\n    19\\t\\n    20\\t\\n    21\\tdef set_seed(seed):\\n    22\\t    random.seed(seed)\\n    23\\t    np.random.seed(seed)\\n    24\\t    torch.manual_seed(seed)\\n    25\\t    torch.cuda.manual_seed_all(seed)\\n    26\\t\\n    27\\t\\n    28\\tclass TokenizedDataset(Dataset):\\n    29\\t\\n    30\\t    def __init__(self, path, tokenizer, max_len):\\n    31\\t        self.samples = []\\n    32\\t        with open(path) as f:\\n    33\\t            for line in f:\\n    34\\t                toks = tokenizer.encode(json.loads(line)[\\\"text\\\"], add_special_tokens=False)[:max_len]\\n    35\\t                if len(toks) >= 16:\\n    36\\t                    self.samples.append(torch.tensor(toks, dtype=torch.long))\\n    37\\t\\n    38\\t    def __len__(self):\\n    39\\t        return len(self.samples)\\n    40\\t\\n    41\\t    def __getitem__(self, idx):\\n    42\\t        return self.samples[idx]\\n    43\\t\\n    44\\t\\n    45\\tdef collate_padded(batch, pad_id):\\n    46\\t    ml = max(len(x) for x in batch)\\n    47\\t    ids = torch.full((len(batch), ml), pad_id, dtype=torch.long)\\n    48\\t    mask = torch.zeros(len(batch), ml, dtype=torch.long)\\n    49\\t    for i, x in enumerate(batch):\\n    50\\t        ids[i, :len(x)] = x\\n    51\\t        mask[i, :len(x)] = 1\\n    52\\t    return {\\\"input_ids\\\": ids, \\\"attention_mask\\\": mask}\\n    53\\t\\n    54\\t\\n    55\\tdef effective_rank(S):\\n    56\\t    \\\"\\\"\\\"Effective rank from singular values: exp(H(normalized_sv)).\\\"\\\"\\\"\\n    57\\t    s = S / S.sum()\\n    58\\t    s = s[s > 0]\\n    59\\t    H = -(s * torch.log(s)).sum().item()\\n    60\\t    return math.exp(H)\\n    61\\t\\n    62\\t\\n    63\\tdef compute_per_example_signals(model, tokenizer, probe_path, device, max_len=256, batch_size=16):\\n    64\\t    \\\"\\\"\\\"Single forward pass computing per-example loss, entropy, spectral_rank\\n    65\\t    plus collecting mean-pooled hidden states for corpus-level sigma.\\\"\\\"\\\"\\n    66\\t    ds = TokenizedDataset(probe_path, tokenizer, max_len)\\n    67\\t    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\\n    68\\t    loader = DataLoader(ds, batch_size=batch_size, collate_fn=lambda b: collate_padded(b, pad_id))\\n    69\\t\\n    70\\t    loss_fn = torch.nn.CrossEntropyLoss(reduction=\\\"none\\\")\\n    71\\t    all_loss = []\\n    72\\t    all_entropy = []\\n    73\\t    all_spectral_rank = []\\n    74\\t    all_mean_hidden = []\\n    75\\t\\n    76\\t    _last_hidden = {}\\n    77\\t    def _capture_last_hidden(module, inp, output):\\n    78\\t        _last_hidden['val'] = output[0].detach()\\n    79\\t    _hook = model.gpt_neox.layers[-1].register_forward_hook(_capture_last_hidden)\\n    80\\t\\n    81\\t    for batch in tqdm(loader, desc=\\\"per-example signals\\\"):\\n    82\\t        ids = batch[\\\"input_ids\\\"].to(device)\\n    83\\t        amask = batch[\\\"attention_mask\\\"].to(device)\\n    84\\t\\n    85\\t        with torch.no_grad():\\n    86\\t            out = model(input_ids=ids, attention_mask=amask)\\n    87\\t\\n    88\\t        logits = out.logits       # [B, L, V]\\n    89\\t        hidden = _last_hidden['val']  # [B, L, D]\\n    90\\t\\n    91\\t        # --- Per-example loss ---\\n    92\\t        shift_logits = logits[:, :-1, :].contiguous()\\n    93\\t        shift_labels = ids[:, 1:].contiguous()\\n    94\\t        shift_mask = amask[:, 1:].float()\\n    95\\t        B, L1, V = shift_logits.shape\\n    96\\t        token_loss = loss_fn(\\n    97\\t            shift_logits.view(-1, V).float(), shift_labels.view(-1)\\n    98\\t        ).view(B, L1)\\n    99\\t        token_loss = token_loss * shift_mask\\n   100\\t        seq_lo\\n\\n... [截断: 输出过长，省略 4397 字符] ...\\n\\n    parser.add_argument(\\\"--gen_max_new_tokens\\\", type=int, default=128, help=\\\"Max new tokens for distinct-n\\\")\\n   183\\t    parser.add_argument(\\\"--batch_size\\\", type=int, default=16, help=\\\"Inference batch size\\\")\\n   184\\t    args = parser.parse_args()\\n   185\\t\\n   186\\t    set_seed(args.seed)\\n   187\\t    device = torch.device(args.device)\\n   188\\t\\n   189\\t    print(f\\\"Loading {args.model_path}...\\\")\\n   190\\t    tokenizer = AutoTokenizer.from_pretrained(args.model_path)\\n   191\\t    if tokenizer.pad_token is None:\\n   192\\t        tokenizer.pad_token = tokenizer.eos_token\\n   193\\t    model = AutoModelForCausalLM.from_pretrained(\\n   194\\t        args.model_path, torch_dtype=torch.bfloat16\\n   195\\t    ).to(device)\\n   196\\t    model.eval()\\n   197\\t\\n   198\\t    # 1/3 Per-example signals + corpus-level sigma\\n   199\\t    print(\\\"1/3 Per-example signals (loss, entropy, spectral_rank) + sigma...\\\")\\n   200\\t    loss_vec, ent_vec, srank_vec, sigma_rank = compute_per_example_signals(\\n   201\\t        model, tokenizer, args.probe_set_path, device, batch_size=args.batch_size\\n   202\\t    )\\n   203\\t\\n   204\\t    # 2/3 Corpus-level distinct-n\\n   205\\t    print(\\\"2/3 Distinct-n...\\\")\\n   206\\t    dn = compute_distinct_n(\\n   207\\t        model, tokenizer, args.probe_set_path, device,\\n   208\\t        prefix_len=args.gen_prefix_len,\\n   209\\t        max_new=args.gen_max_new_tokens,\\n   210\\t        batch_size=args.batch_size,\\n   211\\t    )\\n   212\\t\\n   213\\t    # 3/3 Spearman correlations\\n   214\\t    print(\\\"3/3 Spearman correlations...\\\")\\n   215\\t    rho_le, pval_le = spearmanr(loss_vec, ent_vec)\\n   216\\t    rho_ls, pval_ls = spearmanr(loss_vec, srank_vec)\\n   217\\t\\n   218\\t    loss_arr = np.array(loss_vec)\\n   219\\t    ent_arr = np.array(ent_vec)\\n   220\\t    srank_arr = np.array(srank_vec)\\n   221\\t\\n   222\\t    result = {\\n   223\\t        \\\"gen\\\": args.gen,\\n   224\\t        \\\"seed\\\": args.seed,\\n   225\\t        \\\"per_example\\\": {\\n   226\\t            \\\"loss\\\": [round(x, 4) for x in loss_vec],\\n   227\\t            \\\"entropy\\\": [round(x, 4) for x in ent_vec],\\n   228\\t            \\\"spectral_rank\\\": [round(x, 2) for x in srank_vec],\\n   229\\t        },\\n   230\\t        \\\"aggregated\\\": {\\n   231\\t            \\\"loss_mean\\\": round(float(loss_arr.mean()), 4),\\n   232\\t            \\\"loss_std\\\": round(float(loss_arr.std()), 4),\\n   233\\t            \\\"entropy_mean\\\": round(float(ent_arr.mean()), 4),\\n   234\\t            \\\"entropy_std\\\": round(float(ent_arr.std()), 4),\\n   235\\t            \\\"spectral_rank_mean\\\": round(float(srank_arr.mean()), 2),\\n   236\\t            \\\"spectral_rank_std\\\": round(float(srank_arr.std()), 2),\\n   237\\t        },\\n   238\\t        \\\"corpus_level\\\": {\\n   239\\t            \\\"sigma_spectral_rank\\\": round(sigma_rank, 2),\\n   240\\t            \\\"distinct_1\\\": round(dn[\\\"distinct_1\\\"], 4),\\n   241\\t            \\\"distinct_2\\\": round(dn[\\\"distinct_2\\\"], 4),\\n   242\\t            \\\"distinct_3\\\": round(dn[\\\"distinct_3\\\"], 4),\\n   243\\t        },\\n   244\\t        \\\"correlations\\\": {\\n   245\\t            \\\"rho_loss_entropy\\\": round(float(rho_le), 4),\\n   246\\t            \\\"pval_loss_entropy\\\": round(float(pval_le), 6),\\n   247\\t            \\\"rho_loss_spectral_rank\\\": round(float(rho_ls), 4),\\n   248\\t            \\\"pval_loss_spectral_rank\\\": round(float(pval_ls), 6),\\n   249\\t        },\\n   250\\t        \\\"num_probe_samples\\\": len(loss_vec),\\n   251\\t    }\\n   252\\t\\n   253\\t    os.makedirs(os.path.dirname(os.path.abspath(args.output_path)), exist_ok=True)\\n   254\\t    with open(args.output_path, \\\"w\\\") as f:\\n   255\\t        json.dump(result, f, indent=2)\\n   256\\t    print(f\\\"\\\\nSignals saved to {args.output_path}\\\")\\n   257\\t    print(f\\\"  loss: mean={loss_arr.mean():.4f} std={loss_arr.std():.4f}\\\")\\n   258\\t    print(f\\\"  entropy: mean={ent_arr.mean():.4f} std={ent_arr.std():.4f}\\\")\\n   259\\t    print(f\\\"  spectral_rank: mean={srank_arr.mean():.2f} std={srank_arr.std():.2f}\\\")\\n   260\\t    print(f\\\"  sigma_rank: {sigma_rank:.2f}\\\")\\n   261\\t    print(f\\\"  rho(loss,entropy)={rho_le:.4f} p={pval_le:.6f}\\\")\\n   262\\t    print(f\\\"  rho(loss,spectral_rank)={rho_ls:.4f} p={pval_ls:.6f}\\\")\\n   263\\t\\n   264\\t\\n   265\\tif __name__ == \\\"__main__\\\":\\n   266\\t    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "69794ad2-f7c9-4419-8a65-319b52f5564f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"     1\\\\t\\\\\\\"\\\\\\\"\\\\\\\"\\\\n     2\\\\tcompute_signals.py — Compute per-example and corpus-level collapse signals.\\\\n     3\\\\tPer-example: loss, entropy, spectral_rank (5000-d vectors).\\\\n     4\\\\tCorpus-level: sigma_spectral_rank, distinct-n.\\\\n     5\\\\tPlus per-generation Spearman rho between per-example signals.\\\\n     6\\\\t\\\\\\\"\\\\\\\"\\\\\\\"\\\\n     7\\\\t\\\\n     8\\\\timport os\\\\n     9\\\\timport json\\\\n    10\\\\timport math\\\\n    11\\\\timport random\\\\n    12\\\\timport argparse\\\\n    13\\\\timport numpy as np\\\\n    14\\\\timport torch\\\\n    15\\\\tfrom torch.utils.data import Dataset, DataLoader\\\\n    16\\\\tfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n    17\\\\tfrom tqdm import tqdm\\\\n    18\\\\tfrom scipy.stats import spearmanr\\\\n    19\\\\t\\\\n    20\\\\t\\\\n    21\\\\tdef set_seed(seed):\\\\n    22\\\\t    random.seed(seed)\\\\n    23\\\\t    np.random.seed(seed)\\\\n    24\\\\t    torch.manual_seed(seed)\\\\n    25\\\\t    torch.cuda.manual_seed_all(seed)\\\\n    26\\\\t\\\\n    27\\\\t\\\\n    28\\\\tclass TokenizedDataset(Dataset):\\\\n    29\\\\t\\\\n    30\\\\t    def __init__(self, path, tokenizer, max_len):\\\\n    31\\\\t        self.samples = []\\\\n    32\\\\t        with open(path) as f:\\\\n    33\\\\t            for line in f:\\\\n    34\\\\t                toks = tokenizer.encode(json.loads(line)[\\\\\\\"text\\\\\\\"], add_special_tokens=False)[:max_len]\\\\n    35\\\\t                if len(toks) >= 16:\\\\n    36\\\\t                    self.samples.append(torch.tensor(toks, dtype=torch.long))\\\\n    37\\\\t\\\\n    38\\\\t    def __len__(self):\\\\n    39\\\\t        return len(self.samples)\\\\n    40\\\\t\\\\n    41\\\\t    def __getitem__(self, idx):\\\\n    42\\\\t        return self.samples[idx]\\\\n    43\\\\t\\\\n    44\\\\t\\\\n    45\\\\tdef collate_padded(batch, pad_id):\\\\n    46\\\\t    ml = max(len(x) for x in batch)\\\\n    47\\\\t    ids = torch.full((len(batch), ml), pad_id, dtype=torch.long)\\\\n    48\\\\t    mask = torch.zeros(len(batch), ml, dtype=torch.long)\\\\n    49\\\\t    for i, x in enumerate(batch):\\\\n    50\\\\t        ids[i, :len(x)] = x\\\\n    51\\\\t        mask[i, :len(x)] = 1\\\\n    52\\\\t    return {\\\\\\\"input_ids\\\\\\\": ids, \\\\\\\"attention_mask\\\\\\\": mask}\\\\n    53\\\\t\\\\n    54\\\\t\\\\n    55\\\\tdef effective_rank(S):\\\\n    56\\\\t    \\\\\\\"\\\\\\\"\\\\\\\"Effective rank from singular values: exp(H(normalized_sv)).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    57\\\\t    s = S / S.sum()\\\\n    58\\\\t    s = s[s > 0]\\\\n    59\\\\t    H = -(s * torch.log(s)).sum().item()\\\\n    60\\\\t    return math.exp(H)\\\\n    61\\\\t\\\\n    62\\\\t\\\\n    63\\\\tdef compute_per_example_signals(model, tokenizer, probe_path, device, max_len=256, batch_size=16):\\\\n    64\\\\t    \\\\\\\"\\\\\\\"\\\\\\\"Single forward pass computing per-example loss, entropy, spectral_rank\\\\n    65\\\\t    plus collecting mean-pooled hidden states for corpus-level sigma.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    66\\\\t    ds = TokenizedDataset(probe_path, tokenizer, max_len)\\\\n    67\\\\t    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\\\\n    68\\\\t    loader = DataLoader(ds, batch_size=batch_size, collate_fn=lambda b: collate_padded(b, pad_id))\\\\n    69\\\\t\\\\n    70\\\\t    loss_fn = torch.nn.CrossEntropyLoss(reduction=\\\\\\\"none\\\\\\\")\\\\n    71\\\\t    all_loss = []\\\\n    72\\\\t    all_entropy = []\\\\n    73\\\\t    all_spectral_rank = []\\\\n    74\\\\t    all_mean_hidden = []\\\\n    75\\\\t\\\\n    76\\\\t    _last_hidden = {}\\\\n    77\\\\t    def _capture_last_hidden(module, inp, output):\\\\n    78\\\\t        _last_hidden['val'] = output[0].detach()\\\\n    79\\\\t    _hook = model.gpt_neox.layers[-1].register_forward_hook(_capture_last_hidden)\\\\n    80\\\\t\\\\n    81\\\\t    for batch in tqdm(loader, desc=\\\\\\\"per-example signals\\\\\\\"):\\\\n    82\\\\t        ids = batch[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n    83\\\\t        amask = batch[\\\\\\\"attention_mask\\\\\\\"].to(device)\\\\n    84\\\\t\\\\n    85\\\\t        with torch.no_grad():\\\\n    86\\\\t            out = model(input_ids=ids, attention_mask=amask)\\\\n    87\\\\t\\\\n    88\\\\t        logits = out.logits       # [B, L, V]\\\\n    89\\\\t        hidden = _last_hidden['val']  # [B, L, D]\\\\n    90\\\\t\\\\n    91\\\\t        # --- Per-example loss ---\\\\n    92\\\\t        shift_logits = logits[:, :-1, :].contiguous()\\\\n    93\\\\t        shift_labels = ids[:, 1:].contiguous()\\\\n    94\\\\t        shift_mask = amask[:, 1:].float()\\\\n    95\\\\t        B, L1, V = shift_logits.shape\\\\n    96\\\\t        token_loss = loss_fn(\\\\n    97\\\\t            shift_logits.view(-1, V).float(), shift_labels.view(-1)\\\\n    98\\\\t        ).view(B, L1)\\\\n    99\\\\t        token_loss = token_loss * shift_mask\\\\n   100\\\\t        seq_lo\\\\n\\\\n... [截断: 输出过长，省略 4397 字符] ...\\\\n\\\\n    parser.add_argument(\\\\\\\"--gen_max_new_tokens\\\\\\\", type=int, default=128, help=\\\\\\\"Max new tokens for distinct-n\\\\\\\")\\\\n   183\\\\t    parser.add_argument(\\\\\\\"--batch_size\\\\\\\", type=int, default=16, help=\\\\\\\"Inference batch size\\\\\\\")\\\\n   184\\\\t    args = parser.parse_args()\\\\n   185\\\\t\\\\n   186\\\\t    set_seed(args.seed)\\\\n   187\\\\t    device = torch.device(args.device)\\\\n   188\\\\t\\\\n   189\\\\t    print(f\\\\\\\"Loading {args.model_path}...\\\\\\\")\\\\n   190\\\\t    tokenizer = AutoTokenizer.from_pretrained(args.model_path)\\\\n   191\\\\t    if tokenizer.pad_token is None:\\\\n   192\\\\t        tokenizer.pad_token = tokenizer.eos_token\\\\n   193\\\\t    model = AutoModelForCausalLM.from_pretrained(\\\\n   194\\\\t        args.model_path, torch_dtype=torch.bfloat16\\\\n   195\\\\t    ).to(device)\\\\n   196\\\\t    model.eval()\\\\n   197\\\\t\\\\n   198\\\\t    # 1/3 Per-example signals + corpus-level sigma\\\\n   199\\\\t    print(\\\\\\\"1/3 Per-example signals (loss, entropy, spectral_rank) + sigma...\\\\\\\")\\\\n   200\\\\t    loss_vec, ent_vec, srank_vec, sigma_rank = compute_per_example_signals(\\\\n   201\\\\t        model, tokenizer, args.probe_set_path, device, batch_size=args.batch_size\\\\n   202\\\\t    )\\\\n   203\\\\t\\\\n   204\\\\t    # 2/3 Corpus-level distinct-n\\\\n   205\\\\t    print(\\\\\\\"2/3 Distinct-n...\\\\\\\")\\\\n   206\\\\t    dn = compute_distinct_n(\\\\n   207\\\\t        model, tokenizer, args.probe_set_path, device,\\\\n   208\\\\t        prefix_len=args.gen_prefix_len,\\\\n   209\\\\t        max_new=args.gen_max_new_tokens,\\\\n   210\\\\t        batch_size=args.batch_size,\\\\n   211\\\\t    )\\\\n   212\\\\t\\\\n   213\\\\t    # 3/3 Spearman correlations\\\\n   214\\\\t    print(\\\\\\\"3/3 Spearman correlations...\\\\\\\")\\\\n   215\\\\t    rho_le, pval_le = spearmanr(loss_vec, ent_vec)\\\\n   216\\\\t    rho_ls, pval_ls = spearmanr(loss_vec, srank_vec)\\\\n   217\\\\t\\\\n   218\\\\t    loss_arr = np.array(loss_vec)\\\\n   219\\\\t    ent_arr = np.array(ent_vec)\\\\n   220\\\\t    srank_arr = np.array(srank_vec)\\\\n   221\\\\t\\\\n   222\\\\t    result = {\\\\n   223\\\\t        \\\\\\\"gen\\\\\\\": args.gen,\\\\n   224\\\\t        \\\\\\\"seed\\\\\\\": args.seed,\\\\n   225\\\\t        \\\\\\\"per_example\\\\\\\": {\\\\n   226\\\\t            \\\\\\\"loss\\\\\\\": [round(x, 4) for x in loss_vec],\\\\n   227\\\\t            \\\\\\\"entropy\\\\\\\": [round(x, 4) for x in ent_vec],\\\\n   228\\\\t            \\\\\\\"spectral_rank\\\\\\\": [round(x, 2) for x in srank_vec],\\\\n   229\\\\t        },\\\\n   230\\\\t        \\\\\\\"aggregated\\\\\\\": {\\\\n   231\\\\t            \\\\\\\"loss_mean\\\\\\\": round(float(loss_arr.mean()), 4),\\\\n   232\\\\t            \\\\\\\"loss_std\\\\\\\": round(float(loss_arr.std()), 4),\\\\n   233\\\\t            \\\\\\\"entropy_mean\\\\\\\": round(float(ent_arr.mean()), 4),\\\\n   234\\\\t            \\\\\\\"entropy_std\\\\\\\": round(float(ent_arr.std()), 4),\\\\n   235\\\\t            \\\\\\\"spectral_rank_mean\\\\\\\": round(float(srank_arr.mean()), 2),\\\\n   236\\\\t            \\\\\\\"spectral_rank_std\\\\\\\": round(float(srank_arr.std()), 2),\\\\n   237\\\\t        },\\\\n   238\\\\t        \\\\\\\"corpus_level\\\\\\\": {\\\\n   239\\\\t            \\\\\\\"sigma_spectral_rank\\\\\\\": round(sigma_rank, 2),\\\\n   240\\\\t            \\\\\\\"distinct_1\\\\\\\": round(dn[\\\\\\\"distinct_1\\\\\\\"], 4),\\\\n   241\\\\t            \\\\\\\"distinct_2\\\\\\\": round(dn[\\\\\\\"distinct_2\\\\\\\"], 4),\\\\n   242\\\\t            \\\\\\\"distinct_3\\\\\\\": round(dn[\\\\\\\"distinct_3\\\\\\\"], 4),\\\\n   243\\\\t        },\\\\n   244\\\\t        \\\\\\\"correlations\\\\\\\": {\\\\n   245\\\\t            \\\\\\\"rho_loss_entropy\\\\\\\": round(float(rho_le), 4),\\\\n   246\\\\t            \\\\\\\"pval_loss_entropy\\\\\\\": round(float(pval_le), 6),\\\\n   247\\\\t            \\\\\\\"rho_loss_spectral_rank\\\\\\\": round(float(rho_ls), 4),\\\\n   248\\\\t            \\\\\\\"pval_loss_spectral_rank\\\\\\\": round(float(pval_ls), 6),\\\\n   249\\\\t        },\\\\n   250\\\\t        \\\\\\\"num_probe_samples\\\\\\\": len(loss_vec),\\\\n   251\\\\t    }\\\\n   252\\\\t\\\\n   253\\\\t    os.makedirs(os.path.dirname(os.path.abspath(args.output_path)), exist_ok=True)\\\\n   254\\\\t    with open(args.output_path, \\\\\\\"w\\\\\\\") as f:\\\\n   255\\\\t        json.dump(result, f, indent=2)\\\\n   256\\\\t    print(f\\\\\\\"\\\\\\\\nSignals saved to {args.output_path}\\\\\\\")\\\\n   257\\\\t    print(f\\\\\\\"  loss: mean={loss_arr.mean():.4f} std={loss_arr.std():.4f}\\\\\\\")\\\\n   258\\\\t    print(f\\\\\\\"  entropy: mean={ent_arr.mean():.4f} std={ent_arr.std():.4f}\\\\\\\")\\\\n   259\\\\t    print(f\\\\\\\"  spectral_rank: mean={srank_arr.mean():.2f} std={srank_arr.std():.2f}\\\\\\\")\\\\n   260\\\\t    print(f\\\\\\\"  sigma_rank: {sigma_rank:.2f}\\\\\\\")\\\\n   261\\\\t    print(f\\\\\\\"  rho(loss,entropy)={rho_le:.4f} p={pval_le:.6f}\\\\\\\")\\\\n   262\\\\t    print(f\\\\\\\"  rho(loss,spectral_rank)={rho_ls:.4f} p={pval_ls:.6f}\\\\\\\")\\\\n   263\\\\t\\\\n   264\\\\t\\\\n   265\\\\tif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n   266\\\\t    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.25}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\tcompute_signals.py — Compute per-example and corpus-level collapse signals.\\n     3\\tPer-example: loss, entropy, spectral_rank (5000-d vectors).\\n     4\\tCorpus-level: sigma_spectral_rank, distinct-n.\\n     5\\tPlus per-generation Spearman rho between per-example signals.\\n     6\\t\\\"\\\"\\\"\\n     7\\t\\n     8\\timport os\\n     9\\timport json\\n    10\\timport math\\n    11\\timport random\\n    12\\timport argparse\\n    13\\timport numpy as np\\n    14\\timport torch\\n    15\\tfrom torch.utils.data import Dataset, DataLoader\\n    16\\tfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n    17\\tfrom tqdm import tqdm\\n    18\\tfrom scipy.stats import spearmanr\\n    19\\t\\n    20\\t\\n    21\\tdef set_seed(seed):\\n    22\\t    random.seed(seed)\\n    23\\t    np.random.seed(seed)\\n    24\\t    torch.manual_seed(seed)\\n    25\\t    torch.cuda.manual_seed_all(seed)\\n    26\\t\\n    27\\t\\n    28\\tclass TokenizedDataset(Dataset):\\n    29\\t\\n    30\\t    def __init__(self, path, tokenizer, max_len):\\n    31\\t        self.samples = []\\n    32\\t        with open(path) as f:\\n    33\\t            for line in f:\\n    34\\t                toks = tokenizer.encode(json.loads(line)[\\\"text\\\"], add_special_tokens=False)[:max_len]\\n    35\\t                if len(toks) >= 16:\\n    36\\t                    self.samples.append(torch.tensor(toks, dtype=torch.long))\\n    37\\t\\n    38\\t    def __len__(self):\\n    39\\t        return len(self.samples)\\n    40\\t\\n    41\\t    def __getitem__(self, idx):\\n    42\\t        return self.samples[idx]\\n    43\\t\\n    44\\t\\n    45\\tdef collate_padded(batch, pad_id):\\n    46\\t    ml = max(len(x) for x in batch)\\n    47\\t    ids = torch.full((len(batch), ml), pad_id, dtype=torch.long)\\n    48\\t    mask = torch.zeros(len(batch), ml, dtype=torch.long)\\n    49\\t    for i, x in enumerate(batch):\\n    50\\t        ids[i, :len(x)] = x\\n    51\\t        mask[i, :len(x)] = 1\\n    52\\t    return {\\\"input_ids\\\": ids, \\\"attention_mask\\\": mask}\\n    53\\t\\n    54\\t\\n    55\\tdef effective_rank(S):\\n    56\\t    \\\"\\\"\\\"Effective rank from singular values: exp(H(normalized_sv)).\\\"\\\"\\\"\\n    57\\t    s = S / S.sum()\\n    58\\t    s = s[s > 0]\\n    59\\t    H = -(s * torch.log(s)).sum().item()\\n    60\\t    return math.exp(H)\\n    61\\t\\n    62\\t\\n    63\\tdef compute_per_example_signals(model, tokenizer, probe_path, device, max_len=256, batch_size=16):\\n    64\\t    \\\"\\\"\\\"Single forward pass computing per-example loss, entropy, spectral_rank\\n    65\\t    plus collecting mean-pooled hidden states for corpus-level sigma.\\\"\\\"\\\"\\n    66\\t    ds = TokenizedDataset(probe_path, tokenizer, max_len)\\n    67\\t    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\\n    68\\t    loader = DataLoader(ds, batch_size=batch_size, collate_fn=lambda b: collate_padded(b, pad_id))\\n    69\\t\\n    70\\t    loss_fn = torch.nn.CrossEntropyLoss(reduction=\\\"none\\\")\\n    71\\t    all_loss = []\\n    72\\t    all_entropy = []\\n    73\\t    all_spectral_rank = []\\n    74\\t    all_mean_hidden = []\\n    75\\t\\n    76\\t    _last_hidden = {}\\n    77\\t    def _capture_last_hidden(module, inp, output):\\n    78\\t        _last_hidden['val'] = output[0].detach()\\n    79\\t    _hook = model.gpt_neox.layers[-1].register_forward_hook(_capture_last_hidden)\\n    80\\t\\n    81\\t    for batch in tqdm(loader, desc=\\\"per-example signals\\\"):\\n    82\\t        ids = batch[\\\"input_ids\\\"].to(device)\\n    83\\t        amask = batch[\\\"attention_mask\\\"].to(device)\\n    84\\t\\n    85\\t        with torch.no_grad():\\n    86\\t            out = model(input_ids=ids, attention_mask=amask)\\n    87\\t\\n    88\\t        logits = out.logits       # [B, L, V]\\n    89\\t        hidden = _last_hidden['val']  # [B, L, D]\\n    90\\t\\n    91\\t        # --- Per-example loss ---\\n    92\\t        shift_logits = logits[:, :-1, :].contiguous()\\n    93\\t        shift_labels = ids[:, 1:].contiguous()\\n    94\\t        shift_mask = amask[:, 1:].float()\\n    95\\t        B, L1, V = shift_logits.shape\\n    96\\t        token_loss = loss_fn(\\n    97\\t            shift_logits.view(-1, V).float(), shift_labels.view(-1)\\n    98\\t        ).view(B, L1)\\n    99\\t        token_loss = token_loss * shift_mask\\n   100\\t        seq_lo\\n\\n... [截断: 输出过长，省略 4397 字符] ...\\n\\n    parser.add_argument(\\\"--gen_max_new_tokens\\\", type=int, default=128, help=\\\"Max new tokens for distinct-n\\\")\\n   183\\t    parser.add_argument(\\\"--batch_size\\\", type=int, default=16, help=\\\"Inference batch size\\\")\\n   184\\t    args = parser.parse_args()\\n   185\\t\\n   186\\t    set_seed(args.seed)\\n   187\\t    device = torch.device(args.device)\\n   188\\t\\n   189\\t    print(f\\\"Loading {args.model_path}...\\\")\\n   190\\t    tokenizer = AutoTokenizer.from_pretrained(args.model_path)\\n   191\\t    if tokenizer.pad_token is None:\\n   192\\t        tokenizer.pad_token = tokenizer.eos_token\\n   193\\t    model = AutoModelForCausalLM.from_pretrained(\\n   194\\t        args.model_path, torch_dtype=torch.bfloat16\\n   195\\t    ).to(device)\\n   196\\t    model.eval()\\n   197\\t\\n   198\\t    # 1/3 Per-example signals + corpus-level sigma\\n   199\\t    print(\\\"1/3 Per-example signals (loss, entropy, spectral_rank) + sigma...\\\")\\n   200\\t    loss_vec, ent_vec, srank_vec, sigma_rank = compute_per_example_signals(\\n   201\\t        model, tokenizer, args.probe_set_path, device, batch_size=args.batch_size\\n   202\\t    )\\n   203\\t\\n   204\\t    # 2/3 Corpus-level distinct-n\\n   205\\t    print(\\\"2/3 Distinct-n...\\\")\\n   206\\t    dn = compute_distinct_n(\\n   207\\t        model, tokenizer, args.probe_set_path, device,\\n   208\\t        prefix_len=args.gen_prefix_len,\\n   209\\t        max_new=args.gen_max_new_tokens,\\n   210\\t        batch_size=args.batch_size,\\n   211\\t    )\\n   212\\t\\n   213\\t    # 3/3 Spearman correlations\\n   214\\t    print(\\\"3/3 Spearman correlations...\\\")\\n   215\\t    rho_le, pval_le = spearmanr(loss_vec, ent_vec)\\n   216\\t    rho_ls, pval_ls = spearmanr(loss_vec, srank_vec)\\n   217\\t\\n   218\\t    loss_arr = np.array(loss_vec)\\n   219\\t    ent_arr = np.array(ent_vec)\\n   220\\t    srank_arr = np.array(srank_vec)\\n   221\\t\\n   222\\t    result = {\\n   223\\t        \\\"gen\\\": args.gen,\\n   224\\t        \\\"seed\\\": args.seed,\\n   225\\t        \\\"per_example\\\": {\\n   226\\t            \\\"loss\\\": [round(x, 4) for x in loss_vec],\\n   227\\t            \\\"entropy\\\": [round(x, 4) for x in ent_vec],\\n   228\\t            \\\"spectral_rank\\\": [round(x, 2) for x in srank_vec],\\n   229\\t        },\\n   230\\t        \\\"aggregated\\\": {\\n   231\\t            \\\"loss_mean\\\": round(float(loss_arr.mean()), 4),\\n   232\\t            \\\"loss_std\\\": round(float(loss_arr.std()), 4),\\n   233\\t            \\\"entropy_mean\\\": round(float(ent_arr.mean()), 4),\\n   234\\t            \\\"entropy_std\\\": round(float(ent_arr.std()), 4),\\n   235\\t            \\\"spectral_rank_mean\\\": round(float(srank_arr.mean()), 2),\\n   236\\t            \\\"spectral_rank_std\\\": round(float(srank_arr.std()), 2),\\n   237\\t        },\\n   238\\t        \\\"corpus_level\\\": {\\n   239\\t            \\\"sigma_spectral_rank\\\": round(sigma_rank, 2),\\n   240\\t            \\\"distinct_1\\\": round(dn[\\\"distinct_1\\\"], 4),\\n   241\\t            \\\"distinct_2\\\": round(dn[\\\"distinct_2\\\"], 4),\\n   242\\t            \\\"distinct_3\\\": round(dn[\\\"distinct_3\\\"], 4),\\n   243\\t        },\\n   244\\t        \\\"correlations\\\": {\\n   245\\t            \\\"rho_loss_entropy\\\": round(float(rho_le), 4),\\n   246\\t            \\\"pval_loss_entropy\\\": round(float(pval_le), 6),\\n   247\\t            \\\"rho_loss_spectral_rank\\\": round(float(rho_ls), 4),\\n   248\\t            \\\"pval_loss_spectral_rank\\\": round(float(pval_ls), 6),\\n   249\\t        },\\n   250\\t        \\\"num_probe_samples\\\": len(loss_vec),\\n   251\\t    }\\n   252\\t\\n   253\\t    os.makedirs(os.path.dirname(os.path.abspath(args.output_path)), exist_ok=True)\\n   254\\t    with open(args.output_path, \\\"w\\\") as f:\\n   255\\t        json.dump(result, f, indent=2)\\n   256\\t    print(f\\\"\\\\nSignals saved to {args.output_path}\\\")\\n   257\\t    print(f\\\"  loss: mean={loss_arr.mean():.4f} std={loss_arr.std():.4f}\\\")\\n   258\\t    print(f\\\"  entropy: mean={ent_arr.mean():.4f} std={ent_arr.std():.4f}\\\")\\n   259\\t    print(f\\\"  spectral_rank: mean={srank_arr.mean():.2f} std={srank_arr.std():.2f}\\\")\\n   260\\t    print(f\\\"  sigma_rank: {sigma_rank:.2f}\\\")\\n   261\\t    print(f\\\"  rho(loss,entropy)={rho_le:.4f} p={pval_le:.6f}\\\")\\n   262\\t    print(f\\\"  rho(loss,spectral_rank)={rho_ls:.4f} p={pval_ls:.6f}\\\")\\n   263\\t\\n   264\\t\\n   265\\tif __name__ == \\\"__main__\\\":\\n   266\\t    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T02:01:01.649Z_

<details><summary>↩ Tool result · `toolu_01151oTtrXfnWZ2HER8X5fUY`</summary>

```text
1	# PRISM: Probing the Decoupling of Loss and Collapse Signals in Iterative Synthetic Training
2	
3	---
4	
5	## 2. Related Work
6	
7	### 2.1 Model Collapse in Iterative Training
8	
9	Training generative models on their own outputs across successive generations leads to *model collapse*—a progressive loss of distributional fidelity that manifests as tail truncation and mode reduction. Shumailov et al. (2024) established this phenomenon across LLMs, VAEs, and GMMs, showing that distribution tails vanish first while bulk statistics remain superficially intact. Dohmatob et al. (2025) provided a theoretical grounding through the lens of the data processing inequality (DPI), proving that even trace amounts of synthetic contamination (as low as 1/1000) suffice to trigger collapse under iterative retraining, with degradation following an exponential decay in effective distributional support.
10	
11	A critical design variable is whether synthetic data *replaces* or *accumulates* alongside real data across generations. Gerstgrasser et al. (2024) demonstrated that accumulation strategies can avoid collapse entirely, while replacement strategies—where each generation discards prior data—reliably induce it. Our experimental design deliberately adopts the replacement paradigm (fixed 50/50 real-synthetic ratio, re-generated each generation) to create conditions under which collapse is expected, enabling controlled study of its detection.
12	
13	Schaeffer et al. (2025) drew attention to definitional ambiguity in the collapse literature, cataloguing eight distinct operationalizations. They argued that population-level risk (i.e., validation loss) can remain stable even as tail risk deteriorates—a conceptual precursor to the loss–signal decoupling we investigate. Yi et al. (2025) showed that external verifiers injecting fresh information can prevent collapse, suggesting that if collapse signals can serve as verification criteria, they may enable principled data filtering in iterative pipelines.
14	
15	### 2.2 Data Mixing Strategies
16	
17	Online data mixing methods dynamically adjust domain proportions during training to optimize learning efficiency. DoReMi (Xie et al., 2024) uses a small proxy model to reweight domain mixtures via distributionally robust optimization. AIOLI (Chen et al., 2024) extends this with online gradient-based updates to mixing coefficients. ODM (Fan et al., 2024) optimizes domain mixtures by tracking per-domain loss trajectories.
18	
19	These methods share a common dependency: they use *loss* (or loss-derived gradients) as the sole signal for mixture adjustment. This is well-motivated when training data is static and well-characterized, but becomes problematic in iterative synthetic training where the data distribution itself degrades across generations. If collapse manifests in ways that loss fails to capture—a possibility suggested by the theoretical work reviewed above—then loss-driven mixing may be blind to distributional deterioration.
20	
21	### 2.3 Collapse Detection Beyond Loss
22	
23	Several lines of work have developed signals that capture aspects of model behavior orthogonal to loss.
24	
25	**Entropy-based monitoring.** He et al. (2025) demonstrated a strong linear correlation between training data entropy and model generalization capacity, observing that entropy decline drives a generalization-to-memorization transition during iterative training. Truong & Truong (2025) formalized entropy collapse as a first-order phase transition, arguing that collapsed systems can maintain stable local performance (i.e., loss) while the effective dimensionality of their adaptive behavior has already contracted. This theoretical prediction—that loss stability can coexist with entropy collapse—directly motivates our empirical investigation, but neither work validated the claim in LLM iterative training.
26	
27	**Spectral methods.** Gu et al. (2026) proposed SIGMA, which tracks collapse via the eigenspectrum of embedding Gram matrices, providing scalable one-sided monitoring bounds that serve as early warnings for representation space contraction. Qiu et al. (2025) introduced Spectral Alignment (SA), showing that spectral distributional shifts in weight matrices precede loss explosions by a detectable margin, implying a temporal lag between spectral degradation and loss response. Both works establish spectral signals as informative collapse indicators but neither examines how their correlation with loss evolves across generations.
28	
29	**Diversity metrics.** Zhu et al. (2025) systematically compared diversity measures for synthetic data—including n-gram distinctness, self-BLEU, and the proposed DCScore—finding that classification-based diversity metrics correlate most strongly with human judgments. We adopt distinct-n (n=1,2,3) as a lightweight, interpretable generation-diversity signal alongside our representation-level metrics.
30	
31	**Gap in the literature.** Existing work has (a) theoretically predicted that collapse can occur without loss degradation (Truong & Truong, 2025; Schaeffer et al., 2025), (b) shown that entropy tracks generalization within a single generation (He et al., 2025), and (c) developed spectral monitoring tools that detect collapse independently of loss (Gu et al., 2026; Qiu et al., 2025). However, no prior work has quantified how the *correlation* between loss and these collapse signals evolves across iterative training generations. We address this gap by tracking Spearman rank correlation ρ(loss, signal) across multiple generations, testing whether signals that are initially coupled to loss become progressively decoupled as collapse advances.
32	
33	---
34	
35	## 3. Method
36	
37	### 3.1 Iterative Synthetic Training Setup
38	
39	**Model.** We use Pythia-410M-deduped (Biderman et al., 2023), a decoder-only transformer with 410M parameters pretrained on the Pile (deduplicated). This model is small enough to permit rapid multi-generation iteration on 2× RTX 6000 GPUs while being large enough to exhibit nontrivial language modeling behavior and collapse dynamics. The deduplication ensures our baseline is not already compromised by near-duplicate memorization artifacts.
40	
41	**Real data.** We sample a fixed subset from FineWeb (Penedo et al., 2024), a curated web corpus. Each training generation uses the same real-data pool to isolate the effect of synthetic data degradation across generations.
42	
43	**Synthetic data generation.** At each generation $g$, the model $M_g$ generates synthetic text via nucleus sampling (top-p = 0.9, temperature = 1.0) starting from the BOS token (unconditional generation) to match the token count of the real data portion. Each sample generates up to 256 new tokens. Each generation produces fresh synthetic data; prior generations' synthetic outputs are discarded (replacement paradigm).
44	
45	**Training configuration.** Each generation trains for approximately 200M tokens with a 50/50 real-synthetic mixing ratio (by token count). We use AdamW (β₁=0.9, β₂=0.999, weight decay 0.01) with a cosine learning rate schedule (peak lr = 1e-5, warmup over the first 2% of steps). Batch size is 32 sequences of 1024 tokens. Training resumes from the previous generation's final checkpoint, simulating the iterative retraining scenario studied in the collapse literature (Shumailov et al., 2024; Gerstgrasser et al., 2024).
46	
47	**Iterative protocol.** Starting from the pretrained Pythia-410M checkpoint (Gen 0 baseline), we execute three generations of iterative training:
48	- **Gen 0→1:** Train on 50% FineWeb + 50% synthetic from the pretrained Pythia-410M.
49	- **Gen 1→2:** Train on 50% FineWeb + 50% synthetic from the Gen 1 model.
50	- **Gen 2→3:** Train on 50% FineWeb + 50% synthetic from the Gen 2 model.
51	
52	Each generation produces a model checkpoint and a corresponding set of collapse signal measurements on a fixed probe set.
53	
54	**Reproducibility.** We run the full pipeline with two independent random seeds (42 and 137), controlling for initialization noise in both synthetic data generation and training stochasticity. Both seeds share the same real data subset and probe set.
55	
56	### 3.2 Collapse Signal Definitions
57	
58	We define four collapse signals spanning three levels of granularity: token-level, representation-level, and generation-level. All signals are computed on a fixed **probe set** of 5,000 sequences (256 tokens each) sampled from the FineWeb validation split, with no overlap with the training data.
59	
60	#### 3.2.1 Per-Example Output Entropy
61	
62	For each probe sequence $x = (x_1, \ldots, x_T)$, we compute the mean next-token prediction entropy:
63	
64	$$H(x) = -\frac{1}{T} \sum_{t=1}^{T} \sum_{v \in \mathcal{V}} p_\theta(v \mid x_{&lt;t}) \log p_\theta(v \mid x_{&lt;t})$$
65	
66	where $\mathcal{V}$ is the vocabulary and $p_\theta$ is the model's softmax distribution. Output entropy measures the uncertainty of the model's predictions; collapse concentrates probability mass on fewer tokens, reducing $H$. This yields one scalar per probe example, enabling per-example correlation with loss.
67	
68	#### 3.2.2 Per-Example Spectral Effective Rank
69	
70	For each probe sequence $x$, let $\mathbf{H}_x \in \mathbb{R}^{T \times d}$ be the matrix of last-layer hidden states across all $T$ positions. The spectral effective rank (Roy & Vetterli, 2007) is:
71	
72	$$\text{erank}(\mathbf{H}_x) = \exp\left( -\sum_{i=1}^{\min(T,d)} \hat{\sigma}_i \log \hat{\sigma}_i \right)$$
73	
74	where $\hat{\sigma}_i = \sigma_i / \sum_j \sigma_j$ are the normalized singular values of $\mathbf{H}_x$. Effective rank captures the dimensionality of the representation manifold: collapse reduces the number of directions the model actively uses, concentrating variance into fewer singular values. This yields one scalar per probe example.
75	
76	#### 3.2.3 Distinct-n
77	
78	For a set of generated continuations (all probe-set sequences, each continued for 128 new tokens from 64-token prefixes using the same sampling parameters as training synthetic data), we compute:
79	
80	$$\text{distinct-}n = \frac{|\text{unique } n\text{-grams}|}{|\text{total } n\text{-grams}|}$$
81	
82	for $n \in \{1, 2, 3\}$. Distinct-n directly measures lexical diversity of model outputs; collapse produces repetitive text with declining distinct-n. This is a corpus-level metric (one scalar per generation) and thus contributes to trend analysis rather than per-example correlation.
83	
84	#### 3.2.4 Corpus-Level Spectral Rank
85	
86	For each probe sequence, we mean-pool its last-layer hidden states into a single $d$-dimensional vector, yielding a matrix $\mathbf{H}_{\text{corpus}} \in \mathbb{R}^{5000 \times d}$. We then form the Gram matrix $\mathbf{G} = \mathbf{H}_{\text{corpus}}^\top \mathbf{H}_{\text{corpus}} \in \mathbb{R}^{d \times d}$ and compute its spectral effective rank using the same formula as §3.2.2. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).
87	
88	### 3.3 Statistical Methods
89	
90	Our central analysis quantifies how the relationship between loss and each collapse signal evolves across generations.
91	
92	**Primary metric: Spearman rank correlation.** For each generation $g$ and each per-example signal $s \in \{\text{entropy}, \text{spectral effective rank}\}$, we compute the Spearman rank correlation $\rho_g$ between per-example loss $\ell(x)$ and signal value $s(x)$ across the 5,000 probe examples. Spearman correlation is chosen over Pearson because it captures monotonic relationships without assuming linearity, and is robust to outliers in either loss or signal distributions.
93	
94	**Confidence intervals.** We construct 95% bootstrap confidence intervals for each $\rho_g$ by resampling the 5,000 probe examples with replacement (1,000 bootstrap iterations). This provides uncertainty estimates that account for probe-set heterogeneity without distributional assumptions.
95	
96	**Effect size.** To quantify the magnitude of decoupling, we report $\Delta\rho = \rho_0 - \rho_g$ (the drop in correlation from baseline) and normalize by bootstrap standard error: $\text{effect size} = \Delta\rho / \text{SE}_{\text{bootstrap}}$. This enables comparison across signals with different baseline correlation strengths.
97	
98	**Trend significance.** To assess whether the observed $\rho$ decline constitutes a statistically reliable trend rather than noise, we employ a permutation test: we randomly shuffle the generation labels (0, 1, 2, 3) 10,000 times and compute the Spearman correlation of $\rho$ values with generation index under each permutation. The p-value is the fraction of permuted slopes as steep or steeper than the observed slope.
99	
100	**Signal degradation.** For each collapse signal, we report the mean value per generation and test for monotonic decline. Degradation magnitude is quantified as the relative change from Gen 0 to the final generation: $\Delta_{\text{rel}} = (s_0 - s_G) / s_0$.
101	
102	### 3.4 Pre-registered Pass/Fail Criteria
103	
104	We pre-register three conditions that must all be satisfied for the hypothesis to pass:
105	
106	**C1 (Decoupling).** At least one collapse signal exhibits $|\rho_g|$ with loss dropping from $> 0.7$ at Gen 0–1 to $< 0.5$ at Gen 3. This threshold ensures that the signal begins meaningfully coupled to loss (sharing >49% of rank variance) and ends meaningfully decoupled (sharing <25%).
107	
108	**C2 (Signal degradation).** The same signal's mean value monotonically degrades across generations (each generation lower than the previous), with a cumulative decline of $\geq 15\%$ from Gen 0 to Gen 3. This condition ensures that decoupling is driven by genuine collapse (the signal detects worsening behavior) rather than mere noise inflation that could artificially reduce $\rho$.
109	
110	**C3 (Reproducibility).** C1 and C2 are both observed under both random seeds (42 and 137). Single-seed results cannot distinguish systematic phenomena from run-specific artifacts.
111	
112	**Contingency.** If the pattern emerges in one seed but not the other (weak pass), we run a third seed (7) as a tiebreaker. If all three conditions fail outright, we conclude that three generations are insufficient to observe decoupling at this model scale and either extend to five generations or reassess the hypothesis.
113	
114	---
115	
116	## References
117	
118	- Biderman, S., Schoelkopf, H., Anthony, Q., et al. (2023). Pythia: A suite for analyzing large language models across training and scaling. *ICML 2023*.
119	- Chen, M., et al. (2024). AIOLI: Online data mixing via gradient-based optimization. *arXiv*.
120	- Dohmatob, E., Feng, Y., Yang, P., Charton, F., & Kempe, J. (2025). Strong model collapse. *ICLR 2025 (Spotlight)*.
121	- Fan, Y., et al. (2024). Online data mixing for language model pre-training. *arXiv*.
122	- Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., et al. (2024). Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data. *COLM 2024*.
123	- Gu, Y., et al. (2026). SIGMA: Scalable spectral insights for LLM model collapse. *arXiv*.
124	- He, S., et al. (2025). A closer look at model collapse: From a generalization-to-memorization perspective. *NeurIPS 2025 (Spotlight)*.
125	- Penedo, G., et al. (2024). The FineWeb datasets: Decanting the web for the finest text data at scale. *arXiv*.
126	- Qiu, H., Wu, Y., Tan, Y., Wang, Y., & Yao, Q. (2025). Spectral alignment as predictor of loss explosion in neural network training. *arXiv*.
127	- Roy, O. & Vetterli, M. (2007). The effective rank: A measure of effective dimensionality. *European Signal Processing Conference*.
128	- Schaeffer, R., Kazdan, J., Arulandu, A. C., & Koyejo, S. (2025). Position: Model collapse does not mean what you think. *arXiv (NeurIPS 2025 Position Track)*.
129	- Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature*.
130	- Truong, X. K. & Truong, Q. H. (2025). Entropy collapse: A universal failure mode of intelligent systems. *arXiv*.
131	- Xie, S. M., et al. (2024). DoReMi: Optimizing data mixtures speeds up language model pretraining. *NeurIPS 2024*.
132	- Yi, B., Liu, Q., Cheng, Y., & Xu, H. (2025). Escaping model collapse via synthetic data verification. *ICML 2025*.
133	- Zhu, Y., Zhang, H., Wu, B., et al. (2025). Measuring diversity in synthetic datasets. *ICML 2025*.
134	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "ef94ade8-2ea1-4fdc-a841-da4f38f86706",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/prism_collapse_mixing/artifacts/paper_skeleton.md",
      "content": "# PRISM: Probing the Decoupling of Loss and Collapse Signals in Iterative Synthetic Training\n\n---\n\n## 2. Related Work\n\n### 2.1 Model Collapse in Iterative Training\n\nTraining generative models on their own outputs across successive generations leads to *model collapse*—a progressive loss of distributional fidelity that manifests as tail truncation and mode reduction. Shumailov et al. (2024) established this phenomenon across LLMs, VAEs, and GMMs, showing that distribution tails vanish first while bulk statistics remain superficially intact. Dohmatob et al. (2025) provided a theoretical grounding through the lens of the data processing inequality (DPI), proving that even trace amounts of synthetic contamination (as low as 1/1000) suffice to trigger collapse under iterative retraining, with degradation following an exponential decay in effective distributional support.\n\nA critical design variable is whether synthetic data *replaces* or *accumulates* alongside real data across generations. Gerstgrasser et al. (2024) demonstrated that accumulation strategies can avoid collapse entirely, while replacement strategies—where each generation discards prior data—reliably induce it. Our experimental design deliberately adopts the replacement paradigm (fixed 50/50 real-synthetic ratio, re-generated each generation) to create conditions under which collapse is expected, enabling controlled study of its detection.\n\nSchaeffer et al. (2025) drew attention to definitional ambiguity in the collapse literature, cataloguing eight distinct operationalizations. They argued that population-level risk (i.e., validation loss) can remain stable even as tail risk deteriorates—a conceptual precursor to the loss–signal decoupling we investigate. Yi et al. (2025) showed that external verifiers injecting fresh information can prevent collapse, suggesting that if collapse signals can serve as verification criteria, they may enable principled data filtering in iterative pipelines.\n\n### 2.2 Data Mixing Strategies\n\nOnline data mixing methods dynamically adjust domain proportions during training to optimize learning efficiency. DoReMi (Xie et al., 2024) uses a small proxy model to reweight domain mixtures via distributionally robust optimization. AIOLI (Chen et al., 2024) extends this with online gradient-based updates to mixing coefficients. ODM (Fan et al., 2024) optimizes domain mixtures by tracking per-domain loss trajectories.\n\nThese methods share a common dependency: they use *loss* (or loss-derived gradients) as the sole signal for mixture adjustment. This is well-motivated when training data is static and well-characterized, but becomes problematic in iterative synthetic training where the data distribution itself degrades across generations. If collapse manifests in ways that loss fails to capture—a possibility suggested by the theoretical work reviewed above—then loss-driven mixing may be blind to distributional deterioration.\n\n### 2.3 Collapse Detection Beyond Loss\n\nSeveral lines of work have developed signals that capture aspects of model behavior orthogonal to loss.\n\n**Entropy-based monitoring.** He et al. (2025) demonstrated a strong linear correlation between training data entropy and model generalization capacity, observing that entropy decline drives a generalization-to-memorization transition during iterative training. Truong & Truong (2025) formalized entropy collapse as a first-order phase transition, arguing that collapsed systems can maintain stable local performance (i.e., loss) while the effective dimensionality of their adaptive behavior has already contracted. This theoretical prediction—that loss stability can coexist with entropy collapse—directly motivates our empirical investigation, but neither work validated the claim in LLM iterative training.\n\n**Spectral methods.** Gu et al. (2026) proposed SIGMA, which tracks collapse via the eigenspectrum of embedding Gram matrices, providing scalable one-sided monitoring bounds that serve as early warnings for representation space contraction. Qiu et al. (2025) introduced Spectral Alignment (SA), showing that spectral distributional shifts in weight matrices precede loss explosions by a detectable margin, implying a temporal lag between spectral degradation and loss response. Both works establish spectral signals as informative collapse indicators but neither examines how their correlation with loss evolves across generations.\n\n**Diversity metrics.** Zhu et al. (2025) systematically compared diversity measures for synthetic data—including n-gram distinctness, self-BLEU, and the proposed DCScore—finding that classification-based diversity metrics correlate most strongly with human judgments. We adopt distinct-n (n=1,2,3) as a lightweight, interpretable generation-diversity signal alongside our representation-level metrics.\n\n**Gap in the literature.** Existing work has (a) theoretically predicted that collapse can occur without loss degradation (Truong & Truong, 2025; Schaeffer et al., 2025), (b) shown that entropy tracks generalization within a single generation (He et al., 2025), and (c) developed spectral monitoring tools that detect collapse independently of loss (Gu et al., 2026; Qiu et al., 2025). However, no prior work has quantified how the *correlation* between loss and these collapse signals evolves across iterative training generations. We address this gap by tracking Spearman rank correlation ρ(loss, signal) across multiple generations, testing whether signals that are initially coupled to loss become progressively decoupled as collapse advances.\n\n---\n\n## 3. Method\n\n### 3.1 Iterative Synthetic Training Setup\n\n**Model.** We use Pythia-410M-deduped (Biderman et al., 2023), a decoder-only transformer with 410M parameters pretrained on the Pile (deduplicated). This model is small enough to permit rapid multi-generation iteration on 2× RTX 6000 GPUs while being large enough to exhibit nontrivial language modeling behavior and collapse dynamics. The deduplication ensures our baseline is not already compromised by near-duplicate memorization artifacts.\n\n**Real data.** We sample a fixed subset from FineWeb (Penedo et al., 2024), a curated web corpus. Each training generation uses the same real-data pool to isolate the effect of synthetic data degradation across generations.\n\n**Synthetic data generation.** At each generation $g$, the model $M_g$ generates synthetic text via nucleus sampling (top-p = 0.9, temperature = 1.0) starting from the BOS token (unconditional generation) to match the token count of the real data portion. Each sample generates up to 256 new tokens. Each generation produces fresh synthetic data; prior generations' synthetic outputs are discarded (replacement paradigm).\n\n**Training configuration.** Each generation trains for approximately 200M tokens with a 50/50 real-synthetic mixing ratio (by token count). We use AdamW (β₁=0.9, β₂=0.999, weight decay 0.01) with a cosine learning rate schedule (peak lr = 1e-5, warmup over the first 2% of steps). Batch size is 32 sequences of 1024 tokens. Training resumes from the previous generation's final checkpoint, simulating the iterative retraining scenario studied in the collapse literature (Shumailov et al., 2024; Gerstgrasser et al., 2024).\n\n**Iterative protocol.** Starting from the pretrained Pythia-410M checkpoint (Gen 0 baseline), we execute three generations of iterative training:\n- **Gen 0→1:** Train on 50% FineWeb + 50% synthetic from the pretrained Pythia-410M.\n- **Gen 1→2:** Train on 50% FineWeb + 50% synthetic from the Gen 1 model.\n- **Gen 2→3:** Train on 50% FineWeb + 50% synthetic from the Gen 2 model.\n\nEach generation produces a model checkpoint and a corresponding set of collapse signal measurements on a fixed probe set.\n\n**Reproducibility.** We run the full pipeline with two independent random seeds (42 and 137), controlling for initialization noise in both synthetic data generation and training stochasticity. Both seeds share the same real data subset and probe set.\n\n### 3.2 Collapse Signal Definitions\n\nWe define four collapse signals spanning three levels of granularity: token-level, representation-level, and generation-level. All signals are computed on a fixed **probe set** of 5,000 sequences (256 tokens each) sampled from the FineWeb validation split, with no overlap with the training data.\n\n#### 3.2.1 Per-Example Output Entropy\n\nFor each probe sequence $x = (x_1, \\ldots, x_T)$, we compute the mean next-token prediction entropy:\n\n$$H(x) = -\\frac{1}{T} \\sum_{t=1}^{T} \\sum_{v \\in \\mathcal{V}} p_\\theta(v \\mid x_{&lt;t}) \\log p_\\theta(v \\mid x_{&lt;t})$$\n\nwhere $\\mathcal{V}$ is the vocabulary and $p_\\theta$ is the model's softmax distribution. Output entropy measures the uncertainty of the model's predictions; collapse concentrates probability mass on fewer tokens, reducing $H$. This yields one scalar per probe example, enabling per-example correlation with loss.\n\n#### 3.2.2 Per-Example Spectral Effective Rank\n\nFor each probe sequence $x$, let $\\mathbf{H}_x \\in \\mathbb{R}^{T \\times d}$ be the matrix of last-layer hidden states across all $T$ positions. The spectral effective rank (Roy & Vetterli, 2007) is:\n\n$$\\text{erank}(\\mathbf{H}_x) = \\exp\\left( -\\sum_{i=1}^{\\min(T,d)} \\hat{\\sigma}_i \\log \\hat{\\sigma}_i \\right)$$\n\nwhere $\\hat{\\sigma}_i = \\sigma_i / \\sum_j \\sigma_j$ are the normalized singular values of $\\mathbf{H}_x$. Effective rank captures the dimensionality of the representation manifold: collapse reduces the number of directions the model actively uses, concentrating variance into fewer singular values. This yields one scalar per probe example.\n\n#### 3.2.3 Distinct-n\n\nFor a set of generated continuations (all probe-set sequences, each continued for 128 new tokens from 64-token prefixes using the same sampling parameters as training synthetic data), we compute:\n\n$$\\text{distinct-}n = \\frac{|\\text{unique } n\\text{-grams}|}{|\\text{total } n\\text{-grams}|}$$\n\nfor $n \\in \\{1, 2, 3\\}$. Distinct-n directly measures lexical diversity of model outputs; collapse produces repetitive text with declining distinct-n. This is a corpus-level metric (one scalar per generation) and thus contributes to trend analysis rather than per-example correlation.\n\n#### 3.2.4 Corpus-Level Spectral Rank\n\nFor each probe sequence, we mean-pool its last-layer hidden states into a single $d$-dimensional vector, yielding a matrix $\\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{5000 \\times d}$. We then form the Gram matrix $\\mathbf{G} = \\mathbf{H}_{\\text{corpus}}^\\top \\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{d \\times d}$ and compute its spectral effective rank using the same formula as §3.2.2. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).\n\n### 3.3 Statistical Methods\n\nOur central analysis quantifies how the relationship between loss and each collapse signal evolves across generations.\n\n**Primary metric: Spearman rank correlation.** For each generation $g$ and each per-example signal $s \\in \\{\\text{entropy}, \\text{spectral effective rank}\\}$, we compute the Spearman rank correlation $\\rho_g$ between per-example loss $\\ell(x)$ and signal value $s(x)$ across the 5,000 probe examples. Spearman correlation is chosen over Pearson because it captures monotonic relationships without assuming linearity, and is robust to outliers in either loss or signal distributions.\n\n**Confidence intervals.** We construct 95% bootstrap confidence intervals for each $\\rho_g$ by resampling the 5,000 probe examples with replacement (1,000 bootstrap iterations). This provides uncertainty estimates that account for probe-set heterogeneity without distributional assumptions.\n\n**Effect size.** To quantify the magnitude of decoupling, we report $\\Delta\\rho = \\rho_0 - \\rho_g$ (the drop in correlation from baseline) and normalize by bootstrap standard error: $\\text{effect size} = \\Delta\\rho / \\text{SE}_{\\text{bootstrap}}$. This enables comparison across signals with different baseline correlation strengths.\n\n**Trend significance.** To assess whether the observed $\\rho$ decline constitutes a statistically reliable trend rather than noise, we employ a permutation test: we randomly shuffle the generation labels (0, 1, 2, 3) 10,000 times and compute the Spearman correlation of $\\rho$ values with generation index under each permutation. The p-value is the fraction of permuted slopes as steep or steeper than the observed slope.\n\n**Signal degradation.** For each collapse signal, we report the mean value per generation and test for monotonic decline. Degradation magnitude is quantified as the relative change from Gen 0 to the final generation: $\\Delta_{\\text{rel}} = (s_0 - s_G) / s_0$.\n\n### 3.4 Pre-registered Pass/Fail Criteria\n\nWe pre-register three conditions that must all be satisfied for the hypothesis to pass:\n\n**C1 (Decoupling).** At least one collapse signal exhibits $|\\rho_g|$ with loss dropping from $> 0.7$ at Gen 0–1 to $< 0.5$ at Gen 3. This threshold ensures that the signal begins meaningfully coupled to loss (sharing >49% of rank variance) and ends meaningfully decoupled (sharing <25%).\n\n**C2 (Signal degradation).** The same signal's mean value monotonically degrades across generations (each generation lower than the previous), with a cumulative decline of $\\geq 15\\%$ from Gen 0 to Gen 3. This condition ensures that decoupling is driven by genuine collapse (the signal detects worsening behavior) rather than mere noise inflation that could artificially reduce $\\rho$.\n\n**C3 (Reproducibility).** C1 and C2 are both observed under both random seeds (42 and 137). Single-seed results cannot distinguish systematic phenomena from run-specific artifacts.\n\n**Contingency.** If the pattern emerges in one seed but not the other (weak pass), we run a third seed (7) as a tiebreaker. If all three conditions fail outright, we conclude that three generations are insufficient to observe decoupling at this model scale and either extend to five generations or reassess the hypothesis.\n\n---\n\n## References\n\n- Biderman, S., Schoelkopf, H., Anthony, Q., et al. (2023). Pythia: A suite for analyzing large language models across training and scaling. *ICML 2023*.\n- Chen, M., et al. (2024). AIOLI: Online data mixing via gradient-based optimization. *arXiv*.\n- Dohmatob, E., Feng, Y., Yang, P., Charton, F., & Kempe, J. (2025). Strong model collapse. *ICLR 2025 (Spotlight)*.\n- Fan, Y., et al. (2024). Online data mixing for language model pre-training. *arXiv*.\n- Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., et al. (2024). Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data. *COLM 2024*.\n- Gu, Y., et al. (2026). SIGMA: Scalable spectral insights for LLM model collapse. *arXiv*.\n- He, S., et al. (2025). A closer look at model collapse: From a generalization-to-memorization perspective. *NeurIPS 2025 (Spotlight)*.\n- Penedo, G., et al. (2024). The FineWeb datasets: Decanting the web for the finest text data at scale. *arXiv*.\n- Qiu, H., Wu, Y., Tan, Y., Wang, Y., & Yao, Q. (2025). Spectral alignment as predictor of loss explosion in neural network training. *arXiv*.\n- Roy, O. & Vetterli, M. (2007). The effective rank: A measure of effective dimensionality. *European Signal Processing Conference*.\n- Schaeffer, R., Kazdan, J., Arulandu, A. C., & Koyejo, S. (2025). Position: Model collapse does not mean what you think. *arXiv (NeurIPS 2025 Position Track)*.\n- Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature*.\n- Truong, X. K. & Truong, Q. H. (2025). Entropy collapse: A universal failure mode of intelligent systems. *arXiv*.\n- Xie, S. M., et al. (2024). DoReMi: Optimizing data mixtures speeds up language model pretraining. *NeurIPS 2024*.\n- Yi, B., Liu, Q., Cheng, Y., & Xu, H. (2025). Escaping model collapse via synthetic data verification. *ICML 2025*.\n- Zhu, Y., Zhang, H., Wu, B., et al. (2025). Measuring diversity in synthetic datasets. *ICML 2025*.\n",
      "numLines": 134,
      "startLine": 1,
      "totalLines": 134
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated. I need to see the middle portion of compute_signals.py, specifically the corpus spectral rank computation (around lines 100-140). Let me also check what was cut off.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "8d2318da-1207-45c9-a793-46362398f610",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xdh8xnr4PzXigau6g3wNYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8549,
      "cache_read_input_tokens": 24320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8549
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

_source line 13_

Output was truncated. Let me read the missing portion of the code (around lines 100-140 where corpus spectral rank is computed).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "00924f2b-b8c1-4a4a-9375-f3515509ad21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xdh8xnr4PzXigau6g3wNYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8549,
      "cache_read_input_tokens": 24320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8549
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011U4BBVWYcUaRcba8gD3XL4`</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "head -160 /root/prism_collapse_mixing/compute_signals.py | tail -70",
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
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "9bca5ebd-7159-45da-ae61-d8b5d0457bc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xdh8xnr4PzXigau6g3wNYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8549,
      "cache_read_input_tokens": 24320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8549
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

_source line 15 · 2026-05-16T02:01:07.518Z_

<details><summary>↩ Tool result · `toolu_011U4BBVWYcUaRcba8gD3XL4`</summary>

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
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "a1cc56d6-75df-4428-8be5-8fe8c24a9175",
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01K7y7skgTPuo6zuFRAa1kx5`</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "sed -n '95,145p' /root/prism_collapse_mixing/compute_signals.py",
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
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "04bb946c-f3bc-4eac-9364-e0ffea3a0ae2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGeGrtFSfD6a2fhXU6Bxa5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 32869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
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

_source line 17 · 2026-05-16T02:01:12.417Z_

<details><summary>↩ Tool result · `toolu_01K7y7skgTPuo6zuFRAa1kx5`</summary>

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
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "e86d66aa-f4a4-4193-a505-7655405bc93a",
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

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EUpdP5nGonRbjWjuaQVTTU`</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "tail -n +95 /root/prism_collapse_mixing/compute_signals.py",
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
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "7407edd6-1614-41c5-a920-c9d6e73fd1c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dr4vrsitZoynbLhb7uG7j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 33179,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 220
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

_source line 19 · 2026-05-16T02:01:16.260Z_

<details><summary>↩ Tool result · `toolu_01EUpdP5nGonRbjWjuaQVTTU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"        B, L1, V = shift_logits.shape\\n        token_loss = loss_fn(\\n            shift_logits.view(-1, V).float(), shift_labels.view(-1)\\n        ).view(B, L1)\\n        token_loss = token_loss * shift_mask\\n        seq_loss = token_loss.sum(dim=1) / shift_mask.sum(dim=1).clamp(min=1)\\n        all_loss.extend(seq_loss.cpu().tolist())\\n\\n        # --- Per-example entropy ---\\n        log_probs = torch.log_softmax(logits.float(), dim=-1)\\n        probs = torch.exp(log_probs)\\n        token_ent = -(probs * log_probs).sum(dim=-1)  # [B, L]\\n        token_ent = token_ent * amask.float()\\n        seq_ent = token_ent.sum(dim=1) / amask.sum(dim=1).float().clamp(min=1)\\n        all_entropy.extend(seq_ent.cpu().tolist())\\n\\n        # --- Per-example spectral rank + mean hidden for sigma ---\\n        h_cpu = hidden.cpu().float()\\n        amask_cpu = amask.cpu().bool()\\n        for b in range(h_cpu.shape[0]):\\n            h = h_cpu[b][amask_cpu[b]]  # [seq_actual, D]\\n            all_mean_hidden.append(h.mean(dim=0))\\n            if h.shape[0] < 2:\\n                all_spectral_rank.append(1.0)\\n                continue\\n            _, S, _ = torch.linalg.svd(h, full_matrices=False)\\n            all_spectral_rank.append(effective_rank(S))\\n\\n        del out, logits, hidden, h_cpu\\n        torch.cuda.empty_cache()\\n\\n    _hook.remove()\\n\\n    # --- Corpus-level SIGMA spectral rank ---\\n    mean_mat = torch.stack(all_mean_hidden)  # [N, D]\\n    gram = mean_mat.T @ mean_mat             # [D, D]\\n    _, S_sigma, _ = torch.linalg.svd(gram, full_matrices=False)\\n    sigma_rank = effective_rank(S_sigma)\\n\\n    return all_loss, all_entropy, all_spectral_rank, sigma_rank\\n\\n\\ndef compute_distinct_n(model, tokenizer, probe_path, device,\\n                       prefix_len=64, max_new=128, batch_size=16,\\n                       top_p=0.9, temperature=1.0):\\n    \\\"\\\"\\\"Distinct-1/2/3 from model generations using probe prefixes.\\\"\\\"\\\"\\n    ds = TokenizedDataset(probe_path, tokenizer, prefix_len)\\n    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\\n\\n    all_gen = []\\n    for i in tqdm(range(0, len(ds), batch_size), desc=\\\"distinct\\\"):\\n        seqs = [ds[j] for j in range(i, min(i + batch_size, len(ds)))]\\n        ml = max(len(s) for s in seqs)\\n        ids = torch.full((len(seqs), ml), pad_id, dtype=torch.long)\\n        amask = torch.zeros(len(seqs), ml, dtype=torch.long)\\n        for b, s in enumerate(seqs):\\n            ids[b, ml - len(s):] = s   # left-pad for generation\\n            amask[b, ml - len(s):] = 1\\n        ids, amask = ids.to(device), amask.to(device)\\n        with torch.no_grad():\\n            out = model.generate(\\n                input_ids=ids, attention_mask=amask,\\n                max_new_tokens=max_new, do_sample=True,\\n                top_p=top_p, temperature=temperature,\\n                pad_token_id=pad_id,\\n            )\\n        for b in range(out.shape[0]):\\n            gen = out[b, ids.shape[1]:].cpu().tolist()\\n            gen = [t for t in gen if t != pad_id]\\n            all_gen.extend(gen)\\n\\n    result = {}\\n    for n in [1, 2, 3]:\\n        ngrams = [tuple(all_gen[i:i + n]) for i in range(len(all_gen) - n + 1)]\\n        result[f\\\"distinct_{n}\\\"] = len(set(ngrams)) / len(ngrams) if ngrams else 0.0\\n    return result\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute per-example and corpus-level collapse signals\\\")\\n    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Model checkpoint or HF hub name\\\")\\n    parser.add_argument(\\\"--probe_set_path\\\", required=True, help=\\\"Probe set jsonl (5000 samples, >=256 tokens)\\\")\\n    parser.add_argument(\\\"--output_path\\\", required=True, help=\\\"Output JSON path for signals\\\")\\n    parser.add_argument(\\\"--gen\\\", type=int, required=True, help=\\\"Generation number\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--device\\\", type=str, default=\\\"cuda:0\\\", help=\\\"GPU device (e.g. cuda:0)\\\")\\n    parser.add_argument(\\\"--gen_prefix_len\\\", type=int, default=64, help=\\\"Prefix length for distinct-n generation\\\")\\n    parser.add_argument(\\\"--gen_max_new_tokens\\\", type=int, default=128, help=\\\"Max new tokens for distinct-n\\\")\\n    parser.add_argument(\\\"--batch_size\\\", type=int, default=16, help=\\\"Inference batch size\\\")\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(args.device)\\n\\n    print(f\\\"Loading {args.model_path}...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path)\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path, torch_dtype=torch.bfloat16\\n    ).to(device)\\n    model.eval()\\n\\n    # 1/3 Per-example signals + corpus-level sigma\\n    print(\\\"1/3 Per-example signals (loss, entropy, spectral_rank) + sigma...\\\")\\n    loss_vec, ent_vec, srank_vec, sigma_rank = compute_per_example_signals(\\n        model, tokenizer, args.probe_set_path, device, batch_size=args.batch_size\\n    )\\n\\n    # 2/3 Corpus-level distinct-n\\n    print(\\\"2/3 Distinct-n...\\\")\\n    dn = compute_distinct_n(\\n        model, tokenizer, args.probe_set_path, device,\\n        prefix_len=args.gen_prefix_len,\\n        max_new=args.gen_max_new_tokens,\\n        batch_size=args.batch_size,\\n    )\\n\\n    # 3/3 Spearman correlations\\n    print(\\\"3/3 Spearman correlations...\\\")\\n    rho_le, pval_le = spearmanr(loss_vec, ent_vec)\\n    rho_ls, pval_ls = spearmanr(loss_vec, srank_vec)\\n\\n    loss_arr = np.array(loss_vec)\\n    ent_arr = np.array(ent_vec)\\n    srank_arr = np.array(srank_vec)\\n\\n    result = {\\n        \\\"gen\\\": args.gen,\\n        \\\"seed\\\": args.seed,\\n        \\\"per_example\\\": {\\n            \\\"loss\\\": [round(x, 4) for x in loss_vec],\\n            \\\"entropy\\\": [round(x, 4) for x in ent_vec],\\n            \\\"spectral_rank\\\": [round(x, 2) for x in srank_vec],\\n        },\\n        \\\"aggregated\\\": {\\n            \\\"loss_mean\\\": round(float(loss_arr.mean()), 4),\\n            \\\"loss_std\\\": round(float(loss_arr.std()), 4),\\n            \\\"entropy_mean\\\": round(float(ent_arr.mean()), 4),\\n            \\\"entropy_std\\\": round(float(ent_arr.std()), 4),\\n            \\\"spectral_rank_mean\\\": round(float(srank_arr.mean()), 2),\\n            \\\"spectral_rank_std\\\": round(float(srank_arr.std()), 2),\\n        },\\n        \\\"corpus_level\\\": {\\n            \\\"sigma_spectral_rank\\\": round(sigma_rank, 2),\\n            \\\"distinct_1\\\": round(dn[\\\"distinct_1\\\"], 4),\\n            \\\"distinct_2\\\": round(dn[\\\"distinct_2\\\"], 4),\\n            \\\"distinct_3\\\": round(dn[\\\"distinct_3\\\"], 4),\\n        },\\n        \\\"correlations\\\": {\\n            \\\"rho_loss_entropy\\\": round(float(rho_le), 4),\\n            \\\"pval_loss_entropy\\\": round(float(pval_le), 6),\\n            \\\"rho_loss_spectral_rank\\\": round(float(rho_ls), 4),\\n            \\\"pval_loss_spectral_rank\\\": round(float(pval_ls), 6),\\n        },\\n        \\\"num_probe_samples\\\": len(loss_vec),\\n    }\\n\\n    os.makedirs(os.path.dirname(os.path.abspath(args.output_path)), exist_ok=True)\\n    with open(args.output_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    print(f\\\"\\\\nSignals saved to {args.output_path}\\\")\\n    print(f\\\"  loss: mean={loss_arr.mean():.4f} std={loss_arr.std():.4f}\\\")\\n    print(f\\\"  entropy: mean={ent_arr.mean():.4f} std={ent_arr.std():.4f}\\\")\\n    print(f\\\"  spectral_rank: mean={srank_arr.mean():.2f} std={srank_arr.std():.2f}\\\")\\n    print(f\\\"  sigma_rank: {sigma_rank:.2f}\\\")\\n    print(f\\\"  rho(loss,entropy)={rho_le:.4f} p={pval_le:.6f}\\\")\\n    print(f\\\"  rho(loss,spectral_rank)={rho_ls:.4f} p={pval_ls:.6f}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "13891835-ad69-4129-ac91-2c6ded082002",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"        B, L1, V = shift_logits.shape\\\\n        token_loss = loss_fn(\\\\n            shift_logits.view(-1, V).float(), shift_labels.view(-1)\\\\n        ).view(B, L1)\\\\n        token_loss = token_loss * shift_mask\\\\n        seq_loss = token_loss.sum(dim=1) / shift_mask.sum(dim=1).clamp(min=1)\\\\n        all_loss.extend(seq_loss.cpu().tolist())\\\\n\\\\n        # --- Per-example entropy ---\\\\n        log_probs = torch.log_softmax(logits.float(), dim=-1)\\\\n        probs = torch.exp(log_probs)\\\\n        token_ent = -(probs * log_probs).sum(dim=-1)  # [B, L]\\\\n        token_ent = token_ent * amask.float()\\\\n        seq_ent = token_ent.sum(dim=1) / amask.sum(dim=1).float().clamp(min=1)\\\\n        all_entropy.extend(seq_ent.cpu().tolist())\\\\n\\\\n        # --- Per-example spectral rank + mean hidden for sigma ---\\\\n        h_cpu = hidden.cpu().float()\\\\n        amask_cpu = amask.cpu().bool()\\\\n        for b in range(h_cpu.shape[0]):\\\\n            h = h_cpu[b][amask_cpu[b]]  # [seq_actual, D]\\\\n            all_mean_hidden.append(h.mean(dim=0))\\\\n            if h.shape[0] < 2:\\\\n                all_spectral_rank.append(1.0)\\\\n                continue\\\\n            _, S, _ = torch.linalg.svd(h, full_matrices=False)\\\\n            all_spectral_rank.append(effective_rank(S))\\\\n\\\\n        del out, logits, hidden, h_cpu\\\\n        torch.cuda.empty_cache()\\\\n\\\\n    _hook.remove()\\\\n\\\\n    # --- Corpus-level SIGMA spectral rank ---\\\\n    mean_mat = torch.stack(all_mean_hidden)  # [N, D]\\\\n    gram = mean_mat.T @ mean_mat             # [D, D]\\\\n    _, S_sigma, _ = torch.linalg.svd(gram, full_matrices=False)\\\\n    sigma_rank = effective_rank(S_sigma)\\\\n\\\\n    return all_loss, all_entropy, all_spectral_rank, sigma_rank\\\\n\\\\n\\\\ndef compute_distinct_n(model, tokenizer, probe_path, device,\\\\n                       prefix_len=64, max_new=128, batch_size=16,\\\\n                       top_p=0.9, temperature=1.0):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Distinct-1/2/3 from model generations using probe prefixes.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ds = TokenizedDataset(probe_path, tokenizer, prefix_len)\\\\n    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\\\\n\\\\n    all_gen = []\\\\n    for i in tqdm(range(0, len(ds), batch_size), desc=\\\\\\\"distinct\\\\\\\"):\\\\n        seqs = [ds[j] for j in range(i, min(i + batch_size, len(ds)))]\\\\n        ml = max(len(s) for s in seqs)\\\\n        ids = torch.full((len(seqs), ml), pad_id, dtype=torch.long)\\\\n        amask = torch.zeros(len(seqs), ml, dtype=torch.long)\\\\n        for b, s in enumerate(seqs):\\\\n            ids[b, ml - len(s):] = s   # left-pad for generation\\\\n            amask[b, ml - len(s):] = 1\\\\n        ids, amask = ids.to(device), amask.to(device)\\\\n        with torch.no_grad():\\\\n            out = model.generate(\\\\n                input_ids=ids, attention_mask=amask,\\\\n                max_new_tokens=max_new, do_sample=True,\\\\n                top_p=top_p, temperature=temperature,\\\\n                pad_token_id=pad_id,\\\\n            )\\\\n        for b in range(out.shape[0]):\\\\n            gen = out[b, ids.shape[1]:].cpu().tolist()\\\\n            gen = [t for t in gen if t != pad_id]\\\\n            all_gen.extend(gen)\\\\n\\\\n    result = {}\\\\n    for n in [1, 2, 3]:\\\\n        ngrams = [tuple(all_gen[i:i + n]) for i in range(len(all_gen) - n + 1)]\\\\n        result[f\\\\\\\"distinct_{n}\\\\\\\"] = len(set(ngrams)) / len(ngrams) if ngrams else 0.0\\\\n    return result\\\\n\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"Compute per-example and corpus-level collapse signals\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--model_path\\\\\\\", required=True, help=\\\\\\\"Model checkpoint or HF hub name\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--probe_set_path\\\\\\\", required=True, help=\\\\\\\"Probe set jsonl (5000 samples, >=256 tokens)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output_path\\\\\\\", required=True, help=\\\\\\\"Output JSON path for signals\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--gen\\\\\\\", type=int, required=True, help=\\\\\\\"Generation number\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42, help=\\\\\\\"Random seed\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--device\\\\\\\", type=str, default=\\\\\\\"cuda:0\\\\\\\", help=\\\\\\\"GPU device (e.g. cuda:0)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--gen_prefix_len\\\\\\\", type=int, default=64, help=\\\\\\\"Prefix length for distinct-n generation\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--gen_max_new_tokens\\\\\\\", type=int, default=128, help=\\\\\\\"Max new tokens for distinct-n\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--batch_size\\\\\\\", type=int, default=16, help=\\\\\\\"Inference batch size\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    set_seed(args.seed)\\\\n    device = torch.device(args.device)\\\\n\\\\n    print(f\\\\\\\"Loading {args.model_path}...\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path)\\\\n    if tokenizer.pad_token is None:\\\\n        tokenizer.pad_token = tokenizer.eos_token\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        args.model_path, torch_dtype=torch.bfloat16\\\\n    ).to(device)\\\\n    model.eval()\\\\n\\\\n    # 1/3 Per-example signals + corpus-level sigma\\\\n    print(\\\\\\\"1/3 Per-example signals (loss, entropy, spectral_rank) + sigma...\\\\\\\")\\\\n    loss_vec, ent_vec, srank_vec, sigma_rank = compute_per_example_signals(\\\\n        model, tokenizer, args.probe_set_path, device, batch_size=args.batch_size\\\\n    )\\\\n\\\\n    # 2/3 Corpus-level distinct-n\\\\n    print(\\\\\\\"2/3 Distinct-n...\\\\\\\")\\\\n    dn = compute_distinct_n(\\\\n        model, tokenizer, args.probe_set_path, device,\\\\n        prefix_len=args.gen_prefix_len,\\\\n        max_new=args.gen_max_new_tokens,\\\\n        batch_size=args.batch_size,\\\\n    )\\\\n\\\\n    # 3/3 Spearman correlations\\\\n    print(\\\\\\\"3/3 Spearman correlations...\\\\\\\")\\\\n    rho_le, pval_le = spearmanr(loss_vec, ent_vec)\\\\n    rho_ls, pval_ls = spearmanr(loss_vec, srank_vec)\\\\n\\\\n    loss_arr = np.array(loss_vec)\\\\n    ent_arr = np.array(ent_vec)\\\\n    srank_arr = np.array(srank_vec)\\\\n\\\\n    result = {\\\\n        \\\\\\\"gen\\\\\\\": args.gen,\\\\n        \\\\\\\"seed\\\\\\\": args.seed,\\\\n        \\\\\\\"per_example\\\\\\\": {\\\\n            \\\\\\\"loss\\\\\\\": [round(x, 4) for x in loss_vec],\\\\n            \\\\\\\"entropy\\\\\\\": [round(x, 4) for x in ent_vec],\\\\n            \\\\\\\"spectral_rank\\\\\\\": [round(x, 2) for x in srank_vec],\\\\n        },\\\\n        \\\\\\\"aggregated\\\\\\\": {\\\\n            \\\\\\\"loss_mean\\\\\\\": round(float(loss_arr.mean()), 4),\\\\n            \\\\\\\"loss_std\\\\\\\": round(float(loss_arr.std()), 4),\\\\n            \\\\\\\"entropy_mean\\\\\\\": round(float(ent_arr.mean()), 4),\\\\n            \\\\\\\"entropy_std\\\\\\\": round(float(ent_arr.std()), 4),\\\\n            \\\\\\\"spectral_rank_mean\\\\\\\": round(float(srank_arr.mean()), 2),\\\\n            \\\\\\\"spectral_rank_std\\\\\\\": round(float(srank_arr.std()), 2),\\\\n        },\\\\n        \\\\\\\"corpus_level\\\\\\\": {\\\\n            \\\\\\\"sigma_spectral_rank\\\\\\\": round(sigma_rank, 2),\\\\n            \\\\\\\"distinct_1\\\\\\\": round(dn[\\\\\\\"distinct_1\\\\\\\"], 4),\\\\n            \\\\\\\"distinct_2\\\\\\\": round(dn[\\\\\\\"distinct_2\\\\\\\"], 4),\\\\n            \\\\\\\"distinct_3\\\\\\\": round(dn[\\\\\\\"distinct_3\\\\\\\"], 4),\\\\n        },\\\\n        \\\\\\\"correlations\\\\\\\": {\\\\n            \\\\\\\"rho_loss_entropy\\\\\\\": round(float(rho_le), 4),\\\\n            \\\\\\\"pval_loss_entropy\\\\\\\": round(float(pval_le), 6),\\\\n            \\\\\\\"rho_loss_spectral_rank\\\\\\\": round(float(rho_ls), 4),\\\\n            \\\\\\\"pval_loss_spectral_rank\\\\\\\": round(float(pval_ls), 6),\\\\n        },\\\\n        \\\\\\\"num_probe_samples\\\\\\\": len(loss_vec),\\\\n    }\\\\n\\\\n    os.makedirs(os.path.dirname(os.path.abspath(args.output_path)), exist_ok=True)\\\\n    with open(args.output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(result, f, indent=2)\\\\n    print(f\\\\\\\"\\\\\\\\nSignals saved to {args.output_path}\\\\\\\")\\\\n    print(f\\\\\\\"  loss: mean={loss_arr.mean():.4f} std={loss_arr.std():.4f}\\\\\\\")\\\\n    print(f\\\\\\\"  entropy: mean={ent_arr.mean():.4f} std={ent_arr.std():.4f}\\\\\\\")\\\\n    print(f\\\\\\\"  spectral_rank: mean={srank_arr.mean():.2f} std={srank_arr.std():.2f}\\\\\\\")\\\\n    print(f\\\\\\\"  sigma_rank: {sigma_rank:.2f}\\\\\\\")\\\\n    print(f\\\\\\\"  rho(loss,entropy)={rho_le:.4f} p={pval_le:.6f}\\\\\\\")\\\\n    print(f\\\\\\\"  rho(loss,spectral_rank)={rho_ls:.4f} p={pval_ls:.6f}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"        B, L1, V = shift_logits.shape\\n        token_loss = loss_fn(\\n            shift_logits.view(-1, V).float(), shift_labels.view(-1)\\n        ).view(B, L1)\\n        token_loss = token_loss * shift_mask\\n        seq_loss = token_loss.sum(dim=1) / shift_mask.sum(dim=1).clamp(min=1)\\n        all_loss.extend(seq_loss.cpu().tolist())\\n\\n        # --- Per-example entropy ---\\n        log_probs = torch.log_softmax(logits.float(), dim=-1)\\n        probs = torch.exp(log_probs)\\n        token_ent = -(probs * log_probs).sum(dim=-1)  # [B, L]\\n        token_ent = token_ent * amask.float()\\n        seq_ent = token_ent.sum(dim=1) / amask.sum(dim=1).float().clamp(min=1)\\n        all_entropy.extend(seq_ent.cpu().tolist())\\n\\n        # --- Per-example spectral rank + mean hidden for sigma ---\\n        h_cpu = hidden.cpu().float()\\n        amask_cpu = amask.cpu().bool()\\n        for b in range(h_cpu.shape[0]):\\n            h = h_cpu[b][amask_cpu[b]]  # [seq_actual, D]\\n            all_mean_hidden.append(h.mean(dim=0))\\n            if h.shape[0] < 2:\\n                all_spectral_rank.append(1.0)\\n                continue\\n            _, S, _ = torch.linalg.svd(h, full_matrices=False)\\n            all_spectral_rank.append(effective_rank(S))\\n\\n        del out, logits, hidden, h_cpu\\n        torch.cuda.empty_cache()\\n\\n    _hook.remove()\\n\\n    # --- Corpus-level SIGMA spectral rank ---\\n    mean_mat = torch.stack(all_mean_hidden)  # [N, D]\\n    gram = mean_mat.T @ mean_mat             # [D, D]\\n    _, S_sigma, _ = torch.linalg.svd(gram, full_matrices=False)\\n    sigma_rank = effective_rank(S_sigma)\\n\\n    return all_loss, all_entropy, all_spectral_rank, sigma_rank\\n\\n\\ndef compute_distinct_n(model, tokenizer, probe_path, device,\\n                       prefix_len=64, max_new=128, batch_size=16,\\n                       top_p=0.9, temperature=1.0):\\n    \\\"\\\"\\\"Distinct-1/2/3 from model generations using probe prefixes.\\\"\\\"\\\"\\n    ds = TokenizedDataset(probe_path, tokenizer, prefix_len)\\n    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\\n\\n    all_gen = []\\n    for i in tqdm(range(0, len(ds), batch_size), desc=\\\"distinct\\\"):\\n        seqs = [ds[j] for j in range(i, min(i + batch_size, len(ds)))]\\n        ml = max(len(s) for s in seqs)\\n        ids = torch.full((len(seqs), ml), pad_id, dtype=torch.long)\\n        amask = torch.zeros(len(seqs), ml, dtype=torch.long)\\n        for b, s in enumerate(seqs):\\n            ids[b, ml - len(s):] = s   # left-pad for generation\\n            amask[b, ml - len(s):] = 1\\n        ids, amask = ids.to(device), amask.to(device)\\n        with torch.no_grad():\\n            out = model.generate(\\n                input_ids=ids, attention_mask=amask,\\n                max_new_tokens=max_new, do_sample=True,\\n                top_p=top_p, temperature=temperature,\\n                pad_token_id=pad_id,\\n            )\\n        for b in range(out.shape[0]):\\n            gen = out[b, ids.shape[1]:].cpu().tolist()\\n            gen = [t for t in gen if t != pad_id]\\n            all_gen.extend(gen)\\n\\n    result = {}\\n    for n in [1, 2, 3]:\\n        ngrams = [tuple(all_gen[i:i + n]) for i in range(len(all_gen) - n + 1)]\\n        result[f\\\"distinct_{n}\\\"] = len(set(ngrams)) / len(ngrams) if ngrams else 0.0\\n    return result\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(description=\\\"Compute per-example and corpus-level collapse signals\\\")\\n    parser.add_argument(\\\"--model_path\\\", required=True, help=\\\"Model checkpoint or HF hub name\\\")\\n    parser.add_argument(\\\"--probe_set_path\\\", required=True, help=\\\"Probe set jsonl (5000 samples, >=256 tokens)\\\")\\n    parser.add_argument(\\\"--output_path\\\", required=True, help=\\\"Output JSON path for signals\\\")\\n    parser.add_argument(\\\"--gen\\\", type=int, required=True, help=\\\"Generation number\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--device\\\", type=str, default=\\\"cuda:0\\\", help=\\\"GPU device (e.g. cuda:0)\\\")\\n    parser.add_argument(\\\"--gen_prefix_len\\\", type=int, default=64, help=\\\"Prefix length for distinct-n generation\\\")\\n    parser.add_argument(\\\"--gen_max_new_tokens\\\", type=int, default=128, help=\\\"Max new tokens for distinct-n\\\")\\n    parser.add_argument(\\\"--batch_size\\\", type=int, default=16, help=\\\"Inference batch size\\\")\\n    args = parser.parse_args()\\n\\n    set_seed(args.seed)\\n    device = torch.device(args.device)\\n\\n    print(f\\\"Loading {args.model_path}...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path)\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_path, torch_dtype=torch.bfloat16\\n    ).to(device)\\n    model.eval()\\n\\n    # 1/3 Per-example signals + corpus-level sigma\\n    print(\\\"1/3 Per-example signals (loss, entropy, spectral_rank) + sigma...\\\")\\n    loss_vec, ent_vec, srank_vec, sigma_rank = compute_per_example_signals(\\n        model, tokenizer, args.probe_set_path, device, batch_size=args.batch_size\\n    )\\n\\n    # 2/3 Corpus-level distinct-n\\n    print(\\\"2/3 Distinct-n...\\\")\\n    dn = compute_distinct_n(\\n        model, tokenizer, args.probe_set_path, device,\\n        prefix_len=args.gen_prefix_len,\\n        max_new=args.gen_max_new_tokens,\\n        batch_size=args.batch_size,\\n    )\\n\\n    # 3/3 Spearman correlations\\n    print(\\\"3/3 Spearman correlations...\\\")\\n    rho_le, pval_le = spearmanr(loss_vec, ent_vec)\\n    rho_ls, pval_ls = spearmanr(loss_vec, srank_vec)\\n\\n    loss_arr = np.array(loss_vec)\\n    ent_arr = np.array(ent_vec)\\n    srank_arr = np.array(srank_vec)\\n\\n    result = {\\n        \\\"gen\\\": args.gen,\\n        \\\"seed\\\": args.seed,\\n        \\\"per_example\\\": {\\n            \\\"loss\\\": [round(x, 4) for x in loss_vec],\\n            \\\"entropy\\\": [round(x, 4) for x in ent_vec],\\n            \\\"spectral_rank\\\": [round(x, 2) for x in srank_vec],\\n        },\\n        \\\"aggregated\\\": {\\n            \\\"loss_mean\\\": round(float(loss_arr.mean()), 4),\\n            \\\"loss_std\\\": round(float(loss_arr.std()), 4),\\n            \\\"entropy_mean\\\": round(float(ent_arr.mean()), 4),\\n            \\\"entropy_std\\\": round(float(ent_arr.std()), 4),\\n            \\\"spectral_rank_mean\\\": round(float(srank_arr.mean()), 2),\\n            \\\"spectral_rank_std\\\": round(float(srank_arr.std()), 2),\\n        },\\n        \\\"corpus_level\\\": {\\n            \\\"sigma_spectral_rank\\\": round(sigma_rank, 2),\\n            \\\"distinct_1\\\": round(dn[\\\"distinct_1\\\"], 4),\\n            \\\"distinct_2\\\": round(dn[\\\"distinct_2\\\"], 4),\\n            \\\"distinct_3\\\": round(dn[\\\"distinct_3\\\"], 4),\\n        },\\n        \\\"correlations\\\": {\\n            \\\"rho_loss_entropy\\\": round(float(rho_le), 4),\\n            \\\"pval_loss_entropy\\\": round(float(pval_le), 6),\\n            \\\"rho_loss_spectral_rank\\\": round(float(rho_ls), 4),\\n            \\\"pval_loss_spectral_rank\\\": round(float(pval_ls), 6),\\n        },\\n        \\\"num_probe_samples\\\": len(loss_vec),\\n    }\\n\\n    os.makedirs(os.path.dirname(os.path.abspath(args.output_path)), exist_ok=True)\\n    with open(args.output_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    print(f\\\"\\\\nSignals saved to {args.output_path}\\\")\\n    print(f\\\"  loss: mean={loss_arr.mean():.4f} std={loss_arr.std():.4f}\\\")\\n    print(f\\\"  entropy: mean={ent_arr.mean():.4f} std={ent_arr.std():.4f}\\\")\\n    print(f\\\"  spectral_rank: mean={srank_arr.mean():.2f} std={srank_arr.std():.2f}\\\")\\n    print(f\\\"  sigma_rank: {sigma_rank:.2f}\\\")\\n    print(f\\\"  rho(loss,entropy)={rho_le:.4f} p={pval_le:.6f}\\\")\\n    print(f\\\"  rho(loss,spectral_rank)={rho_ls:.4f} p={pval_ls:.6f}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me summarize the key code facts:

**Per-example spectral rank (§3.2.2):**
- Line 111-121: For each example, take hidden states `h` of shape `[seq_actual, D]` (masked by attention mask)
- Line 117: `h.mean(dim=0)` → mean-pool over sequence dimension → `[D]` vector → stored in `all_mean_hidden`
- Line 120: `torch.linalg.svd(h, full_matrices=False)` → get singular values `S`


- Line 121: Computing the effective rank from those singular values

**Corpus-level SIGMA spectral rank (§3.2.4):**
- Line 129: Stack all the mean hidden states into a matrix of shape `[N, D]` where N=5000
- Line 130: Compute the Gram matrix by multiplying the transpose with itself
- Line 131: Decompose the Gram matrix to extract its singular values
- Line 132: Continuing with the spectral rank calculation on the corpus level

...

The key distinction is that per-example I'm working with the full sequence dimension, while at the corpus level I'm pooling across sequences first, then stacking examples to form a larger matrix before computing the Gram matrix and its spectral properties. I'm realizing that the singular values of the Gram matrix G = H^T H are actually the squared singular values of H itself, which is an important relationship to keep in mind. wait, `torch.linalg.svd(gram)` returns the singular values of gram, not eigenvalues. Since gram = H^T H is symmetric positive semi-definite, its singular values equal its eigenvalues (which are all ≥ 0). And these eigenvalues equal σ² where σ are the singular values of H.

Actually, let me be more precise. `torch.linalg.svd(G)` where G = H^T H:
- G is symmetric PSD
- SVD of G gives singular values which are the absolute eigenvalues
- Since G is PSD, eigenvalues ≥ 0, so singular values = eigenvalues
- These eigenvalues λ_i = σ_i² where σ_i are singular values of H

But the code passes these directly to `effective_rank()`, which normalizes them by dividing by their sum. So it's using the squared singular values of H in the effective rank formula.

Now looking at the current §3.2.4 text, it claims we're "using the same formula as §3.2.2," but that's misleading. In §3.2.2, we apply effective rank to the singular values of H_x directly, whereas here we're applying it to the eigenvalues of the Gram matrix, which are the squared singular values of H.

So the formula (entropy of normalized values) is identical, but the input values are different — one is σ_i, the other is σ_i².

Now I'm tracking the mean-pooling step: for each example, hidden states get pooled over the sequence dimension, collapsing `[seq_actual, D]` down to `[D]`. And for Pythia-410M, that dimension d is 1024.

Let me revise section 3.2.4 to be more precise about the corpus-level spectral rank calculation. We then compute the effective rank from the eigenspectrum of this Gram matrix using a normalized entropy formula based on the eigenvalues, which gives us a single scalar measure of representation diversity for the entire corpus. I need to reconsider whether the effective rank calculation is actually the same when applied to eigenvalues versus singular values. Since the Gram matrix is symmetric and positive semi-definite, its eigenvalues equal its singular values, but when I compute effective rank on λ_i = σ_i² versus σ_i directly, the normalization step produces different probability distributions—normalizing squared values versus the values themselves changes the entropy calculation, so these aren't equivalent approaches. So the same `effective_rank` function applies to both cases, but the inputs differ: per-example uses singular values from the hidden state matrix, while corpus-level uses eigenvalues from the Gram matrix (which are the squared singular values of the mean-pooled hidden states). The reviewer's concern is that calling it "the same formula" obscures these differences, so I need to explicitly show the eigenvalue formulation and clarify how the aggregation method and input to `effective_rank` differ between the two approaches.

Writing the corpus-level section... states across token positions into a single $d$-dimensional vector, yielding a matrix $\mathbf{H}_{\text{corpus}} \in \mathbb{R}^{5000 \times d}$. We form the Gram matrix $\mathbf{G} = \mathbf{H}_{\text{corpus}}^\top \mathbf{H}_{\text{corpus}} \in \mathbb{R}^{d \times d}$ and compute its spectral effective rank:

$$\text{erank}(\mathbf{G}) = \exp\left( -\sum_{i=1}^{d} \hat{\lambda}_i \log \hat{\lambda}_i \right)$$

where $\lambda_i$ are the eigenvalues of $\mathbf{G}$ (obtained via SVD; since $\mathbf{G}$ is positive semi-definite, its singular values equal its eigenvalues) and $\hat{\lambda}_i = \lambda_i / \sum_j \lambda_j$ are their normalized values. This approach differs from per-example effective rank in that it operates on an inter-example Gram matrix of mean-pooled representations rather than intra-sequence hidden states, and it uses eigenvalues of $\mathbf{G}$ instead of singular values directly—capturing overall representation diversity across the corpus. I compute this on the final transformer layer, yielding one scalar per generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "58257e49-bf72-446f-b20e-072fd9c844f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3wTiEGNGYvs2stSpz1fDB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3306,
      "cache_read_input_tokens": 33399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3306
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

_source line 21_

Now I have the full code. Key findings from `compute_signals.py`:

- **Per-example** (line 120): `torch.linalg.svd(h)` on `h ∈ R^{seq_actual × D}` → effective_rank on singular values σ_i
- **Corpus** (lines 129-132): mean-pool each example over tokens (dim=0) → stack to `mean_mat ∈ R^{N × D}` → `gram = mean_mat.T @ mean_mat ∈ R^{D × D}` → `torch.linalg.svd(gram)` → effective_rank on singular values of G (= eigenvalues λ_i of G, since G is PSD, = σ_i² of H_corpus)

The `effective_rank` function (line 55-60) is the same, but the **inputs** differ: singular values σ_i vs eigenvalues λ_i = σ_i².

Now editing §3.2.4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "6071be0e-457a-4765-a261-59bd9591d090",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3wTiEGNGYvs2stSpz1fDB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3306,
      "cache_read_input_tokens": 33399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3306
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01JdnYyiwC8QytQBpGJ7FZmL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/prism_collapse_mixing/artifacts/paper_skeleton.md",
  "old_string": "#### 3.2.4 Corpus-Level Spectral Rank\n\nFor each probe sequence, we mean-pool its last-layer hidden states into a single $d$-dimensional vector, yielding a matrix $\\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{5000 \\times d}$. We then form the Gram matrix $\\mathbf{G} = \\mathbf{H}_{\\text{corpus}}^\\top \\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{d \\times d}$ and compute its spectral effective rank using the same formula as §3.2.2. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).",
  "new_string": "#### 3.2.4 Corpus-Level Spectral Rank\n\nFor each probe sequence, we mean-pool its last-layer hidden states across token positions into a single $d$-dimensional vector, yielding a matrix $\\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{5000 \\times d}$. We form the Gram matrix $\\mathbf{G} = \\mathbf{H}_{\\text{corpus}}^\\top \\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{d \\times d}$ and compute its spectral effective rank:\n\n$$\\text{erank}(\\mathbf{G}) = \\exp\\left( -\\sum_{i=1}^{d} \\hat{\\lambda}_i \\log \\hat{\\lambda}_i \\right)$$\n\nwhere $\\lambda_i$ are the eigenvalues of $\\mathbf{G}$ (obtained via SVD; since $\\mathbf{G}$ is positive semi-definite, its singular values equal its eigenvalues) and $\\hat{\\lambda}_i = \\lambda_i / \\sum_j \\lambda_j$ are their normalized values. This differs from the per-example effective rank (§3.2.2) in two respects: (1) the input is an inter-example Gram matrix constructed from mean-pooled representations, rather than the intra-sequence hidden-state matrix of a single example; and (2) the effective rank operates on eigenvalues $\\lambda_i$ of $\\mathbf{G}$ (equivalently, the squared singular values $\\sigma_i^2$ of $\\mathbf{H}_{\\text{corpus}}$), not on singular values directly. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "3487156c-145c-406b-abfd-bc971aa3fe69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3wTiEGNGYvs2stSpz1fDB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3306,
      "cache_read_input_tokens": 33399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3306
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

_source line 23 · 2026-05-16T02:02:25.133Z_

<details><summary>↩ Tool result · `toolu_01JdnYyiwC8QytQBpGJ7FZmL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/prism_collapse_mixing/artifacts/paper_skeleton.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "729bfc5e-4afa-4cdc-affa-5d72211f358f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/prism_collapse_mixing/artifacts/paper_skeleton.md",
    "oldString": "#### 3.2.4 Corpus-Level Spectral Rank\n\nFor each probe sequence, we mean-pool its last-layer hidden states into a single $d$-dimensional vector, yielding a matrix $\\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{5000 \\times d}$. We then form the Gram matrix $\\mathbf{G} = \\mathbf{H}_{\\text{corpus}}^\\top \\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{d \\times d}$ and compute its spectral effective rank using the same formula as §3.2.2. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).",
    "newString": "#### 3.2.4 Corpus-Level Spectral Rank\n\nFor each probe sequence, we mean-pool its last-layer hidden states across token positions into a single $d$-dimensional vector, yielding a matrix $\\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{5000 \\times d}$. We form the Gram matrix $\\mathbf{G} = \\mathbf{H}_{\\text{corpus}}^\\top \\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{d \\times d}$ and compute its spectral effective rank:\n\n$$\\text{erank}(\\mathbf{G}) = \\exp\\left( -\\sum_{i=1}^{d} \\hat{\\lambda}_i \\log \\hat{\\lambda}_i \\right)$$\n\nwhere $\\lambda_i$ are the eigenvalues of $\\mathbf{G}$ (obtained via SVD; since $\\mathbf{G}$ is positive semi-definite, its singular values equal its eigenvalues) and $\\hat{\\lambda}_i = \\lambda_i / \\sum_j \\lambda_j$ are their normalized values. This differs from the per-example effective rank (§3.2.2) in two respects: (1) the input is an inter-example Gram matrix constructed from mean-pooled representations, rather than the intra-sequence hidden-state matrix of a single example; and (2) the effective rank operates on eigenvalues $\\lambda_i$ of $\\mathbf{G}$ (equivalently, the squared singular values $\\sigma_i^2$ of $\\mathbf{H}_{\\text{corpus}}$), not on singular values directly. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).",
    "originalFile": "# PRISM: Probing the Decoupling of Loss and Collapse Signals in Iterative Synthetic Training\n\n---\n\n## 2. Related Work\n\n### 2.1 Model Collapse in Iterative Training\n\nTraining generative models on their own outputs across successive generations leads to *model collapse*—a progressive loss of distributional fidelity that manifests as tail truncation and mode reduction. Shumailov et al. (2024) established this phenomenon across LLMs, VAEs, and GMMs, showing that distribution tails vanish first while bulk statistics remain superficially intact. Dohmatob et al. (2025) provided a theoretical grounding through the lens of the data processing inequality (DPI), proving that even trace amounts of synthetic contamination (as low as 1/1000) suffice to trigger collapse under iterative retraining, with degradation following an exponential decay in effective distributional support.\n\nA critical design variable is whether synthetic data *replaces* or *accumulates* alongside real data across generations. Gerstgrasser et al. (2024) demonstrated that accumulation strategies can avoid collapse entirely, while replacement strategies—where each generation discards prior data—reliably induce it. Our experimental design deliberately adopts the replacement paradigm (fixed 50/50 real-synthetic ratio, re-generated each generation) to create conditions under which collapse is expected, enabling controlled study of its detection.\n\nSchaeffer et al. (2025) drew attention to definitional ambiguity in the collapse literature, cataloguing eight distinct operationalizations. They argued that population-level risk (i.e., validation loss) can remain stable even as tail risk deteriorates—a conceptual precursor to the loss–signal decoupling we investigate. Yi et al. (2025) showed that external verifiers injecting fresh information can prevent collapse, suggesting that if collapse signals can serve as verification criteria, they may enable principled data filtering in iterative pipelines.\n\n### 2.2 Data Mixing Strategies\n\nOnline data mixing methods dynamically adjust domain proportions during training to optimize learning efficiency. DoReMi (Xie et al., 2024) uses a small proxy model to reweight domain mixtures via distributionally robust optimization. AIOLI (Chen et al., 2024) extends this with online gradient-based updates to mixing coefficients. ODM (Fan et al., 2024) optimizes domain mixtures by tracking per-domain loss trajectories.\n\nThese methods share a common dependency: they use *loss* (or loss-derived gradients) as the sole signal for mixture adjustment. This is well-motivated when training data is static and well-characterized, but becomes problematic in iterative synthetic training where the data distribution itself degrades across generations. If collapse manifests in ways that loss fails to capture—a possibility suggested by the theoretical work reviewed above—then loss-driven mixing may be blind to distributional deterioration.\n\n### 2.3 Collapse Detection Beyond Loss\n\nSeveral lines of work have developed signals that capture aspects of model behavior orthogonal to loss.\n\n**Entropy-based monitoring.** He et al. (2025) demonstrated a strong linear correlation between training data entropy and model generalization capacity, observing that entropy decline drives a generalization-to-memorization transition during iterative training. Truong & Truong (2025) formalized entropy collapse as a first-order phase transition, arguing that collapsed systems can maintain stable local performance (i.e., loss) while the effective dimensionality of their adaptive behavior has already contracted. This theoretical prediction—that loss stability can coexist with entropy collapse—directly motivates our empirical investigation, but neither work validated the claim in LLM iterative training.\n\n**Spectral methods.** Gu et al. (2026) proposed SIGMA, which tracks collapse via the eigenspectrum of embedding Gram matrices, providing scalable one-sided monitoring bounds that serve as early warnings for representation space contraction. Qiu et al. (2025) introduced Spectral Alignment (SA), showing that spectral distributional shifts in weight matrices precede loss explosions by a detectable margin, implying a temporal lag between spectral degradation and loss response. Both works establish spectral signals as informative collapse indicators but neither examines how their correlation with loss evolves across generations.\n\n**Diversity metrics.** Zhu et al. (2025) systematically compared diversity measures for synthetic data—including n-gram distinctness, self-BLEU, and the proposed DCScore—finding that classification-based diversity metrics correlate most strongly with human judgments. We adopt distinct-n (n=1,2,3) as a lightweight, interpretable generation-diversity signal alongside our representation-level metrics.\n\n**Gap in the literature.** Existing work has (a) theoretically predicted that collapse can occur without loss degradation (Truong & Truong, 2025; Schaeffer et al., 2025), (b) shown that entropy tracks generalization within a single generation (He et al., 2025), and (c) developed spectral monitoring tools that detect collapse independently of loss (Gu et al., 2026; Qiu et al., 2025). However, no prior work has quantified how the *correlation* between loss and these collapse signals evolves across iterative training generations. We address this gap by tracking Spearman rank correlation ρ(loss, signal) across multiple generations, testing whether signals that are initially coupled to loss become progressively decoupled as collapse advances.\n\n---\n\n## 3. Method\n\n### 3.1 Iterative Synthetic Training Setup\n\n**Model.** We use Pythia-410M-deduped (Biderman et al., 2023), a decoder-only transformer with 410M parameters pretrained on the Pile (deduplicated). This model is small enough to permit rapid multi-generation iteration on 2× RTX 6000 GPUs while being large enough to exhibit nontrivial language modeling behavior and collapse dynamics. The deduplication ensures our baseline is not already compromised by near-duplicate memorization artifacts.\n\n**Real data.** We sample a fixed subset from FineWeb (Penedo et al., 2024), a curated web corpus. Each training generation uses the same real-data pool to isolate the effect of synthetic data degradation across generations.\n\n**Synthetic data generation.** At each generation $g$, the model $M_g$ generates synthetic text via nucleus sampling (top-p = 0.9, temperature = 1.0) starting from the BOS token (unconditional generation) to match the token count of the real data portion. Each sample generates up to 256 new tokens. Each generation produces fresh synthetic data; prior generations' synthetic outputs are discarded (replacement paradigm).\n\n**Training configuration.** Each generation trains for approximately 200M tokens with a 50/50 real-synthetic mixing ratio (by token count). We use AdamW (β₁=0.9, β₂=0.999, weight decay 0.01) with a cosine learning rate schedule (peak lr = 1e-5, warmup over the first 2% of steps). Batch size is 32 sequences of 1024 tokens. Training resumes from the previous generation's final checkpoint, simulating the iterative retraining scenario studied in the collapse literature (Shumailov et al., 2024; Gerstgrasser et al., 2024).\n\n**Iterative protocol.** Starting from the pretrained Pythia-410M checkpoint (Gen 0 baseline), we execute three generations of iterative training:\n- **Gen 0→1:** Train on 50% FineWeb + 50% synthetic from the pretrained Pythia-410M.\n- **Gen 1→2:** Train on 50% FineWeb + 50% synthetic from the Gen 1 model.\n- **Gen 2→3:** Train on 50% FineWeb + 50% synthetic from the Gen 2 model.\n\nEach generation produces a model checkpoint and a corresponding set of collapse signal measurements on a fixed probe set.\n\n**Reproducibility.** We run the full pipeline with two independent random seeds (42 and 137), controlling for initialization noise in both synthetic data generation and training stochasticity. Both seeds share the same real data subset and probe set.\n\n### 3.2 Collapse Signal Definitions\n\nWe define four collapse signals spanning three levels of granularity: token-level, representation-level, and generation-level. All signals are computed on a fixed **probe set** of 5,000 sequences (256 tokens each) sampled from the FineWeb validation split, with no overlap with the training data.\n\n#### 3.2.1 Per-Example Output Entropy\n\nFor each probe sequence $x = (x_1, \\ldots, x_T)$, we compute the mean next-token prediction entropy:\n\n$$H(x) = -\\frac{1}{T} \\sum_{t=1}^{T} \\sum_{v \\in \\mathcal{V}} p_\\theta(v \\mid x_{&lt;t}) \\log p_\\theta(v \\mid x_{&lt;t})$$\n\nwhere $\\mathcal{V}$ is the vocabulary and $p_\\theta$ is the model's softmax distribution. Output entropy measures the uncertainty of the model's predictions; collapse concentrates probability mass on fewer tokens, reducing $H$. This yields one scalar per probe example, enabling per-example correlation with loss.\n\n#### 3.2.2 Per-Example Spectral Effective Rank\n\nFor each probe sequence $x$, let $\\mathbf{H}_x \\in \\mathbb{R}^{T \\times d}$ be the matrix of last-layer hidden states across all $T$ positions. The spectral effective rank (Roy & Vetterli, 2007) is:\n\n$$\\text{erank}(\\mathbf{H}_x) = \\exp\\left( -\\sum_{i=1}^{\\min(T,d)} \\hat{\\sigma}_i \\log \\hat{\\sigma}_i \\right)$$\n\nwhere $\\hat{\\sigma}_i = \\sigma_i / \\sum_j \\sigma_j$ are the normalized singular values of $\\mathbf{H}_x$. Effective rank captures the dimensionality of the representation manifold: collapse reduces the number of directions the model actively uses, concentrating variance into fewer singular values. This yields one scalar per probe example.\n\n#### 3.2.3 Distinct-n\n\nFor a set of generated continuations (all probe-set sequences, each continued for 128 new tokens from 64-token prefixes using the same sampling parameters as training synthetic data), we compute:\n\n$$\\text{distinct-}n = \\frac{|\\text{unique } n\\text{-grams}|}{|\\text{total } n\\text{-grams}|}$$\n\nfor $n \\in \\{1, 2, 3\\}$. Distinct-n directly measures lexical diversity of model outputs; collapse produces repetitive text with declining distinct-n. This is a corpus-level metric (one scalar per generation) and thus contributes to trend analysis rather than per-example correlation.\n\n#### 3.2.4 Corpus-Level Spectral Rank\n\nFor each probe sequence, we mean-pool its last-layer hidden states into a single $d$-dimensional vector, yielding a matrix $\\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{5000 \\times d}$. We then form the Gram matrix $\\mathbf{G} = \\mathbf{H}_{\\text{corpus}}^\\top \\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{d \\times d}$ and compute its spectral effective rank using the same formula as §3.2.2. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).\n\n### 3.3 Statistical Methods\n\nOur central analysis quantifies how the relationship between loss and each collapse signal evolves across generations.\n\n**Primary metric: Spearman rank correlation.** For each generation $g$ and each per-example signal $s \\in \\{\\text{entropy}, \\text{spectral effective rank}\\}$, we compute the Spearman rank correlation $\\rho_g$ between per-example loss $\\ell(x)$ and signal value $s(x)$ across the 5,000 probe examples. Spearman correlation is chosen over Pearson because it captures monotonic relationships without assuming linearity, and is robust to outliers in either loss or signal distributions.\n\n**Confidence intervals.** We construct 95% bootstrap confidence intervals for each $\\rho_g$ by resampling the 5,000 probe examples with replacement (1,000 bootstrap iterations). This provides uncertainty estimates that account for probe-set heterogeneity without distributional assumptions.\n\n**Effect size.** To quantify the magnitude of decoupling, we report $\\Delta\\rho = \\rho_0 - \\rho_g$ (the drop in correlation from baseline) and normalize by bootstrap standard error: $\\text{effect size} = \\Delta\\rho / \\text{SE}_{\\text{bootstrap}}$. This enables comparison across signals with different baseline correlation strengths.\n\n**Trend significance.** To assess whether the observed $\\rho$ decline constitutes a statistically reliable trend rather than noise, we employ a permutation test: we randomly shuffle the generation labels (0, 1, 2, 3) 10,000 times and compute the Spearman correlation of $\\rho$ values with generation index under each permutation. The p-value is the fraction of permuted slopes as steep or steeper than the observed slope.\n\n**Signal degradation.** For each collapse signal, we report the mean value per generation and test for monotonic decline. Degradation magnitude is quantified as the relative change from Gen 0 to the final generation: $\\Delta_{\\text{rel}} = (s_0 - s_G) / s_0$.\n\n### 3.4 Pre-registered Pass/Fail Criteria\n\nWe pre-register three conditions that must all be satisfied for the hypothesis to pass:\n\n**C1 (Decoupling).** At least one collapse signal exhibits $|\\rho_g|$ with loss dropping from $> 0.7$ at Gen 0–1 to $< 0.5$ at Gen 3. This threshold ensures that the signal begins meaningfully coupled to loss (sharing >49% of rank variance) and ends meaningfully decoupled (sharing <25%).\n\n**C2 (Signal degradation).** The same signal's mean value monotonically degrades across generations (each generation lower than the previous), with a cumulative decline of $\\geq 15\\%$ from Gen 0 to Gen 3. This condition ensures that decoupling is driven by genuine collapse (the signal detects worsening behavior) rather than mere noise inflation that could artificially reduce $\\rho$.\n\n**C3 (Reproducibility).** C1 and C2 are both observed under both random seeds (42 and 137). Single-seed results cannot distinguish systematic phenomena from run-specific artifacts.\n\n**Contingency.** If the pattern emerges in one seed but not the other (weak pass), we run a third seed (7) as a tiebreaker. If all three conditions fail outright, we conclude that three generations are insufficient to observe decoupling at this model scale and either extend to five generations or reassess the hypothesis.\n\n---\n\n## References\n\n- Biderman, S., Schoelkopf, H., Anthony, Q., et al. (2023). Pythia: A suite for analyzing large language models across training and scaling. *ICML 2023*.\n- Chen, M., et al. (2024). AIOLI: Online data mixing via gradient-based optimization. *arXiv*.\n- Dohmatob, E., Feng, Y., Yang, P., Charton, F., & Kempe, J. (2025). Strong model collapse. *ICLR 2025 (Spotlight)*.\n- Fan, Y., et al. (2024). Online data mixing for language model pre-training. *arXiv*.\n- Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., et al. (2024). Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data. *COLM 2024*.\n- Gu, Y., et al. (2026). SIGMA: Scalable spectral insights for LLM model collapse. *arXiv*.\n- He, S., et al. (2025). A closer look at model collapse: From a generalization-to-memorization perspective. *NeurIPS 2025 (Spotlight)*.\n- Penedo, G., et al. (2024). The FineWeb datasets: Decanting the web for the finest text data at scale. *arXiv*.\n- Qiu, H., Wu, Y., Tan, Y., Wang, Y., & Yao, Q. (2025). Spectral alignment as predictor of loss explosion in neural network training. *arXiv*.\n- Roy, O. & Vetterli, M. (2007). The effective rank: A measure of effective dimensionality. *European Signal Processing Conference*.\n- Schaeffer, R., Kazdan, J., Arulandu, A. C., & Koyejo, S. (2025). Position: Model collapse does not mean what you think. *arXiv (NeurIPS 2025 Position Track)*.\n- Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature*.\n- Truong, X. K. & Truong, Q. H. (2025). Entropy collapse: A universal failure mode of intelligent systems. *arXiv*.\n- Xie, S. M., et al. (2024). DoReMi: Optimizing data mixtures speeds up language model pretraining. *NeurIPS 2024*.\n- Yi, B., Liu, Q., Cheng, Y., & Xu, H. (2025). Escaping model collapse via synthetic data verification. *ICML 2025*.\n- Zhu, Y., Zhang, H., Wu, B., et al. (2025). Measuring diversity in synthetic datasets. *ICML 2025*.\n",
    "structuredPatch": [
      {
        "oldStart": 83,
        "oldLines": 8,
        "newStart": 83,
        "newLines": 12,
        "lines": [
          " ",
          " #### 3.2.4 Corpus-Level Spectral Rank",
          " ",
          "-For each probe sequence, we mean-pool its last-layer hidden states into a single $d$-dimensional vector, yielding a matrix $\\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{5000 \\times d}$. We then form the Gram matrix $\\mathbf{G} = \\mathbf{H}_{\\text{corpus}}^\\top \\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{d \\times d}$ and compute its spectral effective rank using the same formula as §3.2.2. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).",
          "+For each probe sequence, we mean-pool its last-layer hidden states across token positions into a single $d$-dimensional vector, yielding a matrix $\\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{5000 \\times d}$. We form the Gram matrix $\\mathbf{G} = \\mathbf{H}_{\\text{corpus}}^\\top \\mathbf{H}_{\\text{corpus}} \\in \\mathbb{R}^{d \\times d}$ and compute its spectral effective rank:",
          " ",
          "+$$\\text{erank}(\\mathbf{G}) = \\exp\\left( -\\sum_{i=1}^{d} \\hat{\\lambda}_i \\log \\hat{\\lambda}_i \\right)$$",
          "+",
          "+where $\\lambda_i$ are the eigenvalues of $\\mathbf{G}$ (obtained via SVD; since $\\mathbf{G}$ is positive semi-definite, its singular values equal its eigenvalues) and $\\hat{\\lambda}_i = \\lambda_i / \\sum_j \\lambda_j$ are their normalized values. This differs from the per-example effective rank (§3.2.2) in two respects: (1) the input is an inter-example Gram matrix constructed from mean-pooled representations, rather than the intra-sequence hidden-state matrix of a single example; and (2) the effective rank operates on eigenvalues $\\lambda_i$ of $\\mathbf{G}$ (equivalently, the squared singular values $\\sigma_i^2$ of $\\mathbf{H}_{\\text{corpus}}$), not on singular values directly. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).",
          "+",
          " ### 3.3 Statistical Methods",
          " ",
          " Our central analysis quantifies how the relationship between loss and each collapse signal evolves across generations."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 24_

§3.2.4 已修改。改动内容：

1. 删除了 "using the same formula as §3.2.2"
2. 写出了显式公式，明确使用 eigenvalues λ_i（而非 singular values σ_i）
3. 说明 mean-pool 是对 token positions 取平均
4. 列出与 §3.2.2 的两点区别：(a) inter-example Gram matrix vs intra-sequence hidden-state matrix；(b) eigenvalues λ_i of G (= σ_i² of H_corpus) vs singular values directly
5. 所有描述均来自 `compute_signals.py` 第 115-132 行的实际代码

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "uuid": "35ffdbd8-0cba-4ca8-80c2-d6d4958fd7b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AiYc37qknb99jGpDBn3zs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4280,
      "cache_read_input_tokens": 36705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4280
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

_source line 25_

§3.2.4 已修改。改动内容：

1. 删除了 "using the same formula as §3.2.2"
2. 写出了显式公式，明确使用 eigenvalues λ_i（而非 singular values σ_i）
3. 说明 mean-pool 是对 token positions 取平均
4. 列出与 §3.2.2 的两点区别：(a) inter-example Gram matrix vs intra-sequence hidden-state matrix；(b) eigenvalues λ_i of G (= σ_i² of H_corpus) vs singular values directly
5. 所有描述均来自 `compute_signals.py` 第 115-132 行的实际代码

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 105187,
  "duration_api_ms": 105194,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "74a34dee-772a-4bf9-99b5-fd79ddebd1b4",
  "total_cost_usd": 0.4095785,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 29144,
    "cache_read_input_tokens": 195855,
    "output_tokens": 5114,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29144,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 195,
        "cache_read_input_tokens": 36705,
        "cache_creation_input_tokens": 4280,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4280
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1516,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001596,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 5114,
      "cacheReadInputTokens": 195855,
      "cacheCreationInputTokens": 29144,
      "webSearchRequests": 0,
      "costUSD": 0.40798249999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3d036154-fb49-43ec-ba6e-af38bd8cd30f"
}
```

</details>

---
