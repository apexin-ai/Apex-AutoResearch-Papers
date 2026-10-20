# analysis e5 bootstrap ci reward — Part 2 of 2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-e5-bootstrap-ci-reward.md) · [Structured JSON](../../../sessions/ba/baacede3614b06c7a01c.json)

## Round 2

### Tool result

_source line 442 · 2026-05-18T10:19:33.883Z_

<details><summary>↩ Tool result · `toolu_01BpaM4Ji6a4W2Q3GfuwSfNZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "3c4cb7be-84f7-4403-bf6e-b68919288f57",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_analysis.py",
    "content": "import json\nimport numpy as np\n\nnp.random.seed(42)\n\n# === Raw data from W&B and logs ===\nsteps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\n\ndata = {\n    \"cka_only\": {\n        \"reward_mean\": [0.253125, 0.218125, 0.25, 0.234375, 0.354375, 0.299375, 0.3075, 0.341875, 0.241875, 0.344375],\n        \"reward_std\":  [0.387209, 0.359799, 0.389845, 0.349655, 0.454006, 0.390239, 0.421871, 0.432306, 0.349333, 0.444011],\n        \"frac_zero_std\": [0.175, 0.2, 0.2, 0.35, 0.15, 0.2, 0.125, 0.25, 0.3, 0.2],\n        \"wandb_run_id\": \"li451oi4\",\n        \"source\": \"wandb\"\n    },\n    \"standard\": {\n        \"reward_mean\": [0.05125, 0.055625, 0.066875, 0.08125, 0.01875, 0.043125, 0.046875, 0.045625, 0.030625, 0.05375],\n        \"reward_std\":  [0.167951, 0.165603, 0.206658, 0.216719, 0.052165, 0.125806, 0.135433, 0.147164, 0.066939, 0.14187],\n        \"frac_zero_std\": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55],\n        \"wandb_run_id\": \"tyv20u2k\",\n        \"source\": \"wandb\"\n    },\n    \"rasp\": {\n        \"reward_mean\": [0.016875, 0.020625, 0.0225, 0.02125, 0.06125, 0.053125, 0.055625, 0.03, 0.015, 0.01],\n        \"reward_std\":  [0.058262, 0.064115, 0.053727, 0.069157, 0.201187, 0.17678, 0.158018, 0.109178, 0.06, 0.04],\n        \"frac_zero_std\": [0.85, 0.85, 0.8, 0.85, 0.725, 0.75, 0.675, 0.775, 0.9, 0.85],\n        \"wandb_run_id\": \"s5zf5akl\",\n        \"source\": \"wandb\"\n    },\n    \"random\": {\n        \"reward_mean\": [0.1606, 0.1419, 0.1663, 0.145, 0.175, 0.1844, 0.19, 0.1419, 0.1725, None],\n        \"reward_std\":  [0.3094, 0.28, 0.3471, 0.3033, 0.3244, 0.3162, 0.3493, 0.2674, 0.2861, None],\n        \"frac_zero_std\": [0.3, 0.325, 0.325, 0.4, 0.3, 0.35, 0.3, 0.375, 0.325, None],\n        \"wandb_run_id\": None,\n        \"source\": \"log_file (crashed before step 100, no W&B sync)\"\n    }\n}\n\n# === Bootstrap parameters ===\nN_BOOTSTRAP = 10000\nCONFIDENCE_LEVEL = 0.95\n# Effective sample size per logging interval:\n# per_device_train_batch_size=2, num_generations=4, logged every 10 steps\n# n = 2 prompts × 4 generations × 10 steps = 80 completions\nN_SAMPLES_PER_INTERVAL = 80\n\nalpha = 1 - CONFIDENCE_LEVEL\nmethods = [\"cka_only\", \"standard\", \"rasp\", \"random\"]\npairs = []\nfor i, m1 in enumerate(methods):\n    for m2 in methods[i+1:]:\n        pairs.append((m1, m2))\n\n# === Parametric bootstrap ===\nresults = {\n    \"metadata\": {\n        \"analysis\": \"Bootstrap CI on reward trajectory gaps\",\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"confidence_level\": CONFIDENCE_LEVEL,\n        \"n_samples_per_interval\": N_SAMPLES_PER_INTERVAL,\n        \"limitation\": (\n            \"W&B only stores aggregate metrics (mean, std) per logging interval, \"\n            \"not per-sample rewards. We use PARAMETRIC bootstrap: at each step, \"\n            \"sample the mean from Normal(mu, sigma^2/n) where n=80 is the estimated \"\n            \"effective sample size (2 prompts × 4 generations × 10 steps per interval). \"\n            \"This assumes approximate normality of the sample mean (CLT with n=80). \"\n            \"True non-parametric bootstrap would require per-sample reward data.\"\n        ),\n        \"random_note\": \"grpo_random_20 crashed at step 90; step 100 is missing.\",\n        \"methods\": {k: {\"wandb_run_id\": v[\"wandb_run_id\"], \"source\": v[\"source\"]}\n                    for k, v in data.items()}\n    },\n    \"per_step_rewards\": {},\n    \"pairwise_gaps\": {},\n    \"trajectory_summary\": {}\n}\n\n# Store per-step rewards\nfor step_idx, step in enumerate(steps):\n    step_key = f\"step_{step}\"\n    results[\"per_step_rewards\"][step_key] = {}\n    for method in methods:\n        mu = data[method][\"reward_mean\"][step_idx]\n        sigma = data[method][\"reward_std\"][step_idx]\n        if mu is not None:\n            se = sigma / np.sqrt(N_SAMPLES_PER_INTERVAL)\n            results[\"per_step_rewards\"][step_key][method] = {\n                \"mean\": mu,\n                \"std\": sigma,\n                \"se\": round(se, 6),\n                \"ci_95_lower\": round(mu - 1.96 * se, 6),\n                \"ci_95_upper\": round(mu + 1.96 * se, 6)\n            }\n\n# Pairwise gap bootstrap\nfor m1, m2 in pairs:\n    pair_key = f\"{m1}_vs_{m2}\"\n    results[\"pairwise_gaps\"][pair_key] = {}\n\n    for step_idx, step in enumerate(steps):\n        step_key = f\"step_{step}\"\n        mu1 = data[m1][\"reward_mean\"][step_idx]\n        mu2 = data[m2][\"reward_mean\"][step_idx]\n        s1 = data[m1][\"reward_std\"][step_idx]\n        s2 = data[m2][\"reward_std\"][step_idx]\n\n        if mu1 is None or mu2 is None:\n            results[\"pairwise_gaps\"][pair_key][step_key] = {\n                \"gap\": None,\n                \"note\": \"missing data for one or both methods\"\n            }\n            continue\n\n        se1 = s1 / np.sqrt(N_SAMPLES_PER_INTERVAL)\n        se2 = s2 / np.sqrt(N_SAMPLES_PER_INTERVAL)\n\n        boot_m1 = np.random.normal(mu1, se1, N_BOOTSTRAP)\n        boot_m2 = np.random.normal(mu2, se2, N_BOOTSTRAP)\n        boot_gap = boot_m1 - boot_m2\n\n        ci_lower = float(np.percentile(boot_gap, 100 * alpha / 2))\n        ci_upper = float(np.percentile(boot_gap, 100 * (1 - alpha / 2)))\n        gap_mean = float(np.mean(boot_gap))\n        gap_se = float(np.std(boot_gap))\n\n        significant = (ci_lower > 0) or (ci_upper < 0)\n\n        results[\"pairwise_gaps\"][pair_key][step_key] = {\n            \"gap_observed\": round(mu1 - mu2, 6),\n            \"gap_bootstrap_mean\": round(gap_mean, 6),\n            \"gap_bootstrap_se\": round(gap_se, 6),\n            \"ci_95\": [round(ci_lower, 6), round(ci_upper, 6)],\n            \"significant\": significant,\n            \"favors\": m1 if (mu1 - mu2) > 0 else m2\n        }\n\n# Trajectory-level summary: average gap over all available steps\nfor m1, m2 in pairs:\n    pair_key = f\"{m1}_vs_{m2}\"\n    all_gaps = []\n    all_boot_gaps = np.zeros(N_BOOTSTRAP)\n    n_valid = 0\n\n    for step_idx, step in enumerate(steps):\n        mu1 = data[m1][\"reward_mean\"][step_idx]\n        mu2 = data[m2][\"reward_mean\"][step_idx]\n        s1 = data[m1][\"reward_std\"][step_idx]\n        s2 = data[m2][\"reward_std\"][step_idx]\n\n        if mu1 is None or mu2 is None:\n            continue\n\n        se1 = s1 / np.sqrt(N_SAMPLES_PER_INTERVAL)\n        se2 = s2 / np.sqrt(N_SAMPLES_PER_INTERVAL)\n\n        boot_m1 = np.random.normal(mu1, se1, N_BOOTSTRAP)\n        boot_m2 = np.random.normal(mu2, se2, N_BOOTSTRAP)\n        all_boot_gaps += (boot_m1 - boot_m2)\n        all_gaps.append(mu1 - mu2)\n        n_valid += 1\n\n    if n_valid > 0:\n        avg_boot_gap = all_boot_gaps / n_valid\n        ci_lower = float(np.percentile(avg_boot_gap, 2.5))\n        ci_upper = float(np.percentile(avg_boot_gap, 97.5))\n        results[\"trajectory_summary\"][pair_key] = {\n            \"mean_gap_observed\": round(np.mean(all_gaps), 6),\n            \"mean_gap_bootstrap\": round(float(np.mean(avg_boot_gap)), 6),\n            \"ci_95\": [round(ci_lower, 6), round(ci_upper, 6)],\n            \"n_steps_compared\": n_valid,\n            \"significant\": (ci_lower > 0) or (ci_upper < 0),\n            \"favors\": m1 if np.mean(all_gaps) > 0 else m2\n        }\n\n# === Sensitivity analysis: vary n ===\nsensitivity = {}\nfor n_eff in [40, 80, 160]:\n    key = f\"n_eff_{n_eff}\"\n    sensitivity[key] = {}\n    for m1, m2 in pairs:\n        pair_key = f\"{m1}_vs_{m2}\"\n        all_boot_gaps = np.zeros(N_BOOTSTRAP)\n        n_valid = 0\n        for step_idx in range(len(steps)):\n            mu1 = data[m1][\"reward_mean\"][step_idx]\n            mu2 = data[m2][\"reward_mean\"][step_idx]\n            s1 = data[m1][\"reward_std\"][step_idx]\n            s2 = data[m2][\"reward_std\"][step_idx]\n            if mu1 is None or mu2 is None:\n                continue\n            se1 = s1 / np.sqrt(n_eff)\n            se2 = s2 / np.sqrt(n_eff)\n            boot_m1 = np.random.normal(mu1, se1, N_BOOTSTRAP)\n            boot_m2 = np.random.normal(mu2, se2, N_BOOTSTRAP)\n            all_boot_gaps += (boot_m1 - boot_m2)\n            n_valid += 1\n        if n_valid > 0:\n            avg_boot_gap = all_boot_gaps / n_valid\n            ci_lower = float(np.percentile(avg_boot_gap, 2.5))\n            ci_upper = float(np.percentile(avg_boot_gap, 97.5))\n            sensitivity[key][pair_key] = {\n                \"ci_95\": [round(ci_lower, 6), round(ci_upper, 6)],\n                \"significant\": (ci_lower > 0) or (ci_upper < 0)\n            }\n\nresults[\"sensitivity_n_eff\"] = sensitivity\n\n# Write output\noutput_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_reward_trajectories.json\"\nwith open(output_path, \"w\") as f:\n    json.dump(results, f, indent=2)\n\nprint(f\"Written to {output_path}\")\nprint(f\"\\n=== Trajectory-level summary (mean gap over all steps, 95% CI) ===\")\nfor pair_key, v in results[\"trajectory_summary\"].items():\n    sig = \"***\" if v[\"significant\"] else \"n.s.\"\n    print(f\"  {pair_key}: gap={v['mean_gap_observed']:.4f}, CI=[{v['ci_95'][0]:.4f}, {v['ci_95'][1]:.4f}] {sig} favors {v['favors']}\")\n\nprint(f\"\\n=== Per-step significant gaps (step 100) ===\")\nfor pair_key, steps_data in results[\"pairwise_gaps\"].items():\n    s100 = steps_data.get(\"step_100\", {})\n    if s100.get(\"gap_observed\") is not None:\n        sig = \"***\" if s100[\"significant\"] else \"n.s.\"\n        print(f\"  {pair_key}: gap={s100['gap_observed']:.4f}, CI=[{s100['ci_95'][0]:.4f}, {s100['ci_95'][1]:.4f}] {sig}\")\n    else:\n        print(f\"  {pair_key}: step 100 data missing\")\n\nprint(f\"\\n=== Sensitivity to n_eff (trajectory mean gap) ===\")\nfor n_key, pairs_data in results[\"sensitivity_n_eff\"].items():\n    print(f\"  {n_key}:\")\n    for pair_key, v in pairs_data.items():\n        sig = \"***\" if v[\"significant\"] else \"n.s.\"\n        print(f\"    {pair_key}: CI=[{v['ci_95'][0]:.4f}, {v['ci_95'][1]:.4f}] {sig}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 443_

<details open><summary>🔧 Tool call — Bash · `toolu_017Y6WsErxGSFTW2MJbJdCDj`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts && python bootstrap_ci_analysis.py",
  "description": "Run bootstrap CI analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "dd04103e-162d-4d0f-bedb-cad5e4b48a1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TF3cm9vJVFpikXDy5G5XuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5685,
      "cache_read_input_tokens": 76736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5685
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

_source line 444 · 2026-05-18T10:19:37.211Z_

<details><summary>↩ Tool result · reported error · `toolu_017Y6WsErxGSFTW2MJbJdCDj`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "acc1ea94-1855-4fa9-9da5-9f2cea2e356c",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---


### Tool call

_source line 445_

<details open><summary>🔧 Tool call — Bash · `toolu_01XwnUTRr3oFTrdu1tHqZiNK`</summary>

```json
{
  "command": "python3 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_analysis.py",
  "description": "Run bootstrap CI analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "3de36624-b093-45f4-a45a-174670ab1920",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgxGugZGFNFMLybeoccxY6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 82421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 152
      },
      "output_tokens": 70,
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

