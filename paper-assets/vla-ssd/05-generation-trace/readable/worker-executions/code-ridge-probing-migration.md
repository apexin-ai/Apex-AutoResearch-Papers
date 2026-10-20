# code ridge probing migration

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 108
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/workers/worker_code_ridge_probing_migration_20260521T050309.log`
- **Structured JSON:** [`c2ebb376ecf82420e12c.json`](../../sessions/c2/c2ebb376ecf82420e12c.json)

## Before a recorded user message

108 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
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
  "uuid": "5b26a225-1fea-4b50-9da0-00ca85315822",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779355800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "272fd214-264b-473f-a645-da4cc9beccc4",
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by connecting to the server and examining the pipeline scripts to understand their current structure before making modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "3f1cfe32-a5c3-4abf-a416-615da1f2a3d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE5AqKPiK5ezzWFVmi3bWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12725,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12725
      },
      "output_tokens": 24,
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

开始执行。先列出所有需要修改的文件并查看其内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "fb5f4494-232e-4d0b-9d57-4e596690d3f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE5AqKPiK5ezzWFVmi3bWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12725,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12725
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017SbuB8dSDvU2CQC5xmJ7A3`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "51cf0770-27d4-4b03-92b8-f78bbd357800",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE5AqKPiK5ezzWFVmi3bWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12725,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12725
      },
      "output_tokens": 24,
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

_source line 7 · 2026-05-21T05:03:23.712Z_

<details><summary>↩ Tool result · `toolu_017SbuB8dSDvU2CQC5xmJ7A3`</summary>

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
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "d71e5228-5050-4cfc-9f03-c88265e89170",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NCoez3y2MCCCJp2r5fJLuw`</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/scripts/*pipeline*.py /root/autodl-tmp/vla-ssd/scripts/*probing*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "820c160d-8b02-4a97-ab02-b219c96147af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdxEdAZ6ztiWBG5662d7hE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 24566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 934
      },
      "output_tokens": 47,
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

_source line 9 · 2026-05-21T05:03:36.927Z_

<details><summary>↩ Tool result · `toolu_01NCoez3y2MCCCJp2r5fJLuw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "0b9b67fa-ea37-4b97-938a-0908e658f57c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\\\n/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\\\n/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\\\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\\\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\\\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.17}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

7 个文件全部存在。先读取所有文件内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "2dc12be7-e2a0-4b91-b5bf-26bee6e2acdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cz8HUVqfcc5ENLaMfDS4tC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 25500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EEPQYTjijBDPgg2XEst9fc`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "6f16b3fa-3f19-4016-8901-35f4dd19b218",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cz8HUVqfcc5ENLaMfDS4tC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 25500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019iiLVvhnwg8vfsaUZCr48u`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "5f4a3a13-bd64-42b6-a4e4-d0f5b0a04306",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cz8HUVqfcc5ENLaMfDS4tC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 25500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 13 · 2026-05-21T05:03:44.636Z_

<details><summary>↩ Tool result · `toolu_01EEPQYTjijBDPgg2XEst9fc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_object\\\"\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef generate_action(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n    input_ids = inputs[\\\"input_ids\\\"]\\n\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = torch.cat(\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\n        )\\n        if \\\"attention_mask\\\" in inputs:\\n            inputs[\\\"attention_mask\\\"] = torch.cat(\\n                (inputs[\\\"attention_mask\\\"],\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\"attention_mask\\\"].dtype)), dim=1\\n            )\\n    inputs[\\\"input_ids\\\"] = input_ids\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            max_new_tokens=7, do_sample=False,\\n        )\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n\\n    vocab_size = model.vocab_size\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\n    norm_act = model.bin_centers[disc]\\n\\n    stats = mode\\n\\n... [截断: 输出过长，省略 16260 字符] ...\\n\\nULTS_DIR, exist_ok=True)\\n\\n    nt = 2 if args.dry_run else len(TASKS)\\n    nd = 1 if args.dry_run else N_DEMOS\\n    ns = 2 if args.dry_run else N_TIMESTEPS\\n    nps = 2 if args.dry_run else N_PROBE_SEEDS\\n    cls_layers = [0, 8, 16, 24, 31] if args.dry_run else None\\n\\n    log(f\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\")\\n    log(f\\\"Output: {RESULTS_DIR}\\\")\\n\\n    log(\\\"Loading model ...\\\")\\n    t0 = time.time()\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True\\n    ).to(DEVICE).eval()\\n    import importlib.util, sys\\n    spec = importlib.util.spec_from_file_location('processing_prismatic', os.path.join(CKPT, 'processing_prismatic.py'))\\n    mod = importlib.util.module_from_spec(spec)\\n    sys.modules['processing_prismatic'] = mod\\n    spec.loader.exec_module(mod)\\n    processor = mod.PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)\\n    log(f\\\"Model loaded in {time.time()-t0:.1f}s\\\")\\n\\n    log(\\\"Validating token layout ...\\\")\\n    hdf5_path = os.path.join(DATA, f\\\"{TASKS[0]}_demo.hdf5\\\")\\n    with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n        img = Image.fromarray(hf[\\\"data/demo_0/obs/agentview_rgb\\\"][0])\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\n    log(f\\\"  input_ids shape: {inputs['input_ids'].shape}\\\")\\n    log(f\\\"  pixel_values shape: {inputs['pixel_values'].shape}\\\")\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n    hs0_shape = out.hidden_states[0].shape\\n    log(f\\\"  hidden_states[0] shape: {hs0_shape}\\\")\\n    expected_seq = inputs[\\\"input_ids\\\"].shape[1] + N_IMG_TOKENS\\n    actual_seq = hs0_shape[1]\\n    if actual_seq != expected_seq:\\n        log(f\\\"  WARNING: seq len mismatch: expected {expected_seq}, got {actual_seq}\\\")\\n        log(f\\\"  Adjusting N_IMG_TOKENS from {N_IMG_TOKENS} to {actual_seq - inputs['input_ids'].shape[1]}\\\")\\n        N_IMG_TOKENS = actual_seq - inputs[\\\"input_ids\\\"].shape[1]\\n    log(f\\\"  Token layout: BOS(1) + img({N_IMG_TOKENS}) + text({inputs['input_ids'].shape[1]-1})\\\")\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, nt, nd, ns)\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(RESULTS_DIR, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(RESULTS_DIR, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(os.path.join(RESULTS_DIR, \\\"cross_instruction_classification.json\\\"), \\\"w\\\") as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n\\n    if not args.skip_rsa:\\n        t_rsa = time.time()\\n        rsa_res = run_rsa(reps, actions, labels)\\n        with open(os.path.join(RESULTS_DIR, \\\"rsa_analysis.json\\\"), \\\"w\\\") as f:\\n            json.dump(rsa_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t_rsa:.1f}s -> rsa_analysis.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n        with open(os.path.join(RESULTS_DIR, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 6: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n\\n    total_t = time.time() - t0\\n    log(f\\\"Pipeline complete in {total_t/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "99321f2c-7861-44e5-84c5-3f40c3163d3b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. RSA: representational similarity across conditions\\\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nAll results -> RESULTS_DIR/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\\\n\\\\nCKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\"\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\\\\\"\\\\nRESULTS_DIR = \\\\\\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\nUNNORM = \\\\\\\"libero_object\\\\\\\"\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the alphabet soup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the cream cheese and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the salad dressing and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the bbq sauce and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the ketchup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the tomato sauce and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the butter and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the milk and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the chocolate pudding and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the orange juice and put it into the basket\\\\\\\",\\\\n]\\\\n\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 4096\\\\nN_IMG_TOKENS = 256\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, image).to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef generate_action(model, processor, instruction, image):\\\\n    inputs = prepare_inputs(processor, instruction, image)\\\\n    input_ids = inputs[\\\\\\\"input_ids\\\\\\\"]\\\\n\\\\n    if not torch.all(input_ids[:, -1] == 29871):\\\\n        input_ids = torch.cat(\\\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\\\n        )\\\\n        if \\\\\\\"attention_mask\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"attention_mask\\\\\\\"] = torch.cat(\\\\n                (inputs[\\\\\\\"attention_mask\\\\\\\"],\\\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\\\\\"attention_mask\\\\\\\"].dtype)), dim=1\\\\n            )\\\\n    inputs[\\\\\\\"input_ids\\\\\\\"] = input_ids\\\\n\\\\n    with torch.no_grad():\\\\n        gen_ids = model.generate(\\\\n            inputs[\\\\\\\"input_ids\\\\\\\"],\\\\n            attention_mask=inputs.get(\\\\\\\"attention_mask\\\\\\\"),\\\\n            pixel_values=inputs.get(\\\\\\\"pixel_values\\\\\\\"),\\\\n            max_new_tokens=7, do_sample=False,\\\\n        )\\\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\\\n\\\\n    vocab_size = model.vocab_size\\\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\\\n    norm_act = model.bin_centers[disc]\\\\n\\\\n    stats = mode\\\\n\\\\n... [截断: 输出过长，省略 16260 字符] ...\\\\n\\\\nULTS_DIR, exist_ok=True)\\\\n\\\\n    nt = 2 if args.dry_run else len(TASKS)\\\\n    nd = 1 if args.dry_run else N_DEMOS\\\\n    ns = 2 if args.dry_run else N_TIMESTEPS\\\\n    nps = 2 if args.dry_run else N_PROBE_SEEDS\\\\n    cls_layers = [0, 8, 16, 24, 31] if args.dry_run else None\\\\n\\\\n    log(f\\\\\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\\\\\")\\\\n    log(f\\\\\\\"Output: {RESULTS_DIR}\\\\\\\")\\\\n\\\\n    log(\\\\\\\"Loading model ...\\\\\\\")\\\\n    t0 = time.time()\\\\n    model = AutoModelForVision2Seq.from_pretrained(\\\\n        CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True\\\\n    ).to(DEVICE).eval()\\\\n    import importlib.util, sys\\\\n    spec = importlib.util.spec_from_file_location('processing_prismatic', os.path.join(CKPT, 'processing_prismatic.py'))\\\\n    mod = importlib.util.module_from_spec(spec)\\\\n    sys.modules['processing_prismatic'] = mod\\\\n    spec.loader.exec_module(mod)\\\\n    processor = mod.PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)\\\\n    log(f\\\\\\\"Model loaded in {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n    log(\\\\\\\"Validating token layout ...\\\\\\\")\\\\n    hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[0]}_demo.hdf5\\\\\\\")\\\\n    with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n        img = Image.fromarray(hf[\\\\\\\"data/demo_0/obs/agentview_rgb\\\\\\\"][0])\\\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\\\n    log(f\\\\\\\"  input_ids shape: {inputs['input_ids'].shape}\\\\\\\")\\\\n    log(f\\\\\\\"  pixel_values shape: {inputs['pixel_values'].shape}\\\\\\\")\\\\n    with torch.no_grad():\\\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\\\n    hs0_shape = out.hidden_states[0].shape\\\\n    log(f\\\\\\\"  hidden_states[0] shape: {hs0_shape}\\\\\\\")\\\\n    expected_seq = inputs[\\\\\\\"input_ids\\\\\\\"].shape[1] + N_IMG_TOKENS\\\\n    actual_seq = hs0_shape[1]\\\\n    if actual_seq != expected_seq:\\\\n        log(f\\\\\\\"  WARNING: seq len mismatch: expected {expected_seq}, got {actual_seq}\\\\\\\")\\\\n        log(f\\\\\\\"  Adjusting N_IMG_TOKENS from {N_IMG_TOKENS} to {actual_seq - inputs['input_ids'].shape[1]}\\\\\\\")\\\\n        N_IMG_TOKENS = actual_seq - inputs[\\\\\\\"input_ids\\\\\\\"].shape[1]\\\\n    log(f\\\\\\\"  Token layout: BOS(1) + img({N_IMG_TOKENS}) + text({inputs['input_ids'].shape[1]-1})\\\\\\\")\\\\n    del out, inputs\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\\\n        model, processor, nt, nd, ns)\\\\n    log(f\\\\\\\"Phase 1: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    if not args.skip_probing:\\\\n        t2 = time.time()\\\\n        probe_res = run_probing(reps, actions, nps)\\\\n        with open(os.path.join(RESULTS_DIR, \\\\\\\"action_r2_probing.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(probe_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\\\\\")\\\\n\\\\n    t3 = time.time()\\\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\\\n    with open(os.path.join(RESULTS_DIR, \\\\\\\"l1_attention_profile.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(attn_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\\\\\")\\\\n\\\\n    del l1_attns, tok_regs\\\\n\\\\n    t4 = time.time()\\\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\\\n    with open(os.path.join(RESULTS_DIR, \\\\\\\"cross_instruction_classification.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(cls_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\\\\\")\\\\n\\\\n\\\\n    if not args.skip_rsa:\\\\n        t_rsa = time.time()\\\\n        rsa_res = run_rsa(reps, actions, labels)\\\\n        with open(os.path.join(RESULTS_DIR, \\\\\\\"rsa_analysis.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(rsa_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 5: {time.time()-t_rsa:.1f}s -> rsa_analysis.json\\\\\\\")\\\\n\\\\n    del reps, actions, labels\\\\n\\\\n    if not args.skip_counterfactual:\\\\n        t5 = time.time()\\\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\\\n        with open(os.path.join(RESULTS_DIR, \\\\\\\"counterfactual_combined.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(cf_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 6: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\\\\\")\\\\n\\\\n    total_t = time.time() - t0\\\\n    log(f\\\\\\\"Pipeline complete in {total_t/60:.1f} min\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_object\\\"\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef generate_action(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n    input_ids = inputs[\\\"input_ids\\\"]\\n\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = torch.cat(\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\n        )\\n        if \\\"attention_mask\\\" in inputs:\\n            inputs[\\\"attention_mask\\\"] = torch.cat(\\n                (inputs[\\\"attention_mask\\\"],\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\"attention_mask\\\"].dtype)), dim=1\\n            )\\n    inputs[\\\"input_ids\\\"] = input_ids\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            max_new_tokens=7, do_sample=False,\\n        )\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n\\n    vocab_size = model.vocab_size\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\n    norm_act = model.bin_centers[disc]\\n\\n    stats = mode\\n\\n... [截断: 输出过长，省略 16260 字符] ...\\n\\nULTS_DIR, exist_ok=True)\\n\\n    nt = 2 if args.dry_run else len(TASKS)\\n    nd = 1 if args.dry_run else N_DEMOS\\n    ns = 2 if args.dry_run else N_TIMESTEPS\\n    nps = 2 if args.dry_run else N_PROBE_SEEDS\\n    cls_layers = [0, 8, 16, 24, 31] if args.dry_run else None\\n\\n    log(f\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\")\\n    log(f\\\"Output: {RESULTS_DIR}\\\")\\n\\n    log(\\\"Loading model ...\\\")\\n    t0 = time.time()\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True\\n    ).to(DEVICE).eval()\\n    import importlib.util, sys\\n    spec = importlib.util.spec_from_file_location('processing_prismatic', os.path.join(CKPT, 'processing_prismatic.py'))\\n    mod = importlib.util.module_from_spec(spec)\\n    sys.modules['processing_prismatic'] = mod\\n    spec.loader.exec_module(mod)\\n    processor = mod.PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)\\n    log(f\\\"Model loaded in {time.time()-t0:.1f}s\\\")\\n\\n    log(\\\"Validating token layout ...\\\")\\n    hdf5_path = os.path.join(DATA, f\\\"{TASKS[0]}_demo.hdf5\\\")\\n    with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n        img = Image.fromarray(hf[\\\"data/demo_0/obs/agentview_rgb\\\"][0])\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\n    log(f\\\"  input_ids shape: {inputs['input_ids'].shape}\\\")\\n    log(f\\\"  pixel_values shape: {inputs['pixel_values'].shape}\\\")\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n    hs0_shape = out.hidden_states[0].shape\\n    log(f\\\"  hidden_states[0] shape: {hs0_shape}\\\")\\n    expected_seq = inputs[\\\"input_ids\\\"].shape[1] + N_IMG_TOKENS\\n    actual_seq = hs0_shape[1]\\n    if actual_seq != expected_seq:\\n        log(f\\\"  WARNING: seq len mismatch: expected {expected_seq}, got {actual_seq}\\\")\\n        log(f\\\"  Adjusting N_IMG_TOKENS from {N_IMG_TOKENS} to {actual_seq - inputs['input_ids'].shape[1]}\\\")\\n        N_IMG_TOKENS = actual_seq - inputs[\\\"input_ids\\\"].shape[1]\\n    log(f\\\"  Token layout: BOS(1) + img({N_IMG_TOKENS}) + text({inputs['input_ids'].shape[1]-1})\\\")\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, nt, nd, ns)\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(RESULTS_DIR, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(RESULTS_DIR, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(os.path.join(RESULTS_DIR, \\\"cross_instruction_classification.json\\\"), \\\"w\\\") as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n\\n    if not args.skip_rsa:\\n        t_rsa = time.time()\\n        rsa_res = run_rsa(reps, actions, labels)\\n        with open(os.path.join(RESULTS_DIR, \\\"rsa_analysis.json\\\"), \\\"w\\\") as f:\\n            json.dump(rsa_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t_rsa:.1f}s -> rsa_analysis.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n        with open(os.path.join(RESULTS_DIR, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 6: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n\\n    total_t = time.time() - t0\\n    log(f\\\"Pipeline complete in {total_t/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T05:03:45.166Z_

<details><summary>↩ Tool result · `toolu_019iiLVvhnwg8vfsaUZCr48u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Goal Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_goal\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"put_the_bowl_on_the_stove\\\",\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n    \\\"put_the_cream_cheese_in_the_bowl\\\",\\n    \\\"put_the_wine_bottle_on_the_rack\\\",\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\",\\n    \\\"turn_on_the_stove\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"open the cabinet's middle drawer\\\",\\n    \\\"open the top drawer and place the bowl in it\\\",\\n    \\\"slide the plate to the stove's front\\\",\\n    \\\"place the bowl onto the plate\\\",\\n    \\\"place the bowl onto the stove\\\",\\n    \\\"place the bowl on the cabinet top\\\",\\n    \\\"put cream cheese into the bowl\\\",\\n    \\\"place the wine bottle on the rack\\\",\\n    \\\"place the wine bottle on the cabinet top\\\",\\n    \\\"switch on the stove\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    messages = [{'role': 'user', 'content': [\\n        {'type': 'image', 'image': image},\\n        {'type': 'text', 'text': instruction}\\n    ]}]\\n    text = processor.apply_chat_template(\\n        messages, tokenize=False, add_generation_prompt=True)\\n    inputs = processor(\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\n            for k, v in inputs.items()}\\n\\n\\ndef find_token_regions(input_ids, config):\\n    ids = input_ids[0].cpu().numpy()\\n    vs_id = config.vision_start_token_id\\n    ve_id = config.vision_end_token_id\\n\\n    vs_pos = np.where(ids == vs_id)[0]\\n    ve_pos = np.where(ids == ve_id)[0]\\n\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\n        img_s = int(vs_pos[0]) + 1\\n        img_e = int(ve_pos[0])\\n    else:\\n        img_s = img_e = 0\\n\\n    bos_e = int(vs_pos[0]) if len(vs_pos) > 0 else 0\\n    txt_s = int(ve_pos[0]) + 1 if len(ve_pos) > 0 else img_e\\n    txt_e = len(ids)\\n\\n    return {\\\"bos\\\": (0, bos_e), \\\"image\\\": (img_s, img_e), \\\"text\\\": (txt_s, txt_e)}\\n\\n\\ndef extract_features(model, processor, config, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.f\\n\\n... [截断: 输出过长，省略 14631 字符] ...\\n\\n\\n    hdf5_path = os.path.join(DATA, f\\\"{TASKS[0]}_demo.hdf5\\\")\\n    with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n        img = Image.fromarray(hf[\\\"data/demo_0/obs/agentview_rgb\\\"][0])\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\n    log(f\\\"  input_ids shape: {inputs['input_ids'].shape}\\\")\\n\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n\\n    tr = find_token_regions(inputs[\\\"input_ids\\\"], config)\\n    n_img = tr[\\\"image\\\"][1] - tr[\\\"image\\\"][0]\\n    log(f\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\")\\n    log(f\\\"  N_IMG_TOKENS={n_img}, hidden={out.hidden_states[0].shape}\\\")\\n    log(f\\\"  Attention: {len(out.attentions)} layers, shape={out.attentions[0].shape}\\\")\\n\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, config, nt, nd, ns\\n    )\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(results_dir, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(results_dir, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(\\n        os.path.join(results_dir, \\\"cross_instruction_classification.json\\\"), \\\"w\\\"\\n    ) as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if condition == \\\"trained\\\" and not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, config, nt, nd, ns)\\n        with open(\\n            os.path.join(results_dir, \\\"counterfactual_combined.json\\\"), \\\"w\\\"\\n        ) as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n    elif condition != \\\"trained\\\":\\n        log(\\\"Phase 5: skipped (untrained model)\\\")\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-probing\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\", nargs=\\\"+\\\", choices=[\\\"trained\\\", \\\"untrained\\\"],\\n        default=[\\\"trained\\\", \\\"untrained\\\"],\\n        help=\\\"Conditions to run (trained untrained)\\\",\\n    )\\n    p.add_argument(\\\"--device\\\", default=None)\\n    args = p.parse_args()\\n\\n    global DEVICE\\n    if args.device:\\n        DEVICE = args.device\\n\\n    conditions = args.conditions\\n    log(f\\\"Pipeline conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            ckpt = UNTRAINED_CKPT\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n\\n        try:\\n            model, processor = load_model(ckpt)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            log(f\\\"  Skipping {condition} condition\\\")\\n            continue\\n\\n        config = model.config\\n        tc = time.time()\\n        run_pipeline(model, processor, config, condition, results_dir, args)\\n        log(f\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "ebed1f10-3d6e-4b6f-8dfe-945525088b5b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nNORA LIBERO-Goal Full Analysis Pipeline\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\\\n\\\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\\\ncosine distance instead of action MSE.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/nora_goal\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\n\\\\n# --- Architecture (Qwen2.5-VL-3B) ---\\\\nN_LAYERS = 36\\\\nN_HEADS = 16\\\\nHIDDEN = 2048\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\",\\\\n    \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_the_plate\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_the_stove\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\",\\\\n    \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\",\\\\n    \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"turn_on_the_stove\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"open the cabinet's middle drawer\\\\\\\",\\\\n    \\\\\\\"open the top drawer and place the bowl in it\\\\\\\",\\\\n    \\\\\\\"slide the plate to the stove's front\\\\\\\",\\\\n    \\\\\\\"place the bowl onto the plate\\\\\\\",\\\\n    \\\\\\\"place the bowl onto the stove\\\\\\\",\\\\n    \\\\\\\"place the bowl on the cabinet top\\\\\\\",\\\\n    \\\\\\\"put cream cheese into the bowl\\\\\\\",\\\\n    \\\\\\\"place the wine bottle on the rack\\\\\\\",\\\\n    \\\\\\\"place the wine bottle on the cabinet top\\\\\\\",\\\\n    \\\\\\\"switch on the stove\\\\\\\",\\\\n]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    messages = [{'role': 'user', 'content': [\\\\n        {'type': 'image', 'image': image},\\\\n        {'type': 'text', 'text': instruction}\\\\n    ]}]\\\\n    text = processor.apply_chat_template(\\\\n        messages, tokenize=False, add_generation_prompt=True)\\\\n    inputs = processor(\\\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\\\n            for k, v in inputs.items()}\\\\n\\\\n\\\\ndef find_token_regions(input_ids, config):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    vs_id = config.vision_start_token_id\\\\n    ve_id = config.vision_end_token_id\\\\n\\\\n    vs_pos = np.where(ids == vs_id)[0]\\\\n    ve_pos = np.where(ids == ve_id)[0]\\\\n\\\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\\\n        img_s = int(vs_pos[0]) + 1\\\\n        img_e = int(ve_pos[0])\\\\n    else:\\\\n        img_s = img_e = 0\\\\n\\\\n    bos_e = int(vs_pos[0]) if len(vs_pos) > 0 else 0\\\\n    txt_s = int(ve_pos[0]) + 1 if len(ve_pos) > 0 else img_e\\\\n    txt_e = len(ids)\\\\n\\\\n    return {\\\\\\\"bos\\\\\\\": (0, bos_e), \\\\\\\"image\\\\\\\": (img_s, img_e), \\\\\\\"text\\\\\\\": (txt_s, txt_e)}\\\\n\\\\n\\\\ndef extract_features(model, processor, config, n_tasks, n_demos, n_timesteps):\\\\n    log(\\\\\\\"Phase 1: representation extraction\\\\\\\")\\\\n    total = n_tasks * n_demos * n_timesteps\\\\n\\\\n    reps = {\\\\n        l: {\\\\n            \\\\\\\"image_mean\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n            \\\\\\\"last_preaction\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n        }\\\\n        for l in range(N_LAYERS)\\\\n    }\\\\n    actions_arr = np.zeros((total, 7), dtype=np.f\\\\n\\\\n... [截断: 输出过长，省略 14631 字符] ...\\\\n\\\\n\\\\n    hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[0]}_demo.hdf5\\\\\\\")\\\\n    with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n        img = Image.fromarray(hf[\\\\\\\"data/demo_0/obs/agentview_rgb\\\\\\\"][0])\\\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\\\n    log(f\\\\\\\"  input_ids shape: {inputs['input_ids'].shape}\\\\\\\")\\\\n\\\\n    with torch.no_grad():\\\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\\\n\\\\n    tr = find_token_regions(inputs[\\\\\\\"input_ids\\\\\\\"], config)\\\\n    n_img = tr[\\\\\\\"image\\\\\\\"][1] - tr[\\\\\\\"image\\\\\\\"][0]\\\\n    log(f\\\\\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\\\\\")\\\\n    log(f\\\\\\\"  N_IMG_TOKENS={n_img}, hidden={out.hidden_states[0].shape}\\\\\\\")\\\\n    log(f\\\\\\\"  Attention: {len(out.attentions)} layers, shape={out.attentions[0].shape}\\\\\\\")\\\\n\\\\n    del out, inputs\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\\\n        model, processor, config, nt, nd, ns\\\\n    )\\\\n    log(f\\\\\\\"Phase 1: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    if not args.skip_probing:\\\\n        t2 = time.time()\\\\n        probe_res = run_probing(reps, actions, nps)\\\\n        with open(os.path.join(results_dir, \\\\\\\"action_r2_probing.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(probe_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\\\\\")\\\\n\\\\n    t3 = time.time()\\\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\\\n    with open(os.path.join(results_dir, \\\\\\\"l1_attention_profile.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(attn_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\\\\\")\\\\n\\\\n    del l1_attns, tok_regs\\\\n\\\\n    t4 = time.time()\\\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\\\n    with open(\\\\n        os.path.join(results_dir, \\\\\\\"cross_instruction_classification.json\\\\\\\"), \\\\\\\"w\\\\\\\"\\\\n    ) as f:\\\\n        json.dump(cls_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\\\\\")\\\\n\\\\n    del reps, actions, labels\\\\n\\\\n    if condition == \\\\\\\"trained\\\\\\\" and not args.skip_counterfactual:\\\\n        t5 = time.time()\\\\n        cf_res = run_counterfactual(model, processor, config, nt, nd, ns)\\\\n        with open(\\\\n            os.path.join(results_dir, \\\\\\\"counterfactual_combined.json\\\\\\\"), \\\\\\\"w\\\\\\\"\\\\n        ) as f:\\\\n            json.dump(cf_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\\\\\")\\\\n    elif condition != \\\\\\\"trained\\\\\\\":\\\\n        log(\\\\\\\"Phase 5: skipped (untrained model)\\\\\\\")\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--dry-run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip-counterfactual\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip-probing\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\n        \\\\\\\"--conditions\\\\\\\", nargs=\\\\\\\"+\\\\\\\", choices=[\\\\\\\"trained\\\\\\\", \\\\\\\"untrained\\\\\\\"],\\\\n        default=[\\\\\\\"trained\\\\\\\", \\\\\\\"untrained\\\\\\\"],\\\\n        help=\\\\\\\"Conditions to run (trained untrained)\\\\\\\",\\\\n    )\\\\n    p.add_argument(\\\\\\\"--device\\\\\\\", default=None)\\\\n    args = p.parse_args()\\\\n\\\\n    global DEVICE\\\\n    if args.device:\\\\n        DEVICE = args.device\\\\n\\\\n    conditions = args.conditions\\\\n    log(f\\\\\\\"Pipeline conditions: {conditions}\\\\\\\")\\\\n\\\\n    t_start = time.time()\\\\n\\\\n    for condition in conditions:\\\\n        if condition == \\\\\\\"trained\\\\\\\":\\\\n            ckpt = TRAINED_CKPT\\\\n        elif condition == \\\\\\\"untrained\\\\\\\":\\\\n            ckpt = UNTRAINED_CKPT\\\\n        else:\\\\n            log(f\\\\\\\"  Unknown condition: {condition}, skipping\\\\\\\")\\\\n            continue\\\\n\\\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\\\n\\\\n        try:\\\\n            model, processor = load_model(ckpt)\\\\n        except Exception as e:\\\\n            log(f\\\\\\\"  ERROR loading {condition} model: {e}\\\\\\\")\\\\n            log(f\\\\\\\"  Skipping {condition} condition\\\\\\\")\\\\n            continue\\\\n\\\\n        config = model.config\\\\n        tc = time.time()\\\\n        run_pipeline(model, processor, config, condition, results_dir, args)\\\\n        log(f\\\\\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\\\\\")\\\\n\\\\n        del model, processor\\\\n        torch.cuda.empty_cache()\\\\n\\\\n    log(f\\\\\\\"All done in {(time.time()-t_start)/60:.1f} min\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Goal Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_goal\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"put_the_bowl_on_the_stove\\\",\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n    \\\"put_the_cream_cheese_in_the_bowl\\\",\\n    \\\"put_the_wine_bottle_on_the_rack\\\",\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\",\\n    \\\"turn_on_the_stove\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"open the cabinet's middle drawer\\\",\\n    \\\"open the top drawer and place the bowl in it\\\",\\n    \\\"slide the plate to the stove's front\\\",\\n    \\\"place the bowl onto the plate\\\",\\n    \\\"place the bowl onto the stove\\\",\\n    \\\"place the bowl on the cabinet top\\\",\\n    \\\"put cream cheese into the bowl\\\",\\n    \\\"place the wine bottle on the rack\\\",\\n    \\\"place the wine bottle on the cabinet top\\\",\\n    \\\"switch on the stove\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    messages = [{'role': 'user', 'content': [\\n        {'type': 'image', 'image': image},\\n        {'type': 'text', 'text': instruction}\\n    ]}]\\n    text = processor.apply_chat_template(\\n        messages, tokenize=False, add_generation_prompt=True)\\n    inputs = processor(\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\n            for k, v in inputs.items()}\\n\\n\\ndef find_token_regions(input_ids, config):\\n    ids = input_ids[0].cpu().numpy()\\n    vs_id = config.vision_start_token_id\\n    ve_id = config.vision_end_token_id\\n\\n    vs_pos = np.where(ids == vs_id)[0]\\n    ve_pos = np.where(ids == ve_id)[0]\\n\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\n        img_s = int(vs_pos[0]) + 1\\n        img_e = int(ve_pos[0])\\n    else:\\n        img_s = img_e = 0\\n\\n    bos_e = int(vs_pos[0]) if len(vs_pos) > 0 else 0\\n    txt_s = int(ve_pos[0]) + 1 if len(ve_pos) > 0 else img_e\\n    txt_e = len(ids)\\n\\n    return {\\\"bos\\\": (0, bos_e), \\\"image\\\": (img_s, img_e), \\\"text\\\": (txt_s, txt_e)}\\n\\n\\ndef extract_features(model, processor, config, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.f\\n\\n... [截断: 输出过长，省略 14631 字符] ...\\n\\n\\n    hdf5_path = os.path.join(DATA, f\\\"{TASKS[0]}_demo.hdf5\\\")\\n    with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n        img = Image.fromarray(hf[\\\"data/demo_0/obs/agentview_rgb\\\"][0])\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\n    log(f\\\"  input_ids shape: {inputs['input_ids'].shape}\\\")\\n\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n\\n    tr = find_token_regions(inputs[\\\"input_ids\\\"], config)\\n    n_img = tr[\\\"image\\\"][1] - tr[\\\"image\\\"][0]\\n    log(f\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\")\\n    log(f\\\"  N_IMG_TOKENS={n_img}, hidden={out.hidden_states[0].shape}\\\")\\n    log(f\\\"  Attention: {len(out.attentions)} layers, shape={out.attentions[0].shape}\\\")\\n\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, config, nt, nd, ns\\n    )\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(results_dir, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(results_dir, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(\\n        os.path.join(results_dir, \\\"cross_instruction_classification.json\\\"), \\\"w\\\"\\n    ) as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if condition == \\\"trained\\\" and not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, config, nt, nd, ns)\\n        with open(\\n            os.path.join(results_dir, \\\"counterfactual_combined.json\\\"), \\\"w\\\"\\n        ) as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n    elif condition != \\\"trained\\\":\\n        log(\\\"Phase 5: skipped (untrained model)\\\")\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-probing\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\", nargs=\\\"+\\\", choices=[\\\"trained\\\", \\\"untrained\\\"],\\n        default=[\\\"trained\\\", \\\"untrained\\\"],\\n        help=\\\"Conditions to run (trained untrained)\\\",\\n    )\\n    p.add_argument(\\\"--device\\\", default=None)\\n    args = p.parse_args()\\n\\n    global DEVICE\\n    if args.device:\\n        DEVICE = args.device\\n\\n    conditions = args.conditions\\n    log(f\\\"Pipeline conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            ckpt = UNTRAINED_CKPT\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n\\n        try:\\n            model, processor = load_model(ckpt)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            log(f\\\"  Skipping {condition} condition\\\")\\n            continue\\n\\n        config = model.config\\n        tc = time.time()\\n        run_pipeline(model, processor, config, condition, results_dir, args)\\n        log(f\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017K89ELApv4KPuab7GE5fKe`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "31f96fb9-2151-4943-813f-01802822ef5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cz8HUVqfcc5ENLaMfDS4tC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 25500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 16 · 2026-05-21T05:03:45.976Z_

