# infra importance vs random

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_infra_importance-vs-random_20260513T222105.log`
- **Structured JSON:** [`1e74323409509b6fdfab.json`](../../sessions/1e/1e74323409509b6fdfab.json)

## Before a recorded user message

42 recorded events

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
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
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
  "uuid": "a277c174-8a4e-416b-bbcc-f170242f125a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778722800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7e04db18-544f-40e6-949b-0f7b62c314c6",
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to run an importance-based vs random masking PPL comparison experiment on their server. Let me break this down:

1. SSH to westd-22162
2. Write the script to the server
3. Run it on cuda:1
4. Report results

Let me start by writing the script to the server and running it.

First, let me load the necessary MCP tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "76e7fe9a-d3cc-47a5-8f5c-82d7f6dbebd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCmY1rggJEfES9bjnNXBeb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14581,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14581
      },
      "output_tokens": 21,
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

开始执行：写入脚本到服务器并运行 importance vs random masking 对比实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "8b3f9c13-ce24-4794-bfdf-39b6f6a16b09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCmY1rggJEfES9bjnNXBeb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14581,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14581
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XAMLq3EFk2BzGzPC72ET4p`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "62213274-cf87-4093-9d1e-ce2271ba2dae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCmY1rggJEfES9bjnNXBeb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14581,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14581
      },
      "output_tokens": 21,
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

_source line 7 · 2026-05-13T22:21:21.323Z_

<details><summary>↩ Tool result · `toolu_01XAMLq3EFk2BzGzPC72ET4p`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "e9fbb64c-89a2-4be4-9dda-2252fca740fe",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UMBqBkLE45TpLiDLh7DynP`</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B/config.json",
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
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "319ff280-c942-4c50-8061-6aeddbc05837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ujy4hyS7Kzepa5nsN6NiEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 26422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1005
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

_source line 9 · 2026-05-13T22:21:25.538Z_

<details><summary>↩ Tool result · `toolu_01UMBqBkLE45TpLiDLh7DynP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "c1fb1b86-c0f6-424a-8a87-e0e306226598",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B/config.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.26}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

模型存在，写入脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "bd77a1fb-f7d3-4e6f-addf-a64862667f14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYPfYhekGzBvds61yJ2T57",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 27427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 252
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01TkLv5uSuum88GsTwyrbo4C`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "cat > /root/autodl-tmp/pacs/importance_vs_random.py << 'SCRIPT_EOF'\n\"\"\"\nCompare importance-based vs random head masking + KV eviction.\nTests on 5 MATH problems at sparsity 10%, 20%, 30%.\n\"\"\"\nimport torch\nimport json\nimport os\nimport numpy as np\n\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"1\"\n\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\ndef compute_ppl(model, input_ids, labels):\n    with torch.no_grad():\n        out = model(input_ids=input_ids, labels=labels)\n        return torch.exp(out.loss).item()\n\ndef importance_based_head_mask(model, input_ids, num_heads, ratio, num_kv_heads=4):\n    calib_ids = input_ids[:, :128] if input_ids.shape[1] > 128 else input_ids\n    with torch.no_grad():\n        out = model(calib_ids, output_attentions=True)\n    \n    head_importance = torch.zeros(num_heads)\n    n_layers = len(out.attentions)\n    for layer_attn in out.attentions:\n        per_head_norm = layer_attn[0].float().norm(dim=(-2, -1))\n        head_importance += per_head_norm.cpu()\n    head_importance /= n_layers\n    \n    n_mask = int(num_heads * ratio)\n    _, least_important = torch.topk(head_importance, n_mask, largest=False)\n    mask = torch.ones(num_heads, dtype=torch.bool)\n    mask[least_important] = False\n    return mask\n\ndef random_head_mask(num_heads, ratio, seed=42):\n    torch.manual_seed(seed)\n    n_mask = int(num_heads * ratio)\n    perm = torch.randperm(num_heads)\n    mask = torch.ones(num_heads, dtype=torch.bool)\n    mask[perm[:n_mask]] = False\n    return mask\n\ndef importance_based_kv_mask(model, input_ids, seq_len, ratio):\n    calib_ids = input_ids[:, :128] if input_ids.shape[1] > 128 else input_ids\n    calib_len = calib_ids.shape[1]\n    with torch.no_grad():\n        out = model(calib_ids, output_attentions=True)\n    \n    pos_importance = torch.zeros(seq_len)\n    n_layers = len(out.attentions)\n    for layer_attn in out.attentions:\n        avg_attn = layer_attn[0].float().mean(dim=0)\n        attn_sum = avg_attn.sum(dim=0).cpu()\n        pos_importance[:calib_len] += attn_sum\n    pos_importance /= n_layers\n    \n    n_evict = int(seq_len * ratio)\n    pos_importance[0] = float('inf')\n    _, least_important = torch.topk(pos_importance, n_evict, largest=False)\n    mask = torch.ones(seq_len, dtype=torch.bool)\n    mask[least_important] = False\n    return mask\n\ndef random_kv_mask(seq_len, ratio, seed=42):\n    torch.manual_seed(seed)\n    n_evict = int(seq_len * ratio)\n    candidates = torch.arange(1, seq_len)\n    perm = candidates[torch.randperm(len(candidates))]\n    evict_indices = perm[:n_evict]\n    mask = torch.ones(seq_len, dtype=torch.bool)\n    mask[evict_indices] = False\n    return mask\n\ndef apply_head_mask_hook(model, head_mask):\n    handles = []\n    num_heads = len(head_mask)\n    \n    for layer in model.model.layers:\n        attn = layer.self_attn\n        def make_hook(mask):\n            def hook(module, input, output):\n                hidden = output[0]\n                head_dim = hidden.shape[-1] // num_heads\n                h = hidden.view(hidden.shape[0], hidden.shape[1], num_heads, head_dim)\n                h[:, :, ~mask, :] = 0\n                return (h.view_as(hidden),) + output[1:]\n            return hook\n        handles.append(attn.o_proj.register_forward_hook(make_hook(head_mask)))\n    return handles\n\ndef apply_kv_mask(model, input_ids, kv_mask):\n    seq_len = input_ids.shape[1]\n    attn_mask = torch.zeros(1, 1, seq_len, seq_len, device=input_ids.device, dtype=torch.float16)\n    causal = torch.triu(torch.ones(seq_len, seq_len, device=input_ids.device), diagonal=1).bool()\n    attn_mask.masked_fill_(causal.unsqueeze(0).unsqueeze(0), float('-inf'))\n    evicted = ~kv_mask.to(input_ids.device)\n    attn_mask[:, :, :, evicted] = float('-inf')\n    return attn_mask\n\ndef main():\n    model_path = \"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\"\n    \n    print(\"Loading model...\")\n    tokenizer = AutoTokenizer.from_pretrained(model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path, torch_dtype=torch.float16, device_map=\"cuda:0\",\n        attn_implementation=\"eager\",\n    )\n    model.eval()\n    \n    num_heads = model.config.num_attention_heads\n    num_kv_heads = model.config.num_key_value_heads\n    print(f\"Heads: {num_heads}, KV heads: {num_kv_heads}\")\n    \n    prompts = [\n        \"Solve step by step: What is the remainder when 2^100 is divided by 7?\\nSolution: Let me think through this systematically.\",\n        \"Solve step by step: If f(x) = x^2 + 3x - 5, find f(f(2)).\\nSolution: First I need to find f(2), then apply f again.\",\n        \"Solve step by step: A circle has center (3, 4) and passes through the origin. What is its radius?\\nSolution: The radius equals the distance from center to origin.\",\n        \"Solve step by step: How many ways can you arrange the letters in MISSISSIPPI?\\nSolution: This is a permutation with repeated elements.\",\n        \"Solve step by step: Find the sum of the first 20 terms of the arithmetic sequence 3, 7, 11, 15, ...\\nSolution: The common difference is 4.\",\n    ]\n    \n    ratios = [0.1, 0.2, 0.3]\n    results = []\n    \n    for i, prompt in enumerate(prompts):\n        print(f\"\\n=== Problem {i+1} ===\")\n        inputs = tokenizer(prompt, return_tensors=\"pt\").to(\"cuda:0\")\n        input_ids = inputs[\"input_ids\"]\n        seq_len = input_ids.shape[1]\n        print(f\"Seq len: {seq_len}\")\n        \n        dense_ppl = compute_ppl(model, input_ids, input_ids)\n        print(f\"Dense PPL: {dense_ppl:.2f}\")\n        \n        for ratio in ratios:\n            print(f\"\\n  --- Sparsity {ratio} ---\")\n            \n            imp_hmask = importance_based_head_mask(model, input_ids, num_heads, ratio, num_kv_heads)\n            rnd_hmask = random_head_mask(num_heads, ratio)\n            \n            imp_kvmask = importance_based_kv_mask(model, input_ids, seq_len, ratio)\n            rnd_kvmask = random_kv_mask(seq_len, ratio)\n            \n            for method, hmask, kvmask in [\n                (\"importance\", imp_hmask, imp_kvmask),\n                (\"random\", rnd_hmask, rnd_kvmask),\n            ]:\n                hooks = apply_head_mask_hook(model, hmask.to(\"cuda:0\"))\n                head_ppl = compute_ppl(model, input_ids, input_ids)\n                for h in hooks: h.remove()\n                \n                kv_attn_mask = apply_kv_mask(model, input_ids, kvmask)\n                with torch.no_grad():\n                    out = model(input_ids=input_ids, attention_mask=kv_attn_mask, labels=input_ids)\n                    kv_ppl = torch.exp(out.loss).item()\n                \n                hooks = apply_head_mask_hook(model, hmask.to(\"cuda:0\"))\n                with torch.no_grad():\n                    out = model(input_ids=input_ids, attention_mask=kv_attn_mask, labels=input_ids)\n                    both_ppl = torch.exp(out.loss).item()\n                for h in hooks: h.remove()\n                \n                print(f\"  {method}: head={head_ppl:.2f} ({head_ppl/dense_ppl:.2f}x), \"\n                      f\"kv={kv_ppl:.2f} ({kv_ppl/dense_ppl:.2f}x), \"\n                      f\"both={both_ppl:.2f} ({both_ppl/dense_ppl:.2f}x)\")\n                \n                results.append({\n                    \"problem\": i,\n                    \"seq_len\": seq_len,\n                    \"ratio\": ratio,\n                    \"method\": method,\n                    \"dense_ppl\": dense_ppl,\n                    \"head_ppl\": head_ppl,\n                    \"kv_ppl\": kv_ppl,\n                    \"both_ppl\": both_ppl,\n                    \"head_degradation\": head_ppl / dense_ppl,\n                    \"kv_degradation\": kv_ppl / dense_ppl,\n                    \"both_degradation\": both_ppl / dense_ppl,\n                })\n    \n    print(\"\\n\" + \"=\"*80)\n    print(\"SUMMARY: Average degradation ratios\")\n    print(\"=\"*80)\n    for ratio in ratios:\n        for method in [\"importance\", \"random\"]:\n            subset = [r for r in results if r[\"ratio\"] == ratio and r[\"method\"] == method]\n            avg_head = np.mean([r[\"head_degradation\"] for r in subset])\n            avg_kv = np.mean([r[\"kv_degradation\"] for r in subset])\n            avg_both = np.mean([r[\"both_degradation\"] for r in subset])\n            print(f\"  {method} @ {ratio}: head={avg_head:.2f}x, kv={avg_kv:.2f}x, both={avg_both:.2f}x\")\n    \n    with open(\"/root/autodl-tmp/pacs/importance_vs_random_results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(\"\\nResults saved.\")\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"SCRIPT_WRITTEN\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "6ab42ddb-853a-40ee-b2fa-8c88b8c0b3a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYPfYhekGzBvds61yJ2T57",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 27427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 252
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

_source line 12 · 2026-05-13T22:22:06.320Z_

<details><summary>↩ Tool result · `toolu_01TkLv5uSuum88GsTwyrbo4C`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"SCRIPT_WRITTEN\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "cb2b1e0a-7b5e-4d3c-a3ac-4ec822dcfcec",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"SCRIPT_WRITTEN\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"SCRIPT_WRITTEN\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

脚本已写入，启动实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "ef2ba75d-e1d8-410c-adb2-a3fa54d65f06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bwQGWz1EP2tQ9Um7emYcH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3086,
      "cache_read_input_tokens": 27679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3086
      },
      "output_tokens": 5,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01P8UP8Snd43CkPMFodfa7RB`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "cd /root/autodl-tmp && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python pacs/importance_vs_random.py' > /tmp/imp_vs_rnd.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "a9509a1d-0355-4e6d-aafb-279b307be377",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bwQGWz1EP2tQ9Um7emYcH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3086,
      "cache_read_input_tokens": 27679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3086
      },
      "output_tokens": 5,
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