_source line 446 · 2026-05-18T10:19:41.105Z_

<details><summary>↩ Tool result · `toolu_01XwnUTRr3oFTrdu1tHqZiNK`</summary>

```text
Written to /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_reward_trajectories.json

=== Trajectory-level summary (mean gap over all steps, 95% CI) ===
  cka_only_vs_standard: gap=0.2351, CI=[0.2048, 0.2646] *** favors cka_only
  cka_only_vs_rasp: gap=0.2539, CI=[0.2241, 0.2822] *** favors cka_only
  cka_only_vs_random: gap=0.1137, CI=[0.0768, 0.1505] *** favors cka_only
  standard_vs_rasp: gap=0.0187, CI=[0.0056, 0.0318] *** favors standard
  standard_vs_random: gap=-0.1153, CI=[-0.1408, -0.0906] *** favors random
  rasp_vs_random: gap=-0.1313, CI=[-0.1556, -0.1069] *** favors random

=== Per-step significant gaps (step 100) ===
  cka_only_vs_standard: gap=0.2906, CI=[0.1864, 0.3929] ***
  cka_only_vs_rasp: gap=0.3344, CI=[0.2364, 0.4338] ***
  cka_only_vs_random: step 100 data missing
  standard_vs_rasp: gap=0.0437, CI=[0.0117, 0.0759] ***
  standard_vs_random: step 100 data missing
  rasp_vs_random: step 100 data missing

=== Sensitivity to n_eff (trajectory mean gap) ===
  n_eff_40:
    cka_only_vs_standard: CI=[0.1932, 0.2774] ***
    cka_only_vs_rasp: CI=[0.2130, 0.2944] ***
    cka_only_vs_random: CI=[0.0627, 0.1642] ***
    standard_vs_rasp: CI=[0.0003, 0.0373] ***
    standard_vs_random: CI=[-0.1512, -0.0798] ***
    rasp_vs_random: CI=[-0.1660, -0.0972] ***
  n_eff_80:
    cka_only_vs_standard: CI=[0.2052, 0.2652] ***
    cka_only_vs_rasp: CI=[0.2257, 0.2825] ***
    cka_only_vs_random: CI=[0.0766, 0.1498] ***
    standard_vs_rasp: CI=[0.0057, 0.0321] ***
    standard_vs_random: CI=[-0.1403, -0.0905] ***
    rasp_vs_random: CI=[-0.1550, -0.1074] ***
  n_eff_160:
    cka_only_vs_standard: CI=[0.2139, 0.2561] ***
    cka_only_vs_rasp: CI=[0.2337, 0.2741] ***
    cka_only_vs_random: CI=[0.0877, 0.1394] ***
    standard_vs_rasp: CI=[0.0095, 0.0279] ***
    standard_vs_random: CI=[-0.1331, -0.0972] ***
    rasp_vs_random: CI=[-0.1481, -0.1140] ***
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "1a983402-3dd3-4178-8f82-a19bfe8f0bf6",
  "tool_use_result": {
    "stdout": "Written to /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_reward_trajectories.json\n\n=== Trajectory-level summary (mean gap over all steps, 95% CI) ===\n  cka_only_vs_standard: gap=0.2351, CI=[0.2048, 0.2646] *** favors cka_only\n  cka_only_vs_rasp: gap=0.2539, CI=[0.2241, 0.2822] *** favors cka_only\n  cka_only_vs_random: gap=0.1137, CI=[0.0768, 0.1505] *** favors cka_only\n  standard_vs_rasp: gap=0.0187, CI=[0.0056, 0.0318] *** favors standard\n  standard_vs_random: gap=-0.1153, CI=[-0.1408, -0.0906] *** favors random\n  rasp_vs_random: gap=-0.1313, CI=[-0.1556, -0.1069] *** favors random\n\n=== Per-step significant gaps (step 100) ===\n  cka_only_vs_standard: gap=0.2906, CI=[0.1864, 0.3929] ***\n  cka_only_vs_rasp: gap=0.3344, CI=[0.2364, 0.4338] ***\n  cka_only_vs_random: step 100 data missing\n  standard_vs_rasp: gap=0.0437, CI=[0.0117, 0.0759] ***\n  standard_vs_random: step 100 data missing\n  rasp_vs_random: step 100 data missing\n\n=== Sensitivity to n_eff (trajectory mean gap) ===\n  n_eff_40:\n    cka_only_vs_standard: CI=[0.1932, 0.2774] ***\n    cka_only_vs_rasp: CI=[0.2130, 0.2944] ***\n    cka_only_vs_random: CI=[0.0627, 0.1642] ***\n    standard_vs_rasp: CI=[0.0003, 0.0373] ***\n    standard_vs_random: CI=[-0.1512, -0.0798] ***\n    rasp_vs_random: CI=[-0.1660, -0.0972] ***\n  n_eff_80:\n    cka_only_vs_standard: CI=[0.2052, 0.2652] ***\n    cka_only_vs_rasp: CI=[0.2257, 0.2825] ***\n    cka_only_vs_random: CI=[0.0766, 0.1498] ***\n    standard_vs_rasp: CI=[0.0057, 0.0321] ***\n    standard_vs_random: CI=[-0.1403, -0.0905] ***\n    rasp_vs_random: CI=[-0.1550, -0.1074] ***\n  n_eff_160:\n    cka_only_vs_standard: CI=[0.2139, 0.2561] ***\n    cka_only_vs_rasp: CI=[0.2337, 0.2741] ***\n    cka_only_vs_random: CI=[0.0877, 0.1394] ***\n    standard_vs_rasp: CI=[0.0095, 0.0279] ***\n    standard_vs_random: CI=[-0.1331, -0.0972] ***\n    rasp_vs_random: CI=[-0.1481, -0.1140] ***",
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

_source line 447_

<details><summary>Logged reasoning block</summary>

```text
All pairwise comparisons are significant at 95% CI, and robust to different effective sample size assumptions (n=40, 80, 160). Let me verify the output JSON and register it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "d5571bfc-12a0-465c-a9b0-46287705d3db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWmd1zbiX5H1dDiijFAZAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 82573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1052
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