<details><summary>↩ Tool result · `toolu_017K89ELApv4KPuab7GE5fKe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Spatial Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the black bowl between the plate and ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl from the center of the table and put it on the plate\\\",\\n    \\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl next to the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl next to the plate and put it on the plate\\\",\\n    \\\"grab the black bowl next to the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl on the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the stove and put it on the plate\\\",\\n    \\\"grab the black bowl on the wooden cabinet and put it on the plate\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    messages = [{'role': 'user', 'content': [\\n        {'type': 'image', 'image': image},\\n        {'type': 'text', 'text': instruction}\\n    ]}]\\n    text = processor.apply_chat_template(\\n        messages, tokenize=False, add_generation_prompt=True)\\n    inputs = processor(\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\n            for k, v in inputs.items()}\\n\\n\\ndef find_token_regions(input_ids, config):\\n    ids = input_ids[0].cpu().numpy()\\n    vs_id = config.vision_start_token_id\\n    ve_id = config.vision_end_token_id\\n\\n    vs_pos = np.where(ids == vs_id)[0]\\n    ve_pos = np.where(ids == ve_id)[0]\\n\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\n        img_s = int(vs_pos[0]) + 1\\n     \\n\\n... [截断: 输出过长，省略 15337 字符] ...\\n\\nng token layout ...\\\")\\n    hdf5_path = os.path.join(DATA, f\\\"{TASKS[0]}_demo.hdf5\\\")\\n    with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n        img = Image.fromarray(hf[\\\"data/demo_0/obs/agentview_rgb\\\"][0])\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\n    log(f\\\"  input_ids shape: {inputs['input_ids'].shape}\\\")\\n\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n\\n    tr = find_token_regions(inputs[\\\"input_ids\\\"], config)\\n    n_img = tr[\\\"image\\\"][1] - tr[\\\"image\\\"][0]\\n    log(f\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\")\\n    log(f\\\"  N_IMG_TOKENS={n_img}, hidden={out.hidden_states[0].shape}\\\")\\n    log(f\\\"  Attention: {len(out.attentions)} layers, shape={out.attentions[0].shape}\\\")\\n\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, config, nt, nd, ns\\n    )\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(results_dir, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(results_dir, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(\\n        os.path.join(results_dir, \\\"cross_instruction_classification.json\\\"), \\\"w\\\"\\n    ) as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if condition == \\\"trained\\\" and not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, config, nt, nd, ns)\\n        with open(\\n            os.path.join(results_dir, \\\"counterfactual_combined.json\\\"), \\\"w\\\"\\n        ) as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n    elif condition != \\\"trained\\\":\\n        log(\\\"Phase 5: skipped (untrained model)\\\")\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-probing\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\",\\n        default=\\\"trained,untrained\\\",\\n        help=\\\"Comma-separated: trained,untrained\\\",\\n    )\\n    p.add_argument(\\\"--device\\\", default=None)\\n    args = p.parse_args()\\n\\n    global DEVICE\\n    if args.device:\\n        DEVICE = args.device\\n\\n    conditions = [c.strip() for c in args.conditions.split(\\\",\\\")]\\n    log(f\\\"Pipeline conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            ckpt = UNTRAINED_CKPT\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n\\n        try:\\n            model, processor = load_model(ckpt)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            log(f\\\"  Skipping {condition} condition\\\")\\n            continue\\n\\n        config = model.config\\n        tc = time.time()\\n        run_pipeline(model, processor, config, condition, results_dir, args)\\n        log(f\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "88c00d74-ec00-47cb-bb24-a68bdb4c0ec4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nNORA LIBERO-Spatial Full Analysis Pipeline\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\\\n\\\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\\\ncosine distance instead of action MSE.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/nora_spatial\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\n\\\\n# --- Architecture (Qwen2.5-VL-3B) ---\\\\nN_LAYERS = 36\\\\nN_HEADS = 16\\\\nHIDDEN = 2048\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the black bowl between the plate and ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl from the center of the table and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the cookie box and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the plate and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the cookie box and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the stove and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the wooden cabinet and put it on the plate\\\\\\\",\\\\n]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    messages = [{'role': 'user', 'content': [\\\\n        {'type': 'image', 'image': image},\\\\n        {'type': 'text', 'text': instruction}\\\\n    ]}]\\\\n    text = processor.apply_chat_template(\\\\n        messages, tokenize=False, add_generation_prompt=True)\\\\n    inputs = processor(\\\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\\\n            for k, v in inputs.items()}\\\\n\\\\n\\\\ndef find_token_regions(input_ids, config):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    vs_id = config.vision_start_token_id\\\\n    ve_id = config.vision_end_token_id\\\\n\\\\n    vs_pos = np.where(ids == vs_id)[0]\\\\n    ve_pos = np.where(ids == ve_id)[0]\\\\n\\\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\\\n        img_s = int(vs_pos[0]) + 1\\\\n     \\\\n\\\\n... [截断: 输出过长，省略 15337 字符] ...\\\\n\\\\nng token layout ...\\\\\\\")\\\\n    hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[0]}_demo.hdf5\\\\\\\")\\\\n    with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n        img = Image.fromarray(hf[\\\\\\\"data/demo_0/obs/agentview_rgb\\\\\\\"][0])\\\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\\\n    log(f\\\\\\\"  input_ids shape: {inputs['input_ids'].shape}\\\\\\\")\\\\n\\\\n    with torch.no_grad():\\\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\\\n\\\\n    tr = find_token_regions(inputs[\\\\\\\"input_ids\\\\\\\"], config)\\\\n    n_img = tr[\\\\\\\"image\\\\\\\"][1] - tr[\\\\\\\"image\\\\\\\"][0]\\\\n    log(f\\\\\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\\\\\")\\\\n    log(f\\\\\\\"  N_IMG_TOKENS={n_img}, hidden={out.hidden_states[0].shape}\\\\\\\")\\\\n    log(f\\\\\\\"  Attention: {len(out.attentions)} layers, shape={out.attentions[0].shape}\\\\\\\")\\\\n\\\\n    del out, inputs\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\\\n        model, processor, config, nt, nd, ns\\\\n    )\\\\n    log(f\\\\\\\"Phase 1: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    if not args.skip_probing:\\\\n        t2 = time.time()\\\\n        probe_res = run_probing(reps, actions, nps)\\\\n        with open(os.path.join(results_dir, \\\\\\\"action_r2_probing.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(probe_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\\\\\")\\\\n\\\\n    t3 = time.time()\\\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\\\n    with open(os.path.join(results_dir, \\\\\\\"l1_attention_profile.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(attn_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\\\\\")\\\\n\\\\n    del l1_attns, tok_regs\\\\n\\\\n    t4 = time.time()\\\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\\\n    with open(\\\\n        os.path.join(results_dir, \\\\\\\"cross_instruction_classification.json\\\\\\\"), \\\\\\\"w\\\\\\\"\\\\n    ) as f:\\\\n        json.dump(cls_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\\\\\")\\\\n\\\\n    del reps, actions, labels\\\\n\\\\n    if condition == \\\\\\\"trained\\\\\\\" and not args.skip_counterfactual:\\\\n        t5 = time.time()\\\\n        cf_res = run_counterfactual(model, processor, config, nt, nd, ns)\\\\n        with open(\\\\n            os.path.join(results_dir, \\\\\\\"counterfactual_combined.json\\\\\\\"), \\\\\\\"w\\\\\\\"\\\\n        ) as f:\\\\n            json.dump(cf_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\\\\\")\\\\n    elif condition != \\\\\\\"trained\\\\\\\":\\\\n        log(\\\\\\\"Phase 5: skipped (untrained model)\\\\\\\")\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--dry-run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip-counterfactual\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip-probing\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\n        \\\\\\\"--conditions\\\\\\\",\\\\n        default=\\\\\\\"trained,untrained\\\\\\\",\\\\n        help=\\\\\\\"Comma-separated: trained,untrained\\\\\\\",\\\\n    )\\\\n    p.add_argument(\\\\\\\"--device\\\\\\\", default=None)\\\\n    args = p.parse_args()\\\\n\\\\n    global DEVICE\\\\n    if args.device:\\\\n        DEVICE = args.device\\\\n\\\\n    conditions = [c.strip() for c in args.conditions.split(\\\\\\\",\\\\\\\")]\\\\n    log(f\\\\\\\"Pipeline conditions: {conditions}\\\\\\\")\\\\n\\\\n    t_start = time.time()\\\\n\\\\n    for condition in conditions:\\\\n        if condition == \\\\\\\"trained\\\\\\\":\\\\n            ckpt = TRAINED_CKPT\\\\n        elif condition == \\\\\\\"untrained\\\\\\\":\\\\n            ckpt = UNTRAINED_CKPT\\\\n        else:\\\\n            log(f\\\\\\\"  Unknown condition: {condition}, skipping\\\\\\\")\\\\n            continue\\\\n\\\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\\\n\\\\n        try:\\\\n            model, processor = load_model(ckpt)\\\\n        except Exception as e:\\\\n            log(f\\\\\\\"  ERROR loading {condition} model: {e}\\\\\\\")\\\\n            log(f\\\\\\\"  Skipping {condition} condition\\\\\\\")\\\\n            continue\\\\n\\\\n        config = model.config\\\\n        tc = time.time()\\\\n        run_pipeline(model, processor, config, condition, results_dir, args)\\\\n        log(f\\\\\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\\\\\")\\\\n\\\\n        del model, processor\\\\n        torch.cuda.empty_cache()\\\\n\\\\n    log(f\\\\\\\"All done in {(time.time()-t_start)/60:.1f} min\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Spatial Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the black bowl between the plate and ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl from the center of the table and put it on the plate\\\",\\n    \\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl next to the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl next to the plate and put it on the plate\\\",\\n    \\\"grab the black bowl next to the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl on the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the stove and put it on the plate\\\",\\n    \\\"grab the black bowl on the wooden cabinet and put it on the plate\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    messages = [{'role': 'user', 'content': [\\n        {'type': 'image', 'image': image},\\n        {'type': 'text', 'text': instruction}\\n    ]}]\\n    text = processor.apply_chat_template(\\n        messages, tokenize=False, add_generation_prompt=True)\\n    inputs = processor(\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\n            for k, v in inputs.items()}\\n\\n\\ndef find_token_regions(input_ids, config):\\n    ids = input_ids[0].cpu().numpy()\\n    vs_id = config.vision_start_token_id\\n    ve_id = config.vision_end_token_id\\n\\n    vs_pos = np.where(ids == vs_id)[0]\\n    ve_pos = np.where(ids == ve_id)[0]\\n\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\n        img_s = int(vs_pos[0]) + 1\\n     \\n\\n... [截断: 输出过长，省略 15337 字符] ...\\n\\nng token layout ...\\\")\\n    hdf5_path = os.path.join(DATA, f\\\"{TASKS[0]}_demo.hdf5\\\")\\n    with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n        img = Image.fromarray(hf[\\\"data/demo_0/obs/agentview_rgb\\\"][0])\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\n    log(f\\\"  input_ids shape: {inputs['input_ids'].shape}\\\")\\n\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n\\n    tr = find_token_regions(inputs[\\\"input_ids\\\"], config)\\n    n_img = tr[\\\"image\\\"][1] - tr[\\\"image\\\"][0]\\n    log(f\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\")\\n    log(f\\\"  N_IMG_TOKENS={n_img}, hidden={out.hidden_states[0].shape}\\\")\\n    log(f\\\"  Attention: {len(out.attentions)} layers, shape={out.attentions[0].shape}\\\")\\n\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, config, nt, nd, ns\\n    )\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(results_dir, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(results_dir, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(\\n        os.path.join(results_dir, \\\"cross_instruction_classification.json\\\"), \\\"w\\\"\\n    ) as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if condition == \\\"trained\\\" and not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, config, nt, nd, ns)\\n        with open(\\n            os.path.join(results_dir, \\\"counterfactual_combined.json\\\"), \\\"w\\\"\\n        ) as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n    elif condition != \\\"trained\\\":\\n        log(\\\"Phase 5: skipped (untrained model)\\\")\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-probing\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\",\\n        default=\\\"trained,untrained\\\",\\n        help=\\\"Comma-separated: trained,untrained\\\",\\n    )\\n    p.add_argument(\\\"--device\\\", default=None)\\n    args = p.parse_args()\\n\\n    global DEVICE\\n    if args.device:\\n        DEVICE = args.device\\n\\n    conditions = [c.strip() for c in args.conditions.split(\\\",\\\")]\\n    log(f\\\"Pipeline conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            ckpt = UNTRAINED_CKPT\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n\\n        try:\\n            model, processor = load_model(ckpt)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            log(f\\\"  Skipping {condition} condition\\\")\\n            continue\\n\\n        config = model.config\\n        tc = time.time()\\n        run_pipeline(model, processor, config, condition, results_dir, args)\\n        log(f\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Rk8YwJha5wJWyMesUMooLQ`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "65020314-35b1-41f4-8ea0-55a5b361b66e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cz8HUVqfcc5ENLaMfDS4tC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 25500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 18 · 2026-05-21T05:03:46.504Z_

<details><summary>↩ Tool result · `toolu_01Rk8YwJha5wJWyMesUMooLQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Spatial Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the black bowl between the plate and ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl from the center of the table and put it on the plate\\\",\\n    \\\"grab the black bowl next to the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl on the stove and put it on the plate\\\",\\n    \\\"grab the black bowl on the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl next to the plate and put it on the plate\\\",\\n    \\\"grab the black bowl next to the ramekin and put it on the plate\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef detect_image_token_id(processor):\\n    return -1\\n\\n\\ndef find_token_regions(input_ids, img_token_id):\\n    ids = input_ids[0].cpu().numpy()\\n    img_mask = ids < 0\\n    img_positions = np.where(img_mask)[0]\\n\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0\\n\\n... [截断: 输出过长，省略 16115 字符] ...\\n\\ninputs['image_sizes']}\\\")\\n\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n\\n    hs0_shape = out.hidden_states[0].shape\\n    log(f\\\"  hidden_states[0] shape: {hs0_shape}\\\")\\n\\n    tr = find_token_regions(original_ids, IMG_TOKEN_ID)\\n    N_IMG_TOKENS = tr[\\\"image\\\"][1] - tr[\\\"image\\\"][0]\\n    log(f\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\")\\n    log(f\\\"  N_IMG_TOKENS={N_IMG_TOKENS}\\\")\\n    log(f\\\"  Total seq_len: input_ids={inputs['input_ids'].shape[1]}, hidden={hs0_shape[1]}\\\")\\n\\n    n_attn_layers = len(out.attentions)\\n    attn_shape = out.attentions[0].shape\\n    log(f\\\"  Attention: {n_attn_layers} layers, shape={attn_shape}\\\")\\n\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, nt, nd, ns, IMG_TOKEN_ID\\n    )\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(results_dir, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(results_dir, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(os.path.join(results_dir, \\\"cross_instruction_classification.json\\\"), \\\"w\\\") as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if condition == \\\"trained\\\" and not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n        with open(os.path.join(results_dir, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n    elif condition != \\\"trained\\\":\\n        log(\\\"Phase 5: skipped (untrained model cannot generate meaningful actions)\\\")\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-probing\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\",\\n        default=\\\"trained,untrained\\\",\\n        help=\\\"Comma-separated: trained,untrained\\\",\\n    )\\n    args = p.parse_args()\\n\\n    conditions = [c.strip() for c in args.conditions.split(\\\",\\\")]\\n    log(f\\\"Pipeline conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\"config.json\\\")):\\n                ckpt = UNTRAINED_CACHE\\n            else:\\n                ckpt = UNTRAINED_CKPT\\n                log(f\\\"  Will download untrained model from {ckpt}\\\")\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n\\n        try:\\n            model, processor = load_model(ckpt, condition)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            log(f\\\"  Skipping {condition} condition\\\")\\n            continue\\n\\n        tc = time.time()\\n        run_pipeline(model, processor, condition, results_dir, args)\\n        log(f\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "0f3d80a8-5832-4299-b7cc-00ec0dccfbf2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Spatial Full Analysis Pipeline for TracVLA-Phi3V\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"microsoft/Phi-3-vision-128k-instruct\\\\\\\"\\\\nUNTRAINED_CACHE = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\\\n\\\\n# --- Architecture ---\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 3072\\\\nN_IMG_TOKENS = 0  # auto-detected\\\\nIMG_TOKEN_ID = -1  # auto-detected\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the black bowl between the plate and ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the cookie box and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl from the center of the table and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the cookie box and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the stove and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the wooden cabinet and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the plate and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the ramekin and put it on the plate\\\\\\\",\\\\n]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return (\\\\n        f\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\"\\\\n    )\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef detect_image_token_id(processor):\\\\n    return -1\\\\n\\\\n\\\\ndef find_token_regions(input_ids, img_token_id):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    img_mask = ids < 0\\\\n    img_positions = np.where(img_mask)[0]\\\\n\\\\n    if len(img_positions) > 0:\\\\n        img_s = int(img_positions[0\\\\n\\\\n... [截断: 输出过长，省略 16115 字符] ...\\\\n\\\\ninputs['image_sizes']}\\\\\\\")\\\\n\\\\n    with torch.no_grad():\\\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\\\n\\\\n    hs0_shape = out.hidden_states[0].shape\\\\n    log(f\\\\\\\"  hidden_states[0] shape: {hs0_shape}\\\\\\\")\\\\n\\\\n    tr = find_token_regions(original_ids, IMG_TOKEN_ID)\\\\n    N_IMG_TOKENS = tr[\\\\\\\"image\\\\\\\"][1] - tr[\\\\\\\"image\\\\\\\"][0]\\\\n    log(f\\\\\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\\\\\")\\\\n    log(f\\\\\\\"  N_IMG_TOKENS={N_IMG_TOKENS}\\\\\\\")\\\\n    log(f\\\\\\\"  Total seq_len: input_ids={inputs['input_ids'].shape[1]}, hidden={hs0_shape[1]}\\\\\\\")\\\\n\\\\n    n_attn_layers = len(out.attentions)\\\\n    attn_shape = out.attentions[0].shape\\\\n    log(f\\\\\\\"  Attention: {n_attn_layers} layers, shape={attn_shape}\\\\\\\")\\\\n\\\\n    del out, inputs\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\\\n        model, processor, nt, nd, ns, IMG_TOKEN_ID\\\\n    )\\\\n    log(f\\\\\\\"Phase 1: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    if not args.skip_probing:\\\\n        t2 = time.time()\\\\n        probe_res = run_probing(reps, actions, nps)\\\\n        with open(os.path.join(results_dir, \\\\\\\"action_r2_probing.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(probe_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\\\\\")\\\\n\\\\n    t3 = time.time()\\\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\\\n    with open(os.path.join(results_dir, \\\\\\\"l1_attention_profile.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(attn_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\\\\\")\\\\n\\\\n    del l1_attns, tok_regs\\\\n\\\\n    t4 = time.time()\\\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\\\n    with open(os.path.join(results_dir, \\\\\\\"cross_instruction_classification.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(cls_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\\\\\")\\\\n\\\\n    del reps, actions, labels\\\\n\\\\n    if condition == \\\\\\\"trained\\\\\\\" and not args.skip_counterfactual:\\\\n        t5 = time.time()\\\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\\\n        with open(os.path.join(results_dir, \\\\\\\"counterfactual_combined.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(cf_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\\\\\")\\\\n    elif condition != \\\\\\\"trained\\\\\\\":\\\\n        log(\\\\\\\"Phase 5: skipped (untrained model cannot generate meaningful actions)\\\\\\\")\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--dry-run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip-counterfactual\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip-probing\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\n        \\\\\\\"--conditions\\\\\\\",\\\\n        default=\\\\\\\"trained,untrained\\\\\\\",\\\\n        help=\\\\\\\"Comma-separated: trained,untrained\\\\\\\",\\\\n    )\\\\n    args = p.parse_args()\\\\n\\\\n    conditions = [c.strip() for c in args.conditions.split(\\\\\\\",\\\\\\\")]\\\\n    log(f\\\\\\\"Pipeline conditions: {conditions}\\\\\\\")\\\\n\\\\n    t_start = time.time()\\\\n\\\\n    for condition in conditions:\\\\n        if condition == \\\\\\\"trained\\\\\\\":\\\\n            ckpt = TRAINED_CKPT\\\\n        elif condition == \\\\\\\"untrained\\\\\\\":\\\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\\\\\"config.json\\\\\\\")):\\\\n                ckpt = UNTRAINED_CACHE\\\\n            else:\\\\n                ckpt = UNTRAINED_CKPT\\\\n                log(f\\\\\\\"  Will download untrained model from {ckpt}\\\\\\\")\\\\n        else:\\\\n            log(f\\\\\\\"  Unknown condition: {condition}, skipping\\\\\\\")\\\\n            continue\\\\n\\\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\\\n\\\\n        try:\\\\n            model, processor = load_model(ckpt, condition)\\\\n        except Exception as e:\\\\n            log(f\\\\\\\"  ERROR loading {condition} model: {e}\\\\\\\")\\\\n            log(f\\\\\\\"  Skipping {condition} condition\\\\\\\")\\\\n            continue\\\\n\\\\n        tc = time.time()\\\\n        run_pipeline(model, processor, condition, results_dir, args)\\\\n        log(f\\\\\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\\\\\")\\\\n\\\\n        del model, processor\\\\n        torch.cuda.empty_cache()\\\\n\\\\n    log(f\\\\\\\"All done in {(time.time()-t_start)/60:.1f} min\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Spatial Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the black bowl between the plate and ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl from the center of the table and put it on the plate\\\",\\n    \\\"grab the black bowl next to the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl on the stove and put it on the plate\\\",\\n    \\\"grab the black bowl on the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl next to the plate and put it on the plate\\\",\\n    \\\"grab the black bowl next to the ramekin and put it on the plate\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef detect_image_token_id(processor):\\n    return -1\\n\\n\\ndef find_token_regions(input_ids, img_token_id):\\n    ids = input_ids[0].cpu().numpy()\\n    img_mask = ids < 0\\n    img_positions = np.where(img_mask)[0]\\n\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0\\n\\n... [截断: 输出过长，省略 16115 字符] ...\\n\\ninputs['image_sizes']}\\\")\\n\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n\\n    hs0_shape = out.hidden_states[0].shape\\n    log(f\\\"  hidden_states[0] shape: {hs0_shape}\\\")\\n\\n    tr = find_token_regions(original_ids, IMG_TOKEN_ID)\\n    N_IMG_TOKENS = tr[\\\"image\\\"][1] - tr[\\\"image\\\"][0]\\n    log(f\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\")\\n    log(f\\\"  N_IMG_TOKENS={N_IMG_TOKENS}\\\")\\n    log(f\\\"  Total seq_len: input_ids={inputs['input_ids'].shape[1]}, hidden={hs0_shape[1]}\\\")\\n\\n    n_attn_layers = len(out.attentions)\\n    attn_shape = out.attentions[0].shape\\n    log(f\\\"  Attention: {n_attn_layers} layers, shape={attn_shape}\\\")\\n\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, nt, nd, ns, IMG_TOKEN_ID\\n    )\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(results_dir, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(results_dir, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(os.path.join(results_dir, \\\"cross_instruction_classification.json\\\"), \\\"w\\\") as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if condition == \\\"trained\\\" and not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n        with open(os.path.join(results_dir, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n    elif condition != \\\"trained\\\":\\n        log(\\\"Phase 5: skipped (untrained model cannot generate meaningful actions)\\\")\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-probing\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\",\\n        default=\\\"trained,untrained\\\",\\n        help=\\\"Comma-separated: trained,untrained\\\",\\n    )\\n    args = p.parse_args()\\n\\n    conditions = [c.strip() for c in args.conditions.split(\\\",\\\")]\\n    log(f\\\"Pipeline conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\"config.json\\\")):\\n                ckpt = UNTRAINED_CACHE\\n            else:\\n                ckpt = UNTRAINED_CKPT\\n                log(f\\\"  Will download untrained model from {ckpt}\\\")\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n\\n        try:\\n            model, processor = load_model(ckpt, condition)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            log(f\\\"  Skipping {condition} condition\\\")\\n            continue\\n\\n        tc = time.time()\\n        run_pipeline(model, processor, condition, results_dir, args)\\n        log(f\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WhQpAsWTbHLxyQxRPNkQTT`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "291f3163-0766-4db1-8868-1701c523d0a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cz8HUVqfcc5ENLaMfDS4tC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 25500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MA9Su4VXGaRVR8XuycS7Bo`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "8d162c10-4ffd-4759-b637-c67bb9fa8851",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cz8HUVqfcc5ENLaMfDS4tC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 25500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 21 · 2026-05-21T05:03:47.474Z_

