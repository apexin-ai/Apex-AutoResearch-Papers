# code fix action divergence

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_code_fix_action_divergence_20260517T103707.log`
- **Structured JSON:** [`8c2443b1151866af2c86.json`](../../sessions/8c/8c2443b1151866af2c86.json)

## Before a recorded user message

74 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
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
  "uuid": "0bb9d182-bae8-420c-93f2-607f65c061cc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779030600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6e2ad39a-af56-442d-9694-26f4cf9c5ef8",
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a"
}
```

---

### Assistant

_source line 4_

Let me first check the existing script and available checkpoints on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "28561b71-2023-4b55-8f56-28e246dd99c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AWEPaVqoZYLHMJMADadAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12793,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12793
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A9zQcs2LoU5togWzGCg3mD`</summary>

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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "737b384d-b248-47a8-bf09-6f96b3fd7c31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AWEPaVqoZYLHMJMADadAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12793,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12793
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-17T10:37:20.414Z_

<details><summary>↩ Tool result · `toolu_01A9zQcs2LoU5togWzGCg3mD`</summary>

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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "0c87925a-31d9-473a-9cae-7eff46c1646a",
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
Let me check the existing script, available checkpoints, and the eval script for reference on how to register ACIS hooks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "4d5e657f-3361-40e2-983b-d46dc9d3c378",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Wk76RFUrMXsSr6smghqRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 687
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BA1DtA74ZhdUmhykND15R5`</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "27dbe34e-1cde-456f-ae03-447d837bbf63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Wk76RFUrMXsSr6smghqRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 687
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F4s4zkVJUz5jyDn4niPhnC`</summary>

```json
{
  "server": "westd-27271",
  "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only*/stage1_done/",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "fbc0d542-b321-4be9-9880-095d85f2d79b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Wk76RFUrMXsSr6smghqRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 687
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01N4DWFHwBoRiroqMpBvRRkK`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"register_acis_hook\\|def register\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "fe5a3912-67de-49c6-9623-0c45e8568814",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Wk76RFUrMXsSr6smghqRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 24634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 687
      },
      "output_tokens": 23,
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

_source line 11 · 2026-05-17T10:37:26.847Z_

<details><summary>↩ Tool result · `toolu_01BA1DtA74ZhdUmhykND15R5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Per-step Action Divergence Analysis: Baseline vs ACIS-pruned model.\\n\\nDrives the environment with baseline actions while recording both models'\\naction outputs at each timestep (same observation). Produces divergence curves\\nand per-dimension breakdown.\\n\\nUsage:\\n    python analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n# Paths\\nBASELINE_CKPT = \\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\"\\nACIS_CKPT = \\\"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\\\"\\nBASELINE_CONFIG = \\\"configs/libero_baseline.yaml\\\"\\nACIS_CONFIG = \\\"configs/libero_acis_stage1only_k07.yaml\\\"\\n\\nSUITE = \\\"libero_object\\\"\\nMAX_STEPS = 280\\nACTION_HORIZON = 50\\nACTION_DIM_NAMES = [\\\"pos_x\\\", \\\"pos_y\\\", \\\"pos_z\\\", \\\"rot_x\\\", \\\"rot_y\\\", \\\"rot_z\\\", \\\"gripper\\\"]\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--gpu\\\", type=int, default=2)\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=5)\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=\\\"0,1,2\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--output_dir\\\", type=str, default=\\\"artifacts\\\")\\n    return p.parse_args()\\n\\n\\ndef load_config(config_path: str) -> dict:\\n    import copy\\n    import yaml\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        for k, v in config.items():\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\n                base_config[k].update(v)\\n            else:\\n                base_config[k] = v\\n        return base_config\\n    return config\\n\\n\\ndef load_baseline_model(device):\\n    from train import load_smolvla_policy\\n    config = load_config(BASELINE_CONFIG)\\n    policy = load_smolvla_policy(config, device)\\n    ckpt = torch.load(BASELINE_CKPT, map_location=device, weights_only=False)\\n    policy.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    policy.eval()\\n    return policy, config\\n\\n\\ndef load_acis_model(device):\\n    from train import load_smolvla_policy, wrap_with_imm\\n    config = load_config(ACIS_CONFIG)\\n    policy = load_smolvla_policy(config, device)\\n    wrapper = wrap_with_imm(policy, config)\\n    wrapper.to(device)\\n    ckpt = torch.load(ACIS_CKPT, map_location=device, weights_only=False)\\n    wrapper.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    wrapper.eval()\\n    return wrapper.policy, wrapper, config\\n\\n\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\n\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\n    q = quat.astype(np.float64)\\n    w = np.clip(q[3], -1.0, 1.0)\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\n    if den > 1e-10:\\n        angle = 2.0 * np.arccos(w)\\n        axis = q[:3] / den\\n        return (axis * angle).astype(np.float32)\\n    return np.zeros(3, dtype=np.float32)\\n\\n\\ndef extract_state(obs: dict) -> np.ndarray:\\n    rs = obs[\\\"robot_state\\\"]\\n    eef_pos = np.asarray(rs[\\\"eef\\\"][\\\"pos\\\"], dtype=np.float32)\\n    eef_quat = np.asarray(rs[\\\"eef\\\"][\\\"quat\\\"], dtype=np.float64)\\n    gripper_qpos = np.asarray(rs[\\\"gripper\\\"][\\\"qpos\\\"], dtype=np.float32)\\n    eef_aa = quat_to_axis_angle(eef_quat)\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\n\\n\\ndef obs_to_\\n\\n... [截断: 输出过长，省略 9638 字符] ...\\n\\n: Path):\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\n\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\n    ax = axes[0]\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\n    task_ids = sorted(all_results.keys())\\n\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        for ep_data in episodes:\\n            steps = ep_data[\\\"timesteps\\\"]\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in steps]\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\n\\n    mean_curve = analysis[\\\"mean_l2_curve\\\"]\\n    std_curve = analysis[\\\"std_l2_curve\\\"]\\n    x = np.arange(len(mean_curve))\\n    ax.plot(x, mean_curve, color=\\\"black\\\", linewidth=2, label=\\\"Mean\\\")\\n    mean_arr = np.array(mean_curve)\\n    std_arr = np.array(std_curve)\\n    valid = ~np.isnan(mean_arr)\\n    ax.fill_between(\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\n        alpha=0.15, color=\\\"black\\\"\\n    )\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Baseline vs ACIS k=0.7: Action Divergence\\\")\\n    ax.legend(loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    # Plot 2: Per-dimension breakdown\\n    ax = axes[1]\\n    dim_data = analysis[\\\"per_dim_mean_abs_diff\\\"]\\n    names = list(dim_data.keys())\\n    values = list(dim_data.values())\\n    bar_colors = [\\\"#2196F3\\\"] * 3 + [\\\"#FF9800\\\"] * 3 + [\\\"#4CAF50\\\"]\\n    ax.bar(names, values, color=bar_colors)\\n    ax.set_xlabel(\\\"Action Dimension\\\")\\n    ax.set_ylabel(\\\"Mean |Difference|\\\")\\n    ax.set_title(\\\"Per-Dimension Divergence\\\")\\n    ax.set_xticklabels(names, rotation=45, ha=\\\"right\\\")\\n    ax.grid(True, alpha=0.3, axis=\\\"y\\\")\\n\\n    # Plot 3: Per-task mean curves\\n    ax = axes[2]\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        task_l2s = []\\n        for ep_data in episodes:\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in ep_data[\\\"timesteps\\\"]]\\n            task_l2s.append(l2_vals)\\n        max_t = max(len(c) for c in task_l2s)\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\n        for i, c in enumerate(task_l2s):\\n            padded[i, :len(c)] = c\\n        task_mean = np.nanmean(padded, axis=0)\\n        task_desc = episodes[0][\\\"task_desc\\\"]\\n        short_desc = task_desc[:30] + \\\"...\\\" if len(task_desc) > 30 else task_desc\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\"T{task_id}: {short_desc}\\\", color=colors[ti % 10])\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Per-Task Mean Divergence\\\")\\n    ax.legend(fontsize=7, loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    plt.tight_layout()\\n    pdf_path = output_dir / \\\"action_divergence_curve.pdf\\\"\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.savefig(output_dir / \\\"action_divergence_curve.png\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    log.info(\\\"Plots saved to %s\\\", pdf_path)\\n\\n    # Summary stats figure\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\n    ax2.axis(\\\"off\\\")\\n    summary_text = (\\n        f\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\n\\\"\\n        f\\\"{'='*50}\\\\n\\\"\\n        f\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\n\\\"\\n        f\\\"Num episodes:           {analysis['num_episodes']}\\\\n\\\"\\n        f\\\"Max episode length:     {analysis['max_episode_length']}\\\\n\\\"\\n        f\\\"\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\n\\\"\\n        f\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\n\\\"\\n    )\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\n             verticalalignment=\\\"top\\\", fontfamily=\\\"monospace\\\")\\n    plt.tight_layout()\\n    plt.savefig(output_dir / \\\"action_divergence_summary.pdf\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_divergence_analysis(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.26}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "a7f81e8a-370e-468f-8b65-63b7d1fae5dd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Per-step Action Divergence Analysis: Baseline vs ACIS-pruned model.\\\\n\\\\nDrives the environment with baseline actions while recording both models'\\\\naction outputs at each timestep (same observation). Produces divergence curves\\\\nand per-dimension breakdown.\\\\n\\\\nUsage:\\\\n    python analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nimport time as time_mod\\\\nfrom pathlib import Path\\\\n\\\\nos.environ.setdefault(\\\\\\\"MUJOCO_GL\\\\\\\", \\\\\\\"egl\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"TRANSFORMERS_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"HF_HUB_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\n\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport numpy as np\\\\nimport torch\\\\n\\\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\\\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\n# Paths\\\\nBASELINE_CKPT = \\\\\\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\\\\\"\\\\nACIS_CKPT = \\\\\\\"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\\\\\\\"\\\\nBASELINE_CONFIG = \\\\\\\"configs/libero_baseline.yaml\\\\\\\"\\\\nACIS_CONFIG = \\\\\\\"configs/libero_acis_stage1only_k07.yaml\\\\\\\"\\\\n\\\\nSUITE = \\\\\\\"libero_object\\\\\\\"\\\\nMAX_STEPS = 280\\\\nACTION_HORIZON = 50\\\\nACTION_DIM_NAMES = [\\\\\\\"pos_x\\\\\\\", \\\\\\\"pos_y\\\\\\\", \\\\\\\"pos_z\\\\\\\", \\\\\\\"rot_x\\\\\\\", \\\\\\\"rot_y\\\\\\\", \\\\\\\"rot_z\\\\\\\", \\\\\\\"gripper\\\\\\\"]\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=2)\\\\n    p.add_argument(\\\\\\\"--num_episodes\\\\\\\", type=int, default=5)\\\\n    p.add_argument(\\\\\\\"--task_ids\\\\\\\", type=str, default=\\\\\\\"0,1,2\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\", type=str, default=\\\\\\\"artifacts\\\\\\\")\\\\n    return p.parse_args()\\\\n\\\\n\\\\ndef load_config(config_path: str) -> dict:\\\\n    import copy\\\\n    import yaml\\\\n    config_path = Path(config_path)\\\\n    with open(config_path) as f:\\\\n        config = yaml.safe_load(f)\\\\n    if \\\\\\\"_base_\\\\\\\" in config:\\\\n        base_path = config_path.parent / config.pop(\\\\\\\"_base_\\\\\\\")\\\\n        base_config = load_config(str(base_path))\\\\n        for k, v in config.items():\\\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\\\n                base_config[k].update(v)\\\\n            else:\\\\n                base_config[k] = v\\\\n        return base_config\\\\n    return config\\\\n\\\\n\\\\ndef load_baseline_model(device):\\\\n    from train import load_smolvla_policy\\\\n    config = load_config(BASELINE_CONFIG)\\\\n    policy = load_smolvla_policy(config, device)\\\\n    ckpt = torch.load(BASELINE_CKPT, map_location=device, weights_only=False)\\\\n    policy.load_state_dict(ckpt[\\\\\\\"model_state_dict\\\\\\\"], strict=False)\\\\n    policy.eval()\\\\n    return policy, config\\\\n\\\\n\\\\ndef load_acis_model(device):\\\\n    from train import load_smolvla_policy, wrap_with_imm\\\\n    config = load_config(ACIS_CONFIG)\\\\n    policy = load_smolvla_policy(config, device)\\\\n    wrapper = wrap_with_imm(policy, config)\\\\n    wrapper.to(device)\\\\n    ckpt = torch.load(ACIS_CKPT, map_location=device, weights_only=False)\\\\n    wrapper.load_state_dict(ckpt[\\\\\\\"model_state_dict\\\\\\\"], strict=False)\\\\n    wrapper.eval()\\\\n    return wrapper.policy, wrapper, config\\\\n\\\\n\\\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\\\n\\\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\\\n    q = quat.astype(np.float64)\\\\n    w = np.clip(q[3], -1.0, 1.0)\\\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\\\n    if den > 1e-10:\\\\n        angle = 2.0 * np.arccos(w)\\\\n        axis = q[:3] / den\\\\n        return (axis * angle).astype(np.float32)\\\\n    return np.zeros(3, dtype=np.float32)\\\\n\\\\n\\\\ndef extract_state(obs: dict) -> np.ndarray:\\\\n    rs = obs[\\\\\\\"robot_state\\\\\\\"]\\\\n    eef_pos = np.asarray(rs[\\\\\\\"eef\\\\\\\"][\\\\\\\"pos\\\\\\\"], dtype=np.float32)\\\\n    eef_quat = np.asarray(rs[\\\\\\\"eef\\\\\\\"][\\\\\\\"quat\\\\\\\"], dtype=np.float64)\\\\n    gripper_qpos = np.asarray(rs[\\\\\\\"gripper\\\\\\\"][\\\\\\\"qpos\\\\\\\"], dtype=np.float32)\\\\n    eef_aa = quat_to_axis_angle(eef_quat)\\\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\\\n\\\\n\\\\ndef obs_to_\\\\n\\\\n... [截断: 输出过长，省略 9638 字符] ...\\\\n\\\\n: Path):\\\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\\\n\\\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\\\n    ax = axes[0]\\\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\\\n    task_ids = sorted(all_results.keys())\\\\n\\\\n    for ti, task_id in enumerate(task_ids):\\\\n        episodes = all_results[task_id]\\\\n        for ep_data in episodes:\\\\n            steps = ep_data[\\\\\\\"timesteps\\\\\\\"]\\\\n            l2_vals = [s[\\\\\\\"l2_distance\\\\\\\"] for s in steps]\\\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\\\n\\\\n    mean_curve = analysis[\\\\\\\"mean_l2_curve\\\\\\\"]\\\\n    std_curve = analysis[\\\\\\\"std_l2_curve\\\\\\\"]\\\\n    x = np.arange(len(mean_curve))\\\\n    ax.plot(x, mean_curve, color=\\\\\\\"black\\\\\\\", linewidth=2, label=\\\\\\\"Mean\\\\\\\")\\\\n    mean_arr = np.array(mean_curve)\\\\n    std_arr = np.array(std_curve)\\\\n    valid = ~np.isnan(mean_arr)\\\\n    ax.fill_between(\\\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\\\n        alpha=0.15, color=\\\\\\\"black\\\\\\\"\\\\n    )\\\\n    ax.set_xlabel(\\\\\\\"Timestep\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"L2 Action Distance\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Baseline vs ACIS k=0.7: Action Divergence\\\\\\\")\\\\n    ax.legend(loc=\\\\\\\"upper left\\\\\\\")\\\\n    ax.grid(True, alpha=0.3)\\\\n\\\\n    # Plot 2: Per-dimension breakdown\\\\n    ax = axes[1]\\\\n    dim_data = analysis[\\\\\\\"per_dim_mean_abs_diff\\\\\\\"]\\\\n    names = list(dim_data.keys())\\\\n    values = list(dim_data.values())\\\\n    bar_colors = [\\\\\\\"#2196F3\\\\\\\"] * 3 + [\\\\\\\"#FF9800\\\\\\\"] * 3 + [\\\\\\\"#4CAF50\\\\\\\"]\\\\n    ax.bar(names, values, color=bar_colors)\\\\n    ax.set_xlabel(\\\\\\\"Action Dimension\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"Mean |Difference|\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Per-Dimension Divergence\\\\\\\")\\\\n    ax.set_xticklabels(names, rotation=45, ha=\\\\\\\"right\\\\\\\")\\\\n    ax.grid(True, alpha=0.3, axis=\\\\\\\"y\\\\\\\")\\\\n\\\\n    # Plot 3: Per-task mean curves\\\\n    ax = axes[2]\\\\n    for ti, task_id in enumerate(task_ids):\\\\n        episodes = all_results[task_id]\\\\n        task_l2s = []\\\\n        for ep_data in episodes:\\\\n            l2_vals = [s[\\\\\\\"l2_distance\\\\\\\"] for s in ep_data[\\\\\\\"timesteps\\\\\\\"]]\\\\n            task_l2s.append(l2_vals)\\\\n        max_t = max(len(c) for c in task_l2s)\\\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\\\n        for i, c in enumerate(task_l2s):\\\\n            padded[i, :len(c)] = c\\\\n        task_mean = np.nanmean(padded, axis=0)\\\\n        task_desc = episodes[0][\\\\\\\"task_desc\\\\\\\"]\\\\n        short_desc = task_desc[:30] + \\\\\\\"...\\\\\\\" if len(task_desc) > 30 else task_desc\\\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\\\\\"T{task_id}: {short_desc}\\\\\\\", color=colors[ti % 10])\\\\n    ax.set_xlabel(\\\\\\\"Timestep\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"L2 Action Distance\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Per-Task Mean Divergence\\\\\\\")\\\\n    ax.legend(fontsize=7, loc=\\\\\\\"upper left\\\\\\\")\\\\n    ax.grid(True, alpha=0.3)\\\\n\\\\n    plt.tight_layout()\\\\n    pdf_path = output_dir / \\\\\\\"action_divergence_curve.pdf\\\\\\\"\\\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.savefig(output_dir / \\\\\\\"action_divergence_curve.png\\\\\\\", dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n    log.info(\\\\\\\"Plots saved to %s\\\\\\\", pdf_path)\\\\n\\\\n    # Summary stats figure\\\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\\\n    ax2.axis(\\\\\\\"off\\\\\\\")\\\\n    summary_text = (\\\\n        f\\\\\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"{'='*50}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Num episodes:           {analysis['num_episodes']}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Max episode length:     {analysis['max_episode_length']}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"\\\\\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\\\\\n\\\\\\\"\\\\n    )\\\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\\\n             verticalalignment=\\\\\\\"top\\\\\\\", fontfamily=\\\\\\\"monospace\\\\\\\")\\\\n    plt.tight_layout()\\\\n    plt.savefig(output_dir / \\\\\\\"action_divergence_summary.pdf\\\\\\\", dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    args = parse_args()\\\\n    run_divergence_analysis(args)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.26}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Per-step Action Divergence Analysis: Baseline vs ACIS-pruned model.\\n\\nDrives the environment with baseline actions while recording both models'\\naction outputs at each timestep (same observation). Produces divergence curves\\nand per-dimension breakdown.\\n\\nUsage:\\n    python analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n# Paths\\nBASELINE_CKPT = \\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\"\\nACIS_CKPT = \\\"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\\\"\\nBASELINE_CONFIG = \\\"configs/libero_baseline.yaml\\\"\\nACIS_CONFIG = \\\"configs/libero_acis_stage1only_k07.yaml\\\"\\n\\nSUITE = \\\"libero_object\\\"\\nMAX_STEPS = 280\\nACTION_HORIZON = 50\\nACTION_DIM_NAMES = [\\\"pos_x\\\", \\\"pos_y\\\", \\\"pos_z\\\", \\\"rot_x\\\", \\\"rot_y\\\", \\\"rot_z\\\", \\\"gripper\\\"]\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--gpu\\\", type=int, default=2)\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=5)\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=\\\"0,1,2\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--output_dir\\\", type=str, default=\\\"artifacts\\\")\\n    return p.parse_args()\\n\\n\\ndef load_config(config_path: str) -> dict:\\n    import copy\\n    import yaml\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        for k, v in config.items():\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\n                base_config[k].update(v)\\n            else:\\n                base_config[k] = v\\n        return base_config\\n    return config\\n\\n\\ndef load_baseline_model(device):\\n    from train import load_smolvla_policy\\n    config = load_config(BASELINE_CONFIG)\\n    policy = load_smolvla_policy(config, device)\\n    ckpt = torch.load(BASELINE_CKPT, map_location=device, weights_only=False)\\n    policy.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    policy.eval()\\n    return policy, config\\n\\n\\ndef load_acis_model(device):\\n    from train import load_smolvla_policy, wrap_with_imm\\n    config = load_config(ACIS_CONFIG)\\n    policy = load_smolvla_policy(config, device)\\n    wrapper = wrap_with_imm(policy, config)\\n    wrapper.to(device)\\n    ckpt = torch.load(ACIS_CKPT, map_location=device, weights_only=False)\\n    wrapper.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    wrapper.eval()\\n    return wrapper.policy, wrapper, config\\n\\n\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\n\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\n    q = quat.astype(np.float64)\\n    w = np.clip(q[3], -1.0, 1.0)\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\n    if den > 1e-10:\\n        angle = 2.0 * np.arccos(w)\\n        axis = q[:3] / den\\n        return (axis * angle).astype(np.float32)\\n    return np.zeros(3, dtype=np.float32)\\n\\n\\ndef extract_state(obs: dict) -> np.ndarray:\\n    rs = obs[\\\"robot_state\\\"]\\n    eef_pos = np.asarray(rs[\\\"eef\\\"][\\\"pos\\\"], dtype=np.float32)\\n    eef_quat = np.asarray(rs[\\\"eef\\\"][\\\"quat\\\"], dtype=np.float64)\\n    gripper_qpos = np.asarray(rs[\\\"gripper\\\"][\\\"qpos\\\"], dtype=np.float32)\\n    eef_aa = quat_to_axis_angle(eef_quat)\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\n\\n\\ndef obs_to_\\n\\n... [截断: 输出过长，省略 9638 字符] ...\\n\\n: Path):\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\n\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\n    ax = axes[0]\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\n    task_ids = sorted(all_results.keys())\\n\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        for ep_data in episodes:\\n            steps = ep_data[\\\"timesteps\\\"]\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in steps]\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\n\\n    mean_curve = analysis[\\\"mean_l2_curve\\\"]\\n    std_curve = analysis[\\\"std_l2_curve\\\"]\\n    x = np.arange(len(mean_curve))\\n    ax.plot(x, mean_curve, color=\\\"black\\\", linewidth=2, label=\\\"Mean\\\")\\n    mean_arr = np.array(mean_curve)\\n    std_arr = np.array(std_curve)\\n    valid = ~np.isnan(mean_arr)\\n    ax.fill_between(\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\n        alpha=0.15, color=\\\"black\\\"\\n    )\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Baseline vs ACIS k=0.7: Action Divergence\\\")\\n    ax.legend(loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    # Plot 2: Per-dimension breakdown\\n    ax = axes[1]\\n    dim_data = analysis[\\\"per_dim_mean_abs_diff\\\"]\\n    names = list(dim_data.keys())\\n    values = list(dim_data.values())\\n    bar_colors = [\\\"#2196F3\\\"] * 3 + [\\\"#FF9800\\\"] * 3 + [\\\"#4CAF50\\\"]\\n    ax.bar(names, values, color=bar_colors)\\n    ax.set_xlabel(\\\"Action Dimension\\\")\\n    ax.set_ylabel(\\\"Mean |Difference|\\\")\\n    ax.set_title(\\\"Per-Dimension Divergence\\\")\\n    ax.set_xticklabels(names, rotation=45, ha=\\\"right\\\")\\n    ax.grid(True, alpha=0.3, axis=\\\"y\\\")\\n\\n    # Plot 3: Per-task mean curves\\n    ax = axes[2]\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        task_l2s = []\\n        for ep_data in episodes:\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in ep_data[\\\"timesteps\\\"]]\\n            task_l2s.append(l2_vals)\\n        max_t = max(len(c) for c in task_l2s)\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\n        for i, c in enumerate(task_l2s):\\n            padded[i, :len(c)] = c\\n        task_mean = np.nanmean(padded, axis=0)\\n        task_desc = episodes[0][\\\"task_desc\\\"]\\n        short_desc = task_desc[:30] + \\\"...\\\" if len(task_desc) > 30 else task_desc\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\"T{task_id}: {short_desc}\\\", color=colors[ti % 10])\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Per-Task Mean Divergence\\\")\\n    ax.legend(fontsize=7, loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    plt.tight_layout()\\n    pdf_path = output_dir / \\\"action_divergence_curve.pdf\\\"\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.savefig(output_dir / \\\"action_divergence_curve.png\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    log.info(\\\"Plots saved to %s\\\", pdf_path)\\n\\n    # Summary stats figure\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\n    ax2.axis(\\\"off\\\")\\n    summary_text = (\\n        f\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\n\\\"\\n        f\\\"{'='*50}\\\\n\\\"\\n        f\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\n\\\"\\n        f\\\"Num episodes:           {analysis['num_episodes']}\\\\n\\\"\\n        f\\\"Max episode length:     {analysis['max_episode_length']}\\\\n\\\"\\n        f\\\"\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\n\\\"\\n        f\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\n\\\"\\n    )\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\n             verticalalignment=\\\"top\\\", fontfamily=\\\"monospace\\\")\\n    plt.tight_layout()\\n    plt.savefig(output_dir / \\\"action_divergence_summary.pdf\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_divergence_analysis(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.26}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T10:37:28.586Z_

<details><summary>↩ Tool result · `toolu_01F4s4zkVJUz5jyDn4niPhnC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/:\\ntotal 899324\\ndrwxr-xr-x 2 root root        35 May 17 16:22 .\\ndrwxr-xr-x 3 root root        33 May 17 16:10 ..\\n-rw-r--r-- 1 root root 920907737 May 17 15:57 checkpoint.pt\\n\\n/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k07/stage1_done/:\\ntotal 899324\\ndrwxr-xr-x 2 root root        35 May 17 16:22 .\\ndrwxr-xr-x 3 root root        33 May 17 16:10 ..\\n-rw-r--r-- 1 root root 920907737 May 17 15:56 checkpoint.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.72}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "a468c9f1-c48c-4233-8a14-4fec3fc0dd5c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/:\\\\ntotal 899324\\\\ndrwxr-xr-x 2 root root        35 May 17 16:22 .\\\\ndrwxr-xr-x 3 root root        33 May 17 16:10 ..\\\\n-rw-r--r-- 1 root root 920907737 May 17 15:57 checkpoint.pt\\\\n\\\\n/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k07/stage1_done/:\\\\ntotal 899324\\\\ndrwxr-xr-x 2 root root        35 May 17 16:22 .\\\\ndrwxr-xr-x 3 root root        33 May 17 16:10 ..\\\\n-rw-r--r-- 1 root root 920907737 May 17 15:56 checkpoint.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.72}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/:\\ntotal 899324\\ndrwxr-xr-x 2 root root        35 May 17 16:22 .\\ndrwxr-xr-x 3 root root        33 May 17 16:10 ..\\n-rw-r--r-- 1 root root 920907737 May 17 15:57 checkpoint.pt\\n\\n/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k07/stage1_done/:\\ntotal 899324\\ndrwxr-xr-x 2 root root        35 May 17 16:22 .\\ndrwxr-xr-x 3 root root        33 May 17 16:10 ..\\n-rw-r--r-- 1 root root 920907737 May 17 15:56 checkpoint.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.72}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T10:37:28.596Z_

<details><summary>↩ Tool result · `toolu_01N4DWFHwBoRiroqMpBvRRkK`</summary>

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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "33f86b57-6c02-4ccc-8b3f-8947c252160b",
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

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Let me get the register_acis_hook function from the eval script, and also check if there's a k=0.5 checkpoint.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "04d84638-1977-4122-9eb0-b2f3894d11b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDzySWt42oKaJCvcVBqJZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 25321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4601
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

Now let me check the hook registration logic and whether a k=0.5 checkpoint exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "be21d355-42ab-4257-9309-eea39d502769",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDzySWt42oKaJCvcVBqJZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 25321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4601
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0143FhE9536RLReQXMmbPAmm`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"register_acis_hook\\|def register\\|def wrap_with_imm\\|true_removal\\|bypass\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "0fcaf83a-e34c-4a1b-8107-399874989163",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDzySWt42oKaJCvcVBqJZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 25321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4601
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

_source line 17 · 2026-05-17T10:37:37.827Z_

<details><summary>↩ Tool result · `toolu_0143FhE9536RLReQXMmbPAmm`</summary>

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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "9a5e3745-c6c3-4f1f-b309-958a61a7712c",
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

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ECJZQekniWyhCNACZL16LA`</summary>

```json
{
  "server": "westd-27271",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only/",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "79141422-14db-446d-846e-d8e9a31f63f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDzySWt42oKaJCvcVBqJZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 25321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4601
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

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014YBGWDy6EkgxpqF1yh12Vb`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"register_acis_hook\\|def register\\|true_removal\\|bypass\\|pruning_hook\\|keep_ratio\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "6c3a8d67-e520-46eb-9ce5-2ebbc4f52a4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDzySWt42oKaJCvcVBqJZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 25321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4601
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

_source line 20 · 2026-05-17T10:37:40.234Z_

<details><summary>↩ Tool result · `toolu_01ECJZQekniWyhCNACZL16LA`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.73}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "4867b6a6-1139-4b21-8a5e-c38d512727c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only/': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.73}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.73}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T10:37:40.244Z_

<details><summary>↩ Tool result · `toolu_014YBGWDy6EkgxpqF1yh12Vb`</summary>

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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "d6ef0cfe-a01e-4833-b24e-1236caef089d",
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

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
The ssh_read_only tool doesn't allow pipe characters. Let me use grep without pipes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "858c845a-a360-45e1-b452-bc432d44a760",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbUVvN9DKoHWydoYZ2E7er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 29922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
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

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MG2d8vwsP22E8RVNMTLsBu`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"register_acis_hook\\|def register\\|true_removal\\|bypass\\|pruning_hook\\|keep_ratio\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "c979073d-3ad0-48e6-9bc8-6f8714f28d7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbUVvN9DKoHWydoYZ2E7er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 29922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
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

_source line 24 · 2026-05-17T10:37:45.144Z_

<details><summary>↩ Tool result · `toolu_01MG2d8vwsP22E8RVNMTLsBu`</summary>

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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "736a2a18-f8ca-4760-b520-9eae645954a7",
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

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013ojNEY9JpvyBub2SsnKPSQ`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"register_acis_hook\\|true_removal\\|bypass\\|pruning_hook\\|keep_ratio\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "8bb29474-b196-45ca-ad3f-6605e7978d71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbUVvN9DKoHWydoYZ2E7er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 29922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
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

_source line 26 · 2026-05-17T10:37:45.808Z_

<details><summary>↩ Tool result · `toolu_013ojNEY9JpvyBub2SsnKPSQ`</summary>

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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "335bca8b-28c0-4e50-949c-a0eb4185bdef",
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

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
The `\|` in grep is being treated as a shell metacharacter. Let me use `-e` flags instead for multiple patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "7f1b775e-8f4f-4b26-bfae-18af0b9b929d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQxQQ9Fz352fGtXD5QPTfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 30793,
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

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ND4U8182eiRiQdsWJ5Qk1r`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n -e \"register_acis_hook\" -e \"def register\" -e \"true_removal\" -e \"bypass\" -e \"pruning_hook\" -e \"keep_ratio\" /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "1f1b165c-6bff-440f-b30f-564ded3a4378",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQxQQ9Fz352fGtXD5QPTfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 30793,
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

_source line 29 · 2026-05-17T10:37:51.474Z_

<details><summary>↩ Tool result · `toolu_01ND4U8182eiRiQdsWJ5Qk1r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"74:                   choices=[\\\"zero_mask\\\", \\\"true_removal\\\", \\\"merge\\\"],\\n75:                   help=\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\")\\n225:def register_acis_hook(connector, mask: torch.Tensor, method: str = \\\"zero_mask\\\",\\n243:        if method == \\\"true_removal\\\":\\n400:                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n405:                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "94cbde49-6388-46ac-abba-4b71322eb29a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"74:                   choices=[\\\\\\\"zero_mask\\\\\\\", \\\\\\\"true_removal\\\\\\\", \\\\\\\"merge\\\\\\\"],\\\\n75:                   help=\\\\\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\\\\\")\\\\n225:def register_acis_hook(connector, mask: torch.Tensor, method: str = \\\\\\\"zero_mask\\\\\\\",\\\\n243:        if method == \\\\\\\"true_removal\\\\\\\":\\\\n400:                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\\\n405:                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.73}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"74:                   choices=[\\\"zero_mask\\\", \\\"true_removal\\\", \\\"merge\\\"],\\n75:                   help=\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\")\\n225:def register_acis_hook(connector, mask: torch.Tensor, method: str = \\\"zero_mask\\\",\\n243:        if method == \\\"true_removal\\\":\\n400:                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n405:                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KuFxerkTQEyRj7sNkfrTQL`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n -e \"register_acis_hook\" -e \"def register\" -e \"true_removal\" -e \"bypass\" -e \"pruning_hook\" -e \"keep_ratio\" -e \"wrap_with_imm\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "929b98cf-75d2-4d3e-a898-903fcf73a6d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQxQQ9Fz352fGtXD5QPTfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 30793,
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

_source line 31 · 2026-05-17T10:37:52.864Z_

<details><summary>↩ Tool result · `toolu_01KuFxerkTQEyRj7sNkfrTQL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"349:def wrap_with_imm(policy, config: Dict[str, Any]):\\n583:        model = wrap_with_imm(policy, config)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.14}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "db3d5345-f3c3-4eef-9e63-998cf5592102",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"349:def wrap_with_imm(policy, config: Dict[str, Any]):\\\\n583:        model = wrap_with_imm(policy, config)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.14}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"349:def wrap_with_imm(policy, config: Dict[str, Any]):\\n583:        model = wrap_with_imm(policy, config)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.14}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RxJi1M3gb88tWM4q18qbPW`</summary>

```json
{
  "server": "westd-27271",
  "command": "head -300 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "ae3e7432-500d-460e-a017-4d3c62f13ca8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XakPtyrtgystrZSfi5pY8B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 31476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 829
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

_source line 33 · 2026-05-17T10:37:57.019Z_

<details><summary>↩ Tool result · `toolu_01RxJi1M3gb88tWM4q18qbPW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO Success Rate Evaluation for SmolVLA / IMM models.\\n\\nEvaluates per-task and overall success rate on LIBERO benchmark suites.\\n\\nUsage:\\n    python eval_success_rate_libero.py \\\\\\n        --checkpoint checkpoints/libero_full_ft/step_025000/checkpoint.pt \\\\\\n        --config configs/libero_baseline.yaml \\\\\\n        --suite libero_object \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n    \\\"libero_90\\\": 400,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"LIBERO success rate evaluation\\\")\\n    p.add_argument(\\\"--checkpoint\\\", type=str, required=True,\\n                   help=\\\"Path to checkpoint.pt\\\")\\n    p.add_argument(\\\"--config\\\", type=str, default=\\\"configs/libero_baseline.yaml\\\",\\n                   help=\\\"Path to YAML config\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()),\\n                   help=\\\"LIBERO suite name\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50,\\n                   help=\\\"Episodes per task\\\")\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--action_horizon\\\", type=int, default=50,\\n                   help=\\\"Actions to execute per chunk before re-planning\\\")\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=None,\\n                   help=\\\"Override max steps per episode (default: per-suite)\\\")\\n    p.add_argument(\\\"--output\\\", type=str, default=None,\\n                   help=\\\"Output JSON path (default: eval_results/libero_{suite}.json)\\\")\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"acis_prune\\\", \\\"random_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=None,\\n                   help=\\\"Comma-separated task IDs to evaluate (default: all)\\\")\\n    p.add_argument(\\\"--pruning-method\\\", type=str, default=\\\"zero_mask\\\",\\n                   choices=[\\\"zero_mask\\\", \\\"true_removal\\\", \\\"merge\\\"],\\n                   help=\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\")\\n    p.add_argument(\\\"--merge_alpha\\\", type=float, default=1.0,\\n                   help=\\\"Weight for merged pruned tokens (only with --pruning_method merge)\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=None,\\n                   help=\\\"Override k_ratio from config (fraction of visual tokens to keep)\\\")\\n    return p.parse_args()\\n\\n\\n# --- Config -------------------------------------------------------------------\\n\\ndef load_config(config_path: str) -> dict:\\n    import copy\\n    import yaml\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        for k, v in config.items():\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\n                base_config[k].update(v)\\n            else:\\n                base_config[k] = v\\n        return base_config\\n    return config\\n\\n\\n# --- Model loading ------------------------------------------------------------\\n\\ndef load_model(args, device: torch.device):\\n    \\\"\\\"\\\"Returns (policy, wrapper_or_None, config).\\\"\\\"\\\"\\n    from train import load_smolvla_policy, wrap_with_imm\\n\\n    c\\n\\n... [截断: 输出过长，省略 3865 字符] ...\\n\\ndevice=device)\\n    mask.scatter_(1, topk_idx, 1.0)\\n    return mask\\n\\n\\n@torch.no_grad()\\ndef compute_random_mask(wrapper, batch: dict, device: torch.device) -> torch.Tensor:\\n    \\\"\\\"\\\"Random baseline: replace ACIS scores with uniform random scores.\\\"\\\"\\\"\\n    images, _ = wrapper.policy.prepare_images(batch)\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\n    B, N_vis = vis_tokens.shape[0], vis_tokens.shape[1]\\n    k = max(1, int(N_vis * wrapper.k_ratio))\\n    scores = torch.rand(B, N_vis, device=device)\\n    _, topk_idx = torch.topk(scores, k, dim=-1)\\n    mask = torch.zeros(B, N_vis, device=device)\\n    mask.scatter_(1, topk_idx, 1.0)\\n    return mask\\n\\n\\ndef register_acis_hook(connector, mask: torch.Tensor, method: str = \\\"zero_mask\\\",\\n                      merge_alpha: float = 1.0):\\n    state = {\\\"offset\\\": 0}\\n\\n    def hook_fn(module, input, output):\\n        tokens = output[0] if isinstance(output, tuple) else output\\n        if tokens.dim() != 3:\\n            return output\\n        n = tokens.shape[1]\\n        offset = state[\\\"offset\\\"]\\n        if offset + n > mask.shape[1]:\\n            return output\\n        cam_mask = mask[:, offset:offset + n]\\n        state[\\\"offset\\\"] = offset + n\\n\\n        B, N, D = tokens.shape\\n        keep_mask = cam_mask[:B]\\n\\n        if method == \\\"true_removal\\\":\\n            kept = keep_mask[0].bool()\\n            masked = tokens[:, kept, :]\\n        elif method == \\\"merge\\\":\\n            k = int(keep_mask[0].sum().item())\\n            keep_indices = keep_mask[0].nonzero(as_tuple=False).squeeze(-1).float()\\n            prune_indices = (1 - keep_mask[0]).nonzero(as_tuple=False).squeeze(-1).float()\\n            keep_idx_int = keep_indices.long()\\n            result_tokens = tokens[:, keep_idx_int, :].clone()\\n            if prune_indices.numel() > 0:\\n                dists = (prune_indices.unsqueeze(1) - keep_indices.unsqueeze(0)).abs()\\n                nearest = dists.argmin(dim=1)\\n                prune_idx_int = prune_indices.long()\\n                for b in range(B):\\n                    pruned_vals = tokens[b, prune_idx_int, :]\\n                    accum = torch.zeros(k, D, device=tokens.device, dtype=tokens.dtype)\\n                    count = torch.zeros(k, 1, device=tokens.device, dtype=tokens.dtype)\\n                    accum.scatter_add_(0, nearest.unsqueeze(-1).expand(-1, D), pruned_vals)\\n                    ones = torch.ones(prune_idx_int.shape[0], 1, device=tokens.device, dtype=tokens.dtype)\\n                    count.scatter_add_(0, nearest.unsqueeze(-1), ones)\\n                    mean_pruned = torch.where(count > 0, accum / count, torch.zeros_like(accum))\\n                    result_tokens[b] = result_tokens[b] + merge_alpha * mean_pruned\\n            masked = result_tokens\\n        else:\\n            masked = tokens * keep_mask.unsqueeze(-1)\\n\\n        if isinstance(output, tuple):\\n            return (masked,) + output[1:]\\n        return masked\\n    return connector.register_forward_hook(hook_fn)\\n\\n\\n# --- Action prediction -------------------------------------------------------\\n\\n@torch.no_grad()\\ndef predict_actions(policy, batch: dict) -> torch.Tensor:\\n    \\\"\\\"\\\"Returns (chunk_size, action_dim) actions for batch_size=1.\\\"\\\"\\\"\\n    images, img_masks = policy.prepare_images(batch)\\n    state = policy.prepare_state(batch)\\n    lang_tokens = batch[\\\"observation.language.tokens\\\"]\\n    lang_masks = batch[\\\"observation.language.attention_mask\\\"]\\n\\n    actions = policy.model.sample_actions(\\n        images, img_masks, lang_tokens, lang_masks, state\\n    )\\n    original_action_dim = policy.config.action_feature.shape[0]\\n    return actions[0, :, :original_action_dim]  # (chunk_size, action_dim)\\n\\n\\n# --- Statistics ---------------------------------------------------------------\\n\\ndef wilson_ci(successes: int, total: int, z: float = 1.96):\\n    if total == 0:\\n        return 0.0, 0.0, 1.0\\n    p = successes / total\\n    denom = 1 + z ** 2 / total\\n    center = (p + z ** 2 / (2 * total)) / denom\\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.22}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "19b1d512-5840-475a-8cd4-22819bedbaf0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO Success Rate Evaluation for SmolVLA / IMM models.\\\\n\\\\nEvaluates per-task and overall success rate on LIBERO benchmark suites.\\\\n\\\\nUsage:\\\\n    python eval_success_rate_libero.py \\\\\\\\\\\\n        --checkpoint checkpoints/libero_full_ft/step_025000/checkpoint.pt \\\\\\\\\\\\n        --config configs/libero_baseline.yaml \\\\\\\\\\\\n        --suite libero_object \\\\\\\\\\\\n        --num_episodes 50 \\\\\\\\\\\\n        --gpu 0\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nimport time as time_mod\\\\nfrom pathlib import Path\\\\n\\\\nos.environ.setdefault(\\\\\\\"MUJOCO_GL\\\\\\\", \\\\\\\"egl\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"TRANSFORMERS_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"HF_HUB_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\n\\\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\nSUITE_MAX_STEPS = {\\\\n    \\\\\\\"libero_spatial\\\\\\\": 280,\\\\n    \\\\\\\"libero_object\\\\\\\": 280,\\\\n    \\\\\\\"libero_goal\\\\\\\": 300,\\\\n    \\\\\\\"libero_10\\\\\\\": 520,\\\\n    \\\\\\\"libero_90\\\\\\\": 400,\\\\n}\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"LIBERO success rate evaluation\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--checkpoint\\\\\\\", type=str, required=True,\\\\n                   help=\\\\\\\"Path to checkpoint.pt\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--config\\\\\\\", type=str, default=\\\\\\\"configs/libero_baseline.yaml\\\\\\\",\\\\n                   help=\\\\\\\"Path to YAML config\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", type=str, default=\\\\\\\"libero_object\\\\\\\",\\\\n                   choices=list(SUITE_MAX_STEPS.keys()),\\\\n                   help=\\\\\\\"LIBERO suite name\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--num_episodes\\\\\\\", type=int, default=50,\\\\n                   help=\\\\\\\"Episodes per task\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--action_horizon\\\\\\\", type=int, default=50,\\\\n                   help=\\\\\\\"Actions to execute per chunk before re-planning\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--max_steps\\\\\\\", type=int, default=None,\\\\n                   help=\\\\\\\"Override max steps per episode (default: per-suite)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--output\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Output JSON path (default: eval_results/libero_{suite}.json)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--mode\\\\\\\", choices=[\\\\\\\"baseline\\\\\\\", \\\\\\\"acis_prune\\\\\\\", \\\\\\\"random_prune\\\\\\\"], default=\\\\\\\"baseline\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--task_ids\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Comma-separated task IDs to evaluate (default: all)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--pruning-method\\\\\\\", type=str, default=\\\\\\\"zero_mask\\\\\\\",\\\\n                   choices=[\\\\\\\"zero_mask\\\\\\\", \\\\\\\"true_removal\\\\\\\", \\\\\\\"merge\\\\\\\"],\\\\n                   help=\\\\\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--merge_alpha\\\\\\\", type=float, default=1.0,\\\\n                   help=\\\\\\\"Weight for merged pruned tokens (only with --pruning_method merge)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--k_ratio\\\\\\\", type=float, default=None,\\\\n                   help=\\\\\\\"Override k_ratio from config (fraction of visual tokens to keep)\\\\\\\")\\\\n    return p.parse_args()\\\\n\\\\n\\\\n# --- Config -------------------------------------------------------------------\\\\n\\\\ndef load_config(config_path: str) -> dict:\\\\n    import copy\\\\n    import yaml\\\\n    config_path = Path(config_path)\\\\n    with open(config_path) as f:\\\\n        config = yaml.safe_load(f)\\\\n    if \\\\\\\"_base_\\\\\\\" in config:\\\\n        base_path = config_path.parent / config.pop(\\\\\\\"_base_\\\\\\\")\\\\n        base_config = load_config(str(base_path))\\\\n        for k, v in config.items():\\\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\\\n                base_config[k].update(v)\\\\n            else:\\\\n                base_config[k] = v\\\\n        return base_config\\\\n    return config\\\\n\\\\n\\\\n# --- Model loading ------------------------------------------------------------\\\\n\\\\ndef load_model(args, device: torch.device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Returns (policy, wrapper_or_None, config).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    from train import load_smolvla_policy, wrap_with_imm\\\\n\\\\n    c\\\\n\\\\n... [截断: 输出过长，省略 3865 字符] ...\\\\n\\\\ndevice=device)\\\\n    mask.scatter_(1, topk_idx, 1.0)\\\\n    return mask\\\\n\\\\n\\\\n@torch.no_grad()\\\\ndef compute_random_mask(wrapper, batch: dict, device: torch.device) -> torch.Tensor:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Random baseline: replace ACIS scores with uniform random scores.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    images, _ = wrapper.policy.prepare_images(batch)\\\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\\\n    B, N_vis = vis_tokens.shape[0], vis_tokens.shape[1]\\\\n    k = max(1, int(N_vis * wrapper.k_ratio))\\\\n    scores = torch.rand(B, N_vis, device=device)\\\\n    _, topk_idx = torch.topk(scores, k, dim=-1)\\\\n    mask = torch.zeros(B, N_vis, device=device)\\\\n    mask.scatter_(1, topk_idx, 1.0)\\\\n    return mask\\\\n\\\\n\\\\ndef register_acis_hook(connector, mask: torch.Tensor, method: str = \\\\\\\"zero_mask\\\\\\\",\\\\n                      merge_alpha: float = 1.0):\\\\n    state = {\\\\\\\"offset\\\\\\\": 0}\\\\n\\\\n    def hook_fn(module, input, output):\\\\n        tokens = output[0] if isinstance(output, tuple) else output\\\\n        if tokens.dim() != 3:\\\\n            return output\\\\n        n = tokens.shape[1]\\\\n        offset = state[\\\\\\\"offset\\\\\\\"]\\\\n        if offset + n > mask.shape[1]:\\\\n            return output\\\\n        cam_mask = mask[:, offset:offset + n]\\\\n        state[\\\\\\\"offset\\\\\\\"] = offset + n\\\\n\\\\n        B, N, D = tokens.shape\\\\n        keep_mask = cam_mask[:B]\\\\n\\\\n        if method == \\\\\\\"true_removal\\\\\\\":\\\\n            kept = keep_mask[0].bool()\\\\n            masked = tokens[:, kept, :]\\\\n        elif method == \\\\\\\"merge\\\\\\\":\\\\n            k = int(keep_mask[0].sum().item())\\\\n            keep_indices = keep_mask[0].nonzero(as_tuple=False).squeeze(-1).float()\\\\n            prune_indices = (1 - keep_mask[0]).nonzero(as_tuple=False).squeeze(-1).float()\\\\n            keep_idx_int = keep_indices.long()\\\\n            result_tokens = tokens[:, keep_idx_int, :].clone()\\\\n            if prune_indices.numel() > 0:\\\\n                dists = (prune_indices.unsqueeze(1) - keep_indices.unsqueeze(0)).abs()\\\\n                nearest = dists.argmin(dim=1)\\\\n                prune_idx_int = prune_indices.long()\\\\n                for b in range(B):\\\\n                    pruned_vals = tokens[b, prune_idx_int, :]\\\\n                    accum = torch.zeros(k, D, device=tokens.device, dtype=tokens.dtype)\\\\n                    count = torch.zeros(k, 1, device=tokens.device, dtype=tokens.dtype)\\\\n                    accum.scatter_add_(0, nearest.unsqueeze(-1).expand(-1, D), pruned_vals)\\\\n                    ones = torch.ones(prune_idx_int.shape[0], 1, device=tokens.device, dtype=tokens.dtype)\\\\n                    count.scatter_add_(0, nearest.unsqueeze(-1), ones)\\\\n                    mean_pruned = torch.where(count > 0, accum / count, torch.zeros_like(accum))\\\\n                    result_tokens[b] = result_tokens[b] + merge_alpha * mean_pruned\\\\n            masked = result_tokens\\\\n        else:\\\\n            masked = tokens * keep_mask.unsqueeze(-1)\\\\n\\\\n        if isinstance(output, tuple):\\\\n            return (masked,) + output[1:]\\\\n        return masked\\\\n    return connector.register_forward_hook(hook_fn)\\\\n\\\\n\\\\n# --- Action prediction -------------------------------------------------------\\\\n\\\\n@torch.no_grad()\\\\ndef predict_actions(policy, batch: dict) -> torch.Tensor:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Returns (chunk_size, action_dim) actions for batch_size=1.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    images, img_masks = policy.prepare_images(batch)\\\\n    state = policy.prepare_state(batch)\\\\n    lang_tokens = batch[\\\\\\\"observation.language.tokens\\\\\\\"]\\\\n    lang_masks = batch[\\\\\\\"observation.language.attention_mask\\\\\\\"]\\\\n\\\\n    actions = policy.model.sample_actions(\\\\n        images, img_masks, lang_tokens, lang_masks, state\\\\n    )\\\\n    original_action_dim = policy.config.action_feature.shape[0]\\\\n    return actions[0, :, :original_action_dim]  # (chunk_size, action_dim)\\\\n\\\\n\\\\n# --- Statistics ---------------------------------------------------------------\\\\n\\\\ndef wilson_ci(successes: int, total: int, z: float = 1.96):\\\\n    if total == 0:\\\\n        return 0.0, 0.0, 1.0\\\\n    p = successes / total\\\\n    denom = 1 + z ** 2 / total\\\\n    center = (p + z ** 2 / (2 * total)) / denom\\\\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.22}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO Success Rate Evaluation for SmolVLA / IMM models.\\n\\nEvaluates per-task and overall success rate on LIBERO benchmark suites.\\n\\nUsage:\\n    python eval_success_rate_libero.py \\\\\\n        --checkpoint checkpoints/libero_full_ft/step_025000/checkpoint.pt \\\\\\n        --config configs/libero_baseline.yaml \\\\\\n        --suite libero_object \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n    \\\"libero_90\\\": 400,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"LIBERO success rate evaluation\\\")\\n    p.add_argument(\\\"--checkpoint\\\", type=str, required=True,\\n                   help=\\\"Path to checkpoint.pt\\\")\\n    p.add_argument(\\\"--config\\\", type=str, default=\\\"configs/libero_baseline.yaml\\\",\\n                   help=\\\"Path to YAML config\\\")\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\",\\n                   choices=list(SUITE_MAX_STEPS.keys()),\\n                   help=\\\"LIBERO suite name\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50,\\n                   help=\\\"Episodes per task\\\")\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--action_horizon\\\", type=int, default=50,\\n                   help=\\\"Actions to execute per chunk before re-planning\\\")\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=None,\\n                   help=\\\"Override max steps per episode (default: per-suite)\\\")\\n    p.add_argument(\\\"--output\\\", type=str, default=None,\\n                   help=\\\"Output JSON path (default: eval_results/libero_{suite}.json)\\\")\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"acis_prune\\\", \\\"random_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=None,\\n                   help=\\\"Comma-separated task IDs to evaluate (default: all)\\\")\\n    p.add_argument(\\\"--pruning-method\\\", type=str, default=\\\"zero_mask\\\",\\n                   choices=[\\\"zero_mask\\\", \\\"true_removal\\\", \\\"merge\\\"],\\n                   help=\\\"zero_mask: zero out pruned tokens; true_removal: drop pruned tokens from sequence; merge: merge pruned into nearest kept\\\")\\n    p.add_argument(\\\"--merge_alpha\\\", type=float, default=1.0,\\n                   help=\\\"Weight for merged pruned tokens (only with --pruning_method merge)\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=None,\\n                   help=\\\"Override k_ratio from config (fraction of visual tokens to keep)\\\")\\n    return p.parse_args()\\n\\n\\n# --- Config -------------------------------------------------------------------\\n\\ndef load_config(config_path: str) -> dict:\\n    import copy\\n    import yaml\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        for k, v in config.items():\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\n                base_config[k].update(v)\\n            else:\\n                base_config[k] = v\\n        return base_config\\n    return config\\n\\n\\n# --- Model loading ------------------------------------------------------------\\n\\ndef load_model(args, device: torch.device):\\n    \\\"\\\"\\\"Returns (policy, wrapper_or_None, config).\\\"\\\"\\\"\\n    from train import load_smolvla_policy, wrap_with_imm\\n\\n    c\\n\\n... [截断: 输出过长，省略 3865 字符] ...\\n\\ndevice=device)\\n    mask.scatter_(1, topk_idx, 1.0)\\n    return mask\\n\\n\\n@torch.no_grad()\\ndef compute_random_mask(wrapper, batch: dict, device: torch.device) -> torch.Tensor:\\n    \\\"\\\"\\\"Random baseline: replace ACIS scores with uniform random scores.\\\"\\\"\\\"\\n    images, _ = wrapper.policy.prepare_images(batch)\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\n    B, N_vis = vis_tokens.shape[0], vis_tokens.shape[1]\\n    k = max(1, int(N_vis * wrapper.k_ratio))\\n    scores = torch.rand(B, N_vis, device=device)\\n    _, topk_idx = torch.topk(scores, k, dim=-1)\\n    mask = torch.zeros(B, N_vis, device=device)\\n    mask.scatter_(1, topk_idx, 1.0)\\n    return mask\\n\\n\\ndef register_acis_hook(connector, mask: torch.Tensor, method: str = \\\"zero_mask\\\",\\n                      merge_alpha: float = 1.0):\\n    state = {\\\"offset\\\": 0}\\n\\n    def hook_fn(module, input, output):\\n        tokens = output[0] if isinstance(output, tuple) else output\\n        if tokens.dim() != 3:\\n            return output\\n        n = tokens.shape[1]\\n        offset = state[\\\"offset\\\"]\\n        if offset + n > mask.shape[1]:\\n            return output\\n        cam_mask = mask[:, offset:offset + n]\\n        state[\\\"offset\\\"] = offset + n\\n\\n        B, N, D = tokens.shape\\n        keep_mask = cam_mask[:B]\\n\\n        if method == \\\"true_removal\\\":\\n            kept = keep_mask[0].bool()\\n            masked = tokens[:, kept, :]\\n        elif method == \\\"merge\\\":\\n            k = int(keep_mask[0].sum().item())\\n            keep_indices = keep_mask[0].nonzero(as_tuple=False).squeeze(-1).float()\\n            prune_indices = (1 - keep_mask[0]).nonzero(as_tuple=False).squeeze(-1).float()\\n            keep_idx_int = keep_indices.long()\\n            result_tokens = tokens[:, keep_idx_int, :].clone()\\n            if prune_indices.numel() > 0:\\n                dists = (prune_indices.unsqueeze(1) - keep_indices.unsqueeze(0)).abs()\\n                nearest = dists.argmin(dim=1)\\n                prune_idx_int = prune_indices.long()\\n                for b in range(B):\\n                    pruned_vals = tokens[b, prune_idx_int, :]\\n                    accum = torch.zeros(k, D, device=tokens.device, dtype=tokens.dtype)\\n                    count = torch.zeros(k, 1, device=tokens.device, dtype=tokens.dtype)\\n                    accum.scatter_add_(0, nearest.unsqueeze(-1).expand(-1, D), pruned_vals)\\n                    ones = torch.ones(prune_idx_int.shape[0], 1, device=tokens.device, dtype=tokens.dtype)\\n                    count.scatter_add_(0, nearest.unsqueeze(-1), ones)\\n                    mean_pruned = torch.where(count > 0, accum / count, torch.zeros_like(accum))\\n                    result_tokens[b] = result_tokens[b] + merge_alpha * mean_pruned\\n            masked = result_tokens\\n        else:\\n            masked = tokens * keep_mask.unsqueeze(-1)\\n\\n        if isinstance(output, tuple):\\n            return (masked,) + output[1:]\\n        return masked\\n    return connector.register_forward_hook(hook_fn)\\n\\n\\n# --- Action prediction -------------------------------------------------------\\n\\n@torch.no_grad()\\ndef predict_actions(policy, batch: dict) -> torch.Tensor:\\n    \\\"\\\"\\\"Returns (chunk_size, action_dim) actions for batch_size=1.\\\"\\\"\\\"\\n    images, img_masks = policy.prepare_images(batch)\\n    state = policy.prepare_state(batch)\\n    lang_tokens = batch[\\\"observation.language.tokens\\\"]\\n    lang_masks = batch[\\\"observation.language.attention_mask\\\"]\\n\\n    actions = policy.model.sample_actions(\\n        images, img_masks, lang_tokens, lang_masks, state\\n    )\\n    original_action_dim = policy.config.action_feature.shape[0]\\n    return actions[0, :, :original_action_dim]  # (chunk_size, action_dim)\\n\\n\\n# --- Statistics ---------------------------------------------------------------\\n\\ndef wilson_ci(successes: int, total: int, z: float = 1.96):\\n    if total == 0:\\n        return 0.0, 0.0, 1.0\\n    p = successes / total\\n    denom = 1 + z ** 2 / total\\n    center = (p + z ** 2 / (2 * total)) / denom\\n    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.22}}"
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
Now I have a good understanding of the code. Let me also look at the relevant parts of the original divergence script more carefully, especially the `obs_to_` function that was truncated, and the `run_divergence_analysis` function. Let me also check the `load_model` function more carefully to understand how wrapper/ACIS is set up.

Let me read the truncated parts of the original script and also the load_model function from eval.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "08a1c227-a471-44f6-bdae-c41096c90ffa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPzif3eLB2AThCymce8M4b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3215,
      "cache_read_input_tokens": 32305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3215
      },
      "output_tokens": 10,
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

Let me read the full eval script's model loading and the truncated parts of the original divergence script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "7af90a86-9b8a-4938-95dc-7cf272ade6fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPzif3eLB2AThCymce8M4b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3215,
      "cache_read_input_tokens": 32305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3215
      },
      "output_tokens": 10,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016EKDb96fr9MrkhR9Z6K5wd`</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -n +100 /root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "fc518b49-c491-48f3-ac7a-85c3eeca9e9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPzif3eLB2AThCymce8M4b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3215,
      "cache_read_input_tokens": 32305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3215
      },
      "output_tokens": 10,
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

_source line 37 · 2026-05-17T10:38:07.540Z_

<details><summary>↩ Tool result · `toolu_016EKDb96fr9MrkhR9Z6K5wd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    return config\\n\\n\\n# --- Model loading ------------------------------------------------------------\\n\\ndef load_model(args, device: torch.device):\\n    \\\"\\\"\\\"Returns (policy, wrapper_or_None, config).\\\"\\\"\\\"\\n    from train import load_smolvla_policy, wrap_with_imm\\n\\n    config = load_config(args.config)\\n    imm_enabled = config.get(\\\"imm\\\", {}).get(\\\"enabled\\\", False)\\n\\n    if not imm_enabled or args.mode == \\\"baseline\\\":\\n        policy = load_smolvla_policy(config, device)\\n        ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)\\n        policy.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n        policy.eval()\\n        return policy, None, config\\n\\n    policy = load_smolvla_policy(config, device)\\n    wrapper = wrap_with_imm(policy, config)\\n    wrapper.to(device)\\n    ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)\\n    wrapper.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    wrapper.eval()\\n    return wrapper.policy, wrapper, config\\n\\n\\n# --- State preprocessing -----------------------------------------------------\\n\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\n    \\\"\\\"\\\"Convert quaternion (x,y,z,w) to axis-angle (3,).\\\"\\\"\\\"\\n    q = quat.astype(np.float64)\\n    w = np.clip(q[3], -1.0, 1.0)\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\n    if den > 1e-10:\\n        angle = 2.0 * np.arccos(w)\\n        axis = q[:3] / den\\n        return (axis * angle).astype(np.float32)\\n    return np.zeros(3, dtype=np.float32)\\n\\n\\ndef extract_state(obs: dict) -> np.ndarray:\\n    \\\"\\\"\\\"Extract 8D state: eef_pos(3) + axis_angle(3) + gripper_qpos(2).\\\"\\\"\\\"\\n    rs = obs[\\\"robot_state\\\"]\\n    eef_pos = np.asarray(rs[\\\"eef\\\"][\\\"pos\\\"], dtype=np.float32)       # (3,)\\n    eef_quat = np.asarray(rs[\\\"eef\\\"][\\\"quat\\\"], dtype=np.float64)     # (4,)\\n    gripper_qpos = np.asarray(rs[\\\"gripper\\\"][\\\"qpos\\\"], dtype=np.float32)  # (2,)\\n    eef_aa = quat_to_axis_angle(eef_quat)                          # (3,)\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])          # (8,)\\n\\n\\n# --- Observation -> batch conversion -----------------------------------------\\n\\ndef obs_to_batch(obs: dict, task_text: str, tokenizer, camera_keys: list, device: torch.device) -> dict:\\n    batch = {}\\n\\n    for cam_key in camera_keys:\\n        short_name = cam_key.split(\\\".\\\")[-1]  # \\\"image\\\" or \\\"image2\\\"\\n        img = obs[\\\"pixels\\\"][short_name]       # (H, W, 3) uint8\\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\\n        img_t = img_t.unsqueeze(0)  # (1, 3, H, W)\\n        # 180 deg flip: flip both H and W dims, matching LiberoProcessorStep\\n        img_t = torch.flip(img_t, dims=[2, 3])\\n        batch[cam_key] = img_t.to(device)\\n\\n    state = extract_state(obs)\\n    batch[\\\"observation.state\\\"] = torch.from_numpy(state).unsqueeze(0).to(device)  # (1, 8)\\n\\n    text = task_text if task_text.endswith(\\\"\\\\n\\\") else task_text + \\\"\\\\n\\\"\\n    encoded = tokenizer(\\n        [text], padding=\\\"longest\\\", max_length=48,\\n        truncation=True, return_tensors=\\\"pt\\\",\\n    )\\n    batch[\\\"observation.language.tokens\\\"] = encoded[\\\"input_ids\\\"].to(device)\\n    batch[\\\"observation.language.attention_mask\\\"] = encoded[\\\"attention_mask\\\"].bool().to(device)\\n\\n    return batch\\n\\n\\n# --- ACIS pruning -------------------------------------------------------------\\n\\ndef find_connector(model):\\n    for name, module in model.named_modules():\\n        if name.endswith(\\\".connector\\\") or \\\"multi_modal_projector\\\" in name:\\n            return module\\n    return None\\n\\n\\n@torch.no_grad()\\ndef compute_acis_mask(wrapper, batch: dict, device: torch.device) -> torch.Tensor:\\n    bm = wrapper.base_model\\n    images, _ = wrapper.policy.prepare_images(batch)\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\n\\n    B = vis_tokens.shape[0]\\n    noise = bm.sample_noise(\\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\\n    )\\n    time = torch.ones(B, device=device)\\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\\n    scores = wrapper.acis(suffix_embs, vis_tokens)\\n\\n    N_vis = vis_tokens.shape[1]\\n\\n... [截断: 输出过长，省略 7502 字符] ...\\n\\n action_chunk is None or action_idx >= args.action_horizon:\\n                    batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\n\\n                    if args.mode == \\\"acis_prune\\\":\\n                        mask = compute_acis_mask(wrapper, batch, device)\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n                        action_chunk = predict_actions(policy, batch)\\n                        hook_handle.remove()\\n                    elif args.mode == \\\"random_prune\\\":\\n                        mask = compute_random_mask(wrapper, batch, device)\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n                        action_chunk = predict_actions(policy, batch)\\n                        hook_handle.remove()\\n                    else:\\n                        action_chunk = predict_actions(policy, batch)\\n\\n                    action_idx = 0\\n\\n                action = action_chunk[action_idx].cpu().numpy().astype(np.float32)\\n                action = np.clip(action, -1.0, 1.0)\\n                action_idx += 1\\n\\n                obs, reward, terminated, truncated, info = env.step(action)\\n\\n                if info.get(\\\"is_success\\\", False):\\n                    success = True\\n                    break\\n\\n                if terminated or truncated:\\n                    break\\n\\n            ep_steps = step + 1\\n            task_successes.append(success)\\n            task_lengths.append(ep_steps)\\n\\n            log.info(\\n                \\\"  Ep %d/%d | %s | steps=%d\\\",\\n                ep + 1, args.num_episodes,\\n                \\\"SUCCESS\\\" if success else \\\"FAIL\\\", ep_steps,\\n            )\\n\\n        env.close()\\n\\n        n_succ = sum(task_successes)\\n        n_total = len(task_successes)\\n        sr = n_succ / n_total if n_total > 0 else 0.0\\n\\n        all_task_results[task_id] = {\\n            \\\"task_id\\\": task_id,\\n            \\\"task_description\\\": task_desc,\\n            \\\"success_count\\\": n_succ,\\n            \\\"total_episodes\\\": n_total,\\n            \\\"success_rate\\\": round(sr, 4),\\n            \\\"mean_steps\\\": round(float(np.mean(task_lengths)), 1),\\n        }\\n        total_successes += n_succ\\n        total_episodes += n_total\\n\\n        log.info(\\\"  Task %d SR: %d/%d (%.1f%%)\\\", task_id, n_succ, n_total, sr * 100)\\n\\n    # Overall\\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\\n\\n    log.info(\\\"=\\\" * 60)\\n    log.info(\\\"SUITE: %s | MODE: %s | PRUNING: %s\\\", args.suite, args.mode, args.pruning_method)\\n    log.info(\\\"Overall SR: %d/%d (%.1f%%)\\\", total_successes, total_episodes, overall_sr * 100)\\n    log.info(\\\"95%% Wilson CI: [%.1f%%, %.1f%%]\\\", ci_lo * 100, ci_hi * 100)\\n\\n    for tid, tr in sorted(all_task_results.items()):\\n        log.info(\\\"  Task %d: %.0f%% (%d/%d) -- %s\\\",\\n                 tid, tr[\\\"success_rate\\\"] * 100, tr[\\\"success_count\\\"],\\n                 tr[\\\"total_episodes\\\"], tr[\\\"task_description\\\"])\\n    log.info(\\\"=\\\" * 60)\\n\\n    summary = {\\n        \\\"suite\\\": args.suite,\\n        \\\"mode\\\": args.mode,\\n        \\\"pruning_method\\\": args.pruning_method,\\n        \\\"checkpoint\\\": args.checkpoint,\\n        \\\"config\\\": args.config,\\n        \\\"total_episodes\\\": total_episodes,\\n        \\\"total_successes\\\": total_successes,\\n        \\\"overall_success_rate\\\": round(overall_sr, 4),\\n        \\\"wilson_ci_95\\\": [round(ci_lo, 4), round(ci_hi, 4)],\\n        \\\"num_episodes_per_task\\\": args.num_episodes,\\n        \\\"max_steps\\\": max_steps,\\n        \\\"action_horizon\\\": args.action_horizon,\\n        \\\"seed\\\": args.seed,\\n        \\\"merge_alpha\\\": args.merge_alpha,\\n        \\\"per_task\\\": all_task_results,\\n    }\\n\\n    output_path.parent.mkdir(parents=True, exist_ok=True)\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(summary, f, indent=2)\\n    log.info(\\\"Results saved to %s\\\", output_path)\\n\\n    return summary\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_evaluation(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.23}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "687027d3-6848-4cfc-99e2-a521c497aaf4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    return config\\\\n\\\\n\\\\n# --- Model loading ------------------------------------------------------------\\\\n\\\\ndef load_model(args, device: torch.device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Returns (policy, wrapper_or_None, config).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    from train import load_smolvla_policy, wrap_with_imm\\\\n\\\\n    config = load_config(args.config)\\\\n    imm_enabled = config.get(\\\\\\\"imm\\\\\\\", {}).get(\\\\\\\"enabled\\\\\\\", False)\\\\n\\\\n    if not imm_enabled or args.mode == \\\\\\\"baseline\\\\\\\":\\\\n        policy = load_smolvla_policy(config, device)\\\\n        ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)\\\\n        policy.load_state_dict(ckpt[\\\\\\\"model_state_dict\\\\\\\"], strict=False)\\\\n        policy.eval()\\\\n        return policy, None, config\\\\n\\\\n    policy = load_smolvla_policy(config, device)\\\\n    wrapper = wrap_with_imm(policy, config)\\\\n    wrapper.to(device)\\\\n    ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)\\\\n    wrapper.load_state_dict(ckpt[\\\\\\\"model_state_dict\\\\\\\"], strict=False)\\\\n    wrapper.eval()\\\\n    return wrapper.policy, wrapper, config\\\\n\\\\n\\\\n# --- State preprocessing -----------------------------------------------------\\\\n\\\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Convert quaternion (x,y,z,w) to axis-angle (3,).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    q = quat.astype(np.float64)\\\\n    w = np.clip(q[3], -1.0, 1.0)\\\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\\\n    if den > 1e-10:\\\\n        angle = 2.0 * np.arccos(w)\\\\n        axis = q[:3] / den\\\\n        return (axis * angle).astype(np.float32)\\\\n    return np.zeros(3, dtype=np.float32)\\\\n\\\\n\\\\ndef extract_state(obs: dict) -> np.ndarray:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Extract 8D state: eef_pos(3) + axis_angle(3) + gripper_qpos(2).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    rs = obs[\\\\\\\"robot_state\\\\\\\"]\\\\n    eef_pos = np.asarray(rs[\\\\\\\"eef\\\\\\\"][\\\\\\\"pos\\\\\\\"], dtype=np.float32)       # (3,)\\\\n    eef_quat = np.asarray(rs[\\\\\\\"eef\\\\\\\"][\\\\\\\"quat\\\\\\\"], dtype=np.float64)     # (4,)\\\\n    gripper_qpos = np.asarray(rs[\\\\\\\"gripper\\\\\\\"][\\\\\\\"qpos\\\\\\\"], dtype=np.float32)  # (2,)\\\\n    eef_aa = quat_to_axis_angle(eef_quat)                          # (3,)\\\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])          # (8,)\\\\n\\\\n\\\\n# --- Observation -> batch conversion -----------------------------------------\\\\n\\\\ndef obs_to_batch(obs: dict, task_text: str, tokenizer, camera_keys: list, device: torch.device) -> dict:\\\\n    batch = {}\\\\n\\\\n    for cam_key in camera_keys:\\\\n        short_name = cam_key.split(\\\\\\\".\\\\\\\")[-1]  # \\\\\\\"image\\\\\\\" or \\\\\\\"image2\\\\\\\"\\\\n        img = obs[\\\\\\\"pixels\\\\\\\"][short_name]       # (H, W, 3) uint8\\\\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\\\\n        img_t = img_t.unsqueeze(0)  # (1, 3, H, W)\\\\n        # 180 deg flip: flip both H and W dims, matching LiberoProcessorStep\\\\n        img_t = torch.flip(img_t, dims=[2, 3])\\\\n        batch[cam_key] = img_t.to(device)\\\\n\\\\n    state = extract_state(obs)\\\\n    batch[\\\\\\\"observation.state\\\\\\\"] = torch.from_numpy(state).unsqueeze(0).to(device)  # (1, 8)\\\\n\\\\n    text = task_text if task_text.endswith(\\\\\\\"\\\\\\\\n\\\\\\\") else task_text + \\\\\\\"\\\\\\\\n\\\\\\\"\\\\n    encoded = tokenizer(\\\\n        [text], padding=\\\\\\\"longest\\\\\\\", max_length=48,\\\\n        truncation=True, return_tensors=\\\\\\\"pt\\\\\\\",\\\\n    )\\\\n    batch[\\\\\\\"observation.language.tokens\\\\\\\"] = encoded[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n    batch[\\\\\\\"observation.language.attention_mask\\\\\\\"] = encoded[\\\\\\\"attention_mask\\\\\\\"].bool().to(device)\\\\n\\\\n    return batch\\\\n\\\\n\\\\n# --- ACIS pruning -------------------------------------------------------------\\\\n\\\\ndef find_connector(model):\\\\n    for name, module in model.named_modules():\\\\n        if name.endswith(\\\\\\\".connector\\\\\\\") or \\\\\\\"multi_modal_projector\\\\\\\" in name:\\\\n            return module\\\\n    return None\\\\n\\\\n\\\\n@torch.no_grad()\\\\ndef compute_acis_mask(wrapper, batch: dict, device: torch.device) -> torch.Tensor:\\\\n    bm = wrapper.base_model\\\\n    images, _ = wrapper.policy.prepare_images(batch)\\\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\\\n\\\\n    B = vis_tokens.shape[0]\\\\n    noise = bm.sample_noise(\\\\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\\\\n    )\\\\n    time = torch.ones(B, device=device)\\\\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\\\\n    scores = wrapper.acis(suffix_embs, vis_tokens)\\\\n\\\\n    N_vis = vis_tokens.shape[1]\\\\n\\\\n... [截断: 输出过长，省略 7502 字符] ...\\\\n\\\\n action_chunk is None or action_idx >= args.action_horizon:\\\\n                    batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\\\n\\\\n                    if args.mode == \\\\\\\"acis_prune\\\\\\\":\\\\n                        mask = compute_acis_mask(wrapper, batch, device)\\\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\\\n                        action_chunk = predict_actions(policy, batch)\\\\n                        hook_handle.remove()\\\\n                    elif args.mode == \\\\\\\"random_prune\\\\\\\":\\\\n                        mask = compute_random_mask(wrapper, batch, device)\\\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\\\n                        action_chunk = predict_actions(policy, batch)\\\\n                        hook_handle.remove()\\\\n                    else:\\\\n                        action_chunk = predict_actions(policy, batch)\\\\n\\\\n                    action_idx = 0\\\\n\\\\n                action = action_chunk[action_idx].cpu().numpy().astype(np.float32)\\\\n                action = np.clip(action, -1.0, 1.0)\\\\n                action_idx += 1\\\\n\\\\n                obs, reward, terminated, truncated, info = env.step(action)\\\\n\\\\n                if info.get(\\\\\\\"is_success\\\\\\\", False):\\\\n                    success = True\\\\n                    break\\\\n\\\\n                if terminated or truncated:\\\\n                    break\\\\n\\\\n            ep_steps = step + 1\\\\n            task_successes.append(success)\\\\n            task_lengths.append(ep_steps)\\\\n\\\\n            log.info(\\\\n                \\\\\\\"  Ep %d/%d | %s | steps=%d\\\\\\\",\\\\n                ep + 1, args.num_episodes,\\\\n                \\\\\\\"SUCCESS\\\\\\\" if success else \\\\\\\"FAIL\\\\\\\", ep_steps,\\\\n            )\\\\n\\\\n        env.close()\\\\n\\\\n        n_succ = sum(task_successes)\\\\n        n_total = len(task_successes)\\\\n        sr = n_succ / n_total if n_total > 0 else 0.0\\\\n\\\\n        all_task_results[task_id] = {\\\\n            \\\\\\\"task_id\\\\\\\": task_id,\\\\n            \\\\\\\"task_description\\\\\\\": task_desc,\\\\n            \\\\\\\"success_count\\\\\\\": n_succ,\\\\n            \\\\\\\"total_episodes\\\\\\\": n_total,\\\\n            \\\\\\\"success_rate\\\\\\\": round(sr, 4),\\\\n            \\\\\\\"mean_steps\\\\\\\": round(float(np.mean(task_lengths)), 1),\\\\n        }\\\\n        total_successes += n_succ\\\\n        total_episodes += n_total\\\\n\\\\n        log.info(\\\\\\\"  Task %d SR: %d/%d (%.1f%%)\\\\\\\", task_id, n_succ, n_total, sr * 100)\\\\n\\\\n    # Overall\\\\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\\\\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\\\\n\\\\n    log.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    log.info(\\\\\\\"SUITE: %s | MODE: %s | PRUNING: %s\\\\\\\", args.suite, args.mode, args.pruning_method)\\\\n    log.info(\\\\\\\"Overall SR: %d/%d (%.1f%%)\\\\\\\", total_successes, total_episodes, overall_sr * 100)\\\\n    log.info(\\\\\\\"95%% Wilson CI: [%.1f%%, %.1f%%]\\\\\\\", ci_lo * 100, ci_hi * 100)\\\\n\\\\n    for tid, tr in sorted(all_task_results.items()):\\\\n        log.info(\\\\\\\"  Task %d: %.0f%% (%d/%d) -- %s\\\\\\\",\\\\n                 tid, tr[\\\\\\\"success_rate\\\\\\\"] * 100, tr[\\\\\\\"success_count\\\\\\\"],\\\\n                 tr[\\\\\\\"total_episodes\\\\\\\"], tr[\\\\\\\"task_description\\\\\\\"])\\\\n    log.info(\\\\\\\"=\\\\\\\" * 60)\\\\n\\\\n    summary = {\\\\n        \\\\\\\"suite\\\\\\\": args.suite,\\\\n        \\\\\\\"mode\\\\\\\": args.mode,\\\\n        \\\\\\\"pruning_method\\\\\\\": args.pruning_method,\\\\n        \\\\\\\"checkpoint\\\\\\\": args.checkpoint,\\\\n        \\\\\\\"config\\\\\\\": args.config,\\\\n        \\\\\\\"total_episodes\\\\\\\": total_episodes,\\\\n        \\\\\\\"total_successes\\\\\\\": total_successes,\\\\n        \\\\\\\"overall_success_rate\\\\\\\": round(overall_sr, 4),\\\\n        \\\\\\\"wilson_ci_95\\\\\\\": [round(ci_lo, 4), round(ci_hi, 4)],\\\\n        \\\\\\\"num_episodes_per_task\\\\\\\": args.num_episodes,\\\\n        \\\\\\\"max_steps\\\\\\\": max_steps,\\\\n        \\\\\\\"action_horizon\\\\\\\": args.action_horizon,\\\\n        \\\\\\\"seed\\\\\\\": args.seed,\\\\n        \\\\\\\"merge_alpha\\\\\\\": args.merge_alpha,\\\\n        \\\\\\\"per_task\\\\\\\": all_task_results,\\\\n    }\\\\n\\\\n    output_path.parent.mkdir(parents=True, exist_ok=True)\\\\n    with open(output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(summary, f, indent=2)\\\\n    log.info(\\\\\\\"Results saved to %s\\\\\\\", output_path)\\\\n\\\\n    return summary\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    args = parse_args()\\\\n    run_evaluation(args)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.23}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    return config\\n\\n\\n# --- Model loading ------------------------------------------------------------\\n\\ndef load_model(args, device: torch.device):\\n    \\\"\\\"\\\"Returns (policy, wrapper_or_None, config).\\\"\\\"\\\"\\n    from train import load_smolvla_policy, wrap_with_imm\\n\\n    config = load_config(args.config)\\n    imm_enabled = config.get(\\\"imm\\\", {}).get(\\\"enabled\\\", False)\\n\\n    if not imm_enabled or args.mode == \\\"baseline\\\":\\n        policy = load_smolvla_policy(config, device)\\n        ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)\\n        policy.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n        policy.eval()\\n        return policy, None, config\\n\\n    policy = load_smolvla_policy(config, device)\\n    wrapper = wrap_with_imm(policy, config)\\n    wrapper.to(device)\\n    ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)\\n    wrapper.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    wrapper.eval()\\n    return wrapper.policy, wrapper, config\\n\\n\\n# --- State preprocessing -----------------------------------------------------\\n\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\n    \\\"\\\"\\\"Convert quaternion (x,y,z,w) to axis-angle (3,).\\\"\\\"\\\"\\n    q = quat.astype(np.float64)\\n    w = np.clip(q[3], -1.0, 1.0)\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\n    if den > 1e-10:\\n        angle = 2.0 * np.arccos(w)\\n        axis = q[:3] / den\\n        return (axis * angle).astype(np.float32)\\n    return np.zeros(3, dtype=np.float32)\\n\\n\\ndef extract_state(obs: dict) -> np.ndarray:\\n    \\\"\\\"\\\"Extract 8D state: eef_pos(3) + axis_angle(3) + gripper_qpos(2).\\\"\\\"\\\"\\n    rs = obs[\\\"robot_state\\\"]\\n    eef_pos = np.asarray(rs[\\\"eef\\\"][\\\"pos\\\"], dtype=np.float32)       # (3,)\\n    eef_quat = np.asarray(rs[\\\"eef\\\"][\\\"quat\\\"], dtype=np.float64)     # (4,)\\n    gripper_qpos = np.asarray(rs[\\\"gripper\\\"][\\\"qpos\\\"], dtype=np.float32)  # (2,)\\n    eef_aa = quat_to_axis_angle(eef_quat)                          # (3,)\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])          # (8,)\\n\\n\\n# --- Observation -> batch conversion -----------------------------------------\\n\\ndef obs_to_batch(obs: dict, task_text: str, tokenizer, camera_keys: list, device: torch.device) -> dict:\\n    batch = {}\\n\\n    for cam_key in camera_keys:\\n        short_name = cam_key.split(\\\".\\\")[-1]  # \\\"image\\\" or \\\"image2\\\"\\n        img = obs[\\\"pixels\\\"][short_name]       # (H, W, 3) uint8\\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\\n        img_t = img_t.unsqueeze(0)  # (1, 3, H, W)\\n        # 180 deg flip: flip both H and W dims, matching LiberoProcessorStep\\n        img_t = torch.flip(img_t, dims=[2, 3])\\n        batch[cam_key] = img_t.to(device)\\n\\n    state = extract_state(obs)\\n    batch[\\\"observation.state\\\"] = torch.from_numpy(state).unsqueeze(0).to(device)  # (1, 8)\\n\\n    text = task_text if task_text.endswith(\\\"\\\\n\\\") else task_text + \\\"\\\\n\\\"\\n    encoded = tokenizer(\\n        [text], padding=\\\"longest\\\", max_length=48,\\n        truncation=True, return_tensors=\\\"pt\\\",\\n    )\\n    batch[\\\"observation.language.tokens\\\"] = encoded[\\\"input_ids\\\"].to(device)\\n    batch[\\\"observation.language.attention_mask\\\"] = encoded[\\\"attention_mask\\\"].bool().to(device)\\n\\n    return batch\\n\\n\\n# --- ACIS pruning -------------------------------------------------------------\\n\\ndef find_connector(model):\\n    for name, module in model.named_modules():\\n        if name.endswith(\\\".connector\\\") or \\\"multi_modal_projector\\\" in name:\\n            return module\\n    return None\\n\\n\\n@torch.no_grad()\\ndef compute_acis_mask(wrapper, batch: dict, device: torch.device) -> torch.Tensor:\\n    bm = wrapper.base_model\\n    images, _ = wrapper.policy.prepare_images(batch)\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\n\\n    B = vis_tokens.shape[0]\\n    noise = bm.sample_noise(\\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\\n    )\\n    time = torch.ones(B, device=device)\\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\\n    scores = wrapper.acis(suffix_embs, vis_tokens)\\n\\n    N_vis = vis_tokens.shape[1]\\n\\n... [截断: 输出过长，省略 7502 字符] ...\\n\\n action_chunk is None or action_idx >= args.action_horizon:\\n                    batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\n\\n                    if args.mode == \\\"acis_prune\\\":\\n                        mask = compute_acis_mask(wrapper, batch, device)\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n                        action_chunk = predict_actions(policy, batch)\\n                        hook_handle.remove()\\n                    elif args.mode == \\\"random_prune\\\":\\n                        mask = compute_random_mask(wrapper, batch, device)\\n                        hook_handle = register_acis_hook(connector, mask, method=args.pruning_method, merge_alpha=args.merge_alpha)\\n                        action_chunk = predict_actions(policy, batch)\\n                        hook_handle.remove()\\n                    else:\\n                        action_chunk = predict_actions(policy, batch)\\n\\n                    action_idx = 0\\n\\n                action = action_chunk[action_idx].cpu().numpy().astype(np.float32)\\n                action = np.clip(action, -1.0, 1.0)\\n                action_idx += 1\\n\\n                obs, reward, terminated, truncated, info = env.step(action)\\n\\n                if info.get(\\\"is_success\\\", False):\\n                    success = True\\n                    break\\n\\n                if terminated or truncated:\\n                    break\\n\\n            ep_steps = step + 1\\n            task_successes.append(success)\\n            task_lengths.append(ep_steps)\\n\\n            log.info(\\n                \\\"  Ep %d/%d | %s | steps=%d\\\",\\n                ep + 1, args.num_episodes,\\n                \\\"SUCCESS\\\" if success else \\\"FAIL\\\", ep_steps,\\n            )\\n\\n        env.close()\\n\\n        n_succ = sum(task_successes)\\n        n_total = len(task_successes)\\n        sr = n_succ / n_total if n_total > 0 else 0.0\\n\\n        all_task_results[task_id] = {\\n            \\\"task_id\\\": task_id,\\n            \\\"task_description\\\": task_desc,\\n            \\\"success_count\\\": n_succ,\\n            \\\"total_episodes\\\": n_total,\\n            \\\"success_rate\\\": round(sr, 4),\\n            \\\"mean_steps\\\": round(float(np.mean(task_lengths)), 1),\\n        }\\n        total_successes += n_succ\\n        total_episodes += n_total\\n\\n        log.info(\\\"  Task %d SR: %d/%d (%.1f%%)\\\", task_id, n_succ, n_total, sr * 100)\\n\\n    # Overall\\n    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0\\n    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)\\n\\n    log.info(\\\"=\\\" * 60)\\n    log.info(\\\"SUITE: %s | MODE: %s | PRUNING: %s\\\", args.suite, args.mode, args.pruning_method)\\n    log.info(\\\"Overall SR: %d/%d (%.1f%%)\\\", total_successes, total_episodes, overall_sr * 100)\\n    log.info(\\\"95%% Wilson CI: [%.1f%%, %.1f%%]\\\", ci_lo * 100, ci_hi * 100)\\n\\n    for tid, tr in sorted(all_task_results.items()):\\n        log.info(\\\"  Task %d: %.0f%% (%d/%d) -- %s\\\",\\n                 tid, tr[\\\"success_rate\\\"] * 100, tr[\\\"success_count\\\"],\\n                 tr[\\\"total_episodes\\\"], tr[\\\"task_description\\\"])\\n    log.info(\\\"=\\\" * 60)\\n\\n    summary = {\\n        \\\"suite\\\": args.suite,\\n        \\\"mode\\\": args.mode,\\n        \\\"pruning_method\\\": args.pruning_method,\\n        \\\"checkpoint\\\": args.checkpoint,\\n        \\\"config\\\": args.config,\\n        \\\"total_episodes\\\": total_episodes,\\n        \\\"total_successes\\\": total_successes,\\n        \\\"overall_success_rate\\\": round(overall_sr, 4),\\n        \\\"wilson_ci_95\\\": [round(ci_lo, 4), round(ci_hi, 4)],\\n        \\\"num_episodes_per_task\\\": args.num_episodes,\\n        \\\"max_steps\\\": max_steps,\\n        \\\"action_horizon\\\": args.action_horizon,\\n        \\\"seed\\\": args.seed,\\n        \\\"merge_alpha\\\": args.merge_alpha,\\n        \\\"per_task\\\": all_task_results,\\n    }\\n\\n    output_path.parent.mkdir(parents=True, exist_ok=True)\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(summary, f, indent=2)\\n    log.info(\\\"Results saved to %s\\\", output_path)\\n\\n    return summary\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_evaluation(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.23}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also read the full divergence script to get the truncated parts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "1154e939-b7da-4765-a81f-a2574eb5d8da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SQKuZu3byvBKAfzcgnXu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 35520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3506
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

_source line 39_

Now let me get the truncated middle section of the original divergence script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "3d1602b8-121d-497e-90d6-4e56f5f1500b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SQKuZu3byvBKAfzcgnXu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 35520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3506
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

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NZMh1iymep1DmmEvYXCvVZ`</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -n +100 /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "98d0c6a5-accf-4d28-bc41-4c6cc94e71d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SQKuZu3byvBKAfzcgnXu6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 35520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3506
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

_source line 41 · 2026-05-17T10:38:14.676Z_

<details><summary>↩ Tool result · `toolu_01NZMh1iymep1DmmEvYXCvVZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    wrapper.eval()\\n    return wrapper.policy, wrapper, config\\n\\n\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\n\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\n    q = quat.astype(np.float64)\\n    w = np.clip(q[3], -1.0, 1.0)\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\n    if den > 1e-10:\\n        angle = 2.0 * np.arccos(w)\\n        axis = q[:3] / den\\n        return (axis * angle).astype(np.float32)\\n    return np.zeros(3, dtype=np.float32)\\n\\n\\ndef extract_state(obs: dict) -> np.ndarray:\\n    rs = obs[\\\"robot_state\\\"]\\n    eef_pos = np.asarray(rs[\\\"eef\\\"][\\\"pos\\\"], dtype=np.float32)\\n    eef_quat = np.asarray(rs[\\\"eef\\\"][\\\"quat\\\"], dtype=np.float64)\\n    gripper_qpos = np.asarray(rs[\\\"gripper\\\"][\\\"qpos\\\"], dtype=np.float32)\\n    eef_aa = quat_to_axis_angle(eef_quat)\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\n\\n\\ndef obs_to_batch(obs, task_text, tokenizer, camera_keys, device):\\n    batch = {}\\n    for cam_key in camera_keys:\\n        short_name = cam_key.split(\\\".\\\")[-1]\\n        img = obs[\\\"pixels\\\"][short_name]\\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\\n        img_t = img_t.unsqueeze(0)\\n        img_t = torch.flip(img_t, dims=[2, 3])\\n        batch[cam_key] = img_t.to(device)\\n    state = extract_state(obs)\\n    batch[\\\"observation.state\\\"] = torch.from_numpy(state).unsqueeze(0).to(device)\\n    text = task_text if task_text.endswith(\\\"\\\\n\\\") else task_text + \\\"\\\\n\\\"\\n    encoded = tokenizer(\\n        [text], padding=\\\"longest\\\", max_length=48, truncation=True, return_tensors=\\\"pt\\\",\\n    )\\n    batch[\\\"observation.language.tokens\\\"] = encoded[\\\"input_ids\\\"].to(device)\\n    batch[\\\"observation.language.attention_mask\\\"] = encoded[\\\"attention_mask\\\"].bool().to(device)\\n    return batch\\n\\n\\ndef find_connector(model):\\n    for name, module in model.named_modules():\\n        if name.endswith(\\\".connector\\\") or \\\"multi_modal_projector\\\" in name:\\n            return module\\n    return None\\n\\n\\n@torch.no_grad()\\ndef compute_acis_mask(wrapper, batch, device):\\n    bm = wrapper.base_model\\n    images, _ = wrapper.policy.prepare_images(batch)\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\n    B = vis_tokens.shape[0]\\n    noise = bm.sample_noise(\\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\\n    )\\n    time = torch.ones(B, device=device)\\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\\n    scores = wrapper.acis(suffix_embs, vis_tokens)\\n    N_vis = vis_tokens.shape[1]\\n    k = max(1, int(N_vis * wrapper.k_ratio))\\n    _, topk_idx = torch.topk(scores, k, dim=-1)\\n    mask = torch.zeros(B, N_vis, device=device)\\n    mask.scatter_(1, topk_idx, 1.0)\\n    return mask\\n\\n\\ndef register_acis_hook(connector, mask):\\n    def hook_fn(module, input, output):\\n        tokens = output[0] if isinstance(output, tuple) else output\\n        if tokens.dim() != 3 or tokens.shape[1] != mask.shape[1]:\\n            return output\\n        masked = tokens * mask[:tokens.shape[0]].unsqueeze(-1)\\n        if isinstance(output, tuple):\\n            return (masked,) + output[1:]\\n        return masked\\n    return connector.register_forward_hook(hook_fn)\\n\\n\\n@torch.no_grad()\\ndef predict_actions(policy, batch):\\n    images, img_masks = policy.prepare_images(batch)\\n    state = policy.prepare_state(batch)\\n    lang_tokens = batch[\\\"observation.language.tokens\\\"]\\n    lang_masks = batch[\\\"observation.language.attention_mask\\\"]\\n    actions = policy.model.sample_actions(\\n        images, img_masks, lang_tokens, lang_masks, state\\n    )\\n    original_action_dim = policy.config.action_feature.shape[0]\\n    return actions[0, :, :original_action_dim]\\n\\n\\ndef run_divergence_analysis(args):\\n    device = torch.device(f\\\"cuda:{args.gpu}\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    task_ids = [int(x) for x in args.task_ids.split(\\\",\\\")]\\n    output_dir = Path(args.output_dir)\\n    output_dir.mkdir(parents=True, exist_ok=True)\\n\\n    np.random.seed(args.seed)\\n    torch.manual_seed(args.seed)\\n\\n    log.info(\\\"Loading baseline model...\\\")\\n    baseline_policy, baseline_config = load_b\\n\\n... [截断: 输出过长，省略 6496 字符] ...\\n\\n: Path):\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\n\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\n    ax = axes[0]\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\n    task_ids = sorted(all_results.keys())\\n\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        for ep_data in episodes:\\n            steps = ep_data[\\\"timesteps\\\"]\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in steps]\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\n\\n    mean_curve = analysis[\\\"mean_l2_curve\\\"]\\n    std_curve = analysis[\\\"std_l2_curve\\\"]\\n    x = np.arange(len(mean_curve))\\n    ax.plot(x, mean_curve, color=\\\"black\\\", linewidth=2, label=\\\"Mean\\\")\\n    mean_arr = np.array(mean_curve)\\n    std_arr = np.array(std_curve)\\n    valid = ~np.isnan(mean_arr)\\n    ax.fill_between(\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\n        alpha=0.15, color=\\\"black\\\"\\n    )\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Baseline vs ACIS k=0.7: Action Divergence\\\")\\n    ax.legend(loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    # Plot 2: Per-dimension breakdown\\n    ax = axes[1]\\n    dim_data = analysis[\\\"per_dim_mean_abs_diff\\\"]\\n    names = list(dim_data.keys())\\n    values = list(dim_data.values())\\n    bar_colors = [\\\"#2196F3\\\"] * 3 + [\\\"#FF9800\\\"] * 3 + [\\\"#4CAF50\\\"]\\n    ax.bar(names, values, color=bar_colors)\\n    ax.set_xlabel(\\\"Action Dimension\\\")\\n    ax.set_ylabel(\\\"Mean |Difference|\\\")\\n    ax.set_title(\\\"Per-Dimension Divergence\\\")\\n    ax.set_xticklabels(names, rotation=45, ha=\\\"right\\\")\\n    ax.grid(True, alpha=0.3, axis=\\\"y\\\")\\n\\n    # Plot 3: Per-task mean curves\\n    ax = axes[2]\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        task_l2s = []\\n        for ep_data in episodes:\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in ep_data[\\\"timesteps\\\"]]\\n            task_l2s.append(l2_vals)\\n        max_t = max(len(c) for c in task_l2s)\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\n        for i, c in enumerate(task_l2s):\\n            padded[i, :len(c)] = c\\n        task_mean = np.nanmean(padded, axis=0)\\n        task_desc = episodes[0][\\\"task_desc\\\"]\\n        short_desc = task_desc[:30] + \\\"...\\\" if len(task_desc) > 30 else task_desc\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\"T{task_id}: {short_desc}\\\", color=colors[ti % 10])\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Per-Task Mean Divergence\\\")\\n    ax.legend(fontsize=7, loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    plt.tight_layout()\\n    pdf_path = output_dir / \\\"action_divergence_curve.pdf\\\"\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.savefig(output_dir / \\\"action_divergence_curve.png\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    log.info(\\\"Plots saved to %s\\\", pdf_path)\\n\\n    # Summary stats figure\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\n    ax2.axis(\\\"off\\\")\\n    summary_text = (\\n        f\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\n\\\"\\n        f\\\"{'='*50}\\\\n\\\"\\n        f\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\n\\\"\\n        f\\\"Num episodes:           {analysis['num_episodes']}\\\\n\\\"\\n        f\\\"Max episode length:     {analysis['max_episode_length']}\\\\n\\\"\\n        f\\\"\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\n\\\"\\n        f\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\n\\\"\\n    )\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\n             verticalalignment=\\\"top\\\", fontfamily=\\\"monospace\\\")\\n    plt.tight_layout()\\n    plt.savefig(output_dir / \\\"action_divergence_summary.pdf\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_divergence_analysis(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.04}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "b3bbb137-d4f0-48dc-be23-637b1a91df05",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    wrapper.eval()\\\\n    return wrapper.policy, wrapper, config\\\\n\\\\n\\\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\\\n\\\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\\\n    q = quat.astype(np.float64)\\\\n    w = np.clip(q[3], -1.0, 1.0)\\\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\\\n    if den > 1e-10:\\\\n        angle = 2.0 * np.arccos(w)\\\\n        axis = q[:3] / den\\\\n        return (axis * angle).astype(np.float32)\\\\n    return np.zeros(3, dtype=np.float32)\\\\n\\\\n\\\\ndef extract_state(obs: dict) -> np.ndarray:\\\\n    rs = obs[\\\\\\\"robot_state\\\\\\\"]\\\\n    eef_pos = np.asarray(rs[\\\\\\\"eef\\\\\\\"][\\\\\\\"pos\\\\\\\"], dtype=np.float32)\\\\n    eef_quat = np.asarray(rs[\\\\\\\"eef\\\\\\\"][\\\\\\\"quat\\\\\\\"], dtype=np.float64)\\\\n    gripper_qpos = np.asarray(rs[\\\\\\\"gripper\\\\\\\"][\\\\\\\"qpos\\\\\\\"], dtype=np.float32)\\\\n    eef_aa = quat_to_axis_angle(eef_quat)\\\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\\\n\\\\n\\\\ndef obs_to_batch(obs, task_text, tokenizer, camera_keys, device):\\\\n    batch = {}\\\\n    for cam_key in camera_keys:\\\\n        short_name = cam_key.split(\\\\\\\".\\\\\\\")[-1]\\\\n        img = obs[\\\\\\\"pixels\\\\\\\"][short_name]\\\\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\\\\n        img_t = img_t.unsqueeze(0)\\\\n        img_t = torch.flip(img_t, dims=[2, 3])\\\\n        batch[cam_key] = img_t.to(device)\\\\n    state = extract_state(obs)\\\\n    batch[\\\\\\\"observation.state\\\\\\\"] = torch.from_numpy(state).unsqueeze(0).to(device)\\\\n    text = task_text if task_text.endswith(\\\\\\\"\\\\\\\\n\\\\\\\") else task_text + \\\\\\\"\\\\\\\\n\\\\\\\"\\\\n    encoded = tokenizer(\\\\n        [text], padding=\\\\\\\"longest\\\\\\\", max_length=48, truncation=True, return_tensors=\\\\\\\"pt\\\\\\\",\\\\n    )\\\\n    batch[\\\\\\\"observation.language.tokens\\\\\\\"] = encoded[\\\\\\\"input_ids\\\\\\\"].to(device)\\\\n    batch[\\\\\\\"observation.language.attention_mask\\\\\\\"] = encoded[\\\\\\\"attention_mask\\\\\\\"].bool().to(device)\\\\n    return batch\\\\n\\\\n\\\\ndef find_connector(model):\\\\n    for name, module in model.named_modules():\\\\n        if name.endswith(\\\\\\\".connector\\\\\\\") or \\\\\\\"multi_modal_projector\\\\\\\" in name:\\\\n            return module\\\\n    return None\\\\n\\\\n\\\\n@torch.no_grad()\\\\ndef compute_acis_mask(wrapper, batch, device):\\\\n    bm = wrapper.base_model\\\\n    images, _ = wrapper.policy.prepare_images(batch)\\\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\\\n    B = vis_tokens.shape[0]\\\\n    noise = bm.sample_noise(\\\\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\\\\n    )\\\\n    time = torch.ones(B, device=device)\\\\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\\\\n    scores = wrapper.acis(suffix_embs, vis_tokens)\\\\n    N_vis = vis_tokens.shape[1]\\\\n    k = max(1, int(N_vis * wrapper.k_ratio))\\\\n    _, topk_idx = torch.topk(scores, k, dim=-1)\\\\n    mask = torch.zeros(B, N_vis, device=device)\\\\n    mask.scatter_(1, topk_idx, 1.0)\\\\n    return mask\\\\n\\\\n\\\\ndef register_acis_hook(connector, mask):\\\\n    def hook_fn(module, input, output):\\\\n        tokens = output[0] if isinstance(output, tuple) else output\\\\n        if tokens.dim() != 3 or tokens.shape[1] != mask.shape[1]:\\\\n            return output\\\\n        masked = tokens * mask[:tokens.shape[0]].unsqueeze(-1)\\\\n        if isinstance(output, tuple):\\\\n            return (masked,) + output[1:]\\\\n        return masked\\\\n    return connector.register_forward_hook(hook_fn)\\\\n\\\\n\\\\n@torch.no_grad()\\\\ndef predict_actions(policy, batch):\\\\n    images, img_masks = policy.prepare_images(batch)\\\\n    state = policy.prepare_state(batch)\\\\n    lang_tokens = batch[\\\\\\\"observation.language.tokens\\\\\\\"]\\\\n    lang_masks = batch[\\\\\\\"observation.language.attention_mask\\\\\\\"]\\\\n    actions = policy.model.sample_actions(\\\\n        images, img_masks, lang_tokens, lang_masks, state\\\\n    )\\\\n    original_action_dim = policy.config.action_feature.shape[0]\\\\n    return actions[0, :, :original_action_dim]\\\\n\\\\n\\\\ndef run_divergence_analysis(args):\\\\n    device = torch.device(f\\\\\\\"cuda:{args.gpu}\\\\\\\" if torch.cuda.is_available() else \\\\\\\"cpu\\\\\\\")\\\\n    task_ids = [int(x) for x in args.task_ids.split(\\\\\\\",\\\\\\\")]\\\\n    output_dir = Path(args.output_dir)\\\\n    output_dir.mkdir(parents=True, exist_ok=True)\\\\n\\\\n    np.random.seed(args.seed)\\\\n    torch.manual_seed(args.seed)\\\\n\\\\n    log.info(\\\\\\\"Loading baseline model...\\\\\\\")\\\\n    baseline_policy, baseline_config = load_b\\\\n\\\\n... [截断: 输出过长，省略 6496 字符] ...\\\\n\\\\n: Path):\\\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\\\n\\\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\\\n    ax = axes[0]\\\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\\\n    task_ids = sorted(all_results.keys())\\\\n\\\\n    for ti, task_id in enumerate(task_ids):\\\\n        episodes = all_results[task_id]\\\\n        for ep_data in episodes:\\\\n            steps = ep_data[\\\\\\\"timesteps\\\\\\\"]\\\\n            l2_vals = [s[\\\\\\\"l2_distance\\\\\\\"] for s in steps]\\\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\\\n\\\\n    mean_curve = analysis[\\\\\\\"mean_l2_curve\\\\\\\"]\\\\n    std_curve = analysis[\\\\\\\"std_l2_curve\\\\\\\"]\\\\n    x = np.arange(len(mean_curve))\\\\n    ax.plot(x, mean_curve, color=\\\\\\\"black\\\\\\\", linewidth=2, label=\\\\\\\"Mean\\\\\\\")\\\\n    mean_arr = np.array(mean_curve)\\\\n    std_arr = np.array(std_curve)\\\\n    valid = ~np.isnan(mean_arr)\\\\n    ax.fill_between(\\\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\\\n        alpha=0.15, color=\\\\\\\"black\\\\\\\"\\\\n    )\\\\n    ax.set_xlabel(\\\\\\\"Timestep\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"L2 Action Distance\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Baseline vs ACIS k=0.7: Action Divergence\\\\\\\")\\\\n    ax.legend(loc=\\\\\\\"upper left\\\\\\\")\\\\n    ax.grid(True, alpha=0.3)\\\\n\\\\n    # Plot 2: Per-dimension breakdown\\\\n    ax = axes[1]\\\\n    dim_data = analysis[\\\\\\\"per_dim_mean_abs_diff\\\\\\\"]\\\\n    names = list(dim_data.keys())\\\\n    values = list(dim_data.values())\\\\n    bar_colors = [\\\\\\\"#2196F3\\\\\\\"] * 3 + [\\\\\\\"#FF9800\\\\\\\"] * 3 + [\\\\\\\"#4CAF50\\\\\\\"]\\\\n    ax.bar(names, values, color=bar_colors)\\\\n    ax.set_xlabel(\\\\\\\"Action Dimension\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"Mean |Difference|\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Per-Dimension Divergence\\\\\\\")\\\\n    ax.set_xticklabels(names, rotation=45, ha=\\\\\\\"right\\\\\\\")\\\\n    ax.grid(True, alpha=0.3, axis=\\\\\\\"y\\\\\\\")\\\\n\\\\n    # Plot 3: Per-task mean curves\\\\n    ax = axes[2]\\\\n    for ti, task_id in enumerate(task_ids):\\\\n        episodes = all_results[task_id]\\\\n        task_l2s = []\\\\n        for ep_data in episodes:\\\\n            l2_vals = [s[\\\\\\\"l2_distance\\\\\\\"] for s in ep_data[\\\\\\\"timesteps\\\\\\\"]]\\\\n            task_l2s.append(l2_vals)\\\\n        max_t = max(len(c) for c in task_l2s)\\\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\\\n        for i, c in enumerate(task_l2s):\\\\n            padded[i, :len(c)] = c\\\\n        task_mean = np.nanmean(padded, axis=0)\\\\n        task_desc = episodes[0][\\\\\\\"task_desc\\\\\\\"]\\\\n        short_desc = task_desc[:30] + \\\\\\\"...\\\\\\\" if len(task_desc) > 30 else task_desc\\\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\\\\\"T{task_id}: {short_desc}\\\\\\\", color=colors[ti % 10])\\\\n    ax.set_xlabel(\\\\\\\"Timestep\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"L2 Action Distance\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Per-Task Mean Divergence\\\\\\\")\\\\n    ax.legend(fontsize=7, loc=\\\\\\\"upper left\\\\\\\")\\\\n    ax.grid(True, alpha=0.3)\\\\n\\\\n    plt.tight_layout()\\\\n    pdf_path = output_dir / \\\\\\\"action_divergence_curve.pdf\\\\\\\"\\\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.savefig(output_dir / \\\\\\\"action_divergence_curve.png\\\\\\\", dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n    log.info(\\\\\\\"Plots saved to %s\\\\\\\", pdf_path)\\\\n\\\\n    # Summary stats figure\\\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\\\n    ax2.axis(\\\\\\\"off\\\\\\\")\\\\n    summary_text = (\\\\n        f\\\\\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"{'='*50}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Num episodes:           {analysis['num_episodes']}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Max episode length:     {analysis['max_episode_length']}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"\\\\\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\\\\\n\\\\\\\"\\\\n    )\\\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\\\n             verticalalignment=\\\\\\\"top\\\\\\\", fontfamily=\\\\\\\"monospace\\\\\\\")\\\\n    plt.tight_layout()\\\\n    plt.savefig(output_dir / \\\\\\\"action_divergence_summary.pdf\\\\\\\", dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    args = parse_args()\\\\n    run_divergence_analysis(args)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.04}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    wrapper.eval()\\n    return wrapper.policy, wrapper, config\\n\\n\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\n\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\n    q = quat.astype(np.float64)\\n    w = np.clip(q[3], -1.0, 1.0)\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\n    if den > 1e-10:\\n        angle = 2.0 * np.arccos(w)\\n        axis = q[:3] / den\\n        return (axis * angle).astype(np.float32)\\n    return np.zeros(3, dtype=np.float32)\\n\\n\\ndef extract_state(obs: dict) -> np.ndarray:\\n    rs = obs[\\\"robot_state\\\"]\\n    eef_pos = np.asarray(rs[\\\"eef\\\"][\\\"pos\\\"], dtype=np.float32)\\n    eef_quat = np.asarray(rs[\\\"eef\\\"][\\\"quat\\\"], dtype=np.float64)\\n    gripper_qpos = np.asarray(rs[\\\"gripper\\\"][\\\"qpos\\\"], dtype=np.float32)\\n    eef_aa = quat_to_axis_angle(eef_quat)\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\n\\n\\ndef obs_to_batch(obs, task_text, tokenizer, camera_keys, device):\\n    batch = {}\\n    for cam_key in camera_keys:\\n        short_name = cam_key.split(\\\".\\\")[-1]\\n        img = obs[\\\"pixels\\\"][short_name]\\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\\n        img_t = img_t.unsqueeze(0)\\n        img_t = torch.flip(img_t, dims=[2, 3])\\n        batch[cam_key] = img_t.to(device)\\n    state = extract_state(obs)\\n    batch[\\\"observation.state\\\"] = torch.from_numpy(state).unsqueeze(0).to(device)\\n    text = task_text if task_text.endswith(\\\"\\\\n\\\") else task_text + \\\"\\\\n\\\"\\n    encoded = tokenizer(\\n        [text], padding=\\\"longest\\\", max_length=48, truncation=True, return_tensors=\\\"pt\\\",\\n    )\\n    batch[\\\"observation.language.tokens\\\"] = encoded[\\\"input_ids\\\"].to(device)\\n    batch[\\\"observation.language.attention_mask\\\"] = encoded[\\\"attention_mask\\\"].bool().to(device)\\n    return batch\\n\\n\\ndef find_connector(model):\\n    for name, module in model.named_modules():\\n        if name.endswith(\\\".connector\\\") or \\\"multi_modal_projector\\\" in name:\\n            return module\\n    return None\\n\\n\\n@torch.no_grad()\\ndef compute_acis_mask(wrapper, batch, device):\\n    bm = wrapper.base_model\\n    images, _ = wrapper.policy.prepare_images(batch)\\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\\n    B = vis_tokens.shape[0]\\n    noise = bm.sample_noise(\\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\\n    )\\n    time = torch.ones(B, device=device)\\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\\n    scores = wrapper.acis(suffix_embs, vis_tokens)\\n    N_vis = vis_tokens.shape[1]\\n    k = max(1, int(N_vis * wrapper.k_ratio))\\n    _, topk_idx = torch.topk(scores, k, dim=-1)\\n    mask = torch.zeros(B, N_vis, device=device)\\n    mask.scatter_(1, topk_idx, 1.0)\\n    return mask\\n\\n\\ndef register_acis_hook(connector, mask):\\n    def hook_fn(module, input, output):\\n        tokens = output[0] if isinstance(output, tuple) else output\\n        if tokens.dim() != 3 or tokens.shape[1] != mask.shape[1]:\\n            return output\\n        masked = tokens * mask[:tokens.shape[0]].unsqueeze(-1)\\n        if isinstance(output, tuple):\\n            return (masked,) + output[1:]\\n        return masked\\n    return connector.register_forward_hook(hook_fn)\\n\\n\\n@torch.no_grad()\\ndef predict_actions(policy, batch):\\n    images, img_masks = policy.prepare_images(batch)\\n    state = policy.prepare_state(batch)\\n    lang_tokens = batch[\\\"observation.language.tokens\\\"]\\n    lang_masks = batch[\\\"observation.language.attention_mask\\\"]\\n    actions = policy.model.sample_actions(\\n        images, img_masks, lang_tokens, lang_masks, state\\n    )\\n    original_action_dim = policy.config.action_feature.shape[0]\\n    return actions[0, :, :original_action_dim]\\n\\n\\ndef run_divergence_analysis(args):\\n    device = torch.device(f\\\"cuda:{args.gpu}\\\" if torch.cuda.is_available() else \\\"cpu\\\")\\n    task_ids = [int(x) for x in args.task_ids.split(\\\",\\\")]\\n    output_dir = Path(args.output_dir)\\n    output_dir.mkdir(parents=True, exist_ok=True)\\n\\n    np.random.seed(args.seed)\\n    torch.manual_seed(args.seed)\\n\\n    log.info(\\\"Loading baseline model...\\\")\\n    baseline_policy, baseline_config = load_b\\n\\n... [截断: 输出过长，省略 6496 字符] ...\\n\\n: Path):\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\n\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\n    ax = axes[0]\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\n    task_ids = sorted(all_results.keys())\\n\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        for ep_data in episodes:\\n            steps = ep_data[\\\"timesteps\\\"]\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in steps]\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\n\\n    mean_curve = analysis[\\\"mean_l2_curve\\\"]\\n    std_curve = analysis[\\\"std_l2_curve\\\"]\\n    x = np.arange(len(mean_curve))\\n    ax.plot(x, mean_curve, color=\\\"black\\\", linewidth=2, label=\\\"Mean\\\")\\n    mean_arr = np.array(mean_curve)\\n    std_arr = np.array(std_curve)\\n    valid = ~np.isnan(mean_arr)\\n    ax.fill_between(\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\n        alpha=0.15, color=\\\"black\\\"\\n    )\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Baseline vs ACIS k=0.7: Action Divergence\\\")\\n    ax.legend(loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    # Plot 2: Per-dimension breakdown\\n    ax = axes[1]\\n    dim_data = analysis[\\\"per_dim_mean_abs_diff\\\"]\\n    names = list(dim_data.keys())\\n    values = list(dim_data.values())\\n    bar_colors = [\\\"#2196F3\\\"] * 3 + [\\\"#FF9800\\\"] * 3 + [\\\"#4CAF50\\\"]\\n    ax.bar(names, values, color=bar_colors)\\n    ax.set_xlabel(\\\"Action Dimension\\\")\\n    ax.set_ylabel(\\\"Mean |Difference|\\\")\\n    ax.set_title(\\\"Per-Dimension Divergence\\\")\\n    ax.set_xticklabels(names, rotation=45, ha=\\\"right\\\")\\n    ax.grid(True, alpha=0.3, axis=\\\"y\\\")\\n\\n    # Plot 3: Per-task mean curves\\n    ax = axes[2]\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        task_l2s = []\\n        for ep_data in episodes:\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in ep_data[\\\"timesteps\\\"]]\\n            task_l2s.append(l2_vals)\\n        max_t = max(len(c) for c in task_l2s)\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\n        for i, c in enumerate(task_l2s):\\n            padded[i, :len(c)] = c\\n        task_mean = np.nanmean(padded, axis=0)\\n        task_desc = episodes[0][\\\"task_desc\\\"]\\n        short_desc = task_desc[:30] + \\\"...\\\" if len(task_desc) > 30 else task_desc\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\"T{task_id}: {short_desc}\\\", color=colors[ti % 10])\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Per-Task Mean Divergence\\\")\\n    ax.legend(fontsize=7, loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    plt.tight_layout()\\n    pdf_path = output_dir / \\\"action_divergence_curve.pdf\\\"\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.savefig(output_dir / \\\"action_divergence_curve.png\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    log.info(\\\"Plots saved to %s\\\", pdf_path)\\n\\n    # Summary stats figure\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\n    ax2.axis(\\\"off\\\")\\n    summary_text = (\\n        f\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\n\\\"\\n        f\\\"{'='*50}\\\\n\\\"\\n        f\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\n\\\"\\n        f\\\"Num episodes:           {analysis['num_episodes']}\\\\n\\\"\\n        f\\\"Max episode length:     {analysis['max_episode_length']}\\\\n\\\"\\n        f\\\"\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\n\\\"\\n        f\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\n\\\"\\n    )\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\n             verticalalignment=\\\"top\\\", fontfamily=\\\"monospace\\\")\\n    plt.tight_layout()\\n    plt.savefig(output_dir / \\\"action_divergence_summary.pdf\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_divergence_analysis(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.04}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
I still have truncation in the middle section. Let me get the specific line range.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "d66df54d-9a54-44a0-adc2-cd0a5dadbea3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lu6kQNxu8ojry2VBCWN8dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3720,
      "cache_read_input_tokens": 39026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3720
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

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YFaWaDepFkFch5VuvNM7Ma`</summary>

```json
{
  "server": "westd-27271",
  "command": "wc -l /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "0dbf0e87-72d0-4e83-85a1-b08705805d03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lu6kQNxu8ojry2VBCWN8dy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3720,
      "cache_read_input_tokens": 39026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3720
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

_source line 44 · 2026-05-17T10:38:22.027Z_

<details><summary>↩ Tool result · `toolu_01YFaWaDepFkFch5VuvNM7Ma`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"485 /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "8fa80e0f-2f13-4a63-a429-3c59876ddebc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"485 /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"485 /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014eosBUBrGg8Xb3Aep2BgKi`</summary>

```json
{
  "server": "westd-27271",
  "command": "head -n 310 /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "c96eb6a3-011b-450c-8a51-3876776e89c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011csfseXPe3AtiUdEsjCwEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 42746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 46 · 2026-05-17T10:38:27.578Z_

<details><summary>↩ Tool result · `toolu_014eosBUBrGg8Xb3Aep2BgKi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Per-step Action Divergence Analysis: Baseline vs ACIS-pruned model.\\n\\nDrives the environment with baseline actions while recording both models'\\naction outputs at each timestep (same observation). Produces divergence curves\\nand per-dimension breakdown.\\n\\nUsage:\\n    python analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n# Paths\\nBASELINE_CKPT = \\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\"\\nACIS_CKPT = \\\"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\\\"\\nBASELINE_CONFIG = \\\"configs/libero_baseline.yaml\\\"\\nACIS_CONFIG = \\\"configs/libero_acis_stage1only_k07.yaml\\\"\\n\\nSUITE = \\\"libero_object\\\"\\nMAX_STEPS = 280\\nACTION_HORIZON = 50\\nACTION_DIM_NAMES = [\\\"pos_x\\\", \\\"pos_y\\\", \\\"pos_z\\\", \\\"rot_x\\\", \\\"rot_y\\\", \\\"rot_z\\\", \\\"gripper\\\"]\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--gpu\\\", type=int, default=2)\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=5)\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=\\\"0,1,2\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--output_dir\\\", type=str, default=\\\"artifacts\\\")\\n    return p.parse_args()\\n\\n\\ndef load_config(config_path: str) -> dict:\\n    import copy\\n    import yaml\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        for k, v in config.items():\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\n                base_config[k].update(v)\\n            else:\\n                base_config[k] = v\\n        return base_config\\n    return config\\n\\n\\ndef load_baseline_model(device):\\n    from train import load_smolvla_policy\\n    config = load_config(BASELINE_CONFIG)\\n    policy = load_smolvla_policy(config, device)\\n    ckpt = torch.load(BASELINE_CKPT, map_location=device, weights_only=False)\\n    policy.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    policy.eval()\\n    return policy, config\\n\\n\\ndef load_acis_model(device):\\n    from train import load_smolvla_policy, wrap_with_imm\\n    config = load_config(ACIS_CONFIG)\\n    policy = load_smolvla_policy(config, device)\\n    wrapper = wrap_with_imm(policy, config)\\n    wrapper.to(device)\\n    ckpt = torch.load(ACIS_CKPT, map_location=device, weights_only=False)\\n    wrapper.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    wrapper.eval()\\n    return wrapper.policy, wrapper, config\\n\\n\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\n\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\n    q = quat.astype(np.float64)\\n    w = np.clip(q[3], -1.0, 1.0)\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\n    if den > 1e-10:\\n        angle = 2.0 * np.arccos(w)\\n        axis = q[:3] / den\\n        return (axis * angle).astype(np.float32)\\n    return np.zeros(3, dtype=np.float32)\\n\\n\\ndef extract_state(obs: dict) -> np.ndarray:\\n    rs = obs[\\\"robot_state\\\"]\\n    eef_pos = np.asarray(rs[\\\"eef\\\"][\\\"pos\\\"], dtype=np.float32)\\n    eef_quat = np.asarray(rs[\\\"eef\\\"][\\\"quat\\\"], dtype=np.float64)\\n    gripper_qpos = np.asarray(rs[\\\"gripper\\\"][\\\"qpos\\\"], dtype=np.float32)\\n    eef_aa = quat_to_axis_angle(eef_quat)\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\n\\n\\ndef obs_to_\\n\\n... [截断: 输出过长，省略 3003 字符] ...\\n\\nm.seed(args.seed)\\n    torch.manual_seed(args.seed)\\n\\n    log.info(\\\"Loading baseline model...\\\")\\n    baseline_policy, baseline_config = load_baseline_model(device)\\n\\n    log.info(\\\"Loading ACIS model...\\\")\\n    acis_policy, acis_wrapper, acis_config = load_acis_model(device)\\n\\n    from train import get_tokenizer_from_policy\\n    tokenizer = get_tokenizer_from_policy(baseline_policy)\\n\\n    camera_keys = baseline_config.get(\\\"dataset\\\", {}).get(\\\"features\\\", {}).get(\\\"cameras\\\", [\\n        \\\"observation.images.image\\\", \\\"observation.images.image2\\\"\\n    ])\\n\\n    acis_connector = find_connector(acis_policy.model)\\n    if acis_connector is None:\\n        raise RuntimeError(\\\"Cannot find connector for ACIS hook\\\")\\n\\n    from libero.libero import benchmark\\n    from lerobot.envs.libero import get_task_init_states, LiberoEnv\\n\\n    bench_dict = benchmark.get_benchmark_dict()\\n    task_suite = bench_dict[SUITE]()\\n\\n    all_results = {}\\n\\n    for task_id in task_ids:\\n        task = task_suite.get_task(task_id)\\n        task_desc = task.language\\n        log.info(\\\"=== Task %d: %s ===\\\", task_id, task_desc)\\n\\n        env = LiberoEnv(\\n            task_suite=task_suite,\\n            task_id=task_id,\\n            task_suite_name=SUITE,\\n            camera_name=\\\"agentview_image,robot0_eye_in_hand_image\\\",\\n            obs_type=\\\"pixels_agent_pos\\\",\\n            observation_width=256,\\n            observation_height=256,\\n            init_states=True,\\n            n_envs=1,\\n            episode_index=0,\\n            control_mode=\\\"relative\\\",\\n        )\\n\\n        task_episodes = []\\n\\n        for ep in range(args.num_episodes):\\n            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)\\n            baseline_chunk = None\\n            baseline_idx = 0\\n            acis_chunk = None\\n            acis_idx = 0\\n            episode_data = {\\n                \\\"task_id\\\": task_id,\\n                \\\"task_desc\\\": task_desc,\\n                \\\"episode\\\": ep,\\n                \\\"timesteps\\\": [],\\n            }\\n\\n            for step in range(MAX_STEPS):\\n                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\n\\n                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)\\n\\n                if need_replan:\\n                    baseline_chunk = predict_actions(baseline_policy, batch)\\n                    baseline_idx = 0\\n\\n                    mask = compute_acis_mask(acis_wrapper, batch, device)\\n                    hook_handle = register_acis_hook(acis_connector, mask)\\n                    acis_chunk = predict_actions(acis_policy, batch)\\n                    hook_handle.remove()\\n                    acis_idx = 0\\n\\n                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)\\n                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)\\n\\n                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)\\n                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)\\n\\n                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))\\n                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()\\n\\n                episode_data[\\\"timesteps\\\"].append({\\n                    \\\"step\\\": step,\\n                    \\\"baseline_action\\\": baseline_action_clipped.tolist(),\\n                    \\\"acis_action\\\": acis_action_clipped.tolist(),\\n                    \\\"l2_distance\\\": l2_dist,\\n                    \\\"per_dim_diff\\\": per_dim_diff,\\n                })\\n\\n                baseline_idx += 1\\n                acis_idx += 1\\n\\n                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)\\n\\n                if info.get(\\\"is_success\\\", False) or terminated or truncated:\\n                    break\\n\\n            task_episodes.append(episode_data)\\n            n_steps = len(episode_data[\\\"timesteps\\\"])\\n            final_l2 = episode_data[\\\"timesteps\\\"][-1][\\\"l2_distance\\\"] if n_steps > 0 else 0\\n            log.info(\\\"  Ep %d: %d steps, final L2=%.4f\\\", ep, n_steps, final_l2)\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.18}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "56cb07f2-1d76-4535-8dd7-0d30e1e0d735",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Per-step Action Divergence Analysis: Baseline vs ACIS-pruned model.\\\\n\\\\nDrives the environment with baseline actions while recording both models'\\\\naction outputs at each timestep (same observation). Produces divergence curves\\\\nand per-dimension breakdown.\\\\n\\\\nUsage:\\\\n    python analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nimport time as time_mod\\\\nfrom pathlib import Path\\\\n\\\\nos.environ.setdefault(\\\\\\\"MUJOCO_GL\\\\\\\", \\\\\\\"egl\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"TRANSFORMERS_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"HF_HUB_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\n\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport numpy as np\\\\nimport torch\\\\n\\\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\\\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\n# Paths\\\\nBASELINE_CKPT = \\\\\\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\\\\\"\\\\nACIS_CKPT = \\\\\\\"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\\\\\\\"\\\\nBASELINE_CONFIG = \\\\\\\"configs/libero_baseline.yaml\\\\\\\"\\\\nACIS_CONFIG = \\\\\\\"configs/libero_acis_stage1only_k07.yaml\\\\\\\"\\\\n\\\\nSUITE = \\\\\\\"libero_object\\\\\\\"\\\\nMAX_STEPS = 280\\\\nACTION_HORIZON = 50\\\\nACTION_DIM_NAMES = [\\\\\\\"pos_x\\\\\\\", \\\\\\\"pos_y\\\\\\\", \\\\\\\"pos_z\\\\\\\", \\\\\\\"rot_x\\\\\\\", \\\\\\\"rot_y\\\\\\\", \\\\\\\"rot_z\\\\\\\", \\\\\\\"gripper\\\\\\\"]\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=2)\\\\n    p.add_argument(\\\\\\\"--num_episodes\\\\\\\", type=int, default=5)\\\\n    p.add_argument(\\\\\\\"--task_ids\\\\\\\", type=str, default=\\\\\\\"0,1,2\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\", type=str, default=\\\\\\\"artifacts\\\\\\\")\\\\n    return p.parse_args()\\\\n\\\\n\\\\ndef load_config(config_path: str) -> dict:\\\\n    import copy\\\\n    import yaml\\\\n    config_path = Path(config_path)\\\\n    with open(config_path) as f:\\\\n        config = yaml.safe_load(f)\\\\n    if \\\\\\\"_base_\\\\\\\" in config:\\\\n        base_path = config_path.parent / config.pop(\\\\\\\"_base_\\\\\\\")\\\\n        base_config = load_config(str(base_path))\\\\n        for k, v in config.items():\\\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\\\n                base_config[k].update(v)\\\\n            else:\\\\n                base_config[k] = v\\\\n        return base_config\\\\n    return config\\\\n\\\\n\\\\ndef load_baseline_model(device):\\\\n    from train import load_smolvla_policy\\\\n    config = load_config(BASELINE_CONFIG)\\\\n    policy = load_smolvla_policy(config, device)\\\\n    ckpt = torch.load(BASELINE_CKPT, map_location=device, weights_only=False)\\\\n    policy.load_state_dict(ckpt[\\\\\\\"model_state_dict\\\\\\\"], strict=False)\\\\n    policy.eval()\\\\n    return policy, config\\\\n\\\\n\\\\ndef load_acis_model(device):\\\\n    from train import load_smolvla_policy, wrap_with_imm\\\\n    config = load_config(ACIS_CONFIG)\\\\n    policy = load_smolvla_policy(config, device)\\\\n    wrapper = wrap_with_imm(policy, config)\\\\n    wrapper.to(device)\\\\n    ckpt = torch.load(ACIS_CKPT, map_location=device, weights_only=False)\\\\n    wrapper.load_state_dict(ckpt[\\\\\\\"model_state_dict\\\\\\\"], strict=False)\\\\n    wrapper.eval()\\\\n    return wrapper.policy, wrapper, config\\\\n\\\\n\\\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\\\n\\\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\\\n    q = quat.astype(np.float64)\\\\n    w = np.clip(q[3], -1.0, 1.0)\\\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\\\n    if den > 1e-10:\\\\n        angle = 2.0 * np.arccos(w)\\\\n        axis = q[:3] / den\\\\n        return (axis * angle).astype(np.float32)\\\\n    return np.zeros(3, dtype=np.float32)\\\\n\\\\n\\\\ndef extract_state(obs: dict) -> np.ndarray:\\\\n    rs = obs[\\\\\\\"robot_state\\\\\\\"]\\\\n    eef_pos = np.asarray(rs[\\\\\\\"eef\\\\\\\"][\\\\\\\"pos\\\\\\\"], dtype=np.float32)\\\\n    eef_quat = np.asarray(rs[\\\\\\\"eef\\\\\\\"][\\\\\\\"quat\\\\\\\"], dtype=np.float64)\\\\n    gripper_qpos = np.asarray(rs[\\\\\\\"gripper\\\\\\\"][\\\\\\\"qpos\\\\\\\"], dtype=np.float32)\\\\n    eef_aa = quat_to_axis_angle(eef_quat)\\\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\\\n\\\\n\\\\ndef obs_to_\\\\n\\\\n... [截断: 输出过长，省略 3003 字符] ...\\\\n\\\\nm.seed(args.seed)\\\\n    torch.manual_seed(args.seed)\\\\n\\\\n    log.info(\\\\\\\"Loading baseline model...\\\\\\\")\\\\n    baseline_policy, baseline_config = load_baseline_model(device)\\\\n\\\\n    log.info(\\\\\\\"Loading ACIS model...\\\\\\\")\\\\n    acis_policy, acis_wrapper, acis_config = load_acis_model(device)\\\\n\\\\n    from train import get_tokenizer_from_policy\\\\n    tokenizer = get_tokenizer_from_policy(baseline_policy)\\\\n\\\\n    camera_keys = baseline_config.get(\\\\\\\"dataset\\\\\\\", {}).get(\\\\\\\"features\\\\\\\", {}).get(\\\\\\\"cameras\\\\\\\", [\\\\n        \\\\\\\"observation.images.image\\\\\\\", \\\\\\\"observation.images.image2\\\\\\\"\\\\n    ])\\\\n\\\\n    acis_connector = find_connector(acis_policy.model)\\\\n    if acis_connector is None:\\\\n        raise RuntimeError(\\\\\\\"Cannot find connector for ACIS hook\\\\\\\")\\\\n\\\\n    from libero.libero import benchmark\\\\n    from lerobot.envs.libero import get_task_init_states, LiberoEnv\\\\n\\\\n    bench_dict = benchmark.get_benchmark_dict()\\\\n    task_suite = bench_dict[SUITE]()\\\\n\\\\n    all_results = {}\\\\n\\\\n    for task_id in task_ids:\\\\n        task = task_suite.get_task(task_id)\\\\n        task_desc = task.language\\\\n        log.info(\\\\\\\"=== Task %d: %s ===\\\\\\\", task_id, task_desc)\\\\n\\\\n        env = LiberoEnv(\\\\n            task_suite=task_suite,\\\\n            task_id=task_id,\\\\n            task_suite_name=SUITE,\\\\n            camera_name=\\\\\\\"agentview_image,robot0_eye_in_hand_image\\\\\\\",\\\\n            obs_type=\\\\\\\"pixels_agent_pos\\\\\\\",\\\\n            observation_width=256,\\\\n            observation_height=256,\\\\n            init_states=True,\\\\n            n_envs=1,\\\\n            episode_index=0,\\\\n            control_mode=\\\\\\\"relative\\\\\\\",\\\\n        )\\\\n\\\\n        task_episodes = []\\\\n\\\\n        for ep in range(args.num_episodes):\\\\n            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)\\\\n            baseline_chunk = None\\\\n            baseline_idx = 0\\\\n            acis_chunk = None\\\\n            acis_idx = 0\\\\n            episode_data = {\\\\n                \\\\\\\"task_id\\\\\\\": task_id,\\\\n                \\\\\\\"task_desc\\\\\\\": task_desc,\\\\n                \\\\\\\"episode\\\\\\\": ep,\\\\n                \\\\\\\"timesteps\\\\\\\": [],\\\\n            }\\\\n\\\\n            for step in range(MAX_STEPS):\\\\n                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\\\n\\\\n                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)\\\\n\\\\n                if need_replan:\\\\n                    baseline_chunk = predict_actions(baseline_policy, batch)\\\\n                    baseline_idx = 0\\\\n\\\\n                    mask = compute_acis_mask(acis_wrapper, batch, device)\\\\n                    hook_handle = register_acis_hook(acis_connector, mask)\\\\n                    acis_chunk = predict_actions(acis_policy, batch)\\\\n                    hook_handle.remove()\\\\n                    acis_idx = 0\\\\n\\\\n                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)\\\\n                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)\\\\n\\\\n                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)\\\\n                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)\\\\n\\\\n                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))\\\\n                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()\\\\n\\\\n                episode_data[\\\\\\\"timesteps\\\\\\\"].append({\\\\n                    \\\\\\\"step\\\\\\\": step,\\\\n                    \\\\\\\"baseline_action\\\\\\\": baseline_action_clipped.tolist(),\\\\n                    \\\\\\\"acis_action\\\\\\\": acis_action_clipped.tolist(),\\\\n                    \\\\\\\"l2_distance\\\\\\\": l2_dist,\\\\n                    \\\\\\\"per_dim_diff\\\\\\\": per_dim_diff,\\\\n                })\\\\n\\\\n                baseline_idx += 1\\\\n                acis_idx += 1\\\\n\\\\n                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)\\\\n\\\\n                if info.get(\\\\\\\"is_success\\\\\\\", False) or terminated or truncated:\\\\n                    break\\\\n\\\\n            task_episodes.append(episode_data)\\\\n            n_steps = len(episode_data[\\\\\\\"timesteps\\\\\\\"])\\\\n            final_l2 = episode_data[\\\\\\\"timesteps\\\\\\\"][-1][\\\\\\\"l2_distance\\\\\\\"] if n_steps > 0 else 0\\\\n            log.info(\\\\\\\"  Ep %d: %d steps, final L2=%.4f\\\\\\\", ep, n_steps, final_l2)\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.18}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Per-step Action Divergence Analysis: Baseline vs ACIS-pruned model.\\n\\nDrives the environment with baseline actions while recording both models'\\naction outputs at each timestep (same observation). Produces divergence curves\\nand per-dimension breakdown.\\n\\nUsage:\\n    python analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nimport torch\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\nsys.path.insert(0, str(ARTIFACTS_DIR))\\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n# Paths\\nBASELINE_CKPT = \\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\"\\nACIS_CKPT = \\\"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\\\"\\nBASELINE_CONFIG = \\\"configs/libero_baseline.yaml\\\"\\nACIS_CONFIG = \\\"configs/libero_acis_stage1only_k07.yaml\\\"\\n\\nSUITE = \\\"libero_object\\\"\\nMAX_STEPS = 280\\nACTION_HORIZON = 50\\nACTION_DIM_NAMES = [\\\"pos_x\\\", \\\"pos_y\\\", \\\"pos_z\\\", \\\"rot_x\\\", \\\"rot_y\\\", \\\"rot_z\\\", \\\"gripper\\\"]\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--gpu\\\", type=int, default=2)\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=5)\\n    p.add_argument(\\\"--task_ids\\\", type=str, default=\\\"0,1,2\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--output_dir\\\", type=str, default=\\\"artifacts\\\")\\n    return p.parse_args()\\n\\n\\ndef load_config(config_path: str) -> dict:\\n    import copy\\n    import yaml\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        for k, v in config.items():\\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\\n                base_config[k].update(v)\\n            else:\\n                base_config[k] = v\\n        return base_config\\n    return config\\n\\n\\ndef load_baseline_model(device):\\n    from train import load_smolvla_policy\\n    config = load_config(BASELINE_CONFIG)\\n    policy = load_smolvla_policy(config, device)\\n    ckpt = torch.load(BASELINE_CKPT, map_location=device, weights_only=False)\\n    policy.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    policy.eval()\\n    return policy, config\\n\\n\\ndef load_acis_model(device):\\n    from train import load_smolvla_policy, wrap_with_imm\\n    config = load_config(ACIS_CONFIG)\\n    policy = load_smolvla_policy(config, device)\\n    wrapper = wrap_with_imm(policy, config)\\n    wrapper.to(device)\\n    ckpt = torch.load(ACIS_CKPT, map_location=device, weights_only=False)\\n    wrapper.load_state_dict(ckpt[\\\"model_state_dict\\\"], strict=False)\\n    wrapper.eval()\\n    return wrapper.policy, wrapper, config\\n\\n\\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\\n\\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\\n    q = quat.astype(np.float64)\\n    w = np.clip(q[3], -1.0, 1.0)\\n    den = np.sqrt(max(1.0 - w * w, 0.0))\\n    if den > 1e-10:\\n        angle = 2.0 * np.arccos(w)\\n        axis = q[:3] / den\\n        return (axis * angle).astype(np.float32)\\n    return np.zeros(3, dtype=np.float32)\\n\\n\\ndef extract_state(obs: dict) -> np.ndarray:\\n    rs = obs[\\\"robot_state\\\"]\\n    eef_pos = np.asarray(rs[\\\"eef\\\"][\\\"pos\\\"], dtype=np.float32)\\n    eef_quat = np.asarray(rs[\\\"eef\\\"][\\\"quat\\\"], dtype=np.float64)\\n    gripper_qpos = np.asarray(rs[\\\"gripper\\\"][\\\"qpos\\\"], dtype=np.float32)\\n    eef_aa = quat_to_axis_angle(eef_quat)\\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\\n\\n\\ndef obs_to_\\n\\n... [截断: 输出过长，省略 3003 字符] ...\\n\\nm.seed(args.seed)\\n    torch.manual_seed(args.seed)\\n\\n    log.info(\\\"Loading baseline model...\\\")\\n    baseline_policy, baseline_config = load_baseline_model(device)\\n\\n    log.info(\\\"Loading ACIS model...\\\")\\n    acis_policy, acis_wrapper, acis_config = load_acis_model(device)\\n\\n    from train import get_tokenizer_from_policy\\n    tokenizer = get_tokenizer_from_policy(baseline_policy)\\n\\n    camera_keys = baseline_config.get(\\\"dataset\\\", {}).get(\\\"features\\\", {}).get(\\\"cameras\\\", [\\n        \\\"observation.images.image\\\", \\\"observation.images.image2\\\"\\n    ])\\n\\n    acis_connector = find_connector(acis_policy.model)\\n    if acis_connector is None:\\n        raise RuntimeError(\\\"Cannot find connector for ACIS hook\\\")\\n\\n    from libero.libero import benchmark\\n    from lerobot.envs.libero import get_task_init_states, LiberoEnv\\n\\n    bench_dict = benchmark.get_benchmark_dict()\\n    task_suite = bench_dict[SUITE]()\\n\\n    all_results = {}\\n\\n    for task_id in task_ids:\\n        task = task_suite.get_task(task_id)\\n        task_desc = task.language\\n        log.info(\\\"=== Task %d: %s ===\\\", task_id, task_desc)\\n\\n        env = LiberoEnv(\\n            task_suite=task_suite,\\n            task_id=task_id,\\n            task_suite_name=SUITE,\\n            camera_name=\\\"agentview_image,robot0_eye_in_hand_image\\\",\\n            obs_type=\\\"pixels_agent_pos\\\",\\n            observation_width=256,\\n            observation_height=256,\\n            init_states=True,\\n            n_envs=1,\\n            episode_index=0,\\n            control_mode=\\\"relative\\\",\\n        )\\n\\n        task_episodes = []\\n\\n        for ep in range(args.num_episodes):\\n            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)\\n            baseline_chunk = None\\n            baseline_idx = 0\\n            acis_chunk = None\\n            acis_idx = 0\\n            episode_data = {\\n                \\\"task_id\\\": task_id,\\n                \\\"task_desc\\\": task_desc,\\n                \\\"episode\\\": ep,\\n                \\\"timesteps\\\": [],\\n            }\\n\\n            for step in range(MAX_STEPS):\\n                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\\n\\n                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)\\n\\n                if need_replan:\\n                    baseline_chunk = predict_actions(baseline_policy, batch)\\n                    baseline_idx = 0\\n\\n                    mask = compute_acis_mask(acis_wrapper, batch, device)\\n                    hook_handle = register_acis_hook(acis_connector, mask)\\n                    acis_chunk = predict_actions(acis_policy, batch)\\n                    hook_handle.remove()\\n                    acis_idx = 0\\n\\n                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)\\n                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)\\n\\n                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)\\n                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)\\n\\n                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))\\n                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()\\n\\n                episode_data[\\\"timesteps\\\"].append({\\n                    \\\"step\\\": step,\\n                    \\\"baseline_action\\\": baseline_action_clipped.tolist(),\\n                    \\\"acis_action\\\": acis_action_clipped.tolist(),\\n                    \\\"l2_distance\\\": l2_dist,\\n                    \\\"per_dim_diff\\\": per_dim_diff,\\n                })\\n\\n                baseline_idx += 1\\n                acis_idx += 1\\n\\n                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)\\n\\n                if info.get(\\\"is_success\\\", False) or terminated or truncated:\\n                    break\\n\\n            task_episodes.append(episode_data)\\n            n_steps = len(episode_data[\\\"timesteps\\\"])\\n            final_l2 = episode_data[\\\"timesteps\\\"][-1][\\\"l2_distance\\\"] if n_steps > 0 else 0\\n            log.info(\\\"  Ep %d: %d steps, final L2=%.4f\\\", ep, n_steps, final_l2)\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.18}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the remaining part (lines 310+).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "c00a3471-cc2e-47a4-b156-174facc453b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017R58p5BE6nDGWKyWf4wMaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3409,
      "cache_read_input_tokens": 43015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3409
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

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HA2MvQKMuWAvbUwArUHWdT`</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -n +310 /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "3705bab1-fb1a-4006-b599-a789fd16a9e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017R58p5BE6nDGWKyWf4wMaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3409,
      "cache_read_input_tokens": 43015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3409
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

_source line 49 · 2026-05-17T10:38:34.502Z_

<details><summary>↩ Tool result · `toolu_01HA2MvQKMuWAvbUwArUHWdT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n        env.close()\\n        all_results[task_id] = task_episodes\\n\\n    # --- Analysis ---\\n    log.info(\\\"Computing statistics...\\\")\\n    analysis = compute_analysis(all_results)\\n\\n    # Save raw data\\n    json_path = output_dir / \\\"action_divergence_data.json\\\"\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump({\\\"episodes\\\": all_results, \\\"analysis\\\": analysis}, f, indent=2)\\n    log.info(\\\"Raw data saved to %s\\\", json_path)\\n\\n    # Plot\\n    plot_divergence_curves(all_results, analysis, output_dir)\\n    log.info(\\\"Done.\\\")\\n\\n\\ndef compute_analysis(all_results: dict) -> dict:\\n    all_l2_curves = []\\n    all_per_dim_curves = []\\n\\n    for task_id, episodes in all_results.items():\\n        for ep_data in episodes:\\n            steps = ep_data[\\\"timesteps\\\"]\\n            l2_curve = [s[\\\"l2_distance\\\"] for s in steps]\\n            per_dim = [s[\\\"per_dim_diff\\\"] for s in steps]\\n            all_l2_curves.append(l2_curve)\\n            all_per_dim_curves.append(per_dim)\\n\\n    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0\\n\\n    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)\\n    for i, curve in enumerate(all_l2_curves):\\n        padded_l2[i, :len(curve)] = curve\\n\\n    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()\\n    std_l2 = np.nanstd(padded_l2, axis=0).tolist()\\n\\n    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]\\n    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0\\n\\n    overall_mean_l2 = float(np.nanmean(padded_l2))\\n\\n    # Per-dimension analysis\\n    n_dims = 7\\n    dim_abs_means = []\\n    for d in range(n_dims):\\n        dim_vals = []\\n        for per_dim_curve in all_per_dim_curves:\\n            for step_diff in per_dim_curve:\\n                if len(step_diff) > d:\\n                    dim_vals.append(abs(step_diff[d]))\\n        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)\\n\\n    # Growth rate: linear regression slope on mean L2\\n    valid_mean = [v for v in mean_l2 if not np.isnan(v)]\\n    if len(valid_mean) > 10:\\n        x = np.arange(len(valid_mean))\\n        slope = float(np.polyfit(x, valid_mean, 1)[0])\\n    else:\\n        slope = 0.0\\n\\n    return {\\n        \\\"overall_mean_l2\\\": overall_mean_l2,\\n        \\\"first_step_mean_l2\\\": avg_first_step,\\n        \\\"l2_growth_rate_per_step\\\": slope,\\n        \\\"per_dim_mean_abs_diff\\\": {\\n            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))\\n        },\\n        \\\"mean_l2_curve\\\": mean_l2,\\n        \\\"std_l2_curve\\\": std_l2,\\n        \\\"num_episodes\\\": len(all_l2_curves),\\n        \\\"max_episode_length\\\": max_len,\\n    }\\n\\n\\ndef plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path):\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\n\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\n    ax = axes[0]\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\n    task_ids = sorted(all_results.keys())\\n\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        for ep_data in episodes:\\n            steps = ep_data[\\\"timesteps\\\"]\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in steps]\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\n\\n    mean_curve = analysis[\\\"mean_l2_curve\\\"]\\n    std_curve = analysis[\\\"std_l2_curve\\\"]\\n    x = np.arange(len(mean_curve))\\n    ax.plot(x, mean_curve, color=\\\"black\\\", linewidth=2, label=\\\"Mean\\\")\\n    mean_arr = np.array(mean_curve)\\n    std_arr = np.array(std_curve)\\n    valid = ~np.isnan(mean_arr)\\n    ax.fill_between(\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\n        alpha=0.15, color=\\\"black\\\"\\n    )\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Baseline vs ACIS k=0.7: Action Divergence\\\")\\n    ax.legend(loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    # Plot 2: Per-dimension breakdown\\n    ax = axes[1]\\n    dim_data = analysis[\\\"per_dim_mean_abs_diff\\\"]\\n    names = list(dim_data.keys())\\n    values = list(dim_data.values())\\n    bar_colors = [\\\"#2196F3\\\"] * 3 + [\\\"#FF9800\\\"] * 3 + [\\\"#4CAF50\\\"]\\n    ax.bar(names, values, color=bar_colors)\\n    ax.set_xlabel(\\\"Action Dimension\\\")\\n    ax.set_ylabel(\\\"Mean |Difference|\\\")\\n    ax.set_title(\\\"Per-Dimension Divergence\\\")\\n    ax.set_xticklabels(names, rotation=45, ha=\\\"right\\\")\\n    ax.grid(True, alpha=0.3, axis=\\\"y\\\")\\n\\n    # Plot 3: Per-task mean curves\\n    ax = axes[2]\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        task_l2s = []\\n        for ep_data in episodes:\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in ep_data[\\\"timesteps\\\"]]\\n            task_l2s.append(l2_vals)\\n        max_t = max(len(c) for c in task_l2s)\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\n        for i, c in enumerate(task_l2s):\\n            padded[i, :len(c)] = c\\n        task_mean = np.nanmean(padded, axis=0)\\n        task_desc = episodes[0][\\\"task_desc\\\"]\\n        short_desc = task_desc[:30] + \\\"...\\\" if len(task_desc) > 30 else task_desc\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\"T{task_id}: {short_desc}\\\", color=colors[ti % 10])\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Per-Task Mean Divergence\\\")\\n    ax.legend(fontsize=7, loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    plt.tight_layout()\\n    pdf_path = output_dir / \\\"action_divergence_curve.pdf\\\"\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.savefig(output_dir / \\\"action_divergence_curve.png\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    log.info(\\\"Plots saved to %s\\\", pdf_path)\\n\\n    # Summary stats figure\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\n    ax2.axis(\\\"off\\\")\\n    summary_text = (\\n        f\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\n\\\"\\n        f\\\"{'='*50}\\\\n\\\"\\n        f\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\n\\\"\\n        f\\\"Num episodes:           {analysis['num_episodes']}\\\\n\\\"\\n        f\\\"Max episode length:     {analysis['max_episode_length']}\\\\n\\\"\\n        f\\\"\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\n\\\"\\n        f\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\n\\\"\\n    )\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\n             verticalalignment=\\\"top\\\", fontfamily=\\\"monospace\\\")\\n    plt.tight_layout()\\n    plt.savefig(output_dir / \\\"action_divergence_summary.pdf\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_divergence_analysis(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "d4e8622e-2453-4e12-80c7-6b46b4dfe0c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\n        env.close()\\\\n        all_results[task_id] = task_episodes\\\\n\\\\n    # --- Analysis ---\\\\n    log.info(\\\\\\\"Computing statistics...\\\\\\\")\\\\n    analysis = compute_analysis(all_results)\\\\n\\\\n    # Save raw data\\\\n    json_path = output_dir / \\\\\\\"action_divergence_data.json\\\\\\\"\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump({\\\\\\\"episodes\\\\\\\": all_results, \\\\\\\"analysis\\\\\\\": analysis}, f, indent=2)\\\\n    log.info(\\\\\\\"Raw data saved to %s\\\\\\\", json_path)\\\\n\\\\n    # Plot\\\\n    plot_divergence_curves(all_results, analysis, output_dir)\\\\n    log.info(\\\\\\\"Done.\\\\\\\")\\\\n\\\\n\\\\ndef compute_analysis(all_results: dict) -> dict:\\\\n    all_l2_curves = []\\\\n    all_per_dim_curves = []\\\\n\\\\n    for task_id, episodes in all_results.items():\\\\n        for ep_data in episodes:\\\\n            steps = ep_data[\\\\\\\"timesteps\\\\\\\"]\\\\n            l2_curve = [s[\\\\\\\"l2_distance\\\\\\\"] for s in steps]\\\\n            per_dim = [s[\\\\\\\"per_dim_diff\\\\\\\"] for s in steps]\\\\n            all_l2_curves.append(l2_curve)\\\\n            all_per_dim_curves.append(per_dim)\\\\n\\\\n    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0\\\\n\\\\n    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)\\\\n    for i, curve in enumerate(all_l2_curves):\\\\n        padded_l2[i, :len(curve)] = curve\\\\n\\\\n    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()\\\\n    std_l2 = np.nanstd(padded_l2, axis=0).tolist()\\\\n\\\\n    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]\\\\n    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0\\\\n\\\\n    overall_mean_l2 = float(np.nanmean(padded_l2))\\\\n\\\\n    # Per-dimension analysis\\\\n    n_dims = 7\\\\n    dim_abs_means = []\\\\n    for d in range(n_dims):\\\\n        dim_vals = []\\\\n        for per_dim_curve in all_per_dim_curves:\\\\n            for step_diff in per_dim_curve:\\\\n                if len(step_diff) > d:\\\\n                    dim_vals.append(abs(step_diff[d]))\\\\n        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)\\\\n\\\\n    # Growth rate: linear regression slope on mean L2\\\\n    valid_mean = [v for v in mean_l2 if not np.isnan(v)]\\\\n    if len(valid_mean) > 10:\\\\n        x = np.arange(len(valid_mean))\\\\n        slope = float(np.polyfit(x, valid_mean, 1)[0])\\\\n    else:\\\\n        slope = 0.0\\\\n\\\\n    return {\\\\n        \\\\\\\"overall_mean_l2\\\\\\\": overall_mean_l2,\\\\n        \\\\\\\"first_step_mean_l2\\\\\\\": avg_first_step,\\\\n        \\\\\\\"l2_growth_rate_per_step\\\\\\\": slope,\\\\n        \\\\\\\"per_dim_mean_abs_diff\\\\\\\": {\\\\n            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))\\\\n        },\\\\n        \\\\\\\"mean_l2_curve\\\\\\\": mean_l2,\\\\n        \\\\\\\"std_l2_curve\\\\\\\": std_l2,\\\\n        \\\\\\\"num_episodes\\\\\\\": len(all_l2_curves),\\\\n        \\\\\\\"max_episode_length\\\\\\\": max_len,\\\\n    }\\\\n\\\\n\\\\ndef plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path):\\\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\\\n\\\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\\\n    ax = axes[0]\\\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\\\n    task_ids = sorted(all_results.keys())\\\\n\\\\n    for ti, task_id in enumerate(task_ids):\\\\n        episodes = all_results[task_id]\\\\n        for ep_data in episodes:\\\\n            steps = ep_data[\\\\\\\"timesteps\\\\\\\"]\\\\n            l2_vals = [s[\\\\\\\"l2_distance\\\\\\\"] for s in steps]\\\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\\\n\\\\n    mean_curve = analysis[\\\\\\\"mean_l2_curve\\\\\\\"]\\\\n    std_curve = analysis[\\\\\\\"std_l2_curve\\\\\\\"]\\\\n    x = np.arange(len(mean_curve))\\\\n    ax.plot(x, mean_curve, color=\\\\\\\"black\\\\\\\", linewidth=2, label=\\\\\\\"Mean\\\\\\\")\\\\n    mean_arr = np.array(mean_curve)\\\\n    std_arr = np.array(std_curve)\\\\n    valid = ~np.isnan(mean_arr)\\\\n    ax.fill_between(\\\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\\\n        alpha=0.15, color=\\\\\\\"black\\\\\\\"\\\\n    )\\\\n    ax.set_xlabel(\\\\\\\"Timestep\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"L2 Action Distance\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Baseline vs ACIS k=0.7: Action Divergence\\\\\\\")\\\\n    ax.legend(loc=\\\\\\\"upper left\\\\\\\")\\\\n    ax.grid(True, alpha=0.3)\\\\n\\\\n    # Plot 2: Per-dimension breakdown\\\\n    ax = axes[1]\\\\n    dim_data = analysis[\\\\\\\"per_dim_mean_abs_diff\\\\\\\"]\\\\n    names = list(dim_data.keys())\\\\n    values = list(dim_data.values())\\\\n    bar_colors = [\\\\\\\"#2196F3\\\\\\\"] * 3 + [\\\\\\\"#FF9800\\\\\\\"] * 3 + [\\\\\\\"#4CAF50\\\\\\\"]\\\\n    ax.bar(names, values, color=bar_colors)\\\\n    ax.set_xlabel(\\\\\\\"Action Dimension\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"Mean |Difference|\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Per-Dimension Divergence\\\\\\\")\\\\n    ax.set_xticklabels(names, rotation=45, ha=\\\\\\\"right\\\\\\\")\\\\n    ax.grid(True, alpha=0.3, axis=\\\\\\\"y\\\\\\\")\\\\n\\\\n    # Plot 3: Per-task mean curves\\\\n    ax = axes[2]\\\\n    for ti, task_id in enumerate(task_ids):\\\\n        episodes = all_results[task_id]\\\\n        task_l2s = []\\\\n        for ep_data in episodes:\\\\n            l2_vals = [s[\\\\\\\"l2_distance\\\\\\\"] for s in ep_data[\\\\\\\"timesteps\\\\\\\"]]\\\\n            task_l2s.append(l2_vals)\\\\n        max_t = max(len(c) for c in task_l2s)\\\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\\\n        for i, c in enumerate(task_l2s):\\\\n            padded[i, :len(c)] = c\\\\n        task_mean = np.nanmean(padded, axis=0)\\\\n        task_desc = episodes[0][\\\\\\\"task_desc\\\\\\\"]\\\\n        short_desc = task_desc[:30] + \\\\\\\"...\\\\\\\" if len(task_desc) > 30 else task_desc\\\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\\\\\"T{task_id}: {short_desc}\\\\\\\", color=colors[ti % 10])\\\\n    ax.set_xlabel(\\\\\\\"Timestep\\\\\\\")\\\\n    ax.set_ylabel(\\\\\\\"L2 Action Distance\\\\\\\")\\\\n    ax.set_title(\\\\\\\"Per-Task Mean Divergence\\\\\\\")\\\\n    ax.legend(fontsize=7, loc=\\\\\\\"upper left\\\\\\\")\\\\n    ax.grid(True, alpha=0.3)\\\\n\\\\n    plt.tight_layout()\\\\n    pdf_path = output_dir / \\\\\\\"action_divergence_curve.pdf\\\\\\\"\\\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.savefig(output_dir / \\\\\\\"action_divergence_curve.png\\\\\\\", dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n    log.info(\\\\\\\"Plots saved to %s\\\\\\\", pdf_path)\\\\n\\\\n    # Summary stats figure\\\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\\\n    ax2.axis(\\\\\\\"off\\\\\\\")\\\\n    summary_text = (\\\\n        f\\\\\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"{'='*50}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Num episodes:           {analysis['num_episodes']}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Max episode length:     {analysis['max_episode_length']}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"\\\\\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\\\\\n\\\\\\\"\\\\n        f\\\\\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\\\\\n\\\\\\\"\\\\n    )\\\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\\\n             verticalalignment=\\\\\\\"top\\\\\\\", fontfamily=\\\\\\\"monospace\\\\\\\")\\\\n    plt.tight_layout()\\\\n    plt.savefig(output_dir / \\\\\\\"action_divergence_summary.pdf\\\\\\\", dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    args = parse_args()\\\\n    run_divergence_analysis(args)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\n        env.close()\\n        all_results[task_id] = task_episodes\\n\\n    # --- Analysis ---\\n    log.info(\\\"Computing statistics...\\\")\\n    analysis = compute_analysis(all_results)\\n\\n    # Save raw data\\n    json_path = output_dir / \\\"action_divergence_data.json\\\"\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump({\\\"episodes\\\": all_results, \\\"analysis\\\": analysis}, f, indent=2)\\n    log.info(\\\"Raw data saved to %s\\\", json_path)\\n\\n    # Plot\\n    plot_divergence_curves(all_results, analysis, output_dir)\\n    log.info(\\\"Done.\\\")\\n\\n\\ndef compute_analysis(all_results: dict) -> dict:\\n    all_l2_curves = []\\n    all_per_dim_curves = []\\n\\n    for task_id, episodes in all_results.items():\\n        for ep_data in episodes:\\n            steps = ep_data[\\\"timesteps\\\"]\\n            l2_curve = [s[\\\"l2_distance\\\"] for s in steps]\\n            per_dim = [s[\\\"per_dim_diff\\\"] for s in steps]\\n            all_l2_curves.append(l2_curve)\\n            all_per_dim_curves.append(per_dim)\\n\\n    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0\\n\\n    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)\\n    for i, curve in enumerate(all_l2_curves):\\n        padded_l2[i, :len(curve)] = curve\\n\\n    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()\\n    std_l2 = np.nanstd(padded_l2, axis=0).tolist()\\n\\n    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]\\n    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0\\n\\n    overall_mean_l2 = float(np.nanmean(padded_l2))\\n\\n    # Per-dimension analysis\\n    n_dims = 7\\n    dim_abs_means = []\\n    for d in range(n_dims):\\n        dim_vals = []\\n        for per_dim_curve in all_per_dim_curves:\\n            for step_diff in per_dim_curve:\\n                if len(step_diff) > d:\\n                    dim_vals.append(abs(step_diff[d]))\\n        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)\\n\\n    # Growth rate: linear regression slope on mean L2\\n    valid_mean = [v for v in mean_l2 if not np.isnan(v)]\\n    if len(valid_mean) > 10:\\n        x = np.arange(len(valid_mean))\\n        slope = float(np.polyfit(x, valid_mean, 1)[0])\\n    else:\\n        slope = 0.0\\n\\n    return {\\n        \\\"overall_mean_l2\\\": overall_mean_l2,\\n        \\\"first_step_mean_l2\\\": avg_first_step,\\n        \\\"l2_growth_rate_per_step\\\": slope,\\n        \\\"per_dim_mean_abs_diff\\\": {\\n            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))\\n        },\\n        \\\"mean_l2_curve\\\": mean_l2,\\n        \\\"std_l2_curve\\\": std_l2,\\n        \\\"num_episodes\\\": len(all_l2_curves),\\n        \\\"max_episode_length\\\": max_len,\\n    }\\n\\n\\ndef plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path):\\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\\n\\n    # Plot 1: L2 divergence curves (all episodes + mean)\\n    ax = axes[0]\\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\\n    task_ids = sorted(all_results.keys())\\n\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        for ep_data in episodes:\\n            steps = ep_data[\\\"timesteps\\\"]\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in steps]\\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\\n\\n    mean_curve = analysis[\\\"mean_l2_curve\\\"]\\n    std_curve = analysis[\\\"std_l2_curve\\\"]\\n    x = np.arange(len(mean_curve))\\n    ax.plot(x, mean_curve, color=\\\"black\\\", linewidth=2, label=\\\"Mean\\\")\\n    mean_arr = np.array(mean_curve)\\n    std_arr = np.array(std_curve)\\n    valid = ~np.isnan(mean_arr)\\n    ax.fill_between(\\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\\n        alpha=0.15, color=\\\"black\\\"\\n    )\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Baseline vs ACIS k=0.7: Action Divergence\\\")\\n    ax.legend(loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    # Plot 2: Per-dimension breakdown\\n    ax = axes[1]\\n    dim_data = analysis[\\\"per_dim_mean_abs_diff\\\"]\\n    names = list(dim_data.keys())\\n    values = list(dim_data.values())\\n    bar_colors = [\\\"#2196F3\\\"] * 3 + [\\\"#FF9800\\\"] * 3 + [\\\"#4CAF50\\\"]\\n    ax.bar(names, values, color=bar_colors)\\n    ax.set_xlabel(\\\"Action Dimension\\\")\\n    ax.set_ylabel(\\\"Mean |Difference|\\\")\\n    ax.set_title(\\\"Per-Dimension Divergence\\\")\\n    ax.set_xticklabels(names, rotation=45, ha=\\\"right\\\")\\n    ax.grid(True, alpha=0.3, axis=\\\"y\\\")\\n\\n    # Plot 3: Per-task mean curves\\n    ax = axes[2]\\n    for ti, task_id in enumerate(task_ids):\\n        episodes = all_results[task_id]\\n        task_l2s = []\\n        for ep_data in episodes:\\n            l2_vals = [s[\\\"l2_distance\\\"] for s in ep_data[\\\"timesteps\\\"]]\\n            task_l2s.append(l2_vals)\\n        max_t = max(len(c) for c in task_l2s)\\n        padded = np.full((len(task_l2s), max_t), np.nan)\\n        for i, c in enumerate(task_l2s):\\n            padded[i, :len(c)] = c\\n        task_mean = np.nanmean(padded, axis=0)\\n        task_desc = episodes[0][\\\"task_desc\\\"]\\n        short_desc = task_desc[:30] + \\\"...\\\" if len(task_desc) > 30 else task_desc\\n        ax.plot(task_mean, linewidth=1.5, label=f\\\"T{task_id}: {short_desc}\\\", color=colors[ti % 10])\\n    ax.set_xlabel(\\\"Timestep\\\")\\n    ax.set_ylabel(\\\"L2 Action Distance\\\")\\n    ax.set_title(\\\"Per-Task Mean Divergence\\\")\\n    ax.legend(fontsize=7, loc=\\\"upper left\\\")\\n    ax.grid(True, alpha=0.3)\\n\\n    plt.tight_layout()\\n    pdf_path = output_dir / \\\"action_divergence_curve.pdf\\\"\\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.savefig(output_dir / \\\"action_divergence_curve.png\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    log.info(\\\"Plots saved to %s\\\", pdf_path)\\n\\n    # Summary stats figure\\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\\n    ax2.axis(\\\"off\\\")\\n    summary_text = (\\n        f\\\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\\\n\\\"\\n        f\\\"{'='*50}\\\\n\\\"\\n        f\\\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\\\n\\\"\\n        f\\\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\\\n\\\"\\n        f\\\"Num episodes:           {analysis['num_episodes']}\\\\n\\\"\\n        f\\\"Max episode length:     {analysis['max_episode_length']}\\\\n\\\"\\n        f\\\"\\\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\\\n\\\"\\n        f\\\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\\\n\\\"\\n    )\\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\\n             verticalalignment=\\\"top\\\", fontfamily=\\\"monospace\\\")\\n    plt.tight_layout()\\n    plt.savefig(output_dir / \\\"action_divergence_summary.pdf\\\", dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    args = parse_args()\\n    run_divergence_analysis(args)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the ACIS config to understand what k_ratio is used:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "3225d21b-4159-4613-af05-4fc81bea3392",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ncw11ZzurNdsS1jVGPYcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3272,
      "cache_read_input_tokens": 46424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3272
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

_source line 51_

Let me check the ACIS config file for k_ratio settings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "da374a2f-d932-42ca-b34c-7922ce787816",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ncw11ZzurNdsS1jVGPYcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3272,
      "cache_read_input_tokens": 46424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3272
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

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UFPWC3DA7qL3M7Dkr2Bcic`</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/configs/libero_acis_stage1only_k07.yaml",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "f415fd1e-2075-4fb9-83e4-74378cb74912",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ncw11ZzurNdsS1jVGPYcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3272,
      "cache_read_input_tokens": 46424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3272
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

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014fW5zNGYB4RntjTX6Z9njc`</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"k_ratio\" /root/autodl-tmp/importance_margin_vla_compress/train.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "3988c987-12ab-4f14-bdd0-3b4d21ae57de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ncw11ZzurNdsS1jVGPYcG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3272,
      "cache_read_input_tokens": 46424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3272
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

_source line 54 · 2026-05-17T10:38:54.148Z_

<details><summary>↩ Tool result · `toolu_01UFPWC3DA7qL3M7Dkr2Bcic`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# ACIS Stage1-only: k=0.7 (retain 70% visual tokens)\\n# Freeze expert, train ACIS selector only, 10K steps.\\n# Purpose: SR vs compression ratio curve point (k=0.7)\\n\\n_base_: libero_baseline.yaml\\n\\nmodel:\\n  train_expert_only: true\\n  lora:\\n    rank: 0\\n\\nimm:\\n  enabled: true\\n  gradient_isolation: false\\n  lambda_margin: 1.0\\n  delta: 0.3\\n  k_ratio: 0.7\\n  temperature: 0.5\\n  soft_topk_method: \\\"sigmoid\\\"\\n  warmup_steps: 0\\n\\nacis:\\n  visual_dim: 960\\n  action_dim: 720\\n  num_heads: 8\\n  dropout: 0.0\\n\\ntwostage:\\n  train_mode: \\\"twostage_fullft\\\"\\n  baseline_checkpoint: \\\"checkpoints/libero_full_ft/step_099999/checkpoint.pt\\\"\\n  stage1_steps: 10000\\n  stage2_steps: 0\\n  stage1_lr: 3.0e-4\\n  stage2_lr: 1.0e-4\\n  stage1_warmup_steps: 500\\n  stage2_warmup_steps: 0\\n  checkpoint_after_stage1: true\\n  stage1_freeze_backbone: true\\n  stage1_train_acis: true\\n  stage2_freeze_acis: true\\n  stage2_train_expert_only: true\\n\\ntraining:\\n  output_dir: \\\"checkpoints/libero_acis_stage1only_k07\\\"\\n  total_steps: 10000\\n  grad_clip: 10.0\\n  save_every: 5000\\n  eval_every: 999999\\n  log_every: 50\\n  batch_size: 4\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "6c4610b2-6736-4b0a-940e-1322c7a671b9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# ACIS Stage1-only: k=0.7 (retain 70% visual tokens)\\\\n# Freeze expert, train ACIS selector only, 10K steps.\\\\n# Purpose: SR vs compression ratio curve point (k=0.7)\\\\n\\\\n_base_: libero_baseline.yaml\\\\n\\\\nmodel:\\\\n  train_expert_only: true\\\\n  lora:\\\\n    rank: 0\\\\n\\\\nimm:\\\\n  enabled: true\\\\n  gradient_isolation: false\\\\n  lambda_margin: 1.0\\\\n  delta: 0.3\\\\n  k_ratio: 0.7\\\\n  temperature: 0.5\\\\n  soft_topk_method: \\\\\\\"sigmoid\\\\\\\"\\\\n  warmup_steps: 0\\\\n\\\\nacis:\\\\n  visual_dim: 960\\\\n  action_dim: 720\\\\n  num_heads: 8\\\\n  dropout: 0.0\\\\n\\\\ntwostage:\\\\n  train_mode: \\\\\\\"twostage_fullft\\\\\\\"\\\\n  baseline_checkpoint: \\\\\\\"checkpoints/libero_full_ft/step_099999/checkpoint.pt\\\\\\\"\\\\n  stage1_steps: 10000\\\\n  stage2_steps: 0\\\\n  stage1_lr: 3.0e-4\\\\n  stage2_lr: 1.0e-4\\\\n  stage1_warmup_steps: 500\\\\n  stage2_warmup_steps: 0\\\\n  checkpoint_after_stage1: true\\\\n  stage1_freeze_backbone: true\\\\n  stage1_train_acis: true\\\\n  stage2_freeze_acis: true\\\\n  stage2_train_expert_only: true\\\\n\\\\ntraining:\\\\n  output_dir: \\\\\\\"checkpoints/libero_acis_stage1only_k07\\\\\\\"\\\\n  total_steps: 10000\\\\n  grad_clip: 10.0\\\\n  save_every: 5000\\\\n  eval_every: 999999\\\\n  log_every: 50\\\\n  batch_size: 4\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 12.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# ACIS Stage1-only: k=0.7 (retain 70% visual tokens)\\n# Freeze expert, train ACIS selector only, 10K steps.\\n# Purpose: SR vs compression ratio curve point (k=0.7)\\n\\n_base_: libero_baseline.yaml\\n\\nmodel:\\n  train_expert_only: true\\n  lora:\\n    rank: 0\\n\\nimm:\\n  enabled: true\\n  gradient_isolation: false\\n  lambda_margin: 1.0\\n  delta: 0.3\\n  k_ratio: 0.7\\n  temperature: 0.5\\n  soft_topk_method: \\\"sigmoid\\\"\\n  warmup_steps: 0\\n\\nacis:\\n  visual_dim: 960\\n  action_dim: 720\\n  num_heads: 8\\n  dropout: 0.0\\n\\ntwostage:\\n  train_mode: \\\"twostage_fullft\\\"\\n  baseline_checkpoint: \\\"checkpoints/libero_full_ft/step_099999/checkpoint.pt\\\"\\n  stage1_steps: 10000\\n  stage2_steps: 0\\n  stage1_lr: 3.0e-4\\n  stage2_lr: 1.0e-4\\n  stage1_warmup_steps: 500\\n  stage2_warmup_steps: 0\\n  checkpoint_after_stage1: true\\n  stage1_freeze_backbone: true\\n  stage1_train_acis: true\\n  stage2_freeze_acis: true\\n  stage2_train_expert_only: true\\n\\ntraining:\\n  output_dir: \\\"checkpoints/libero_acis_stage1only_k07\\\"\\n  total_steps: 10000\\n  grad_clip: 10.0\\n  save_every: 5000\\n  eval_every: 999999\\n  log_every: 50\\n  batch_size: 4\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.35}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-17T10:38:55.344Z_

<details><summary>↩ Tool result · `toolu_014fW5zNGYB4RntjTX6Z9njc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"322:def compute_k_ratio(step: int, config: Dict[str, Any]) -> Optional[float]:\\n323:    \\\"\\\"\\\"Compute dynamic k_ratio based on annealing schedule in config.\\\"\\\"\\\"\\n325:    schedule = imm_cfg.get(\\\"k_ratio_schedule\\\")\\n363:        \\\"k_ratio\\\": imm_cfg.get(\\\"k_ratio\\\", 0.5),\\n641:        # Dynamic k_ratio annealing\\n642:        if imm_enabled and hasattr(model, 'k_ratio'):\\n643:            new_k_ratio = compute_k_ratio(step, config)\\n644:            if new_k_ratio is not None:\\n645:                model.k_ratio = new_k_ratio\\n680:                if hasattr(model, 'k_ratio'):\\n681:                    log_dict[\\\"train/k_ratio\\\"] = model.k_ratio\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "8a1f419d-5daa-41d6-ba06-dd7af046928d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"322:def compute_k_ratio(step: int, config: Dict[str, Any]) -> Optional[float]:\\\\n323:    \\\\\\\"\\\\\\\"\\\\\\\"Compute dynamic k_ratio based on annealing schedule in config.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n325:    schedule = imm_cfg.get(\\\\\\\"k_ratio_schedule\\\\\\\")\\\\n363:        \\\\\\\"k_ratio\\\\\\\": imm_cfg.get(\\\\\\\"k_ratio\\\\\\\", 0.5),\\\\n641:        # Dynamic k_ratio annealing\\\\n642:        if imm_enabled and hasattr(model, 'k_ratio'):\\\\n643:            new_k_ratio = compute_k_ratio(step, config)\\\\n644:            if new_k_ratio is not None:\\\\n645:                model.k_ratio = new_k_ratio\\\\n680:                if hasattr(model, 'k_ratio'):\\\\n681:                    log_dict[\\\\\\\"train/k_ratio\\\\\\\"] = model.k_ratio\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.18}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"322:def compute_k_ratio(step: int, config: Dict[str, Any]) -> Optional[float]:\\n323:    \\\"\\\"\\\"Compute dynamic k_ratio based on annealing schedule in config.\\\"\\\"\\\"\\n325:    schedule = imm_cfg.get(\\\"k_ratio_schedule\\\")\\n363:        \\\"k_ratio\\\": imm_cfg.get(\\\"k_ratio\\\", 0.5),\\n641:        # Dynamic k_ratio annealing\\n642:        if imm_enabled and hasattr(model, 'k_ratio'):\\n643:            new_k_ratio = compute_k_ratio(step, config)\\n644:            if new_k_ratio is not None:\\n645:                model.k_ratio = new_k_ratio\\n680:                if hasattr(model, 'k_ratio'):\\n681:                    log_dict[\\\"train/k_ratio\\\"] = model.k_ratio\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Now I need to check the `wrap_with_imm` function to understand how the wrapper is constructed and how `k_ratio` gets set.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "9d83f964-5bc0-46d7-8adb-b2c3dff8f4db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BvFTheuurzcTK2VydmN1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 49696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1265
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

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Af9hqhf9bSLaUfc2YqxLMB`</summary>

```json
{
  "server": "westd-27271",
  "command": "head -n 400 /root/autodl-tmp/importance_margin_vla_compress/train.py",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "324010ce-3490-4bc1-981c-cf645415b307",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BvFTheuurzcTK2VydmN1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1265,
      "cache_read_input_tokens": 49696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1265
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

_source line 58 · 2026-05-17T10:39:00.857Z_

<details><summary>↩ Tool result · `toolu_01Af9hqhf9bSLaUfc2YqxLMB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"IMM Training Pipeline for SmolVLA + LIBERO.\\n\\nUsage:\\n    python train.py --config configs/baseline.yaml\\n    python train.py --config configs/imm_anchor.yaml\\n    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest\\n\\nTwo modes:\\n  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.\\n  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.\\n\\nDepends: lerobot, torch, wandb, peft.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport copy\\nimport json\\nimport logging\\nimport os\\nimport signal\\nimport sys\\nimport time\\nfrom pathlib import Path\\nfrom typing import Any, Dict, Optional\\n\\nimport torch\\nimport torch.nn.functional as F\\nimport wandb\\nimport yaml\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\n\\n\\ndef parse_args():\\n    parser = argparse.ArgumentParser(description=\\\"IMM training for SmolVLA on LIBERO\\\")\\n    parser.add_argument(\\\"--config\\\", type=str, required=True, help=\\\"Path to YAML config file\\\")\\n    parser.add_argument(\\\"--resume\\\", type=str, default=None, help=\\\"Path to checkpoint dir to resume from\\\")\\n    parser.add_argument(\\\"--gpu\\\", type=int, default=0, help=\\\"GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--wandb_project\\\", type=str, default=\\\"imm-vla-compress\\\", help=\\\"W&B project name\\\")\\n    parser.add_argument(\\\"--wandb_run\\\", type=str, default=None, help=\\\"W&B run name (auto-generated if None)\\\")\\n    return parser.parse_args()\\n\\n\\ndef load_config(config_path: str) -> Dict[str, Any]:\\n    \\\"\\\"\\\"Load YAML config with _base_ inheritance support.\\\"\\\"\\\"\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        base_config = deep_merge(base_config, config)\\n        return base_config\\n\\n    return config\\n\\n\\ndef deep_merge(base: Dict, override: Dict) -> Dict:\\n    \\\"\\\"\\\"Recursively merge override into base.\\\"\\\"\\\"\\n    result = copy.deepcopy(base)\\n    for k, v in override.items():\\n        if k in result and isinstance(result[k], dict) and isinstance(v, dict):\\n            result[k] = deep_merge(result[k], v)\\n        else:\\n            result[k] = copy.deepcopy(v)\\n    return result\\n\\n\\ndef set_seed(seed: int):\\n    import random\\n    import numpy as np\\n\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    if torch.cuda.is_available():\\n        torch.cuda.manual_seed_all(seed)\\n\\n\\ndef _adapt_projections(policy, features: Dict[str, Any]):\\n    \\\"\\\"\\\"Update SmolVLAConfig features for target dataset dimensions.\\\"\\\"\\\"\\n    from lerobot.configs.types import FeatureType, PolicyFeature\\n\\n    state_dim = features.get(\\\"state_dim\\\")\\n    action_dim = features.get(\\\"action_dim\\\")\\n    cameras = features.get(\\\"cameras\\\")\\n\\n    if state_dim is not None:\\n        old_shape = None\\n        if policy.config.input_features and \\\"observation.state\\\" in policy.config.input_features:\\n            old_shape = policy.config.input_features[\\\"observation.state\\\"].shape\\n        policy.config.input_features[\\\"observation.state\\\"] = PolicyFeature(\\n            type=FeatureType.STATE, shape=(state_dim,)\\n        )\\n        log.info(\\\"Updated state feature shape: %s -> (%d,)\\\", old_shape, state_dim)\\n\\n    if action_dim is not None:\\n        old_shape = None\\n        if policy.config.output_features and \\\"action\\\" in policy.config.output_features:\\n            old_shape = policy.config.output_features[\\\"action\\\"].shape\\n        policy.config.output_features[\\\"action\\\"] = PolicyFeature(\\n            type=FeatureType.ACTION, shape=(action_dim,)\\n        )\\n        log.info(\\\"Updated action feature shape: %s -> (%d,)\\\", old_shape, action_dim)\\n\\n    if cameras is not None:\\n        imag\\n\\n... [截断: 输出过长，省略 6281 字符] ...\\n\\ns\\\"] = torch.ones(B, 1, dtype=torch.long)\\n        batch[\\\"observation.language.attention_mask\\\"] = torch.ones(B, 1, dtype=torch.bool)\\n\\n    for key in list(batch.keys()):\\n        if not isinstance(batch[key], torch.Tensor):\\n            del batch[key]\\n\\n    if device is not None:\\n        batch = {k: v.to(device) for k, v in batch.items()}\\n\\n    return batch\\n\\n\\n\\ndef baseline_forward(policy, batch):\\n    \\\"\\\"\\\"Baseline forward: flow matching loss without action_is_pad masking.\\n\\n    Bypasses SmolVLAPolicy.forward() which dilutes loss via pad masking.\\n    Uses the same approach as IMMSmolVLAWrapper.forward() for consistency.\\n    \\\"\\\"\\\"\\n    from lerobot.utils.constants import OBS_LANGUAGE_TOKENS, OBS_LANGUAGE_ATTENTION_MASK\\n\\n    images, img_masks = policy.prepare_images(batch)\\n    state = policy.prepare_state(batch)\\n    lang_tokens = batch[OBS_LANGUAGE_TOKENS]\\n    lang_masks = batch[OBS_LANGUAGE_ATTENTION_MASK]\\n    actions = policy.prepare_action(batch)\\n\\n    losses = policy.model.forward(\\n        images, img_masks, lang_tokens, lang_masks, state, actions, None, None\\n    )\\n\\n    action_dim = policy.config.action_feature.shape[0]\\n    loss = losses[:, :, :action_dim].mean()\\n    return loss, {\\\"action_loss\\\": loss.detach()}\\n\\n\\n\\n\\ndef compute_k_ratio(step: int, config: Dict[str, Any]) -> Optional[float]:\\n    \\\"\\\"\\\"Compute dynamic k_ratio based on annealing schedule in config.\\\"\\\"\\\"\\n    imm_cfg = config.get(\\\"imm\\\", {})\\n    schedule = imm_cfg.get(\\\"k_ratio_schedule\\\")\\n    if schedule is None:\\n        return None\\n\\n    start = schedule[\\\"start\\\"]\\n    end = schedule[\\\"end\\\"]\\n    warmup_steps = schedule.get(\\\"warmup_steps\\\", 0)\\n    anneal_steps = schedule.get(\\\"anneal_steps\\\", 20000)\\n\\n    if step < warmup_steps:\\n        return start\\n\\n    anneal_progress = min(1.0, (step - warmup_steps) / anneal_steps)\\n\\n    sched_type = schedule.get(\\\"type\\\", \\\"linear\\\")\\n    if sched_type == \\\"cosine\\\":\\n        import math as _math\\n        ratio = start + (end - start) * (1 - _math.cos(_math.pi * anneal_progress)) / 2\\n    else:  # linear\\n        ratio = start + (end - start) * anneal_progress\\n\\n    return ratio\\n\\n\\ndef wrap_with_imm(policy, config: Dict[str, Any]):\\n    \\\"\\\"\\\"Wrap SmolVLAPolicy.model with IMMSmolVLAWrapper.\\\"\\\"\\\"\\n    sys.path.insert(0, str(ARTIFACTS_DIR))\\n    from imm.smolvla_wrapper import IMMSmolVLAWrapper\\n\\n    imm_cfg = config[\\\"imm\\\"]\\n    acis_cfg = config.get(\\\"acis\\\", {})\\n\\n    imm_kwargs = {\\n        \\\"lambda_margin\\\": imm_cfg.get(\\\"lambda_margin\\\", 0.1),\\n        \\\"delta\\\": imm_cfg.get(\\\"delta\\\", 1.0),\\n        \\\"warmup_steps\\\": imm_cfg.get(\\\"warmup_steps\\\", 1000),\\n        \\\"temperature\\\": imm_cfg.get(\\\"temperature\\\", 1.0),\\n        \\\"method\\\": imm_cfg.get(\\\"soft_topk_method\\\", \\\"sigmoid\\\"),\\n        \\\"k_ratio\\\": imm_cfg.get(\\\"k_ratio\\\", 0.5),\\n        \\\"gradient_isolation\\\": imm_cfg.get(\\\"gradient_isolation\\\", False),\\n    }\\n\\n    wrapper = IMMSmolVLAWrapper(\\n        smolvla_policy=policy,\\n        acis_config=acis_cfg,\\n        imm_config=imm_kwargs,\\n    )\\n    return wrapper\\n\\n\\ndef setup_twostage(model, config, device):\\n    \\\"\\\"\\\"Load baseline LoRA weights and freeze everything except ACIS for two-stage Stage 1.\\\"\\\"\\\"\\n    ts_cfg = config[\\\"twostage\\\"]\\n    baseline_ckpt = ts_cfg.get(\\\"baseline_checkpoint\\\", \\\"checkpoints/baseline/step_029999/checkpoint.pt\\\")\\n\\n    ckpt_path = Path(baseline_ckpt)\\n    if not ckpt_path.is_absolute():\\n        ckpt_path = ARTIFACTS_DIR / ckpt_path\\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\\n    model.policy.load_state_dict(ckpt[\\\"model_state_dict\\\"])\\n    log.info(\\\"Loaded baseline LoRA weights from %s (step %d)\\\", ckpt_path, ckpt.get(\\\"step\\\", -1))\\n\\n    acis_param_ids = {id(p) for p in model.acis.parameters()}\\n    n_frozen = 0\\n    n_trainable = 0\\n    for name, param in model.named_parameters():\\n        if id(param) in acis_param_ids:\\n            param.requires_grad = True\\n            n_trainable += param.numel()\\n        else:\\n            param.requires_grad = False\\n            n_frozen += param.numel()\\n\\n    log.info(\\\"Two-stage Stage 1: frozen=%d, trainable(ACIS)=%d\\\", n_frozen, n_trainable)\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.22}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "8e239027-edb2-4f40-b1e5-d7f6a64be471",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"IMM Training Pipeline for SmolVLA + LIBERO.\\\\n\\\\nUsage:\\\\n    python train.py --config configs/baseline.yaml\\\\n    python train.py --config configs/imm_anchor.yaml\\\\n    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest\\\\n\\\\nTwo modes:\\\\n  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.\\\\n  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.\\\\n\\\\nDepends: lerobot, torch, wandb, peft.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport copy\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport signal\\\\nimport sys\\\\nimport time\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, Optional\\\\n\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nimport wandb\\\\nimport yaml\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\\\n\\\\n\\\\ndef parse_args():\\\\n    parser = argparse.ArgumentParser(description=\\\\\\\"IMM training for SmolVLA on LIBERO\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--config\\\\\\\", type=str, required=True, help=\\\\\\\"Path to YAML config file\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--resume\\\\\\\", type=str, default=None, help=\\\\\\\"Path to checkpoint dir to resume from\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0, help=\\\\\\\"GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42, help=\\\\\\\"Random seed\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--wandb_project\\\\\\\", type=str, default=\\\\\\\"imm-vla-compress\\\\\\\", help=\\\\\\\"W&B project name\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--wandb_run\\\\\\\", type=str, default=None, help=\\\\\\\"W&B run name (auto-generated if None)\\\\\\\")\\\\n    return parser.parse_args()\\\\n\\\\n\\\\ndef load_config(config_path: str) -> Dict[str, Any]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load YAML config with _base_ inheritance support.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    config_path = Path(config_path)\\\\n    with open(config_path) as f:\\\\n        config = yaml.safe_load(f)\\\\n\\\\n    if \\\\\\\"_base_\\\\\\\" in config:\\\\n        base_path = config_path.parent / config.pop(\\\\\\\"_base_\\\\\\\")\\\\n        base_config = load_config(str(base_path))\\\\n        base_config = deep_merge(base_config, config)\\\\n        return base_config\\\\n\\\\n    return config\\\\n\\\\n\\\\ndef deep_merge(base: Dict, override: Dict) -> Dict:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Recursively merge override into base.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    result = copy.deepcopy(base)\\\\n    for k, v in override.items():\\\\n        if k in result and isinstance(result[k], dict) and isinstance(v, dict):\\\\n            result[k] = deep_merge(result[k], v)\\\\n        else:\\\\n            result[k] = copy.deepcopy(v)\\\\n    return result\\\\n\\\\n\\\\ndef set_seed(seed: int):\\\\n    import random\\\\n    import numpy as np\\\\n\\\\n    random.seed(seed)\\\\n    np.random.seed(seed)\\\\n    torch.manual_seed(seed)\\\\n    if torch.cuda.is_available():\\\\n        torch.cuda.manual_seed_all(seed)\\\\n\\\\n\\\\ndef _adapt_projections(policy, features: Dict[str, Any]):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Update SmolVLAConfig features for target dataset dimensions.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    from lerobot.configs.types import FeatureType, PolicyFeature\\\\n\\\\n    state_dim = features.get(\\\\\\\"state_dim\\\\\\\")\\\\n    action_dim = features.get(\\\\\\\"action_dim\\\\\\\")\\\\n    cameras = features.get(\\\\\\\"cameras\\\\\\\")\\\\n\\\\n    if state_dim is not None:\\\\n        old_shape = None\\\\n        if policy.config.input_features and \\\\\\\"observation.state\\\\\\\" in policy.config.input_features:\\\\n            old_shape = policy.config.input_features[\\\\\\\"observation.state\\\\\\\"].shape\\\\n        policy.config.input_features[\\\\\\\"observation.state\\\\\\\"] = PolicyFeature(\\\\n            type=FeatureType.STATE, shape=(state_dim,)\\\\n        )\\\\n        log.info(\\\\\\\"Updated state feature shape: %s -> (%d,)\\\\\\\", old_shape, state_dim)\\\\n\\\\n    if action_dim is not None:\\\\n        old_shape = None\\\\n        if policy.config.output_features and \\\\\\\"action\\\\\\\" in policy.config.output_features:\\\\n            old_shape = policy.config.output_features[\\\\\\\"action\\\\\\\"].shape\\\\n        policy.config.output_features[\\\\\\\"action\\\\\\\"] = PolicyFeature(\\\\n            type=FeatureType.ACTION, shape=(action_dim,)\\\\n        )\\\\n        log.info(\\\\\\\"Updated action feature shape: %s -> (%d,)\\\\\\\", old_shape, action_dim)\\\\n\\\\n    if cameras is not None:\\\\n        imag\\\\n\\\\n... [截断: 输出过长，省略 6281 字符] ...\\\\n\\\\ns\\\\\\\"] = torch.ones(B, 1, dtype=torch.long)\\\\n        batch[\\\\\\\"observation.language.attention_mask\\\\\\\"] = torch.ones(B, 1, dtype=torch.bool)\\\\n\\\\n    for key in list(batch.keys()):\\\\n        if not isinstance(batch[key], torch.Tensor):\\\\n            del batch[key]\\\\n\\\\n    if device is not None:\\\\n        batch = {k: v.to(device) for k, v in batch.items()}\\\\n\\\\n    return batch\\\\n\\\\n\\\\n\\\\ndef baseline_forward(policy, batch):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Baseline forward: flow matching loss without action_is_pad masking.\\\\n\\\\n    Bypasses SmolVLAPolicy.forward() which dilutes loss via pad masking.\\\\n    Uses the same approach as IMMSmolVLAWrapper.forward() for consistency.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    from lerobot.utils.constants import OBS_LANGUAGE_TOKENS, OBS_LANGUAGE_ATTENTION_MASK\\\\n\\\\n    images, img_masks = policy.prepare_images(batch)\\\\n    state = policy.prepare_state(batch)\\\\n    lang_tokens = batch[OBS_LANGUAGE_TOKENS]\\\\n    lang_masks = batch[OBS_LANGUAGE_ATTENTION_MASK]\\\\n    actions = policy.prepare_action(batch)\\\\n\\\\n    losses = policy.model.forward(\\\\n        images, img_masks, lang_tokens, lang_masks, state, actions, None, None\\\\n    )\\\\n\\\\n    action_dim = policy.config.action_feature.shape[0]\\\\n    loss = losses[:, :, :action_dim].mean()\\\\n    return loss, {\\\\\\\"action_loss\\\\\\\": loss.detach()}\\\\n\\\\n\\\\n\\\\n\\\\ndef compute_k_ratio(step: int, config: Dict[str, Any]) -> Optional[float]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute dynamic k_ratio based on annealing schedule in config.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    imm_cfg = config.get(\\\\\\\"imm\\\\\\\", {})\\\\n    schedule = imm_cfg.get(\\\\\\\"k_ratio_schedule\\\\\\\")\\\\n    if schedule is None:\\\\n        return None\\\\n\\\\n    start = schedule[\\\\\\\"start\\\\\\\"]\\\\n    end = schedule[\\\\\\\"end\\\\\\\"]\\\\n    warmup_steps = schedule.get(\\\\\\\"warmup_steps\\\\\\\", 0)\\\\n    anneal_steps = schedule.get(\\\\\\\"anneal_steps\\\\\\\", 20000)\\\\n\\\\n    if step < warmup_steps:\\\\n        return start\\\\n\\\\n    anneal_progress = min(1.0, (step - warmup_steps) / anneal_steps)\\\\n\\\\n    sched_type = schedule.get(\\\\\\\"type\\\\\\\", \\\\\\\"linear\\\\\\\")\\\\n    if sched_type == \\\\\\\"cosine\\\\\\\":\\\\n        import math as _math\\\\n        ratio = start + (end - start) * (1 - _math.cos(_math.pi * anneal_progress)) / 2\\\\n    else:  # linear\\\\n        ratio = start + (end - start) * anneal_progress\\\\n\\\\n    return ratio\\\\n\\\\n\\\\ndef wrap_with_imm(policy, config: Dict[str, Any]):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Wrap SmolVLAPolicy.model with IMMSmolVLAWrapper.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    sys.path.insert(0, str(ARTIFACTS_DIR))\\\\n    from imm.smolvla_wrapper import IMMSmolVLAWrapper\\\\n\\\\n    imm_cfg = config[\\\\\\\"imm\\\\\\\"]\\\\n    acis_cfg = config.get(\\\\\\\"acis\\\\\\\", {})\\\\n\\\\n    imm_kwargs = {\\\\n        \\\\\\\"lambda_margin\\\\\\\": imm_cfg.get(\\\\\\\"lambda_margin\\\\\\\", 0.1),\\\\n        \\\\\\\"delta\\\\\\\": imm_cfg.get(\\\\\\\"delta\\\\\\\", 1.0),\\\\n        \\\\\\\"warmup_steps\\\\\\\": imm_cfg.get(\\\\\\\"warmup_steps\\\\\\\", 1000),\\\\n        \\\\\\\"temperature\\\\\\\": imm_cfg.get(\\\\\\\"temperature\\\\\\\", 1.0),\\\\n        \\\\\\\"method\\\\\\\": imm_cfg.get(\\\\\\\"soft_topk_method\\\\\\\", \\\\\\\"sigmoid\\\\\\\"),\\\\n        \\\\\\\"k_ratio\\\\\\\": imm_cfg.get(\\\\\\\"k_ratio\\\\\\\", 0.5),\\\\n        \\\\\\\"gradient_isolation\\\\\\\": imm_cfg.get(\\\\\\\"gradient_isolation\\\\\\\", False),\\\\n    }\\\\n\\\\n    wrapper = IMMSmolVLAWrapper(\\\\n        smolvla_policy=policy,\\\\n        acis_config=acis_cfg,\\\\n        imm_config=imm_kwargs,\\\\n    )\\\\n    return wrapper\\\\n\\\\n\\\\ndef setup_twostage(model, config, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load baseline LoRA weights and freeze everything except ACIS for two-stage Stage 1.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ts_cfg = config[\\\\\\\"twostage\\\\\\\"]\\\\n    baseline_ckpt = ts_cfg.get(\\\\\\\"baseline_checkpoint\\\\\\\", \\\\\\\"checkpoints/baseline/step_029999/checkpoint.pt\\\\\\\")\\\\n\\\\n    ckpt_path = Path(baseline_ckpt)\\\\n    if not ckpt_path.is_absolute():\\\\n        ckpt_path = ARTIFACTS_DIR / ckpt_path\\\\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\\\\n    model.policy.load_state_dict(ckpt[\\\\\\\"model_state_dict\\\\\\\"])\\\\n    log.info(\\\\\\\"Loaded baseline LoRA weights from %s (step %d)\\\\\\\", ckpt_path, ckpt.get(\\\\\\\"step\\\\\\\", -1))\\\\n\\\\n    acis_param_ids = {id(p) for p in model.acis.parameters()}\\\\n    n_frozen = 0\\\\n    n_trainable = 0\\\\n    for name, param in model.named_parameters():\\\\n        if id(param) in acis_param_ids:\\\\n            param.requires_grad = True\\\\n            n_trainable += param.numel()\\\\n        else:\\\\n            param.requires_grad = False\\\\n            n_frozen += param.numel()\\\\n\\\\n    log.info(\\\\\\\"Two-stage Stage 1: frozen=%d, trainable(ACIS)=%d\\\\\\\", n_frozen, n_trainable)\\\\n\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.22}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"IMM Training Pipeline for SmolVLA + LIBERO.\\n\\nUsage:\\n    python train.py --config configs/baseline.yaml\\n    python train.py --config configs/imm_anchor.yaml\\n    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest\\n\\nTwo modes:\\n  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.\\n  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.\\n\\nDepends: lerobot, torch, wandb, peft.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport copy\\nimport json\\nimport logging\\nimport os\\nimport signal\\nimport sys\\nimport time\\nfrom pathlib import Path\\nfrom typing import Any, Dict, Optional\\n\\nimport torch\\nimport torch.nn.functional as F\\nimport wandb\\nimport yaml\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nARTIFACTS_DIR = Path(__file__).resolve().parent\\n\\n\\ndef parse_args():\\n    parser = argparse.ArgumentParser(description=\\\"IMM training for SmolVLA on LIBERO\\\")\\n    parser.add_argument(\\\"--config\\\", type=str, required=True, help=\\\"Path to YAML config file\\\")\\n    parser.add_argument(\\\"--resume\\\", type=str, default=None, help=\\\"Path to checkpoint dir to resume from\\\")\\n    parser.add_argument(\\\"--gpu\\\", type=int, default=0, help=\\\"GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, default=42, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--wandb_project\\\", type=str, default=\\\"imm-vla-compress\\\", help=\\\"W&B project name\\\")\\n    parser.add_argument(\\\"--wandb_run\\\", type=str, default=None, help=\\\"W&B run name (auto-generated if None)\\\")\\n    return parser.parse_args()\\n\\n\\ndef load_config(config_path: str) -> Dict[str, Any]:\\n    \\\"\\\"\\\"Load YAML config with _base_ inheritance support.\\\"\\\"\\\"\\n    config_path = Path(config_path)\\n    with open(config_path) as f:\\n        config = yaml.safe_load(f)\\n\\n    if \\\"_base_\\\" in config:\\n        base_path = config_path.parent / config.pop(\\\"_base_\\\")\\n        base_config = load_config(str(base_path))\\n        base_config = deep_merge(base_config, config)\\n        return base_config\\n\\n    return config\\n\\n\\ndef deep_merge(base: Dict, override: Dict) -> Dict:\\n    \\\"\\\"\\\"Recursively merge override into base.\\\"\\\"\\\"\\n    result = copy.deepcopy(base)\\n    for k, v in override.items():\\n        if k in result and isinstance(result[k], dict) and isinstance(v, dict):\\n            result[k] = deep_merge(result[k], v)\\n        else:\\n            result[k] = copy.deepcopy(v)\\n    return result\\n\\n\\ndef set_seed(seed: int):\\n    import random\\n    import numpy as np\\n\\n    random.seed(seed)\\n    np.random.seed(seed)\\n    torch.manual_seed(seed)\\n    if torch.cuda.is_available():\\n        torch.cuda.manual_seed_all(seed)\\n\\n\\ndef _adapt_projections(policy, features: Dict[str, Any]):\\n    \\\"\\\"\\\"Update SmolVLAConfig features for target dataset dimensions.\\\"\\\"\\\"\\n    from lerobot.configs.types import FeatureType, PolicyFeature\\n\\n    state_dim = features.get(\\\"state_dim\\\")\\n    action_dim = features.get(\\\"action_dim\\\")\\n    cameras = features.get(\\\"cameras\\\")\\n\\n    if state_dim is not None:\\n        old_shape = None\\n        if policy.config.input_features and \\\"observation.state\\\" in policy.config.input_features:\\n            old_shape = policy.config.input_features[\\\"observation.state\\\"].shape\\n        policy.config.input_features[\\\"observation.state\\\"] = PolicyFeature(\\n            type=FeatureType.STATE, shape=(state_dim,)\\n        )\\n        log.info(\\\"Updated state feature shape: %s -> (%d,)\\\", old_shape, state_dim)\\n\\n    if action_dim is not None:\\n        old_shape = None\\n        if policy.config.output_features and \\\"action\\\" in policy.config.output_features:\\n            old_shape = policy.config.output_features[\\\"action\\\"].shape\\n        policy.config.output_features[\\\"action\\\"] = PolicyFeature(\\n            type=FeatureType.ACTION, shape=(action_dim,)\\n        )\\n        log.info(\\\"Updated action feature shape: %s -> (%d,)\\\", old_shape, action_dim)\\n\\n    if cameras is not None:\\n        imag\\n\\n... [截断: 输出过长，省略 6281 字符] ...\\n\\ns\\\"] = torch.ones(B, 1, dtype=torch.long)\\n        batch[\\\"observation.language.attention_mask\\\"] = torch.ones(B, 1, dtype=torch.bool)\\n\\n    for key in list(batch.keys()):\\n        if not isinstance(batch[key], torch.Tensor):\\n            del batch[key]\\n\\n    if device is not None:\\n        batch = {k: v.to(device) for k, v in batch.items()}\\n\\n    return batch\\n\\n\\n\\ndef baseline_forward(policy, batch):\\n    \\\"\\\"\\\"Baseline forward: flow matching loss without action_is_pad masking.\\n\\n    Bypasses SmolVLAPolicy.forward() which dilutes loss via pad masking.\\n    Uses the same approach as IMMSmolVLAWrapper.forward() for consistency.\\n    \\\"\\\"\\\"\\n    from lerobot.utils.constants import OBS_LANGUAGE_TOKENS, OBS_LANGUAGE_ATTENTION_MASK\\n\\n    images, img_masks = policy.prepare_images(batch)\\n    state = policy.prepare_state(batch)\\n    lang_tokens = batch[OBS_LANGUAGE_TOKENS]\\n    lang_masks = batch[OBS_LANGUAGE_ATTENTION_MASK]\\n    actions = policy.prepare_action(batch)\\n\\n    losses = policy.model.forward(\\n        images, img_masks, lang_tokens, lang_masks, state, actions, None, None\\n    )\\n\\n    action_dim = policy.config.action_feature.shape[0]\\n    loss = losses[:, :, :action_dim].mean()\\n    return loss, {\\\"action_loss\\\": loss.detach()}\\n\\n\\n\\n\\ndef compute_k_ratio(step: int, config: Dict[str, Any]) -> Optional[float]:\\n    \\\"\\\"\\\"Compute dynamic k_ratio based on annealing schedule in config.\\\"\\\"\\\"\\n    imm_cfg = config.get(\\\"imm\\\", {})\\n    schedule = imm_cfg.get(\\\"k_ratio_schedule\\\")\\n    if schedule is None:\\n        return None\\n\\n    start = schedule[\\\"start\\\"]\\n    end = schedule[\\\"end\\\"]\\n    warmup_steps = schedule.get(\\\"warmup_steps\\\", 0)\\n    anneal_steps = schedule.get(\\\"anneal_steps\\\", 20000)\\n\\n    if step < warmup_steps:\\n        return start\\n\\n    anneal_progress = min(1.0, (step - warmup_steps) / anneal_steps)\\n\\n    sched_type = schedule.get(\\\"type\\\", \\\"linear\\\")\\n    if sched_type == \\\"cosine\\\":\\n        import math as _math\\n        ratio = start + (end - start) * (1 - _math.cos(_math.pi * anneal_progress)) / 2\\n    else:  # linear\\n        ratio = start + (end - start) * anneal_progress\\n\\n    return ratio\\n\\n\\ndef wrap_with_imm(policy, config: Dict[str, Any]):\\n    \\\"\\\"\\\"Wrap SmolVLAPolicy.model with IMMSmolVLAWrapper.\\\"\\\"\\\"\\n    sys.path.insert(0, str(ARTIFACTS_DIR))\\n    from imm.smolvla_wrapper import IMMSmolVLAWrapper\\n\\n    imm_cfg = config[\\\"imm\\\"]\\n    acis_cfg = config.get(\\\"acis\\\", {})\\n\\n    imm_kwargs = {\\n        \\\"lambda_margin\\\": imm_cfg.get(\\\"lambda_margin\\\", 0.1),\\n        \\\"delta\\\": imm_cfg.get(\\\"delta\\\", 1.0),\\n        \\\"warmup_steps\\\": imm_cfg.get(\\\"warmup_steps\\\", 1000),\\n        \\\"temperature\\\": imm_cfg.get(\\\"temperature\\\", 1.0),\\n        \\\"method\\\": imm_cfg.get(\\\"soft_topk_method\\\", \\\"sigmoid\\\"),\\n        \\\"k_ratio\\\": imm_cfg.get(\\\"k_ratio\\\", 0.5),\\n        \\\"gradient_isolation\\\": imm_cfg.get(\\\"gradient_isolation\\\", False),\\n    }\\n\\n    wrapper = IMMSmolVLAWrapper(\\n        smolvla_policy=policy,\\n        acis_config=acis_cfg,\\n        imm_config=imm_kwargs,\\n    )\\n    return wrapper\\n\\n\\ndef setup_twostage(model, config, device):\\n    \\\"\\\"\\\"Load baseline LoRA weights and freeze everything except ACIS for two-stage Stage 1.\\\"\\\"\\\"\\n    ts_cfg = config[\\\"twostage\\\"]\\n    baseline_ckpt = ts_cfg.get(\\\"baseline_checkpoint\\\", \\\"checkpoints/baseline/step_029999/checkpoint.pt\\\")\\n\\n    ckpt_path = Path(baseline_ckpt)\\n    if not ckpt_path.is_absolute():\\n        ckpt_path = ARTIFACTS_DIR / ckpt_path\\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\\n    model.policy.load_state_dict(ckpt[\\\"model_state_dict\\\"])\\n    log.info(\\\"Loaded baseline LoRA weights from %s (step %d)\\\", ckpt_path, ckpt.get(\\\"step\\\", -1))\\n\\n    acis_param_ids = {id(p) for p in model.acis.parameters()}\\n    n_frozen = 0\\n    n_trainable = 0\\n    for name, param in model.named_parameters():\\n        if id(param) in acis_param_ids:\\n            param.requires_grad = True\\n            n_trainable += param.numel()\\n        else:\\n            param.requires_grad = False\\n            n_frozen += param.numel()\\n\\n    log.info(\\\"Two-stage Stage 1: frozen=%d, trainable(ACIS)=%d\\\", n_frozen, n_trainable)\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.22}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

Now I have everything. Let me also check if k=0.5 configs exist (since the user mentioned preferring k=0.5 if available).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "a035340f-0ae8-44db-bfc6-578d49c9e4cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fSbxjwR9yYxz8s4efdAnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3463,
      "cache_read_input_tokens": 50961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3463
      },
      "output_tokens": 2,
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

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TRQP6a2w56rr9wCfBnS7CY`</summary>

```json
{
  "server": "westd-27271",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "e4a27605-3e4d-43b8-8ea7-8f23aeea7dd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fSbxjwR9yYxz8s4efdAnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3463,
      "cache_read_input_tokens": 50961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3463
      },
      "output_tokens": 2,
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

_source line 61 · 2026-05-17T10:39:08.429Z_

<details><summary>↩ Tool result · `toolu_01TRQP6a2w56rr9wCfBnS7CY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "e6f50740-e485-47e2-a45c-2a0b82617d9e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
No k=0.5 checkpoint exists. Only k=0.3 and k=0.7. The user specified to use k=0.7 checkpoint with k=0.5 pruning ratio. Let me re-read the instructions:

> - **两个 run 都用**: `checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt`
>   （或如果存在 k=0.5 版本：`checkpoints/libero_acis_stage1only/stage1_done/checkpoint.pt`，先 `ls checkpoints/libero_acis_stage1only*/` 确认）


>
> - **ACIS run**: prune mode（k=0.5, true_removal）

So I should use the k=0.7 checkpoint for both runs, but apply k=0.5 as the pruning ratio during evaluation—the checkpoint was trained with k=0.7, but we're testing the pruning hook at k=0.5.

For the v2 script, I need to load both models from the same checkpoint at `checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt` and configure the pruning wrapper to override the keep ratio to 0.5. For the ACIS variant, I'll load the same checkpoint with the wrapper but this time register the pruning hook at inference with true_removal and k=0.5, making sure to use the eval script's version of the hook registration since it properly handles the true_removal mode. Now I'm writing out the complete script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "73600920-b244-46a1-bf06-bce237792f51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTUDrSRQf1y34M1uQ5iB4T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 294
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

_source line 63_

Available checkpoints: k=0.3 and k=0.7 (no k=0.5). Will use the k=0.7 checkpoint for both runs as specified, with k=0.5 pruning ratio at inference.

Now writing the v2 script locally, then uploading.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "1b732c4d-f098-45a1-be7f-1e119a981704",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTUDrSRQf1y34M1uQ5iB4T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 294
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

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01HKZ4F8Z2W1qTKS6ExtEpgq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/analyze_action_divergence.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "147ab1b3-4386-4d16-8763-537fcd63bb8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTUDrSRQf1y34M1uQ5iB4T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 294
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

_source line 65 · 2026-05-17T10:39:33.743Z_

<details><summary>↩ Tool result · `toolu_01HKZ4F8Z2W1qTKS6ExtEpgq`</summary>

```text
1	"""Per-step Action Divergence Analysis: Baseline vs ACIS-pruned model.
2	
3	Drives the environment with baseline actions while recording both models'
4	action outputs at each timestep (same observation). Produces divergence curves
5	and per-dimension breakdown.
6	
7	Usage:
8	    python analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2
9	"""
10	
11	from __future__ import annotations
12	
13	import argparse
14	import json
15	import logging
16	import os
17	import sys
18	import time as time_mod
19	from pathlib import Path
20	
21	os.environ.setdefault("MUJOCO_GL", "egl")
22	os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
23	os.environ.setdefault("HF_HUB_OFFLINE", "1")
24	
25	import matplotlib
26	matplotlib.use("Agg")
27	import matplotlib.pyplot as plt
28	import numpy as np
29	import torch
30	
31	ARTIFACTS_DIR = Path(__file__).resolve().parent
32	sys.path.insert(0, str(ARTIFACTS_DIR))
33	
34	logging.basicConfig(
35	    level=logging.INFO,
36	    format="%(asctime)s [%(levelname)s] %(message)s",
37	    datefmt="%Y-%m-%d %H:%M:%S",
38	)
39	log = logging.getLogger(__name__)
40	
41	# Paths
42	BASELINE_CKPT = "checkpoints/libero_full_ft_100k/checkpoint.pt"
43	ACIS_CKPT = "checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt"
44	BASELINE_CONFIG = "configs/libero_baseline.yaml"
45	ACIS_CONFIG = "configs/libero_acis_stage1only_k07.yaml"
46	
47	SUITE = "libero_object"
48	MAX_STEPS = 280
49	ACTION_HORIZON = 50
50	ACTION_DIM_NAMES = ["pos_x", "pos_y", "pos_z", "rot_x", "rot_y", "rot_z", "gripper"]
51	
52	
53	def parse_args():
54	    p = argparse.ArgumentParser()
55	    p.add_argument("--gpu", type=int, default=2)
56	    p.add_argument("--num_episodes", type=int, default=5)
57	    p.add_argument("--task_ids", type=str, default="0,1,2")
58	    p.add_argument("--seed", type=int, default=42)
59	    p.add_argument("--output_dir", type=str, default="artifacts")
60	    return p.parse_args()
61	
62	
63	def load_config(config_path: str) -> dict:
64	    import copy
65	    import yaml
66	    config_path = Path(config_path)
67	    with open(config_path) as f:
68	        config = yaml.safe_load(f)
69	    if "_base_" in config:
70	        base_path = config_path.parent / config.pop("_base_")
71	        base_config = load_config(str(base_path))
72	        for k, v in config.items():
73	            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):
74	                base_config[k].update(v)
75	            else:
76	                base_config[k] = v
77	        return base_config
78	    return config
79	
80	
81	def load_baseline_model(device):
82	    from train import load_smolvla_policy
83	    config = load_config(BASELINE_CONFIG)
84	    policy = load_smolvla_policy(config, device)
85	    ckpt = torch.load(BASELINE_CKPT, map_location=device, weights_only=False)
86	    policy.load_state_dict(ckpt["model_state_dict"], strict=False)
87	    policy.eval()
88	    return policy, config
89	
90	
91	def load_acis_model(device):
92	    from train import load_smolvla_policy, wrap_with_imm
93	    config = load_config(ACIS_CONFIG)
94	    policy = load_smolvla_policy(config, device)
95	    wrapper = wrap_with_imm(policy, config)
96	    wrapper.to(device)
97	    ckpt = torch.load(ACIS_CKPT, map_location=device, weights_only=False)
98	    wrapper.load_state_dict(ckpt["model_state_dict"], strict=False)
99	    wrapper.eval()
100	    return wrapper.policy, wrapper, config
101	
102	
103	# --- Observation / Action utilities (from eval_success_rate_libero.py) ---
104	
105	def quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:
106	    q = quat.astype(np.float64)
107	    w = np.clip(q[3], -1.0, 1.0)
108	    den = np.sqrt(max(1.0 - w * w, 0.0))
109	    if den > 1e-10:
110	        angle = 2.0 * np.arccos(w)
111	        axis = q[:3] / den
112	        return (axis * angle).astype(np.float32)
113	    return np.zeros(3, dtype=np.float32)
114	
115	
116	def extract_state(obs: dict) -> np.ndarray:
117	    rs = obs["robot_state"]
118	    eef_pos = np.asarray(rs["eef"]["pos"], dtype=np.float32)
119	    eef_quat = np.asarray(rs["eef"]["quat"], dtype=np.float64)
120	    gripper_qpos = np.asarray(rs["gripper"]["qpos"], dtype=np.float32)
121	    eef_aa = quat_to_axis_angle(eef_quat)
122	    return np.concatenate([eef_pos, eef_aa, gripper_qpos])
123	
124	
125	def obs_to_batch(obs, task_text, tokenizer, camera_keys, device):
126	    batch = {}
127	    for cam_key in camera_keys:
128	        short_name = cam_key.split(".")[-1]
129	        img = obs["pixels"][short_name]
130	        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0
131	        img_t = img_t.unsqueeze(0)
132	        img_t = torch.flip(img_t, dims=[2, 3])
133	        batch[cam_key] = img_t.to(device)
134	    state = extract_state(obs)
135	    batch["observation.state"] = torch.from_numpy(state).unsqueeze(0).to(device)
136	    text = task_text if task_text.endswith("\n") else task_text + "\n"
137	    encoded = tokenizer(
138	        [text], padding="longest", max_length=48, truncation=True, return_tensors="pt",
139	    )
140	    batch["observation.language.tokens"] = encoded["input_ids"].to(device)
141	    batch["observation.language.attention_mask"] = encoded["attention_mask"].bool().to(device)
142	    return batch
143	
144	
145	def find_connector(model):
146	    for name, module in model.named_modules():
147	        if name.endswith(".connector") or "multi_modal_projector" in name:
148	            return module
149	    return None
150	
151	
152	@torch.no_grad()
153	def compute_acis_mask(wrapper, batch, device):
154	    bm = wrapper.base_model
155	    images, _ = wrapper.policy.prepare_images(batch)
156	    vis_tokens, _ = wrapper._get_visual_tokens(images)
157	    B = vis_tokens.shape[0]
158	    noise = bm.sample_noise(
159	        (B, bm.config.chunk_size, bm.config.max_action_dim), device
160	    )
161	    time = torch.ones(B, device=device)
162	    suffix_embs, _, _ = bm.embed_suffix(noise, time)
163	    scores = wrapper.acis(suffix_embs, vis_tokens)
164	    N_vis = vis_tokens.shape[1]
165	    k = max(1, int(N_vis * wrapper.k_ratio))
166	    _, topk_idx = torch.topk(scores, k, dim=-1)
167	    mask = torch.zeros(B, N_vis, device=device)
168	    mask.scatter_(1, topk_idx, 1.0)
169	    return mask
170	
171	
172	def register_acis_hook(connector, mask):
173	    def hook_fn(module, input, output):
174	        tokens = output[0] if isinstance(output, tuple) else output
175	        if tokens.dim() != 3 or tokens.shape[1] != mask.shape[1]:
176	            return output
177	        masked = tokens * mask[:tokens.shape[0]].unsqueeze(-1)
178	        if isinstance(output, tuple):
179	            return (masked,) + output[1:]
180	        return masked
181	    return connector.register_forward_hook(hook_fn)
182	
183	
184	@torch.no_grad()
185	def predict_actions(policy, batch):
186	    images, img_masks = policy.prepare_images(batch)
187	    state = policy.prepare_state(batch)
188	    lang_tokens = batch["observation.language.tokens"]
189	    lang_masks = batch["observation.language.attention_mask"]
190	    actions = policy.model.sample_actions(
191	        images, img_masks, lang_tokens, lang_masks, state
192	    )
193	    original_action_dim = policy.config.action_feature.shape[0]
194	    return actions[0, :, :original_action_dim]
195	
196	
197	def run_divergence_analysis(args):
198	    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
199	    task_ids = [int(x) for x in args.task_ids.split(",")]
200	    output_dir = Path(args.output_dir)
201	    output_dir.mkdir(parents=True, exist_ok=True)
202	
203	    np.random.seed(args.seed)
204	    torch.manual_seed(args.seed)
205	
206	    log.info("Loading baseline model...")
207	    baseline_policy, baseline_config = load_baseline_model(device)
208	
209	    log.info("Loading ACIS model...")
210	    acis_policy, acis_wrapper, acis_config = load_acis_model(device)
211	
212	    from train import get_tokenizer_from_policy
213	    tokenizer = get_tokenizer_from_policy(baseline_policy)
214	
215	    camera_keys = baseline_config.get("dataset", {}).get("features", {}).get("cameras", [
216	        "observation.images.image", "observation.images.image2"
217	    ])
218	
219	    acis_connector = find_connector(acis_policy.model)
220	    if acis_connector is None:
221	        raise RuntimeError("Cannot find connector for ACIS hook")
222	
223	    from libero.libero import benchmark
224	    from lerobot.envs.libero import get_task_init_states, LiberoEnv
225	
226	    bench_dict = benchmark.get_benchmark_dict()
227	    task_suite = bench_dict[SUITE]()
228	
229	    all_results = {}
230	
231	    for task_id in task_ids:
232	        task = task_suite.get_task(task_id)
233	        task_desc = task.language
234	        log.info("=== Task %d: %s ===", task_id, task_desc)
235	
236	        env = LiberoEnv(
237	            task_suite=task_suite,
238	            task_id=task_id,
239	            task_suite_name=SUITE,
240	            camera_name="agentview_image,robot0_eye_in_hand_image",
241	            obs_type="pixels_agent_pos",
242	            observation_width=256,
243	            observation_height=256,
244	            init_states=True,
245	            n_envs=1,
246	            episode_index=0,
247	            control_mode="relative",
248	        )
249	
250	        task_episodes = []
251	
252	        for ep in range(args.num_episodes):
253	            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)
254	            baseline_chunk = None
255	            baseline_idx = 0
256	            episode_data = {
257	                "task_id": task_id,
258	                "task_desc": task_desc,
259	                "episode": ep,
260	                "timesteps": [],
261	            }
262	
263	            for step in range(MAX_STEPS):
264	                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)
265	
266	                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)
267	
268	                if need_replan:
269	                    baseline_chunk = predict_actions(baseline_policy, batch)
270	                    baseline_idx = 0
271	
272	                    mask = compute_acis_mask(acis_wrapper, batch, device)
273	                    hook_handle = register_acis_hook(acis_connector, mask)
274	                    acis_chunk = predict_actions(acis_policy, batch)
275	                    hook_handle.remove()
276	                    acis_idx = 0
277	
278	                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)
279	                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)
280	
281	                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)
282	                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)
283	
284	                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))
285	                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()
286	
287	                episode_data["timesteps"].append({
288	                    "step": step,
289	                    "baseline_action": baseline_action_clipped.tolist(),
290	                    "acis_action": acis_action_clipped.tolist(),
291	                    "l2_distance": l2_dist,
292	                    "per_dim_diff": per_dim_diff,
293	                })
294	
295	                baseline_idx += 1
296	                acis_idx += 1
297	
298	                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)
299	
300	                if info.get("is_success", False) or terminated or truncated:
301	                    break
302	
303	            task_episodes.append(episode_data)
304	            n_steps = len(episode_data["timesteps"])
305	            final_l2 = episode_data["timesteps"][-1]["l2_distance"] if n_steps > 0 else 0
306	            log.info("  Ep %d: %d steps, final L2=%.4f", ep, n_steps, final_l2)
307	
308	        env.close()
309	        all_results[task_id] = task_episodes
310	
311	    # --- Analysis ---
312	    log.info("Computing statistics...")
313	    analysis = compute_analysis(all_results)
314	
315	    # Save raw data
316	    json_path = output_dir / "action_divergence_data.json"
317	    with open(json_path, "w") as f:
318	        json.dump({"episodes": all_results, "analysis": analysis}, f, indent=2)
319	    log.info("Raw data saved to %s", json_path)
320	
321	    # Plot
322	    plot_divergence_curves(all_results, analysis, output_dir)
323	    log.info("Done.")
324	
325	
326	def compute_analysis(all_results: dict) -> dict:
327	    all_l2_curves = []
328	    all_per_dim_curves = []
329	
330	    for task_id, episodes in all_results.items():
331	        for ep_data in episodes:
332	            steps = ep_data["timesteps"]
333	            l2_curve = [s["l2_distance"] for s in steps]
334	            per_dim = [s["per_dim_diff"] for s in steps]
335	            all_l2_curves.append(l2_curve)
336	            all_per_dim_curves.append(per_dim)
337	
338	    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0
339	
340	    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)
341	    for i, curve in enumerate(all_l2_curves):
342	        padded_l2[i, :len(curve)] = curve
343	
344	    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()
345	    std_l2 = np.nanstd(padded_l2, axis=0).tolist()
346	
347	    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]
348	    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0
349	
350	    overall_mean_l2 = float(np.nanmean(padded_l2))
351	
352	    # Per-dimension analysis
353	    n_dims = 7
354	    dim_abs_means = []
355	    for d in range(n_dims):
356	        dim_vals = []
357	        for per_dim_curve in all_per_dim_curves:
358	            for step_diff in per_dim_curve:
359	                if len(step_diff) > d:
360	                    dim_vals.append(abs(step_diff[d]))
361	        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)
362	
363	    # Growth rate: linear regression slope on mean L2
364	    valid_mean = [v for v in mean_l2 if not np.isnan(v)]
365	    if len(valid_mean) > 10:
366	        x = np.arange(len(valid_mean))
367	        slope = float(np.polyfit(x, valid_mean, 1)[0])
368	    else:
369	        slope = 0.0
370	
371	    return {
372	        "overall_mean_l2": overall_mean_l2,
373	        "first_step_mean_l2": avg_first_step,
374	        "l2_growth_rate_per_step": slope,
375	        "per_dim_mean_abs_diff": {
376	            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))
377	        },
378	        "mean_l2_curve": mean_l2,
379	        "std_l2_curve": std_l2,
380	        "num_episodes": len(all_l2_curves),
381	        "max_episode_length": max_len,
382	    }
383	
384	
385	def plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path):
386	    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
387	
388	    # Plot 1: L2 divergence curves (all episodes + mean)
389	    ax = axes[0]
390	    colors = plt.cm.tab10(np.linspace(0, 1, 10))
391	    task_ids = sorted(all_results.keys())
392	
393	    for ti, task_id in enumerate(task_ids):
394	        episodes = all_results[task_id]
395	        for ep_data in episodes:
396	            steps = ep_data["timesteps"]
397	            l2_vals = [s["l2_distance"] for s in steps]
398	            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)
399	
400	    mean_curve = analysis["mean_l2_curve"]
401	    std_curve = analysis["std_l2_curve"]
402	    x = np.arange(len(mean_curve))
403	    ax.plot(x, mean_curve, color="black", linewidth=2, label="Mean")
404	    mean_arr = np.array(mean_curve)
405	    std_arr = np.array(std_curve)
406	    valid = ~np.isnan(mean_arr)
407	    ax.fill_between(
408	        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],
409	        alpha=0.15, color="black"
410	    )
411	    ax.set_xlabel("Timestep")
412	    ax.set_ylabel("L2 Action Distance")
413	    ax.set_title("Baseline vs ACIS k=0.7: Action Divergence")
414	    ax.legend(loc="upper left")
415	    ax.grid(True, alpha=0.3)
416	
417	    # Plot 2: Per-dimension breakdown
418	    ax = axes[1]
419	    dim_data = analysis["per_dim_mean_abs_diff"]
420	    names = list(dim_data.keys())
421	    values = list(dim_data.values())
422	    bar_colors = ["#2196F3"] * 3 + ["#FF9800"] * 3 + ["#4CAF50"]
423	    ax.bar(names, values, color=bar_colors)
424	    ax.set_xlabel("Action Dimension")
425	    ax.set_ylabel("Mean |Difference|")
426	    ax.set_title("Per-Dimension Divergence")
427	    ax.set_xticklabels(names, rotation=45, ha="right")
428	    ax.grid(True, alpha=0.3, axis="y")
429	
430	    # Plot 3: Per-task mean curves
431	    ax = axes[2]
432	    for ti, task_id in enumerate(task_ids):
433	        episodes = all_results[task_id]
434	        task_l2s = []
435	        for ep_data in episodes:
436	            l2_vals = [s["l2_distance"] for s in ep_data["timesteps"]]
437	            task_l2s.append(l2_vals)
438	        max_t = max(len(c) for c in task_l2s)
439	        padded = np.full((len(task_l2s), max_t), np.nan)
440	        for i, c in enumerate(task_l2s):
441	            padded[i, :len(c)] = c
442	        task_mean = np.nanmean(padded, axis=0)
443	        task_desc = episodes[0]["task_desc"]
444	        short_desc = task_desc[:30] + "..." if len(task_desc) > 30 else task_desc
445	        ax.plot(task_mean, linewidth=1.5, label=f"T{task_id}: {short_desc}", color=colors[ti % 10])
446	    ax.set_xlabel("Timestep")
447	    ax.set_ylabel("L2 Action Distance")
448	    ax.set_title("Per-Task Mean Divergence")
449	    ax.legend(fontsize=7, loc="upper left")
450	    ax.grid(True, alpha=0.3)
451	
452	    plt.tight_layout()
453	    pdf_path = output_dir / "action_divergence_curve.pdf"
454	    plt.savefig(pdf_path, dpi=150, bbox_inches="tight")
455	    plt.savefig(output_dir / "action_divergence_curve.png", dpi=150, bbox_inches="tight")
456	    plt.close()
457	    log.info("Plots saved to %s", pdf_path)
458	
459	    # Summary stats figure
460	    fig2, ax2 = plt.subplots(figsize=(6, 3))
461	    ax2.axis("off")
462	    summary_text = (
463	        f"Action Divergence Summary (Baseline vs ACIS k=0.7)\n"
464	        f"{'='*50}\n"
465	        f"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\n"
466	        f"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\n"
467	        f"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\n"
468	        f"Num episodes:           {analysis['num_episodes']}\n"
469	        f"Max episode length:     {analysis['max_episode_length']}\n"
470	        f"\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\n"
471	        f"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\n"
472	    )
473	    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,
474	             verticalalignment="top", fontfamily="monospace")
475	    plt.tight_layout()
476	    plt.savefig(output_dir / "action_divergence_summary.pdf", dpi=150, bbox_inches="tight")
477	    plt.close()
478	
479	
480	if __name__ == "__main__":
481	    args = parse_args()
482	    run_divergence_analysis(args)
483	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "aefd778d-a8f6-4022-bc51-a2196fdcf93d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/analyze_action_divergence.py",
      "content": "\"\"\"Per-step Action Divergence Analysis: Baseline vs ACIS-pruned model.\n\nDrives the environment with baseline actions while recording both models'\naction outputs at each timestep (same observation). Produces divergence curves\nand per-dimension breakdown.\n\nUsage:\n    python analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\nos.environ.setdefault(\"TRANSFORMERS_OFFLINE\", \"1\")\nos.environ.setdefault(\"HF_HUB_OFFLINE\", \"1\")\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport torch\n\nARTIFACTS_DIR = Path(__file__).resolve().parent\nsys.path.insert(0, str(ARTIFACTS_DIR))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n# Paths\nBASELINE_CKPT = \"checkpoints/libero_full_ft_100k/checkpoint.pt\"\nACIS_CKPT = \"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\"\nBASELINE_CONFIG = \"configs/libero_baseline.yaml\"\nACIS_CONFIG = \"configs/libero_acis_stage1only_k07.yaml\"\n\nSUITE = \"libero_object\"\nMAX_STEPS = 280\nACTION_HORIZON = 50\nACTION_DIM_NAMES = [\"pos_x\", \"pos_y\", \"pos_z\", \"rot_x\", \"rot_y\", \"rot_z\", \"gripper\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--gpu\", type=int, default=2)\n    p.add_argument(\"--num_episodes\", type=int, default=5)\n    p.add_argument(\"--task_ids\", type=str, default=\"0,1,2\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--output_dir\", type=str, default=\"artifacts\")\n    return p.parse_args()\n\n\ndef load_config(config_path: str) -> dict:\n    import copy\n    import yaml\n    config_path = Path(config_path)\n    with open(config_path) as f:\n        config = yaml.safe_load(f)\n    if \"_base_\" in config:\n        base_path = config_path.parent / config.pop(\"_base_\")\n        base_config = load_config(str(base_path))\n        for k, v in config.items():\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\n                base_config[k].update(v)\n            else:\n                base_config[k] = v\n        return base_config\n    return config\n\n\ndef load_baseline_model(device):\n    from train import load_smolvla_policy\n    config = load_config(BASELINE_CONFIG)\n    policy = load_smolvla_policy(config, device)\n    ckpt = torch.load(BASELINE_CKPT, map_location=device, weights_only=False)\n    policy.load_state_dict(ckpt[\"model_state_dict\"], strict=False)\n    policy.eval()\n    return policy, config\n\n\ndef load_acis_model(device):\n    from train import load_smolvla_policy, wrap_with_imm\n    config = load_config(ACIS_CONFIG)\n    policy = load_smolvla_policy(config, device)\n    wrapper = wrap_with_imm(policy, config)\n    wrapper.to(device)\n    ckpt = torch.load(ACIS_CKPT, map_location=device, weights_only=False)\n    wrapper.load_state_dict(ckpt[\"model_state_dict\"], strict=False)\n    wrapper.eval()\n    return wrapper.policy, wrapper, config\n\n\n# --- Observation / Action utilities (from eval_success_rate_libero.py) ---\n\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\n    q = quat.astype(np.float64)\n    w = np.clip(q[3], -1.0, 1.0)\n    den = np.sqrt(max(1.0 - w * w, 0.0))\n    if den > 1e-10:\n        angle = 2.0 * np.arccos(w)\n        axis = q[:3] / den\n        return (axis * angle).astype(np.float32)\n    return np.zeros(3, dtype=np.float32)\n\n\ndef extract_state(obs: dict) -> np.ndarray:\n    rs = obs[\"robot_state\"]\n    eef_pos = np.asarray(rs[\"eef\"][\"pos\"], dtype=np.float32)\n    eef_quat = np.asarray(rs[\"eef\"][\"quat\"], dtype=np.float64)\n    gripper_qpos = np.asarray(rs[\"gripper\"][\"qpos\"], dtype=np.float32)\n    eef_aa = quat_to_axis_angle(eef_quat)\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\n\n\ndef obs_to_batch(obs, task_text, tokenizer, camera_keys, device):\n    batch = {}\n    for cam_key in camera_keys:\n        short_name = cam_key.split(\".\")[-1]\n        img = obs[\"pixels\"][short_name]\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\n        img_t = img_t.unsqueeze(0)\n        img_t = torch.flip(img_t, dims=[2, 3])\n        batch[cam_key] = img_t.to(device)\n    state = extract_state(obs)\n    batch[\"observation.state\"] = torch.from_numpy(state).unsqueeze(0).to(device)\n    text = task_text if task_text.endswith(\"\\n\") else task_text + \"\\n\"\n    encoded = tokenizer(\n        [text], padding=\"longest\", max_length=48, truncation=True, return_tensors=\"pt\",\n    )\n    batch[\"observation.language.tokens\"] = encoded[\"input_ids\"].to(device)\n    batch[\"observation.language.attention_mask\"] = encoded[\"attention_mask\"].bool().to(device)\n    return batch\n\n\ndef find_connector(model):\n    for name, module in model.named_modules():\n        if name.endswith(\".connector\") or \"multi_modal_projector\" in name:\n            return module\n    return None\n\n\n@torch.no_grad()\ndef compute_acis_mask(wrapper, batch, device):\n    bm = wrapper.base_model\n    images, _ = wrapper.policy.prepare_images(batch)\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\n    B = vis_tokens.shape[0]\n    noise = bm.sample_noise(\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\n    )\n    time = torch.ones(B, device=device)\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\n    scores = wrapper.acis(suffix_embs, vis_tokens)\n    N_vis = vis_tokens.shape[1]\n    k = max(1, int(N_vis * wrapper.k_ratio))\n    _, topk_idx = torch.topk(scores, k, dim=-1)\n    mask = torch.zeros(B, N_vis, device=device)\n    mask.scatter_(1, topk_idx, 1.0)\n    return mask\n\n\ndef register_acis_hook(connector, mask):\n    def hook_fn(module, input, output):\n        tokens = output[0] if isinstance(output, tuple) else output\n        if tokens.dim() != 3 or tokens.shape[1] != mask.shape[1]:\n            return output\n        masked = tokens * mask[:tokens.shape[0]].unsqueeze(-1)\n        if isinstance(output, tuple):\n            return (masked,) + output[1:]\n        return masked\n    return connector.register_forward_hook(hook_fn)\n\n\n@torch.no_grad()\ndef predict_actions(policy, batch):\n    images, img_masks = policy.prepare_images(batch)\n    state = policy.prepare_state(batch)\n    lang_tokens = batch[\"observation.language.tokens\"]\n    lang_masks = batch[\"observation.language.attention_mask\"]\n    actions = policy.model.sample_actions(\n        images, img_masks, lang_tokens, lang_masks, state\n    )\n    original_action_dim = policy.config.action_feature.shape[0]\n    return actions[0, :, :original_action_dim]\n\n\ndef run_divergence_analysis(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    task_ids = [int(x) for x in args.task_ids.split(\",\")]\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    log.info(\"Loading baseline model...\")\n    baseline_policy, baseline_config = load_baseline_model(device)\n\n    log.info(\"Loading ACIS model...\")\n    acis_policy, acis_wrapper, acis_config = load_acis_model(device)\n\n    from train import get_tokenizer_from_policy\n    tokenizer = get_tokenizer_from_policy(baseline_policy)\n\n    camera_keys = baseline_config.get(\"dataset\", {}).get(\"features\", {}).get(\"cameras\", [\n        \"observation.images.image\", \"observation.images.image2\"\n    ])\n\n    acis_connector = find_connector(acis_policy.model)\n    if acis_connector is None:\n        raise RuntimeError(\"Cannot find connector for ACIS hook\")\n\n    from libero.libero import benchmark\n    from lerobot.envs.libero import get_task_init_states, LiberoEnv\n\n    bench_dict = benchmark.get_benchmark_dict()\n    task_suite = bench_dict[SUITE]()\n\n    all_results = {}\n\n    for task_id in task_ids:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        log.info(\"=== Task %d: %s ===\", task_id, task_desc)\n\n        env = LiberoEnv(\n            task_suite=task_suite,\n            task_id=task_id,\n            task_suite_name=SUITE,\n            camera_name=\"agentview_image,robot0_eye_in_hand_image\",\n            obs_type=\"pixels_agent_pos\",\n            observation_width=256,\n            observation_height=256,\n            init_states=True,\n            n_envs=1,\n            episode_index=0,\n            control_mode=\"relative\",\n        )\n\n        task_episodes = []\n\n        for ep in range(args.num_episodes):\n            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)\n            baseline_chunk = None\n            baseline_idx = 0\n            episode_data = {\n                \"task_id\": task_id,\n                \"task_desc\": task_desc,\n                \"episode\": ep,\n                \"timesteps\": [],\n            }\n\n            for step in range(MAX_STEPS):\n                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\n\n                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)\n\n                if need_replan:\n                    baseline_chunk = predict_actions(baseline_policy, batch)\n                    baseline_idx = 0\n\n                    mask = compute_acis_mask(acis_wrapper, batch, device)\n                    hook_handle = register_acis_hook(acis_connector, mask)\n                    acis_chunk = predict_actions(acis_policy, batch)\n                    hook_handle.remove()\n                    acis_idx = 0\n\n                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)\n                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)\n\n                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)\n                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)\n\n                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))\n                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()\n\n                episode_data[\"timesteps\"].append({\n                    \"step\": step,\n                    \"baseline_action\": baseline_action_clipped.tolist(),\n                    \"acis_action\": acis_action_clipped.tolist(),\n                    \"l2_distance\": l2_dist,\n                    \"per_dim_diff\": per_dim_diff,\n                })\n\n                baseline_idx += 1\n                acis_idx += 1\n\n                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)\n\n                if info.get(\"is_success\", False) or terminated or truncated:\n                    break\n\n            task_episodes.append(episode_data)\n            n_steps = len(episode_data[\"timesteps\"])\n            final_l2 = episode_data[\"timesteps\"][-1][\"l2_distance\"] if n_steps > 0 else 0\n            log.info(\"  Ep %d: %d steps, final L2=%.4f\", ep, n_steps, final_l2)\n\n        env.close()\n        all_results[task_id] = task_episodes\n\n    # --- Analysis ---\n    log.info(\"Computing statistics...\")\n    analysis = compute_analysis(all_results)\n\n    # Save raw data\n    json_path = output_dir / \"action_divergence_data.json\"\n    with open(json_path, \"w\") as f:\n        json.dump({\"episodes\": all_results, \"analysis\": analysis}, f, indent=2)\n    log.info(\"Raw data saved to %s\", json_path)\n\n    # Plot\n    plot_divergence_curves(all_results, analysis, output_dir)\n    log.info(\"Done.\")\n\n\ndef compute_analysis(all_results: dict) -> dict:\n    all_l2_curves = []\n    all_per_dim_curves = []\n\n    for task_id, episodes in all_results.items():\n        for ep_data in episodes:\n            steps = ep_data[\"timesteps\"]\n            l2_curve = [s[\"l2_distance\"] for s in steps]\n            per_dim = [s[\"per_dim_diff\"] for s in steps]\n            all_l2_curves.append(l2_curve)\n            all_per_dim_curves.append(per_dim)\n\n    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0\n\n    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)\n    for i, curve in enumerate(all_l2_curves):\n        padded_l2[i, :len(curve)] = curve\n\n    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()\n    std_l2 = np.nanstd(padded_l2, axis=0).tolist()\n\n    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]\n    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0\n\n    overall_mean_l2 = float(np.nanmean(padded_l2))\n\n    # Per-dimension analysis\n    n_dims = 7\n    dim_abs_means = []\n    for d in range(n_dims):\n        dim_vals = []\n        for per_dim_curve in all_per_dim_curves:\n            for step_diff in per_dim_curve:\n                if len(step_diff) > d:\n                    dim_vals.append(abs(step_diff[d]))\n        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)\n\n    # Growth rate: linear regression slope on mean L2\n    valid_mean = [v for v in mean_l2 if not np.isnan(v)]\n    if len(valid_mean) > 10:\n        x = np.arange(len(valid_mean))\n        slope = float(np.polyfit(x, valid_mean, 1)[0])\n    else:\n        slope = 0.0\n\n    return {\n        \"overall_mean_l2\": overall_mean_l2,\n        \"first_step_mean_l2\": avg_first_step,\n        \"l2_growth_rate_per_step\": slope,\n        \"per_dim_mean_abs_diff\": {\n            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))\n        },\n        \"mean_l2_curve\": mean_l2,\n        \"std_l2_curve\": std_l2,\n        \"num_episodes\": len(all_l2_curves),\n        \"max_episode_length\": max_len,\n    }\n\n\ndef plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path):\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\n\n    # Plot 1: L2 divergence curves (all episodes + mean)\n    ax = axes[0]\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\n    task_ids = sorted(all_results.keys())\n\n    for ti, task_id in enumerate(task_ids):\n        episodes = all_results[task_id]\n        for ep_data in episodes:\n            steps = ep_data[\"timesteps\"]\n            l2_vals = [s[\"l2_distance\"] for s in steps]\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\n\n    mean_curve = analysis[\"mean_l2_curve\"]\n    std_curve = analysis[\"std_l2_curve\"]\n    x = np.arange(len(mean_curve))\n    ax.plot(x, mean_curve, color=\"black\", linewidth=2, label=\"Mean\")\n    mean_arr = np.array(mean_curve)\n    std_arr = np.array(std_curve)\n    valid = ~np.isnan(mean_arr)\n    ax.fill_between(\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\n        alpha=0.15, color=\"black\"\n    )\n    ax.set_xlabel(\"Timestep\")\n    ax.set_ylabel(\"L2 Action Distance\")\n    ax.set_title(\"Baseline vs ACIS k=0.7: Action Divergence\")\n    ax.legend(loc=\"upper left\")\n    ax.grid(True, alpha=0.3)\n\n    # Plot 2: Per-dimension breakdown\n    ax = axes[1]\n    dim_data = analysis[\"per_dim_mean_abs_diff\"]\n    names = list(dim_data.keys())\n    values = list(dim_data.values())\n    bar_colors = [\"#2196F3\"] * 3 + [\"#FF9800\"] * 3 + [\"#4CAF50\"]\n    ax.bar(names, values, color=bar_colors)\n    ax.set_xlabel(\"Action Dimension\")\n    ax.set_ylabel(\"Mean |Difference|\")\n    ax.set_title(\"Per-Dimension Divergence\")\n    ax.set_xticklabels(names, rotation=45, ha=\"right\")\n    ax.grid(True, alpha=0.3, axis=\"y\")\n\n    # Plot 3: Per-task mean curves\n    ax = axes[2]\n    for ti, task_id in enumerate(task_ids):\n        episodes = all_results[task_id]\n        task_l2s = []\n        for ep_data in episodes:\n            l2_vals = [s[\"l2_distance\"] for s in ep_data[\"timesteps\"]]\n            task_l2s.append(l2_vals)\n        max_t = max(len(c) for c in task_l2s)\n        padded = np.full((len(task_l2s), max_t), np.nan)\n        for i, c in enumerate(task_l2s):\n            padded[i, :len(c)] = c\n        task_mean = np.nanmean(padded, axis=0)\n        task_desc = episodes[0][\"task_desc\"]\n        short_desc = task_desc[:30] + \"...\" if len(task_desc) > 30 else task_desc\n        ax.plot(task_mean, linewidth=1.5, label=f\"T{task_id}: {short_desc}\", color=colors[ti % 10])\n    ax.set_xlabel(\"Timestep\")\n    ax.set_ylabel(\"L2 Action Distance\")\n    ax.set_title(\"Per-Task Mean Divergence\")\n    ax.legend(fontsize=7, loc=\"upper left\")\n    ax.grid(True, alpha=0.3)\n\n    plt.tight_layout()\n    pdf_path = output_dir / \"action_divergence_curve.pdf\"\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\"tight\")\n    plt.savefig(output_dir / \"action_divergence_curve.png\", dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    log.info(\"Plots saved to %s\", pdf_path)\n\n    # Summary stats figure\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\n    ax2.axis(\"off\")\n    summary_text = (\n        f\"Action Divergence Summary (Baseline vs ACIS k=0.7)\\n\"\n        f\"{'='*50}\\n\"\n        f\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\n\"\n        f\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\n\"\n        f\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\n\"\n        f\"Num episodes:           {analysis['num_episodes']}\\n\"\n        f\"Max episode length:     {analysis['max_episode_length']}\\n\"\n        f\"\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\n\"\n        f\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\n\"\n    )\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\n             verticalalignment=\"top\", fontfamily=\"monospace\")\n    plt.tight_layout()\n    plt.savefig(output_dir / \"action_divergence_summary.pdf\", dpi=150, bbox_inches=\"tight\")\n    plt.close()\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_divergence_analysis(args)\n",
      "numLines": 483,
      "startLine": 1,
      "totalLines": 483
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Write · `toolu_01Bq3VimZkVLnGM1Soxshyd2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/analyze_action_divergence_v2.py",
  "content": "\"\"\"Per-step Action Divergence Analysis (v2): Same-checkpoint, pruning-only comparison.\n\nLoads the SAME checkpoint for both runs. BASELINE does full forward (no pruning),\nACIS applies true_removal pruning at k=0.5. Pruning is the only variable.\n\nDrives the environment with baseline actions while recording both models'\naction outputs at each timestep (same observation). Produces divergence curves\nand per-dimension breakdown.\n\nUsage:\n    python analyze_action_divergence_v2.py --gpu 2 --num_episodes 10 --task_ids 0,1,2\n    python analyze_action_divergence_v2.py --gpu 2 --k_ratio 0.3 --checkpoint checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\nos.environ.setdefault(\"TRANSFORMERS_OFFLINE\", \"1\")\nos.environ.setdefault(\"HF_HUB_OFFLINE\", \"1\")\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport torch\n\nARTIFACTS_DIR = Path(__file__).resolve().parent\nsys.path.insert(0, str(ARTIFACTS_DIR))\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nCHECKPOINT = \"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\"\nCONFIG = \"configs/libero_acis_stage1only_k07.yaml\"\n\nSUITE = \"libero_object\"\nMAX_STEPS = 280\nACTION_HORIZON = 50\nACTION_DIM_NAMES = [\"pos_x\", \"pos_y\", \"pos_z\", \"rot_x\", \"rot_y\", \"rot_z\", \"gripper\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--gpu\", type=int, default=2)\n    p.add_argument(\"--num_episodes\", type=int, default=10)\n    p.add_argument(\"--task_ids\", type=str, default=\"0,1,2\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--output_dir\", type=str, default=\"artifacts\")\n    p.add_argument(\"--checkpoint\", type=str, default=CHECKPOINT)\n    p.add_argument(\"--config\", type=str, default=CONFIG)\n    p.add_argument(\"--k_ratio\", type=float, default=0.5)\n    return p.parse_args()\n\n\ndef load_config(config_path: str) -> dict:\n    import yaml\n    config_path = Path(config_path)\n    with open(config_path) as f:\n        config = yaml.safe_load(f)\n    if \"_base_\" in config:\n        base_path = config_path.parent / config.pop(\"_base_\")\n        base_config = load_config(str(base_path))\n        for k, v in config.items():\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\n                base_config[k].update(v)\n            else:\n                base_config[k] = v\n        return base_config\n    return config\n\n\ndef load_model_pair(checkpoint: str, config_path: str, k_ratio: float, device):\n    \"\"\"Load the same checkpoint twice: once as baseline (no pruning), once for ACIS.\n\n    Returns (baseline_policy, acis_policy, acis_wrapper, config).\n    \"\"\"\n    from train import load_smolvla_policy, wrap_with_imm\n\n    config = load_config(config_path)\n\n    # --- Baseline: load via wrapper (to match state_dict keys), extract policy ---\n    baseline_policy = load_smolvla_policy(config, device)\n    baseline_wrapper = wrap_with_imm(baseline_policy, config)\n    baseline_wrapper.to(device)\n    ckpt = torch.load(checkpoint, map_location=device, weights_only=False)\n    baseline_wrapper.load_state_dict(ckpt[\"model_state_dict\"], strict=False)\n    baseline_wrapper.eval()\n    baseline_policy = baseline_wrapper.policy\n\n    # --- ACIS: load via wrapper, override k_ratio ---\n    acis_policy = load_smolvla_policy(config, device)\n    acis_wrapper = wrap_with_imm(acis_policy, config)\n    acis_wrapper.to(device)\n    ckpt2 = torch.load(checkpoint, map_location=device, weights_only=False)\n    acis_wrapper.load_state_dict(ckpt2[\"model_state_dict\"], strict=False)\n    acis_wrapper.k_ratio = k_ratio\n    acis_wrapper.eval()\n    acis_policy = acis_wrapper.policy\n\n    log.info(\"Loaded same checkpoint for both runs: %s\", checkpoint)\n    log.info(\"Baseline: full forward (no pruning)\")\n    log.info(\"ACIS: true_removal, k_ratio=%.2f\", k_ratio)\n\n    return baseline_policy, acis_policy, acis_wrapper, config\n\n\n# --- Observation / Action utilities ---\n\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\n    q = quat.astype(np.float64)\n    w = np.clip(q[3], -1.0, 1.0)\n    den = np.sqrt(max(1.0 - w * w, 0.0))\n    if den > 1e-10:\n        angle = 2.0 * np.arccos(w)\n        axis = q[:3] / den\n        return (axis * angle).astype(np.float32)\n    return np.zeros(3, dtype=np.float32)\n\n\ndef extract_state(obs: dict) -> np.ndarray:\n    rs = obs[\"robot_state\"]\n    eef_pos = np.asarray(rs[\"eef\"][\"pos\"], dtype=np.float32)\n    eef_quat = np.asarray(rs[\"eef\"][\"quat\"], dtype=np.float64)\n    gripper_qpos = np.asarray(rs[\"gripper\"][\"qpos\"], dtype=np.float32)\n    eef_aa = quat_to_axis_angle(eef_quat)\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\n\n\ndef obs_to_batch(obs, task_text, tokenizer, camera_keys, device):\n    batch = {}\n    for cam_key in camera_keys:\n        short_name = cam_key.split(\".\")[-1]\n        img = obs[\"pixels\"][short_name]\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\n        img_t = img_t.unsqueeze(0)\n        img_t = torch.flip(img_t, dims=[2, 3])\n        batch[cam_key] = img_t.to(device)\n    state = extract_state(obs)\n    batch[\"observation.state\"] = torch.from_numpy(state).unsqueeze(0).to(device)\n    text = task_text if task_text.endswith(\"\\n\") else task_text + \"\\n\"\n    encoded = tokenizer(\n        [text], padding=\"longest\", max_length=48, truncation=True, return_tensors=\"pt\",\n    )\n    batch[\"observation.language.tokens\"] = encoded[\"input_ids\"].to(device)\n    batch[\"observation.language.attention_mask\"] = encoded[\"attention_mask\"].bool().to(device)\n    return batch\n\n\ndef find_connector(model):\n    for name, module in model.named_modules():\n        if name.endswith(\".connector\") or \"multi_modal_projector\" in name:\n            return module\n    return None\n\n\n@torch.no_grad()\ndef compute_acis_mask(wrapper, batch, device):\n    bm = wrapper.base_model\n    images, _ = wrapper.policy.prepare_images(batch)\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\n    B = vis_tokens.shape[0]\n    noise = bm.sample_noise(\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\n    )\n    time = torch.ones(B, device=device)\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\n    scores = wrapper.acis(suffix_embs, vis_tokens)\n    N_vis = vis_tokens.shape[1]\n    k = max(1, int(N_vis * wrapper.k_ratio))\n    _, topk_idx = torch.topk(scores, k, dim=-1)\n    mask = torch.zeros(B, N_vis, device=device)\n    mask.scatter_(1, topk_idx, 1.0)\n    return mask\n\n\ndef register_acis_hook(connector, mask: torch.Tensor, method: str = \"true_removal\"):\n    \"\"\"Register forward hook on connector that prunes visual tokens.\n\n    Uses the stateful offset approach from eval_success_rate_libero.py to handle\n    multi-camera setups where the connector is called once per camera.\n    \"\"\"\n    state = {\"offset\": 0}\n\n    def hook_fn(module, input, output):\n        tokens = output[0] if isinstance(output, tuple) else output\n        if tokens.dim() != 3:\n            return output\n        n = tokens.shape[1]\n        offset = state[\"offset\"]\n        if offset + n > mask.shape[1]:\n            return output\n        cam_mask = mask[:, offset:offset + n]\n        state[\"offset\"] = offset + n\n\n        B, N, D = tokens.shape\n        keep_mask = cam_mask[:B]\n\n        if method == \"true_removal\":\n            kept = keep_mask[0].bool()\n            masked = tokens[:, kept, :]\n        else:\n            masked = tokens * keep_mask.unsqueeze(-1)\n\n        if isinstance(output, tuple):\n            return (masked,) + output[1:]\n        return masked\n\n    return connector.register_forward_hook(hook_fn)\n\n\n@torch.no_grad()\ndef predict_actions(policy, batch):\n    images, img_masks = policy.prepare_images(batch)\n    state = policy.prepare_state(batch)\n    lang_tokens = batch[\"observation.language.tokens\"]\n    lang_masks = batch[\"observation.language.attention_mask\"]\n    actions = policy.model.sample_actions(\n        images, img_masks, lang_tokens, lang_masks, state\n    )\n    original_action_dim = policy.config.action_feature.shape[0]\n    return actions[0, :, :original_action_dim]\n\n\ndef run_divergence_analysis(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    task_ids = [int(x) for x in args.task_ids.split(\",\")]\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    log.info(\"Loading model pair from same checkpoint...\")\n    baseline_policy, acis_policy, acis_wrapper, config = load_model_pair(\n        args.checkpoint, args.config, args.k_ratio, device\n    )\n\n    from train import get_tokenizer_from_policy\n    tokenizer = get_tokenizer_from_policy(baseline_policy)\n\n    camera_keys = config.get(\"dataset\", {}).get(\"features\", {}).get(\"cameras\", [\n        \"observation.images.image\", \"observation.images.image2\"\n    ])\n\n    acis_connector = find_connector(acis_policy.model)\n    if acis_connector is None:\n        raise RuntimeError(\"Cannot find connector for ACIS hook\")\n\n    from libero.libero import benchmark\n    from lerobot.envs.libero import get_task_init_states, LiberoEnv\n\n    bench_dict = benchmark.get_benchmark_dict()\n    task_suite = bench_dict[SUITE]()\n\n    all_results = {}\n\n    for task_id in task_ids:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        log.info(\"=== Task %d: %s ===\", task_id, task_desc)\n\n        env = LiberoEnv(\n            task_suite=task_suite,\n            task_id=task_id,\n            task_suite_name=SUITE,\n            camera_name=\"agentview_image,robot0_eye_in_hand_image\",\n            obs_type=\"pixels_agent_pos\",\n            observation_width=256,\n            observation_height=256,\n            init_states=True,\n            n_envs=1,\n            episode_index=0,\n            control_mode=\"relative\",\n        )\n\n        task_episodes = []\n\n        for ep in range(args.num_episodes):\n            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)\n            baseline_chunk = None\n            baseline_idx = 0\n            acis_chunk = None\n            acis_idx = 0\n            episode_data = {\n                \"task_id\": task_id,\n                \"task_desc\": task_desc,\n                \"episode\": ep,\n                \"timesteps\": [],\n            }\n\n            for step in range(MAX_STEPS):\n                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\n\n                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)\n\n                if need_replan:\n                    baseline_chunk = predict_actions(baseline_policy, batch)\n                    baseline_idx = 0\n\n                    mask = compute_acis_mask(acis_wrapper, batch, device)\n                    hook_handle = register_acis_hook(acis_connector, mask, method=\"true_removal\")\n                    acis_chunk = predict_actions(acis_policy, batch)\n                    hook_handle.remove()\n                    acis_idx = 0\n\n                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)\n                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)\n\n                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)\n                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)\n\n                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))\n                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()\n\n                episode_data[\"timesteps\"].append({\n                    \"step\": step,\n                    \"baseline_action\": baseline_action_clipped.tolist(),\n                    \"acis_action\": acis_action_clipped.tolist(),\n                    \"l2_distance\": l2_dist,\n                    \"per_dim_diff\": per_dim_diff,\n                })\n\n                baseline_idx += 1\n                acis_idx += 1\n\n                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)\n\n                if info.get(\"is_success\", False) or terminated or truncated:\n                    break\n\n            task_episodes.append(episode_data)\n            n_steps = len(episode_data[\"timesteps\"])\n            final_l2 = episode_data[\"timesteps\"][-1][\"l2_distance\"] if n_steps > 0 else 0\n            log.info(\"  Ep %d: %d steps, final L2=%.4f\", ep, n_steps, final_l2)\n\n        env.close()\n        all_results[task_id] = task_episodes\n\n    # --- Analysis ---\n    log.info(\"Computing statistics...\")\n    analysis = compute_analysis(all_results)\n\n    # Save raw data\n    json_path = output_dir / \"action_divergence_v2_data.json\"\n    with open(json_path, \"w\") as f:\n        json.dump({\n            \"metadata\": {\n                \"checkpoint\": args.checkpoint,\n                \"config\": args.config,\n                \"k_ratio\": args.k_ratio,\n                \"pruning_method\": \"true_removal\",\n                \"baseline_mode\": \"bypass (no pruning)\",\n                \"num_episodes\": args.num_episodes,\n                \"seed\": args.seed,\n            },\n            \"episodes\": all_results,\n            \"analysis\": analysis,\n        }, f, indent=2)\n    log.info(\"Raw data saved to %s\", json_path)\n\n    # Plot\n    plot_divergence_curves(all_results, analysis, output_dir, args.k_ratio)\n    log.info(\"Done.\")\n\n\ndef compute_analysis(all_results: dict) -> dict:\n    all_l2_curves = []\n    all_per_dim_curves = []\n\n    for task_id, episodes in all_results.items():\n        for ep_data in episodes:\n            steps = ep_data[\"timesteps\"]\n            l2_curve = [s[\"l2_distance\"] for s in steps]\n            per_dim = [s[\"per_dim_diff\"] for s in steps]\n            all_l2_curves.append(l2_curve)\n            all_per_dim_curves.append(per_dim)\n\n    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0\n\n    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)\n    for i, curve in enumerate(all_l2_curves):\n        padded_l2[i, :len(curve)] = curve\n\n    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()\n    std_l2 = np.nanstd(padded_l2, axis=0).tolist()\n\n    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]\n    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0\n\n    overall_mean_l2 = float(np.nanmean(padded_l2))\n\n    n_dims = 7\n    dim_abs_means = []\n    for d in range(n_dims):\n        dim_vals = []\n        for per_dim_curve in all_per_dim_curves:\n            for step_diff in per_dim_curve:\n                if len(step_diff) > d:\n                    dim_vals.append(abs(step_diff[d]))\n        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)\n\n    valid_mean = [v for v in mean_l2 if not np.isnan(v)]\n    if len(valid_mean) > 10:\n        x = np.arange(len(valid_mean))\n        slope = float(np.polyfit(x, valid_mean, 1)[0])\n    else:\n        slope = 0.0\n\n    return {\n        \"overall_mean_l2\": overall_mean_l2,\n        \"first_step_mean_l2\": avg_first_step,\n        \"l2_growth_rate_per_step\": slope,\n        \"per_dim_mean_abs_diff\": {\n            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))\n        },\n        \"mean_l2_curve\": mean_l2,\n        \"std_l2_curve\": std_l2,\n        \"num_episodes\": len(all_l2_curves),\n        \"max_episode_length\": max_len,\n    }\n\n\ndef plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path,\n                           k_ratio: float):\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\n\n    ax = axes[0]\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\n    task_ids = sorted(all_results.keys())\n\n    for ti, task_id in enumerate(task_ids):\n        episodes = all_results[task_id]\n        for ep_data in episodes:\n            steps = ep_data[\"timesteps\"]\n            l2_vals = [s[\"l2_distance\"] for s in steps]\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\n\n    mean_curve = analysis[\"mean_l2_curve\"]\n    std_curve = analysis[\"std_l2_curve\"]\n    x = np.arange(len(mean_curve))\n    ax.plot(x, mean_curve, color=\"black\", linewidth=2, label=\"Mean\")\n    mean_arr = np.array(mean_curve)\n    std_arr = np.array(std_curve)\n    valid = ~np.isnan(mean_arr)\n    ax.fill_between(\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\n        alpha=0.15, color=\"black\"\n    )\n    ax.set_xlabel(\"Timestep\")\n    ax.set_ylabel(\"L2 Action Distance\")\n    ax.set_title(f\"Same ckpt: bypass vs ACIS true_removal k={k_ratio}\")\n    ax.legend(loc=\"upper left\")\n    ax.grid(True, alpha=0.3)\n\n    ax = axes[1]\n    dim_data = analysis[\"per_dim_mean_abs_diff\"]\n    names = list(dim_data.keys())\n    values = list(dim_data.values())\n    bar_colors = [\"#2196F3\"] * 3 + [\"#FF9800\"] * 3 + [\"#4CAF50\"]\n    ax.bar(names, values, color=bar_colors)\n    ax.set_xlabel(\"Action Dimension\")\n    ax.set_ylabel(\"Mean |Difference|\")\n    ax.set_title(\"Per-Dimension Divergence\")\n    ax.set_xticklabels(names, rotation=45, ha=\"right\")\n    ax.grid(True, alpha=0.3, axis=\"y\")\n\n    ax = axes[2]\n    for ti, task_id in enumerate(task_ids):\n        episodes = all_results[task_id]\n        task_l2s = []\n        for ep_data in episodes:\n            l2_vals = [s[\"l2_distance\"] for s in ep_data[\"timesteps\"]]\n            task_l2s.append(l2_vals)\n        max_t = max(len(c) for c in task_l2s)\n        padded = np.full((len(task_l2s), max_t), np.nan)\n        for i, c in enumerate(task_l2s):\n            padded[i, :len(c)] = c\n        task_mean = np.nanmean(padded, axis=0)\n        task_desc = episodes[0][\"task_desc\"]\n        short_desc = task_desc[:30] + \"...\" if len(task_desc) > 30 else task_desc\n        ax.plot(task_mean, linewidth=1.5, label=f\"T{task_id}: {short_desc}\", color=colors[ti % 10])\n    ax.set_xlabel(\"Timestep\")\n    ax.set_ylabel(\"L2 Action Distance\")\n    ax.set_title(\"Per-Task Mean Divergence\")\n    ax.legend(fontsize=7, loc=\"upper left\")\n    ax.grid(True, alpha=0.3)\n\n    plt.tight_layout()\n    pdf_path = output_dir / \"action_divergence_v2_curve.pdf\"\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\"tight\")\n    plt.savefig(output_dir / \"action_divergence_v2_curve.png\", dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    log.info(\"Plots saved to %s\", pdf_path)\n\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\n    ax2.axis(\"off\")\n    summary_text = (\n        f\"Action Divergence Summary (same ckpt, true_removal k={k_ratio})\\n\"\n        f\"{'='*55}\\n\"\n        f\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\n\"\n        f\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\n\"\n        f\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\n\"\n        f\"Num episodes:           {analysis['num_episodes']}\\n\"\n        f\"Max episode length:     {analysis['max_episode_length']}\\n\"\n        f\"\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\n\"\n        f\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\n\"\n    )\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\n             verticalalignment=\"top\", fontfamily=\"monospace\")\n    plt.tight_layout()\n    plt.savefig(output_dir / \"action_divergence_v2_summary.pdf\", dpi=150, bbox_inches=\"tight\")\n    plt.close()\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_divergence_analysis(args)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "71f9e0bc-aa1c-4393-a37a-5953a0b7bf90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfRhdpT9NQLwYDAarw5Jhi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8149,
      "cache_read_input_tokens": 54718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8149
      },
      "output_tokens": 35,
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

_source line 67 · 2026-05-17T10:41:12.831Z_

<details><summary>↩ Tool result · `toolu_01Bq3VimZkVLnGM1Soxshyd2`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/analyze_action_divergence_v2.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "d055f664-efca-4aa3-8efd-6b461fd1c143",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/analyze_action_divergence_v2.py",
    "content": "\"\"\"Per-step Action Divergence Analysis (v2): Same-checkpoint, pruning-only comparison.\n\nLoads the SAME checkpoint for both runs. BASELINE does full forward (no pruning),\nACIS applies true_removal pruning at k=0.5. Pruning is the only variable.\n\nDrives the environment with baseline actions while recording both models'\naction outputs at each timestep (same observation). Produces divergence curves\nand per-dimension breakdown.\n\nUsage:\n    python analyze_action_divergence_v2.py --gpu 2 --num_episodes 10 --task_ids 0,1,2\n    python analyze_action_divergence_v2.py --gpu 2 --k_ratio 0.3 --checkpoint checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\nos.environ.setdefault(\"TRANSFORMERS_OFFLINE\", \"1\")\nos.environ.setdefault(\"HF_HUB_OFFLINE\", \"1\")\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport torch\n\nARTIFACTS_DIR = Path(__file__).resolve().parent\nsys.path.insert(0, str(ARTIFACTS_DIR))\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nCHECKPOINT = \"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\"\nCONFIG = \"configs/libero_acis_stage1only_k07.yaml\"\n\nSUITE = \"libero_object\"\nMAX_STEPS = 280\nACTION_HORIZON = 50\nACTION_DIM_NAMES = [\"pos_x\", \"pos_y\", \"pos_z\", \"rot_x\", \"rot_y\", \"rot_z\", \"gripper\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--gpu\", type=int, default=2)\n    p.add_argument(\"--num_episodes\", type=int, default=10)\n    p.add_argument(\"--task_ids\", type=str, default=\"0,1,2\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--output_dir\", type=str, default=\"artifacts\")\n    p.add_argument(\"--checkpoint\", type=str, default=CHECKPOINT)\n    p.add_argument(\"--config\", type=str, default=CONFIG)\n    p.add_argument(\"--k_ratio\", type=float, default=0.5)\n    return p.parse_args()\n\n\ndef load_config(config_path: str) -> dict:\n    import yaml\n    config_path = Path(config_path)\n    with open(config_path) as f:\n        config = yaml.safe_load(f)\n    if \"_base_\" in config:\n        base_path = config_path.parent / config.pop(\"_base_\")\n        base_config = load_config(str(base_path))\n        for k, v in config.items():\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\n                base_config[k].update(v)\n            else:\n                base_config[k] = v\n        return base_config\n    return config\n\n\ndef load_model_pair(checkpoint: str, config_path: str, k_ratio: float, device):\n    \"\"\"Load the same checkpoint twice: once as baseline (no pruning), once for ACIS.\n\n    Returns (baseline_policy, acis_policy, acis_wrapper, config).\n    \"\"\"\n    from train import load_smolvla_policy, wrap_with_imm\n\n    config = load_config(config_path)\n\n    # --- Baseline: load via wrapper (to match state_dict keys), extract policy ---\n    baseline_policy = load_smolvla_policy(config, device)\n    baseline_wrapper = wrap_with_imm(baseline_policy, config)\n    baseline_wrapper.to(device)\n    ckpt = torch.load(checkpoint, map_location=device, weights_only=False)\n    baseline_wrapper.load_state_dict(ckpt[\"model_state_dict\"], strict=False)\n    baseline_wrapper.eval()\n    baseline_policy = baseline_wrapper.policy\n\n    # --- ACIS: load via wrapper, override k_ratio ---\n    acis_policy = load_smolvla_policy(config, device)\n    acis_wrapper = wrap_with_imm(acis_policy, config)\n    acis_wrapper.to(device)\n    ckpt2 = torch.load(checkpoint, map_location=device, weights_only=False)\n    acis_wrapper.load_state_dict(ckpt2[\"model_state_dict\"], strict=False)\n    acis_wrapper.k_ratio = k_ratio\n    acis_wrapper.eval()\n    acis_policy = acis_wrapper.policy\n\n    log.info(\"Loaded same checkpoint for both runs: %s\", checkpoint)\n    log.info(\"Baseline: full forward (no pruning)\")\n    log.info(\"ACIS: true_removal, k_ratio=%.2f\", k_ratio)\n\n    return baseline_policy, acis_policy, acis_wrapper, config\n\n\n# --- Observation / Action utilities ---\n\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\n    q = quat.astype(np.float64)\n    w = np.clip(q[3], -1.0, 1.0)\n    den = np.sqrt(max(1.0 - w * w, 0.0))\n    if den > 1e-10:\n        angle = 2.0 * np.arccos(w)\n        axis = q[:3] / den\n        return (axis * angle).astype(np.float32)\n    return np.zeros(3, dtype=np.float32)\n\n\ndef extract_state(obs: dict) -> np.ndarray:\n    rs = obs[\"robot_state\"]\n    eef_pos = np.asarray(rs[\"eef\"][\"pos\"], dtype=np.float32)\n    eef_quat = np.asarray(rs[\"eef\"][\"quat\"], dtype=np.float64)\n    gripper_qpos = np.asarray(rs[\"gripper\"][\"qpos\"], dtype=np.float32)\n    eef_aa = quat_to_axis_angle(eef_quat)\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\n\n\ndef obs_to_batch(obs, task_text, tokenizer, camera_keys, device):\n    batch = {}\n    for cam_key in camera_keys:\n        short_name = cam_key.split(\".\")[-1]\n        img = obs[\"pixels\"][short_name]\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\n        img_t = img_t.unsqueeze(0)\n        img_t = torch.flip(img_t, dims=[2, 3])\n        batch[cam_key] = img_t.to(device)\n    state = extract_state(obs)\n    batch[\"observation.state\"] = torch.from_numpy(state).unsqueeze(0).to(device)\n    text = task_text if task_text.endswith(\"\\n\") else task_text + \"\\n\"\n    encoded = tokenizer(\n        [text], padding=\"longest\", max_length=48, truncation=True, return_tensors=\"pt\",\n    )\n    batch[\"observation.language.tokens\"] = encoded[\"input_ids\"].to(device)\n    batch[\"observation.language.attention_mask\"] = encoded[\"attention_mask\"].bool().to(device)\n    return batch\n\n\ndef find_connector(model):\n    for name, module in model.named_modules():\n        if name.endswith(\".connector\") or \"multi_modal_projector\" in name:\n            return module\n    return None\n\n\n@torch.no_grad()\ndef compute_acis_mask(wrapper, batch, device):\n    bm = wrapper.base_model\n    images, _ = wrapper.policy.prepare_images(batch)\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\n    B = vis_tokens.shape[0]\n    noise = bm.sample_noise(\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\n    )\n    time = torch.ones(B, device=device)\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\n    scores = wrapper.acis(suffix_embs, vis_tokens)\n    N_vis = vis_tokens.shape[1]\n    k = max(1, int(N_vis * wrapper.k_ratio))\n    _, topk_idx = torch.topk(scores, k, dim=-1)\n    mask = torch.zeros(B, N_vis, device=device)\n    mask.scatter_(1, topk_idx, 1.0)\n    return mask\n\n\ndef register_acis_hook(connector, mask: torch.Tensor, method: str = \"true_removal\"):\n    \"\"\"Register forward hook on connector that prunes visual tokens.\n\n    Uses the stateful offset approach from eval_success_rate_libero.py to handle\n    multi-camera setups where the connector is called once per camera.\n    \"\"\"\n    state = {\"offset\": 0}\n\n    def hook_fn(module, input, output):\n        tokens = output[0] if isinstance(output, tuple) else output\n        if tokens.dim() != 3:\n            return output\n        n = tokens.shape[1]\n        offset = state[\"offset\"]\n        if offset + n > mask.shape[1]:\n            return output\n        cam_mask = mask[:, offset:offset + n]\n        state[\"offset\"] = offset + n\n\n        B, N, D = tokens.shape\n        keep_mask = cam_mask[:B]\n\n        if method == \"true_removal\":\n            kept = keep_mask[0].bool()\n            masked = tokens[:, kept, :]\n        else:\n            masked = tokens * keep_mask.unsqueeze(-1)\n\n        if isinstance(output, tuple):\n            return (masked,) + output[1:]\n        return masked\n\n    return connector.register_forward_hook(hook_fn)\n\n\n@torch.no_grad()\ndef predict_actions(policy, batch):\n    images, img_masks = policy.prepare_images(batch)\n    state = policy.prepare_state(batch)\n    lang_tokens = batch[\"observation.language.tokens\"]\n    lang_masks = batch[\"observation.language.attention_mask\"]\n    actions = policy.model.sample_actions(\n        images, img_masks, lang_tokens, lang_masks, state\n    )\n    original_action_dim = policy.config.action_feature.shape[0]\n    return actions[0, :, :original_action_dim]\n\n\ndef run_divergence_analysis(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    task_ids = [int(x) for x in args.task_ids.split(\",\")]\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    log.info(\"Loading model pair from same checkpoint...\")\n    baseline_policy, acis_policy, acis_wrapper, config = load_model_pair(\n        args.checkpoint, args.config, args.k_ratio, device\n    )\n\n    from train import get_tokenizer_from_policy\n    tokenizer = get_tokenizer_from_policy(baseline_policy)\n\n    camera_keys = config.get(\"dataset\", {}).get(\"features\", {}).get(\"cameras\", [\n        \"observation.images.image\", \"observation.images.image2\"\n    ])\n\n    acis_connector = find_connector(acis_policy.model)\n    if acis_connector is None:\n        raise RuntimeError(\"Cannot find connector for ACIS hook\")\n\n    from libero.libero import benchmark\n    from lerobot.envs.libero import get_task_init_states, LiberoEnv\n\n    bench_dict = benchmark.get_benchmark_dict()\n    task_suite = bench_dict[SUITE]()\n\n    all_results = {}\n\n    for task_id in task_ids:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        log.info(\"=== Task %d: %s ===\", task_id, task_desc)\n\n        env = LiberoEnv(\n            task_suite=task_suite,\n            task_id=task_id,\n            task_suite_name=SUITE,\n            camera_name=\"agentview_image,robot0_eye_in_hand_image\",\n            obs_type=\"pixels_agent_pos\",\n            observation_width=256,\n            observation_height=256,\n            init_states=True,\n            n_envs=1,\n            episode_index=0,\n            control_mode=\"relative\",\n        )\n\n        task_episodes = []\n\n        for ep in range(args.num_episodes):\n            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)\n            baseline_chunk = None\n            baseline_idx = 0\n            acis_chunk = None\n            acis_idx = 0\n            episode_data = {\n                \"task_id\": task_id,\n                \"task_desc\": task_desc,\n                \"episode\": ep,\n                \"timesteps\": [],\n            }\n\n            for step in range(MAX_STEPS):\n                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\n\n                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)\n\n                if need_replan:\n                    baseline_chunk = predict_actions(baseline_policy, batch)\n                    baseline_idx = 0\n\n                    mask = compute_acis_mask(acis_wrapper, batch, device)\n                    hook_handle = register_acis_hook(acis_connector, mask, method=\"true_removal\")\n                    acis_chunk = predict_actions(acis_policy, batch)\n                    hook_handle.remove()\n                    acis_idx = 0\n\n                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)\n                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)\n\n                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)\n                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)\n\n                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))\n                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()\n\n                episode_data[\"timesteps\"].append({\n                    \"step\": step,\n                    \"baseline_action\": baseline_action_clipped.tolist(),\n                    \"acis_action\": acis_action_clipped.tolist(),\n                    \"l2_distance\": l2_dist,\n                    \"per_dim_diff\": per_dim_diff,\n                })\n\n                baseline_idx += 1\n                acis_idx += 1\n\n                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)\n\n                if info.get(\"is_success\", False) or terminated or truncated:\n                    break\n\n            task_episodes.append(episode_data)\n            n_steps = len(episode_data[\"timesteps\"])\n            final_l2 = episode_data[\"timesteps\"][-1][\"l2_distance\"] if n_steps > 0 else 0\n            log.info(\"  Ep %d: %d steps, final L2=%.4f\", ep, n_steps, final_l2)\n\n        env.close()\n        all_results[task_id] = task_episodes\n\n    # --- Analysis ---\n    log.info(\"Computing statistics...\")\n    analysis = compute_analysis(all_results)\n\n    # Save raw data\n    json_path = output_dir / \"action_divergence_v2_data.json\"\n    with open(json_path, \"w\") as f:\n        json.dump({\n            \"metadata\": {\n                \"checkpoint\": args.checkpoint,\n                \"config\": args.config,\n                \"k_ratio\": args.k_ratio,\n                \"pruning_method\": \"true_removal\",\n                \"baseline_mode\": \"bypass (no pruning)\",\n                \"num_episodes\": args.num_episodes,\n                \"seed\": args.seed,\n            },\n            \"episodes\": all_results,\n            \"analysis\": analysis,\n        }, f, indent=2)\n    log.info(\"Raw data saved to %s\", json_path)\n\n    # Plot\n    plot_divergence_curves(all_results, analysis, output_dir, args.k_ratio)\n    log.info(\"Done.\")\n\n\ndef compute_analysis(all_results: dict) -> dict:\n    all_l2_curves = []\n    all_per_dim_curves = []\n\n    for task_id, episodes in all_results.items():\n        for ep_data in episodes:\n            steps = ep_data[\"timesteps\"]\n            l2_curve = [s[\"l2_distance\"] for s in steps]\n            per_dim = [s[\"per_dim_diff\"] for s in steps]\n            all_l2_curves.append(l2_curve)\n            all_per_dim_curves.append(per_dim)\n\n    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0\n\n    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)\n    for i, curve in enumerate(all_l2_curves):\n        padded_l2[i, :len(curve)] = curve\n\n    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()\n    std_l2 = np.nanstd(padded_l2, axis=0).tolist()\n\n    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]\n    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0\n\n    overall_mean_l2 = float(np.nanmean(padded_l2))\n\n    n_dims = 7\n    dim_abs_means = []\n    for d in range(n_dims):\n        dim_vals = []\n        for per_dim_curve in all_per_dim_curves:\n            for step_diff in per_dim_curve:\n                if len(step_diff) > d:\n                    dim_vals.append(abs(step_diff[d]))\n        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)\n\n    valid_mean = [v for v in mean_l2 if not np.isnan(v)]\n    if len(valid_mean) > 10:\n        x = np.arange(len(valid_mean))\n        slope = float(np.polyfit(x, valid_mean, 1)[0])\n    else:\n        slope = 0.0\n\n    return {\n        \"overall_mean_l2\": overall_mean_l2,\n        \"first_step_mean_l2\": avg_first_step,\n        \"l2_growth_rate_per_step\": slope,\n        \"per_dim_mean_abs_diff\": {\n            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))\n        },\n        \"mean_l2_curve\": mean_l2,\n        \"std_l2_curve\": std_l2,\n        \"num_episodes\": len(all_l2_curves),\n        \"max_episode_length\": max_len,\n    }\n\n\ndef plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path,\n                           k_ratio: float):\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\n\n    ax = axes[0]\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\n    task_ids = sorted(all_results.keys())\n\n    for ti, task_id in enumerate(task_ids):\n        episodes = all_results[task_id]\n        for ep_data in episodes:\n            steps = ep_data[\"timesteps\"]\n            l2_vals = [s[\"l2_distance\"] for s in steps]\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\n\n    mean_curve = analysis[\"mean_l2_curve\"]\n    std_curve = analysis[\"std_l2_curve\"]\n    x = np.arange(len(mean_curve))\n    ax.plot(x, mean_curve, color=\"black\", linewidth=2, label=\"Mean\")\n    mean_arr = np.array(mean_curve)\n    std_arr = np.array(std_curve)\n    valid = ~np.isnan(mean_arr)\n    ax.fill_between(\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\n        alpha=0.15, color=\"black\"\n    )\n    ax.set_xlabel(\"Timestep\")\n    ax.set_ylabel(\"L2 Action Distance\")\n    ax.set_title(f\"Same ckpt: bypass vs ACIS true_removal k={k_ratio}\")\n    ax.legend(loc=\"upper left\")\n    ax.grid(True, alpha=0.3)\n\n    ax = axes[1]\n    dim_data = analysis[\"per_dim_mean_abs_diff\"]\n    names = list(dim_data.keys())\n    values = list(dim_data.values())\n    bar_colors = [\"#2196F3\"] * 3 + [\"#FF9800\"] * 3 + [\"#4CAF50\"]\n    ax.bar(names, values, color=bar_colors)\n    ax.set_xlabel(\"Action Dimension\")\n    ax.set_ylabel(\"Mean |Difference|\")\n    ax.set_title(\"Per-Dimension Divergence\")\n    ax.set_xticklabels(names, rotation=45, ha=\"right\")\n    ax.grid(True, alpha=0.3, axis=\"y\")\n\n    ax = axes[2]\n    for ti, task_id in enumerate(task_ids):\n        episodes = all_results[task_id]\n        task_l2s = []\n        for ep_data in episodes:\n            l2_vals = [s[\"l2_distance\"] for s in ep_data[\"timesteps\"]]\n            task_l2s.append(l2_vals)\n        max_t = max(len(c) for c in task_l2s)\n        padded = np.full((len(task_l2s), max_t), np.nan)\n        for i, c in enumerate(task_l2s):\n            padded[i, :len(c)] = c\n        task_mean = np.nanmean(padded, axis=0)\n        task_desc = episodes[0][\"task_desc\"]\n        short_desc = task_desc[:30] + \"...\" if len(task_desc) > 30 else task_desc\n        ax.plot(task_mean, linewidth=1.5, label=f\"T{task_id}: {short_desc}\", color=colors[ti % 10])\n    ax.set_xlabel(\"Timestep\")\n    ax.set_ylabel(\"L2 Action Distance\")\n    ax.set_title(\"Per-Task Mean Divergence\")\n    ax.legend(fontsize=7, loc=\"upper left\")\n    ax.grid(True, alpha=0.3)\n\n    plt.tight_layout()\n    pdf_path = output_dir / \"action_divergence_v2_curve.pdf\"\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\"tight\")\n    plt.savefig(output_dir / \"action_divergence_v2_curve.png\", dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    log.info(\"Plots saved to %s\", pdf_path)\n\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\n    ax2.axis(\"off\")\n    summary_text = (\n        f\"Action Divergence Summary (same ckpt, true_removal k={k_ratio})\\n\"\n        f\"{'='*55}\\n\"\n        f\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\n\"\n        f\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\n\"\n        f\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\n\"\n        f\"Num episodes:           {analysis['num_episodes']}\\n\"\n        f\"Max episode length:     {analysis['max_episode_length']}\\n\"\n        f\"\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\n\"\n        f\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\n\"\n    )\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\n             verticalalignment=\"top\", fontfamily=\"monospace\")\n    plt.tight_layout()\n    plt.savefig(output_dir / \"action_divergence_v2_summary.pdf\", dpi=150, bbox_inches=\"tight\")\n    plt.close()\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_divergence_analysis(args)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 68_

Now upload to server and run syntax check.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "3a7681b2-d358-4c15-99b3-40a30a9ba712",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuqNTmJ5DqtVkVij23x3NK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6799,
      "cache_read_input_tokens": 62867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6799
      },
      "output_tokens": 2,
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

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01V5Cc9QmKZZRTFzHgPb7jbZ`</summary>

```json
{
  "server": "westd-27271",
  "command": "cat > /root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence_v2.py << 'SCRIPT_EOF'\n\"\"\"Per-step Action Divergence Analysis (v2): Same-checkpoint, pruning-only comparison.\n\nLoads the SAME checkpoint for both runs. BASELINE does full forward (no pruning),\nACIS applies true_removal pruning at k=0.5. Pruning is the only variable.\n\nDrives the environment with baseline actions while recording both models'\naction outputs at each timestep (same observation). Produces divergence curves\nand per-dimension breakdown.\n\nUsage:\n    python analyze_action_divergence_v2.py --gpu 2 --num_episodes 10 --task_ids 0,1,2\n    python analyze_action_divergence_v2.py --gpu 2 --k_ratio 0.3 --checkpoint checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time as time_mod\nfrom pathlib import Path\n\nos.environ.setdefault(\"MUJOCO_GL\", \"egl\")\nos.environ.setdefault(\"TRANSFORMERS_OFFLINE\", \"1\")\nos.environ.setdefault(\"HF_HUB_OFFLINE\", \"1\")\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport torch\n\nARTIFACTS_DIR = Path(__file__).resolve().parent\nsys.path.insert(0, str(ARTIFACTS_DIR))\nsys.path.insert(0, str(ARTIFACTS_DIR.parent))\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nCHECKPOINT = \"checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt\"\nCONFIG = \"configs/libero_acis_stage1only_k07.yaml\"\n\nSUITE = \"libero_object\"\nMAX_STEPS = 280\nACTION_HORIZON = 50\nACTION_DIM_NAMES = [\"pos_x\", \"pos_y\", \"pos_z\", \"rot_x\", \"rot_y\", \"rot_z\", \"gripper\"]\n\n\ndef parse_args():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--gpu\", type=int, default=2)\n    p.add_argument(\"--num_episodes\", type=int, default=10)\n    p.add_argument(\"--task_ids\", type=str, default=\"0,1,2\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--output_dir\", type=str, default=\"artifacts\")\n    p.add_argument(\"--checkpoint\", type=str, default=CHECKPOINT)\n    p.add_argument(\"--config\", type=str, default=CONFIG)\n    p.add_argument(\"--k_ratio\", type=float, default=0.5)\n    return p.parse_args()\n\n\ndef load_config(config_path: str) -> dict:\n    import yaml\n    config_path = Path(config_path)\n    with open(config_path) as f:\n        config = yaml.safe_load(f)\n    if \"_base_\" in config:\n        base_path = config_path.parent / config.pop(\"_base_\")\n        base_config = load_config(str(base_path))\n        for k, v in config.items():\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\n                base_config[k].update(v)\n            else:\n                base_config[k] = v\n        return base_config\n    return config\n\n\ndef load_model_pair(checkpoint: str, config_path: str, k_ratio: float, device):\n    \"\"\"Load the same checkpoint twice: once as baseline (no pruning), once for ACIS.\n\n    Returns (baseline_policy, acis_policy, acis_wrapper, config).\n    \"\"\"\n    from train import load_smolvla_policy, wrap_with_imm\n\n    config = load_config(config_path)\n\n    # --- Baseline: load via wrapper (to match state_dict keys), extract policy ---\n    baseline_policy = load_smolvla_policy(config, device)\n    baseline_wrapper = wrap_with_imm(baseline_policy, config)\n    baseline_wrapper.to(device)\n    ckpt = torch.load(checkpoint, map_location=device, weights_only=False)\n    baseline_wrapper.load_state_dict(ckpt[\"model_state_dict\"], strict=False)\n    baseline_wrapper.eval()\n    baseline_policy = baseline_wrapper.policy\n\n    # --- ACIS: load via wrapper, override k_ratio ---\n    acis_policy = load_smolvla_policy(config, device)\n    acis_wrapper = wrap_with_imm(acis_policy, config)\n    acis_wrapper.to(device)\n    ckpt2 = torch.load(checkpoint, map_location=device, weights_only=False)\n    acis_wrapper.load_state_dict(ckpt2[\"model_state_dict\"], strict=False)\n    acis_wrapper.k_ratio = k_ratio\n    acis_wrapper.eval()\n    acis_policy = acis_wrapper.policy\n\n    log.info(\"Loaded same checkpoint for both runs: %s\", checkpoint)\n    log.info(\"Baseline: full forward (no pruning)\")\n    log.info(\"ACIS: true_removal, k_ratio=%.2f\", k_ratio)\n\n    return baseline_policy, acis_policy, acis_wrapper, config\n\n\n# --- Observation / Action utilities ---\n\ndef quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:\n    q = quat.astype(np.float64)\n    w = np.clip(q[3], -1.0, 1.0)\n    den = np.sqrt(max(1.0 - w * w, 0.0))\n    if den > 1e-10:\n        angle = 2.0 * np.arccos(w)\n        axis = q[:3] / den\n        return (axis * angle).astype(np.float32)\n    return np.zeros(3, dtype=np.float32)\n\n\ndef extract_state(obs: dict) -> np.ndarray:\n    rs = obs[\"robot_state\"]\n    eef_pos = np.asarray(rs[\"eef\"][\"pos\"], dtype=np.float32)\n    eef_quat = np.asarray(rs[\"eef\"][\"quat\"], dtype=np.float64)\n    gripper_qpos = np.asarray(rs[\"gripper\"][\"qpos\"], dtype=np.float32)\n    eef_aa = quat_to_axis_angle(eef_quat)\n    return np.concatenate([eef_pos, eef_aa, gripper_qpos])\n\n\ndef obs_to_batch(obs, task_text, tokenizer, camera_keys, device):\n    batch = {}\n    for cam_key in camera_keys:\n        short_name = cam_key.split(\".\")[-1]\n        img = obs[\"pixels\"][short_name]\n        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0\n        img_t = img_t.unsqueeze(0)\n        img_t = torch.flip(img_t, dims=[2, 3])\n        batch[cam_key] = img_t.to(device)\n    state = extract_state(obs)\n    batch[\"observation.state\"] = torch.from_numpy(state).unsqueeze(0).to(device)\n    text = task_text if task_text.endswith(\"\\n\") else task_text + \"\\n\"\n    encoded = tokenizer(\n        [text], padding=\"longest\", max_length=48, truncation=True, return_tensors=\"pt\",\n    )\n    batch[\"observation.language.tokens\"] = encoded[\"input_ids\"].to(device)\n    batch[\"observation.language.attention_mask\"] = encoded[\"attention_mask\"].bool().to(device)\n    return batch\n\n\ndef find_connector(model):\n    for name, module in model.named_modules():\n        if name.endswith(\".connector\") or \"multi_modal_projector\" in name:\n            return module\n    return None\n\n\n@torch.no_grad()\ndef compute_acis_mask(wrapper, batch, device):\n    bm = wrapper.base_model\n    images, _ = wrapper.policy.prepare_images(batch)\n    vis_tokens, _ = wrapper._get_visual_tokens(images)\n    B = vis_tokens.shape[0]\n    noise = bm.sample_noise(\n        (B, bm.config.chunk_size, bm.config.max_action_dim), device\n    )\n    time = torch.ones(B, device=device)\n    suffix_embs, _, _ = bm.embed_suffix(noise, time)\n    scores = wrapper.acis(suffix_embs, vis_tokens)\n    N_vis = vis_tokens.shape[1]\n    k = max(1, int(N_vis * wrapper.k_ratio))\n    _, topk_idx = torch.topk(scores, k, dim=-1)\n    mask = torch.zeros(B, N_vis, device=device)\n    mask.scatter_(1, topk_idx, 1.0)\n    return mask\n\n\ndef register_acis_hook(connector, mask: torch.Tensor, method: str = \"true_removal\"):\n    \"\"\"Register forward hook on connector that prunes visual tokens.\n\n    Uses the stateful offset approach from eval_success_rate_libero.py to handle\n    multi-camera setups where the connector is called once per camera.\n    \"\"\"\n    state = {\"offset\": 0}\n\n    def hook_fn(module, input, output):\n        tokens = output[0] if isinstance(output, tuple) else output\n        if tokens.dim() != 3:\n            return output\n        n = tokens.shape[1]\n        offset = state[\"offset\"]\n        if offset + n > mask.shape[1]:\n            return output\n        cam_mask = mask[:, offset:offset + n]\n        state[\"offset\"] = offset + n\n\n        B, N, D = tokens.shape\n        keep_mask = cam_mask[:B]\n\n        if method == \"true_removal\":\n            kept = keep_mask[0].bool()\n            masked = tokens[:, kept, :]\n        else:\n            masked = tokens * keep_mask.unsqueeze(-1)\n\n        if isinstance(output, tuple):\n            return (masked,) + output[1:]\n        return masked\n\n    return connector.register_forward_hook(hook_fn)\n\n\n@torch.no_grad()\ndef predict_actions(policy, batch):\n    images, img_masks = policy.prepare_images(batch)\n    state = policy.prepare_state(batch)\n    lang_tokens = batch[\"observation.language.tokens\"]\n    lang_masks = batch[\"observation.language.attention_mask\"]\n    actions = policy.model.sample_actions(\n        images, img_masks, lang_tokens, lang_masks, state\n    )\n    original_action_dim = policy.config.action_feature.shape[0]\n    return actions[0, :, :original_action_dim]\n\n\ndef run_divergence_analysis(args):\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    task_ids = [int(x) for x in args.task_ids.split(\",\")]\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    log.info(\"Loading model pair from same checkpoint...\")\n    baseline_policy, acis_policy, acis_wrapper, config = load_model_pair(\n        args.checkpoint, args.config, args.k_ratio, device\n    )\n\n    from train import get_tokenizer_from_policy\n    tokenizer = get_tokenizer_from_policy(baseline_policy)\n\n    camera_keys = config.get(\"dataset\", {}).get(\"features\", {}).get(\"cameras\", [\n        \"observation.images.image\", \"observation.images.image2\"\n    ])\n\n    acis_connector = find_connector(acis_policy.model)\n    if acis_connector is None:\n        raise RuntimeError(\"Cannot find connector for ACIS hook\")\n\n    from libero.libero import benchmark\n    from lerobot.envs.libero import get_task_init_states, LiberoEnv\n\n    bench_dict = benchmark.get_benchmark_dict()\n    task_suite = bench_dict[SUITE]()\n\n    all_results = {}\n\n    for task_id in task_ids:\n        task = task_suite.get_task(task_id)\n        task_desc = task.language\n        log.info(\"=== Task %d: %s ===\", task_id, task_desc)\n\n        env = LiberoEnv(\n            task_suite=task_suite,\n            task_id=task_id,\n            task_suite_name=SUITE,\n            camera_name=\"agentview_image,robot0_eye_in_hand_image\",\n            obs_type=\"pixels_agent_pos\",\n            observation_width=256,\n            observation_height=256,\n            init_states=True,\n            n_envs=1,\n            episode_index=0,\n            control_mode=\"relative\",\n        )\n\n        task_episodes = []\n\n        for ep in range(args.num_episodes):\n            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)\n            baseline_chunk = None\n            baseline_idx = 0\n            acis_chunk = None\n            acis_idx = 0\n            episode_data = {\n                \"task_id\": task_id,\n                \"task_desc\": task_desc,\n                \"episode\": ep,\n                \"timesteps\": [],\n            }\n\n            for step in range(MAX_STEPS):\n                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)\n\n                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)\n\n                if need_replan:\n                    baseline_chunk = predict_actions(baseline_policy, batch)\n                    baseline_idx = 0\n\n                    mask = compute_acis_mask(acis_wrapper, batch, device)\n                    hook_handle = register_acis_hook(acis_connector, mask, method=\"true_removal\")\n                    acis_chunk = predict_actions(acis_policy, batch)\n                    hook_handle.remove()\n                    acis_idx = 0\n\n                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)\n                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)\n\n                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)\n                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)\n\n                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))\n                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()\n\n                episode_data[\"timesteps\"].append({\n                    \"step\": step,\n                    \"baseline_action\": baseline_action_clipped.tolist(),\n                    \"acis_action\": acis_action_clipped.tolist(),\n                    \"l2_distance\": l2_dist,\n                    \"per_dim_diff\": per_dim_diff,\n                })\n\n                baseline_idx += 1\n                acis_idx += 1\n\n                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)\n\n                if info.get(\"is_success\", False) or terminated or truncated:\n                    break\n\n            task_episodes.append(episode_data)\n            n_steps = len(episode_data[\"timesteps\"])\n            final_l2 = episode_data[\"timesteps\"][-1][\"l2_distance\"] if n_steps > 0 else 0\n            log.info(\"  Ep %d: %d steps, final L2=%.4f\", ep, n_steps, final_l2)\n\n        env.close()\n        all_results[task_id] = task_episodes\n\n    # --- Analysis ---\n    log.info(\"Computing statistics...\")\n    analysis = compute_analysis(all_results)\n\n    # Save raw data\n    json_path = output_dir / \"action_divergence_v2_data.json\"\n    with open(json_path, \"w\") as f:\n        json.dump({\n            \"metadata\": {\n                \"checkpoint\": args.checkpoint,\n                \"config\": args.config,\n                \"k_ratio\": args.k_ratio,\n                \"pruning_method\": \"true_removal\",\n                \"baseline_mode\": \"bypass (no pruning)\",\n                \"num_episodes\": args.num_episodes,\n                \"seed\": args.seed,\n            },\n            \"episodes\": all_results,\n            \"analysis\": analysis,\n        }, f, indent=2)\n    log.info(\"Raw data saved to %s\", json_path)\n\n    # Plot\n    plot_divergence_curves(all_results, analysis, output_dir, args.k_ratio)\n    log.info(\"Done.\")\n\n\ndef compute_analysis(all_results: dict) -> dict:\n    all_l2_curves = []\n    all_per_dim_curves = []\n\n    for task_id, episodes in all_results.items():\n        for ep_data in episodes:\n            steps = ep_data[\"timesteps\"]\n            l2_curve = [s[\"l2_distance\"] for s in steps]\n            per_dim = [s[\"per_dim_diff\"] for s in steps]\n            all_l2_curves.append(l2_curve)\n            all_per_dim_curves.append(per_dim)\n\n    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0\n\n    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)\n    for i, curve in enumerate(all_l2_curves):\n        padded_l2[i, :len(curve)] = curve\n\n    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()\n    std_l2 = np.nanstd(padded_l2, axis=0).tolist()\n\n    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]\n    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0\n\n    overall_mean_l2 = float(np.nanmean(padded_l2))\n\n    n_dims = 7\n    dim_abs_means = []\n    for d in range(n_dims):\n        dim_vals = []\n        for per_dim_curve in all_per_dim_curves:\n            for step_diff in per_dim_curve:\n                if len(step_diff) > d:\n                    dim_vals.append(abs(step_diff[d]))\n        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)\n\n    valid_mean = [v for v in mean_l2 if not np.isnan(v)]\n    if len(valid_mean) > 10:\n        x = np.arange(len(valid_mean))\n        slope = float(np.polyfit(x, valid_mean, 1)[0])\n    else:\n        slope = 0.0\n\n    return {\n        \"overall_mean_l2\": overall_mean_l2,\n        \"first_step_mean_l2\": avg_first_step,\n        \"l2_growth_rate_per_step\": slope,\n        \"per_dim_mean_abs_diff\": {\n            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))\n        },\n        \"mean_l2_curve\": mean_l2,\n        \"std_l2_curve\": std_l2,\n        \"num_episodes\": len(all_l2_curves),\n        \"max_episode_length\": max_len,\n    }\n\n\ndef plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path,\n                           k_ratio: float):\n    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))\n\n    ax = axes[0]\n    colors = plt.cm.tab10(np.linspace(0, 1, 10))\n    task_ids = sorted(all_results.keys())\n\n    for ti, task_id in enumerate(task_ids):\n        episodes = all_results[task_id]\n        for ep_data in episodes:\n            steps = ep_data[\"timesteps\"]\n            l2_vals = [s[\"l2_distance\"] for s in steps]\n            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)\n\n    mean_curve = analysis[\"mean_l2_curve\"]\n    std_curve = analysis[\"std_l2_curve\"]\n    x = np.arange(len(mean_curve))\n    ax.plot(x, mean_curve, color=\"black\", linewidth=2, label=\"Mean\")\n    mean_arr = np.array(mean_curve)\n    std_arr = np.array(std_curve)\n    valid = ~np.isnan(mean_arr)\n    ax.fill_between(\n        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],\n        alpha=0.15, color=\"black\"\n    )\n    ax.set_xlabel(\"Timestep\")\n    ax.set_ylabel(\"L2 Action Distance\")\n    ax.set_title(f\"Same ckpt: bypass vs ACIS true_removal k={k_ratio}\")\n    ax.legend(loc=\"upper left\")\n    ax.grid(True, alpha=0.3)\n\n    ax = axes[1]\n    dim_data = analysis[\"per_dim_mean_abs_diff\"]\n    names = list(dim_data.keys())\n    values = list(dim_data.values())\n    bar_colors = [\"#2196F3\"] * 3 + [\"#FF9800\"] * 3 + [\"#4CAF50\"]\n    ax.bar(names, values, color=bar_colors)\n    ax.set_xlabel(\"Action Dimension\")\n    ax.set_ylabel(\"Mean |Difference|\")\n    ax.set_title(\"Per-Dimension Divergence\")\n    ax.set_xticklabels(names, rotation=45, ha=\"right\")\n    ax.grid(True, alpha=0.3, axis=\"y\")\n\n    ax = axes[2]\n    for ti, task_id in enumerate(task_ids):\n        episodes = all_results[task_id]\n        task_l2s = []\n        for ep_data in episodes:\n            l2_vals = [s[\"l2_distance\"] for s in ep_data[\"timesteps\"]]\n            task_l2s.append(l2_vals)\n        max_t = max(len(c) for c in task_l2s)\n        padded = np.full((len(task_l2s), max_t), np.nan)\n        for i, c in enumerate(task_l2s):\n            padded[i, :len(c)] = c\n        task_mean = np.nanmean(padded, axis=0)\n        task_desc = episodes[0][\"task_desc\"]\n        short_desc = task_desc[:30] + \"...\" if len(task_desc) > 30 else task_desc\n        ax.plot(task_mean, linewidth=1.5, label=f\"T{task_id}: {short_desc}\", color=colors[ti % 10])\n    ax.set_xlabel(\"Timestep\")\n    ax.set_ylabel(\"L2 Action Distance\")\n    ax.set_title(\"Per-Task Mean Divergence\")\n    ax.legend(fontsize=7, loc=\"upper left\")\n    ax.grid(True, alpha=0.3)\n\n    plt.tight_layout()\n    pdf_path = output_dir / \"action_divergence_v2_curve.pdf\"\n    plt.savefig(pdf_path, dpi=150, bbox_inches=\"tight\")\n    plt.savefig(output_dir / \"action_divergence_v2_curve.png\", dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    log.info(\"Plots saved to %s\", pdf_path)\n\n    fig2, ax2 = plt.subplots(figsize=(6, 3))\n    ax2.axis(\"off\")\n    summary_text = (\n        f\"Action Divergence Summary (same ckpt, true_removal k={k_ratio})\\n\"\n        f\"{'='*55}\\n\"\n        f\"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\\n\"\n        f\"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\\n\"\n        f\"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\\n\"\n        f\"Num episodes:           {analysis['num_episodes']}\\n\"\n        f\"Max episode length:     {analysis['max_episode_length']}\\n\"\n        f\"\\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\\n\"\n        f\"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\\n\"\n    )\n    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,\n             verticalalignment=\"top\", fontfamily=\"monospace\")\n    plt.tight_layout()\n    plt.savefig(output_dir / \"action_divergence_v2_summary.pdf\", dpi=150, bbox_inches=\"tight\")\n    plt.close()\n\n\nif __name__ == \"__main__\":\n    args = parse_args()\n    run_divergence_analysis(args)\nSCRIPT_EOF",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "59acefb9-e364-4a3f-936f-3023c0886db8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuqNTmJ5DqtVkVij23x3NK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6799,
      "cache_read_input_tokens": 62867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6799
      },
      "output_tokens": 2,
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

_source line 70 · 2026-05-17T10:42:51.924Z_

<details><summary>↩ Tool result · `toolu_01V5Cc9QmKZZRTFzHgPb7jbZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.17}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "4484e1e8-5894-4dcf-b7eb-fd04ece5488d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.17}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.17}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_012bb97moqVPEJoUHcVmyBDW`</summary>

```json
{
  "server": "westd-27271",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -c \"import ast; ast.parse(open('artifacts/analyze_action_divergence_v2.py').read()); print('Syntax OK')\"",
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
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "a0d6986b-43ed-4006-9be1-6bed3c17eea1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkbHwkqGpE69JEoxTdb1MV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6952,
      "cache_read_input_tokens": 69666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6952
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

_source line 72 · 2026-05-17T10:43:01.149Z_

<details><summary>↩ Tool result · `toolu_012bb97moqVPEJoUHcVmyBDW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Syntax OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "4bf763be-ede8-40be-a09f-d5bef5763f4d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Syntax OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Syntax OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 73_

语法通过。

v1 → v2 的关键修改：

1. **同一 checkpoint**：两个模型都从 `libero_acis_stage1only_k07/stage1_done/checkpoint.pt` 加载（通过 `load_model_pair` 函数），消除 checkpoint 差异作为混杂变量
2. **Baseline = bypass**：加载 wrapper（确保 state_dict key 匹配），但不注册任何 pruning hook，全 128 tokens forward
3. **ACIS = true_removal**：使用 eval 脚本中带 offset 状态的 `register_acis_hook`（支持多相机），method 设为 `true_removal`，`k_ratio=0.5`
4. **默认 episodes**：`--num_episodes` 从 5 改为 10
5. **可配置**：新增 `--checkpoint`、`--config`、`--k_ratio` 参数，可灵活测试不同 k 值（如 `--k_ratio 0.3 --checkpoint .../k03/...`）
6. **输出文件**：JSON/图表输出为 `*_v2_*` 后缀，不覆盖原版

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "uuid": "e4f56800-20df-4771-b062-09053c79a32b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCAhW3nW6ZYRs8SznH8NQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 76618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
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

_source line 74_

语法通过。

v1 → v2 的关键修改：

1. **同一 checkpoint**：两个模型都从 `libero_acis_stage1only_k07/stage1_done/checkpoint.pt` 加载（通过 `load_model_pair` 函数），消除 checkpoint 差异作为混杂变量
2. **Baseline = bypass**：加载 wrapper（确保 state_dict key 匹配），但不注册任何 pruning hook，全 128 tokens forward
3. **ACIS = true_removal**：使用 eval 脚本中带 offset 状态的 `register_acis_hook`（支持多相机），method 设为 `true_removal`，`k_ratio=0.5`
4. **默认 episodes**：`--num_episodes` 从 5 改为 10
5. **可配置**：新增 `--checkpoint`、`--config`、`--k_ratio` 参数，可灵活测试不同 k 值（如 `--k_ratio 0.3 --checkpoint .../k03/...`）
6. **输出文件**：JSON/图表输出为 `*_v2_*` 后缀，不覆盖原版

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 357039,
  "duration_api_ms": 326571,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "235c7d89-ece9-4ab3-9bdf-78b2aad11e5a",
  "total_cost_usd": 1.2761874999999998,
  "usage": {
    "input_tokens": 23,
    "cache_creation_input_tokens": 65032,
    "cache_read_input_tokens": 811973,
    "output_tokens": 18488,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 65032,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 333,
        "cache_read_input_tokens": 76618,
        "cache_creation_input_tokens": 255,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 255
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1366,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001436,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 23,
      "outputTokens": 18488,
      "cacheReadInputTokens": 811973,
      "cacheCreationInputTokens": 65032,
      "webSearchRequests": 0,
      "costUSD": 1.2747514999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "750bf6a3-83fc-4505-81ea-00e1f03e7cf4"
}
```

</details>

---