_source line 448_

分析完成。所有 pairwise 比较在 95% CI 下均显著，且对 n_eff 假设稳健。注册 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "4525d5b6-02ef-48f7-ab46-35aa9309ba9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWmd1zbiX5H1dDiijFAZAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 82573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1052
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

_source line 449_

<details open><summary>🔧 Tool call — Read · `toolu_01SvsCFeAwH3JQ9AGkwNYfg3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_reward_trajectories.json",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "ee0a29a8-00d8-4286-9f33-7de3db0514e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWmd1zbiX5H1dDiijFAZAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 82573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1052
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

_source line 450 · 2026-05-18T10:19:46.497Z_

<details><summary>↩ Tool result · `toolu_01SvsCFeAwH3JQ9AGkwNYfg3`</summary>

```text
1	{
2	  "metadata": {
3	    "analysis": "Bootstrap CI on reward trajectory gaps",
4	    "n_bootstrap": 10000,
5	    "confidence_level": 0.95,
6	    "n_samples_per_interval": 80,
7	    "limitation": "W&B only stores aggregate metrics (mean, std) per logging interval, not per-sample rewards. We use PARAMETRIC bootstrap: at each step, sample the mean from Normal(mu, sigma^2/n) where n=80 is the estimated effective sample size (2 prompts \u00d7 4 generations \u00d7 10 steps per interval). This assumes approximate normality of the sample mean (CLT with n=80). True non-parametric bootstrap would require per-sample reward data.",
8	    "random_note": "grpo_random_20 crashed at step 90; step 100 is missing.",
9	    "methods": {
10	      "cka_only": {
11	        "wandb_run_id": "li451oi4",
12	        "source": "wandb"
13	      },
14	      "standard": {
15	        "wandb_run_id": "tyv20u2k",
16	        "source": "wandb"
17	      },
18	      "rasp": {
19	        "wandb_run_id": "s5zf5akl",
20	        "source": "wandb"
21	      },
22	      "random": {
23	        "wandb_run_id": null,
24	        "source": "log_file (crashed before step 100, no W&B sync)"
25	      }
26	    }
27	  },
28	  "per_step_rewards": {
29	    "step_10": {
30	      "cka_only": {
31	        "mean": 0.253125,
32	        "std": 0.387209,
33	        "se": 0.043291,
34	        "ci_95_lower": 0.168274,
35	        "ci_95_upper": 0.337976
36	      },
37	      "standard": {
38	        "mean": 0.05125,
39	        "std": 0.167951,
40	        "se": 0.018777,
41	        "ci_95_lower": 0.014446,
42	        "ci_95_upper": 0.088054
43	      },
44	      "rasp": {
45	        "mean": 0.016875,
46	        "std": 0.058262,
47	        "se": 0.006514,
48	        "ci_95_lower": 0.004108,
49	        "ci_95_upper": 0.029642
50	      },
51	      "random": {
52	        "mean": 0.1606,
53	        "std": 0.3094,
54	        "se": 0.034592,
55	        "ci_95_lower": 0.0928,
56	        "ci_95_upper": 0.2284
57	      }
58	    },
59	    "step_20": {
60	      "cka_only": {
61	        "mean": 0.218125,
62	        "std": 0.359799,
63	        "se": 0.040227,
64	        "ci_95_lower": 0.139281,
65	        "ci_95_upper": 0.296969
66	      },
67	      "standard": {
68	        "mean": 0.055625,
69	        "std": 0.165603,
70	        "se": 0.018515,
71	        "ci_95_lower": 0.019336,
72	        "ci_95_upper": 0.091914
73	      },
74	      "rasp": {
75	        "mean": 0.020625,
76	        "std": 0.064115,
77	        "se": 0.007168,
78	        "ci_95_lower": 0.006575,
79	        "ci_95_upper": 0.034675
80	      },
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "6f8d11f6-9add-4fa5-a937-57a7fd6e9a1a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_reward_trajectories.json",
      "content": "{\n  \"metadata\": {\n    \"analysis\": \"Bootstrap CI on reward trajectory gaps\",\n    \"n_bootstrap\": 10000,\n    \"confidence_level\": 0.95,\n    \"n_samples_per_interval\": 80,\n    \"limitation\": \"W&B only stores aggregate metrics (mean, std) per logging interval, not per-sample rewards. We use PARAMETRIC bootstrap: at each step, sample the mean from Normal(mu, sigma^2/n) where n=80 is the estimated effective sample size (2 prompts \\u00d7 4 generations \\u00d7 10 steps per interval). This assumes approximate normality of the sample mean (CLT with n=80). True non-parametric bootstrap would require per-sample reward data.\",\n    \"random_note\": \"grpo_random_20 crashed at step 90; step 100 is missing.\",\n    \"methods\": {\n      \"cka_only\": {\n        \"wandb_run_id\": \"li451oi4\",\n        \"source\": \"wandb\"\n      },\n      \"standard\": {\n        \"wandb_run_id\": \"tyv20u2k\",\n        \"source\": \"wandb\"\n      },\n      \"rasp\": {\n        \"wandb_run_id\": \"s5zf5akl\",\n        \"source\": \"wandb\"\n      },\n      \"random\": {\n        \"wandb_run_id\": null,\n        \"source\": \"log_file (crashed before step 100, no W&B sync)\"\n      }\n    }\n  },\n  \"per_step_rewards\": {\n    \"step_10\": {\n      \"cka_only\": {\n        \"mean\": 0.253125,\n        \"std\": 0.387209,\n        \"se\": 0.043291,\n        \"ci_95_lower\": 0.168274,\n        \"ci_95_upper\": 0.337976\n      },\n      \"standard\": {\n        \"mean\": 0.05125,\n        \"std\": 0.167951,\n        \"se\": 0.018777,\n        \"ci_95_lower\": 0.014446,\n        \"ci_95_upper\": 0.088054\n      },\n      \"rasp\": {\n        \"mean\": 0.016875,\n        \"std\": 0.058262,\n        \"se\": 0.006514,\n        \"ci_95_lower\": 0.004108,\n        \"ci_95_upper\": 0.029642\n      },\n      \"random\": {\n        \"mean\": 0.1606,\n        \"std\": 0.3094,\n        \"se\": 0.034592,\n        \"ci_95_lower\": 0.0928,\n        \"ci_95_upper\": 0.2284\n      }\n    },\n    \"step_20\": {\n      \"cka_only\": {\n        \"mean\": 0.218125,\n        \"std\": 0.359799,\n        \"se\": 0.040227,\n        \"ci_95_lower\": 0.139281,\n        \"ci_95_upper\": 0.296969\n      },\n      \"standard\": {\n        \"mean\": 0.055625,\n        \"std\": 0.165603,\n        \"se\": 0.018515,\n        \"ci_95_lower\": 0.019336,\n        \"ci_95_upper\": 0.091914\n      },\n      \"rasp\": {\n        \"mean\": 0.020625,\n        \"std\": 0.064115,\n        \"se\": 0.007168,\n        \"ci_95_lower\": 0.006575,\n        \"ci_95_upper\": 0.034675\n      },",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 1178
    }
  }
}
```

</details>

---


### Tool call

_source line 451_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01XzoPP1iJgtqhd8W9byqWh6`</summary>