<details><summary>↩ Tool result · `toolu_01WhQpAsWTbHLxyQxRPNkQTT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_object\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef detect_image_token_id(processor):\\n    return -1\\n\\n\\ndef find_token_regions(input_ids, img_token_id):\\n    ids = input_ids[0].cpu().numpy()\\n    img_mask = ids < 0\\n    img_positions = np.where(img_mask)[0]\\n\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0])\\n        img_e = int(img_positions[-1]) + 1\\n    else:\\n        img_s = img_e = 1\\n\\n    txt_s = img_e\\n    txt_e = len(ids)\\n\\n    return {\\\"bos\\\": (0, img_s), \\\"image\\\": (img_s, img_e), \\\"text\\\": (txt_s, txt_e)}\\n\\n\\ndef generate_action_phi3v(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n          \\n\\n... [截断: 输出过长，省略 15714 字符] ...\\n\\ninputs['image_sizes']}\\\")\\n\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n\\n    hs0_shape = out.hidden_states[0].shape\\n    log(f\\\"  hidden_states[0] shape: {hs0_shape}\\\")\\n\\n    tr = find_token_regions(original_ids, IMG_TOKEN_ID)\\n    N_IMG_TOKENS = tr[\\\"image\\\"][1] - tr[\\\"image\\\"][0]\\n    log(f\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\")\\n    log(f\\\"  N_IMG_TOKENS={N_IMG_TOKENS}\\\")\\n    log(f\\\"  Total seq_len: input_ids={inputs['input_ids'].shape[1]}, hidden={hs0_shape[1]}\\\")\\n\\n    n_attn_layers = len(out.attentions)\\n    attn_shape = out.attentions[0].shape\\n    log(f\\\"  Attention: {n_attn_layers} layers, shape={attn_shape}\\\")\\n\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, nt, nd, ns, IMG_TOKEN_ID\\n    )\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(results_dir, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(results_dir, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(os.path.join(results_dir, \\\"cross_instruction_classification.json\\\"), \\\"w\\\") as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if condition == \\\"trained\\\" and not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n        with open(os.path.join(results_dir, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n    elif condition != \\\"trained\\\":\\n        log(\\\"Phase 5: skipped (untrained model cannot generate meaningful actions)\\\")\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-probing\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\",\\n        default=\\\"trained,untrained\\\",\\n        help=\\\"Comma-separated: trained,untrained\\\",\\n    )\\n    args = p.parse_args()\\n\\n    conditions = [c.strip() for c in args.conditions.split(\\\",\\\")]\\n    log(f\\\"Pipeline conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\"config.json\\\")):\\n                ckpt = UNTRAINED_CACHE\\n            else:\\n                ckpt = UNTRAINED_CKPT\\n                log(f\\\"  Will download untrained model from {ckpt}\\\")\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n\\n        try:\\n            model, processor = load_model(ckpt, condition)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            log(f\\\"  Skipping {condition} condition\\\")\\n            continue\\n\\n        tc = time.time()\\n        run_pipeline(model, processor, condition, results_dir, args)\\n        log(f\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "41b6e464-3e12-452f-a251-685a655627ca",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Object Full Analysis Pipeline for TracVLA-Phi3V\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"microsoft/Phi-3-vision-128k-instruct\\\\\\\"\\\\nUNTRAINED_CACHE = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/tracvla_object\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\\\n\\\\n# --- Architecture ---\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 3072\\\\nN_IMG_TOKENS = 0  # auto-detected\\\\nIMG_TOKEN_ID = -1  # auto-detected\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the alphabet soup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the bbq sauce and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the butter and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the chocolate pudding and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the cream cheese and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the ketchup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the milk and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the orange juice and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the salad dressing and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the tomato sauce and put it into the basket\\\\\\\",\\\\n]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return (\\\\n        f\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\"\\\\n    )\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef detect_image_token_id(processor):\\\\n    return -1\\\\n\\\\n\\\\ndef find_token_regions(input_ids, img_token_id):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    img_mask = ids < 0\\\\n    img_positions = np.where(img_mask)[0]\\\\n\\\\n    if len(img_positions) > 0:\\\\n        img_s = int(img_positions[0])\\\\n        img_e = int(img_positions[-1]) + 1\\\\n    else:\\\\n        img_s = img_e = 1\\\\n\\\\n    txt_s = img_e\\\\n    txt_e = len(ids)\\\\n\\\\n    return {\\\\\\\"bos\\\\\\\": (0, img_s), \\\\\\\"image\\\\\\\": (img_s, img_e), \\\\\\\"text\\\\\\\": (txt_s, txt_e)}\\\\n\\\\n\\\\ndef generate_action_phi3v(model, processor, instruction, image):\\\\n    inputs = prepare_inputs(processor, instruction, image)\\\\n\\\\n    with torch.no_grad():\\\\n        gen_ids = model.generate(\\\\n          \\\\n\\\\n... [截断: 输出过长，省略 15714 字符] ...\\\\n\\\\ninputs['image_sizes']}\\\\\\\")\\\\n\\\\n    with torch.no_grad():\\\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\\\n\\\\n    hs0_shape = out.hidden_states[0].shape\\\\n    log(f\\\\\\\"  hidden_states[0] shape: {hs0_shape}\\\\\\\")\\\\n\\\\n    tr = find_token_regions(original_ids, IMG_TOKEN_ID)\\\\n    N_IMG_TOKENS = tr[\\\\\\\"image\\\\\\\"][1] - tr[\\\\\\\"image\\\\\\\"][0]\\\\n    log(f\\\\\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\\\\\")\\\\n    log(f\\\\\\\"  N_IMG_TOKENS={N_IMG_TOKENS}\\\\\\\")\\\\n    log(f\\\\\\\"  Total seq_len: input_ids={inputs['input_ids'].shape[1]}, hidden={hs0_shape[1]}\\\\\\\")\\\\n\\\\n    n_attn_layers = len(out.attentions)\\\\n    attn_shape = out.attentions[0].shape\\\\n    log(f\\\\\\\"  Attention: {n_attn_layers} layers, shape={attn_shape}\\\\\\\")\\\\n\\\\n    del out, inputs\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\\\n        model, processor, nt, nd, ns, IMG_TOKEN_ID\\\\n    )\\\\n    log(f\\\\\\\"Phase 1: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    if not args.skip_probing:\\\\n        t2 = time.time()\\\\n        probe_res = run_probing(reps, actions, nps)\\\\n        with open(os.path.join(results_dir, \\\\\\\"action_r2_probing.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(probe_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\\\\\")\\\\n\\\\n    t3 = time.time()\\\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\\\n    with open(os.path.join(results_dir, \\\\\\\"l1_attention_profile.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(attn_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\\\\\")\\\\n\\\\n    del l1_attns, tok_regs\\\\n\\\\n    t4 = time.time()\\\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\\\n    with open(os.path.join(results_dir, \\\\\\\"cross_instruction_classification.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(cls_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\\\\\")\\\\n\\\\n    del reps, actions, labels\\\\n\\\\n    if condition == \\\\\\\"trained\\\\\\\" and not args.skip_counterfactual:\\\\n        t5 = time.time()\\\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\\\n        with open(os.path.join(results_dir, \\\\\\\"counterfactual_combined.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(cf_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\\\\\")\\\\n    elif condition != \\\\\\\"trained\\\\\\\":\\\\n        log(\\\\\\\"Phase 5: skipped (untrained model cannot generate meaningful actions)\\\\\\\")\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--dry-run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip-counterfactual\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip-probing\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\n        \\\\\\\"--conditions\\\\\\\",\\\\n        default=\\\\\\\"trained,untrained\\\\\\\",\\\\n        help=\\\\\\\"Comma-separated: trained,untrained\\\\\\\",\\\\n    )\\\\n    args = p.parse_args()\\\\n\\\\n    conditions = [c.strip() for c in args.conditions.split(\\\\\\\",\\\\\\\")]\\\\n    log(f\\\\\\\"Pipeline conditions: {conditions}\\\\\\\")\\\\n\\\\n    t_start = time.time()\\\\n\\\\n    for condition in conditions:\\\\n        if condition == \\\\\\\"trained\\\\\\\":\\\\n            ckpt = TRAINED_CKPT\\\\n        elif condition == \\\\\\\"untrained\\\\\\\":\\\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\\\\\"config.json\\\\\\\")):\\\\n                ckpt = UNTRAINED_CACHE\\\\n            else:\\\\n                ckpt = UNTRAINED_CKPT\\\\n                log(f\\\\\\\"  Will download untrained model from {ckpt}\\\\\\\")\\\\n        else:\\\\n            log(f\\\\\\\"  Unknown condition: {condition}, skipping\\\\\\\")\\\\n            continue\\\\n\\\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\\\n\\\\n        try:\\\\n            model, processor = load_model(ckpt, condition)\\\\n        except Exception as e:\\\\n            log(f\\\\\\\"  ERROR loading {condition} model: {e}\\\\\\\")\\\\n            log(f\\\\\\\"  Skipping {condition} condition\\\\\\\")\\\\n            continue\\\\n\\\\n        tc = time.time()\\\\n        run_pipeline(model, processor, condition, results_dir, args)\\\\n        log(f\\\\\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\\\\\")\\\\n\\\\n        del model, processor\\\\n        torch.cuda.empty_cache()\\\\n\\\\n    log(f\\\\\\\"All done in {(time.time()-t_start)/60:.1f} min\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_object\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef detect_image_token_id(processor):\\n    return -1\\n\\n\\ndef find_token_regions(input_ids, img_token_id):\\n    ids = input_ids[0].cpu().numpy()\\n    img_mask = ids < 0\\n    img_positions = np.where(img_mask)[0]\\n\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0])\\n        img_e = int(img_positions[-1]) + 1\\n    else:\\n        img_s = img_e = 1\\n\\n    txt_s = img_e\\n    txt_e = len(ids)\\n\\n    return {\\\"bos\\\": (0, img_s), \\\"image\\\": (img_s, img_e), \\\"text\\\": (txt_s, txt_e)}\\n\\n\\ndef generate_action_phi3v(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n          \\n\\n... [截断: 输出过长，省略 15714 字符] ...\\n\\ninputs['image_sizes']}\\\")\\n\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n\\n    hs0_shape = out.hidden_states[0].shape\\n    log(f\\\"  hidden_states[0] shape: {hs0_shape}\\\")\\n\\n    tr = find_token_regions(original_ids, IMG_TOKEN_ID)\\n    N_IMG_TOKENS = tr[\\\"image\\\"][1] - tr[\\\"image\\\"][0]\\n    log(f\\\"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}\\\")\\n    log(f\\\"  N_IMG_TOKENS={N_IMG_TOKENS}\\\")\\n    log(f\\\"  Total seq_len: input_ids={inputs['input_ids'].shape[1]}, hidden={hs0_shape[1]}\\\")\\n\\n    n_attn_layers = len(out.attentions)\\n    attn_shape = out.attentions[0].shape\\n    log(f\\\"  Attention: {n_attn_layers} layers, shape={attn_shape}\\\")\\n\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, nt, nd, ns, IMG_TOKEN_ID\\n    )\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(results_dir, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(results_dir, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(os.path.join(results_dir, \\\"cross_instruction_classification.json\\\"), \\\"w\\\") as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if condition == \\\"trained\\\" and not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n        with open(os.path.join(results_dir, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n    elif condition != \\\"trained\\\":\\n        log(\\\"Phase 5: skipped (untrained model cannot generate meaningful actions)\\\")\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-counterfactual\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\\"--skip-probing\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\",\\n        default=\\\"trained,untrained\\\",\\n        help=\\\"Comma-separated: trained,untrained\\\",\\n    )\\n    args = p.parse_args()\\n\\n    conditions = [c.strip() for c in args.conditions.split(\\\",\\\")]\\n    log(f\\\"Pipeline conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\"config.json\\\")):\\n                ckpt = UNTRAINED_CACHE\\n            else:\\n                ckpt = UNTRAINED_CKPT\\n                log(f\\\"  Will download untrained model from {ckpt}\\\")\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n\\n        try:\\n            model, processor = load_model(ckpt, condition)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            log(f\\\"  Skipping {condition} condition\\\")\\n            continue\\n\\n        tc = time.time()\\n        run_pipeline(model, processor, condition, results_dir, args)\\n        log(f\\\"  {condition} complete in {(time.time()-tc)/60:.1f} min\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T05:03:47.992Z_

<details><summary>↩ Tool result · `toolu_01MA9Su4VXGaRVR8XuycS7Bo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Long Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_long\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_10\\\"\\n\\nTASKS = [\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\",\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\",\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\",\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\",\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\",\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\",\\n]\\nINSTRUCTIONS = [\\n    \\\"turn on the stove and put the moka pot on it\\\",\\n    \\\"put the black bowl in the bottom drawer of the cabinet and close it\\\",\\n    \\\"put the yellow and white mug in the microwave and close it\\\",\\n    \\\"put both moka pots on the stove\\\",\\n    \\\"put both the alphabet soup and the cream cheese box in the basket\\\",\\n    \\\"put both the alphabet soup and the tomato sauce in the basket\\\",\\n    \\\"put both the cream cheese box and the butter in the basket\\\",\\n    \\\"put the white mug on the left plate and put the yellow and white mug on the right plate\\\",\\n    \\\"put the white mug on the plate and put the chocolate pudding to the right of the plate\\\",\\n    \\\"pick up the book and place it in the back compartment of the caddy\\\",\\n]\\nPARAPHRASES = [\\n    \\\"switch on the stove and place the moka pot on it\\\",\\n    \\\"place the black bowl in the bottom drawer of the cabinet and shut it\\\",\\n    \\\"place the yellow and white mug in the microwave and shut it\\\",\\n    \\\"put both of the moka pots on the stove\\\",\\n    \\\"place the alphabet soup and cream cheese box into the basket\\\",\\n    \\\"place the alphabet soup and tomato sauce into the basket\\\",\\n    \\\"place the cream cheese box and butter into the basket\\\",\\n    \\\"place the white mug on the left plate and the yellow white mug on the right plate\\\",\\n    \\\"place the white mug on the plate and the chocolate pudding to the right of the plate\\\",\\n    \\\"grab the book and put it in the back section of the caddy\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef g\\n\\n... [截断: 输出过长，省略 17349 字符] ...\\n\\nULTS_DIR, exist_ok=True)\\n\\n    nt = 2 if args.dry_run else len(TASKS)\\n    nd = 1 if args.dry_run else N_DEMOS\\n    ns = 2 if args.dry_run else N_TIMESTEPS\\n    nps = 2 if args.dry_run else N_PROBE_SEEDS\\n    cls_layers = [0, 8, 16, 24, 31] if args.dry_run else None\\n\\n    log(f\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\")\\n    log(f\\\"Output: {RESULTS_DIR}\\\")\\n\\n    log(\\\"Loading model ...\\\")\\n    t0 = time.time()\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True\\n    ).to(DEVICE).eval()\\n    import importlib.util, sys\\n    spec = importlib.util.spec_from_file_location('processing_prismatic', os.path.join(CKPT, 'processing_prismatic.py'))\\n    mod = importlib.util.module_from_spec(spec)\\n    sys.modules['processing_prismatic'] = mod\\n    spec.loader.exec_module(mod)\\n    processor = mod.PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)\\n    log(f\\\"Model loaded in {time.time()-t0:.1f}s\\\")\\n\\n    log(\\\"Validating token layout ...\\\")\\n    hdf5_path = os.path.join(DATA, f\\\"{TASKS[0]}_demo.hdf5\\\")\\n    with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n        img = Image.fromarray(hf[\\\"data/demo_0/obs/agentview_rgb\\\"][0])\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\n    log(f\\\"  input_ids shape: {inputs['input_ids'].shape}\\\")\\n    log(f\\\"  pixel_values shape: {inputs['pixel_values'].shape}\\\")\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n    hs0_shape = out.hidden_states[0].shape\\n    log(f\\\"  hidden_states[0] shape: {hs0_shape}\\\")\\n    expected_seq = inputs[\\\"input_ids\\\"].shape[1] + N_IMG_TOKENS\\n    actual_seq = hs0_shape[1]\\n    if actual_seq != expected_seq:\\n        log(f\\\"  WARNING: seq len mismatch: expected {expected_seq}, got {actual_seq}\\\")\\n        log(f\\\"  Adjusting N_IMG_TOKENS from {N_IMG_TOKENS} to {actual_seq - inputs['input_ids'].shape[1]}\\\")\\n        N_IMG_TOKENS = actual_seq - inputs[\\\"input_ids\\\"].shape[1]\\n    log(f\\\"  Token layout: BOS(1) + img({N_IMG_TOKENS}) + text({inputs['input_ids'].shape[1]-1})\\\")\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, nt, nd, ns)\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(RESULTS_DIR, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(RESULTS_DIR, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(os.path.join(RESULTS_DIR, \\\"cross_instruction_classification.json\\\"), \\\"w\\\") as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n\\n    if not args.skip_rsa:\\n        t_rsa = time.time()\\n        rsa_res = run_rsa(reps, actions, labels)\\n        with open(os.path.join(RESULTS_DIR, \\\"rsa_analysis.json\\\"), \\\"w\\\") as f:\\n            json.dump(rsa_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t_rsa:.1f}s -> rsa_analysis.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n        with open(os.path.join(RESULTS_DIR, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 6: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n\\n    total_t = time.time() - t0\\n    log(f\\\"Pipeline complete in {total_t/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "78496979-f3f8-4bf6-b38f-9de5e66d47d1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Long Full Analysis Pipeline (Streaming)\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. RSA: representational similarity across conditions\\\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nAll results -> RESULTS_DIR/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\\\n\\\\nCKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\\\\\"\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\\\\\"\\\\nRESULTS_DIR = \\\\\\\"/root/autodl-tmp/vla-ssd/results/libero_long\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\nUNNORM = \\\\\\\"libero_10\\\\\\\"\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\\\\\",\\\\n    \\\\\\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\\\\\",\\\\n    \\\\\\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\\\\\",\\\\n    \\\\\\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\\\\\",\\\\n    \\\\\\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [\\\\n    \\\\\\\"turn on the stove and put the moka pot on it\\\\\\\",\\\\n    \\\\\\\"put the black bowl in the bottom drawer of the cabinet and close it\\\\\\\",\\\\n    \\\\\\\"put the yellow and white mug in the microwave and close it\\\\\\\",\\\\n    \\\\\\\"put both moka pots on the stove\\\\\\\",\\\\n    \\\\\\\"put both the alphabet soup and the cream cheese box in the basket\\\\\\\",\\\\n    \\\\\\\"put both the alphabet soup and the tomato sauce in the basket\\\\\\\",\\\\n    \\\\\\\"put both the cream cheese box and the butter in the basket\\\\\\\",\\\\n    \\\\\\\"put the white mug on the left plate and put the yellow and white mug on the right plate\\\\\\\",\\\\n    \\\\\\\"put the white mug on the plate and put the chocolate pudding to the right of the plate\\\\\\\",\\\\n    \\\\\\\"pick up the book and place it in the back compartment of the caddy\\\\\\\",\\\\n]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"switch on the stove and place the moka pot on it\\\\\\\",\\\\n    \\\\\\\"place the black bowl in the bottom drawer of the cabinet and shut it\\\\\\\",\\\\n    \\\\\\\"place the yellow and white mug in the microwave and shut it\\\\\\\",\\\\n    \\\\\\\"put both of the moka pots on the stove\\\\\\\",\\\\n    \\\\\\\"place the alphabet soup and cream cheese box into the basket\\\\\\\",\\\\n    \\\\\\\"place the alphabet soup and tomato sauce into the basket\\\\\\\",\\\\n    \\\\\\\"place the cream cheese box and butter into the basket\\\\\\\",\\\\n    \\\\\\\"place the white mug on the left plate and the yellow white mug on the right plate\\\\\\\",\\\\n    \\\\\\\"place the white mug on the plate and the chocolate pudding to the right of the plate\\\\\\\",\\\\n    \\\\\\\"grab the book and put it in the back section of the caddy\\\\\\\",\\\\n]\\\\n\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 4096\\\\nN_IMG_TOKENS = 256\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, image).to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef g\\\\n\\\\n... [截断: 输出过长，省略 17349 字符] ...\\\\n\\\\nULTS_DIR, exist_ok=True)\\\\n\\\\n    nt = 2 if args.dry_run else len(TASKS)\\\\n    nd = 1 if args.dry_run else N_DEMOS\\\\n    ns = 2 if args.dry_run else N_TIMESTEPS\\\\n    nps = 2 if args.dry_run else N_PROBE_SEEDS\\\\n    cls_layers = [0, 8, 16, 24, 31] if args.dry_run else None\\\\n\\\\n    log(f\\\\\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\\\\\")\\\\n    log(f\\\\\\\"Output: {RESULTS_DIR}\\\\\\\")\\\\n\\\\n    log(\\\\\\\"Loading model ...\\\\\\\")\\\\n    t0 = time.time()\\\\n    model = AutoModelForVision2Seq.from_pretrained(\\\\n        CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True\\\\n    ).to(DEVICE).eval()\\\\n    import importlib.util, sys\\\\n    spec = importlib.util.spec_from_file_location('processing_prismatic', os.path.join(CKPT, 'processing_prismatic.py'))\\\\n    mod = importlib.util.module_from_spec(spec)\\\\n    sys.modules['processing_prismatic'] = mod\\\\n    spec.loader.exec_module(mod)\\\\n    processor = mod.PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)\\\\n    log(f\\\\\\\"Model loaded in {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n    log(\\\\\\\"Validating token layout ...\\\\\\\")\\\\n    hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[0]}_demo.hdf5\\\\\\\")\\\\n    with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n        img = Image.fromarray(hf[\\\\\\\"data/demo_0/obs/agentview_rgb\\\\\\\"][0])\\\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\\\n    log(f\\\\\\\"  input_ids shape: {inputs['input_ids'].shape}\\\\\\\")\\\\n    log(f\\\\\\\"  pixel_values shape: {inputs['pixel_values'].shape}\\\\\\\")\\\\n    with torch.no_grad():\\\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\\\n    hs0_shape = out.hidden_states[0].shape\\\\n    log(f\\\\\\\"  hidden_states[0] shape: {hs0_shape}\\\\\\\")\\\\n    expected_seq = inputs[\\\\\\\"input_ids\\\\\\\"].shape[1] + N_IMG_TOKENS\\\\n    actual_seq = hs0_shape[1]\\\\n    if actual_seq != expected_seq:\\\\n        log(f\\\\\\\"  WARNING: seq len mismatch: expected {expected_seq}, got {actual_seq}\\\\\\\")\\\\n        log(f\\\\\\\"  Adjusting N_IMG_TOKENS from {N_IMG_TOKENS} to {actual_seq - inputs['input_ids'].shape[1]}\\\\\\\")\\\\n        N_IMG_TOKENS = actual_seq - inputs[\\\\\\\"input_ids\\\\\\\"].shape[1]\\\\n    log(f\\\\\\\"  Token layout: BOS(1) + img({N_IMG_TOKENS}) + text({inputs['input_ids'].shape[1]-1})\\\\\\\")\\\\n    del out, inputs\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\\\n        model, processor, nt, nd, ns)\\\\n    log(f\\\\\\\"Phase 1: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    if not args.skip_probing:\\\\n        t2 = time.time()\\\\n        probe_res = run_probing(reps, actions, nps)\\\\n        with open(os.path.join(RESULTS_DIR, \\\\\\\"action_r2_probing.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(probe_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\\\\\")\\\\n\\\\n    t3 = time.time()\\\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\\\n    with open(os.path.join(RESULTS_DIR, \\\\\\\"l1_attention_profile.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(attn_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\\\\\")\\\\n\\\\n    del l1_attns, tok_regs\\\\n\\\\n    t4 = time.time()\\\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\\\n    with open(os.path.join(RESULTS_DIR, \\\\\\\"cross_instruction_classification.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(cls_res, f, indent=2)\\\\n    log(f\\\\\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\\\\\")\\\\n\\\\n\\\\n    if not args.skip_rsa:\\\\n        t_rsa = time.time()\\\\n        rsa_res = run_rsa(reps, actions, labels)\\\\n        with open(os.path.join(RESULTS_DIR, \\\\\\\"rsa_analysis.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(rsa_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 5: {time.time()-t_rsa:.1f}s -> rsa_analysis.json\\\\\\\")\\\\n\\\\n    del reps, actions, labels\\\\n\\\\n    if not args.skip_counterfactual:\\\\n        t5 = time.time()\\\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\\\n        with open(os.path.join(RESULTS_DIR, \\\\\\\"counterfactual_combined.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(cf_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 6: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\\\\\")\\\\n\\\\n    total_t = time.time() - t0\\\\n    log(f\\\\\\\"Pipeline complete in {total_t/60:.1f} min\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Long Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_long\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_10\\\"\\n\\nTASKS = [\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\",\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\",\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\",\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\",\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\",\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\",\\n]\\nINSTRUCTIONS = [\\n    \\\"turn on the stove and put the moka pot on it\\\",\\n    \\\"put the black bowl in the bottom drawer of the cabinet and close it\\\",\\n    \\\"put the yellow and white mug in the microwave and close it\\\",\\n    \\\"put both moka pots on the stove\\\",\\n    \\\"put both the alphabet soup and the cream cheese box in the basket\\\",\\n    \\\"put both the alphabet soup and the tomato sauce in the basket\\\",\\n    \\\"put both the cream cheese box and the butter in the basket\\\",\\n    \\\"put the white mug on the left plate and put the yellow and white mug on the right plate\\\",\\n    \\\"put the white mug on the plate and put the chocolate pudding to the right of the plate\\\",\\n    \\\"pick up the book and place it in the back compartment of the caddy\\\",\\n]\\nPARAPHRASES = [\\n    \\\"switch on the stove and place the moka pot on it\\\",\\n    \\\"place the black bowl in the bottom drawer of the cabinet and shut it\\\",\\n    \\\"place the yellow and white mug in the microwave and shut it\\\",\\n    \\\"put both of the moka pots on the stove\\\",\\n    \\\"place the alphabet soup and cream cheese box into the basket\\\",\\n    \\\"place the alphabet soup and tomato sauce into the basket\\\",\\n    \\\"place the cream cheese box and butter into the basket\\\",\\n    \\\"place the white mug on the left plate and the yellow white mug on the right plate\\\",\\n    \\\"place the white mug on the plate and the chocolate pudding to the right of the plate\\\",\\n    \\\"grab the book and put it in the back section of the caddy\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef g\\n\\n... [截断: 输出过长，省略 17349 字符] ...\\n\\nULTS_DIR, exist_ok=True)\\n\\n    nt = 2 if args.dry_run else len(TASKS)\\n    nd = 1 if args.dry_run else N_DEMOS\\n    ns = 2 if args.dry_run else N_TIMESTEPS\\n    nps = 2 if args.dry_run else N_PROBE_SEEDS\\n    cls_layers = [0, 8, 16, 24, 31] if args.dry_run else None\\n\\n    log(f\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\")\\n    log(f\\\"Output: {RESULTS_DIR}\\\")\\n\\n    log(\\\"Loading model ...\\\")\\n    t0 = time.time()\\n    model = AutoModelForVision2Seq.from_pretrained(\\n        CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True\\n    ).to(DEVICE).eval()\\n    import importlib.util, sys\\n    spec = importlib.util.spec_from_file_location('processing_prismatic', os.path.join(CKPT, 'processing_prismatic.py'))\\n    mod = importlib.util.module_from_spec(spec)\\n    sys.modules['processing_prismatic'] = mod\\n    spec.loader.exec_module(mod)\\n    processor = mod.PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)\\n    log(f\\\"Model loaded in {time.time()-t0:.1f}s\\\")\\n\\n    log(\\\"Validating token layout ...\\\")\\n    hdf5_path = os.path.join(DATA, f\\\"{TASKS[0]}_demo.hdf5\\\")\\n    with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n        img = Image.fromarray(hf[\\\"data/demo_0/obs/agentview_rgb\\\"][0])\\n    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)\\n    log(f\\\"  input_ids shape: {inputs['input_ids'].shape}\\\")\\n    log(f\\\"  pixel_values shape: {inputs['pixel_values'].shape}\\\")\\n    with torch.no_grad():\\n        out = model(**inputs, output_hidden_states=True, output_attentions=True)\\n    hs0_shape = out.hidden_states[0].shape\\n    log(f\\\"  hidden_states[0] shape: {hs0_shape}\\\")\\n    expected_seq = inputs[\\\"input_ids\\\"].shape[1] + N_IMG_TOKENS\\n    actual_seq = hs0_shape[1]\\n    if actual_seq != expected_seq:\\n        log(f\\\"  WARNING: seq len mismatch: expected {expected_seq}, got {actual_seq}\\\")\\n        log(f\\\"  Adjusting N_IMG_TOKENS from {N_IMG_TOKENS} to {actual_seq - inputs['input_ids'].shape[1]}\\\")\\n        N_IMG_TOKENS = actual_seq - inputs[\\\"input_ids\\\"].shape[1]\\n    log(f\\\"  Token layout: BOS(1) + img({N_IMG_TOKENS}) + text({inputs['input_ids'].shape[1]-1})\\\")\\n    del out, inputs\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    reps, actions, labels, l1_attns, tok_regs = extract_features(\\n        model, processor, nt, nd, ns)\\n    log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n    if not args.skip_probing:\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        with open(os.path.join(RESULTS_DIR, \\\"action_r2_probing.json\\\"), \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json\\\")\\n\\n    t3 = time.time()\\n    attn_res = analyze_attention(l1_attns, tok_regs)\\n    with open(os.path.join(RESULTS_DIR, \\\"l1_attention_profile.json\\\"), \\\"w\\\") as f:\\n        json.dump(attn_res, f, indent=2)\\n    log(f\\\"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json\\\")\\n\\n    del l1_attns, tok_regs\\n\\n    t4 = time.time()\\n    cls_res = run_classification(reps, labels, layers=cls_layers)\\n    with open(os.path.join(RESULTS_DIR, \\\"cross_instruction_classification.json\\\"), \\\"w\\\") as f:\\n        json.dump(cls_res, f, indent=2)\\n    log(f\\\"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json\\\")\\n\\n\\n    if not args.skip_rsa:\\n        t_rsa = time.time()\\n        rsa_res = run_rsa(reps, actions, labels)\\n        with open(os.path.join(RESULTS_DIR, \\\"rsa_analysis.json\\\"), \\\"w\\\") as f:\\n            json.dump(rsa_res, f, indent=2)\\n        log(f\\\"Phase 5: {time.time()-t_rsa:.1f}s -> rsa_analysis.json\\\")\\n\\n    del reps, actions, labels\\n\\n    if not args.skip_counterfactual:\\n        t5 = time.time()\\n        cf_res = run_counterfactual(model, processor, nt, nd, ns)\\n        with open(os.path.join(RESULTS_DIR, \\\"counterfactual_combined.json\\\"), \\\"w\\\") as f:\\n            json.dump(cf_res, f, indent=2)\\n        log(f\\\"Phase 6: {time.time()-t5:.1f}s -> counterfactual_combined.json\\\")\\n\\n    total_t = time.time() - t0\\n    log(f\\\"Pipeline complete in {total_t/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Morf4ZFJTaHKBxiFhyzL22`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "b3b83a1c-b8e2-47c3-b351-b25b5507fd24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cz8HUVqfcc5ENLaMfDS4tC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 25500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 400
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

