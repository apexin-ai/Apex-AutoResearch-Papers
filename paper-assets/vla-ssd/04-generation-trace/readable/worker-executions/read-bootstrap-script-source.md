# read bootstrap script source

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_read_bootstrap_script_source_20260522T200549.log`
- **Structured JSON:** [`8a3ecb321b08fe805356.json`](../../sessions/8a/8a3ecb321b08fe805356.json)

## Before a recorded user message

28 recorded events

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
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
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
  "uuid": "240dd581-01d5-4e96-9f0e-b613f28e9606",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779484800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bcd85177-be82-4980-a8a3-509e062cc148",
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f"
}
```

---

### Tool call

_source line 4_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018A9pSXHCfacA2u1X8GHTE6`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "f957d5c3-0548-42c9-b6d4-1e9c15a92034",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017n5JCdQhd98DCrsuRBAW78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11056,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11056
      },
      "output_tokens": 34,
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

_source line 5 · 2026-05-22T20:06:00.773Z_

<details><summary>↩ Tool result · `toolu_018A9pSXHCfacA2u1X8GHTE6`</summary>

````text
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
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "0be87b1a-1c48-4ae1-91cb-5d7fbefcef55",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QnSypMJzqafKz35mE5m6KF`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "5e2b1c9f-0a93-4631-9919-dbb12689e7ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xieqD1ABJcUxuNDQUQwGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 22897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 427
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

_source line 7 · 2026-05-22T20:06:13.950Z_

<details><summary>↩ Tool result · `toolu_01QnSypMJzqafKz35mE5m6KF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n      \\n\\n... [截断: 输出过长，省略 9531 字符] ...\\n\\nt_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\", \\\"long\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    suite_data_name = \\\"libero_10\\\" if args.suite == \\\"long\\\" else f\\\"libero_{args.suite}\\\"\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "7e685aa1-b7eb-4948-a3bf-6a4cc9378fe6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"long\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"long\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n      \\\\n\\\\n... [截断: 输出过长，省略 9531 字符] ...\\\\n\\\\nt_l]\\\\n    deltas = peak_r2_boot - exit_r2_boot\\\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\\\n\\\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\\\n\\\\n    return {\\\\n        \\\\\\\"per_layer_r2\\\\\\\": {f\\\\\\\"L{l}\\\\\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\\\n        \\\\\\\"peak_r2\\\\\\\": round(canon_r2[canon_peak_l], 4),\\\\n        \\\\\\\"peak_layer\\\\\\\": f\\\\\\\"L{canon_peak_l}\\\\\\\",\\\\n        \\\\\\\"exit_r2\\\\\\\": round(canon_r2[exit_l], 4),\\\\n        \\\\\\\"exit_layer\\\\\\\": f\\\\\\\"L{exit_l}\\\\\\\",\\\\n        \\\\\\\"delta\\\\\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\\\n        \\\\\\\"delta_ci_95\\\\\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\\\n        \\\\\\\"bootstrap_deltas_summary\\\\\\\": {\\\\n            \\\\\\\"mean\\\\\\\": round(float(np.mean(deltas)), 4),\\\\n            \\\\\\\"std\\\\\\\": round(float(np.std(deltas)), 4),\\\\n            \\\\\\\"median\\\\\\\": round(float(np.median(deltas)), 4),\\\\n        },\\\\n    }\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--arch\\\\\\\", required=True, choices=[\\\\\\\"openvla\\\\\\\", \\\\\\\"tracvla\\\\\\\", \\\\\\\"nora\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", required=True, choices=[\\\\\\\"goal\\\\\\\", \\\\\\\"spatial\\\\\\\", \\\\\\\"object\\\\\\\", \\\\\\\"long\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--condition\\\\\\\", required=True, choices=[\\\\\\\"trained\\\\\\\", \\\\\\\"untrained\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--n_bootstrap\\\\\\\", type=int, default=10000)\\\\n    p.add_argument(\\\\\\\"--n_demos\\\\\\\", type=int, default=10)\\\\n    p.add_argument(\\\\\\\"--n_timesteps\\\\\\\", type=int, default=50)\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\",\\\\n                   default=\\\\\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--dry_run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    args = p.parse_args()\\\\n\\\\n    if args.dry_run:\\\\n        args.n_demos = 2\\\\n        args.n_timesteps = 5\\\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\\\n\\\\n    if args.suite not in CKPT.get(args.arch, {}):\\\\n        log(f\\\\\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n    if args.condition not in CKPT[args.arch][args.suite]:\\\\n        log(f\\\\\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    device = f\\\\\\\"cuda:{args.gpu}\\\\\\\"\\\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\\\n    suite_data_name = \\\\\\\"libero_10\\\\\\\" if args.suite == \\\\\\\"long\\\\\\\" else f\\\\\\\"libero_{args.suite}\\\\\\\"\\\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\\\n\\\\n    log(f\\\\\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\\\\\")\\\\n    log(f\\\\\\\"Checkpoint: {ckpt_path}\\\\\\\")\\\\n    log(f\\\\\\\"Data: {data_dir}\\\\\\\")\\\\n    log(f\\\\\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\\\\\")\\\\n    if args.dry_run:\\\\n        log(\\\\\\\"DRY RUN\\\\\\\")\\\\n\\\\n    tasks, instructions = discover_tasks(data_dir)\\\\n    if args.dry_run:\\\\n        tasks = tasks[:2]\\\\n        instructions = instructions[:2]\\\\n    log(f\\\\\\\"Tasks: {len(tasks)}\\\\\\\")\\\\n\\\\n    model, processor = load_model(args.arch, ckpt_path, device)\\\\n\\\\n    t0 = time.time()\\\\n    features, actions, demo_ids = extract_features(\\\\n        args.arch, model, processor, tasks, instructions, data_dir,\\\\n        device, args.n_demos, args.n_timesteps)\\\\n    log(f\\\\\\\"Extraction: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n    del model, processor\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    n_layers = ARCH_INFO[args.arch][\\\\\\\"n_layers\\\\\\\"]\\\\n    result = clustered_bootstrap_r2(\\\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\\\n    log(f\\\\\\\"Bootstrap: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    result[\\\\\\\"arch\\\\\\\"] = args.arch\\\\n    result[\\\\\\\"suite\\\\\\\"] = args.suite\\\\n    result[\\\\\\\"condition\\\\\\\"] = args.condition\\\\n    result[\\\\\\\"n_demos\\\\\\\"] = int(len(np.unique(demo_ids)))\\\\n    result[\\\\\\\"n_total_samples\\\\\\\"] = int(len(actions))\\\\n    result[\\\\\\\"n_bootstrap\\\\\\\"] = args.n_bootstrap\\\\n    result[\\\\\\\"dry_run\\\\\\\"] = args.dry_run\\\\n\\\\n    out_dir = os.path.join(args.output_dir, f\\\\\\\"{args.arch}_{args.suite}\\\\\\\")\\\\n    os.makedirs(out_dir, exist_ok=True)\\\\n    out_path = os.path.join(out_dir, f\\\\\\\"{args.condition}.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(result, f, indent=2)\\\\n    log(f\\\\\\\"Saved: {out_path}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.19}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n      \\n\\n... [截断: 输出过长，省略 9531 字符] ...\\n\\nt_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\", \\\"long\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    suite_data_name = \\\"libero_10\\\" if args.suite == \\\"long\\\" else f\\\"libero_{args.suite}\\\"\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated. I need to get the full file. Let me check the file size first and then read it in parts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "18e3cd48-5e8f-4bb7-8a56-935719c75f15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjULnEeepE9U4kkxcmMcXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3910,
      "cache_read_input_tokens": 23324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3910
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

_source line 9_

输出被截断了，分段读取完整内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "1989c0d2-5bea-47b6-9d44-727883327c98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjULnEeepE9U4kkxcmMcXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3910,
      "cache_read_input_tokens": 23324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3910
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016kG6BLH6U6TQsygsvCR55r`</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "9a51dccf-8e48-4091-b475-97f537b977e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjULnEeepE9U4kkxcmMcXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3910,
      "cache_read_input_tokens": 23324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3910
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

_source line 11 · 2026-05-22T20:06:22.404Z_

<details><summary>↩ Tool result · `toolu_016kG6BLH6U6TQsygsvCR55r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"435 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "e496514a-6b15-44f1-9a29-0fab5578c512",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"435 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"435 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XZsWhXoFiNcQHWpdGk6hb1`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -150 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "aa9b0ec8-366a-46c6-8c7a-323de7930460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Zq6xJHFh86S5j7r18XF5P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 27234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 13 · 2026-05-22T20:06:34.200Z_