_source line 15 · 2026-05-13T22:22:21.077Z_

<details><summary>↩ Tool result · `toolu_01P8UP8Snd43CkPMFodfa7RB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=18395\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.07}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "a472cb8b-e34a-4aac-8149-7fb2e6b2968d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"PID=18395\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.07}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"PID=18395\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.07}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

PID=18395，后台运行中。等待模型加载后检查进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "3e225c8a-c7ee-4164-a175-6eb7a1feada1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PV5NZjGi16jUaNvhMH2dTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 30765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DAbQFUdZzhizShU1LVRbru`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "tail -20 /tmp/imp_vs_rnd.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "0cdb1379-4db2-478f-a37a-2430f82dc735",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PV5NZjGi16jUaNvhMH2dTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 30765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

_source line 18 · 2026-05-13T22:22:24.306Z_

<details><summary>↩ Tool result · `toolu_01DAbQFUdZzhizShU1LVRbru`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/transformers/utils/deprecation.py\\\", line 172, in wrapped_func\\n    return func(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/transformers/models/qwen2/modeling_qwen2.py\\\", line 182, in forward\\n    attn_output = self.o_proj(attn_output)\\n                  ^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\", line 1776, in _wrapped_call_impl\\n    return self._call_impl(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\", line 1882, in _call_impl\\n    return inner()\\n           ^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\", line 1843, in inner\\n    hook_result = hook(self, args, result)\\n                  ^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/autodl-tmp/pacs/importance_vs_random.py\\\", line 86, in hook\\n    h = hidden.view(hidden.shape[0], hidden.shape[1], num_heads, head_dim)\\n        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\nRuntimeError: shape '[33, 3584, 28, 128]' is invalid for input of size 118272\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "14911567-813d-4159-95aa-ac5848ee0a20",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/transformers/utils/deprecation.py\\\\\\\", line 172, in wrapped_func\\\\n    return func(*args, **kwargs)\\\\n           ^^^^^^^^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/transformers/models/qwen2/modeling_qwen2.py\\\\\\\", line 182, in forward\\\\n    attn_output = self.o_proj(attn_output)\\\\n                  ^^^^^^^^^^^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\\\\\", line 1776, in _wrapped_call_impl\\\\n    return self._call_impl(*args, **kwargs)\\\\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\\\\\", line 1882, in _call_impl\\\\n    return inner()\\\\n           ^^^^^^^\\\\n  File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\\\\\", line 1843, in inner\\\\n    hook_result = hook(self, args, result)\\\\n                  ^^^^^^^^^^^^^^^^^^^^^^^^\\\\n  File \\\\\\\"/root/autodl-tmp/pacs/importance_vs_random.py\\\\\\\", line 86, in hook\\\\n    h = hidden.view(hidden.shape[0], hidden.shape[1], num_heads, head_dim)\\\\n        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\\\nRuntimeError: shape '[33, 3584, 28, 128]' is invalid for input of size 118272\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/transformers/utils/deprecation.py\\\", line 172, in wrapped_func\\n    return func(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/transformers/models/qwen2/modeling_qwen2.py\\\", line 182, in forward\\n    attn_output = self.o_proj(attn_output)\\n                  ^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\", line 1776, in _wrapped_call_impl\\n    return self._call_impl(*args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\", line 1882, in _call_impl\\n    return inner()\\n           ^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py\\\", line 1843, in inner\\n    hook_result = hook(self, args, result)\\n                  ^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/autodl-tmp/pacs/importance_vs_random.py\\\", line 86, in hook\\n    h = hidden.view(hidden.shape[0], hidden.shape[1], num_heads, head_dim)\\n        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\nRuntimeError: shape '[33, 3584, 28, 128]' is invalid for input of size 118272\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The issue is that the `o_proj` output shape doesn't match what we expect. The o_proj output is `(batch, seq, hidden_dim)` but hidden_dim = 3584 and num_heads = 28, so head_dim = 128, which means 28*128 = 3584. But the actual size is 118272. Let me check: 33 * 3584 = 118272. So the shape is (33, 3584) - it seems the output is 2D, not 3D.

Wait, looking more carefully: the error says `shape '[33, 3584, 28, 128]' is invalid for input of size 118272`. 

So the hidden tensor is (33, 3584) with 118272 total elements, but we're trying to reshape it to (33, 3584, 28, 128) which would require far more elements. The real issue is that o_proj outputs (batch, seq, hidden_dim) where hidden_dim is already the full 3584, not the pre-projection attention output, so trying to view it as separate heads and head dimensions doesn't work. So the hook receives the tensor directly from `nn.Linear`, not a tuple—`output` is already the tensor with shape `(1, 33, 3584)`, and indexing it with `[0]` just grabs the first batch element, giving `(33, 3584)`. I need to fix the hook to work with the tensor directly instead of treating it like a tuple.