_source line 24 · 2026-05-21T05:03:48.517Z_

<details><summary>↩ Tool result · `toolu_01Morf4ZFJTaHKBxiFhyzL22`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nTraceVLA-Spatial R² probing-only补跑脚本\\n\\n只跑 Phase 1 (feature extraction) + Phase 2 (R² probing)。\\n跳过 L1 attention / cross-instruction classification / counterfactual。\\n输出: RESULTS_DIR/{condition}/action_r2_probing.json\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, time\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nHIDDEN = 3072\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef find_token_regions(input_ids):\\n    ids = input_ids[0].cpu().numpy()\\n    img_positions = np.where(ids < 0)[0]\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0])\\n        img_e = int(img_positions[-1]) + 1\\n    else:\\n        img_s = img_e = 1\\n    return {\\\"bos\\\": (0, img_s), \\\"image\\\": (img_s, img_e), \\\"text\\\": (img_e, len(ids))}\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction (probing only)\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti][:60]}...\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    original_ids = inputs[\\\"input_ids\\\"].clone()\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                   \\n\\n... [截断: 输出过长，省略 1354 字符] ...\\n\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 4 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef load_model(ckpt_path, condition):\\n    log(f\\\"Loading {condition} model from {ckpt_path} ...\\\")\\n    t0 = time.time()\\n    model = AutoModelForCausalLM.from_pretrained(\\n        ckpt_path,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        attn_implementation=\\\"eager\\\",\\n    ).to(DEVICE).eval()\\n    processor = AutoProcessor.from_pretrained(\\n        ckpt_path, trust_remote_code=True, num_crops=1\\n    )\\n    log(f\\\"  Model loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser(description=\\\"TraceVLA-Spatial R² probing only\\\")\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\", default=\\\"trained\\\",\\n        help=\\\"Comma-separated: trained,untrained (default: trained)\\\",\\n    )\\n    args = p.parse_args()\\n\\n    conditions = [c.strip() for c in args.conditions.split(\\\",\\\")]\\n    log(f\\\"Probing-only pipeline, conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\"config.json\\\")):\\n                ckpt = UNTRAINED_CACHE\\n            else:\\n                ckpt = UNTRAINED_CKPT\\n                log(f\\\"  Will download untrained model from {ckpt}\\\")\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n        os.makedirs(results_dir, exist_ok=True)\\n\\n        nt = 2 if args.dry_run else len(TASKS)\\n        nd = 1 if args.dry_run else N_DEMOS\\n        ns = 2 if args.dry_run else N_TIMESTEPS\\n        nps = 2 if args.dry_run else N_PROBE_SEEDS\\n\\n        log(f\\\"=== {condition.upper()} probing ===\\\")\\n        log(f\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\")\\n        log(f\\\"Output: {results_dir}\\\")\\n\\n        try:\\n            model, processor = load_model(ckpt, condition)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            continue\\n\\n        t1 = time.time()\\n        reps, actions = extract_features(model, processor, nt, nd, ns)\\n        log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        out_path = os.path.join(results_dir, \\\"action_r2_probing.json\\\")\\n        with open(out_path, \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> {out_path}\\\")\\n\\n        del reps, actions\\n\\n        log(f\\\"  {condition} complete in {(time.time()-t1)/60:.1f} min\\\")\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "d2719725-9d32-420a-beea-165a1cfb59c4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nTraceVLA-Spatial R² probing-only补跑脚本\\\\n\\\\n只跑 Phase 1 (feature extraction) + Phase 2 (R² probing)。\\\\n跳过 L1 attention / cross-instruction classification / counterfactual。\\\\n输出: RESULTS_DIR/{condition}/action_r2_probing.json\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, time\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"microsoft/Phi-3-vision-128k-instruct\\\\\\\"\\\\nUNTRAINED_CACHE = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\n\\\\n# --- Architecture ---\\\\nN_LAYERS = 32\\\\nHIDDEN = 3072\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return (\\\\n        f\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\"\\\\n    )\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef find_token_regions(input_ids):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    img_positions = np.where(ids < 0)[0]\\\\n    if len(img_positions) > 0:\\\\n        img_s = int(img_positions[0])\\\\n        img_e = int(img_positions[-1]) + 1\\\\n    else:\\\\n        img_s = img_e = 1\\\\n    return {\\\\\\\"bos\\\\\\\": (0, img_s), \\\\\\\"image\\\\\\\": (img_s, img_e), \\\\\\\"text\\\\\\\": (img_e, len(ids))}\\\\n\\\\n\\\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\\\n    log(\\\\\\\"Phase 1: representation extraction (probing only)\\\\\\\")\\\\n    total = n_tasks * n_demos * n_timesteps\\\\n\\\\n    reps = {\\\\n        l: {\\\\n            \\\\\\\"image_mean\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n            \\\\\\\"last_preaction\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n        }\\\\n        for l in range(N_LAYERS)\\\\n    }\\\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti][:60]}...\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    original_ids = inputs[\\\\\\\"input_ids\\\\\\\"].clone()\\\\n                    with torch.no_grad():\\\\n                        out = model(\\\\n                            **inputs,\\\\n                   \\\\n\\\\n... [截断: 输出过长，省略 1354 字符] ...\\\\n\\\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n                use_es = len(Xtr) >= 10\\\\n                probe = MLPRegressor(\\\\n                    hidden_layer_sizes=(256,),\\\\n                    max_iter=200,\\\\n                    early_stopping=use_es,\\\\n                    validation_fraction=0.2 if use_es else 0.1,\\\\n                    random_state=s,\\\\n                    n_iter_no_change=10,\\\\n                )\\\\n                probe.fit(Xtr, ytr)\\\\n                pred = probe.predict(Xv)\\\\n                ss_res = np.sum((yv - pred) ** 2)\\\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(r2s)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(r2s)), 4),\\\\n                \\\\\\\"values\\\\\\\": [round(v, 4) for v in r2s],\\\\n            }\\\\n        if l % 4 == 0:\\\\n            log(\\\\n                f\\\\\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\\\\\"\\\\n            )\\\\n    return results\\\\n\\\\n\\\\ndef load_model(ckpt_path, condition):\\\\n    log(f\\\\\\\"Loading {condition} model from {ckpt_path} ...\\\\\\\")\\\\n    t0 = time.time()\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        ckpt_path,\\\\n        torch_dtype=torch.bfloat16,\\\\n        trust_remote_code=True,\\\\n        attn_implementation=\\\\\\\"eager\\\\\\\",\\\\n    ).to(DEVICE).eval()\\\\n    processor = AutoProcessor.from_pretrained(\\\\n        ckpt_path, trust_remote_code=True, num_crops=1\\\\n    )\\\\n    log(f\\\\\\\"  Model loaded in {time.time()-t0:.1f}s\\\\\\\")\\\\n    return model, processor\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"TraceVLA-Spatial R² probing only\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--dry-run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    p.add_argument(\\\\n        \\\\\\\"--conditions\\\\\\\", default=\\\\\\\"trained\\\\\\\",\\\\n        help=\\\\\\\"Comma-separated: trained,untrained (default: trained)\\\\\\\",\\\\n    )\\\\n    args = p.parse_args()\\\\n\\\\n    conditions = [c.strip() for c in args.conditions.split(\\\\\\\",\\\\\\\")]\\\\n    log(f\\\\\\\"Probing-only pipeline, conditions: {conditions}\\\\\\\")\\\\n\\\\n    t_start = time.time()\\\\n\\\\n    for condition in conditions:\\\\n        if condition == \\\\\\\"trained\\\\\\\":\\\\n            ckpt = TRAINED_CKPT\\\\n        elif condition == \\\\\\\"untrained\\\\\\\":\\\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\\\\\"config.json\\\\\\\")):\\\\n                ckpt = UNTRAINED_CACHE\\\\n            else:\\\\n                ckpt = UNTRAINED_CKPT\\\\n                log(f\\\\\\\"  Will download untrained model from {ckpt}\\\\\\\")\\\\n        else:\\\\n            log(f\\\\\\\"  Unknown condition: {condition}, skipping\\\\\\\")\\\\n            continue\\\\n\\\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\\\n        os.makedirs(results_dir, exist_ok=True)\\\\n\\\\n        nt = 2 if args.dry_run else len(TASKS)\\\\n        nd = 1 if args.dry_run else N_DEMOS\\\\n        ns = 2 if args.dry_run else N_TIMESTEPS\\\\n        nps = 2 if args.dry_run else N_PROBE_SEEDS\\\\n\\\\n        log(f\\\\\\\"=== {condition.upper()} probing ===\\\\\\\")\\\\n        log(f\\\\\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\\\\\")\\\\n        log(f\\\\\\\"Output: {results_dir}\\\\\\\")\\\\n\\\\n        try:\\\\n            model, processor = load_model(ckpt, condition)\\\\n        except Exception as e:\\\\n            log(f\\\\\\\"  ERROR loading {condition} model: {e}\\\\\\\")\\\\n            continue\\\\n\\\\n        t1 = time.time()\\\\n        reps, actions = extract_features(model, processor, nt, nd, ns)\\\\n        log(f\\\\\\\"Phase 1: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n        del model, processor\\\\n        torch.cuda.empty_cache()\\\\n\\\\n        t2 = time.time()\\\\n        probe_res = run_probing(reps, actions, nps)\\\\n        out_path = os.path.join(results_dir, \\\\\\\"action_r2_probing.json\\\\\\\")\\\\n        with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(probe_res, f, indent=2)\\\\n        log(f\\\\\\\"Phase 2: {time.time()-t2:.1f}s -> {out_path}\\\\\\\")\\\\n\\\\n        del reps, actions\\\\n\\\\n        log(f\\\\\\\"  {condition} complete in {(time.time()-t1)/60:.1f} min\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"All done in {(time.time()-t_start)/60:.1f} min\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nTraceVLA-Spatial R² probing-only补跑脚本\\n\\n只跑 Phase 1 (feature extraction) + Phase 2 (R² probing)。\\n跳过 L1 attention / cross-instruction classification / counterfactual。\\n输出: RESULTS_DIR/{condition}/action_r2_probing.json\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, time\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nHIDDEN = 3072\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef find_token_regions(input_ids):\\n    ids = input_ids[0].cpu().numpy()\\n    img_positions = np.where(ids < 0)[0]\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0])\\n        img_e = int(img_positions[-1]) + 1\\n    else:\\n        img_s = img_e = 1\\n    return {\\\"bos\\\": (0, img_s), \\\"image\\\": (img_s, img_e), \\\"text\\\": (img_e, len(ids))}\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction (probing only)\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti][:60]}...\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    original_ids = inputs[\\\"input_ids\\\"].clone()\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                   \\n\\n... [截断: 输出过长，省略 1354 字符] ...\\n\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 4 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef load_model(ckpt_path, condition):\\n    log(f\\\"Loading {condition} model from {ckpt_path} ...\\\")\\n    t0 = time.time()\\n    model = AutoModelForCausalLM.from_pretrained(\\n        ckpt_path,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        attn_implementation=\\\"eager\\\",\\n    ).to(DEVICE).eval()\\n    processor = AutoProcessor.from_pretrained(\\n        ckpt_path, trust_remote_code=True, num_crops=1\\n    )\\n    log(f\\\"  Model loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser(description=\\\"TraceVLA-Spatial R² probing only\\\")\\n    p.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\")\\n    p.add_argument(\\n        \\\"--conditions\\\", default=\\\"trained\\\",\\n        help=\\\"Comma-separated: trained,untrained (default: trained)\\\",\\n    )\\n    args = p.parse_args()\\n\\n    conditions = [c.strip() for c in args.conditions.split(\\\",\\\")]\\n    log(f\\\"Probing-only pipeline, conditions: {conditions}\\\")\\n\\n    t_start = time.time()\\n\\n    for condition in conditions:\\n        if condition == \\\"trained\\\":\\n            ckpt = TRAINED_CKPT\\n        elif condition == \\\"untrained\\\":\\n            if os.path.exists(os.path.join(UNTRAINED_CACHE, \\\"config.json\\\")):\\n                ckpt = UNTRAINED_CACHE\\n            else:\\n                ckpt = UNTRAINED_CKPT\\n                log(f\\\"  Will download untrained model from {ckpt}\\\")\\n        else:\\n            log(f\\\"  Unknown condition: {condition}, skipping\\\")\\n            continue\\n\\n        results_dir = os.path.join(RESULTS_BASE, condition)\\n        os.makedirs(results_dir, exist_ok=True)\\n\\n        nt = 2 if args.dry_run else len(TASKS)\\n        nd = 1 if args.dry_run else N_DEMOS\\n        ns = 2 if args.dry_run else N_TIMESTEPS\\n        nps = 2 if args.dry_run else N_PROBE_SEEDS\\n\\n        log(f\\\"=== {condition.upper()} probing ===\\\")\\n        log(f\\\"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}\\\")\\n        log(f\\\"Output: {results_dir}\\\")\\n\\n        try:\\n            model, processor = load_model(ckpt, condition)\\n        except Exception as e:\\n            log(f\\\"  ERROR loading {condition} model: {e}\\\")\\n            continue\\n\\n        t1 = time.time()\\n        reps, actions = extract_features(model, processor, nt, nd, ns)\\n        log(f\\\"Phase 1: {time.time()-t1:.1f}s\\\")\\n\\n        del model, processor\\n        torch.cuda.empty_cache()\\n\\n        t2 = time.time()\\n        probe_res = run_probing(reps, actions, nps)\\n        out_path = os.path.join(results_dir, \\\"action_r2_probing.json\\\")\\n        with open(out_path, \\\"w\\\") as f:\\n            json.dump(probe_res, f, indent=2)\\n        log(f\\\"Phase 2: {time.time()-t2:.1f}s -> {out_path}\\\")\\n\\n        del reps, actions\\n\\n        log(f\\\"  {condition} complete in {(time.time()-t1)/60:.1f} min\\\")\\n\\n    log(f\\\"All done in {(time.time()-t_start)/60:.1f} min\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have all 7 files. Let me analyze the `run_probing` function in each file to understand the exact pattern I need to replace. Let me look at the truncated parts that I need to see - specifically the `run_probing` function in each file.

From the output I can see:
1. **libero_object_full_pipeline.py** - uses `MLPRegressor`, `N_PROBE_SEEDS = 15`, truncated but I can see the pattern
2. **nora_goal_full_pipeline.py** - uses `MLPRegressor`, `N_PROBE_SEEDS = 15`, truncated 


3. **nora_spatial_full_pipeline.py** - uses `MLPRegressor`, `N_PROBE_SEEDS = 15`, truncated
4. **tracvla_spatial_full_pipeline.py** - uses `MLPRegressor`, `N_PROBE_SEEDS = 15`, truncated
5. **tracvla_object_full_pipeline.py** - uses `MLPRegressor`, `N_PROBE_SEEDS = 15`, truncated
6. **libero_long_full_pipeline.py** - uses `MLPRegressor`, `N_PROBE_SEEDS = 15`, truncated
7. **tracvla_spatial_probing_only.py** - uses `MLPRegressor` as well, and the pattern appears consistent across all files.

Looking at the complete `run_probing` function from file 7, I can see it iterates through multiple seeds, creating an MLP regressor with specific hyperparameters like 256 hidden units, 200 max iterations, and early stopping enabled when appropriate. The regressor trains on the training data and then generates predictions on validation data.

Calculating R² scores...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "4ab83a4b-69b7-4d41-8cf7-159369e6d405",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

需要看到每个文件的 `run_probing` 函数完整代码。被截断了，用 grep 定位行号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "ece7d06d-445a-4a9b-b04f-037c8f569633",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KyAPtLpCNnjbD1oFwXEr5d`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_probing\\|MLPRegressor\\|from sklearn\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "67af7c5b-2ceb-49b5-8373-206fedc6dbe0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

_source line 28 · 2026-05-21T05:04:04.818Z_

<details><summary>↩ Tool result · `toolu_01KyAPtLpCNnjbD1oFwXEr5d`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "18069799-c154-47ad-9e4f-2f2c3abe1e91",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MDb8WGhzC4hrq1VSSWNyBA`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_probing\\|MLPRegressor\\|from sklearn\" /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "9d21306e-5e89-4748-b7c5-ec02a0d4158e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

_source line 30 · 2026-05-21T05:04:05.211Z_

<details><summary>↩ Tool result · `toolu_01MDb8WGhzC4hrq1VSSWNyBA`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "f9117a69-513e-406e-9f8e-4712004fb318",
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

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015f2h2Pi3eHaYruX2bgRiDG`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_probing\\|MLPRegressor\\|from sklearn\" /root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "656aceff-8b0c-4668-aa44-cb04b73af932",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

_source line 32 · 2026-05-21T05:04:06.141Z_

<details><summary>↩ Tool result · `toolu_015f2h2Pi3eHaYruX2bgRiDG`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "4ce4e8e3-75fc-463a-8597-0f7c7acd6359",
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

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UR2ZctxSKBWSyn9aqU3Q3K`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_probing\\|MLPRegressor\\|from sklearn\" /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "e7cdf057-7d20-4088-b49f-0dcc1b69d9fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

_source line 34 · 2026-05-21T05:04:07.125Z_

<details><summary>↩ Tool result · `toolu_01UR2ZctxSKBWSyn9aqU3Q3K`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "135687e5-e82a-40bc-9fdb-8d6d18e0ba70",
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

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011RqvwD5g2T8unavF932TW7`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_probing\\|MLPRegressor\\|from sklearn\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "266f5b10-a669-4822-a181-555bfac709a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

_source line 36 · 2026-05-21T05:04:08.086Z_

<details><summary>↩ Tool result · `toolu_011RqvwD5g2T8unavF932TW7`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "9f67174e-c22a-4ade-b431-1c3902927863",
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

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VHqxZcCFXoZC4rAUfMbjvX`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_probing\\|MLPRegressor\\|from sklearn\" /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "801bf73e-3c3f-4ffc-a1a7-f673a78493ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

_source line 38 · 2026-05-21T05:04:09.023Z_

<details><summary>↩ Tool result · `toolu_01VHqxZcCFXoZC4rAUfMbjvX`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "b1d271d1-b9db-4c80-a8be-b7337a04a6f2",
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

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Q16pL2x9jUvhuBKM69P5Tc`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_probing\\|MLPRegressor\\|from sklearn\" /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "dc4d8b57-b068-477f-b3e5-280d4384e549",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVmg4NUrStotos9N1KQtvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25578,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25578
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

_source line 40 · 2026-05-21T05:04:09.338Z_

<details><summary>↩ Tool result · `toolu_01Q16pL2x9jUvhuBKM69P5Tc`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "adc06f70-d4ba-411f-af27-9e704038d97a",
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

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Right, can't use `|` in ssh_read_only. Let me use grep -n without pipe.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "bd4dd7f7-1820-4e82-ad05-606666ba0ab1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdEbt1jUvdPk4My45ySDCh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2335,
      "cache_read_input_tokens": 51478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2335
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WRNc9FtMhvLNEaN2yiojDj`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"def run_probing\\|MLPRegressor\\|from sklearn\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "d967a495-7f9c-4977-9cb8-d20070c1ae50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdEbt1jUvdPk4My45ySDCh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2335,
      "cache_read_input_tokens": 51478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2335
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

_source line 43 · 2026-05-21T05:04:24.565Z_

<details><summary>↩ Tool result · `toolu_01WRNc9FtMhvLNEaN2yiojDj`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "7a7d018c-0ba7-4e0b-a49b-1b1873364695",
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

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
The `\|` is being interpreted as a pipe. I need to use `-e` flag instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "c3b951ae-1a5e-480d-a4ae-8d6b60a71ab5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmzqJLYjjAkD9XT95zitXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Dfnhqqr9CZfUrBGFKjijTe`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n -e \"def run_probing\" -e \"MLPRegressor\" -e \"from sklearn\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "62cd546b-fae7-4c85-ad80-5fe850f22840",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmzqJLYjjAkD9XT95zitXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 46 · 2026-05-21T05:04:28.919Z_

<details><summary>↩ Tool result · `toolu_01Dfnhqqr9CZfUrBGFKjijTe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:from sklearn.linear_model import LogisticRegression\\n25:from sklearn.neural_network import MLPRegressor\\n185:def run_probing(reps, actions, n_seeds):\\n199:                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "f341a22a-d0e2-4566-a4c5-cff7213a3bab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"24:from sklearn.linear_model import LogisticRegression\\\\n25:from sklearn.neural_network import MLPRegressor\\\\n185:def run_probing(reps, actions, n_seeds):\\\\n199:                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"24:from sklearn.linear_model import LogisticRegression\\n25:from sklearn.neural_network import MLPRegressor\\n185:def run_probing(reps, actions, n_seeds):\\n199:                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MRmEHKuUyZpS1QNjbdR7iH`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n -e \"def run_probing\" -e \"MLPRegressor\" -e \"from sklearn\" /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "ca2af25b-979c-4df7-893e-39fdccff3452",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmzqJLYjjAkD9XT95zitXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 48 · 2026-05-21T05:04:29.825Z_

<details><summary>↩ Tool result · `toolu_01MRmEHKuUyZpS1QNjbdR7iH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"27:from sklearn.linear_model import LogisticRegression\\n28:from sklearn.neural_network import MLPRegressor\\n182:def run_probing(reps, actions, n_seeds):\\n197:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "f2e19846-8b89-4ef5-8ad0-1ea777e3af85",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"27:from sklearn.linear_model import LogisticRegression\\\\n28:from sklearn.neural_network import MLPRegressor\\\\n182:def run_probing(reps, actions, n_seeds):\\\\n197:                probe = MLPRegressor(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"27:from sklearn.linear_model import LogisticRegression\\n28:from sklearn.neural_network import MLPRegressor\\n182:def run_probing(reps, actions, n_seeds):\\n197:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SGdSEmXyLnMPq7Fvv2WGQW`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n -e \"def run_probing\" -e \"MLPRegressor\" -e \"from sklearn\" /root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "d8ea30c0-ebdb-4dbd-a036-93304b9f88b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmzqJLYjjAkD9XT95zitXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 50 · 2026-05-21T05:04:30.693Z_

<details><summary>↩ Tool result · `toolu_01SGdSEmXyLnMPq7Fvv2WGQW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"27:from sklearn.linear_model import LogisticRegression\\n28:from sklearn.neural_network import MLPRegressor\\n182:def run_probing(reps, actions, n_seeds):\\n197:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "5c3171cf-7a75-4ee6-ae2b-88b0254fd27f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"27:from sklearn.linear_model import LogisticRegression\\\\n28:from sklearn.neural_network import MLPRegressor\\\\n182:def run_probing(reps, actions, n_seeds):\\\\n197:                probe = MLPRegressor(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"27:from sklearn.linear_model import LogisticRegression\\n28:from sklearn.neural_network import MLPRegressor\\n182:def run_probing(reps, actions, n_seeds):\\n197:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R4N15s5MPoQCLEcpyaSwyy`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n -e \"def run_probing\" -e \"MLPRegressor\" -e \"from sklearn\" /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "491b1150-91cd-42d1-a17f-8ba221624719",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmzqJLYjjAkD9XT95zitXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 52 · 2026-05-21T05:04:31.580Z_

<details><summary>↩ Tool result · `toolu_01R4N15s5MPoQCLEcpyaSwyy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:from sklearn.linear_model import LogisticRegression\\n25:from sklearn.neural_network import MLPRegressor\\n211:def run_probing(reps, actions, n_seeds):\\n226:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "d38a42df-5263-463d-8c39-7111597b88c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"24:from sklearn.linear_model import LogisticRegression\\\\n25:from sklearn.neural_network import MLPRegressor\\\\n211:def run_probing(reps, actions, n_seeds):\\\\n226:                probe = MLPRegressor(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"24:from sklearn.linear_model import LogisticRegression\\n25:from sklearn.neural_network import MLPRegressor\\n211:def run_probing(reps, actions, n_seeds):\\n226:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UExSiZFXibCj7uerWP4wEL`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n -e \"def run_probing\" -e \"MLPRegressor\" -e \"from sklearn\" /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "179ca836-d7e1-479d-af59-66bcec082fca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmzqJLYjjAkD9XT95zitXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 54 · 2026-05-21T05:04:32.669Z_

<details><summary>↩ Tool result · `toolu_01UExSiZFXibCj7uerWP4wEL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:from sklearn.linear_model import LogisticRegression\\n25:from sklearn.neural_network import MLPRegressor\\n211:def run_probing(reps, actions, n_seeds):\\n226:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "64a1da3a-8aff-42c6-9d10-b65c1dcb93b2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"24:from sklearn.linear_model import LogisticRegression\\\\n25:from sklearn.neural_network import MLPRegressor\\\\n211:def run_probing(reps, actions, n_seeds):\\\\n226:                probe = MLPRegressor(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"24:from sklearn.linear_model import LogisticRegression\\n25:from sklearn.neural_network import MLPRegressor\\n211:def run_probing(reps, actions, n_seeds):\\n226:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KsMjsi8sCmQGagL1KL7fmn`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n -e \"def run_probing\" -e \"MLPRegressor\" -e \"from sklearn\" /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "6ea5deb1-d0a1-4e11-8417-34b25eec0640",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmzqJLYjjAkD9XT95zitXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 56 · 2026-05-21T05:04:33.461Z_

<details><summary>↩ Tool result · `toolu_01KsMjsi8sCmQGagL1KL7fmn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:from sklearn.linear_model import LogisticRegression\\n25:from sklearn.neural_network import MLPRegressor\\n196:def run_probing(reps, actions, n_seeds):\\n210:                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "28ec5ad0-a603-4641-8136-7ae46d11fdba",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"24:from sklearn.linear_model import LogisticRegression\\\\n25:from sklearn.neural_network import MLPRegressor\\\\n196:def run_probing(reps, actions, n_seeds):\\\\n210:                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"24:from sklearn.linear_model import LogisticRegression\\n25:from sklearn.neural_network import MLPRegressor\\n196:def run_probing(reps, actions, n_seeds):\\n210:                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TziWrSrvytvBeGXJmNYdFG`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n -e \"def run_probing\" -e \"MLPRegressor\" -e \"from sklearn\" /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "ec382697-db1c-4d50-8e41-317bf704bbec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmzqJLYjjAkD9XT95zitXw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 58 · 2026-05-21T05:04:34.289Z_

<details><summary>↩ Tool result · `toolu_01TziWrSrvytvBeGXJmNYdFG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"16:from sklearn.neural_network import MLPRegressor\\n143:def run_probing(reps, actions, n_seeds):\\n158:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "7d2257d1-5be7-49cd-bdf6-6bbd87a94c3d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"16:from sklearn.neural_network import MLPRegressor\\\\n143:def run_probing(reps, actions, n_seeds):\\\\n158:                probe = MLPRegressor(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"16:from sklearn.neural_network import MLPRegressor\\n143:def run_probing(reps, actions, n_seeds):\\n158:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now I have the line numbers for each file. Let me read the `run_probing` function from each file. I need to see the exact code to write the sed replacement. Let me read the specific ranges.

File mapping:
1. `libero_object_full_pipeline.py` - run_probing at line 185, MLPRegressor at 199
2. `nora_goal_full_pipeline.py` - run_probing at line 182, MLPRegressor at 197
3. `nora_spatial_full_pipeline.py` - run_probing at line 182, MLPRegressor at 197


4. `tracvla_spatial_full_pipeline.py` - run_probing at line 211, MLPRegressor at 226
5. `tracvla_object_full_pipeline.py` - run_probing at line 211, MLPRegressor at 226
6. `libero_long_full_pipeline.py` - run_probing at line 196, MLPRegressor at 210
7. `tracvla_spatial_probing_only.py` - run_probing at line 143, MLPRegressor at 158

Now I need to examine each run_probing function to understand the exact code structure before making the replacements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "1839f5d5-32f1-4f28-ad1f-3e7418c3ce5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 60_

读取每个文件的 `run_probing` 函数完整代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "927fc3ee-202a-443c-a045-45e6f7bebe87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 61_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CseCRk7fZ5xLQFdW7GamJN`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -230 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "ef3c2f72-40c5-4357-b82a-60b386ac0665",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 62 · 2026-05-21T05:04:44.422Z_

<details><summary>↩ Tool result · `toolu_01CseCRk7fZ5xLQFdW7GamJN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_object\\\"\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef generate_action(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n    input_ids = inputs[\\\"input_ids\\\"]\\n\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = torch.cat(\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\n        )\\n        if \\\"attention_mask\\\" in inputs:\\n            inputs[\\\"attention_mask\\\"] = torch.cat(\\n                (inputs[\\\"attention_mask\\\"],\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\"attention_mask\\\"].dtype)), dim=1\\n            )\\n    inputs[\\\"input_ids\\\"] = input_ids\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            max_new_tokens=7, do_sample=False,\\n        )\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n\\n    vocab_size = model.vocab_size\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\n    norm_act = model.bin_centers[disc]\\n\\n    stats = mode\\n\\n... [截断: 输出过长，省略 623 字符] ...\\n\\noat32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(**inputs,\\n                                    output_hidden_states=True,\\n                                    output_attentions=True)\\n\\n                    seq_len = out.hidden_states[0].shape[1]\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\n                    txt_s, txt_e = img_e, seq_len\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        reps[l][\\\"last_preaction\\\"][idx] = hs[-1].float().cpu().numpy()\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append({\\\"bos\\\": (0, 1), \\\"image\\\": (img_s, img_e),\\n                                          \\\"text\\\": (txt_s, txt_e)})\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\n            l1_attns, token_regions)\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X); nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\n                                     early_stopping=use_es, validation_fraction=0.2 if use_es else 0.1,\\n                                     random_state=s, n_iter_no_change=10)\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 8 == 0:\\n            log(f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\")\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n        tr = token_regions[i]\\n        last = attn.shape[1] - 1\\n        is_, ie = tr[\\\"image\\\"]\\n        ts, te = tr[\\\"text\\\"]\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "4f121531-2225-43d6-9e33-8c9a361c2d3b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. RSA: representational similarity across conditions\\\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nAll results -> RESULTS_DIR/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\\\n\\\\nCKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\"\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\\\\\"\\\\nRESULTS_DIR = \\\\\\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\nUNNORM = \\\\\\\"libero_object\\\\\\\"\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the alphabet soup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the cream cheese and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the salad dressing and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the bbq sauce and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the ketchup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the tomato sauce and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the butter and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the milk and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the chocolate pudding and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the orange juice and put it into the basket\\\\\\\",\\\\n]\\\\n\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 4096\\\\nN_IMG_TOKENS = 256\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, image).to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef generate_action(model, processor, instruction, image):\\\\n    inputs = prepare_inputs(processor, instruction, image)\\\\n    input_ids = inputs[\\\\\\\"input_ids\\\\\\\"]\\\\n\\\\n    if not torch.all(input_ids[:, -1] == 29871):\\\\n        input_ids = torch.cat(\\\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\\\n        )\\\\n        if \\\\\\\"attention_mask\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"attention_mask\\\\\\\"] = torch.cat(\\\\n                (inputs[\\\\\\\"attention_mask\\\\\\\"],\\\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\\\\\"attention_mask\\\\\\\"].dtype)), dim=1\\\\n            )\\\\n    inputs[\\\\\\\"input_ids\\\\\\\"] = input_ids\\\\n\\\\n    with torch.no_grad():\\\\n        gen_ids = model.generate(\\\\n            inputs[\\\\\\\"input_ids\\\\\\\"],\\\\n            attention_mask=inputs.get(\\\\\\\"attention_mask\\\\\\\"),\\\\n            pixel_values=inputs.get(\\\\\\\"pixel_values\\\\\\\"),\\\\n            max_new_tokens=7, do_sample=False,\\\\n        )\\\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\\\n\\\\n    vocab_size = model.vocab_size\\\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\\\n    norm_act = model.bin_centers[disc]\\\\n\\\\n    stats = mode\\\\n\\\\n... [截断: 输出过长，省略 623 字符] ...\\\\n\\\\noat32),\\\\n        }\\\\n        for l in range(N_LAYERS)\\\\n    }\\\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\\\n    task_labels = np.zeros(total, dtype=np.int64)\\\\n    l1_attns = []\\\\n    token_regions = []\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    with torch.no_grad():\\\\n                        out = model(**inputs,\\\\n                                    output_hidden_states=True,\\\\n                                    output_attentions=True)\\\\n\\\\n                    seq_len = out.hidden_states[0].shape[1]\\\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\\\n                    txt_s, txt_e = img_e, seq_len\\\\n\\\\n                    for l in range(N_LAYERS):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        reps[l][\\\\\\\"image_mean\\\\\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\\\n                        reps[l][\\\\\\\"last_preaction\\\\\\\"][idx] = hs[-1].float().cpu().numpy()\\\\n\\\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\\\n                    l1_attns.append(l1)\\\\n                    token_regions.append({\\\\\\\"bos\\\\\\\": (0, 1), \\\\\\\"image\\\\\\\": (img_s, img_e),\\\\n                                          \\\\\\\"text\\\\\\\": (txt_s, txt_e)})\\\\n\\\\n                    actions_arr[idx] = act\\\\n                    task_labels[idx] = ti\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 100 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Phase 1 done: {idx} samples\\\\\\\")\\\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\\\n            l1_attns, token_regions)\\\\n\\\\n\\\\ndef run_probing(reps, actions, n_seeds):\\\\n    log(\\\\\\\"Phase 2: action R2 probing\\\\\\\")\\\\n    results = {}\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            r2s = []\\\\n            for s in range(n_seeds):\\\\n                n = len(X); nt = int(n * 0.8)\\\\n                perm = np.random.RandomState(s).permutation(n)\\\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n                use_es = len(Xtr) >= 10\\\\n                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\\\n                                     early_stopping=use_es, validation_fraction=0.2 if use_es else 0.1,\\\\n                                     random_state=s, n_iter_no_change=10)\\\\n                probe.fit(Xtr, ytr)\\\\n                pred = probe.predict(Xv)\\\\n                ss_res = np.sum((yv - pred) ** 2)\\\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(r2s)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(r2s)), 4),\\\\n                \\\\\\\"values\\\\\\\": [round(v, 4) for v in r2s],\\\\n            }\\\\n        if l % 8 == 0:\\\\n            log(f\\\\\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\\\\\")\\\\n    return results\\\\n\\\\n\\\\ndef analyze_attention(l1_attns, token_regions):\\\\n    log(\\\\\\\"Phase 3: L1 attention profile\\\\\\\")\\\\n    n = len(l1_attns)\\\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\\\n\\\\n    for i in range(n):\\\\n        attn = l1_attns[i]\\\\n        tr = token_regions[i]\\\\n        last = attn.shape[1] - 1\\\\n        is_, ie = tr[\\\\\\\"image\\\\\\\"]\\\\n        ts, te = tr[\\\\\\\"text\\\\\\\"]\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_object\\\"\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef generate_action(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n    input_ids = inputs[\\\"input_ids\\\"]\\n\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = torch.cat(\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\n        )\\n        if \\\"attention_mask\\\" in inputs:\\n            inputs[\\\"attention_mask\\\"] = torch.cat(\\n                (inputs[\\\"attention_mask\\\"],\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\"attention_mask\\\"].dtype)), dim=1\\n            )\\n    inputs[\\\"input_ids\\\"] = input_ids\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            max_new_tokens=7, do_sample=False,\\n        )\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n\\n    vocab_size = model.vocab_size\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\n    norm_act = model.bin_centers[disc]\\n\\n    stats = mode\\n\\n... [截断: 输出过长，省略 623 字符] ...\\n\\noat32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(**inputs,\\n                                    output_hidden_states=True,\\n                                    output_attentions=True)\\n\\n                    seq_len = out.hidden_states[0].shape[1]\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\n                    txt_s, txt_e = img_e, seq_len\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        reps[l][\\\"last_preaction\\\"][idx] = hs[-1].float().cpu().numpy()\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append({\\\"bos\\\": (0, 1), \\\"image\\\": (img_s, img_e),\\n                                          \\\"text\\\": (txt_s, txt_e)})\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\n            l1_attns, token_regions)\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X); nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\n                                     early_stopping=use_es, validation_fraction=0.2 if use_es else 0.1,\\n                                     random_state=s, n_iter_no_change=10)\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 8 == 0:\\n            log(f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\")\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n        tr = token_regions[i]\\n        last = attn.shape[1] - 1\\n        is_, ie = tr[\\\"image\\\"]\\n        ts, te = tr[\\\"text\\\"]\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Mp6kyA5bzQT6k3dgKMuGVR`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -230 /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "88ff34ef-719a-4324-8841-188f22bcac6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 64 · 2026-05-21T05:04:45.442Z_

<details><summary>↩ Tool result · `toolu_01Mp6kyA5bzQT6k3dgKMuGVR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Goal Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_goal\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"put_the_bowl_on_the_stove\\\",\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n    \\\"put_the_cream_cheese_in_the_bowl\\\",\\n    \\\"put_the_wine_bottle_on_the_rack\\\",\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\",\\n    \\\"turn_on_the_stove\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"open the cabinet's middle drawer\\\",\\n    \\\"open the top drawer and place the bowl in it\\\",\\n    \\\"slide the plate to the stove's front\\\",\\n    \\\"place the bowl onto the plate\\\",\\n    \\\"place the bowl onto the stove\\\",\\n    \\\"place the bowl on the cabinet top\\\",\\n    \\\"put cream cheese into the bowl\\\",\\n    \\\"place the wine bottle on the rack\\\",\\n    \\\"place the wine bottle on the cabinet top\\\",\\n    \\\"switch on the stove\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    messages = [{'role': 'user', 'content': [\\n        {'type': 'image', 'image': image},\\n        {'type': 'text', 'text': instruction}\\n    ]}]\\n    text = processor.apply_chat_template(\\n        messages, tokenize=False, add_generation_prompt=True)\\n    inputs = processor(\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\n            for k, v in inputs.items()}\\n\\n\\ndef find_token_regions(input_ids, config):\\n    ids = input_ids[0].cpu().numpy()\\n    vs_id = config.vision_start_token_id\\n    ve_id = config.vision_end_token_id\\n\\n    vs_pos = np.where(ids == vs_id)[0]\\n    ve_pos = np.where(ids == ve_id)[0]\\n\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\n        img_s = int(vs_pos[0]) + 1\\n        img_e = int(ve_pos[0])\\n    else:\\n        img_s = img_e = 0\\n\\n    bos_e = int(vs_pos[0]) if len(vs_pos) > 0 else 0\\n    txt_s = int(ve_pos[0]) + 1 if len(ve_pos) > 0 else img_e\\n    txt_e = len(ids)\\n\\n    return {\\\"bos\\\": (0, bos_e), \\\"image\\\": (img_s, img_e), \\\"text\\\": (txt_s, txt_e)}\\n\\n\\ndef extract_features(model, processor, config, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=True,\\n                        )\\n\\n                    tr = find_token_regions(inputs[\\\"input_ids\\\"], config)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        if img_s < img_e:\\n                            reps[l][\\\"image_mean\\\"][idx] = (\\n                                hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                            )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append(tr)\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 9 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "7800e655-f27a-4d5a-a6dc-41b68ce21ee8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nNORA LIBERO-Goal Full Analysis Pipeline\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\\\n\\\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\\\ncosine distance instead of action MSE.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/nora_goal\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\n\\\\n# --- Architecture (Qwen2.5-VL-3B) ---\\\\nN_LAYERS = 36\\\\nN_HEADS = 16\\\\nHIDDEN = 2048\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\",\\\\n    \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_the_plate\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_the_stove\\\\\\\",\\\\n    \\\\\\\"put_the_bowl_on_top_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"put_the_cream_cheese_in_the_bowl\\\\\\\",\\\\n    \\\\\\\"put_the_wine_bottle_on_the_rack\\\\\\\",\\\\n    \\\\\\\"put_the_wine_bottle_on_top_of_the_cabinet\\\\\\\",\\\\n    \\\\\\\"turn_on_the_stove\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"open the cabinet's middle drawer\\\\\\\",\\\\n    \\\\\\\"open the top drawer and place the bowl in it\\\\\\\",\\\\n    \\\\\\\"slide the plate to the stove's front\\\\\\\",\\\\n    \\\\\\\"place the bowl onto the plate\\\\\\\",\\\\n    \\\\\\\"place the bowl onto the stove\\\\\\\",\\\\n    \\\\\\\"place the bowl on the cabinet top\\\\\\\",\\\\n    \\\\\\\"put cream cheese into the bowl\\\\\\\",\\\\n    \\\\\\\"place the wine bottle on the rack\\\\\\\",\\\\n    \\\\\\\"place the wine bottle on the cabinet top\\\\\\\",\\\\n    \\\\\\\"switch on the stove\\\\\\\",\\\\n]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    messages = [{'role': 'user', 'content': [\\\\n        {'type': 'image', 'image': image},\\\\n        {'type': 'text', 'text': instruction}\\\\n    ]}]\\\\n    text = processor.apply_chat_template(\\\\n        messages, tokenize=False, add_generation_prompt=True)\\\\n    inputs = processor(\\\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\\\n            for k, v in inputs.items()}\\\\n\\\\n\\\\ndef find_token_regions(input_ids, config):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    vs_id = config.vision_start_token_id\\\\n    ve_id = config.vision_end_token_id\\\\n\\\\n    vs_pos = np.where(ids == vs_id)[0]\\\\n    ve_pos = np.where(ids == ve_id)[0]\\\\n\\\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\\\n        img_s = int(vs_pos[0]) + 1\\\\n        img_e = int(ve_pos[0])\\\\n    else:\\\\n        img_s = img_e = 0\\\\n\\\\n    bos_e = int(vs_pos[0]) if len(vs_pos) > 0 else 0\\\\n    txt_s = int(ve_pos[0]) + 1 if len(ve_pos) > 0 else img_e\\\\n    txt_e = len(ids)\\\\n\\\\n    return {\\\\\\\"bos\\\\\\\": (0, bos_e), \\\\\\\"image\\\\\\\": (img_s, img_e), \\\\\\\"text\\\\\\\": (txt_s, txt_e)}\\\\n\\\\n\\\\ndef extract_features(model, processor, config, n_tasks, n_demos, n_timesteps):\\\\n    log(\\\\\\\"Phase 1: representation extraction\\\\\\\")\\\\n    total = n_tasks * n_demos * n_timesteps\\\\n\\\\n    reps = {\\\\n        l: {\\\\n            \\\\\\\"image_mean\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n            \\\\\\\"last_preaction\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n        }\\\\n        for l in range(N_LAYERS)\\\\n    }\\\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\\\n    task_labels = np.zeros(total, dtype=np.int64)\\\\n    l1_attns = []\\\\n    token_regions = []\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    with torch.no_grad():\\\\n                        out = model(\\\\n                            **inputs,\\\\n                            output_hidden_states=True,\\\\n                            output_attentions=True,\\\\n                        )\\\\n\\\\n                    tr = find_token_regions(inputs[\\\\\\\"input_ids\\\\\\\"], config)\\\\n                    img_s, img_e = tr[\\\\\\\"image\\\\\\\"]\\\\n\\\\n                    for l in range(N_LAYERS):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        if img_s < img_e:\\\\n                            reps[l][\\\\\\\"image_mean\\\\\\\"][idx] = (\\\\n                                hs[img_s:img_e].float().mean(0).cpu().numpy()\\\\n                            )\\\\n                        reps[l][\\\\\\\"last_preaction\\\\\\\"][idx] = (\\\\n                            hs[-1].float().cpu().numpy()\\\\n                        )\\\\n\\\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\\\n                    l1_attns.append(l1)\\\\n                    token_regions.append(tr)\\\\n\\\\n                    actions_arr[idx] = act\\\\n                    task_labels[idx] = ti\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 100 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Phase 1 done: {idx} samples\\\\\\\")\\\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\\\n\\\\n\\\\ndef run_probing(reps, actions, n_seeds):\\\\n    log(\\\\\\\"Phase 2: action R2 probing\\\\\\\")\\\\n    results = {}\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            r2s = []\\\\n            for s in range(n_seeds):\\\\n                n = len(X)\\\\n                nt = int(n * 0.8)\\\\n                perm = np.random.RandomState(s).permutation(n)\\\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n                use_es = len(Xtr) >= 10\\\\n                probe = MLPRegressor(\\\\n                    hidden_layer_sizes=(256,),\\\\n                    max_iter=200,\\\\n                    early_stopping=use_es,\\\\n                    validation_fraction=0.2 if use_es else 0.1,\\\\n                    random_state=s,\\\\n                    n_iter_no_change=10,\\\\n                )\\\\n                probe.fit(Xtr, ytr)\\\\n                pred = probe.predict(Xv)\\\\n                ss_res = np.sum((yv - pred) ** 2)\\\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(r2s)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(r2s)), 4),\\\\n                \\\\\\\"values\\\\\\\": [round(v, 4) for v in r2s],\\\\n            }\\\\n        if l % 9 == 0:\\\\n            log(\\\\n                f\\\\\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\\\\\"\\\\n            )\\\\n    return results\\\\n\\\\n\\\\ndef analyze_attention(l1_attns, token_regions):\\\\n    log(\\\\\\\"Phase 3: L1 attention profile\\\\\\\")\\\\n    n = len(l1_attns)\\\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\\\n\\\\n    for i in range(n):\\\\n        attn = l1_attns[i]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Goal Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_goal\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n    \\\"put_the_bowl_on_the_plate\\\",\\n    \\\"put_the_bowl_on_the_stove\\\",\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n    \\\"put_the_cream_cheese_in_the_bowl\\\",\\n    \\\"put_the_wine_bottle_on_the_rack\\\",\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\",\\n    \\\"turn_on_the_stove\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"open the cabinet's middle drawer\\\",\\n    \\\"open the top drawer and place the bowl in it\\\",\\n    \\\"slide the plate to the stove's front\\\",\\n    \\\"place the bowl onto the plate\\\",\\n    \\\"place the bowl onto the stove\\\",\\n    \\\"place the bowl on the cabinet top\\\",\\n    \\\"put cream cheese into the bowl\\\",\\n    \\\"place the wine bottle on the rack\\\",\\n    \\\"place the wine bottle on the cabinet top\\\",\\n    \\\"switch on the stove\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    messages = [{'role': 'user', 'content': [\\n        {'type': 'image', 'image': image},\\n        {'type': 'text', 'text': instruction}\\n    ]}]\\n    text = processor.apply_chat_template(\\n        messages, tokenize=False, add_generation_prompt=True)\\n    inputs = processor(\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\n            for k, v in inputs.items()}\\n\\n\\ndef find_token_regions(input_ids, config):\\n    ids = input_ids[0].cpu().numpy()\\n    vs_id = config.vision_start_token_id\\n    ve_id = config.vision_end_token_id\\n\\n    vs_pos = np.where(ids == vs_id)[0]\\n    ve_pos = np.where(ids == ve_id)[0]\\n\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\n        img_s = int(vs_pos[0]) + 1\\n        img_e = int(ve_pos[0])\\n    else:\\n        img_s = img_e = 0\\n\\n    bos_e = int(vs_pos[0]) if len(vs_pos) > 0 else 0\\n    txt_s = int(ve_pos[0]) + 1 if len(ve_pos) > 0 else img_e\\n    txt_e = len(ids)\\n\\n    return {\\\"bos\\\": (0, bos_e), \\\"image\\\": (img_s, img_e), \\\"text\\\": (txt_s, txt_e)}\\n\\n\\ndef extract_features(model, processor, config, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=True,\\n                        )\\n\\n                    tr = find_token_regions(inputs[\\\"input_ids\\\"], config)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        if img_s < img_e:\\n                            reps[l][\\\"image_mean\\\"][idx] = (\\n                                hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                            )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append(tr)\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 9 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015oi3WUrJF2Y5pbWR13yasV`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -230 /root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "d5bb35c7-7ed8-4eab-a201-2ee340502460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 66 · 2026-05-21T05:04:45.965Z_

<details><summary>↩ Tool result · `toolu_015oi3WUrJF2Y5pbWR13yasV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Spatial Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the black bowl between the plate and ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl from the center of the table and put it on the plate\\\",\\n    \\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl next to the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl next to the plate and put it on the plate\\\",\\n    \\\"grab the black bowl next to the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl on the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the stove and put it on the plate\\\",\\n    \\\"grab the black bowl on the wooden cabinet and put it on the plate\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    messages = [{'role': 'user', 'content': [\\n        {'type': 'image', 'image': image},\\n        {'type': 'text', 'text': instruction}\\n    ]}]\\n    text = processor.apply_chat_template(\\n        messages, tokenize=False, add_generation_prompt=True)\\n    inputs = processor(\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\n            for k, v in inputs.items()}\\n\\n\\ndef find_token_regions(input_ids, config):\\n    ids = input_ids[0].cpu().numpy()\\n    vs_id = config.vision_start_token_id\\n    ve_id = config.vision_end_token_id\\n\\n    vs_pos = np.where(ids == vs_id)[0]\\n    ve_pos = np.where(ids == ve_id)[0]\\n\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\n        img_s = int(vs_pos[0]) + 1\\n     \\n\\n... [截断: 输出过长，省略 645 字符] ...\\n\\nl in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=True,\\n                        )\\n\\n                    tr = find_token_regions(inputs[\\\"input_ids\\\"], config)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        if img_s < img_e:\\n                            reps[l][\\\"image_mean\\\"][idx] = (\\n                                hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                            )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append(tr)\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 9 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "cabd3caa-847c-43e4-ba53-0c76c5b5805b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nNORA LIBERO-Spatial Full Analysis Pipeline\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\\\n\\\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\\\ncosine distance instead of action MSE.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/nora_spatial\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\n\\\\n# --- Architecture (Qwen2.5-VL-3B) ---\\\\nN_LAYERS = 36\\\\nN_HEADS = 16\\\\nHIDDEN = 2048\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the black bowl between the plate and ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl from the center of the table and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the cookie box and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the plate and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the cookie box and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the stove and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the wooden cabinet and put it on the plate\\\\\\\",\\\\n]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    messages = [{'role': 'user', 'content': [\\\\n        {'type': 'image', 'image': image},\\\\n        {'type': 'text', 'text': instruction}\\\\n    ]}]\\\\n    text = processor.apply_chat_template(\\\\n        messages, tokenize=False, add_generation_prompt=True)\\\\n    inputs = processor(\\\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\\\n            for k, v in inputs.items()}\\\\n\\\\n\\\\ndef find_token_regions(input_ids, config):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    vs_id = config.vision_start_token_id\\\\n    ve_id = config.vision_end_token_id\\\\n\\\\n    vs_pos = np.where(ids == vs_id)[0]\\\\n    ve_pos = np.where(ids == ve_id)[0]\\\\n\\\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\\\n        img_s = int(vs_pos[0]) + 1\\\\n     \\\\n\\\\n... [截断: 输出过长，省略 645 字符] ...\\\\n\\\\nl in range(N_LAYERS)\\\\n    }\\\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\\\n    task_labels = np.zeros(total, dtype=np.int64)\\\\n    l1_attns = []\\\\n    token_regions = []\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    with torch.no_grad():\\\\n                        out = model(\\\\n                            **inputs,\\\\n                            output_hidden_states=True,\\\\n                            output_attentions=True,\\\\n                        )\\\\n\\\\n                    tr = find_token_regions(inputs[\\\\\\\"input_ids\\\\\\\"], config)\\\\n                    img_s, img_e = tr[\\\\\\\"image\\\\\\\"]\\\\n\\\\n                    for l in range(N_LAYERS):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        if img_s < img_e:\\\\n                            reps[l][\\\\\\\"image_mean\\\\\\\"][idx] = (\\\\n                                hs[img_s:img_e].float().mean(0).cpu().numpy()\\\\n                            )\\\\n                        reps[l][\\\\\\\"last_preaction\\\\\\\"][idx] = (\\\\n                            hs[-1].float().cpu().numpy()\\\\n                        )\\\\n\\\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\\\n                    l1_attns.append(l1)\\\\n                    token_regions.append(tr)\\\\n\\\\n                    actions_arr[idx] = act\\\\n                    task_labels[idx] = ti\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 100 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Phase 1 done: {idx} samples\\\\\\\")\\\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\\\n\\\\n\\\\ndef run_probing(reps, actions, n_seeds):\\\\n    log(\\\\\\\"Phase 2: action R2 probing\\\\\\\")\\\\n    results = {}\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            r2s = []\\\\n            for s in range(n_seeds):\\\\n                n = len(X)\\\\n                nt = int(n * 0.8)\\\\n                perm = np.random.RandomState(s).permutation(n)\\\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n                use_es = len(Xtr) >= 10\\\\n                probe = MLPRegressor(\\\\n                    hidden_layer_sizes=(256,),\\\\n                    max_iter=200,\\\\n                    early_stopping=use_es,\\\\n                    validation_fraction=0.2 if use_es else 0.1,\\\\n                    random_state=s,\\\\n                    n_iter_no_change=10,\\\\n                )\\\\n                probe.fit(Xtr, ytr)\\\\n                pred = probe.predict(Xv)\\\\n                ss_res = np.sum((yv - pred) ** 2)\\\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(r2s)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(r2s)), 4),\\\\n                \\\\\\\"values\\\\\\\": [round(v, 4) for v in r2s],\\\\n            }\\\\n        if l % 9 == 0:\\\\n            log(\\\\n                f\\\\\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\\\\\"\\\\n            )\\\\n    return results\\\\n\\\\n\\\\ndef analyze_attention(l1_attns, token_regions):\\\\n    log(\\\\\\\"Phase 3: L1 attention profile\\\\\\\")\\\\n    n = len(l1_attns)\\\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\\\n\\\\n    for i in range(n):\\\\n        attn = l1_attns[i]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nNORA LIBERO-Spatial Full Analysis Pipeline\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased)\\n\\nRuns both trained (NORA) and untrained (Qwen2.5-VL-3B base) sequentially.\\nNORA uses FAST+ action tokenizer, so counterfactual uses representation-based\\ncosine distance instead of action MSE.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForImageTextToText, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/nora_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture (Qwen2.5-VL-3B) ---\\nN_LAYERS = 36\\nN_HEADS = 16\\nHIDDEN = 2048\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the black bowl between the plate and ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl from the center of the table and put it on the plate\\\",\\n    \\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl next to the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl next to the plate and put it on the plate\\\",\\n    \\\"grab the black bowl next to the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl on the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the stove and put it on the plate\\\",\\n    \\\"grab the black bowl on the wooden cabinet and put it on the plate\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    messages = [{'role': 'user', 'content': [\\n        {'type': 'image', 'image': image},\\n        {'type': 'text', 'text': instruction}\\n    ]}]\\n    text = processor.apply_chat_template(\\n        messages, tokenize=False, add_generation_prompt=True)\\n    inputs = processor(\\n        text=[text], images=[image], return_tensors='pt', padding=True)\\n    return {k: v.to(DEVICE) if isinstance(v, torch.Tensor) else v\\n            for k, v in inputs.items()}\\n\\n\\ndef find_token_regions(input_ids, config):\\n    ids = input_ids[0].cpu().numpy()\\n    vs_id = config.vision_start_token_id\\n    ve_id = config.vision_end_token_id\\n\\n    vs_pos = np.where(ids == vs_id)[0]\\n    ve_pos = np.where(ids == ve_id)[0]\\n\\n    if len(vs_pos) > 0 and len(ve_pos) > 0:\\n        img_s = int(vs_pos[0]) + 1\\n     \\n\\n... [截断: 输出过长，省略 645 字符] ...\\n\\nl in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=True,\\n                        )\\n\\n                    tr = find_token_regions(inputs[\\\"input_ids\\\"], config)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        if img_s < img_e:\\n                            reps[l][\\\"image_mean\\\"][idx] = (\\n                                hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                            )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append(tr)\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 9 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014eNCfxRfdiaTbcQJR1Pfh7`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -260 /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "f07e2946-5d12-4646-9d72-ea641b90645f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 68 · 2026-05-21T05:04:46.873Z_

<details><summary>↩ Tool result · `toolu_014eNCfxRfdiaTbcQJR1Pfh7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Spatial Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the black bowl between the plate and ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl from the center of the table and put it on the plate\\\",\\n    \\\"grab the black bowl next to the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl on the stove and put it on the plate\\\",\\n    \\\"grab the black bowl on the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl next to the plate and put it on the plate\\\",\\n    \\\"grab the black bowl next to the ramekin and put it on the plate\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef detect_image_token_id(processor):\\n    return -1\\n\\n\\ndef find_token_regions(input_ids, img_token_id):\\n    ids = input_ids[0].cpu().numpy()\\n    img_mask = ids < 0\\n    img_positions = np.where(img_mask)[0]\\n\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0\\n\\n... [截断: 输出过长，省略 1460 字符] ...\\n\\n_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    original_ids = inputs[\\\"input_ids\\\"].clone()\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=True,\\n                        )\\n\\n                    tr = find_token_regions(original_ids, img_token_id)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = (\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append(tr)\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 8 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n        tr = token_regions[i]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "f0bc2952-9a03-4d79-a207-2922bf73c6cb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Spatial Full Analysis Pipeline for TracVLA-Phi3V\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"microsoft/Phi-3-vision-128k-instruct\\\\\\\"\\\\nUNTRAINED_CACHE = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\\\n\\\\n# --- Architecture ---\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 3072\\\\nN_IMG_TOKENS = 0  # auto-detected\\\\nIMG_TOKEN_ID = -1  # auto-detected\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the black bowl between the plate and ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the ramekin and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the cookie box and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl from the center of the table and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the cookie box and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the stove and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl on the wooden cabinet and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the plate and put it on the plate\\\\\\\",\\\\n    \\\\\\\"grab the black bowl next to the ramekin and put it on the plate\\\\\\\",\\\\n]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return (\\\\n        f\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\"\\\\n    )\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef detect_image_token_id(processor):\\\\n    return -1\\\\n\\\\n\\\\ndef find_token_regions(input_ids, img_token_id):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    img_mask = ids < 0\\\\n    img_positions = np.where(img_mask)[0]\\\\n\\\\n    if len(img_positions) > 0:\\\\n        img_s = int(img_positions[0\\\\n\\\\n... [截断: 输出过长，省略 1460 字符] ...\\\\n\\\\n_arr = np.zeros((total, 7), dtype=np.float32)\\\\n    task_labels = np.zeros(total, dtype=np.int64)\\\\n    l1_attns = []\\\\n    token_regions = []\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    original_ids = inputs[\\\\\\\"input_ids\\\\\\\"].clone()\\\\n                    with torch.no_grad():\\\\n                        out = model(\\\\n                            **inputs,\\\\n                            output_hidden_states=True,\\\\n                            output_attentions=True,\\\\n                        )\\\\n\\\\n                    tr = find_token_regions(original_ids, img_token_id)\\\\n                    img_s, img_e = tr[\\\\\\\"image\\\\\\\"]\\\\n\\\\n                    for l in range(N_LAYERS):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        reps[l][\\\\\\\"image_mean\\\\\\\"][idx] = (\\\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\\\n                        )\\\\n                        reps[l][\\\\\\\"last_preaction\\\\\\\"][idx] = (\\\\n                            hs[-1].float().cpu().numpy()\\\\n                        )\\\\n\\\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\\\n                    l1_attns.append(l1)\\\\n                    token_regions.append(tr)\\\\n\\\\n                    actions_arr[idx] = act\\\\n                    task_labels[idx] = ti\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 100 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Phase 1 done: {idx} samples\\\\\\\")\\\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\\\n\\\\n\\\\ndef run_probing(reps, actions, n_seeds):\\\\n    log(\\\\\\\"Phase 2: action R2 probing\\\\\\\")\\\\n    results = {}\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            r2s = []\\\\n            for s in range(n_seeds):\\\\n                n = len(X)\\\\n                nt = int(n * 0.8)\\\\n                perm = np.random.RandomState(s).permutation(n)\\\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n                use_es = len(Xtr) >= 10\\\\n                probe = MLPRegressor(\\\\n                    hidden_layer_sizes=(256,),\\\\n                    max_iter=200,\\\\n                    early_stopping=use_es,\\\\n                    validation_fraction=0.2 if use_es else 0.1,\\\\n                    random_state=s,\\\\n                    n_iter_no_change=10,\\\\n                )\\\\n                probe.fit(Xtr, ytr)\\\\n                pred = probe.predict(Xv)\\\\n                ss_res = np.sum((yv - pred) ** 2)\\\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(r2s)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(r2s)), 4),\\\\n                \\\\\\\"values\\\\\\\": [round(v, 4) for v in r2s],\\\\n            }\\\\n        if l % 8 == 0:\\\\n            log(\\\\n                f\\\\\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\\\\\"\\\\n            )\\\\n    return results\\\\n\\\\n\\\\ndef analyze_attention(l1_attns, token_regions):\\\\n    log(\\\\\\\"Phase 3: L1 attention profile\\\\\\\")\\\\n    n = len(l1_attns)\\\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\\\n\\\\n    for i in range(n):\\\\n        attn = l1_attns[i]\\\\n        tr = token_regions[i]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Spatial Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the black bowl between the plate and ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the ramekin and put it on the plate\\\",\\n    \\\"grab the black bowl on the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl in the top drawer of the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl from the center of the table and put it on the plate\\\",\\n    \\\"grab the black bowl next to the cookie box and put it on the plate\\\",\\n    \\\"grab the black bowl on the stove and put it on the plate\\\",\\n    \\\"grab the black bowl on the wooden cabinet and put it on the plate\\\",\\n    \\\"grab the black bowl next to the plate and put it on the plate\\\",\\n    \\\"grab the black bowl next to the ramekin and put it on the plate\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef detect_image_token_id(processor):\\n    return -1\\n\\n\\ndef find_token_regions(input_ids, img_token_id):\\n    ids = input_ids[0].cpu().numpy()\\n    img_mask = ids < 0\\n    img_positions = np.where(img_mask)[0]\\n\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0\\n\\n... [截断: 输出过长，省略 1460 字符] ...\\n\\n_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    original_ids = inputs[\\\"input_ids\\\"].clone()\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=True,\\n                        )\\n\\n                    tr = find_token_regions(original_ids, img_token_id)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = (\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append(tr)\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 8 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n        tr = token_regions[i]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0183x26apj3wgXLyD4ZyBCRq`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -260 /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "2be8f650-3a13-47ae-ad1a-48bf260e5d1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 70 · 2026-05-21T05:04:47.397Z_

<details><summary>↩ Tool result · `toolu_0183x26apj3wgXLyD4ZyBCRq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_object\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef detect_image_token_id(processor):\\n    return -1\\n\\n\\ndef find_token_regions(input_ids, img_token_id):\\n    ids = input_ids[0].cpu().numpy()\\n    img_mask = ids < 0\\n    img_positions = np.where(img_mask)[0]\\n\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0])\\n        img_e = int(img_positions[-1]) + 1\\n    else:\\n        img_s = img_e = 1\\n\\n    txt_s = img_e\\n    txt_e = len(ids)\\n\\n    return {\\\"bos\\\": (0, img_s), \\\"image\\\": (img_s, img_e), \\\"text\\\": (txt_s, txt_e)}\\n\\n\\ndef generate_action_phi3v(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n          \\n\\n... [截断: 输出过长，省略 1060 字符] ...\\n\\n_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    original_ids = inputs[\\\"input_ids\\\"].clone()\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=True,\\n                        )\\n\\n                    tr = find_token_regions(original_ids, img_token_id)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = (\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append(tr)\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 8 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n        tr = token_regions[i]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "e2571579-78b3-48f3-b426-3e58287adea6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Object Full Analysis Pipeline for TracVLA-Phi3V\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"microsoft/Phi-3-vision-128k-instruct\\\\\\\"\\\\nUNTRAINED_CACHE = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/tracvla_object\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\\\n\\\\n# --- Architecture ---\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 3072\\\\nN_IMG_TOKENS = 0  # auto-detected\\\\nIMG_TOKEN_ID = -1  # auto-detected\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the alphabet soup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the bbq sauce and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the butter and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the chocolate pudding and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the cream cheese and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the ketchup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the milk and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the orange juice and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the salad dressing and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the tomato sauce and put it into the basket\\\\\\\",\\\\n]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return (\\\\n        f\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\"\\\\n    )\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef detect_image_token_id(processor):\\\\n    return -1\\\\n\\\\n\\\\ndef find_token_regions(input_ids, img_token_id):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    img_mask = ids < 0\\\\n    img_positions = np.where(img_mask)[0]\\\\n\\\\n    if len(img_positions) > 0:\\\\n        img_s = int(img_positions[0])\\\\n        img_e = int(img_positions[-1]) + 1\\\\n    else:\\\\n        img_s = img_e = 1\\\\n\\\\n    txt_s = img_e\\\\n    txt_e = len(ids)\\\\n\\\\n    return {\\\\\\\"bos\\\\\\\": (0, img_s), \\\\\\\"image\\\\\\\": (img_s, img_e), \\\\\\\"text\\\\\\\": (txt_s, txt_e)}\\\\n\\\\n\\\\ndef generate_action_phi3v(model, processor, instruction, image):\\\\n    inputs = prepare_inputs(processor, instruction, image)\\\\n\\\\n    with torch.no_grad():\\\\n        gen_ids = model.generate(\\\\n          \\\\n\\\\n... [截断: 输出过长，省略 1060 字符] ...\\\\n\\\\n_arr = np.zeros((total, 7), dtype=np.float32)\\\\n    task_labels = np.zeros(total, dtype=np.int64)\\\\n    l1_attns = []\\\\n    token_regions = []\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    original_ids = inputs[\\\\\\\"input_ids\\\\\\\"].clone()\\\\n                    with torch.no_grad():\\\\n                        out = model(\\\\n                            **inputs,\\\\n                            output_hidden_states=True,\\\\n                            output_attentions=True,\\\\n                        )\\\\n\\\\n                    tr = find_token_regions(original_ids, img_token_id)\\\\n                    img_s, img_e = tr[\\\\\\\"image\\\\\\\"]\\\\n\\\\n                    for l in range(N_LAYERS):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        reps[l][\\\\\\\"image_mean\\\\\\\"][idx] = (\\\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\\\n                        )\\\\n                        reps[l][\\\\\\\"last_preaction\\\\\\\"][idx] = (\\\\n                            hs[-1].float().cpu().numpy()\\\\n                        )\\\\n\\\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\\\n                    l1_attns.append(l1)\\\\n                    token_regions.append(tr)\\\\n\\\\n                    actions_arr[idx] = act\\\\n                    task_labels[idx] = ti\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 100 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Phase 1 done: {idx} samples\\\\\\\")\\\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\\\n\\\\n\\\\ndef run_probing(reps, actions, n_seeds):\\\\n    log(\\\\\\\"Phase 2: action R2 probing\\\\\\\")\\\\n    results = {}\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            r2s = []\\\\n            for s in range(n_seeds):\\\\n                n = len(X)\\\\n                nt = int(n * 0.8)\\\\n                perm = np.random.RandomState(s).permutation(n)\\\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n                use_es = len(Xtr) >= 10\\\\n                probe = MLPRegressor(\\\\n                    hidden_layer_sizes=(256,),\\\\n                    max_iter=200,\\\\n                    early_stopping=use_es,\\\\n                    validation_fraction=0.2 if use_es else 0.1,\\\\n                    random_state=s,\\\\n                    n_iter_no_change=10,\\\\n                )\\\\n                probe.fit(Xtr, ytr)\\\\n                pred = probe.predict(Xv)\\\\n                ss_res = np.sum((yv - pred) ** 2)\\\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(r2s)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(r2s)), 4),\\\\n                \\\\\\\"values\\\\\\\": [round(v, 4) for v in r2s],\\\\n            }\\\\n        if l % 8 == 0:\\\\n            log(\\\\n                f\\\\\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\\\\\"\\\\n            )\\\\n    return results\\\\n\\\\n\\\\ndef analyze_attention(l1_attns, token_regions):\\\\n    log(\\\\\\\"Phase 3: L1 attention profile\\\\\\\")\\\\n    n = len(l1_attns)\\\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\\\n\\\\n    for i in range(n):\\\\n        attn = l1_attns[i]\\\\n        tr = token_regions[i]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_object\\\"\\nDEVICE = \\\"cuda:0\\\"  # submit_training_job sets CUDA_VISIBLE_DEVICES\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 3072\\nN_IMG_TOKENS = 0  # auto-detected\\nIMG_TOKEN_ID = -1  # auto-detected\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef detect_image_token_id(processor):\\n    return -1\\n\\n\\ndef find_token_regions(input_ids, img_token_id):\\n    ids = input_ids[0].cpu().numpy()\\n    img_mask = ids < 0\\n    img_positions = np.where(img_mask)[0]\\n\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0])\\n        img_e = int(img_positions[-1]) + 1\\n    else:\\n        img_s = img_e = 1\\n\\n    txt_s = img_e\\n    txt_e = len(ids)\\n\\n    return {\\\"bos\\\": (0, img_s), \\\"image\\\": (img_s, img_e), \\\"text\\\": (txt_s, txt_e)}\\n\\n\\ndef generate_action_phi3v(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n          \\n\\n... [截断: 输出过长，省略 1060 字符] ...\\n\\n_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    original_ids = inputs[\\\"input_ids\\\"].clone()\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=True,\\n                        )\\n\\n                    tr = find_token_regions(original_ids, img_token_id)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = (\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append(tr)\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 8 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n        tr = token_regions[i]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DYGbiCZ5euk5LUzTzAfLTw`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -245 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "ec3575af-2479-4a2d-bfaa-242ebd5465ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 72 · 2026-05-21T05:04:48.290Z_

<details><summary>↩ Tool result · `toolu_01DYGbiCZ5euk5LUzTzAfLTw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Long Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_long\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_10\\\"\\n\\nTASKS = [\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\",\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\",\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\",\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\",\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\",\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\",\\n]\\nINSTRUCTIONS = [\\n    \\\"turn on the stove and put the moka pot on it\\\",\\n    \\\"put the black bowl in the bottom drawer of the cabinet and close it\\\",\\n    \\\"put the yellow and white mug in the microwave and close it\\\",\\n    \\\"put both moka pots on the stove\\\",\\n    \\\"put both the alphabet soup and the cream cheese box in the basket\\\",\\n    \\\"put both the alphabet soup and the tomato sauce in the basket\\\",\\n    \\\"put both the cream cheese box and the butter in the basket\\\",\\n    \\\"put the white mug on the left plate and put the yellow and white mug on the right plate\\\",\\n    \\\"put the white mug on the plate and put the chocolate pudding to the right of the plate\\\",\\n    \\\"pick up the book and place it in the back compartment of the caddy\\\",\\n]\\nPARAPHRASES = [\\n    \\\"switch on the stove and place the moka pot on it\\\",\\n    \\\"place the black bowl in the bottom drawer of the cabinet and shut it\\\",\\n    \\\"place the yellow and white mug in the microwave and shut it\\\",\\n    \\\"put both of the moka pots on the stove\\\",\\n    \\\"place the alphabet soup and cream cheese box into the basket\\\",\\n    \\\"place the alphabet soup and tomato sauce into the basket\\\",\\n    \\\"place the cream cheese box and butter into the basket\\\",\\n    \\\"place the white mug on the left plate and the yellow white mug on the right plate\\\",\\n    \\\"place the white mug on the plate and the chocolate pudding to the right of the plate\\\",\\n    \\\"grab the book and put it in the back section of the caddy\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef g\\n\\n... [截断: 输出过长，省略 1857 字符] ...\\n\\ntal, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(**inputs,\\n                                    output_hidden_states=True,\\n                                    output_attentions=True)\\n\\n                    seq_len = out.hidden_states[0].shape[1]\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\n                    txt_s, txt_e = img_e, seq_len\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        reps[l][\\\"last_preaction\\\"][idx] = hs[-1].float().cpu().numpy()\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append({\\\"bos\\\": (0, 1), \\\"image\\\": (img_s, img_e),\\n                                          \\\"text\\\": (txt_s, txt_e)})\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\n            l1_attns, token_regions)\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X); nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\n                                     early_stopping=use_es, validation_fraction=0.2 if use_es else 0.1,\\n                                     random_state=s, n_iter_no_change=10)\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 8 == 0:\\n            log(f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\")\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n        tr = token_regions[i]\\n        last = attn.shape[1] - 1\\n        is_, ie = tr[\\\"image\\\"]\\n        ts, te = tr[\\\"text\\\"]\\n\\n        for h in range(N_HEADS):\\n            row = attn[h, last, :]\\n            img_a = row[is_:ie].sum()\\n            txt_a = row[ts:te].sum()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "9003b1cd-52df-40d8-b444-882d28d48697",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Long Full Analysis Pipeline (Streaming)\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. RSA: representational similarity across conditions\\\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nAll results -> RESULTS_DIR/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\\\n\\\\nCKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\\\\\"\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\\\\\"\\\\nRESULTS_DIR = \\\\\\\"/root/autodl-tmp/vla-ssd/results/libero_long\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\nUNNORM = \\\\\\\"libero_10\\\\\\\"\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\\\\\",\\\\n    \\\\\\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\\\\\",\\\\n    \\\\\\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\\\\\",\\\\n    \\\\\\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\\\\\",\\\\n    \\\\\\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\\\\\",\\\\n    \\\\\\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [\\\\n    \\\\\\\"turn on the stove and put the moka pot on it\\\\\\\",\\\\n    \\\\\\\"put the black bowl in the bottom drawer of the cabinet and close it\\\\\\\",\\\\n    \\\\\\\"put the yellow and white mug in the microwave and close it\\\\\\\",\\\\n    \\\\\\\"put both moka pots on the stove\\\\\\\",\\\\n    \\\\\\\"put both the alphabet soup and the cream cheese box in the basket\\\\\\\",\\\\n    \\\\\\\"put both the alphabet soup and the tomato sauce in the basket\\\\\\\",\\\\n    \\\\\\\"put both the cream cheese box and the butter in the basket\\\\\\\",\\\\n    \\\\\\\"put the white mug on the left plate and put the yellow and white mug on the right plate\\\\\\\",\\\\n    \\\\\\\"put the white mug on the plate and put the chocolate pudding to the right of the plate\\\\\\\",\\\\n    \\\\\\\"pick up the book and place it in the back compartment of the caddy\\\\\\\",\\\\n]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"switch on the stove and place the moka pot on it\\\\\\\",\\\\n    \\\\\\\"place the black bowl in the bottom drawer of the cabinet and shut it\\\\\\\",\\\\n    \\\\\\\"place the yellow and white mug in the microwave and shut it\\\\\\\",\\\\n    \\\\\\\"put both of the moka pots on the stove\\\\\\\",\\\\n    \\\\\\\"place the alphabet soup and cream cheese box into the basket\\\\\\\",\\\\n    \\\\\\\"place the alphabet soup and tomato sauce into the basket\\\\\\\",\\\\n    \\\\\\\"place the cream cheese box and butter into the basket\\\\\\\",\\\\n    \\\\\\\"place the white mug on the left plate and the yellow white mug on the right plate\\\\\\\",\\\\n    \\\\\\\"place the white mug on the plate and the chocolate pudding to the right of the plate\\\\\\\",\\\\n    \\\\\\\"grab the book and put it in the back section of the caddy\\\\\\\",\\\\n]\\\\n\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 4096\\\\nN_IMG_TOKENS = 256\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, image).to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef g\\\\n\\\\n... [截断: 输出过长，省略 1857 字符] ...\\\\n\\\\ntal, dtype=np.int64)\\\\n    l1_attns = []\\\\n    token_regions = []\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    with torch.no_grad():\\\\n                        out = model(**inputs,\\\\n                                    output_hidden_states=True,\\\\n                                    output_attentions=True)\\\\n\\\\n                    seq_len = out.hidden_states[0].shape[1]\\\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\\\n                    txt_s, txt_e = img_e, seq_len\\\\n\\\\n                    for l in range(N_LAYERS):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        reps[l][\\\\\\\"image_mean\\\\\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\\\n                        reps[l][\\\\\\\"last_preaction\\\\\\\"][idx] = hs[-1].float().cpu().numpy()\\\\n\\\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\\\n                    l1_attns.append(l1)\\\\n                    token_regions.append({\\\\\\\"bos\\\\\\\": (0, 1), \\\\\\\"image\\\\\\\": (img_s, img_e),\\\\n                                          \\\\\\\"text\\\\\\\": (txt_s, txt_e)})\\\\n\\\\n                    actions_arr[idx] = act\\\\n                    task_labels[idx] = ti\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 100 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Phase 1 done: {idx} samples\\\\\\\")\\\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\\\n            l1_attns, token_regions)\\\\n\\\\n\\\\ndef run_probing(reps, actions, n_seeds):\\\\n    log(\\\\\\\"Phase 2: action R2 probing\\\\\\\")\\\\n    results = {}\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            r2s = []\\\\n            for s in range(n_seeds):\\\\n                n = len(X); nt = int(n * 0.8)\\\\n                perm = np.random.RandomState(s).permutation(n)\\\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n                use_es = len(Xtr) >= 10\\\\n                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\\\n                                     early_stopping=use_es, validation_fraction=0.2 if use_es else 0.1,\\\\n                                     random_state=s, n_iter_no_change=10)\\\\n                probe.fit(Xtr, ytr)\\\\n                pred = probe.predict(Xv)\\\\n                ss_res = np.sum((yv - pred) ** 2)\\\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(r2s)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(r2s)), 4),\\\\n                \\\\\\\"values\\\\\\\": [round(v, 4) for v in r2s],\\\\n            }\\\\n        if l % 8 == 0:\\\\n            log(f\\\\\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\\\\\")\\\\n    return results\\\\n\\\\n\\\\ndef analyze_attention(l1_attns, token_regions):\\\\n    log(\\\\\\\"Phase 3: L1 attention profile\\\\\\\")\\\\n    n = len(l1_attns)\\\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\\\n\\\\n    for i in range(n):\\\\n        attn = l1_attns[i]\\\\n        tr = token_regions[i]\\\\n        last = attn.shape[1] - 1\\\\n        is_, ie = tr[\\\\\\\"image\\\\\\\"]\\\\n        ts, te = tr[\\\\\\\"text\\\\\\\"]\\\\n\\\\n        for h in range(N_HEADS):\\\\n            row = attn[h, last, :]\\\\n            img_a = row[is_:ie].sum()\\\\n            txt_a = row[ts:te].sum()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Long Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer MLP probe, 15 seeds\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_long\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_10\\\"\\n\\nTASKS = [\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\",\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\",\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\",\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\",\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\",\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\",\\n]\\nINSTRUCTIONS = [\\n    \\\"turn on the stove and put the moka pot on it\\\",\\n    \\\"put the black bowl in the bottom drawer of the cabinet and close it\\\",\\n    \\\"put the yellow and white mug in the microwave and close it\\\",\\n    \\\"put both moka pots on the stove\\\",\\n    \\\"put both the alphabet soup and the cream cheese box in the basket\\\",\\n    \\\"put both the alphabet soup and the tomato sauce in the basket\\\",\\n    \\\"put both the cream cheese box and the butter in the basket\\\",\\n    \\\"put the white mug on the left plate and put the yellow and white mug on the right plate\\\",\\n    \\\"put the white mug on the plate and put the chocolate pudding to the right of the plate\\\",\\n    \\\"pick up the book and place it in the back compartment of the caddy\\\",\\n]\\nPARAPHRASES = [\\n    \\\"switch on the stove and place the moka pot on it\\\",\\n    \\\"place the black bowl in the bottom drawer of the cabinet and shut it\\\",\\n    \\\"place the yellow and white mug in the microwave and shut it\\\",\\n    \\\"put both of the moka pots on the stove\\\",\\n    \\\"place the alphabet soup and cream cheese box into the basket\\\",\\n    \\\"place the alphabet soup and tomato sauce into the basket\\\",\\n    \\\"place the cream cheese box and butter into the basket\\\",\\n    \\\"place the white mug on the left plate and the yellow white mug on the right plate\\\",\\n    \\\"place the white mug on the plate and the chocolate pudding to the right of the plate\\\",\\n    \\\"grab the book and put it in the back section of the caddy\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef g\\n\\n... [截断: 输出过长，省略 1857 字符] ...\\n\\ntal, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(**inputs,\\n                                    output_hidden_states=True,\\n                                    output_attentions=True)\\n\\n                    seq_len = out.hidden_states[0].shape[1]\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\n                    txt_s, txt_e = img_e, seq_len\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        reps[l][\\\"last_preaction\\\"][idx] = hs[-1].float().cpu().numpy()\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append({\\\"bos\\\": (0, 1), \\\"image\\\": (img_s, img_e),\\n                                          \\\"text\\\": (txt_s, txt_e)})\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\n            l1_attns, token_regions)\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X); nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,\\n                                     early_stopping=use_es, validation_fraction=0.2 if use_es else 0.1,\\n                                     random_state=s, n_iter_no_change=10)\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 8 == 0:\\n            log(f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\")\\n    return results\\n\\n\\ndef analyze_attention(l1_attns, token_regions):\\n    log(\\\"Phase 3: L1 attention profile\\\")\\n    n = len(l1_attns)\\n    head_ratios = {h: [] for h in range(N_HEADS)}\\n\\n    for i in range(n):\\n        attn = l1_attns[i]\\n        tr = token_regions[i]\\n        last = attn.shape[1] - 1\\n        is_, ie = tr[\\\"image\\\"]\\n        ts, te = tr[\\\"text\\\"]\\n\\n        for h in range(N_HEADS):\\n            row = attn[h, last, :]\\n            img_a = row[is_:ie].sum()\\n            txt_a = row[ts:te].sum()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AinyMh1k6rX8SqYMGWKgMe`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -195 /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "0a197a74-b600-4674-b13e-8526fb784b5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzYEqQZP7EmvvdJ7zgXSuw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2134,
      "cache_read_input_tokens": 54075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2134
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

_source line 74 · 2026-05-21T05:04:48.817Z_

<details><summary>↩ Tool result · `toolu_01AinyMh1k6rX8SqYMGWKgMe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nTraceVLA-Spatial R² probing-only补跑脚本\\n\\n只跑 Phase 1 (feature extraction) + Phase 2 (R² probing)。\\n跳过 L1 attention / cross-instruction classification / counterfactual。\\n输出: RESULTS_DIR/{condition}/action_r2_probing.json\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, time\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nHIDDEN = 3072\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef find_token_regions(input_ids):\\n    ids = input_ids[0].cpu().numpy()\\n    img_positions = np.where(ids < 0)[0]\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0])\\n        img_e = int(img_positions[-1]) + 1\\n    else:\\n        img_s = img_e = 1\\n    return {\\\"bos\\\": (0, img_s), \\\"image\\\": (img_s, img_e), \\\"text\\\": (img_e, len(ids))}\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction (probing only)\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti][:60]}...\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    original_ids = inputs[\\\"input_ids\\\"].clone()\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=False,\\n                        )\\n\\n                    tr = find_token_regions(original_ids)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = (\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    actions_arr[idx] = act\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx]\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 4 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef load_model(ckpt_path, condition):\\n    log(f\\\"Loading {condition} model from {ckpt_path} ...\\\")\\n    t0 = time.time()\\n    model = AutoModelForCausalLM.from_pretrained(\\n        ckpt_path,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        attn_implementation=\\\"eager\\\",\\n    ).to(DEVICE).eval()\\n    processor = AutoProcessor.from_pretrained(\\n        ckpt_path, trust_remote_code=True, num_crops=1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "4c75eaba-a6bf-4c6d-9834-26602f33d490",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nTraceVLA-Spatial R² probing-only补跑脚本\\\\n\\\\n只跑 Phase 1 (feature extraction) + Phase 2 (R² probing)。\\\\n跳过 L1 attention / cross-instruction classification / counterfactual。\\\\n输出: RESULTS_DIR/{condition}/action_r2_probing.json\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, time\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.neural_network import MLPRegressor\\\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\\\n\\\\n# --- Checkpoints ---\\\\nTRAINED_CKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\\\\\"\\\\nUNTRAINED_CKPT = \\\\\\\"microsoft/Phi-3-vision-128k-instruct\\\\\\\"\\\\nUNTRAINED_CACHE = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\\\\\"\\\\n\\\\n# --- Data ---\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\\\\\"\\\\nRESULTS_BASE = \\\\\\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\n\\\\n# --- Architecture ---\\\\nN_LAYERS = 32\\\\nHIDDEN = 3072\\\\n\\\\n# --- Data config ---\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\",\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return (\\\\n        f\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\"\\\\n    )\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef find_token_regions(input_ids):\\\\n    ids = input_ids[0].cpu().numpy()\\\\n    img_positions = np.where(ids < 0)[0]\\\\n    if len(img_positions) > 0:\\\\n        img_s = int(img_positions[0])\\\\n        img_e = int(img_positions[-1]) + 1\\\\n    else:\\\\n        img_s = img_e = 1\\\\n    return {\\\\\\\"bos\\\\\\\": (0, img_s), \\\\\\\"image\\\\\\\": (img_s, img_e), \\\\\\\"text\\\\\\\": (img_e, len(ids))}\\\\n\\\\n\\\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\\\n    log(\\\\\\\"Phase 1: representation extraction (probing only)\\\\\\\")\\\\n    total = n_tasks * n_demos * n_timesteps\\\\n\\\\n    reps = {\\\\n        l: {\\\\n            \\\\\\\"image_mean\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n            \\\\\\\"last_preaction\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n        }\\\\n        for l in range(N_LAYERS)\\\\n    }\\\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti][:60]}...\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    original_ids = inputs[\\\\\\\"input_ids\\\\\\\"].clone()\\\\n                    with torch.no_grad():\\\\n                        out = model(\\\\n                            **inputs,\\\\n                            output_hidden_states=True,\\\\n                            output_attentions=False,\\\\n                        )\\\\n\\\\n                    tr = find_token_regions(original_ids)\\\\n                    img_s, img_e = tr[\\\\\\\"image\\\\\\\"]\\\\n\\\\n                    for l in range(N_LAYERS):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        reps[l][\\\\\\\"image_mean\\\\\\\"][idx] = (\\\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\\\n                        )\\\\n                        reps[l][\\\\\\\"last_preaction\\\\\\\"][idx] = (\\\\n                            hs[-1].float().cpu().numpy()\\\\n                        )\\\\n\\\\n                    actions_arr[idx] = act\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 100 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Phase 1 done: {idx} samples\\\\\\\")\\\\n    return reps, actions_arr[:idx]\\\\n\\\\n\\\\ndef run_probing(reps, actions, n_seeds):\\\\n    log(\\\\\\\"Phase 2: action R2 probing\\\\\\\")\\\\n    results = {}\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            r2s = []\\\\n            for s in range(n_seeds):\\\\n                n = len(X)\\\\n                nt = int(n * 0.8)\\\\n                perm = np.random.RandomState(s).permutation(n)\\\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n                use_es = len(Xtr) >= 10\\\\n                probe = MLPRegressor(\\\\n                    hidden_layer_sizes=(256,),\\\\n                    max_iter=200,\\\\n                    early_stopping=use_es,\\\\n                    validation_fraction=0.2 if use_es else 0.1,\\\\n                    random_state=s,\\\\n                    n_iter_no_change=10,\\\\n                )\\\\n                probe.fit(Xtr, ytr)\\\\n                pred = probe.predict(Xv)\\\\n                ss_res = np.sum((yv - pred) ** 2)\\\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(r2s)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(r2s)), 4),\\\\n                \\\\\\\"values\\\\\\\": [round(v, 4) for v in r2s],\\\\n            }\\\\n        if l % 4 == 0:\\\\n            log(\\\\n                f\\\\\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\\\\\"\\\\n            )\\\\n    return results\\\\n\\\\n\\\\ndef load_model(ckpt_path, condition):\\\\n    log(f\\\\\\\"Loading {condition} model from {ckpt_path} ...\\\\\\\")\\\\n    t0 = time.time()\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        ckpt_path,\\\\n        torch_dtype=torch.bfloat16,\\\\n        trust_remote_code=True,\\\\n        attn_implementation=\\\\\\\"eager\\\\\\\",\\\\n    ).to(DEVICE).eval()\\\\n    processor = AutoProcessor.from_pretrained(\\\\n        ckpt_path, trust_remote_code=True, num_crops=1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nTraceVLA-Spatial R² probing-only补跑脚本\\n\\n只跑 Phase 1 (feature extraction) + Phase 2 (R² probing)。\\n跳过 L1 attention / cross-instruction classification / counterfactual。\\n输出: RESULTS_DIR/{condition}/action_r2_probing.json\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, time\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.neural_network import MLPRegressor\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"microsoft/Phi-3-vision-128k-instruct\\\"\\nUNTRAINED_CACHE = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\\n# --- Data ---\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\\"\\nDEVICE = \\\"cuda:0\\\"\\n\\n# --- Architecture ---\\nN_LAYERS = 32\\nHIDDEN = 3072\\n\\n# --- Data config ---\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\nTASKS = [\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return (\\n        f\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n        f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n        f\\\"<|assistant|>\\\\n\\\"\\n    )\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef find_token_regions(input_ids):\\n    ids = input_ids[0].cpu().numpy()\\n    img_positions = np.where(ids < 0)[0]\\n    if len(img_positions) > 0:\\n        img_s = int(img_positions[0])\\n        img_e = int(img_positions[-1]) + 1\\n    else:\\n        img_s = img_e = 1\\n    return {\\\"bos\\\": (0, img_s), \\\"image\\\": (img_s, img_e), \\\"text\\\": (img_e, len(ids))}\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction (probing only)\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti][:60]}...\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    original_ids = inputs[\\\"input_ids\\\"].clone()\\n                    with torch.no_grad():\\n                        out = model(\\n                            **inputs,\\n                            output_hidden_states=True,\\n                            output_attentions=False,\\n                        )\\n\\n                    tr = find_token_regions(original_ids)\\n                    img_s, img_e = tr[\\\"image\\\"]\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = (\\n                            hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        )\\n                        reps[l][\\\"last_preaction\\\"][idx] = (\\n                            hs[-1].float().cpu().numpy()\\n                        )\\n\\n                    actions_arr[idx] = act\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return reps, actions_arr[:idx]\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing\\\")\\n    results = {}\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            r2s = []\\n            for s in range(n_seeds):\\n                n = len(X)\\n                nt = int(n * 0.8)\\n                perm = np.random.RandomState(s).permutation(n)\\n                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n                Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n                use_es = len(Xtr) >= 10\\n                probe = MLPRegressor(\\n                    hidden_layer_sizes=(256,),\\n                    max_iter=200,\\n                    early_stopping=use_es,\\n                    validation_fraction=0.2 if use_es else 0.1,\\n                    random_state=s,\\n                    n_iter_no_change=10,\\n                )\\n                probe.fit(Xtr, ytr)\\n                pred = probe.predict(Xv)\\n                ss_res = np.sum((yv - pred) ** 2)\\n                ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(float(np.mean(r2s)), 4),\\n                \\\"std\\\": round(float(np.std(r2s)), 4),\\n                \\\"values\\\": [round(v, 4) for v in r2s],\\n            }\\n        if l % 4 == 0:\\n            log(\\n                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n            )\\n    return results\\n\\n\\ndef load_model(ckpt_path, condition):\\n    log(f\\\"Loading {condition} model from {ckpt_path} ...\\\")\\n    t0 = time.time()\\n    model = AutoModelForCausalLM.from_pretrained(\\n        ckpt_path,\\n        torch_dtype=torch.bfloat16,\\n        trust_remote_code=True,\\n        attn_implementation=\\\"eager\\\",\\n    ).to(DEVICE).eval()\\n    processor = AutoProcessor.from_pretrained(\\n        ckpt_path, trust_remote_code=True, num_crops=1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 75_

<details><summary>Logged reasoning block</summary>

````text
Now I have a clear picture of all 7 files. I can see there are two patterns for `run_probing`:

**Pattern A (compact, single-line MLPRegressor init)** - used in:
1. `libero_object_full_pipeline.py` (line 199)
6. `libero_long_full_pipeline.py` (line 210)

```python
                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,
                                     early_stopping=use_es, validation_fraction=0.2 if use_es else 0.1,
                                     random_state=s, n_iter_no_change=10)