```json
{
  "name": "bootstrap_ci_reward_trajectories",
  "type": "data",
  "description": "Bootstrap CI analysis (10K parametric resamples) on pairwise reward gaps across 4 GRPO methods (CKA-only, Standard, RASP, Random) over 100-step trajectories. All 6 pairwise comparisons significant at 95% CI, robust to n_eff sensitivity.",
  "project": "recovery_aware_struct_prune",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_reward_trajectories.json",
  "tags": [
    "E5",
    "bootstrap",
    "reward_trajectory",
    "confidence_interval",
    "GRPO"
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
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "7cf1ecdd-7ffd-4c8a-ac7a-6a0adfcf0e31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kp428VWUm32xydVAQSS5EF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 83625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1294
      },
      "output_tokens": 62,
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

_source line 452 · 2026-05-18T10:19:53.963Z_

<details><summary>↩ Tool result · `toolu_01XzoPP1iJgtqhd8W9byqWh6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_1fe0aa\", \"name\": \"bootstrap_ci_reward_trajectories\", \"type\": \"data\", \"description\": \"Bootstrap CI analysis (10K parametric resamples) on pairwise reward gaps across 4 GRPO methods (CKA-only, Standard, RASP, Random) over 100-step trajectories. All 6 pairwise comparisons significant at 95% CI, robust to n_eff sensitivity.\", \"path\": \"projects/recovery_aware_struct_prune/artifacts/_project/data/bootstrap_ci_reward_trajectories.json\", \"url\": null, \"project\": \"recovery_aware_struct_prune\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-18T10:19:53.794823+00:00\", \"tags\": [\"E5\", \"bootstrap\", \"reward_trajectory\", \"confidence_interval\", \"GRPO\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "9a6e9fb9-fb95-4eb0-ba12-ac7faf69a703",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260518_1fe0aa\\\", \\\"name\\\": \\\"bootstrap_ci_reward_trajectories\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Bootstrap CI analysis (10K parametric resamples) on pairwise reward gaps across 4 GRPO methods (CKA-only, Standard, RASP, Random) over 100-step trajectories. All 6 pairwise comparisons significant at 95% CI, robust to n_eff sensitivity.\\\", \\\"path\\\": \\\"projects/recovery_aware_struct_prune/artifacts/_project/data/bootstrap_ci_reward_trajectories.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"recovery_aware_struct_prune\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-18T10:19:53.794823+00:00\\\", \\\"tags\\\": [\\\"E5\\\", \\\"bootstrap\\\", \\\"reward_trajectory\\\", \\\"confidence_interval\\\", \\\"GRPO\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_1fe0aa\", \"name\": \"bootstrap_ci_reward_trajectories\", \"type\": \"data\", \"description\": \"Bootstrap CI analysis (10K parametric resamples) on pairwise reward gaps across 4 GRPO methods (CKA-only, Standard, RASP, Random) over 100-step trajectories. All 6 pairwise comparisons significant at 95% CI, robust to n_eff sensitivity.\", \"path\": \"projects/recovery_aware_struct_prune/artifacts/_project/data/bootstrap_ci_reward_trajectories.json\", \"url\": null, \"project\": \"recovery_aware_struct_prune\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-18T10:19:53.794823+00:00\", \"tags\": [\"E5\", \"bootstrap\", \"reward_trajectory\", \"confidence_interval\", \"GRPO\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 453_