Writing the corrected hook...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "3decc5f6-3f87-4a5f-bf04-a1bbf280e859",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hz6CyjwX43P1dy62RkU5sU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 664,
      "cache_read_input_tokens": 31044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 664
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

### Assistant

_source line 20_

`o_proj` 是 `nn.Linear`，hook 的 output 是 tensor 而非 tuple。修复脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "91b67fca-03b0-44a0-974c-dea1b4a99b3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hz6CyjwX43P1dy62RkU5sU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 664,
      "cache_read_input_tokens": 31044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 664
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

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01PWpnPGDEBWBgBxYHuVam5K`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "cat > /root/autodl-tmp/pacs/importance_vs_random.py << 'SCRIPT_EOF'\n\"\"\"\nCompare importance-based vs random head masking + KV eviction.\nTests on 5 MATH problems at sparsity 10%, 20%, 30%.\n\"\"\"\nimport torch\nimport json\nimport os\nimport numpy as np\n\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"1\"\n\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\ndef compute_ppl(model, input_ids, labels):\n    with torch.no_grad():\n        out = model(input_ids=input_ids, labels=labels)\n        return torch.exp(out.loss).item()\n\ndef importance_based_head_mask(model, input_ids, num_heads, ratio, num_kv_heads=4):\n    calib_ids = input_ids[:, :128] if input_ids.shape[1] > 128 else input_ids\n    with torch.no_grad():\n        out = model(calib_ids, output_attentions=True)\n    \n    head_importance = torch.zeros(num_heads)\n    n_layers = len(out.attentions)\n    for layer_attn in out.attentions:\n        per_head_norm = layer_attn[0].float().norm(dim=(-2, -1))\n        head_importance += per_head_norm.cpu()\n    head_importance /= n_layers\n    \n    n_mask = int(num_heads * ratio)\n    _, least_important = torch.topk(head_importance, n_mask, largest=False)\n    mask = torch.ones(num_heads, dtype=torch.bool)\n    mask[least_important] = False\n    return mask\n\ndef random_head_mask(num_heads, ratio, seed=42):\n    torch.manual_seed(seed)\n    n_mask = int(num_heads * ratio)\n    perm = torch.randperm(num_heads)\n    mask = torch.ones(num_heads, dtype=torch.bool)\n    mask[perm[:n_mask]] = False\n    return mask\n\ndef importance_based_kv_mask(model, input_ids, seq_len, ratio):\n    calib_ids = input_ids[:, :128] if input_ids.shape[1] > 128 else input_ids\n    calib_len = calib_ids.shape[1]\n    with torch.no_grad():\n        out = model(calib_ids, output_attentions=True)\n    \n    pos_importance = torch.zeros(seq_len)\n    n_layers = len(out.attentions)\n    for layer_attn in out.attentions:\n        avg_attn = layer_attn[0].float().mean(dim=0)\n        attn_sum = avg_attn.sum(dim=0).cpu()\n        pos_importance[:calib_len] += attn_sum\n    pos_importance /= n_layers\n    \n    n_evict = int(seq_len * ratio)\n    pos_importance[0] = float('inf')\n    _, least_important = torch.topk(pos_importance, n_evict, largest=False)\n    mask = torch.ones(seq_len, dtype=torch.bool)\n    mask[least_important] = False\n    return mask\n\ndef random_kv_mask(seq_len, ratio, seed=42):\n    torch.manual_seed(seed)\n    n_evict = int(seq_len * ratio)\n    candidates = torch.arange(1, seq_len)\n    perm = candidates[torch.randperm(len(candidates))]\n    evict_indices = perm[:n_evict]\n    mask = torch.ones(seq_len, dtype=torch.bool)\n    mask[evict_indices] = False\n    return mask\n\ndef apply_head_mask_hook(model, head_mask):\n    handles = []\n    num_heads = len(head_mask)\n    \n    for layer in model.model.layers:\n        attn = layer.self_attn\n        def make_hook(mask):\n            def hook(module, input, output):\n                # o_proj is nn.Linear, output is tensor (batch, seq, hidden_dim)\n                hidden = output\n                head_dim = hidden.shape[-1] // num_heads\n                h = hidden.view(hidden.shape[0], hidden.shape[1], num_heads, head_dim)\n                h[:, :, ~mask, :] = 0\n                return h.view_as(hidden)\n            return hook\n        handles.append(attn.o_proj.register_forward_hook(make_hook(head_mask)))\n    return handles\n\ndef apply_kv_mask(model, input_ids, kv_mask):\n    seq_len = input_ids.shape[1]\n    attn_mask = torch.zeros(1, 1, seq_len, seq_len, device=input_ids.device, dtype=torch.float16)\n    causal = torch.triu(torch.ones(seq_len, seq_len, device=input_ids.device), diagonal=1).bool()\n    attn_mask.masked_fill_(causal.unsqueeze(0).unsqueeze(0), float('-inf'))\n    evicted = ~kv_mask.to(input_ids.device)\n    attn_mask[:, :, :, evicted] = float('-inf')\n    return attn_mask\n\ndef main():\n    model_path = \"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\"\n    \n    print(\"Loading model...\")\n    tokenizer = AutoTokenizer.from_pretrained(model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path, torch_dtype=torch.float16, device_map=\"cuda:0\",\n        attn_implementation=\"eager\",\n    )\n    model.eval()\n    \n    num_heads = model.config.num_attention_heads\n    num_kv_heads = model.config.num_key_value_heads\n    print(f\"Heads: {num_heads}, KV heads: {num_kv_heads}\")\n    \n    prompts = [\n        \"Solve step by step: What is the remainder when 2^100 is divided by 7?\\nSolution: Let me think through this systematically.\",\n        \"Solve step by step: If f(x) = x^2 + 3x - 5, find f(f(2)).\\nSolution: First I need to find f(2), then apply f again.\",\n        \"Solve step by step: A circle has center (3, 4) and passes through the origin. What is its radius?\\nSolution: The radius equals the distance from center to origin.\",\n        \"Solve step by step: How many ways can you arrange the letters in MISSISSIPPI?\\nSolution: This is a permutation with repeated elements.\",\n        \"Solve step by step: Find the sum of the first 20 terms of the arithmetic sequence 3, 7, 11, 15, ...\\nSolution: The common difference is 4.\",\n    ]\n    \n    ratios = [0.1, 0.2, 0.3]\n    results = []\n    \n    for i, prompt in enumerate(prompts):\n        print(f\"\\n=== Problem {i+1} ===\")\n        inputs = tokenizer(prompt, return_tensors=\"pt\").to(\"cuda:0\")\n        input_ids = inputs[\"input_ids\"]\n        seq_len = input_ids.shape[1]\n        print(f\"Seq len: {seq_len}\")\n        \n        dense_ppl = compute_ppl(model, input_ids, input_ids)\n        print(f\"Dense PPL: {dense_ppl:.2f}\")\n        \n        for ratio in ratios:\n            print(f\"\\n  --- Sparsity {ratio} ---\")\n            \n            imp_hmask = importance_based_head_mask(model, input_ids, num_heads, ratio, num_kv_heads)\n            rnd_hmask = random_head_mask(num_heads, ratio)\n            \n            imp_kvmask = importance_based_kv_mask(model, input_ids, seq_len, ratio)\n            rnd_kvmask = random_kv_mask(seq_len, ratio)\n            \n            for method, hmask, kvmask in [\n                (\"importance\", imp_hmask, imp_kvmask),\n                (\"random\", rnd_hmask, rnd_kvmask),\n            ]:\n                # Head-only\n                hooks = apply_head_mask_hook(model, hmask.to(\"cuda:0\"))\n                head_ppl = compute_ppl(model, input_ids, input_ids)\n                for h in hooks: h.remove()\n                \n                # KV-only\n                kv_attn_mask = apply_kv_mask(model, input_ids, kvmask)\n                with torch.no_grad():\n                    out = model(input_ids=input_ids, attention_mask=kv_attn_mask, labels=input_ids)\n                    kv_ppl = torch.exp(out.loss).item()\n                \n                # Compound (head + KV)\n                hooks = apply_head_mask_hook(model, hmask.to(\"cuda:0\"))\n                with torch.no_grad():\n                    out = model(input_ids=input_ids, attention_mask=kv_attn_mask, labels=input_ids)\n                    both_ppl = torch.exp(out.loss).item()\n                for h in hooks: h.remove()\n                \n                print(f\"  {method}: head={head_ppl:.2f} ({head_ppl/dense_ppl:.2f}x), \"\n                      f\"kv={kv_ppl:.2f} ({kv_ppl/dense_ppl:.2f}x), \"\n                      f\"both={both_ppl:.2f} ({both_ppl/dense_ppl:.2f}x)\")\n                \n                results.append({\n                    \"problem\": i,\n                    \"seq_len\": seq_len,\n                    \"ratio\": ratio,\n                    \"method\": method,\n                    \"dense_ppl\": dense_ppl,\n                    \"head_ppl\": head_ppl,\n                    \"kv_ppl\": kv_ppl,\n                    \"both_ppl\": both_ppl,\n                    \"head_degradation\": head_ppl / dense_ppl,\n                    \"kv_degradation\": kv_ppl / dense_ppl,\n                    \"both_degradation\": both_ppl / dense_ppl,\n                })\n    \n    print(\"\\n\" + \"=\"*80)\n    print(\"SUMMARY: Average degradation ratios\")\n    print(\"=\"*80)\n    for ratio in ratios:\n        for method in [\"importance\", \"random\"]:\n            subset = [r for r in results if r[\"ratio\"] == ratio and r[\"method\"] == method]\n            avg_head = np.mean([r[\"head_degradation\"] for r in subset])\n            avg_kv = np.mean([r[\"kv_degradation\"] for r in subset])\n            avg_both = np.mean([r[\"both_degradation\"] for r in subset])\n            print(f\"  {method} @ {ratio}: head={avg_head:.2f}x, kv={avg_kv:.2f}x, both={avg_both:.2f}x\")\n    \n    with open(\"/root/autodl-tmp/pacs/importance_vs_random_results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(\"\\nResults saved.\")\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"SCRIPT_WRITTEN\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "57eba888-b55c-4396-ae40-5ded067fa4d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hz6CyjwX43P1dy62RkU5sU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 664,
      "cache_read_input_tokens": 31044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 664
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

_source line 22 · 2026-05-13T22:23:22.912Z_

<details><summary>↩ Tool result · `toolu_01PWpnPGDEBWBgBxYHuVam5K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"SCRIPT_WRITTEN\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "c6bfee48-429c-4920-8f2f-6d8cc3a620dd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"SCRIPT_WRITTEN\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"SCRIPT_WRITTEN\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Nc1qYBiC2vPmWioeJDYgmx`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "kill 18395 2>/dev/null; cd /root/autodl-tmp && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python pacs/importance_vs_random.py' > /tmp/imp_vs_rnd.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "de76ca76-41c3-4e56-bd3d-e5e2fc0764a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AnrhjDQxmphyMUAbo9BgD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4162,
      "cache_read_input_tokens": 31708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4162
      },
      "output_tokens": 41,
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

_source line 24 · 2026-05-13T22:23:40.132Z_

<details><summary>↩ Tool result · `toolu_01Nc1qYBiC2vPmWioeJDYgmx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=18701\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.85}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "701c9246-4205-4568-be1e-166ca37aaf99",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"PID=18701\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 12.85}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"PID=18701\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.85}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