```

With the progress logging: `if l % 8 == 0:`

**Pattern B (multi-line MLPRegressor init)** - used in the remaining 5 files, which completes the MLPRegressor initialization with the same parameters but formatted differently across multiple lines.

The logging frequency varies by file group: nora files use `if l % 9 == 0:`, tracvla full pipelines use `if l % 8 == 0:`, tracvla probing uses `if l % 4 == 0:`, and libero files use `if l % 8 == 0:`. Now I need to write a script to handle these replacements systematically.

For the modifications, I need to update the imports to use RidgeCV instead of MLPRegressor, then refactor the run_probing function to remove the multi-seed loop and replace it with a single RidgeCV call using a fixed random state, adjusting the output format to report a single R² value rather than mean and standard deviation. I need to decide on the output format—whether to keep the same JSON structure with `mean`, `std`, and `values` keys but use a single value, or simplify it. The task specifies the format should remain unchanged, so I'll stick with `{"mean": X, "std": 0.0, "values": [X]}`. Now I'm planning to write a Python script that patches all the files by replacing the `run_probing` function with a simpler version that uses Ridge regression with a fixed random state instead of multiple seeds.

Writing the replacement function... I'm storing the R² score and logging progress every 8 layers, but I'm realizing there's a discrepancy in how sklearn's `score()` method calculates R² for multi-output regression versus the original implementation that computes it across all outputs combined. Writing the patching script... Writing the patch script... Writing the patch script... Completing the Ridge regression probe setup...

The string escaping is getting unwieldy, so I'll write the entire patch script as a heredoc directly to the server and execute it from there.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "175d12dd-8050-4ddd-bb3c-330f1e6ac927",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6QvJ7pZhJq5nhrNs5NTcq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24249,
      "cache_read_input_tokens": 56209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24249
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

_source line 76_

All 7 files read. They share the same `run_probing` pattern. Now I'll write a patch script and execute it on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "c6a9b81e-84f6-459a-ba99-d357f29d53dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6QvJ7pZhJq5nhrNs5NTcq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24249,
      "cache_read_input_tokens": 56209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24249
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

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01SyRWykoLhhBQcdE7TYq7Bi`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /tmp/patch_ridge.py << 'PYEOF'\nimport re, os\n\nfiles = [\n    \"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py\",\n]\n\nNEW_FUNC = '''def run_probing(reps, actions, n_seeds):\n    log(\"Phase 2: action R2 probing (Ridge)\")\n    results = {}\n    n = len(actions)\n    nt = int(n * 0.8)\n    perm = np.random.RandomState(42).permutation(n)\n    for l in range(N_LAYERS):\n        for pos in (\"image_mean\", \"last_preaction\"):\n            X, y = reps[l][pos], actions\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\n            Xv, yv = X[perm[nt:]], y[perm[nt:]]\n\n            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\n            probe.fit(Xtr, ytr)\n            pred = probe.predict(Xv)\n            ss_res = np.sum((yv - pred) ** 2)\n            ss_tot = np.sum((yv - yv.mean(0)) ** 2)\n            r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\n\n            results[f\"L{l}_{pos}\"] = {\n                \"mean\": round(r2, 4),\n                \"std\": 0.0,\n                \"values\": [round(r2, 4)],\n            }\n        if l % 8 == 0:\n            log(\n                f\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \"\n                f\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\"\n            )\n    return results'''\n\nfor filepath in files:\n    with open(filepath, 'r') as f:\n        content = f.read()\n\n    # 1. Replace import: MLPRegressor -> RidgeCV\n    content = content.replace(\n        'from sklearn.neural_network import MLPRegressor',\n        'from sklearn.linear_model import RidgeCV'\n    )\n\n    # 2. Replace run_probing function body\n    # Match from \"def run_probing\" to the next top-level \"def \" or end of file\n    pattern = r'(def run_probing\\(reps, actions, n_seeds\\):.*?)(?=\\ndef |\\Z)'\n    match = re.search(pattern, content, re.DOTALL)\n    if match:\n        old_func = match.group(1)\n        content = content.replace(old_func, NEW_FUNC)\n        print(f\"OK  {os.path.basename(filepath)}: replaced run_probing ({len(old_func)} -> {len(NEW_FUNC)} chars)\")\n    else:\n        print(f\"ERR {os.path.basename(filepath)}: run_probing not found!\")\n\n    # 3. Update docstring: \"MLP probe, 15 seeds\" -> \"Ridge probe\"\n    content = content.replace('per-layer MLP probe, 15 seeds', 'per-layer Ridge probe')\n    content = content.replace('Action R2 probing: per-layer MLP probe', 'Action R2 probing: per-layer Ridge probe')\n\n    with open(filepath, 'w') as f:\n        f.write(content)\n\nprint(\"\\nDone. All files patched.\")\nPYEOF\npython3 /tmp/patch_ridge.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "74381bcf-92b4-4ff6-a853-4e33a06abfde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6QvJ7pZhJq5nhrNs5NTcq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24249,
      "cache_read_input_tokens": 56209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24249
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

_source line 78 · 2026-05-21T05:05:59.853Z_

<details><summary>↩ Tool result · `toolu_01SyRWykoLhhBQcdE7TYq7Bi`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cat > /tmp/patch_ridge.py << \\\\'PYEOF\\\\'\\\\nimport re, os\\\\n\\\\nfiles = [\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py\\\",\\\\n]\\\\n\\\\nNEW_FUNC = \\\\'\\\\'\\\\'def run_probing(reps, actions, n_seeds):\\\\n    log(\\\"Phase 2: action R2 probing (Ridge)\\\")\\\\n    results = {}\\\\n    n = len(actions)\\\\n    nt = int(n * 0.8)\\\\n    perm = np.random.RandomState(42).permutation(n)\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n            Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\\\n            probe.fit(Xtr, ytr)\\\\n            pred = probe.predict(Xv)\\\\n            ss_res = np.sum((yv - pred) ** 2)\\\\n            ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n            r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\\\n\\\\n            results[f\\\"L{l}_{pos}\\\"] = {\\\\n                \\\"mean\\\": round(r2, 4),\\\\n                \\\"std\\\": 0.0,\\\\n                \\\"values\\\": [round(r2, 4)],\\\\n            }\\\\n        if l % 8 == 0:\\\\n            log(\\\\n                f\\\"  L{l}: img_mean R2={results[f\\\\'L{l}_image_mean\\\\'][\\\\'mean\\\\']:.4f}  \\\"\\\\n                f\\\"last_pre R2={results[f\\\\'L{l}_last_preaction\\\\'][\\\\'mean\\\\']:.4f}\\\"\\\\n            )\\\\n    return results\\\\'\\\\'\\\\'\\\\n\\\\nfor filepath in files:\\\\n    with open(filepath, \\\\'r\\\\') as f:\\\\n        content = f.read()\\\\n\\\\n    # 1. Replace import: MLPRegressor -> RidgeCV\\\\n    content = content.replace(\\\\n        \\\\'from sklearn.neural_network import MLPRegressor\\\\',\\\\n        \\\\'from sklearn.linear_model import RidgeCV\\\\'\\\\n    )\\\\n\\\\n    # 2. Replace run_probing function body\\\\n    # Match from \\\"def run_probing\\\" to the next top-level \\\"def \\\" or end of file\\\\n    pattern = r\\\\'(def run_probing\\\\\\\\(reps, actions, n_seeds\\\\\\\\):.*?)(?=\\\\\\\\ndef |\\\\\\\\Z)\\\\'\\\\n    match = re.search(pattern, content, re.DOTALL)\\\\n    if match:\\\\n        old_func = match.group(1)\\\\n        content = content.replace(old_func, NEW_FUNC)\\\\n        print(f\\\"OK  {os.path.basename(filepath)}: replaced run_probing ({len(old_func)} -> {len(NEW_FUNC)} chars)\\\")\\\\n    else:\\\\n        print(f\\\"ERR {os.path.basename(filepath)}: run_probing not found!\\\")\\\\n\\\\n    # 3. Update docstring: \\\"MLP probe, 15 seeds\\\" -> \\\"Ridge probe\\\"\\\\n    content = content.replace(\\\\'per-layer MLP probe, 15 seeds\\\\', \\\\'per-layer Ridge probe\\\\')\\\\n    content = content.replace(\\\\'Action R2 probing: per-layer MLP probe\\\\', \\\\'Action R2 probing: per-layer Ridge probe\\\\')\\\\n\\\\n    with open(filepath, \\\\'w\\\\') as f:\\\\n        f.write(content)\\\\n\\\\nprint(\\\"\\\\\\\\nDone. All files patched.\\\")\\\\nPYEOF\\\\npython3 /tmp/patch_ridge.py'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 75: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "c3d63a4c-0cdd-47d1-afcd-85fdd407d844",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cat > /tmp/patch_ridge.py << \\\\\\\\'PYEOF\\\\\\\\'\\\\\\\\nimport re, os\\\\\\\\n\\\\\\\\nfiles = [\\\\\\\\n    \\\\\\\"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\\\\\\",\\\\\\\\n    \\\\\\\"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\\\\\\",\\\\\\\\n    \\\\\\\"/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\\\\\\\",\\\\\\\\n    \\\\\\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\\\\\\\",\\\\\\\\n    \\\\\\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\\\\\\\",\\\\\\\\n    \\\\\\\"/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\\\\\\",\\\\\\\\n    \\\\\\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py\\\\\\\",\\\\\\\\n]\\\\\\\\n\\\\\\\\nNEW_FUNC = \\\\\\\\'\\\\\\\\'\\\\\\\\'def run_probing(reps, actions, n_seeds):\\\\\\\\n    log(\\\\\\\"Phase 2: action R2 probing (Ridge)\\\\\\\")\\\\\\\\n    results = {}\\\\\\\\n    n = len(actions)\\\\\\\\n    nt = int(n * 0.8)\\\\\\\\n    perm = np.random.RandomState(42).permutation(n)\\\\\\\\n    for l in range(N_LAYERS):\\\\\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\\\\\n            X, y = reps[l][pos], actions\\\\\\\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\\\\\n            Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\\\\\n\\\\\\\\n            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\\\\\\\n            probe.fit(Xtr, ytr)\\\\\\\\n            pred = probe.predict(Xv)\\\\\\\\n            ss_res = np.sum((yv - pred) ** 2)\\\\\\\\n            ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\\\\\n            r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\\\\\\\n\\\\\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\\\\\n                \\\\\\\"mean\\\\\\\": round(r2, 4),\\\\\\\\n                \\\\\\\"std\\\\\\\": 0.0,\\\\\\\\n                \\\\\\\"values\\\\\\\": [round(r2, 4)],\\\\\\\\n            }\\\\\\\\n        if l % 8 == 0:\\\\\\\\n            log(\\\\\\\\n                f\\\\\\\"  L{l}: img_mean R2={results[f\\\\\\\\'L{l}_image_mean\\\\\\\\'][\\\\\\\\'mean\\\\\\\\']:.4f}  \\\\\\\"\\\\\\\\n                f\\\\\\\"last_pre R2={results[f\\\\\\\\'L{l}_last_preaction\\\\\\\\'][\\\\\\\\'mean\\\\\\\\']:.4f}\\\\\\\"\\\\\\\\n            )\\\\\\\\n    return results\\\\\\\\'\\\\\\\\'\\\\\\\\'\\\\\\\\n\\\\\\\\nfor filepath in files:\\\\\\\\n    with open(filepath, \\\\\\\\'r\\\\\\\\') as f:\\\\\\\\n        content = f.read()\\\\\\\\n\\\\\\\\n    # 1. Replace import: MLPRegressor -> RidgeCV\\\\\\\\n    content = content.replace(\\\\\\\\n        \\\\\\\\'from sklearn.neural_network import MLPRegressor\\\\\\\\',\\\\\\\\n        \\\\\\\\'from sklearn.linear_model import RidgeCV\\\\\\\\'\\\\\\\\n    )\\\\\\\\n\\\\\\\\n    # 2. Replace run_probing function body\\\\\\\\n    # Match from \\\\\\\"def run_probing\\\\\\\" to the next top-level \\\\\\\"def \\\\\\\" or end of file\\\\\\\\n    pattern = r\\\\\\\\'(def run_probing\\\\\\\\\\\\\\\\(reps, actions, n_seeds\\\\\\\\\\\\\\\\):.*?)(?=\\\\\\\\\\\\\\\\ndef |\\\\\\\\\\\\\\\\Z)\\\\\\\\'\\\\\\\\n    match = re.search(pattern, content, re.DOTALL)\\\\\\\\n    if match:\\\\\\\\n        old_func = match.group(1)\\\\\\\\n        content = content.replace(old_func, NEW_FUNC)\\\\\\\\n        print(f\\\\\\\"OK  {os.path.basename(filepath)}: replaced run_probing ({len(old_func)} -> {len(NEW_FUNC)} chars)\\\\\\\")\\\\\\\\n    else:\\\\\\\\n        print(f\\\\\\\"ERR {os.path.basename(filepath)}: run_probing not found!\\\\\\\")\\\\\\\\n\\\\\\\\n    # 3. Update docstring: \\\\\\\"MLP probe, 15 seeds\\\\\\\" -> \\\\\\\"Ridge probe\\\\\\\"\\\\\\\\n    content = content.replace(\\\\\\\\'per-layer MLP probe, 15 seeds\\\\\\\\', \\\\\\\\'per-layer Ridge probe\\\\\\\\')\\\\\\\\n    content = content.replace(\\\\\\\\'Action R2 probing: per-layer MLP probe\\\\\\\\', \\\\\\\\'Action R2 probing: per-layer Ridge probe\\\\\\\\')\\\\\\\\n\\\\\\\\n    with open(filepath, \\\\\\\\'w\\\\\\\\') as f:\\\\\\\\n        f.write(content)\\\\\\\\n\\\\\\\\nprint(\\\\\\\"\\\\\\\\\\\\\\\\nDone. All files patched.\\\\\\\")\\\\\\\\nPYEOF\\\\\\\\npython3 /tmp/patch_ridge.py'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 75: python3: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cat > /tmp/patch_ridge.py << \\\\'PYEOF\\\\'\\\\nimport re, os\\\\n\\\\nfiles = [\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\\\",\\\\n    \\\"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py\\\",\\\\n]\\\\n\\\\nNEW_FUNC = \\\\'\\\\'\\\\'def run_probing(reps, actions, n_seeds):\\\\n    log(\\\"Phase 2: action R2 probing (Ridge)\\\")\\\\n    results = {}\\\\n    n = len(actions)\\\\n    nt = int(n * 0.8)\\\\n    perm = np.random.RandomState(42).permutation(n)\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n            Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\\\n            probe.fit(Xtr, ytr)\\\\n            pred = probe.predict(Xv)\\\\n            ss_res = np.sum((yv - pred) ** 2)\\\\n            ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n            r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\\\n\\\\n            results[f\\\"L{l}_{pos}\\\"] = {\\\\n                \\\"mean\\\": round(r2, 4),\\\\n                \\\"std\\\": 0.0,\\\\n                \\\"values\\\": [round(r2, 4)],\\\\n            }\\\\n        if l % 8 == 0:\\\\n            log(\\\\n                f\\\"  L{l}: img_mean R2={results[f\\\\'L{l}_image_mean\\\\'][\\\\'mean\\\\']:.4f}  \\\"\\\\n                f\\\"last_pre R2={results[f\\\\'L{l}_last_preaction\\\\'][\\\\'mean\\\\']:.4f}\\\"\\\\n            )\\\\n    return results\\\\'\\\\'\\\\'\\\\n\\\\nfor filepath in files:\\\\n    with open(filepath, \\\\'r\\\\') as f:\\\\n        content = f.read()\\\\n\\\\n    # 1. Replace import: MLPRegressor -> RidgeCV\\\\n    content = content.replace(\\\\n        \\\\'from sklearn.neural_network import MLPRegressor\\\\',\\\\n        \\\\'from sklearn.linear_model import RidgeCV\\\\'\\\\n    )\\\\n\\\\n    # 2. Replace run_probing function body\\\\n    # Match from \\\"def run_probing\\\" to the next top-level \\\"def \\\" or end of file\\\\n    pattern = r\\\\'(def run_probing\\\\\\\\(reps, actions, n_seeds\\\\\\\\):.*?)(?=\\\\\\\\ndef |\\\\\\\\Z)\\\\'\\\\n    match = re.search(pattern, content, re.DOTALL)\\\\n    if match:\\\\n        old_func = match.group(1)\\\\n        content = content.replace(old_func, NEW_FUNC)\\\\n        print(f\\\"OK  {os.path.basename(filepath)}: replaced run_probing ({len(old_func)} -> {len(NEW_FUNC)} chars)\\\")\\\\n    else:\\\\n        print(f\\\"ERR {os.path.basename(filepath)}: run_probing not found!\\\")\\\\n\\\\n    # 3. Update docstring: \\\"MLP probe, 15 seeds\\\" -> \\\"Ridge probe\\\"\\\\n    content = content.replace(\\\\'per-layer MLP probe, 15 seeds\\\\', \\\\'per-layer Ridge probe\\\\')\\\\n    content = content.replace(\\\\'Action R2 probing: per-layer MLP probe\\\\', \\\\'Action R2 probing: per-layer Ridge probe\\\\')\\\\n\\\\n    with open(filepath, \\\\'w\\\\') as f:\\\\n        f.write(content)\\\\n\\\\nprint(\\\"\\\\\\\\nDone. All files patched.\\\")\\\\nPYEOF\\\\npython3 /tmp/patch_ridge.py'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 75: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
The python3 command is not found directly. I need to use the conda environment. Let me adjust.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "82788457-14fa-4b65-a2c0-2396a04b0ec7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLt3cgtJZpSeybniY3jkvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6346,
      "cache_read_input_tokens": 80458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6346
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

_source line 80_

需要用 conda 环境的 Python。先写脚本文件，然后用 conda python 执行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "6fa35fe7-d9f7-4314-800b-477d0a57c7b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLt3cgtJZpSeybniY3jkvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6346,
      "cache_read_input_tokens": 80458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6346
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

_source line 81_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01VdmfdCEUnJxFBMkfjgvbZ7`</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && which python"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "5324e32d-7470-4558-9eda-4645efed96e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLt3cgtJZpSeybniY3jkvf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6346,
      "cache_read_input_tokens": 80458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6346
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

_source line 82 · 2026-05-21T05:06:07.141Z_

<details><summary>↩ Tool result · `toolu_01VdmfdCEUnJxFBMkfjgvbZ7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "ecf06910-ddca-49aa-b35f-d4e01ea31c04",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/miniconda3/bin/python\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.11}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_019qMdUEnWb9nczb4SZe7Mcs`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /tmp/patch_ridge.py << 'ENDOFSCRIPT'\nimport re, os\n\nfiles = [\n    \"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py\",\n    \"/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py\",\n]\n\nNEW_FUNC = (\n    'def run_probing(reps, actions, n_seeds):\\n'\n    '    log(\"Phase 2: action R2 probing (Ridge)\")\\n'\n    '    results = {}\\n'\n    '    n = len(actions)\\n'\n    '    nt = int(n * 0.8)\\n'\n    '    perm = np.random.RandomState(42).permutation(n)\\n'\n    '    for l in range(N_LAYERS):\\n'\n    '        for pos in (\"image_mean\", \"last_preaction\"):\\n'\n    '            X, y = reps[l][pos], actions\\n'\n    '            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n'\n    '            Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n'\n    '\\n'\n    '            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\n'\n    '            probe.fit(Xtr, ytr)\\n'\n    '            pred = probe.predict(Xv)\\n'\n    '            ss_res = np.sum((yv - pred) ** 2)\\n'\n    '            ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n'\n    '            r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n'\n    '\\n'\n    '            results[f\"L{l}_{pos}\"] = {\\n'\n    '                \"mean\": round(r2, 4),\\n'\n    '                \"std\": 0.0,\\n'\n    '                \"values\": [round(r2, 4)],\\n'\n    '            }\\n'\n    '        if l % 8 == 0:\\n'\n    '            log(\\n'\n    \"                f\\\"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  \\\"\\n\"\n    \"                f\\\"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}\\\"\\n\"\n    '            )\\n'\n    '    return results'\n)\n\nfor filepath in files:\n    with open(filepath, 'r') as f:\n        content = f.read()\n\n    # 1. Replace import: MLPRegressor -> RidgeCV\n    content = content.replace(\n        'from sklearn.neural_network import MLPRegressor',\n        'from sklearn.linear_model import RidgeCV'\n    )\n\n    # 2. Replace run_probing function body\n    pattern = r'(def run_probing\\(reps, actions, n_seeds\\):.*?)(?=\\ndef |\\Z)'\n    match = re.search(pattern, content, re.DOTALL)\n    if match:\n        old_func = match.group(1).rstrip()\n        content = content.replace(old_func, NEW_FUNC)\n        print(f\"OK  {os.path.basename(filepath)}: replaced run_probing ({len(old_func)} -> {len(NEW_FUNC)} chars)\")\n    else:\n        print(f\"ERR {os.path.basename(filepath)}: run_probing not found!\")\n\n    # 3. Update docstring\n    content = content.replace('per-layer MLP probe, 15 seeds', 'per-layer Ridge probe')\n\n    with open(filepath, 'w') as f:\n        f.write(content)\n\nprint(\"\\nDone. All files patched.\")\nENDOFSCRIPT\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "382aa2c7-93bb-4931-a2cb-535136c69149",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSLz2W57GG7eEVtmmzxfnd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 86804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 261
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

_source line 84 · 2026-05-21T05:06:25.107Z_

<details><summary>↩ Tool result · `toolu_019qMdUEnWb9nczb4SZe7Mcs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "397fe353-9fa3-437e-8548-c7d41160851a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Script written OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01VS3aaK3LaTyLNfQ8UyrsJd`</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /tmp/patch_ridge.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "5416794e-8bc6-4643-9df3-6f1d43ca93f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NK1L8tFTnFLnhj6a53az4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1344,
      "cache_read_input_tokens": 87065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1344
      },
      "output_tokens": 40,
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