<details><summary>↩ Tool result · `toolu_01XZsWhXoFiNcQHWpdGk6hb1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(arch, ckpt_path, device):\\n    log(f\\\"Loading {arch} from {ckpt_path}\\\")\\n    t0 = time.time()\\n\\n    if arch == \\\"openvla\\\":\\n        _load_openvla_modules(ckpt_path)\\n        config_cls = sys.modules[\\\"configuration_prismatic\\\"].OpenVLAConfig\\n        model_cls = sys.modules[\\\"modeling_prismatic\\\"].OpenVLAForActionPrediction\\n        proc_cls = sys.modules[\\\"processing_prismatic\\\"].PrismaticProcessor\\n\\n        config = config_cls.from_pretrained(ckpt_path)\\n        model = model_cls.from_pretrained(\\n            ckpt_path, config=config, dtype=torch.bfloat16\\n        ).to(device).eval()\\n        # Patch transformers.tokenization_utils for HF cache loading\\n        import transformers.tokenization_utils_base as _tub\\n        from transformers.utils import PaddingStrategy as _PS\\n        _tu = sys.modules[\\\"transformers.tokenization_utils\\\"]\\n        _tu.PaddingStrategy = _PS\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\n        _tu.TextInput = _tub.TextInput\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "a9b11ed0-9a9a-4972-847a-33e677c522b4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"long\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"long\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        src = src.replace(\\\\n            \\\\\\\"def tie_weights(self) -> None:\\\\\\\",\\\\n            \\\\\\\"def tie_weights(self, **kwargs) -> None:\\\\\\\"\\\\n        )\\\\n        code = compile(src, fpath, \\\\\\\"exec\\\\\\\")\\\\n        exec(code, sys.modules[full].__dict__)\\\\n\\\\n\\\\ndef load_model(arch, ckpt_path, device):\\\\n    log(f\\\\\\\"Loading {arch} from {ckpt_path}\\\\\\\")\\\\n    t0 = time.time()\\\\n\\\\n    if arch == \\\\\\\"openvla\\\\\\\":\\\\n        _load_openvla_modules(ckpt_path)\\\\n        config_cls = sys.modules[\\\\\\\"configuration_prismatic\\\\\\\"].OpenVLAConfig\\\\n        model_cls = sys.modules[\\\\\\\"modeling_prismatic\\\\\\\"].OpenVLAForActionPrediction\\\\n        proc_cls = sys.modules[\\\\\\\"processing_prismatic\\\\\\\"].PrismaticProcessor\\\\n\\\\n        config = config_cls.from_pretrained(ckpt_path)\\\\n        model = model_cls.from_pretrained(\\\\n            ckpt_path, config=config, dtype=torch.bfloat16\\\\n        ).to(device).eval()\\\\n        # Patch transformers.tokenization_utils for HF cache loading\\\\n        import transformers.tokenization_utils_base as _tub\\\\n        from transformers.utils import PaddingStrategy as _PS\\\\n        _tu = sys.modules[\\\\\\\"transformers.tokenization_utils\\\\\\\"]\\\\n        _tu.PaddingStrategy = _PS\\\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\\\n        _tu.TextInput = _tub.TextInput\\\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n        ds_path = os.path.join(ckpt_path, \\\\\\\"dataset_statistics.json\\\\\\\")\\\\n        if os.path.exists(ds_path):\\\\n            with open(ds_path) as f:\\\\n                ds_stats = json.load(f)\\\\n            for k, v in ds_stats.items():\\\\n                if k not in model.norm_stats:\\\\n                    model.norm_stats[k] = v\\\\n\\\\n    elif arch == \\\\\\\"tracvla\\\\\\\":\\\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\\\n        model = AutoModelForCausalLM.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    elif arch == \\\\\\\"nora\\\\\\\":\\\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\\\n        model = AutoModelForImageTextToText.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    log(f\\\\\\\"  Loaded in {time.time()-t0:.1f}s\\\\\\\")\\\\n    return model, processor\\\\n\\\\n\\\\ndef prepare_inputs(arch, processor, instruction, image, device):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.54}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(arch, ckpt_path, device):\\n    log(f\\\"Loading {arch} from {ckpt_path}\\\")\\n    t0 = time.time()\\n\\n    if arch == \\\"openvla\\\":\\n        _load_openvla_modules(ckpt_path)\\n        config_cls = sys.modules[\\\"configuration_prismatic\\\"].OpenVLAConfig\\n        model_cls = sys.modules[\\\"modeling_prismatic\\\"].OpenVLAForActionPrediction\\n        proc_cls = sys.modules[\\\"processing_prismatic\\\"].PrismaticProcessor\\n\\n        config = config_cls.from_pretrained(ckpt_path)\\n        model = model_cls.from_pretrained(\\n            ckpt_path, config=config, dtype=torch.bfloat16\\n        ).to(device).eval()\\n        # Patch transformers.tokenization_utils for HF cache loading\\n        import transformers.tokenization_utils_base as _tub\\n        from transformers.utils import PaddingStrategy as _PS\\n        _tu = sys.modules[\\\"transformers.tokenization_utils\\\"]\\n        _tu.PaddingStrategy = _PS\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\n        _tu.TextInput = _tub.TextInput\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F1iU7BhVQTt9uvMBXbUtiP`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -300 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "3069b1e6-f871-4e3a-8747-0ff8d6cb3daf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TiWCEfVQLwMYZw7k61nHHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2957,
      "cache_read_input_tokens": 27507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2957
      },
      "output_tokens": 42,
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

_source line 15 · 2026-05-22T20:06:41.021Z_

<details><summary>↩ Tool result · `toolu_01F1iU7BhVQTt9uvMBXbUtiP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n      \\n\\n... [截断: 输出过长，省略 4506 字符] ...\\n\\n \\\") for t in tasks]\\n    return tasks, instructions\\n\\n\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\n                     device, n_demos, n_timesteps):\\n    info = ARCH_INFO[arch]\\n    n_layers = info[\\\"n_layers\\\"]\\n    hidden = info[\\\"hidden\\\"]\\n    total = len(tasks) * n_demos * n_timesteps\\n\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\n    actions = np.zeros((total, 7), dtype=np.float32)\\n    demo_ids = np.zeros(total, dtype=np.int64)\\n\\n    idx = 0\\n    gd = 0\\n\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\n        hdf5_path = os.path.join(data_dir, f\\\"{task}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{len(tasks)}: {task}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo_key = f\\\"data/demo_{di}\\\"\\n                if demo_key not in hf:\\n                    gd += 1\\n                    continue\\n                n_avail = hf[demo_key][\\\"actions\\\"].shape[0]\\n\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo_key}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo_key}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\n                    with torch.no_grad():\\n                        out = model(**inputs, output_hidden_states=True)\\n\\n                    for l in range(n_layers):\\n                        hs = out.hidden_states[l + 1][0]\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\n\\n                    actions[idx] = act\\n                    demo_ids[idx] = gd\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 50 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total} samples\\\")\\n\\n                gd += 1\\n\\n    log(f\\\"  Extraction done: {idx} samples, {gd} demos\\\")\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\n    return features, actions[:idx], demo_ids[:idx]\\n\\n\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\n    unique_demos = np.unique(demo_ids)\\n    n_total = len(unique_demos)\\n    n_train = int(0.8 * n_total)\\n    log(f\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\")\\n\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\n\\n    rng = np.random.RandomState(seed)\\n    canon_perm = rng.permutation(unique_demos)\\n    canon_train = set(canon_perm[:n_train].tolist())\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\n    test_mask = ~train_mask\\n\\n    y_tr_canon = actions[train_mask]\\n    y_te_canon = actions[test_mask]\\n\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\n    best_alpha = {}\\n    canon_r2 = {}\\n\\n    log(\\\"  Canonical split -- fitting RidgeCV per layer...\\\")\\n    for l in range(n_layers):\\n        probe = RidgeCV(alphas=alphas_list)\\n        probe.fit(features[l][train_mask], y_tr_canon)\\n        best_alpha[l] = float(probe.alpha_)\\n        pred = probe.predict(features[l][test_mask])\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n\\n    # Precompute kernel matrices per layer for efficient bootstrap\\n    log(\\\"  Precomputing kernel matrices...\\\")\\n    N = len(actions)\\n    kernels = {}\\n    for l in range(n_layers):\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\n\\n    log(f\\\"  Bootstrap ({n_bootstrap} iterations)...\\\")\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\n    rng2 = np.random.RandomState(seed + 1)\\n    report_every = max(1, n_bootstrap // 10)\\n\\n    for b in range(n_bootstrap):\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\n        tr_demos = resampled[:n_train]\\n        te_demos = resampled[n_train:]\\n\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "1c3f31c4-6ff1-49b5-883d-f8c147e4e49f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"long\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"long\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n      \\\\n\\\\n... [截断: 输出过长，省略 4506 字符] ...\\\\n\\\\n \\\\\\\") for t in tasks]\\\\n    return tasks, instructions\\\\n\\\\n\\\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\\\n                     device, n_demos, n_timesteps):\\\\n    info = ARCH_INFO[arch]\\\\n    n_layers = info[\\\\\\\"n_layers\\\\\\\"]\\\\n    hidden = info[\\\\\\\"hidden\\\\\\\"]\\\\n    total = len(tasks) * n_demos * n_timesteps\\\\n\\\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\\\n    actions = np.zeros((total, 7), dtype=np.float32)\\\\n    demo_ids = np.zeros(total, dtype=np.int64)\\\\n\\\\n    idx = 0\\\\n    gd = 0\\\\n\\\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\\\n        hdf5_path = os.path.join(data_dir, f\\\\\\\"{task}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{len(tasks)}: {task}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo_key = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                if demo_key not in hf:\\\\n                    gd += 1\\\\n                    continue\\\\n                n_avail = hf[demo_key][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo_key}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo_key}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\\\n                    with torch.no_grad():\\\\n                        out = model(**inputs, output_hidden_states=True)\\\\n\\\\n                    for l in range(n_layers):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\\\n\\\\n                    actions[idx] = act\\\\n                    demo_ids[idx] = gd\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 50 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total} samples\\\\\\\")\\\\n\\\\n                gd += 1\\\\n\\\\n    log(f\\\\\\\"  Extraction done: {idx} samples, {gd} demos\\\\\\\")\\\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\\\n    return features, actions[:idx], demo_ids[:idx]\\\\n\\\\n\\\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\\\n    unique_demos = np.unique(demo_ids)\\\\n    n_total = len(unique_demos)\\\\n    n_train = int(0.8 * n_total)\\\\n    log(f\\\\\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\\\\\")\\\\n\\\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\\\n\\\\n    rng = np.random.RandomState(seed)\\\\n    canon_perm = rng.permutation(unique_demos)\\\\n    canon_train = set(canon_perm[:n_train].tolist())\\\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\\\n    test_mask = ~train_mask\\\\n\\\\n    y_tr_canon = actions[train_mask]\\\\n    y_te_canon = actions[test_mask]\\\\n\\\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\\\n    best_alpha = {}\\\\n    canon_r2 = {}\\\\n\\\\n    log(\\\\\\\"  Canonical split -- fitting RidgeCV per layer...\\\\\\\")\\\\n    for l in range(n_layers):\\\\n        probe = RidgeCV(alphas=alphas_list)\\\\n        probe.fit(features[l][train_mask], y_tr_canon)\\\\n        best_alpha[l] = float(probe.alpha_)\\\\n        pred = probe.predict(features[l][test_mask])\\\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\\\n\\\\n    # Precompute kernel matrices per layer for efficient bootstrap\\\\n    log(\\\\\\\"  Precomputing kernel matrices...\\\\\\\")\\\\n    N = len(actions)\\\\n    kernels = {}\\\\n    for l in range(n_layers):\\\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\\\n\\\\n    log(f\\\\\\\"  Bootstrap ({n_bootstrap} iterations)...\\\\\\\")\\\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\\\n    rng2 = np.random.RandomState(seed + 1)\\\\n    report_every = max(1, n_bootstrap // 10)\\\\n\\\\n    for b in range(n_bootstrap):\\\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\\\n        tr_demos = resampled[:n_train]\\\\n        te_demos = resampled[n_train:]\\\\n\\\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.56}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n      \\n\\n... [截断: 输出过长，省略 4506 字符] ...\\n\\n \\\") for t in tasks]\\n    return tasks, instructions\\n\\n\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\n                     device, n_demos, n_timesteps):\\n    info = ARCH_INFO[arch]\\n    n_layers = info[\\\"n_layers\\\"]\\n    hidden = info[\\\"hidden\\\"]\\n    total = len(tasks) * n_demos * n_timesteps\\n\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\n    actions = np.zeros((total, 7), dtype=np.float32)\\n    demo_ids = np.zeros(total, dtype=np.int64)\\n\\n    idx = 0\\n    gd = 0\\n\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\n        hdf5_path = os.path.join(data_dir, f\\\"{task}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{len(tasks)}: {task}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo_key = f\\\"data/demo_{di}\\\"\\n                if demo_key not in hf:\\n                    gd += 1\\n                    continue\\n                n_avail = hf[demo_key][\\\"actions\\\"].shape[0]\\n\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo_key}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo_key}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\n                    with torch.no_grad():\\n                        out = model(**inputs, output_hidden_states=True)\\n\\n                    for l in range(n_layers):\\n                        hs = out.hidden_states[l + 1][0]\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\n\\n                    actions[idx] = act\\n                    demo_ids[idx] = gd\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 50 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total} samples\\\")\\n\\n                gd += 1\\n\\n    log(f\\\"  Extraction done: {idx} samples, {gd} demos\\\")\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\n    return features, actions[:idx], demo_ids[:idx]\\n\\n\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\n    unique_demos = np.unique(demo_ids)\\n    n_total = len(unique_demos)\\n    n_train = int(0.8 * n_total)\\n    log(f\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\")\\n\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\n\\n    rng = np.random.RandomState(seed)\\n    canon_perm = rng.permutation(unique_demos)\\n    canon_train = set(canon_perm[:n_train].tolist())\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\n    test_mask = ~train_mask\\n\\n    y_tr_canon = actions[train_mask]\\n    y_te_canon = actions[test_mask]\\n\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\n    best_alpha = {}\\n    canon_r2 = {}\\n\\n    log(\\\"  Canonical split -- fitting RidgeCV per layer...\\\")\\n    for l in range(n_layers):\\n        probe = RidgeCV(alphas=alphas_list)\\n        probe.fit(features[l][train_mask], y_tr_canon)\\n        best_alpha[l] = float(probe.alpha_)\\n        pred = probe.predict(features[l][test_mask])\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n\\n    # Precompute kernel matrices per layer for efficient bootstrap\\n    log(\\\"  Precomputing kernel matrices...\\\")\\n    N = len(actions)\\n    kernels = {}\\n    for l in range(n_layers):\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\n\\n    log(f\\\"  Bootstrap ({n_bootstrap} iterations)...\\\")\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\n    rng2 = np.random.RandomState(seed + 1)\\n    report_every = max(1, n_bootstrap // 10)\\n\\n    for b in range(n_bootstrap):\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\n        tr_demos = resampled[:n_train]\\n        te_demos = resampled[n_train:]\\n\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015gssuEhQTxmm1eH8J5Xi3p`</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -150 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "ed41c923-ad3d-4b8c-9769-18128f6ae355",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01137xw5e5DqnzZqyGbwCirY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3632,
      "cache_read_input_tokens": 30464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3632
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