重新启动 PID=18701。等模型加载完后检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "7a0bdac4-d1c7-4967-bdb9-3ca32b99d396",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ve1tavwJF5ZXWZeKhMPHXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 35870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
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

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PW9z8tak9ngoC1AMRhm7dr`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "tail -30 /tmp/imp_vs_rnd.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "d7fa6e9e-19c7-4b1c-9a3e-40c92fd86cc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ve1tavwJF5ZXWZeKhMPHXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 35870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
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

_source line 27 · 2026-05-13T22:23:46.543Z_

<details><summary>↩ Tool result · `toolu_01PW9z8tak9ngoC1AMRhm7dr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n\\n=== Problem 5 ===\\nSeq len: 45\\nDense PPL: nan\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n\\n================================================================================\\nSUMMARY: Average degradation ratios\\n================================================================================\\n  importance @ 0.1: head=nanx, kv=nanx, both=nanx\\n  random @ 0.1: head=nanx, kv=nanx, both=nanx\\n  importance @ 0.2: head=nanx, kv=nanx, both=nanx\\n  random @ 0.2: head=nanx, kv=nanx, both=nanx\\n  importance @ 0.3: head=nanx, kv=nanx, both=nanx\\n  random @ 0.3: head=nanx, kv=nanx, both=nanx\\n\\nResults saved.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "95bd44f8-ecbb-493d-8833-1391e1963673",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\\\n\\\\n=== Problem 5 ===\\\\nSeq len: 45\\\\nDense PPL: nan\\\\n\\\\n  --- Sparsity 0.1 ---\\\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\\\n\\\\n  --- Sparsity 0.2 ---\\\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\\\n\\\\n  --- Sparsity 0.3 ---\\\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\\\n\\\\n================================================================================\\\\nSUMMARY: Average degradation ratios\\\\n================================================================================\\\\n  importance @ 0.1: head=nanx, kv=nanx, both=nanx\\\\n  random @ 0.1: head=nanx, kv=nanx, both=nanx\\\\n  importance @ 0.2: head=nanx, kv=nanx, both=nanx\\\\n  random @ 0.2: head=nanx, kv=nanx, both=nanx\\\\n  importance @ 0.3: head=nanx, kv=nanx, both=nanx\\\\n  random @ 0.3: head=nanx, kv=nanx, both=nanx\\\\n\\\\nResults saved.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n\\n=== Problem 5 ===\\nSeq len: 45\\nDense PPL: nan\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n  random: head=nan (nanx), kv=nan (nanx), both=nan (nanx)\\n\\n================================================================================\\nSUMMARY: Average degradation ratios\\n================================================================================\\n  importance @ 0.1: head=nanx, kv=nanx, both=nanx\\n  random @ 0.1: head=nanx, kv=nanx, both=nanx\\n  importance @ 0.2: head=nanx, kv=nanx, both=nanx\\n  random @ 0.2: head=nanx, kv=nanx, both=nanx\\n  importance @ 0.3: head=nanx, kv=nanx, both=nanx\\n  random @ 0.3: head=nanx, kv=nanx, both=nanx\\n\\nResults saved.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
All values are nan. This is likely because the loss is nan, probably due to the 4D attention mask format being incompatible with how the model processes it. The model might be expecting a 2D attention mask (batch, seq_len) rather than a 4D one. Also, the dense PPL is nan, which means even the basic `compute_ppl` is returning nan.

Wait, even the dense PPL is nan? Let me check - the dense_ppl computation doesn't use any mask. It's just `model(input_ids=input_ids, labels=labels)`. If that's nan, there's a fundamental issue.
 
Actually, I'm wondering if using `input_ids` directly as `labels` is the culprit here - the model shifts labels internally by 1, but that shouldn't break the loss computation. Could this be an fp16 precision issue? If the loss gets very large, `torch.exp(loss)` would overflow to infinity rather than nan. The nan might actually be coming from the attention mask with -inf values in fp16 precision causing numerical instability.

But wait, the dense baseline doesn't use a mask and it's also producing nan, so the problem must be in the core perplexity calculation itself. The model's loss output might already be nan, which could happen if certain positions have such poor predictions that cross-entropy loss overflows in fp16. I should modify the script to use float32 for loss computation, inspect the actual loss values, and check whether HuggingFace models handle loss computation in float32 internally regardless of the model's dtype. the model is in fp16. The `out.loss` should already be float32. Let me check if the issue is something else.

Could the issue be that `input_ids` used as both input and labels creates a problem? No, that's standard for computing PPL.

Let me add some debugging to the script: print out.loss directly, check if it's nan or inf. Also let me try with `torch.float32` model or with `output_hidden_states=True` to debug.

Actually, let me think about this differently. Maybe the issue is that the tokenizer adds special tokens and the first token has no valid label, making the loss weird? No, that's handled by the shift internally.

Let me just add debugging and re-run with float32 loss handling.

Actually, I wonder if the issue is simpler: maybe `out.loss` is None because the labels need to be passed differently? No, passing `labels=input_ids` should work.

Let me add a debug line to print `out.loss` and see what happens. The fact that all 5 problems are returning nan is really suspicious—something fundamental is broken here. Let me reconsider the setup: the model is on `cuda:0` with `CUDA_VISIBLE_DEVICES=1`, which should map correctly to the physical GPU. But I'm wondering if `attn_implementation="eager"` might be causing numerical instability in fp16, so let me try switching to `bfloat16` or wrapping the forward pass with `torch.autocast`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "b19728b0-6c30-42bf-b44e-be7c70442014",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Au4LuCH7byWo9VKe6PBXBV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 36147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 683
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

_source line 29_