_source line 86 · 2026-05-21T05:06:30.111Z_

<details><summary>↩ Tool result · `toolu_01VS3aaK3LaTyLNfQ8UyrsJd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"OK  libero_object_full_pipeline.py: replaced run_probing (1473 -> 1120 chars)\\nOK  nora_goal_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\nOK  nora_spatial_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\nOK  tracvla_spatial_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\nOK  tracvla_object_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\nOK  libero_long_full_pipeline.py: replaced run_probing (1473 -> 1120 chars)\\nOK  tracvla_spatial_probing_only.py: replaced run_probing (1583 -> 1120 chars)\\n\\nDone. All files patched.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "68737465-e194-47cd-9aff-61450042ebc2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"OK  libero_object_full_pipeline.py: replaced run_probing (1473 -> 1120 chars)\\\\nOK  nora_goal_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\\\nOK  nora_spatial_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\\\nOK  tracvla_spatial_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\\\nOK  tracvla_object_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\\\nOK  libero_long_full_pipeline.py: replaced run_probing (1473 -> 1120 chars)\\\\nOK  tracvla_spatial_probing_only.py: replaced run_probing (1583 -> 1120 chars)\\\\n\\\\nDone. All files patched.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"OK  libero_object_full_pipeline.py: replaced run_probing (1473 -> 1120 chars)\\nOK  nora_goal_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\nOK  nora_spatial_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\nOK  tracvla_spatial_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\nOK  tracvla_object_full_pipeline.py: replaced run_probing (1583 -> 1120 chars)\\nOK  libero_long_full_pipeline.py: replaced run_probing (1473 -> 1120 chars)\\nOK  tracvla_spatial_probing_only.py: replaced run_probing (1583 -> 1120 chars)\\n\\nDone. All files patched.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 87_

7 个文件全部替换成功。验证修改结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "19d2a1c9-98a5-4542-8dca-3e4ba7d8a22a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDKd6bJD4HjzrAn45cgqbc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 88409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 426
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

_source line 88_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WxL4sN4Bff7Ph7e1je68Ar`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"RidgeCV\\|MLPRegressor\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "5f92613e-fd96-4b9d-8b36-83c71b56054c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDKd6bJD4HjzrAn45cgqbc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 88409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 426
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