_source line 17 · 2026-05-22T20:06:49.476Z_

<details><summary>↩ Tool result · `toolu_015gssuEhQTxmm1eH8J5Xi3p`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    kernels = {}\\n    for l in range(n_layers):\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\n\\n    log(f\\\"  Bootstrap ({n_bootstrap} iterations)...\\\")\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\n    rng2 = np.random.RandomState(seed + 1)\\n    report_every = max(1, n_bootstrap // 10)\\n\\n    for b in range(n_bootstrap):\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\n        tr_demos = resampled[:n_train]\\n        te_demos = resampled[n_train:]\\n\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\n\\n        if len(te_idx) == 0:\\n            continue\\n\\n        y_tr = actions[tr_idx]\\n        y_te = actions[te_idx]\\n        y_te_mean = y_te.mean(axis=0)\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\n        if ss_tot < 1e-10:\\n            continue\\n\\n        n_tr = len(tr_idx)\\n        for l in range(n_layers):\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\n            try:\\n                w = np.linalg.solve(K_tr, y_tr)\\n                pred = K_te_tr @ w\\n                ss_res = np.sum((y_te - pred) ** 2)\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\n            except np.linalg.LinAlgError:\\n                boot_r2[b, l] = 0.0\\n\\n        if (b + 1) % report_every == 0:\\n            log(f\\\"    {b+1}/{n_bootstrap}\\\")\\n\\n    exit_l = n_layers - 1\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\n    exit_r2_boot = boot_r2[:, exit_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\", \\\"long\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    suite_data_name = \\\"libero_10\\\" if args.suite == \\\"long\\\" else f\\\"libero_{args.suite}\\\"\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "cf93eaf7-df91-415f-b3ac-5c1dc32ce03f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    kernels = {}\\\\n    for l in range(n_layers):\\\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\\\n\\\\n    log(f\\\\\\\"  Bootstrap ({n_bootstrap} iterations)...\\\\\\\")\\\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\\\n    rng2 = np.random.RandomState(seed + 1)\\\\n    report_every = max(1, n_bootstrap // 10)\\\\n\\\\n    for b in range(n_bootstrap):\\\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\\\n        tr_demos = resampled[:n_train]\\\\n        te_demos = resampled[n_train:]\\\\n\\\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\\\n\\\\n        if len(te_idx) == 0:\\\\n            continue\\\\n\\\\n        y_tr = actions[tr_idx]\\\\n        y_te = actions[te_idx]\\\\n        y_te_mean = y_te.mean(axis=0)\\\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\\\n        if ss_tot < 1e-10:\\\\n            continue\\\\n\\\\n        n_tr = len(tr_idx)\\\\n        for l in range(n_layers):\\\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\\\n            try:\\\\n                w = np.linalg.solve(K_tr, y_tr)\\\\n                pred = K_te_tr @ w\\\\n                ss_res = np.sum((y_te - pred) ** 2)\\\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\\\n            except np.linalg.LinAlgError:\\\\n                boot_r2[b, l] = 0.0\\\\n\\\\n        if (b + 1) % report_every == 0:\\\\n            log(f\\\\\\\"    {b+1}/{n_bootstrap}\\\\\\\")\\\\n\\\\n    exit_l = n_layers - 1\\\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\\\n    exit_r2_boot = boot_r2[:, exit_l]\\\\n    deltas = peak_r2_boot - exit_r2_boot\\\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\\\n\\\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\\\n\\\\n    return {\\\\n        \\\\\\\"per_layer_r2\\\\\\\": {f\\\\\\\"L{l}\\\\\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\\\n        \\\\\\\"peak_r2\\\\\\\": round(canon_r2[canon_peak_l], 4),\\\\n        \\\\\\\"peak_layer\\\\\\\": f\\\\\\\"L{canon_peak_l}\\\\\\\",\\\\n        \\\\\\\"exit_r2\\\\\\\": round(canon_r2[exit_l], 4),\\\\n        \\\\\\\"exit_layer\\\\\\\": f\\\\\\\"L{exit_l}\\\\\\\",\\\\n        \\\\\\\"delta\\\\\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\\\n        \\\\\\\"delta_ci_95\\\\\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\\\n        \\\\\\\"bootstrap_deltas_summary\\\\\\\": {\\\\n            \\\\\\\"mean\\\\\\\": round(float(np.mean(deltas)), 4),\\\\n            \\\\\\\"std\\\\\\\": round(float(np.std(deltas)), 4),\\\\n            \\\\\\\"median\\\\\\\": round(float(np.median(deltas)), 4),\\\\n        },\\\\n    }\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--arch\\\\\\\", required=True, choices=[\\\\\\\"openvla\\\\\\\", \\\\\\\"tracvla\\\\\\\", \\\\\\\"nora\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", required=True, choices=[\\\\\\\"goal\\\\\\\", \\\\\\\"spatial\\\\\\\", \\\\\\\"object\\\\\\\", \\\\\\\"long\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--condition\\\\\\\", required=True, choices=[\\\\\\\"trained\\\\\\\", \\\\\\\"untrained\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--n_bootstrap\\\\\\\", type=int, default=10000)\\\\n    p.add_argument(\\\\\\\"--n_demos\\\\\\\", type=int, default=10)\\\\n    p.add_argument(\\\\\\\"--n_timesteps\\\\\\\", type=int, default=50)\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\",\\\\n                   default=\\\\\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--dry_run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    args = p.parse_args()\\\\n\\\\n    if args.dry_run:\\\\n        args.n_demos = 2\\\\n        args.n_timesteps = 5\\\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\\\n\\\\n    if args.suite not in CKPT.get(args.arch, {}):\\\\n        log(f\\\\\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n    if args.condition not in CKPT[args.arch][args.suite]:\\\\n        log(f\\\\\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    device = f\\\\\\\"cuda:{args.gpu}\\\\\\\"\\\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\\\n    suite_data_name = \\\\\\\"libero_10\\\\\\\" if args.suite == \\\\\\\"long\\\\\\\" else f\\\\\\\"libero_{args.suite}\\\\\\\"\\\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\\\n\\\\n    log(f\\\\\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\\\\\")\\\\n    log(f\\\\\\\"Checkpoint: {ckpt_path}\\\\\\\")\\\\n    log(f\\\\\\\"Data: {data_dir}\\\\\\\")\\\\n    log(f\\\\\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\\\\\")\\\\n    if args.dry_run:\\\\n        log(\\\\\\\"DRY RUN\\\\\\\")\\\\n\\\\n    tasks, instructions = discover_tasks(data_dir)\\\\n    if args.dry_run:\\\\n        tasks = tasks[:2]\\\\n        instructions = instructions[:2]\\\\n    log(f\\\\\\\"Tasks: {len(tasks)}\\\\\\\")\\\\n\\\\n    model, processor = load_model(args.arch, ckpt_path, device)\\\\n\\\\n    t0 = time.time()\\\\n    features, actions, demo_ids = extract_features(\\\\n        args.arch, model, processor, tasks, instructions, data_dir,\\\\n        device, args.n_demos, args.n_timesteps)\\\\n    log(f\\\\\\\"Extraction: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n    del model, processor\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    n_layers = ARCH_INFO[args.arch][\\\\\\\"n_layers\\\\\\\"]\\\\n    result = clustered_bootstrap_r2(\\\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\\\n    log(f\\\\\\\"Bootstrap: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    result[\\\\\\\"arch\\\\\\\"] = args.arch\\\\n    result[\\\\\\\"suite\\\\\\\"] = args.suite\\\\n    result[\\\\\\\"condition\\\\\\\"] = args.condition\\\\n    result[\\\\\\\"n_demos\\\\\\\"] = int(len(np.unique(demo_ids)))\\\\n    result[\\\\\\\"n_total_samples\\\\\\\"] = int(len(actions))\\\\n    result[\\\\\\\"n_bootstrap\\\\\\\"] = args.n_bootstrap\\\\n    result[\\\\\\\"dry_run\\\\\\\"] = args.dry_run\\\\n\\\\n    out_dir = os.path.join(args.output_dir, f\\\\\\\"{args.arch}_{args.suite}\\\\\\\")\\\\n    os.makedirs(out_dir, exist_ok=True)\\\\n    out_path = os.path.join(out_dir, f\\\\\\\"{args.condition}.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(result, f, indent=2)\\\\n    log(f\\\\\\\"Saved: {out_path}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    kernels = {}\\n    for l in range(n_layers):\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\n\\n    log(f\\\"  Bootstrap ({n_bootstrap} iterations)...\\\")\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\n    rng2 = np.random.RandomState(seed + 1)\\n    report_every = max(1, n_bootstrap // 10)\\n\\n    for b in range(n_bootstrap):\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\n        tr_demos = resampled[:n_train]\\n        te_demos = resampled[n_train:]\\n\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\n\\n        if len(te_idx) == 0:\\n            continue\\n\\n        y_tr = actions[tr_idx]\\n        y_te = actions[te_idx]\\n        y_te_mean = y_te.mean(axis=0)\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\n        if ss_tot < 1e-10:\\n            continue\\n\\n        n_tr = len(tr_idx)\\n        for l in range(n_layers):\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\n            try:\\n                w = np.linalg.solve(K_tr, y_tr)\\n                pred = K_te_tr @ w\\n                ss_res = np.sum((y_te - pred) ** 2)\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\n            except np.linalg.LinAlgError:\\n                boot_r2[b, l] = 0.0\\n\\n        if (b + 1) % report_every == 0:\\n            log(f\\\"    {b+1}/{n_bootstrap}\\\")\\n\\n    exit_l = n_layers - 1\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\n    exit_r2_boot = boot_r2[:, exit_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\", \\\"long\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    suite_data_name = \\\"libero_10\\\" if args.suite == \\\"long\\\" else f\\\"libero_{args.suite}\\\"\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
I still have a gap in the middle. Let me get lines 150-300 to fill in the missing part.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "02a49153-069e-4ab9-9ad2-98d3540ffd9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERDncPhXjtPsomheffLrn5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 34096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

_source line 19_

中间部分还有截断，补上缺失段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "be0180d2-2222-46cc-a45c-799aa1550c5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERDncPhXjtPsomheffLrn5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 34096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CG2bcAHPfsTwScL6jP5Wvi`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -220 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "e5333faa-dcf7-4531-95c1-92bb50519e99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERDncPhXjtPsomheffLrn5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 34096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

_source line 21 · 2026-05-22T20:06:56.773Z_

<details><summary>↩ Tool result · `toolu_01CG2bcAHPfsTwScL6jP5Wvi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n      \\n\\n... [截断: 输出过长，省略 1412 字符] ...\\n\\nined(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n    if arch == \\\"openvla\\\":\\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n        inputs = processor(prompt, image).to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        ids = inputs[\\\"input_ids\\\"]\\n        if not torch.all(ids[:, -1] == 29871):\\n            ids = torch.cat(\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\n            if \\\"attention_mask\\\" in inputs:\\n                inputs[\\\"attention_mask\\\"] = torch.cat(\\n                    (inputs[\\\"attention_mask\\\"],\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\"attention_mask\\\"].dtype)),\\n                    dim=1)\\n        inputs[\\\"input_ids\\\"] = ids\\n        return inputs\\n\\n    elif arch == \\\"tracvla\\\":\\n        prompt = (\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n                  f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n                  \\\"<|assistant|>\\\\n\\\")\\n        inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        return inputs\\n\\n    elif arch == \\\"nora\\\":\\n        messages = [{\\\"role\\\": \\\"user\\\", \\\"content\\\": [\\n            {\\\"type\\\": \\\"image\\\", \\\"image\\\": image},\\n            {\\\"type\\\": \\\"text\\\", \\\"text\\\": instruction},\\n        ]}]\\n        text = processor.apply_chat_template(\\n            messages, tokenize=False, add_generation_prompt=True)\\n        inputs = processor(text=[text], images=[image], return_tensors=\\\"pt\\\", padding=True)\\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\\n                for k, v in inputs.items()}\\n\\n\\ndef discover_tasks(data_dir):\\n    tasks = []\\n    for f in sorted(os.listdir(data_dir)):\\n        if f.endswith(\\\"_demo.hdf5\\\"):\\n            tasks.append(f.replace(\\\"_demo.hdf5\\\", \\\"\\\"))\\n    instructions = [t.replace(\\\"_\\\", \\\" \\\") for t in tasks]\\n    return tasks, instructions\\n\\n\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\n                     device, n_demos, n_timesteps):\\n    info = ARCH_INFO[arch]\\n    n_layers = info[\\\"n_layers\\\"]\\n    hidden = info[\\\"hidden\\\"]\\n    total = len(tasks) * n_demos * n_timesteps\\n\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\n    actions = np.zeros((total, 7), dtype=np.float32)\\n    demo_ids = np.zeros(total, dtype=np.int64)\\n\\n    idx = 0\\n    gd = 0\\n\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\n        hdf5_path = os.path.join(data_dir, f\\\"{task}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{len(tasks)}: {task}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo_key = f\\\"data/demo_{di}\\\"\\n                if demo_key not in hf:\\n                    gd += 1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "64ea63c8-3ff9-453b-9f08-8ae8709365ee",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"long\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"long\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n      \\\\n\\\\n... [截断: 输出过长，省略 1412 字符] ...\\\\n\\\\nined(ckpt_path, trust_remote_code=True)\\\\n\\\\n        ds_path = os.path.join(ckpt_path, \\\\\\\"dataset_statistics.json\\\\\\\")\\\\n        if os.path.exists(ds_path):\\\\n            with open(ds_path) as f:\\\\n                ds_stats = json.load(f)\\\\n            for k, v in ds_stats.items():\\\\n                if k not in model.norm_stats:\\\\n                    model.norm_stats[k] = v\\\\n\\\\n    elif arch == \\\\\\\"tracvla\\\\\\\":\\\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\\\n        model = AutoModelForCausalLM.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    elif arch == \\\\\\\"nora\\\\\\\":\\\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\\\n        model = AutoModelForImageTextToText.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    log(f\\\\\\\"  Loaded in {time.time()-t0:.1f}s\\\\\\\")\\\\n    return model, processor\\\\n\\\\n\\\\ndef prepare_inputs(arch, processor, instruction, image, device):\\\\n    if arch == \\\\\\\"openvla\\\\\\\":\\\\n        prompt = f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n        inputs = processor(prompt, image).to(device)\\\\n        if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n        ids = inputs[\\\\\\\"input_ids\\\\\\\"]\\\\n        if not torch.all(ids[:, -1] == 29871):\\\\n            ids = torch.cat(\\\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\\\n            if \\\\\\\"attention_mask\\\\\\\" in inputs:\\\\n                inputs[\\\\\\\"attention_mask\\\\\\\"] = torch.cat(\\\\n                    (inputs[\\\\\\\"attention_mask\\\\\\\"],\\\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\\\\\"attention_mask\\\\\\\"].dtype)),\\\\n                    dim=1)\\\\n        inputs[\\\\\\\"input_ids\\\\\\\"] = ids\\\\n        return inputs\\\\n\\\\n    elif arch == \\\\\\\"tracvla\\\\\\\":\\\\n        prompt = (\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n                  f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n                  \\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\")\\\\n        inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(device)\\\\n        if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n        return inputs\\\\n\\\\n    elif arch == \\\\\\\"nora\\\\\\\":\\\\n        messages = [{\\\\\\\"role\\\\\\\": \\\\\\\"user\\\\\\\", \\\\\\\"content\\\\\\\": [\\\\n            {\\\\\\\"type\\\\\\\": \\\\\\\"image\\\\\\\", \\\\\\\"image\\\\\\\": image},\\\\n            {\\\\\\\"type\\\\\\\": \\\\\\\"text\\\\\\\", \\\\\\\"text\\\\\\\": instruction},\\\\n        ]}]\\\\n        text = processor.apply_chat_template(\\\\n            messages, tokenize=False, add_generation_prompt=True)\\\\n        inputs = processor(text=[text], images=[image], return_tensors=\\\\\\\"pt\\\\\\\", padding=True)\\\\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\\\\n                for k, v in inputs.items()}\\\\n\\\\n\\\\ndef discover_tasks(data_dir):\\\\n    tasks = []\\\\n    for f in sorted(os.listdir(data_dir)):\\\\n        if f.endswith(\\\\\\\"_demo.hdf5\\\\\\\"):\\\\n            tasks.append(f.replace(\\\\\\\"_demo.hdf5\\\\\\\", \\\\\\\"\\\\\\\"))\\\\n    instructions = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in tasks]\\\\n    return tasks, instructions\\\\n\\\\n\\\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\\\n                     device, n_demos, n_timesteps):\\\\n    info = ARCH_INFO[arch]\\\\n    n_layers = info[\\\\\\\"n_layers\\\\\\\"]\\\\n    hidden = info[\\\\\\\"hidden\\\\\\\"]\\\\n    total = len(tasks) * n_demos * n_timesteps\\\\n\\\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\\\n    actions = np.zeros((total, 7), dtype=np.float32)\\\\n    demo_ids = np.zeros(total, dtype=np.int64)\\\\n\\\\n    idx = 0\\\\n    gd = 0\\\\n\\\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\\\n        hdf5_path = os.path.join(data_dir, f\\\\\\\"{task}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{len(tasks)}: {task}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo_key = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                if demo_key not in hf:\\\\n                    gd += 1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"long\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n      \\n\\n... [截断: 输出过长，省略 1412 字符] ...\\n\\nined(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n    if arch == \\\"openvla\\\":\\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n        inputs = processor(prompt, image).to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        ids = inputs[\\\"input_ids\\\"]\\n        if not torch.all(ids[:, -1] == 29871):\\n            ids = torch.cat(\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\n            if \\\"attention_mask\\\" in inputs:\\n                inputs[\\\"attention_mask\\\"] = torch.cat(\\n                    (inputs[\\\"attention_mask\\\"],\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\"attention_mask\\\"].dtype)),\\n                    dim=1)\\n        inputs[\\\"input_ids\\\"] = ids\\n        return inputs\\n\\n    elif arch == \\\"tracvla\\\":\\n        prompt = (\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n                  f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n                  \\\"<|assistant|>\\\\n\\\")\\n        inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        return inputs\\n\\n    elif arch == \\\"nora\\\":\\n        messages = [{\\\"role\\\": \\\"user\\\", \\\"content\\\": [\\n            {\\\"type\\\": \\\"image\\\", \\\"image\\\": image},\\n            {\\\"type\\\": \\\"text\\\", \\\"text\\\": instruction},\\n        ]}]\\n        text = processor.apply_chat_template(\\n            messages, tokenize=False, add_generation_prompt=True)\\n        inputs = processor(text=[text], images=[image], return_tensors=\\\"pt\\\", padding=True)\\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\\n                for k, v in inputs.items()}\\n\\n\\ndef discover_tasks(data_dir):\\n    tasks = []\\n    for f in sorted(os.listdir(data_dir)):\\n        if f.endswith(\\\"_demo.hdf5\\\"):\\n            tasks.append(f.replace(\\\"_demo.hdf5\\\", \\\"\\\"))\\n    instructions = [t.replace(\\\"_\\\", \\\" \\\") for t in tasks]\\n    return tasks, instructions\\n\\n\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\n                     device, n_demos, n_timesteps):\\n    info = ARCH_INFO[arch]\\n    n_layers = info[\\\"n_layers\\\"]\\n    hidden = info[\\\"hidden\\\"]\\n    total = len(tasks) * n_demos * n_timesteps\\n\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\n    actions = np.zeros((total, 7), dtype=np.float32)\\n    demo_ids = np.zeros(total, dtype=np.int64)\\n\\n    idx = 0\\n    gd = 0\\n\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\n        hdf5_path = os.path.join(data_dir, f\\\"{task}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{len(tasks)}: {task}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo_key = f\\\"data/demo_{di}\\\"\\n                if demo_key not in hf:\\n                    gd += 1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
I'm still missing the section from around line 90 to 110 (the second loop in `_load_openvla_modules` and the beginning of `load_model`). Let me try to get just that part.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "964f9e32-0742-494b-addc-f84330eee78b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGAedbUHo9S5yu3afT6o1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 36807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3654
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

_source line 23_

还差中间一小段，精确读取。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "6aeb80cc-280b-46bc-9736-c17b9e54923d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGAedbUHo9S5yu3afT6o1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 36807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3654
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HQ3C2UXh27zRuvq2imvaai`</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +90 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "af5557c2-8d61-42a0-a35f-f1c629fc2d04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGAedbUHo9S5yu3afT6o1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 36807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3654
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

_source line 25 · 2026-05-22T20:07:04.860Z_

<details><summary>↩ Tool result · `toolu_01HQ3C2UXh27zRuvq2imvaai`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(arch, ckpt_path, device):\\n    log(f\\\"Loading {arch} from {ckpt_path}\\\")\\n    t0 = time.time()\\n\\n    if arch == \\\"openvla\\\":\\n        _load_openvla_modules(ckpt_path)\\n        config_cls = sys.modules[\\\"configuration_prismatic\\\"].OpenVLAConfig\\n        model_cls = sys.modules[\\\"modeling_prismatic\\\"].OpenVLAForActionPrediction\\n        proc_cls = sys.modules[\\\"processing_prismatic\\\"].PrismaticProcessor\\n\\n        config = config_cls.from_pretrained(ckpt_path)\\n        model = model_cls.from_pretrained(\\n            ckpt_path, config=config, dtype=torch.bfloat16\\n        ).to(device).eval()\\n        # Patch transformers.tokenization_utils for HF cache loading\\n        import transformers.tokenization_utils_base as _tub\\n        from transformers.utils import PaddingStrategy as _PS\\n        _tu = sys.modules[\\\"transformers.tokenization_utils\\\"]\\n        _tu.PaddingStrategy = _PS\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\n        _tu.TextInput = _tub.TextInput\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n    if arch == \\\"openvla\\\":\\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n        inputs = processor(prompt, image).to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        ids = inputs[\\\"input_ids\\\"]\\n        if not torch.all(ids[:, -1] == 29871):\\n            ids = torch.cat(\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\n            if \\\"attention_mask\\\" in inputs:\\n                inputs[\\\"attention_mask\\\"] = torch.cat(\\n                    (inputs[\\\"attention_mask\\\"],\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\"attention_mask\\\"].dtype)),\\n                    dim=1)\\n        inputs[\\\"input_ids\\\"] = ids\\n        return inputs\\n\\n    elif arch == \\\"tracvla\\\":\\n        prompt = (\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n                  f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n                  \\\"<|assistant|>\\\\n\\\")\\n        inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        return inputs\\n\\n    elif arch == \\\"nora\\\":\\n        messages = [{\\\"role\\\": \\\"user\\\", \\\"content\\\": [\\n            {\\\"type\\\": \\\"image\\\", \\\"image\\\": image},\\n            {\\\"type\\\": \\\"text\\\", \\\"text\\\": instruction},\\n        ]}]\\n        text = process\\n\\n... [截断: 输出过长，省略 5537 字符] ...\\n\\nt_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\", \\\"long\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    suite_data_name = \\\"libero_10\\\" if args.suite == \\\"long\\\" else f\\\"libero_{args.suite}\\\"\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "f7433dc7-50e4-4df0-826d-713552cf9fc4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        src = src.replace(\\\\n            \\\\\\\"def tie_weights(self) -> None:\\\\\\\",\\\\n            \\\\\\\"def tie_weights(self, **kwargs) -> None:\\\\\\\"\\\\n        )\\\\n        code = compile(src, fpath, \\\\\\\"exec\\\\\\\")\\\\n        exec(code, sys.modules[full].__dict__)\\\\n\\\\n\\\\ndef load_model(arch, ckpt_path, device):\\\\n    log(f\\\\\\\"Loading {arch} from {ckpt_path}\\\\\\\")\\\\n    t0 = time.time()\\\\n\\\\n    if arch == \\\\\\\"openvla\\\\\\\":\\\\n        _load_openvla_modules(ckpt_path)\\\\n        config_cls = sys.modules[\\\\\\\"configuration_prismatic\\\\\\\"].OpenVLAConfig\\\\n        model_cls = sys.modules[\\\\\\\"modeling_prismatic\\\\\\\"].OpenVLAForActionPrediction\\\\n        proc_cls = sys.modules[\\\\\\\"processing_prismatic\\\\\\\"].PrismaticProcessor\\\\n\\\\n        config = config_cls.from_pretrained(ckpt_path)\\\\n        model = model_cls.from_pretrained(\\\\n            ckpt_path, config=config, dtype=torch.bfloat16\\\\n        ).to(device).eval()\\\\n        # Patch transformers.tokenization_utils for HF cache loading\\\\n        import transformers.tokenization_utils_base as _tub\\\\n        from transformers.utils import PaddingStrategy as _PS\\\\n        _tu = sys.modules[\\\\\\\"transformers.tokenization_utils\\\\\\\"]\\\\n        _tu.PaddingStrategy = _PS\\\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\\\n        _tu.TextInput = _tub.TextInput\\\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n        ds_path = os.path.join(ckpt_path, \\\\\\\"dataset_statistics.json\\\\\\\")\\\\n        if os.path.exists(ds_path):\\\\n            with open(ds_path) as f:\\\\n                ds_stats = json.load(f)\\\\n            for k, v in ds_stats.items():\\\\n                if k not in model.norm_stats:\\\\n                    model.norm_stats[k] = v\\\\n\\\\n    elif arch == \\\\\\\"tracvla\\\\\\\":\\\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\\\n        model = AutoModelForCausalLM.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    elif arch == \\\\\\\"nora\\\\\\\":\\\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\\\n        model = AutoModelForImageTextToText.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    log(f\\\\\\\"  Loaded in {time.time()-t0:.1f}s\\\\\\\")\\\\n    return model, processor\\\\n\\\\n\\\\ndef prepare_inputs(arch, processor, instruction, image, device):\\\\n    if arch == \\\\\\\"openvla\\\\\\\":\\\\n        prompt = f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n        inputs = processor(prompt, image).to(device)\\\\n        if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n        ids = inputs[\\\\\\\"input_ids\\\\\\\"]\\\\n        if not torch.all(ids[:, -1] == 29871):\\\\n            ids = torch.cat(\\\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\\\n            if \\\\\\\"attention_mask\\\\\\\" in inputs:\\\\n                inputs[\\\\\\\"attention_mask\\\\\\\"] = torch.cat(\\\\n                    (inputs[\\\\\\\"attention_mask\\\\\\\"],\\\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\\\\\"attention_mask\\\\\\\"].dtype)),\\\\n                    dim=1)\\\\n        inputs[\\\\\\\"input_ids\\\\\\\"] = ids\\\\n        return inputs\\\\n\\\\n    elif arch == \\\\\\\"tracvla\\\\\\\":\\\\n        prompt = (\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n                  f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n                  \\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\")\\\\n        inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(device)\\\\n        if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n        return inputs\\\\n\\\\n    elif arch == \\\\\\\"nora\\\\\\\":\\\\n        messages = [{\\\\\\\"role\\\\\\\": \\\\\\\"user\\\\\\\", \\\\\\\"content\\\\\\\": [\\\\n            {\\\\\\\"type\\\\\\\": \\\\\\\"image\\\\\\\", \\\\\\\"image\\\\\\\": image},\\\\n            {\\\\\\\"type\\\\\\\": \\\\\\\"text\\\\\\\", \\\\\\\"text\\\\\\\": instruction},\\\\n        ]}]\\\\n        text = process\\\\n\\\\n... [截断: 输出过长，省略 5537 字符] ...\\\\n\\\\nt_l]\\\\n    deltas = peak_r2_boot - exit_r2_boot\\\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\\\n\\\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\\\n\\\\n    return {\\\\n        \\\\\\\"per_layer_r2\\\\\\\": {f\\\\\\\"L{l}\\\\\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\\\n        \\\\\\\"peak_r2\\\\\\\": round(canon_r2[canon_peak_l], 4),\\\\n        \\\\\\\"peak_layer\\\\\\\": f\\\\\\\"L{canon_peak_l}\\\\\\\",\\\\n        \\\\\\\"exit_r2\\\\\\\": round(canon_r2[exit_l], 4),\\\\n        \\\\\\\"exit_layer\\\\\\\": f\\\\\\\"L{exit_l}\\\\\\\",\\\\n        \\\\\\\"delta\\\\\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\\\n        \\\\\\\"delta_ci_95\\\\\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\\\n        \\\\\\\"bootstrap_deltas_summary\\\\\\\": {\\\\n            \\\\\\\"mean\\\\\\\": round(float(np.mean(deltas)), 4),\\\\n            \\\\\\\"std\\\\\\\": round(float(np.std(deltas)), 4),\\\\n            \\\\\\\"median\\\\\\\": round(float(np.median(deltas)), 4),\\\\n        },\\\\n    }\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--arch\\\\\\\", required=True, choices=[\\\\\\\"openvla\\\\\\\", \\\\\\\"tracvla\\\\\\\", \\\\\\\"nora\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", required=True, choices=[\\\\\\\"goal\\\\\\\", \\\\\\\"spatial\\\\\\\", \\\\\\\"object\\\\\\\", \\\\\\\"long\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--condition\\\\\\\", required=True, choices=[\\\\\\\"trained\\\\\\\", \\\\\\\"untrained\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--n_bootstrap\\\\\\\", type=int, default=10000)\\\\n    p.add_argument(\\\\\\\"--n_demos\\\\\\\", type=int, default=10)\\\\n    p.add_argument(\\\\\\\"--n_timesteps\\\\\\\", type=int, default=50)\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\",\\\\n                   default=\\\\\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--dry_run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    args = p.parse_args()\\\\n\\\\n    if args.dry_run:\\\\n        args.n_demos = 2\\\\n        args.n_timesteps = 5\\\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\\\n\\\\n    if args.suite not in CKPT.get(args.arch, {}):\\\\n        log(f\\\\\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n    if args.condition not in CKPT[args.arch][args.suite]:\\\\n        log(f\\\\\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    device = f\\\\\\\"cuda:{args.gpu}\\\\\\\"\\\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\\\n    suite_data_name = \\\\\\\"libero_10\\\\\\\" if args.suite == \\\\\\\"long\\\\\\\" else f\\\\\\\"libero_{args.suite}\\\\\\\"\\\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\\\n\\\\n    log(f\\\\\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\\\\\")\\\\n    log(f\\\\\\\"Checkpoint: {ckpt_path}\\\\\\\")\\\\n    log(f\\\\\\\"Data: {data_dir}\\\\\\\")\\\\n    log(f\\\\\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\\\\\")\\\\n    if args.dry_run:\\\\n        log(\\\\\\\"DRY RUN\\\\\\\")\\\\n\\\\n    tasks, instructions = discover_tasks(data_dir)\\\\n    if args.dry_run:\\\\n        tasks = tasks[:2]\\\\n        instructions = instructions[:2]\\\\n    log(f\\\\\\\"Tasks: {len(tasks)}\\\\\\\")\\\\n\\\\n    model, processor = load_model(args.arch, ckpt_path, device)\\\\n\\\\n    t0 = time.time()\\\\n    features, actions, demo_ids = extract_features(\\\\n        args.arch, model, processor, tasks, instructions, data_dir,\\\\n        device, args.n_demos, args.n_timesteps)\\\\n    log(f\\\\\\\"Extraction: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n    del model, processor\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    n_layers = ARCH_INFO[args.arch][\\\\\\\"n_layers\\\\\\\"]\\\\n    result = clustered_bootstrap_r2(\\\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\\\n    log(f\\\\\\\"Bootstrap: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    result[\\\\\\\"arch\\\\\\\"] = args.arch\\\\n    result[\\\\\\\"suite\\\\\\\"] = args.suite\\\\n    result[\\\\\\\"condition\\\\\\\"] = args.condition\\\\n    result[\\\\\\\"n_demos\\\\\\\"] = int(len(np.unique(demo_ids)))\\\\n    result[\\\\\\\"n_total_samples\\\\\\\"] = int(len(actions))\\\\n    result[\\\\\\\"n_bootstrap\\\\\\\"] = args.n_bootstrap\\\\n    result[\\\\\\\"dry_run\\\\\\\"] = args.dry_run\\\\n\\\\n    out_dir = os.path.join(args.output_dir, f\\\\\\\"{args.arch}_{args.suite}\\\\\\\")\\\\n    os.makedirs(out_dir, exist_ok=True)\\\\n    out_path = os.path.join(out_dir, f\\\\\\\"{args.condition}.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(result, f, indent=2)\\\\n    log(f\\\\\\\"Saved: {out_path}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.57}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(arch, ckpt_path, device):\\n    log(f\\\"Loading {arch} from {ckpt_path}\\\")\\n    t0 = time.time()\\n\\n    if arch == \\\"openvla\\\":\\n        _load_openvla_modules(ckpt_path)\\n        config_cls = sys.modules[\\\"configuration_prismatic\\\"].OpenVLAConfig\\n        model_cls = sys.modules[\\\"modeling_prismatic\\\"].OpenVLAForActionPrediction\\n        proc_cls = sys.modules[\\\"processing_prismatic\\\"].PrismaticProcessor\\n\\n        config = config_cls.from_pretrained(ckpt_path)\\n        model = model_cls.from_pretrained(\\n            ckpt_path, config=config, dtype=torch.bfloat16\\n        ).to(device).eval()\\n        # Patch transformers.tokenization_utils for HF cache loading\\n        import transformers.tokenization_utils_base as _tub\\n        from transformers.utils import PaddingStrategy as _PS\\n        _tu = sys.modules[\\\"transformers.tokenization_utils\\\"]\\n        _tu.PaddingStrategy = _PS\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\n        _tu.TextInput = _tub.TextInput\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n    if arch == \\\"openvla\\\":\\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n        inputs = processor(prompt, image).to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        ids = inputs[\\\"input_ids\\\"]\\n        if not torch.all(ids[:, -1] == 29871):\\n            ids = torch.cat(\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\n            if \\\"attention_mask\\\" in inputs:\\n                inputs[\\\"attention_mask\\\"] = torch.cat(\\n                    (inputs[\\\"attention_mask\\\"],\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\"attention_mask\\\"].dtype)),\\n                    dim=1)\\n        inputs[\\\"input_ids\\\"] = ids\\n        return inputs\\n\\n    elif arch == \\\"tracvla\\\":\\n        prompt = (\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n                  f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n                  \\\"<|assistant|>\\\\n\\\")\\n        inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        return inputs\\n\\n    elif arch == \\\"nora\\\":\\n        messages = [{\\\"role\\\": \\\"user\\\", \\\"content\\\": [\\n            {\\\"type\\\": \\\"image\\\", \\\"image\\\": image},\\n            {\\\"type\\\": \\\"text\\\", \\\"text\\\": instruction},\\n        ]}]\\n        text = process\\n\\n... [截断: 输出过长，省略 5537 字符] ...\\n\\nt_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\", \\\"long\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    suite_data_name = \\\"libero_10\\\" if args.suite == \\\"long\\\" else f\\\"libero_{args.suite}\\\"\\n    data_dir = os.path.join(DATA_ROOT, suite_data_name)\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have essentially the complete file. Let me piece it together. The only bit I'm potentially missing is around lines 86-98 which is the tail end of the first loop and the beginning of the second loop in `_load_openvla_modules`. But I actually already have that from the first read (lines 1-150). Let me reconstruct the full file from all the reads.

Actually, looking at the outputs carefully, I have all the pieces now:

1. Lines 1-150 from the first `head -150` call
2. Lines 90+ from `tail -n +90` 


3. Lines 286-435 from `tail -150`

The only part that was consistently truncated is around the second loop in `_load_openvla_modules` (lines ~86-97). Let me get that specific section.

Actually wait, from the `tail -n +90` output, I can see lines starting from the import statement replacements and code compilation logic. I have enough coverage now to see the full structure of the file. I'm seeing the second loop continues with more string replacements to handle the `tie_weights` method signature, then compiles and executes the modified source code for each of those three modules.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "8ab26a41-344e-47cb-a9d2-5cf118b768a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TfyF7nxQ6uRsaCYJNVRF2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3721,
      "cache_read_input_tokens": 40461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3721
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

_source line 27_

完整源码（435行）拼合如下：

```python
#!/usr/bin/env python3
"""Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting."""

import argparse, json, os, sys, time, types
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import numpy as np
import h5py
import torch
from PIL import Image
from sklearn.linear_model import RidgeCV
import importlib.util


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


CKPT = {
    "openvla": {
        "goal":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"},
        "spatial": {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"},
        "object":  {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"},
        "long":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"},
    },
    "tracvla": {
        "goal":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base"},
        "spatial": {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base"},
        "object":  {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base"},
        "long":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base"},
    },
    "nora": {
        "goal":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base"},
        "spatial": {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base"},
    },
}

ARCH_INFO = {
    "openvla": {"n_layers": 32, "hidden": 4096},
    "tracvla": {"n_layers": 32, "hidden": 3072},
    "nora":    {"n_layers": 36, "hidden": 2048},
}

DATA_ROOT = "/root/autodl-tmp/vla-ssd/data/libero"


def _load_openvla_modules(ckpt_path):
    pkg_name = "_openvla_pkg"
    pkg = types.ModuleType(pkg_name)
    pkg.__path__ = [ckpt_path]
    pkg.__package__ = pkg_name
    sys.modules[pkg_name] = pkg

    for name in ["configuration_prismatic", "modeling_prismatic", "processing_prismatic"]:
        full = f"{pkg_name}.{name}"
        fpath = os.path.join(ckpt_path, f"{name}.py")
        with open(fpath) as f:
            src = f.read()
        src = src.replace(
            "from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy",
            "from transformers.utils import PaddingStrategy\n"
            "from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy"
        )
        mod = types.ModuleType(full)
        mod.__file__ = fpath
        mod.__package__ = pkg_name
        sys.modules[full] = mod
        sys.modules[name] = mod
        setattr(pkg, name, mod)

    for name in ["configuration_prismatic", "modeling_prismatic", "processing_prismatic"]:
        full = f"{pkg_name}.{name}"
        fpath = os.path.join(ckpt_path, f"{name}.py")
        with open(fpath) as f:
            src = f.read()
        src = src.replace(
            "from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy",
            "from transformers.utils import PaddingStrategy\n"
            "from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy"
        )
        src = src.replace(
            "def tie_weights(self) -> None:",
            "def tie_weights(self, **kwargs) -> None:"
        )
        code = compile(src, fpath, "exec")
        exec(code, sys.modules[full].__dict__)


def load_model(arch, ckpt_path, device):
    log(f"Loading {arch} from {ckpt_path}")
    t0 = time.time()

    if arch == "openvla":
        _load_openvla_modules(ckpt_path)
        config_cls = sys.modules["configuration_prismatic"].OpenVLAConfig
        model_cls = sys.modules["modeling_prismatic"].OpenVLAForActionPrediction
        proc_cls = sys.modules["processing_prismatic"].PrismaticProcessor

        config = config_cls.from_pretrained(ckpt_path)
        model = model_cls.from_pretrained(
            ckpt_path, config=config, dtype=torch.bfloat16
        ).to(device).eval()
        import transformers.tokenization_utils_base as _tub
        from transformers.utils import PaddingStrategy as _PS
        _tu = sys.modules["transformers.tokenization_utils"]
        _tu.PaddingStrategy = _PS
        _tu.PreTokenizedInput = _tub.PreTokenizedInput
        _tu.TextInput = _tub.TextInput
        _tu.TruncationStrategy = _tub.TruncationStrategy
        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)

        ds_path = os.path.join(ckpt_path, "dataset_statistics.json")
        if os.path.exists(ds_path):
            with open(ds_path) as f:
                ds_stats = json.load(f)
            for k, v in ds_stats.items():
                if k not in model.norm_stats:
                    model.norm_stats[k] = v

    elif arch == "tracvla":
        from transformers import AutoModelForCausalLM, AutoProcessor
        model = AutoModelForCausalLM.from_pretrained(
            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True
        ).to(device).eval()
        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)

    elif arch == "nora":
        from transformers import AutoModelForImageTextToText, AutoProcessor
        model = AutoModelForImageTextToText.from_pretrained(
            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True
        ).to(device).eval()
        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)

    log(f"  Loaded in {time.time()-t0:.1f}s")
    return model, processor


def prepare_inputs(arch, processor, instruction, image, device):
    if arch == "openvla":
        prompt = f"In: What action should the robot take to {instruction}?\nOut:"
        inputs = processor(prompt, image).to(device)
        if "pixel_values" in inputs:
            inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        ids = inputs["input_ids"]
        if not torch.all(ids[:, -1] == 29871):
            ids = torch.cat(
                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)
            if "attention_mask" in inputs:
                inputs["attention_mask"] = torch.cat(
                    (inputs["attention_mask"],
                     torch.ones(1, 1, device=device, dtype=inputs["attention_mask"].dtype)),
                    dim=1)
        inputs["input_ids"] = ids
        return inputs

    elif arch == "tracvla":
        prompt = ("<|user|>\n<|image_1|>\n"
                  f"What action should the robot take to {instruction}?<|end|>\n"
                  "<|assistant|>\n")
        inputs = processor(prompt, [image], return_tensors="pt").to(device)
        if "pixel_values" in inputs:
            inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        return inputs

    elif arch == "nora":
        messages = [{"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": instruction},
        ]}]
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(text=[text], images=[image], return_tensors="pt", padding=True)
        return {k: v.to(device) if isinstance(v, torch.Tensor) else v
                for k, v in inputs.items()}


def discover_tasks(data_dir):
    tasks = []
    for f in sorted(os.listdir(data_dir)):
        if f.endswith("_demo.hdf5"):
            tasks.append(f.replace("_demo.hdf5", ""))
    instructions = [t.replace("_", " ") for t in tasks]
    return tasks, instructions


def extract_features(arch, model, processor, tasks, instructions, data_dir,
                     device, n_demos, n_timesteps):
    info = ARCH_INFO[arch]
    n_layers = info["n_layers"]
    hidden = info["hidden"]
    total = len(tasks) * n_demos * n_timesteps

    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}
    actions = np.zeros((total, 7), dtype=np.float32)
    demo_ids = np.zeros(total, dtype=np.int64)

    idx = 0
    gd = 0

    for ti, (task, instr) in enumerate(zip(tasks, instructions)):
        hdf5_path = os.path.join(data_dir, f"{task}_demo.hdf5")
        log(f"  Task {ti}/{len(tasks)}: {task}")

        with h5py.File(hdf5_path, "r") as hf:
            for di in range(n_demos):
                demo_key = f"data/demo_{di}"
                if demo_key not in hf:
                    gd += 1
                    continue
                n_avail = hf[demo_key]["actions"].shape[0]

                for t in range(min(n_timesteps, n_avail)):
                    img = Image.fromarray(hf[f"{demo_key}/obs/agentview_rgb"][t])
                    act = np.array(hf[f"{demo_key}/actions"][t], dtype=np.float32)

                    inputs = prepare_inputs(arch, processor, instr, img, device)
                    with torch.no_grad():
                        out = model(**inputs, output_hidden_states=True)

                    for l in range(n_layers):
                        hs = out.hidden_states[l + 1][0]
                        features[l][idx] = hs[-1].float().cpu().numpy()

                    actions[idx] = act
                    demo_ids[idx] = gd
                    idx += 1

                    del out, inputs
                    if idx % 50 == 0:
                        torch.cuda.empty_cache()
                        log(f"    {idx}/{total} samples")

                gd += 1

    log(f"  Extraction done: {idx} samples, {gd} demos")
    features = {l: features[l][:idx] for l in range(n_layers)}
    return features, actions[:idx], demo_ids[:idx]


def clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):
    unique_demos = np.unique(demo_ids)
    n_total = len(unique_demos)
    n_train = int(0.8 * n_total)
    log(f"  {n_total} demos, split {n_train}/{n_total - n_train}")

    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}

    rng = np.random.RandomState(seed)
    canon_perm = rng.permutation(unique_demos)
    canon_train = set(canon_perm[:n_train].tolist())
    train_mask = np.array([d in canon_train for d in demo_ids])
    test_mask = ~train_mask

    y_tr_canon = actions[train_mask]
    y_te_canon = actions[test_mask]

    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]
    best_alpha = {}
    canon_r2 = {}

    log("  Canonical split -- fitting RidgeCV per layer...")
    for l in range(n_layers):
        probe = RidgeCV(alphas=alphas_list)
        probe.fit(features[l][train_mask], y_tr_canon)
        best_alpha[l] = float(probe.alpha_)
        pred = probe.predict(features[l][test_mask])
        ss_res = np.sum((y_te_canon - pred) ** 2)
        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)
        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0

    log("  Precomputing kernel matrices...")
    N = len(actions)
    kernels = {}
    for l in range(n_layers):
        kernels[l] = features[l] @ features[l].T  # (N, N)

    log(f"  Bootstrap ({n_bootstrap} iterations)...")
    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)
    rng2 = np.random.RandomState(seed + 1)
    report_every = max(1, n_bootstrap // 10)

    for b in range(n_bootstrap):
        resampled = rng2.choice(unique_demos, size=n_total, replace=True)
        tr_demos = resampled[:n_train]
        te_demos = resampled[n_train:]

        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])
        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])

        if len(te_idx) == 0:
            continue

        y_tr = actions[tr_idx]
        y_te = actions[te_idx]
        y_te_mean = y_te.mean(axis=0)
        ss_tot = np.sum((y_te - y_te_mean) ** 2)
        if ss_tot < 1e-10:
            continue

        n_tr = len(tr_idx)
        for l in range(n_layers):
            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]
            K_tr[np.diag_indices(n_tr)] += best_alpha[l]
            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]
            try:
                w = np.linalg.solve(K_tr, y_tr)
                pred = K_te_tr @ w
                ss_res = np.sum((y_te - pred) ** 2)
                boot_r2[b, l] = 1.0 - ss_res / ss_tot
            except np.linalg.LinAlgError:
                boot_r2[b, l] = 0.0

        if (b + 1) % report_every == 0:
            log(f"    {b+1}/{n_bootstrap}")

    exit_l = n_layers - 1
    peak_r2_boot = np.max(boot_r2, axis=1)
    exit_r2_boot = boot_r2[:, exit_l]
    deltas = peak_r2_boot - exit_r2_boot
    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])

    canon_peak_l = max(canon_r2, key=canon_r2.get)

    return {
        "per_layer_r2": {f"L{l}": round(canon_r2[l], 4) for l in range(n_layers)},
        "peak_r2": round(canon_r2[canon_peak_l], 4),
        "peak_layer": f"L{canon_peak_l}",
        "exit_r2": round(canon_r2[exit_l], 4),
        "exit_layer": f"L{exit_l}",
        "delta": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),
        "delta_ci_95": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
        "bootstrap_deltas_summary": {
            "mean": round(float(np.mean(deltas)), 4),
            "std": round(float(np.std(deltas)), 4),
            "median": round(float(np.median(deltas)), 4),
        },
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--arch", required=True, choices=["openvla", "tracvla", "nora"])
    p.add_argument("--suite", required=True, choices=["goal", "spatial", "object", "long"])
    p.add_argument("--condition", required=True, choices=["trained", "untrained"])
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--n_bootstrap", type=int, default=10000)
    p.add_argument("--n_demos", type=int, default=10)
    p.add_argument("--n_timesteps", type=int, default=50)
    p.add_argument("--output_dir",
                   default="/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/")
    p.add_argument("--dry_run", action="store_true")
    args = p.parse_args()

    if args.dry_run:
        args.n_demos = 2
        args.n_timesteps = 5
        args.n_bootstrap = min(args.n_bootstrap, 100)

    if args.suite not in CKPT.get(args.arch, {}):
        log(f"ERROR: no checkpoint for {args.arch}/{args.suite}")
        sys.exit(1)
    if args.condition not in CKPT[args.arch][args.suite]:
        log(f"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}")
        sys.exit(1)

    device = f"cuda:{args.gpu}"
    ckpt_path = CKPT[args.arch][args.suite][args.condition]
    suite_data_name = "libero_10" if args.suite == "long" else f"libero_{args.suite}"
    data_dir = os.path.join(DATA_ROOT, suite_data_name)

    log(f"=== {args.arch} / {args.suite} / {args.condition} ===")
    log(f"Checkpoint: {ckpt_path}")
    log(f"Data: {data_dir}")
    log(f"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}")
    if args.dry_run:
        log("DRY RUN")

    tasks, instructions = discover_tasks(data_dir)
    if args.dry_run:
        tasks = tasks[:2]
        instructions = instructions[:2]
    log(f"Tasks: {len(tasks)}")

    model, processor = load_model(args.arch, ckpt_path, device)

    t0 = time.time()
    features, actions, demo_ids = extract_features(
        args.arch, model, processor, tasks, instructions, data_dir,
        device, args.n_demos, args.n_timesteps)
    log(f"Extraction: {time.time()-t0:.1f}s")

    del model, processor
    torch.cuda.empty_cache()

    t1 = time.time()
    n_layers = ARCH_INFO[args.arch]["n_layers"]
    result = clustered_bootstrap_r2(
        features, actions, demo_ids, n_layers, args.n_bootstrap)
    log(f"Bootstrap: {time.time()-t1:.1f}s")

    result["arch"] = args.arch
    result["suite"] = args.suite
    result["condition"] = args.condition
    result["n_demos"] = int(len(np.unique(demo_ids)))
    result["n_total_samples"] = int(len(actions))
    result["n_bootstrap"] = args.n_bootstrap
    result["dry_run"] = args.dry_run

    out_dir = os.path.join(args.output_dir, f"{args.arch}_{args.suite}")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{args.condition}.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    log(f"Saved: {out_path}")

    log(f"Peak R2={result['peak_r2']} @ {result['peak_layer']}")
    log(f"Exit R2={result['exit_r2']} @ {result['exit_layer']}")
    log(f"Delta={result['delta']}  CI95={result['delta_ci_95']}")


if __name__ == "__main__":
    main()
```

以上是完整的 435 行源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "uuid": "6327ddca-cdce-4dce-8dc0-e9be45679f11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TfyF7nxQ6uRsaCYJNVRF2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3721,
      "cache_read_input_tokens": 40461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3721
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

_source line 28_

完整源码（435行）拼合如下：

```python
#!/usr/bin/env python3
"""Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting."""

import argparse, json, os, sys, time, types
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import numpy as np
import h5py
import torch
from PIL import Image
from sklearn.linear_model import RidgeCV
import importlib.util


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


CKPT = {
    "openvla": {
        "goal":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"},
        "spatial": {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"},
        "object":  {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"},
        "long":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"},
    },
    "tracvla": {
        "goal":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base"},
        "spatial": {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base"},
        "object":  {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base"},
        "long":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base"},
    },
    "nora": {
        "goal":    {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base"},
        "spatial": {"trained": "/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial",
                    "untrained": "/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base"},
    },
}

ARCH_INFO = {
    "openvla": {"n_layers": 32, "hidden": 4096},
    "tracvla": {"n_layers": 32, "hidden": 3072},
    "nora":    {"n_layers": 36, "hidden": 2048},
}

DATA_ROOT = "/root/autodl-tmp/vla-ssd/data/libero"


def _load_openvla_modules(ckpt_path):
    pkg_name = "_openvla_pkg"
    pkg = types.ModuleType(pkg_name)
    pkg.__path__ = [ckpt_path]
    pkg.__package__ = pkg_name
    sys.modules[pkg_name] = pkg

    for name in ["configuration_prismatic", "modeling_prismatic", "processing_prismatic"]:
        full = f"{pkg_name}.{name}"
        fpath = os.path.join(ckpt_path, f"{name}.py")
        with open(fpath) as f:
            src = f.read()
        src = src.replace(
            "from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy",
            "from transformers.utils import PaddingStrategy\n"
            "from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy"
        )
        mod = types.ModuleType(full)
        mod.__file__ = fpath
        mod.__package__ = pkg_name
        sys.modules[full] = mod
        sys.modules[name] = mod
        setattr(pkg, name, mod)

    for name in ["configuration_prismatic", "modeling_prismatic", "processing_prismatic"]:
        full = f"{pkg_name}.{name}"
        fpath = os.path.join(ckpt_path, f"{name}.py")
        with open(fpath) as f:
            src = f.read()
        src = src.replace(
            "from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy",
            "from transformers.utils import PaddingStrategy\n"
            "from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy"
        )
        src = src.replace(
            "def tie_weights(self) -> None:",
            "def tie_weights(self, **kwargs) -> None:"
        )
        code = compile(src, fpath, "exec")
        exec(code, sys.modules[full].__dict__)


def load_model(arch, ckpt_path, device):
    log(f"Loading {arch} from {ckpt_path}")
    t0 = time.time()

    if arch == "openvla":
        _load_openvla_modules(ckpt_path)
        config_cls = sys.modules["configuration_prismatic"].OpenVLAConfig
        model_cls = sys.modules["modeling_prismatic"].OpenVLAForActionPrediction
        proc_cls = sys.modules["processing_prismatic"].PrismaticProcessor

        config = config_cls.from_pretrained(ckpt_path)
        model = model_cls.from_pretrained(
            ckpt_path, config=config, dtype=torch.bfloat16
        ).to(device).eval()
        import transformers.tokenization_utils_base as _tub
        from transformers.utils import PaddingStrategy as _PS
        _tu = sys.modules["transformers.tokenization_utils"]
        _tu.PaddingStrategy = _PS
        _tu.PreTokenizedInput = _tub.PreTokenizedInput
        _tu.TextInput = _tub.TextInput
        _tu.TruncationStrategy = _tub.TruncationStrategy
        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)

        ds_path = os.path.join(ckpt_path, "dataset_statistics.json")
        if os.path.exists(ds_path):
            with open(ds_path) as f:
                ds_stats = json.load(f)
            for k, v in ds_stats.items():
                if k not in model.norm_stats:
                    model.norm_stats[k] = v

    elif arch == "tracvla":
        from transformers import AutoModelForCausalLM, AutoProcessor
        model = AutoModelForCausalLM.from_pretrained(
            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True
        ).to(device).eval()
        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)

    elif arch == "nora":
        from transformers import AutoModelForImageTextToText, AutoProcessor
        model = AutoModelForImageTextToText.from_pretrained(
            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True
        ).to(device).eval()
        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)

    log(f"  Loaded in {time.time()-t0:.1f}s")
    return model, processor


def prepare_inputs(arch, processor, instruction, image, device):
    if arch == "openvla":
        prompt = f"In: What action should the robot take to {instruction}?\nOut:"
        inputs = processor(prompt, image).to(device)
        if "pixel_values" in inputs:
            inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        ids = inputs["input_ids"]
        if not torch.all(ids[:, -1] == 29871):
            ids = torch.cat(
                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)
            if "attention_mask" in inputs:
                inputs["attention_mask"] = torch.cat(
                    (inputs["attention_mask"],
                     torch.ones(1, 1, device=device, dtype=inputs["attention_mask"].dtype)),
                    dim=1)
        inputs["input_ids"] = ids
        return inputs

    elif arch == "tracvla":
        prompt = ("<|user|>\n<|image_1|>\n"
                  f"What action should the robot take to {instruction}?<|end|>\n"
                  "<|assistant|>\n")
        inputs = processor(prompt, [image], return_tensors="pt").to(device)
        if "pixel_values" in inputs:
            inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        return inputs

    elif arch == "nora":
        messages = [{"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": instruction},
        ]}]
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(text=[text], images=[image], return_tensors="pt", padding=True)
        return {k: v.to(device) if isinstance(v, torch.Tensor) else v
                for k, v in inputs.items()}


def discover_tasks(data_dir):
    tasks = []
    for f in sorted(os.listdir(data_dir)):
        if f.endswith("_demo.hdf5"):
            tasks.append(f.replace("_demo.hdf5", ""))
    instructions = [t.replace("_", " ") for t in tasks]
    return tasks, instructions


def extract_features(arch, model, processor, tasks, instructions, data_dir,
                     device, n_demos, n_timesteps):
    info = ARCH_INFO[arch]
    n_layers = info["n_layers"]
    hidden = info["hidden"]
    total = len(tasks) * n_demos * n_timesteps

    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}
    actions = np.zeros((total, 7), dtype=np.float32)
    demo_ids = np.zeros(total, dtype=np.int64)

    idx = 0
    gd = 0

    for ti, (task, instr) in enumerate(zip(tasks, instructions)):
        hdf5_path = os.path.join(data_dir, f"{task}_demo.hdf5")
        log(f"  Task {ti}/{len(tasks)}: {task}")

        with h5py.File(hdf5_path, "r") as hf:
            for di in range(n_demos):
                demo_key = f"data/demo_{di}"
                if demo_key not in hf:
                    gd += 1
                    continue
                n_avail = hf[demo_key]["actions"].shape[0]

                for t in range(min(n_timesteps, n_avail)):
                    img = Image.fromarray(hf[f"{demo_key}/obs/agentview_rgb"][t])
                    act = np.array(hf[f"{demo_key}/actions"][t], dtype=np.float32)

                    inputs = prepare_inputs(arch, processor, instr, img, device)
                    with torch.no_grad():
                        out = model(**inputs, output_hidden_states=True)

                    for l in range(n_layers):
                        hs = out.hidden_states[l + 1][0]
                        features[l][idx] = hs[-1].float().cpu().numpy()

                    actions[idx] = act
                    demo_ids[idx] = gd
                    idx += 1

                    del out, inputs
                    if idx % 50 == 0:
                        torch.cuda.empty_cache()
                        log(f"    {idx}/{total} samples")

                gd += 1

    log(f"  Extraction done: {idx} samples, {gd} demos")
    features = {l: features[l][:idx] for l in range(n_layers)}
    return features, actions[:idx], demo_ids[:idx]


def clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):
    unique_demos = np.unique(demo_ids)
    n_total = len(unique_demos)
    n_train = int(0.8 * n_total)
    log(f"  {n_total} demos, split {n_train}/{n_total - n_train}")

    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}

    rng = np.random.RandomState(seed)
    canon_perm = rng.permutation(unique_demos)
    canon_train = set(canon_perm[:n_train].tolist())
    train_mask = np.array([d in canon_train for d in demo_ids])
    test_mask = ~train_mask

    y_tr_canon = actions[train_mask]
    y_te_canon = actions[test_mask]

    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]
    best_alpha = {}
    canon_r2 = {}

    log("  Canonical split -- fitting RidgeCV per layer...")
    for l in range(n_layers):
        probe = RidgeCV(alphas=alphas_list)
        probe.fit(features[l][train_mask], y_tr_canon)
        best_alpha[l] = float(probe.alpha_)
        pred = probe.predict(features[l][test_mask])
        ss_res = np.sum((y_te_canon - pred) ** 2)
        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)
        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0

    log("  Precomputing kernel matrices...")
    N = len(actions)
    kernels = {}
    for l in range(n_layers):
        kernels[l] = features[l] @ features[l].T  # (N, N)

    log(f"  Bootstrap ({n_bootstrap} iterations)...")
    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)
    rng2 = np.random.RandomState(seed + 1)
    report_every = max(1, n_bootstrap // 10)

    for b in range(n_bootstrap):
        resampled = rng2.choice(unique_demos, size=n_total, replace=True)
        tr_demos = resampled[:n_train]
        te_demos = resampled[n_train:]

        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])
        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])

        if len(te_idx) == 0:
            continue

        y_tr = actions[tr_idx]
        y_te = actions[te_idx]
        y_te_mean = y_te.mean(axis=0)
        ss_tot = np.sum((y_te - y_te_mean) ** 2)
        if ss_tot < 1e-10:
            continue

        n_tr = len(tr_idx)
        for l in range(n_layers):
            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]
            K_tr[np.diag_indices(n_tr)] += best_alpha[l]
            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]
            try:
                w = np.linalg.solve(K_tr, y_tr)
                pred = K_te_tr @ w
                ss_res = np.sum((y_te - pred) ** 2)
                boot_r2[b, l] = 1.0 - ss_res / ss_tot
            except np.linalg.LinAlgError:
                boot_r2[b, l] = 0.0

        if (b + 1) % report_every == 0:
            log(f"    {b+1}/{n_bootstrap}")

    exit_l = n_layers - 1
    peak_r2_boot = np.max(boot_r2, axis=1)
    exit_r2_boot = boot_r2[:, exit_l]
    deltas = peak_r2_boot - exit_r2_boot
    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])

    canon_peak_l = max(canon_r2, key=canon_r2.get)

    return {
        "per_layer_r2": {f"L{l}": round(canon_r2[l], 4) for l in range(n_layers)},
        "peak_r2": round(canon_r2[canon_peak_l], 4),
        "peak_layer": f"L{canon_peak_l}",
        "exit_r2": round(canon_r2[exit_l], 4),
        "exit_layer": f"L{exit_l}",
        "delta": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),
        "delta_ci_95": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
        "bootstrap_deltas_summary": {
            "mean": round(float(np.mean(deltas)), 4),
            "std": round(float(np.std(deltas)), 4),
            "median": round(float(np.median(deltas)), 4),
        },
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--arch", required=True, choices=["openvla", "tracvla", "nora"])
    p.add_argument("--suite", required=True, choices=["goal", "spatial", "object", "long"])
    p.add_argument("--condition", required=True, choices=["trained", "untrained"])
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--n_bootstrap", type=int, default=10000)
    p.add_argument("--n_demos", type=int, default=10)
    p.add_argument("--n_timesteps", type=int, default=50)
    p.add_argument("--output_dir",
                   default="/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/")
    p.add_argument("--dry_run", action="store_true")
    args = p.parse_args()

    if args.dry_run:
        args.n_demos = 2
        args.n_timesteps = 5
        args.n_bootstrap = min(args.n_bootstrap, 100)

    if args.suite not in CKPT.get(args.arch, {}):
        log(f"ERROR: no checkpoint for {args.arch}/{args.suite}")
        sys.exit(1)
    if args.condition not in CKPT[args.arch][args.suite]:
        log(f"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}")
        sys.exit(1)

    device = f"cuda:{args.gpu}"
    ckpt_path = CKPT[args.arch][args.suite][args.condition]
    suite_data_name = "libero_10" if args.suite == "long" else f"libero_{args.suite}"
    data_dir = os.path.join(DATA_ROOT, suite_data_name)

    log(f"=== {args.arch} / {args.suite} / {args.condition} ===")
    log(f"Checkpoint: {ckpt_path}")
    log(f"Data: {data_dir}")
    log(f"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}")
    if args.dry_run:
        log("DRY RUN")

    tasks, instructions = discover_tasks(data_dir)
    if args.dry_run:
        tasks = tasks[:2]
        instructions = instructions[:2]
    log(f"Tasks: {len(tasks)}")

    model, processor = load_model(args.arch, ckpt_path, device)

    t0 = time.time()
    features, actions, demo_ids = extract_features(
        args.arch, model, processor, tasks, instructions, data_dir,
        device, args.n_demos, args.n_timesteps)
    log(f"Extraction: {time.time()-t0:.1f}s")

    del model, processor
    torch.cuda.empty_cache()

    t1 = time.time()
    n_layers = ARCH_INFO[args.arch]["n_layers"]
    result = clustered_bootstrap_r2(
        features, actions, demo_ids, n_layers, args.n_bootstrap)
    log(f"Bootstrap: {time.time()-t1:.1f}s")

    result["arch"] = args.arch
    result["suite"] = args.suite
    result["condition"] = args.condition
    result["n_demos"] = int(len(np.unique(demo_ids)))
    result["n_total_samples"] = int(len(actions))
    result["n_bootstrap"] = args.n_bootstrap
    result["dry_run"] = args.dry_run

    out_dir = os.path.join(args.output_dir, f"{args.arch}_{args.suite}")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{args.condition}.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    log(f"Saved: {out_path}")

    log(f"Peak R2={result['peak_r2']} @ {result['peak_layer']}")
    log(f"Exit R2={result['exit_r2']} @ {result['exit_layer']}")
    log(f"Delta={result['delta']}  CI95={result['delta_ci_95']}")


if __name__ == "__main__":
    main()
```

以上是完整的 435 行源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 165131,
  "duration_api_ms": 162342,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "d9a5e09f-be0a-4b62-acbf-f121e80e4a3f",
  "total_cost_usd": 0.5308297500000001,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 32341,
    "cache_read_input_tokens": 254631,
    "output_tokens": 8017,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32341,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 6949,
        "cache_read_input_tokens": 40461,
        "cache_creation_input_tokens": 3721,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3721
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 818,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.000893,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 8017,
      "cacheReadInputTokens": 254631,
      "cacheCreationInputTokens": 32341,
      "webSearchRequests": 0,
      "costUSD": 0.5299367500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9f8d8b7a-8692-4ef3-8437-9059588f2250"
}
```

</details>

---