全部 nan，连 dense baseline 都是。可能是 fp16 数值溢出问题。用 bf16 并加调试。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "540b8463-10ee-4713-8543-9c9983709188",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Au4LuCH7byWo9VKe6PBXBV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 36147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 683
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

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01NqWHzBC6gz8JKatp1AfcQ4`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "cat > /root/autodl-tmp/pacs/importance_vs_random.py << 'SCRIPT_EOF'\n\"\"\"\nCompare importance-based vs random head masking + KV eviction.\nTests on 5 MATH problems at sparsity 10%, 20%, 30%.\n\"\"\"\nimport torch\nimport json\nimport os\nimport numpy as np\n\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"1\"\n\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\ndef compute_ppl(model, input_ids):\n    with torch.no_grad():\n        out = model(input_ids=input_ids, labels=input_ids)\n        loss = out.loss.float()\n        return torch.exp(loss).item()\n\ndef compute_ppl_with_mask(model, input_ids, attn_mask=None):\n    with torch.no_grad():\n        out = model(input_ids=input_ids, attention_mask=attn_mask, labels=input_ids)\n        loss = out.loss.float()\n        return torch.exp(loss).item()\n\ndef importance_based_head_mask(model, input_ids, num_heads, ratio):\n    calib_ids = input_ids[:, :128] if input_ids.shape[1] > 128 else input_ids\n    with torch.no_grad():\n        out = model(calib_ids, output_attentions=True)\n    \n    head_importance = torch.zeros(num_heads)\n    n_layers = len(out.attentions)\n    for layer_attn in out.attentions:\n        per_head_norm = layer_attn[0].float().norm(dim=(-2, -1))\n        head_importance += per_head_norm.cpu()\n    head_importance /= n_layers\n    \n    n_mask = int(num_heads * ratio)\n    if n_mask == 0:\n        return torch.ones(num_heads, dtype=torch.bool)\n    _, least_important = torch.topk(head_importance, n_mask, largest=False)\n    mask = torch.ones(num_heads, dtype=torch.bool)\n    mask[least_important] = False\n    return mask\n\ndef random_head_mask(num_heads, ratio, seed=42):\n    torch.manual_seed(seed)\n    n_mask = int(num_heads * ratio)\n    if n_mask == 0:\n        return torch.ones(num_heads, dtype=torch.bool)\n    perm = torch.randperm(num_heads)\n    mask = torch.ones(num_heads, dtype=torch.bool)\n    mask[perm[:n_mask]] = False\n    return mask\n\ndef importance_based_kv_mask(model, input_ids, seq_len, ratio):\n    calib_ids = input_ids[:, :128] if input_ids.shape[1] > 128 else input_ids\n    calib_len = calib_ids.shape[1]\n    with torch.no_grad():\n        out = model(calib_ids, output_attentions=True)\n    \n    pos_importance = torch.zeros(seq_len)\n    n_layers = len(out.attentions)\n    for layer_attn in out.attentions:\n        avg_attn = layer_attn[0].float().mean(dim=0)\n        attn_sum = avg_attn.sum(dim=0).cpu()\n        pos_importance[:calib_len] += attn_sum\n    pos_importance /= n_layers\n    \n    n_evict = int(seq_len * ratio)\n    if n_evict == 0:\n        return torch.ones(seq_len, dtype=torch.bool)\n    pos_importance[0] = float('inf')\n    _, least_important = torch.topk(pos_importance, n_evict, largest=False)\n    mask = torch.ones(seq_len, dtype=torch.bool)\n    mask[least_important] = False\n    return mask\n\ndef random_kv_mask(seq_len, ratio, seed=42):\n    torch.manual_seed(seed)\n    n_evict = int(seq_len * ratio)\n    if n_evict == 0:\n        return torch.ones(seq_len, dtype=torch.bool)\n    candidates = torch.arange(1, seq_len)\n    perm = candidates[torch.randperm(len(candidates))]\n    evict_indices = perm[:n_evict]\n    mask = torch.ones(seq_len, dtype=torch.bool)\n    mask[evict_indices] = False\n    return mask\n\ndef apply_head_mask_hook(model, head_mask):\n    handles = []\n    num_heads = len(head_mask)\n    \n    for layer in model.model.layers:\n        attn = layer.self_attn\n        def make_hook(mask):\n            def hook(module, input, output):\n                hidden = output  # (batch, seq, hidden_dim) from nn.Linear\n                head_dim = hidden.shape[-1] // num_heads\n                h = hidden.view(hidden.shape[0], hidden.shape[1], num_heads, head_dim)\n                h[:, :, ~mask, :] = 0\n                return h.view_as(hidden)\n            return hook\n        handles.append(attn.o_proj.register_forward_hook(make_hook(head_mask)))\n    return handles\n\ndef build_kv_attn_mask(input_ids, kv_mask):\n    seq_len = input_ids.shape[1]\n    dtype = torch.bfloat16\n    attn_mask = torch.zeros(1, 1, seq_len, seq_len, device=input_ids.device, dtype=dtype)\n    causal = torch.triu(torch.ones(seq_len, seq_len, device=input_ids.device, dtype=torch.bool), diagonal=1)\n    attn_mask.masked_fill_(causal.unsqueeze(0).unsqueeze(0), torch.finfo(dtype).min)\n    evicted = ~kv_mask.to(input_ids.device)\n    attn_mask[:, :, :, evicted] = torch.finfo(dtype).min\n    return attn_mask\n\ndef main():\n    model_path = \"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\"\n    \n    print(\"Loading model...\")\n    tokenizer = AutoTokenizer.from_pretrained(model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path, torch_dtype=torch.bfloat16, device_map=\"cuda:0\",\n        attn_implementation=\"eager\",\n    )\n    model.eval()\n    \n    num_heads = model.config.num_attention_heads\n    num_kv_heads = model.config.num_key_value_heads\n    print(f\"Heads: {num_heads}, KV heads: {num_kv_heads}\")\n    \n    # Quick sanity check\n    test_input = tokenizer(\"Hello world\", return_tensors=\"pt\").to(\"cuda:0\")\n    with torch.no_grad():\n        out = model(input_ids=test_input[\"input_ids\"], labels=test_input[\"input_ids\"])\n        print(f\"Sanity check - loss: {out.loss.item():.4f}, ppl: {torch.exp(out.loss.float()).item():.2f}\")\n    \n    prompts = [\n        \"Solve step by step: What is the remainder when 2^100 is divided by 7?\\nSolution: Let me think through this systematically.\",\n        \"Solve step by step: If f(x) = x^2 + 3x - 5, find f(f(2)).\\nSolution: First I need to find f(2), then apply f again.\",\n        \"Solve step by step: A circle has center (3, 4) and passes through the origin. What is its radius?\\nSolution: The radius equals the distance from center to origin.\",\n        \"Solve step by step: How many ways can you arrange the letters in MISSISSIPPI?\\nSolution: This is a permutation with repeated elements.\",\n        \"Solve step by step: Find the sum of the first 20 terms of the arithmetic sequence 3, 7, 11, 15, ...\\nSolution: The common difference is 4.\",\n    ]\n    \n    ratios = [0.1, 0.2, 0.3]\n    results = []\n    \n    for i, prompt in enumerate(prompts):\n        print(f\"\\n=== Problem {i+1} ===\")\n        inputs = tokenizer(prompt, return_tensors=\"pt\").to(\"cuda:0\")\n        input_ids = inputs[\"input_ids\"]\n        seq_len = input_ids.shape[1]\n        print(f\"Seq len: {seq_len}\")\n        \n        dense_ppl = compute_ppl(model, input_ids)\n        print(f\"Dense PPL: {dense_ppl:.2f}\")\n        \n        for ratio in ratios:\n            print(f\"\\n  --- Sparsity {ratio} ---\")\n            \n            imp_hmask = importance_based_head_mask(model, input_ids, num_heads, ratio)\n            rnd_hmask = random_head_mask(num_heads, ratio)\n            \n            imp_kvmask = importance_based_kv_mask(model, input_ids, seq_len, ratio)\n            rnd_kvmask = random_kv_mask(seq_len, ratio)\n            \n            for method, hmask, kvmask in [\n                (\"importance\", imp_hmask, imp_kvmask),\n                (\"random\", rnd_hmask, rnd_kvmask),\n            ]:\n                # Head-only\n                hooks = apply_head_mask_hook(model, hmask.to(\"cuda:0\"))\n                head_ppl = compute_ppl(model, input_ids)\n                for h in hooks: h.remove()\n                \n                # KV-only\n                kv_attn_mask = build_kv_attn_mask(input_ids, kvmask)\n                kv_ppl = compute_ppl_with_mask(model, input_ids, kv_attn_mask)\n                \n                # Compound (head + KV)\n                hooks = apply_head_mask_hook(model, hmask.to(\"cuda:0\"))\n                both_ppl = compute_ppl_with_mask(model, input_ids, kv_attn_mask)\n                for h in hooks: h.remove()\n                \n                print(f\"  {method}: head={head_ppl:.2f} ({head_ppl/dense_ppl:.2f}x), \"\n                      f\"kv={kv_ppl:.2f} ({kv_ppl/dense_ppl:.2f}x), \"\n                      f\"both={both_ppl:.2f} ({both_ppl/dense_ppl:.2f}x)\")\n                \n                results.append({\n                    \"problem\": i,\n                    \"seq_len\": seq_len,\n                    \"ratio\": ratio,\n                    \"method\": method,\n                    \"dense_ppl\": dense_ppl,\n                    \"head_ppl\": head_ppl,\n                    \"kv_ppl\": kv_ppl,\n                    \"both_ppl\": both_ppl,\n                    \"head_degradation\": head_ppl / dense_ppl,\n                    \"kv_degradation\": kv_ppl / dense_ppl,\n                    \"both_degradation\": both_ppl / dense_ppl,\n                })\n    \n    print(\"\\n\" + \"=\"*80)\n    print(\"SUMMARY: Average degradation ratios\")\n    print(\"=\"*80)\n    for ratio in ratios:\n        for method in [\"importance\", \"random\"]:\n            subset = [r for r in results if r[\"ratio\"] == ratio and r[\"method\"] == method]\n            avg_head = np.mean([r[\"head_degradation\"] for r in subset])\n            avg_kv = np.mean([r[\"kv_degradation\"] for r in subset])\n            avg_both = np.mean([r[\"both_degradation\"] for r in subset])\n            print(f\"  {method} @ {ratio}: head={avg_head:.2f}x, kv={avg_kv:.2f}x, both={avg_both:.2f}x\")\n    \n    with open(\"/root/autodl-tmp/pacs/importance_vs_random_results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(\"\\nResults saved.\")\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "4c4f14ab-6196-4d99-a816-81dc2876ae49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Au4LuCH7byWo9VKe6PBXBV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 36147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 683
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

_source line 31 · 2026-05-13T22:24:53.691Z_

<details><summary>↩ Tool result · `toolu_01NqWHzBC6gz8JKatp1AfcQ4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "26559ab7-a008-44e0-8237-41de58638f45",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