_source line 89 · 2026-05-21T05:06:34.803Z_

<details><summary>↩ Tool result · `toolu_01WxL4sN4Bff7Ph7e1je68Ar`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "87c7c974-d592-4988-a937-8f5cafa56373",
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

_source line 90_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NvjPVG6D7AwLnYDhkW4tKh`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"RidgeCV\\|MLPRegressor\" /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "f558711b-3300-4f1f-bf9a-1484dedbd63e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDKd6bJD4HjzrAn45cgqbc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 88409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 426
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

_source line 91 · 2026-05-21T05:06:35.913Z_

<details><summary>↩ Tool result · `toolu_01NvjPVG6D7AwLnYDhkW4tKh`</summary>

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
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "6e8e4123-1da3-48d0-bfb1-85addff82d6f",
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

_source line 92_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018Yp1LTvSd14StEqQ6cchPy`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -rn \"MLPRegressor\" /root/autodl-tmp/vla-ssd/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "b8e79e37-efe6-4c97-8514-df1f9e18b001",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDKd6bJD4HjzrAn45cgqbc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 88409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 426
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

_source line 93 · 2026-05-21T05:06:37.138Z_

<details><summary>↩ Tool result · `toolu_018Yp1LTvSd14StEqQ6cchPy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py.bak:28:from sklearn.neural_network import MLPRegressor\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py.bak:197:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "954937f6-630e-4fc7-b28a-2f0900d0b533",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py.bak:28:from sklearn.neural_network import MLPRegressor\\\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py.bak:197:                probe = MLPRegressor(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py.bak:28:from sklearn.neural_network import MLPRegressor\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py.bak:197:                probe = MLPRegressor(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Azxp2JTwjAsV5sqShqMTvn`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -c \"RidgeCV\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "77a4bb68-f89d-40e6-b604-549aa283dcab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDKd6bJD4HjzrAn45cgqbc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 88409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 426
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