完成。结果摘要：

**数据限制**: W&B 只存 aggregate metrics（mean, std），无 per-sample rewards。使用 parametric bootstrap（假设 CLT，n_eff=80 per interval）。

**Trajectory 级别平均 gap（95% CI，全部显著）**:

| Comparison | Gap | 95% CI | Favors |
|---|---|---|---|
| CKA-only vs Standard | +0.2351 | [0.205, 0.265] | CKA-only |
| CKA-only vs RASP | +0.2539 | [0.224, 0.282] | CKA-only |
| CKA-only vs Random | +0.1137 | [0.077, 0.151] | CKA-only |
| Standard vs RASP | +0.0187 | [0.006, 0.032] | Standard |
| Standard vs Random | -0.1153 | [-0.141, -0.091] | Random |
| RASP vs Random | -0.1313 | [-0.156, -0.107] | Random |

**关键发现**:
- CKA-only 显著优于所有其他方法（gap 0.11-0.25）
- Random pruning 显著优于 Standard 和 RASP（即 magnitude/RASP 剪枝反而不如 random）
- Standard 仅 marginally 优于 RASP（gap 0.019，CI 刚好不含 0）
- 所有结论对 n_eff∈{40,80,160} 稳健

Random 缺 step 100 数据（crash before sync）。结果已保存至 `artifacts/bootstrap_ci_reward_trajectories.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "uuid": "161d829d-9572-4256-bfdd-e624ee0cfc8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6TDEEtcgQiUmNyccJN6vb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 84919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 634
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

_source line 454_

完成。结果摘要：

**数据限制**: W&B 只存 aggregate metrics（mean, std），无 per-sample rewards。使用 parametric bootstrap（假设 CLT，n_eff=80 per interval）。

**Trajectory 级别平均 gap（95% CI，全部显著）**:

| Comparison | Gap | 95% CI | Favors |
|---|---|---|---|
| CKA-only vs Standard | +0.2351 | [0.205, 0.265] | CKA-only |
| CKA-only vs RASP | +0.2539 | [0.224, 0.282] | CKA-only |
| CKA-only vs Random | +0.1137 | [0.077, 0.151] | CKA-only |
| Standard vs RASP | +0.0187 | [0.006, 0.032] | Standard |
| Standard vs Random | -0.1153 | [-0.141, -0.091] | Random |
| RASP vs Random | -0.1313 | [-0.156, -0.107] | Random |

**关键发现**:
- CKA-only 显著优于所有其他方法（gap 0.11-0.25）
- Random pruning 显著优于 Standard 和 RASP（即 magnitude/RASP 剪枝反而不如 random）
- Standard 仅 marginally 优于 RASP（gap 0.019，CI 刚好不含 0）
- 所有结论对 n_eff∈{40,80,160} 稳健

Random 缺 step 100 数据（crash before sync）。结果已保存至 `artifacts/bootstrap_ci_reward_trajectories.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 611952,
  "duration_api_ms": 566010,
  "num_turns": 78,
  "stop_reason": "end_turn",
  "session_id": "10c5ee96-171d-4700-9af5-06ee7b72c81f",
  "total_cost_usd": 2.982022749999999,
  "usage": {
    "input_tokens": 59,
    "cache_creation_input_tokens": 73712,
    "cache_read_input_tokens": 3004929,
    "output_tokens": 24170,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 73712,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 469,
        "cache_read_input_tokens": 84919,
        "cache_creation_input_tokens": 634,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 634
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1960,
      "outputTokens": 10083,
      "cacheReadInputTokens": 2067895,
      "cacheCreationInputTokens": 124119,
      "webSearchRequests": 0,
      "costUSD": 0.4143132500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 59,
      "outputTokens": 24170,
      "cacheReadInputTokens": 3004929,
      "cacheCreationInputTokens": 73712,
      "webSearchRequests": 0,
      "costUSD": 2.5677095,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "628bb1cf-2a18-4a88-a457-3f1a4a6324b3"
}
```

</details>

---