主要改动：bf16 替代 fp16，用 `torch.finfo(dtype).min` 替代 `float('-inf')`，loss 转 float32 再 exp。重新运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "083055c3-1e73-4660-a95b-a7d5ae07847a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NT5F9PtvtFibsNDmrKBe4P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4355,
      "cache_read_input_tokens": 36830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4355
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

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01F7mqmvKs5eDG8rPiGeGwUk`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "cd /root/autodl-tmp && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python pacs/importance_vs_random.py' > /tmp/imp_vs_rnd.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "62ac54af-4c0a-472a-8fca-be2b6198c41f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NT5F9PtvtFibsNDmrKBe4P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4355,
      "cache_read_input_tokens": 36830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4355
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

_source line 34 · 2026-05-13T22:25:14.785Z_

<details><summary>↩ Tool result · `toolu_01F7mqmvKs5eDG8rPiGeGwUk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=19030\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "2fcc0d79-f39f-4d55-999d-f7dcf7735f0b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"PID=19030\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 12.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"PID=19030\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.4}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

PID=19030。等模型加载和 sanity check 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "f0ee1b6f-323e-488b-bafc-dbec0d5c3200",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eXMxijFtQ2h9qRDgRDRsR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 41185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 320
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

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018ZScfLkv4viV54gmQWzQ2b`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "tail -20 /tmp/imp_vs_rnd.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "fb55890c-3a86-4ec2-89af-22d8c1e0667d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eXMxijFtQ2h9qRDgRDRsR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 41185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 320
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

_source line 37 · 2026-05-13T22:25:18.627Z_

<details><summary>↩ Tool result · `toolu_018ZScfLkv4viV54gmQWzQ2b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n  --- Sparsity 0.2 ---\\n  importance: head=11.84 (1.49x), kv=22.56 (2.84x), both=29.02 (3.66x)\\n  random: head=9.92 (1.25x), kv=36.66 (4.62x), both=35.00 (4.41x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=17.33 (2.19x), kv=45.97 (5.80x), both=42.39 (5.34x)\\n  random: head=43.78 (5.52x), kv=116.99 (14.75x), both=155.72 (19.63x)\\n\\n================================================================================\\nSUMMARY: Average degradation ratios\\n================================================================================\\n  importance @ 0.1: head=1.07x, kv=1.46x, both=1.54x\\n  random @ 0.1: head=0.97x, kv=2.20x, both=2.23x\\n  importance @ 0.2: head=1.22x, kv=2.28x, both=2.71x\\n  random @ 0.2: head=1.31x, kv=6.48x, both=7.31x\\n  importance @ 0.3: head=1.47x, kv=5.09x, both=4.65x\\n  random @ 0.3: head=4.02x, kv=13.80x, both=26.20x\\n\\nResults saved.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "da2ea76b-94bc-4a37-803b-911db4d05981",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n  --- Sparsity 0.2 ---\\\\n  importance: head=11.84 (1.49x), kv=22.56 (2.84x), both=29.02 (3.66x)\\\\n  random: head=9.92 (1.25x), kv=36.66 (4.62x), both=35.00 (4.41x)\\\\n\\\\n  --- Sparsity 0.3 ---\\\\n  importance: head=17.33 (2.19x), kv=45.97 (5.80x), both=42.39 (5.34x)\\\\n  random: head=43.78 (5.52x), kv=116.99 (14.75x), both=155.72 (19.63x)\\\\n\\\\n================================================================================\\\\nSUMMARY: Average degradation ratios\\\\n================================================================================\\\\n  importance @ 0.1: head=1.07x, kv=1.46x, both=1.54x\\\\n  random @ 0.1: head=0.97x, kv=2.20x, both=2.23x\\\\n  importance @ 0.2: head=1.22x, kv=2.28x, both=2.71x\\\\n  random @ 0.2: head=1.31x, kv=6.48x, both=7.31x\\\\n  importance @ 0.3: head=1.47x, kv=5.09x, both=4.65x\\\\n  random @ 0.3: head=4.02x, kv=13.80x, both=26.20x\\\\n\\\\nResults saved.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n  --- Sparsity 0.2 ---\\n  importance: head=11.84 (1.49x), kv=22.56 (2.84x), both=29.02 (3.66x)\\n  random: head=9.92 (1.25x), kv=36.66 (4.62x), both=35.00 (4.41x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=17.33 (2.19x), kv=45.97 (5.80x), both=42.39 (5.34x)\\n  random: head=43.78 (5.52x), kv=116.99 (14.75x), both=155.72 (19.63x)\\n\\n================================================================================\\nSUMMARY: Average degradation ratios\\n================================================================================\\n  importance @ 0.1: head=1.07x, kv=1.46x, both=1.54x\\n  random @ 0.1: head=0.97x, kv=2.20x, both=2.23x\\n  importance @ 0.2: head=1.22x, kv=2.28x, both=2.71x\\n  random @ 0.2: head=1.31x, kv=6.48x, both=7.31x\\n  importance @ 0.3: head=1.47x, kv=5.09x, both=4.65x\\n  random @ 0.3: head=4.02x, kv=13.80x, both=26.20x\\n\\nResults saved.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

实验完成。看完整输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "00d3f5e7-3bca-4b7d-b1b2-d94545d59a76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHBciwRvN1oT3aUhJfWM6F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 41505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
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

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017vUGy35Cs7e7eYJ5He9gJe`</summary>

```json
{
  "server": "westd-22162",
  "account": "root",
  "command": "cat /tmp/imp_vs_rnd.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "578e490b-5fb7-4bd7-b08d-4260eb64f248",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHBciwRvN1oT3aUhJfWM6F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 41505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
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

_source line 40 · 2026-05-13T22:25:21.661Z_

<details><summary>↩ Tool result · `toolu_017vUGy35Cs7e7eYJ5He9gJe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\nLoading model...\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:02<00:02,  2.36s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:04<00:00,  2.06s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:04<00:00,  2.11s/it]\\nHeads: 28, KV heads: 4\\nSanity check - loss: 11.1358, ppl: 68586.43\\n\\n=== Problem 1 ===\\nSeq len: 33\\nDense PPL: 26.94\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=24.73 (0.92x), kv=32.19 (1.19x), both=32.02 (1.19x)\\n  random: head=23.50 (0.87x), kv=57.08 (2.12x), both=71.81 (2.67x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=36.18 (1.34x), kv=46.21 (1.72x), both=61.36 (2.28x)\\n  random: head=23.61 (0.88x), kv=97.83 (3.63x), both=93.28 (3.46x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=29.69 (1.10x), kv=142.87 (5.30x), both=106.87 (3.97x)\\n  random: head=82.73 (3.07x), kv=133.26 (4.95x), both=395.15 (14.67x)\\n\\n=== Problem 2 ===\\nSeq len: 45\\nDense PPL: 10.84\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=11.23 (1.04x), kv=11.86 (1.09x), both=13.60 (1.25x)\\n  random: head=12.16 (1.12x), kv=27.30 (2.52x), both=22.22 (2.05x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=13.30 (1.23x), kv=21.96 (2.03x), both=30.85 (2.85x)\\n  random: head=21.14 (1.95x), kv=65.78 (6.07x), both=62.66 (5.78x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=13.04 (1.20x), kv=31.78 (2.93x), both=40.99 (3.78x)\\n  random: head=45.59 (4.21x), kv=159.44 (14.71x), both=304.92 (28.13x)\\n\\n=== Problem 3 ===\\nSeq len: 40\\nDense PPL: 16.25\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=14.86 (0.91x), kv=18.31 (1.13x), both=17.96 (1.11x)\\n  random: head=16.39 (1.01x), kv=30.11 (1.85x), both=34.25 (2.11x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=14.56 (0.90x), kv=38.08 (2.34x), both=35.45 (2.18x)\\n  random: head=17.05 (1.05x), kv=102.11 (6.28x), both=133.10 (8.19x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=15.59 (0.96x), kv=91.85 (5.65x), both=67.61 (4.16x)\\n  random: head=44.23 (2.72x), kv=125.14 (7.70x), both=267.66 (16.47x)\\n\\n=== Problem 4 ===\\nSeq len: 31\\nDense PPL: 32.85\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=40.91 (1.25x), kv=87.65 (2.67x), both=86.92 (2.65x)\\n  random: head=30.48 (0.93x), kv=72.46 (2.21x), both=85.07 (2.59x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=37.26 (1.13x), kv=80.88 (2.46x), both=85.04 (2.59x)\\n  random: head=46.06 (1.40x), kv=386.64 (11.77x), both=482.30 (14.68x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=61.83 (1.88x), kv=190.11 (5.79x), both=196.71 (5.99x)\\n  random: head=150.05 (4.57x), kv=883.27 (26.89x), both=1712.02 (52.12x)\\n\\n=== Problem 5 ===\\nSeq len: 45\\nDense PPL: 7.93\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=9.90 (1.25x), kv=9.77 (1.23x), both=12.07 (1.52x)\\n  random: head=7.11 (0.90x), kv=18.39 (2.32x), both=13.93 (1.76x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=11.84 (1.49x), kv=22.56 (2.84x), both=29.02 (3.66x)\\n  random: head=9.92 (1.25x), kv=36.66 (4.62x), both=35.00 (4.41x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=17.33 (2.19x), kv=45.97 (5.80x), both=42.39 (5.34x)\\n  random: head=43.78 (5.52x), kv=116.99 (14.75x), both=155.72 (19.63x)\\n\\n================================================================================\\nSUMMARY: Average degradation ratios\\n================================================================================\\n  importance @ 0.1: head=1.07x, kv=1.46x, both=1.54x\\n  random @ 0.1: head=0.97x, kv=2.20x, both=2.23x\\n  importance @ 0.2: head=1.22x, kv=2.28x, both=2.71x\\n  random @ 0.2: head=1.31x, kv=6.48x, both=7.31x\\n  importance @ 0.3: head=1.47x, kv=5.09x, both=4.65x\\n  random @ 0.3: head=4.02x, kv=13.80x, both=26.20x\\n\\nResults saved.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "d8d29ef5-dd3f-4fd8-8a9a-ae3f5aaefcaf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"`torch_dtype` is deprecated! Use `dtype` instead!\\\\nLoading model...\\\\n\\\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:02<00:02,  2.36s/it]\\\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:04<00:00,  2.06s/it]\\\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:04<00:00,  2.11s/it]\\\\nHeads: 28, KV heads: 4\\\\nSanity check - loss: 11.1358, ppl: 68586.43\\\\n\\\\n=== Problem 1 ===\\\\nSeq len: 33\\\\nDense PPL: 26.94\\\\n\\\\n  --- Sparsity 0.1 ---\\\\n  importance: head=24.73 (0.92x), kv=32.19 (1.19x), both=32.02 (1.19x)\\\\n  random: head=23.50 (0.87x), kv=57.08 (2.12x), both=71.81 (2.67x)\\\\n\\\\n  --- Sparsity 0.2 ---\\\\n  importance: head=36.18 (1.34x), kv=46.21 (1.72x), both=61.36 (2.28x)\\\\n  random: head=23.61 (0.88x), kv=97.83 (3.63x), both=93.28 (3.46x)\\\\n\\\\n  --- Sparsity 0.3 ---\\\\n  importance: head=29.69 (1.10x), kv=142.87 (5.30x), both=106.87 (3.97x)\\\\n  random: head=82.73 (3.07x), kv=133.26 (4.95x), both=395.15 (14.67x)\\\\n\\\\n=== Problem 2 ===\\\\nSeq len: 45\\\\nDense PPL: 10.84\\\\n\\\\n  --- Sparsity 0.1 ---\\\\n  importance: head=11.23 (1.04x), kv=11.86 (1.09x), both=13.60 (1.25x)\\\\n  random: head=12.16 (1.12x), kv=27.30 (2.52x), both=22.22 (2.05x)\\\\n\\\\n  --- Sparsity 0.2 ---\\\\n  importance: head=13.30 (1.23x), kv=21.96 (2.03x), both=30.85 (2.85x)\\\\n  random: head=21.14 (1.95x), kv=65.78 (6.07x), both=62.66 (5.78x)\\\\n\\\\n  --- Sparsity 0.3 ---\\\\n  importance: head=13.04 (1.20x), kv=31.78 (2.93x), both=40.99 (3.78x)\\\\n  random: head=45.59 (4.21x), kv=159.44 (14.71x), both=304.92 (28.13x)\\\\n\\\\n=== Problem 3 ===\\\\nSeq len: 40\\\\nDense PPL: 16.25\\\\n\\\\n  --- Sparsity 0.1 ---\\\\n  importance: head=14.86 (0.91x), kv=18.31 (1.13x), both=17.96 (1.11x)\\\\n  random: head=16.39 (1.01x), kv=30.11 (1.85x), both=34.25 (2.11x)\\\\n\\\\n  --- Sparsity 0.2 ---\\\\n  importance: head=14.56 (0.90x), kv=38.08 (2.34x), both=35.45 (2.18x)\\\\n  random: head=17.05 (1.05x), kv=102.11 (6.28x), both=133.10 (8.19x)\\\\n\\\\n  --- Sparsity 0.3 ---\\\\n  importance: head=15.59 (0.96x), kv=91.85 (5.65x), both=67.61 (4.16x)\\\\n  random: head=44.23 (2.72x), kv=125.14 (7.70x), both=267.66 (16.47x)\\\\n\\\\n=== Problem 4 ===\\\\nSeq len: 31\\\\nDense PPL: 32.85\\\\n\\\\n  --- Sparsity 0.1 ---\\\\n  importance: head=40.91 (1.25x), kv=87.65 (2.67x), both=86.92 (2.65x)\\\\n  random: head=30.48 (0.93x), kv=72.46 (2.21x), both=85.07 (2.59x)\\\\n\\\\n  --- Sparsity 0.2 ---\\\\n  importance: head=37.26 (1.13x), kv=80.88 (2.46x), both=85.04 (2.59x)\\\\n  random: head=46.06 (1.40x), kv=386.64 (11.77x), both=482.30 (14.68x)\\\\n\\\\n  --- Sparsity 0.3 ---\\\\n  importance: head=61.83 (1.88x), kv=190.11 (5.79x), both=196.71 (5.99x)\\\\n  random: head=150.05 (4.57x), kv=883.27 (26.89x), both=1712.02 (52.12x)\\\\n\\\\n=== Problem 5 ===\\\\nSeq len: 45\\\\nDense PPL: 7.93\\\\n\\\\n  --- Sparsity 0.1 ---\\\\n  importance: head=9.90 (1.25x), kv=9.77 (1.23x), both=12.07 (1.52x)\\\\n  random: head=7.11 (0.90x), kv=18.39 (2.32x), both=13.93 (1.76x)\\\\n\\\\n  --- Sparsity 0.2 ---\\\\n  importance: head=11.84 (1.49x), kv=22.56 (2.84x), both=29.02 (3.66x)\\\\n  random: head=9.92 (1.25x), kv=36.66 (4.62x), both=35.00 (4.41x)\\\\n\\\\n  --- Sparsity 0.3 ---\\\\n  importance: head=17.33 (2.19x), kv=45.97 (5.80x), both=42.39 (5.34x)\\\\n  random: head=43.78 (5.52x), kv=116.99 (14.75x), both=155.72 (19.63x)\\\\n\\\\n================================================================================\\\\nSUMMARY: Average degradation ratios\\\\n================================================================================\\\\n  importance @ 0.1: head=1.07x, kv=1.46x, both=1.54x\\\\n  random @ 0.1: head=0.97x, kv=2.20x, both=2.23x\\\\n  importance @ 0.2: head=1.22x, kv=2.28x, both=2.71x\\\\n  random @ 0.2: head=1.31x, kv=6.48x, both=7.31x\\\\n  importance @ 0.3: head=1.47x, kv=5.09x, both=4.65x\\\\n  random @ 0.3: head=4.02x, kv=13.80x, both=26.20x\\\\n\\\\nResults saved.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\nLoading model...\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:02<00:02,  2.36s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:04<00:00,  2.06s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:04<00:00,  2.11s/it]\\nHeads: 28, KV heads: 4\\nSanity check - loss: 11.1358, ppl: 68586.43\\n\\n=== Problem 1 ===\\nSeq len: 33\\nDense PPL: 26.94\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=24.73 (0.92x), kv=32.19 (1.19x), both=32.02 (1.19x)\\n  random: head=23.50 (0.87x), kv=57.08 (2.12x), both=71.81 (2.67x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=36.18 (1.34x), kv=46.21 (1.72x), both=61.36 (2.28x)\\n  random: head=23.61 (0.88x), kv=97.83 (3.63x), both=93.28 (3.46x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=29.69 (1.10x), kv=142.87 (5.30x), both=106.87 (3.97x)\\n  random: head=82.73 (3.07x), kv=133.26 (4.95x), both=395.15 (14.67x)\\n\\n=== Problem 2 ===\\nSeq len: 45\\nDense PPL: 10.84\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=11.23 (1.04x), kv=11.86 (1.09x), both=13.60 (1.25x)\\n  random: head=12.16 (1.12x), kv=27.30 (2.52x), both=22.22 (2.05x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=13.30 (1.23x), kv=21.96 (2.03x), both=30.85 (2.85x)\\n  random: head=21.14 (1.95x), kv=65.78 (6.07x), both=62.66 (5.78x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=13.04 (1.20x), kv=31.78 (2.93x), both=40.99 (3.78x)\\n  random: head=45.59 (4.21x), kv=159.44 (14.71x), both=304.92 (28.13x)\\n\\n=== Problem 3 ===\\nSeq len: 40\\nDense PPL: 16.25\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=14.86 (0.91x), kv=18.31 (1.13x), both=17.96 (1.11x)\\n  random: head=16.39 (1.01x), kv=30.11 (1.85x), both=34.25 (2.11x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=14.56 (0.90x), kv=38.08 (2.34x), both=35.45 (2.18x)\\n  random: head=17.05 (1.05x), kv=102.11 (6.28x), both=133.10 (8.19x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=15.59 (0.96x), kv=91.85 (5.65x), both=67.61 (4.16x)\\n  random: head=44.23 (2.72x), kv=125.14 (7.70x), both=267.66 (16.47x)\\n\\n=== Problem 4 ===\\nSeq len: 31\\nDense PPL: 32.85\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=40.91 (1.25x), kv=87.65 (2.67x), both=86.92 (2.65x)\\n  random: head=30.48 (0.93x), kv=72.46 (2.21x), both=85.07 (2.59x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=37.26 (1.13x), kv=80.88 (2.46x), both=85.04 (2.59x)\\n  random: head=46.06 (1.40x), kv=386.64 (11.77x), both=482.30 (14.68x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=61.83 (1.88x), kv=190.11 (5.79x), both=196.71 (5.99x)\\n  random: head=150.05 (4.57x), kv=883.27 (26.89x), both=1712.02 (52.12x)\\n\\n=== Problem 5 ===\\nSeq len: 45\\nDense PPL: 7.93\\n\\n  --- Sparsity 0.1 ---\\n  importance: head=9.90 (1.25x), kv=9.77 (1.23x), both=12.07 (1.52x)\\n  random: head=7.11 (0.90x), kv=18.39 (2.32x), both=13.93 (1.76x)\\n\\n  --- Sparsity 0.2 ---\\n  importance: head=11.84 (1.49x), kv=22.56 (2.84x), both=29.02 (3.66x)\\n  random: head=9.92 (1.25x), kv=36.66 (4.62x), both=35.00 (4.41x)\\n\\n  --- Sparsity 0.3 ---\\n  importance: head=17.33 (2.19x), kv=45.97 (5.80x), both=42.39 (5.34x)\\n  random: head=43.78 (5.52x), kv=116.99 (14.75x), both=155.72 (19.63x)\\n\\n================================================================================\\nSUMMARY: Average degradation ratios\\n================================================================================\\n  importance @ 0.1: head=1.07x, kv=1.46x, both=1.54x\\n  random @ 0.1: head=0.97x, kv=2.20x, both=2.23x\\n  importance @ 0.2: head=1.22x, kv=2.28x, both=2.71x\\n  random @ 0.2: head=1.31x, kv=6.48x, both=7.31x\\n  importance @ 0.3: head=1.47x, kv=5.09x, both=4.65x\\n  random @ 0.3: head=4.02x, kv=13.80x, both=26.20x\\n\\nResults saved.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

实验完成。结果汇总：

## Importance vs Random Masking PPL 退化对比

| Sparsity | Method | Head-only | KV-only | Compound (Head+KV) |
|----------|--------|-----------|---------|---------------------|
| **10%** | importance | **1.07x** | **1.46x** | **1.54x** |
| 10% | random | 0.97x | 2.20x | 2.23x |
| **20%** | importance | **1.22x** | **2.28x** | **2.71x** |
| 20% | random | 1.31x | 6.48x | 7.31x |
| **30%** | importance | **1.47x** | **5.09x** | **4.65x** |
| 30% | random | 4.02x | 13.80x | **26.20x** |

### 关键发现

1. **Importance-based 显著优于 random**，尤其在高 sparsity 下差距急剧扩大：
   - 30% compound: importance 4.65x vs random **26.20x**（差 5.6 倍）
   - 20% compound: importance 2.71x vs random 7.31x（差 2.7 倍）

2. **KV eviction 是退化主因**，不是 head masking：
   - 30% importance: head 仅 1.47x，KV 达 5.09x
   - Random KV eviction 在 30% 已达 13.80x，是灾难性的

3. **Head masking 本身退化可控**：importance-based 在 30% 仅 1.47x，说明确实有大量冗余 head 可以安全剪掉。Random 在 30% 也才 4.02x，远低于 compound 的 26.20x。

4. **M1v2 的 24-33x 退化主要来自 random KV eviction + compound 叠加效应**，而非 head pruning 本身。Importance-based 选择可以将 30% compound 退化从 26x 降到 4.6x。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "uuid": "aca29353-e774-43cc-a772-4a043b9a2823",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZqj3AMGs9S6yN1Bf74rkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2378,
      "cache_read_input_tokens": 42131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2378
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

_source line 42_

实验完成。结果汇总：

## Importance vs Random Masking PPL 退化对比

| Sparsity | Method | Head-only | KV-only | Compound (Head+KV) |
|----------|--------|-----------|---------|---------------------|
| **10%** | importance | **1.07x** | **1.46x** | **1.54x** |
| 10% | random | 0.97x | 2.20x | 2.23x |
| **20%** | importance | **1.22x** | **2.28x** | **2.71x** |
| 20% | random | 1.31x | 6.48x | 7.31x |
| **30%** | importance | **1.47x** | **5.09x** | **4.65x** |
| 30% | random | 4.02x | 13.80x | **26.20x** |

### 关键发现

1. **Importance-based 显著优于 random**，尤其在高 sparsity 下差距急剧扩大：
   - 30% compound: importance 4.65x vs random **26.20x**（差 5.6 倍）
   - 20% compound: importance 2.71x vs random 7.31x（差 2.7 倍）

2. **KV eviction 是退化主因**，不是 head masking：
   - 30% importance: head 仅 1.47x，KV 达 5.09x
   - Random KV eviction 在 30% 已达 13.80x，是灾难性的

3. **Head masking 本身退化可控**：importance-based 在 30% 仅 1.47x，说明确实有大量冗余 head 可以安全剪掉。Random 在 30% 也才 4.02x，远低于 compound 的 26.20x。

4. **M1v2 的 24-33x 退化主要来自 random KV eviction + compound 叠加效应**，而非 head pruning 本身。Importance-based 选择可以将 30% compound 退化从 26x 降到 4.6x。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 261034,
  "duration_api_ms": 222575,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "c080caa3-7e89-4296-8453-f26bbd71c0a9",
  "total_cost_usd": 0.7543479999999998,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 32668,
    "cache_read_input_tokens": 420554,
    "output_tokens": 13412,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32668,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 585,
        "cache_read_input_tokens": 42131,
        "cache_creation_input_tokens": 2378,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2378
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 4426,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.004511,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 13412,
      "cacheReadInputTokens": 420554,
      "cacheCreationInputTokens": 32668,
      "webSearchRequests": 0,
      "costUSD": 0.7498369999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "eef71bca-f85e-4efb-a776-e4a9c7e41164"
}
```

</details>

---