_source line 95 · 2026-05-21T05:06:38.775Z_

<details><summary>↩ Tool result · `toolu_01Azxp2JTwjAsV5sqShqMTvn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py:2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "c217c214-a62c-4522-b376-c5e7ae5e9a36",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py:2\\\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py:2\\\\n/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py:2\\\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py:2\\\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py:2\\\\n/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py:2\\\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py:2\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py:2\\n/root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_probing_only.py:2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 96_

<details><summary>Logged reasoning block</summary>

```text
All 7 files have RidgeCV (2 occurrences each - import + usage). MLPRegressor only exists in a .bak file. Let me verify one file's run_probing function and then do the import validation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "7f05ea37-98ed-4a11-8c3b-8e98ec5f8316",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDB6fq6yTwc7kZPjz27WE2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 88835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1350
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

_source line 97_

所有 7 个文件已替换：每个文件 2 处 RidgeCV（import + 使用），MLPRegressor 仅残留在 .bak 文件中。验证 import 和函数正确性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "e7337f64-71b6-4068-a7ae-68d1399abc58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDB6fq6yTwc7kZPjz27WE2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 88835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1350
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

_source line 98_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Ai2srEtfqQTVRqVQoShGaH`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"RidgeCV\" /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "902b98c1-e98f-407e-b064-cdea65206a11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDB6fq6yTwc7kZPjz27WE2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 88835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1350
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

_source line 99_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017T2V11GvW25PQDjsFQiNtU`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -210 /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "a636abc1-731e-4b96-be1f-1516e7da5d09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDB6fq6yTwc7kZPjz27WE2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 88835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1350
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

_source line 100 · 2026-05-21T05:06:45.671Z_

<details><summary>↩ Tool result · `toolu_01Ai2srEtfqQTVRqVQoShGaH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"25:from sklearn.linear_model import RidgeCV\\n197:            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "e81ecb9b-b337-41a2-927e-35bddb3584f2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"25:from sklearn.linear_model import RidgeCV\\\\n197:            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"25:from sklearn.linear_model import RidgeCV\\n197:            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-21T05:06:46.206Z_

<details><summary>↩ Tool result · `toolu_017T2V11GvW25PQDjsFQiNtU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_object\\\"\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef generate_action(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n    input_ids = inputs[\\\"input_ids\\\"]\\n\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = torch.cat(\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\n        )\\n        if \\\"attention_mask\\\" in inputs:\\n            inputs[\\\"attention_mask\\\"] = torch.cat(\\n                (inputs[\\\"attention_mask\\\"],\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\"attention_mask\\\"].dtype)), dim=1\\n            )\\n    inputs[\\\"input_ids\\\"] = input_ids\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            max_new_tokens=7, do_sample=False,\\n        )\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n\\n    vocab_size = model.vocab_size\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\n    norm_act = model.bin_centers[disc]\\n\\n    stats = model.get_action_stats(UNNORM)\\n    mask = np.array(stats.get(\\\"mask\\\", [True] * 7))\\n    high, low = np.array(stats[\\\"q99\\\"]), np.array(stats[\\\"q01\\\"])\\n    action = np.where(mask, 0.5 * (norm_act + 1) * (high - low) + low, norm_act)\\n\\n    del inputs, gen_ids\\n    return action.astype(np.float64), token_ids\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(**inputs,\\n                                    output_hidden_states=True,\\n                                    output_attentions=True)\\n\\n                    seq_len = out.hidden_states[0].shape[1]\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\n                    txt_s, txt_e = img_e, seq_len\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        reps[l][\\\"last_preaction\\\"][idx] = hs[-1].float().cpu().numpy()\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append({\\\"bos\\\": (0, 1), \\\"image\\\": (img_s, img_e),\\n                                          \\\"text\\\": (txt_s, txt_e)})\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\n            l1_attns, token_regions)\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing (Ridge)\\\")\\n    results = {}\\n    n = len(actions)\\n    nt = int(n * 0.8)\\n    perm = np.random.RandomState(42).permutation(n)\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n            Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\n            probe.fit(Xtr, ytr)\\n            pred = probe.predict(Xv)\\n            ss_res = np.sum((yv - pred) ** 2)\\n            ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n            r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(r2, 4),\\n                \\\"std\\\": 0.0,\\n                \\\"values\\\": [round(r2, 4)],\\n            }\\n        if l % 8 == 0:\\n            log(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "836d60bb-f5cf-451e-8781-651219168692",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\\\n\\\\nPhases:\\\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\\\n  2. Action R2 probing: per-layer Ridge probe\\\\n  3. L1 attention profile: per-head instruction/image attention classification\\\\n  4. Cross-instruction classification: 10-way per-layer\\\\n  5. RSA: representational similarity across conditions\\\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\\\n\\\\nAll results -> RESULTS_DIR/*.json\\\\nNo intermediate features saved to disk.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, random, sys, time\\\\nfrom collections import defaultdict\\\\n\\\\nimport h5py\\\\nimport numpy as np\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import LogisticRegression\\\\nfrom sklearn.linear_model import RidgeCV\\\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\\\n\\\\nCKPT = \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\"\\\\nDATA = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\\\\\"\\\\nRESULTS_DIR = \\\\\\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\\\\\"\\\\nDEVICE = \\\\\\\"cuda:0\\\\\\\"\\\\nUNNORM = \\\\\\\"libero_object\\\\\\\"\\\\n\\\\nTASKS = [\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\",\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\",\\\\n]\\\\nINSTRUCTIONS = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in TASKS]\\\\nPARAPHRASES = [\\\\n    \\\\\\\"grab the alphabet soup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the cream cheese and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the salad dressing and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the bbq sauce and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the ketchup and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the tomato sauce and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the butter and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the milk and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the chocolate pudding and put it into the basket\\\\\\\",\\\\n    \\\\\\\"grab the orange juice and put it into the basket\\\\\\\",\\\\n]\\\\n\\\\nN_LAYERS = 32\\\\nN_HEADS = 32\\\\nHIDDEN = 4096\\\\nN_IMG_TOKENS = 256\\\\nN_DEMOS = 10\\\\nN_TIMESTEPS = 50\\\\nN_PROBE_SEEDS = 15\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\ndef make_prompt(instruction):\\\\n    return f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n\\\\n\\\\ndef prepare_inputs(processor, instruction, image):\\\\n    prompt = make_prompt(instruction)\\\\n    inputs = processor(prompt, image).to(DEVICE)\\\\n    if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n        inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n    return inputs\\\\n\\\\n\\\\ndef generate_action(model, processor, instruction, image):\\\\n    inputs = prepare_inputs(processor, instruction, image)\\\\n    input_ids = inputs[\\\\\\\"input_ids\\\\\\\"]\\\\n\\\\n    if not torch.all(input_ids[:, -1] == 29871):\\\\n        input_ids = torch.cat(\\\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\\\n        )\\\\n        if \\\\\\\"attention_mask\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"attention_mask\\\\\\\"] = torch.cat(\\\\n                (inputs[\\\\\\\"attention_mask\\\\\\\"],\\\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\\\\\"attention_mask\\\\\\\"].dtype)), dim=1\\\\n            )\\\\n    inputs[\\\\\\\"input_ids\\\\\\\"] = input_ids\\\\n\\\\n    with torch.no_grad():\\\\n        gen_ids = model.generate(\\\\n            inputs[\\\\\\\"input_ids\\\\\\\"],\\\\n            attention_mask=inputs.get(\\\\\\\"attention_mask\\\\\\\"),\\\\n            pixel_values=inputs.get(\\\\\\\"pixel_values\\\\\\\"),\\\\n            max_new_tokens=7, do_sample=False,\\\\n        )\\\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\\\n\\\\n    vocab_size = model.vocab_size\\\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\\\n    norm_act = model.bin_centers[disc]\\\\n\\\\n    stats = model.get_action_stats(UNNORM)\\\\n    mask = np.array(stats.get(\\\\\\\"mask\\\\\\\", [True] * 7))\\\\n    high, low = np.array(stats[\\\\\\\"q99\\\\\\\"]), np.array(stats[\\\\\\\"q01\\\\\\\"])\\\\n    action = np.where(mask, 0.5 * (norm_act + 1) * (high - low) + low, norm_act)\\\\n\\\\n    del inputs, gen_ids\\\\n    return action.astype(np.float64), token_ids\\\\n\\\\n\\\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\\\n    log(\\\\\\\"Phase 1: representation extraction\\\\\\\")\\\\n    total = n_tasks * n_demos * n_timesteps\\\\n\\\\n    reps = {\\\\n        l: {\\\\n            \\\\\\\"image_mean\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n            \\\\\\\"last_preaction\\\\\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\\\n        }\\\\n        for l in range(N_LAYERS)\\\\n    }\\\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\\\n    task_labels = np.zeros(total, dtype=np.int64)\\\\n    l1_attns = []\\\\n    token_regions = []\\\\n\\\\n    idx = 0\\\\n    for ti in range(n_tasks):\\\\n        hdf5_path = os.path.join(DATA, f\\\\\\\"{TASKS[ti]}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                n_avail = hf[demo][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\\\n                    with torch.no_grad():\\\\n                        out = model(**inputs,\\\\n                                    output_hidden_states=True,\\\\n                                    output_attentions=True)\\\\n\\\\n                    seq_len = out.hidden_states[0].shape[1]\\\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\\\n                    txt_s, txt_e = img_e, seq_len\\\\n\\\\n                    for l in range(N_LAYERS):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        reps[l][\\\\\\\"image_mean\\\\\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\\\n                        reps[l][\\\\\\\"last_preaction\\\\\\\"][idx] = hs[-1].float().cpu().numpy()\\\\n\\\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\\\n                    l1_attns.append(l1)\\\\n                    token_regions.append({\\\\\\\"bos\\\\\\\": (0, 1), \\\\\\\"image\\\\\\\": (img_s, img_e),\\\\n                                          \\\\\\\"text\\\\\\\": (txt_s, txt_e)})\\\\n\\\\n                    actions_arr[idx] = act\\\\n                    task_labels[idx] = ti\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 100 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Phase 1 done: {idx} samples\\\\\\\")\\\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\\\n            l1_attns, token_regions)\\\\n\\\\n\\\\ndef run_probing(reps, actions, n_seeds):\\\\n    log(\\\\\\\"Phase 2: action R2 probing (Ridge)\\\\\\\")\\\\n    results = {}\\\\n    n = len(actions)\\\\n    nt = int(n * 0.8)\\\\n    perm = np.random.RandomState(42).permutation(n)\\\\n    for l in range(N_LAYERS):\\\\n        for pos in (\\\\\\\"image_mean\\\\\\\", \\\\\\\"last_preaction\\\\\\\"):\\\\n            X, y = reps[l][pos], actions\\\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\\\n            Xv, yv = X[perm[nt:]], y[perm[nt:]]\\\\n\\\\n            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\\\n            probe.fit(Xtr, ytr)\\\\n            pred = probe.predict(Xv)\\\\n            ss_res = np.sum((yv - pred) ** 2)\\\\n            ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\\\n            r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\\\n\\\\n            results[f\\\\\\\"L{l}_{pos}\\\\\\\"] = {\\\\n                \\\\\\\"mean\\\\\\\": round(r2, 4),\\\\n                \\\\\\\"std\\\\\\\": 0.0,\\\\n                \\\\\\\"values\\\\\\\": [round(r2, 4)],\\\\n            }\\\\n        if l % 8 == 0:\\\\n            log(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Object Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nCKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_object\\\"\\nRESULTS_DIR = \\\"/root/autodl-tmp/vla-ssd/results/libero_object\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM = \\\"libero_object\\\"\\n\\nTASKS = [\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\",\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\",\\n]\\nINSTRUCTIONS = [t.replace(\\\"_\\\", \\\" \\\") for t in TASKS]\\nPARAPHRASES = [\\n    \\\"grab the alphabet soup and put it into the basket\\\",\\n    \\\"grab the cream cheese and put it into the basket\\\",\\n    \\\"grab the salad dressing and put it into the basket\\\",\\n    \\\"grab the bbq sauce and put it into the basket\\\",\\n    \\\"grab the ketchup and put it into the basket\\\",\\n    \\\"grab the tomato sauce and put it into the basket\\\",\\n    \\\"grab the butter and put it into the basket\\\",\\n    \\\"grab the milk and put it into the basket\\\",\\n    \\\"grab the chocolate pudding and put it into the basket\\\",\\n    \\\"grab the orange juice and put it into the basket\\\",\\n]\\n\\nN_LAYERS = 32\\nN_HEADS = 32\\nHIDDEN = 4096\\nN_IMG_TOKENS = 256\\nN_DEMOS = 10\\nN_TIMESTEPS = 50\\nN_PROBE_SEEDS = 15\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef make_prompt(instruction):\\n    return f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n\\n\\ndef prepare_inputs(processor, instruction, image):\\n    prompt = make_prompt(instruction)\\n    inputs = processor(prompt, image).to(DEVICE)\\n    if \\\"pixel_values\\\" in inputs:\\n        inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n    return inputs\\n\\n\\ndef generate_action(model, processor, instruction, image):\\n    inputs = prepare_inputs(processor, instruction, image)\\n    input_ids = inputs[\\\"input_ids\\\"]\\n\\n    if not torch.all(input_ids[:, -1] == 29871):\\n        input_ids = torch.cat(\\n            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1\\n        )\\n        if \\\"attention_mask\\\" in inputs:\\n            inputs[\\\"attention_mask\\\"] = torch.cat(\\n                (inputs[\\\"attention_mask\\\"],\\n                 torch.ones(1, 1, device=DEVICE, dtype=inputs[\\\"attention_mask\\\"].dtype)), dim=1\\n            )\\n    inputs[\\\"input_ids\\\"] = input_ids\\n\\n    with torch.no_grad():\\n        gen_ids = model.generate(\\n            inputs[\\\"input_ids\\\"],\\n            attention_mask=inputs.get(\\\"attention_mask\\\"),\\n            pixel_values=inputs.get(\\\"pixel_values\\\"),\\n            max_new_tokens=7, do_sample=False,\\n        )\\n    token_ids = gen_ids[0, -7:].cpu().numpy()\\n\\n    vocab_size = model.vocab_size\\n    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)\\n    norm_act = model.bin_centers[disc]\\n\\n    stats = model.get_action_stats(UNNORM)\\n    mask = np.array(stats.get(\\\"mask\\\", [True] * 7))\\n    high, low = np.array(stats[\\\"q99\\\"]), np.array(stats[\\\"q01\\\"])\\n    action = np.where(mask, 0.5 * (norm_act + 1) * (high - low) + low, norm_act)\\n\\n    del inputs, gen_ids\\n    return action.astype(np.float64), token_ids\\n\\n\\ndef extract_features(model, processor, n_tasks, n_demos, n_timesteps):\\n    log(\\\"Phase 1: representation extraction\\\")\\n    total = n_tasks * n_demos * n_timesteps\\n\\n    reps = {\\n        l: {\\n            \\\"image_mean\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n            \\\"last_preaction\\\": np.zeros((total, HIDDEN), dtype=np.float32),\\n        }\\n        for l in range(N_LAYERS)\\n    }\\n    actions_arr = np.zeros((total, 7), dtype=np.float32)\\n    task_labels = np.zeros(total, dtype=np.int64)\\n    l1_attns = []\\n    token_regions = []\\n\\n    idx = 0\\n    for ti in range(n_tasks):\\n        hdf5_path = os.path.join(DATA, f\\\"{TASKS[ti]}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{n_tasks}: {TASKS[ti]}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo = f\\\"data/demo_{di}\\\"\\n                n_avail = hf[demo][\\\"actions\\\"].shape[0]\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)\\n                    with torch.no_grad():\\n                        out = model(**inputs,\\n                                    output_hidden_states=True,\\n                                    output_attentions=True)\\n\\n                    seq_len = out.hidden_states[0].shape[1]\\n                    img_s, img_e = 1, 1 + N_IMG_TOKENS\\n                    txt_s, txt_e = img_e, seq_len\\n\\n                    for l in range(N_LAYERS):\\n                        hs = out.hidden_states[l + 1][0]\\n                        reps[l][\\\"image_mean\\\"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()\\n                        reps[l][\\\"last_preaction\\\"][idx] = hs[-1].float().cpu().numpy()\\n\\n                    l1 = out.attentions[1][0].float().cpu().numpy()\\n                    l1_attns.append(l1)\\n                    token_regions.append({\\\"bos\\\": (0, 1), \\\"image\\\": (img_s, img_e),\\n                                          \\\"text\\\": (txt_s, txt_e)})\\n\\n                    actions_arr[idx] = act\\n                    task_labels[idx] = ti\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 100 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total}\\\")\\n\\n    log(f\\\"Phase 1 done: {idx} samples\\\")\\n    return (reps, actions_arr[:idx], task_labels[:idx],\\n            l1_attns, token_regions)\\n\\n\\ndef run_probing(reps, actions, n_seeds):\\n    log(\\\"Phase 2: action R2 probing (Ridge)\\\")\\n    results = {}\\n    n = len(actions)\\n    nt = int(n * 0.8)\\n    perm = np.random.RandomState(42).permutation(n)\\n    for l in range(N_LAYERS):\\n        for pos in (\\\"image_mean\\\", \\\"last_preaction\\\"):\\n            X, y = reps[l][pos], actions\\n            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]\\n            Xv, yv = X[perm[nt:]], y[perm[nt:]]\\n\\n            probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])\\n            probe.fit(Xtr, ytr)\\n            pred = probe.predict(Xv)\\n            ss_res = np.sum((yv - pred) ** 2)\\n            ss_tot = np.sum((yv - yv.mean(0)) ** 2)\\n            r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n\\n            results[f\\\"L{l}_{pos}\\\"] = {\\n                \\\"mean\\\": round(r2, 4),\\n                \\\"std\\\": 0.0,\\n                \\\"values\\\": [round(r2, 4)],\\n            }\\n        if l % 8 == 0:\\n            log(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 102_

替换正确。验证 RidgeCV import 在两个环境下可用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "668a1003-aee7-40eb-8df9-d242aafe5b65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NK2fXg88fFJ2NM7nsbLrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 90185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3887
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

_source line 103_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Lfn5xq2aTRyhJEtLKsFAGB`</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"from sklearn.linear_model import RidgeCV; print('RidgeCV OK in conda base')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "1784d6b5-ebf7-4e64-b620-b7bd409c224e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NK2fXg88fFJ2NM7nsbLrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 90185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3887
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

_source line 104_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01KQ5HcAaoX4emWM51tnAGCm`</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/autodl-tmp/vla-ssd/envs/nora/bin/activate && python -c \"from sklearn.linear_model import RidgeCV; print('RidgeCV OK in NORA venv')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "3f5c8bfa-b0dd-4141-b85c-ad0407933500",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NK2fXg88fFJ2NM7nsbLrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 90185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3887
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

_source line 105 · 2026-05-21T05:06:53.053Z_

<details><summary>↩ Tool result · `toolu_01Lfn5xq2aTRyhJEtLKsFAGB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"RidgeCV OK in conda base\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "7ce6f531-085b-4ed2-9165-cdc4184fea5e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"RidgeCV OK in conda base\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"RidgeCV OK in conda base\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-21T05:06:54.493Z_

<details><summary>↩ Tool result · `toolu_01KQ5HcAaoX4emWM51tnAGCm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"RidgeCV OK in NORA venv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "a922a4df-cd51-4cdd-b572-1a76b5ded923",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"RidgeCV OK in NORA venv\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"RidgeCV OK in NORA venv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 107_

两个环境 RidgeCV import 均通过。

## 完成总结

### 修改了 7 个文件

| # | 文件 | 修改内容 |
|---|------|---------|
| 1 | `libero_object_full_pipeline.py` | import + run_probing |
| 2 | `nora_goal_full_pipeline.py` | import + run_probing |
| 3 | `nora_spatial_full_pipeline.py` | import + run_probing |
| 4 | `tracvla_spatial_full_pipeline.py` | import + run_probing |
| 5 | `tracvla_object_full_pipeline.py` | import + run_probing |
| 6 | `libero_long_full_pipeline.py` | import + run_probing |
| 7 | `tracvla_spatial_probing_only.py` | import + run_probing |

### 每个文件的具体修改

1. **Import**: `from sklearn.neural_network import MLPRegressor` → `from sklearn.linear_model import RidgeCV`
2. **run_probing 函数**:
   - MLPRegressor(hidden_layer_sizes=(256,), ...) → RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])
   - 去掉 15-seed 循环，改为单次 train/test split（固定 random_state=42）
   - R² 计算方式不变（全局 ss_res/ss_tot，保持与 MLP 版本可比性）
   - 输出 JSON 格式不变：`{"mean": X, "std": 0.0, "values": [X]}`
3. **Docstring**: `per-layer MLP probe, 15 seeds` → `per-layer Ridge probe`

### 验证结果

- conda base 环境：RidgeCV OK
- NORA venv 环境：RidgeCV OK

### 重提交命令

**cuda:0 — OpenVLA Object:**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
```

**cuda:1 — NORA Goal:**
```bash
bash -c "source /root/autodl-tmp/vla-ssd/envs/nora/bin/activate && python /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py --conditions trained untrained"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "uuid": "9c87a53e-0ccf-42d0-9fcf-0ebfc0b9e764",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYNyjWUgVCKa2MpzVsZK7F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 94072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
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

_source line 108_

两个环境 RidgeCV import 均通过。

## 完成总结

### 修改了 7 个文件

| # | 文件 | 修改内容 |
|---|------|---------|
| 1 | `libero_object_full_pipeline.py` | import + run_probing |
| 2 | `nora_goal_full_pipeline.py` | import + run_probing |
| 3 | `nora_spatial_full_pipeline.py` | import + run_probing |
| 4 | `tracvla_spatial_full_pipeline.py` | import + run_probing |
| 5 | `tracvla_object_full_pipeline.py` | import + run_probing |
| 6 | `libero_long_full_pipeline.py` | import + run_probing |
| 7 | `tracvla_spatial_probing_only.py` | import + run_probing |

### 每个文件的具体修改

1. **Import**: `from sklearn.neural_network import MLPRegressor` → `from sklearn.linear_model import RidgeCV`
2. **run_probing 函数**:
   - MLPRegressor(hidden_layer_sizes=(256,), ...) → RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])
   - 去掉 15-seed 循环，改为单次 train/test split（固定 random_state=42）
   - R² 计算方式不变（全局 ss_res/ss_tot，保持与 MLP 版本可比性）
   - 输出 JSON 格式不变：`{"mean": X, "std": 0.0, "values": [X]}`
3. **Docstring**: `per-layer MLP probe, 15 seeds` → `per-layer Ridge probe`

### 验证结果

- conda base 环境：RidgeCV OK
- NORA venv 环境：RidgeCV OK

### 重提交命令

**cuda:0 — OpenVLA Object:**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
```

**cuda:1 — NORA Goal:**
```bash
bash -c "source /root/autodl-tmp/vla-ssd/envs/nora/bin/activate && python /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py --conditions trained untrained"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 230094,
  "duration_api_ms": 223416,
  "num_turns": 44,
  "stop_reason": "end_turn",
  "session_id": "c89b8496-ddd9-45eb-a7ff-f962678306e3",
  "total_cost_usd": 1.29849775,
  "usage": {
    "input_tokens": 19,
    "cache_creation_input_tokens": 82735,
    "cache_read_input_tokens": 919210,
    "output_tokens": 12765,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 82735,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 688,
        "cache_read_input_tokens": 94072,
        "cache_creation_input_tokens": 504,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 504
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2484,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002579,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 19,
      "outputTokens": 12765,
      "cacheReadInputTokens": 919210,
      "cacheCreationInputTokens": 82735,
      "webSearchRequests": 0,
      "costUSD": 1.29591875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6d66eae1-55d5-4c63-9c19-98f5d5a6a37b"
}
```

</details>

---
