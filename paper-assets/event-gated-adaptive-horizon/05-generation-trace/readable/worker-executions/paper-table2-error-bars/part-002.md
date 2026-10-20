# paper table2 error bars — Part 2 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../paper-table2-error-bars.md) · [Structured JSON](../../../sessions/a0/a0597f58d1c8194e9a23.json)

## Round 1

### Assistant

_source line 177_

让我系统性地从 registry.yaml 提取每个分组的 eval_return。同时查看缺失数据的报告文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "882e4836-ea63-43dd-9fa7-db26b5807c80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2JWp7gJiQRPBz3vEQw8u4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4475,
      "cache_read_input_tokens": 87538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4475
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

_source line 178_

<details open><summary>🔧 Tool call — Bash · `toolu_01U1M6fr2CF2Frp3p5Xn5pSB`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml, json, re, os\nfrom collections import defaultdict\n\nwith open(\"registry.yaml\") as f:\n    reg = yaml.safe_load(f)\n\nexperiments = reg.get(\"experiments\", reg)\n\ndef get_eval(exp):\n    \"\"\"Extract eval_return from experiment metrics.\"\"\"\n    m = exp.get(\"metrics\", {}) or {}\n    # Try multiple keys\n    for k in [\"eval_return_final\", \"eval_final\", \"final_eval_return\", \"eval_return_105K\", \n              \"eval_return_105k\", \"eval_return_mean\"]:\n        if k in m and m[k] is not None:\n            try:\n                return float(m[k])\n            except (TypeError, ValueError):\n                continue\n    return None\n\n# Build groups for Table 2\n# Each group: list of (exp_id, eval_return, env)\ngroups = defaultdict(list)\n\nfor eid, exp in experiments.items():\n    status = exp.get(\"status\", \"\")\n    concl = exp.get(\"conclusion\", \"\")\n    hyp = str(exp.get(\"hypothesis\", \"\")).lower()\n    eid_lower = eid.lower()\n    \n    # Skip non-DONE or failed/killed experiments (unless they have useful data)\n    if concl in (\"killed\", \"failed\") and get_eval(exp) is None:\n        continue\n    \n    eval_val = get_eval(exp)\n    \n    # Determine environment\n    env = \"unknown\"\n    if \"walker\" in eid_lower or \"walker\" in hyp:\n        env = \"walker\"\n    elif \"cheetah\" in eid_lower or \"cheetah\" in hyp:\n        env = \"cheetah\"\n    elif \"pickcube\" in eid_lower or \"pickcube\" in hyp:\n        env = \"pickcube\"\n    elif \"hopper\" in eid_lower or \"hopper\" in hyp:\n        env = \"hopper\"\n    elif \"cartpole\" in eid_lower or \"cartpole\" in hyp:\n        env = \"cartpole\"\n    \n    # --- GROUP 1: Untreated (008d trigger: trained dt_emb + subsample ON + dt=2 + H=8) ---\n    # Walker 008d seeds\n    if any(x in eid_lower for x in [\"008d\", \"009b_008d\", \"009e_008d\"]) and env == \"walker\":\n        if \"extension\" not in eid_lower and \"treatment\" not in eid_lower:\n            groups[\"untreated\"].append((eid, eval_val, env, concl))\n    # Also newer walker 008d experiments\n    elif \"walker_008d_s\" in eid_lower:\n        groups[\"untreated\"].append((eid, eval_val, env, concl))\n    elif eid_lower == \"exp_068_008d_walker_repro_s1\":\n        groups[\"untreated\"].append((eid, eval_val, env, concl))\n    elif eid_lower == \"exp_059_walker_trained_s5\":\n        groups[\"untreated\"].append((eid, eval_val, env, concl))\n    # Cheetah 008d seeds\n    elif (\"010b\" in eid_lower or \"078\" in eid_lower or \"088\" in eid_lower or \n          \"091\" in eid_lower or \"097\" in eid_lower) and env == \"cheetah\":\n        if \"extension\" not in eid_lower:\n            groups[\"untreated\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 2: Reward-only SGS ---\n    if (\"016\" in eid_lower or \"044\" in eid_lower) and \"sgs\" in hyp and \"reward\" in hyp:\n        if eval_val is not None:\n            groups[\"reward_sgs\"].append((eid, eval_val, env, concl))\n    elif eid_lower == \"exp_044_gradient_stop_walker\":\n        groups[\"reward_sgs\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 3: Full-pathway SGS ---\n    if (\"018\" in eid_lower or \"021\" in eid_lower) and (\"full\" in hyp or \"full\" in eid_lower):\n        if eval_val is not None:\n            groups[\"full_sgs\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 4: Obs-decoder SGS ---\n    if \"025_obs_sgs\" in eid_lower or \"026_obs_sgs\" in eid_lower:\n        if eval_val is not None or concl not in (\"killed\", \"failed\"):\n            groups[\"obs_sgs\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 5: RAVE ---\n    if \"rave\" in eid_lower or \"rave\" in hyp:\n        if eval_val is not None:\n            groups[\"rave\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 6-9: TCN ---\n    if \"tcn\" in eid_lower:\n        sigma = None\n        full_hyp = str(exp.get(\"hypothesis\", \"\"))\n        cmd = str(exp.get(\"spec\", {}).get(\"command\", \"\"))\n        \n        if \"sigma01\" in eid_lower or \"sigma_01\" in eid_lower or \"σ=0.1\" in full_hyp or \"sigma=0.1\" in full_hyp:\n            sigma = \"0.1\"\n        elif \"sigma02\" in eid_lower or \"sigma_02\" in eid_lower or \"σ=0.2\" in full_hyp:\n            sigma = \"0.2\"\n        elif \"sigma05\" in eid_lower or \"sigma_05\" in eid_lower or \"σ=0.5\" in full_hyp:\n            sigma = \"0.5\"\n        elif \"sigma10\" in eid_lower or \"sigma_10\" in eid_lower or \"σ=1.0\" in full_hyp:\n            sigma = \"1.0\"\n        \n        # Also check command\n        if sigma is None:\n            if \"0.5\" in cmd and \"sigma\" in cmd:\n                sigma = \"0.5\"\n            elif \"0.2\" in cmd and \"sigma\" in cmd:\n                sigma = \"0.2\"\n            elif \"0.1\" in cmd and \"sigma\" in cmd:\n                sigma = \"0.1\"\n            elif \"1.0\" in cmd and \"sigma\" in cmd:\n                sigma = \"1.0\"\n        \n        # Also handle exp_027 (default sigma=0.5)\n        if eid_lower == \"exp_027_tcn_walker_s0\" and sigma is None:\n            sigma = \"0.5\"\n        if eid_lower == \"exp_027_tcn_walker_s1\" and sigma is None:\n            sigma = \"0.5\"\n        if eid_lower == \"exp_030b_tcn_cheetah_s0_sigma05\":\n            sigma = \"0.5\"\n        if eid_lower == \"exp_030c_tcn_cheetah_s0_sigma10\":\n            sigma = \"1.0\"\n        \n        if sigma and eval_val is not None:\n            groups[f\"tcn_{sigma}\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 10: Wide single ---\n    if \"wide\" in eid_lower and \"dual\" not in eid_lower and \"critic\" in eid_lower:\n        if eval_val is not None:\n            groups[\"wide_single\"].append((eid, eval_val, env, concl))\n    elif eid_lower == \"exp_033_wide_critic_walker\":\n        groups[\"wide_single\"].append((eid, eval_val, env, concl))\n    elif eid_lower == \"exp_037_wide_critic_cheetah\":\n        if eval_val is not None:\n            groups[\"wide_single\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 11: Narrow dual (min) ---\n    if \"narrow\" in eid_lower and \"dual\" in eid_lower:\n        if eval_val is not None:\n            groups[\"narrow_dual\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 12: Wide dual (min) ---\n    if (\"dual_critic\" in eid_lower or \"dual-critic\" in eid_lower) and \"narrow\" not in eid_lower:\n        if eval_val is not None and \"wide\" not in eid_lower:\n            groups[\"wide_dual\"].append((eid, eval_val, env, concl))\n    # Also exp_040 which is wide dual cheetah\n    if \"040_wide_dual\" in eid_lower or \"040_dual\" in eid_lower:\n        if eval_val is not None:\n            groups[\"wide_dual\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 13: Embedding frozen ---\n    if (\"frozen\" in eid_lower or \"freeze\" in hyp or \"frozen\" in hyp) and \"dt_emb\" in (eid_lower + hyp):\n        if eval_val is not None and \"hopper\" not in env:\n            groups[\"frozen\"].append((eid, eval_val, env, concl))\n    \n    # --- GROUP 14: Embedding removed ---\n    if (\"008f\" in eid_lower or \"no_dt_emb\" in eid_lower) and env in (\"walker\", \"cheetah\"):\n        if eval_val is not None and \"baseline\" not in eid_lower and \"pickcube\" not in eid_lower:\n            groups[\"removed\"].append((eid, eval_val, env, concl))\n\n# Print results\nimport numpy as np\n\nprint(\"=\" * 80)\nfor gname in [\"untreated\", \"reward_sgs\", \"full_sgs\", \"obs_sgs\", \"rave\", \n              \"tcn_0.1\", \"tcn_0.2\", \"tcn_0.5\", \"tcn_1.0\",\n              \"wide_single\", \"narrow_dual\", \"wide_dual\", \"frozen\", \"removed\"]:\n    entries = groups.get(gname, [])\n    print(f\"\\n{'='*60}\")\n    print(f\"GROUP: {gname} (n={len(entries)})\")\n    vals = []\n    for eid, ev, env, concl in entries:\n        print(f\"  {eid}: eval={ev}, env={env}, concl={concl}\")\n        if ev is not None:\n            vals.append(ev)\n    \n    if vals:\n        arr = np.array(vals)\n        print(f\"  >>> n_with_eval={len(vals)}, mean={arr.mean():.1f}, std={arr.std():.1f}\")\n    else:\n        print(f\"  >>> NO EVAL VALUES AVAILABLE\")\n\nPYEOF\n",
  "description": "Map all experiments to Table 2 groups with eval_return",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a4de4a8e-c1ee-412f-954b-523e6cd9ca2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2JWp7gJiQRPBz3vEQw8u4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4475,
      "cache_read_input_tokens": 87538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4475
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

_source line 179 · 2026-05-29T00:40:22.595Z_

<details><summary>↩ Tool result · `toolu_01U1M6fr2CF2Frp3p5Xn5pSB`</summary>

```text
================================================================================

============================================================
GROUP: untreated (n=11)
  exp_008d_civo_trigger_s4: eval=None, env=walker, concl=success
  exp_009b_008d_walker_s2: eval=None, env=walker, concl=negative
  exp_009e_008d_walker_s1: eval=None, env=walker, concl=negative
  exp_010b_cheetah_civo_trigger_s0: eval=0.83, env=cheetah, concl=success
  exp_059_walker_trained_s5: eval=95.8, env=walker, concl=success
  exp_068_008d_walker_repro_s1: eval=39.1, env=walker, concl=success
  exp_078_cheetah_008d_s0: eval=119.5, env=walker, concl=success
  exp_088_cheetah_008d_s1: eval=309.3, env=cheetah, concl=negative
  exp_091_cheetah_008d_s2: eval=2.5, env=cheetah, concl=success
  exp_097_cheetah_008d_s3: eval=61.7, env=walker, concl=success
  exp_quadruped_008d_s0: eval=None, env=walker, concl=
  >>> n_with_eval=7, mean=89.8, std=98.6

============================================================
GROUP: reward_sgs (n=2)
  exp_016e_sgs_walker_s1: eval=31.73, env=walker, concl=negative
  exp_044_gradient_stop_walker: eval=538.6, env=walker, concl=success
  >>> n_with_eval=2, mean=285.2, std=253.4

============================================================
GROUP: full_sgs (n=3)
  exp_018_full_sgs_walker_s1: eval=915.7, env=walker, concl=killed
  exp_018v2_full_sgs_walker_s1: eval=448.3, env=walker, concl=negative
  exp_021_full_sgs_cheetah_s1: eval=221.5, env=cheetah, concl=negative
  >>> n_with_eval=3, mean=528.5, std=289.0

============================================================
GROUP: obs_sgs (n=1)
  exp_025_obs_sgs_walker_s2: eval=None, env=walker, concl=negative
  >>> NO EVAL VALUES AVAILABLE

============================================================
GROUP: rave (n=1)
  exp_028_rave_walker_s0_ceil15: eval=76.2, env=walker, concl=negative
  >>> n_with_eval=1, mean=76.2, std=0.0

============================================================
GROUP: tcn_0.1 (n=1)
  exp_029c_tcn_walker_s0_sigma01: eval=328.3, env=walker, concl=negative
  >>> n_with_eval=1, mean=328.3, std=0.0

============================================================
GROUP: tcn_0.2 (n=4)
  exp_027_tcn_walker_s0_sigma02: eval=236.4, env=walker, concl=success
  exp_029a_tcn_walker_s1_sigma02: eval=319.4, env=walker, concl=success
  exp_029b_tcn_walker_s2_sigma02: eval=31.97, env=walker, concl=negative
  exp_029d_tcn_walker_s3_sigma02: eval=104.5, env=walker, concl=negative
  >>> n_with_eval=4, mean=173.1, std=111.8

============================================================
GROUP: tcn_0.5 (n=2)
  exp_027_tcn_walker_s0: eval=95.5, env=walker, concl=negative
  exp_030b_tcn_cheetah_s0_sigma05: eval=104.4, env=walker, concl=negative
  >>> n_with_eval=2, mean=100.0, std=4.5

============================================================
GROUP: tcn_1.0 (n=1)
  exp_030c_tcn_cheetah_s0_sigma10: eval=47.2, env=cheetah, concl=negative
  >>> n_with_eval=1, mean=47.2, std=0.0

============================================================
GROUP: wide_single (n=1)
  exp_037_wide_critic_cheetah: eval=146.1, env=walker, concl=negative
  >>> n_with_eval=1, mean=146.1, std=0.0

============================================================
GROUP: narrow_dual (n=2)
  exp_035_narrow_dual_critic_walker: eval=697.8, env=walker, concl=success
  exp_039_narrow_dual_critic_walker_s1: eval=592.7, env=walker, concl=success
  >>> n_with_eval=2, mean=645.2, std=52.5

============================================================
GROUP: wide_dual (n=6)
  exp_032_dual_critic_walker: eval=739.7, env=walker, concl=success
  exp_032b_dual_critic_walker_s1: eval=516.0, env=walker, concl=success
  exp_034_dual_critic_cheetah: eval=97.5, env=cheetah, concl=negative
  exp_036_dual_critic_pickcube: eval=27.7, env=walker, concl=negative
  exp_038_dual_critic_walker_s2: eval=120.9, env=walker, concl=negative
  exp_041_dual_critic_walker_s3: eval=544.0, env=walker, concl=success
  >>> n_with_eval=6, mean=341.0, std=269.8

============================================================
GROUP: frozen (n=16)
  exp_015b_frozen_dt_emb: eval=204.2, env=walker, concl=negative
  exp_022_untrained_dt_emb_learned_gate: eval=189.1, env=unknown, concl=killed
  exp_022b_no_curriculum: eval=300.7, env=unknown, concl=success
  exp_042_frozen_dt_emb_walker: eval=612.45, env=walker, concl=success
  exp_046_frozen_dt_emb_cheetah: eval=150.5, env=walker, concl=success
  exp_047_frozen_dt_emb_walker_s1: eval=144.22, env=walker, concl=success
  exp_051_stackcube_frozen_dt_emb_s0: eval=45.3, env=walker, concl=negative
  exp_056_peginsertion_frozen_s1: eval=4.37, env=unknown, concl=success
  exp_057_frozen_dt_emb_walker_s2: eval=123.94, env=walker, concl=success
  exp_058_frozen_dt_emb_cheetah_s1: eval=80.46, env=cheetah, concl=success
  exp_057: eval=123.9, env=walker, concl=success
  exp_067_frozen_dt_emb_walker_plan015: eval=281.5, env=walker, concl=success
  exp_084_frozen_dt_emb_walker_s0: eval=281.48, env=walker, concl=success
  exp_085_frozen_dt_emb_walker_s1: eval=69.26, env=walker, concl=success
  exp_086_frozen_dt_emb_cheetah_s0: eval=53.3, env=cheetah, concl=success
  exp_087_frozen_dt_emb_cheetah_s1: eval=186.9, env=cheetah, concl=success
  >>> n_with_eval=16, mean=178.2, std=141.1

============================================================
GROUP: removed (n=13)
  exp_008f_s3_no_dt_embed_walker: eval=363.8, env=walker, concl=success
  exp_008f_s4: eval=306.5, env=walker, concl=negative
  exp_024b_cheetah_no_dt_emb_s0: eval=96.5, env=walker, concl=success
  exp_024b_cheetah_no_dt_emb_s1: eval=77.3, env=cheetah, concl=success
  exp_043_008f_walker_s1: eval=673.73, env=walker, concl=success
  exp_069_008f_walker_repro_s1: eval=237.8, env=walker, concl=success
  exp_071_008f_walker_s3: eval=311.9, env=walker, concl=success
  exp_073_008f_walker_s4: eval=289.3, env=walker, concl=success
  exp_082_cheetah_no_dt_emb_s0: eval=83.2, env=cheetah, concl=success
  exp_092_cheetah_no_dt_emb_s1: eval=77.3, env=cheetah, concl=success
  exp_093_cheetah_no_dt_emb_s2: eval=151.2, env=cheetah, concl=success
  exp_walker_no_dt_emb_s1: eval=468.83, env=walker, concl=success
  exp_walker_008f_s0: eval=139.54, env=walker, concl=success
  >>> n_with_eval=13, mean=252.1, std=171.4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "9d77ba44-a82f-4398-b681-20bf8d88da53",
  "tool_use_result": {
    "stdout": "================================================================================\n\n============================================================\nGROUP: untreated (n=11)\n  exp_008d_civo_trigger_s4: eval=None, env=walker, concl=success\n  exp_009b_008d_walker_s2: eval=None, env=walker, concl=negative\n  exp_009e_008d_walker_s1: eval=None, env=walker, concl=negative\n  exp_010b_cheetah_civo_trigger_s0: eval=0.83, env=cheetah, concl=success\n  exp_059_walker_trained_s5: eval=95.8, env=walker, concl=success\n  exp_068_008d_walker_repro_s1: eval=39.1, env=walker, concl=success\n  exp_078_cheetah_008d_s0: eval=119.5, env=walker, concl=success\n  exp_088_cheetah_008d_s1: eval=309.3, env=cheetah, concl=negative\n  exp_091_cheetah_008d_s2: eval=2.5, env=cheetah, concl=success\n  exp_097_cheetah_008d_s3: eval=61.7, env=walker, concl=success\n  exp_quadruped_008d_s0: eval=None, env=walker, concl=\n  >>> n_with_eval=7, mean=89.8, std=98.6\n\n============================================================\nGROUP: reward_sgs (n=2)\n  exp_016e_sgs_walker_s1: eval=31.73, env=walker, concl=negative\n  exp_044_gradient_stop_walker: eval=538.6, env=walker, concl=success\n  >>> n_with_eval=2, mean=285.2, std=253.4\n\n============================================================\nGROUP: full_sgs (n=3)\n  exp_018_full_sgs_walker_s1: eval=915.7, env=walker, concl=killed\n  exp_018v2_full_sgs_walker_s1: eval=448.3, env=walker, concl=negative\n  exp_021_full_sgs_cheetah_s1: eval=221.5, env=cheetah, concl=negative\n  >>> n_with_eval=3, mean=528.5, std=289.0\n\n============================================================\nGROUP: obs_sgs (n=1)\n  exp_025_obs_sgs_walker_s2: eval=None, env=walker, concl=negative\n  >>> NO EVAL VALUES AVAILABLE\n\n============================================================\nGROUP: rave (n=1)\n  exp_028_rave_walker_s0_ceil15: eval=76.2, env=walker, concl=negative\n  >>> n_with_eval=1, mean=76.2, std=0.0\n\n============================================================\nGROUP: tcn_0.1 (n=1)\n  exp_029c_tcn_walker_s0_sigma01: eval=328.3, env=walker, concl=negative\n  >>> n_with_eval=1, mean=328.3, std=0.0\n\n============================================================\nGROUP: tcn_0.2 (n=4)\n  exp_027_tcn_walker_s0_sigma02: eval=236.4, env=walker, concl=success\n  exp_029a_tcn_walker_s1_sigma02: eval=319.4, env=walker, concl=success\n  exp_029b_tcn_walker_s2_sigma02: eval=31.97, env=walker, concl=negative\n  exp_029d_tcn_walker_s3_sigma02: eval=104.5, env=walker, concl=negative\n  >>> n_with_eval=4, mean=173.1, std=111.8\n\n============================================================\nGROUP: tcn_0.5 (n=2)\n  exp_027_tcn_walker_s0: eval=95.5, env=walker, concl=negative\n  exp_030b_tcn_cheetah_s0_sigma05: eval=104.4, env=walker, concl=negative\n  >>> n_with_eval=2, mean=100.0, std=4.5\n\n============================================================\nGROUP: tcn_1.0 (n=1)\n  exp_030c_tcn_cheetah_s0_sigma10: eval=47.2, env=cheetah, concl=negative\n  >>> n_with_eval=1, mean=47.2, std=0.0\n\n============================================================\nGROUP: wide_single (n=1)\n  exp_037_wide_critic_cheetah: eval=146.1, env=walker, concl=negative\n  >>> n_with_eval=1, mean=146.1, std=0.0\n\n============================================================\nGROUP: narrow_dual (n=2)\n  exp_035_narrow_dual_critic_walker: eval=697.8, env=walker, concl=success\n  exp_039_narrow_dual_critic_walker_s1: eval=592.7, env=walker, concl=success\n  >>> n_with_eval=2, mean=645.2, std=52.5\n\n============================================================\nGROUP: wide_dual (n=6)\n  exp_032_dual_critic_walker: eval=739.7, env=walker, concl=success\n  exp_032b_dual_critic_walker_s1: eval=516.0, env=walker, concl=success\n  exp_034_dual_critic_cheetah: eval=97.5, env=cheetah, concl=negative\n  exp_036_dual_critic_pickcube: eval=27.7, env=walker, concl=negative\n  exp_038_dual_critic_walker_s2: eval=120.9, env=walker, concl=negative\n  exp_041_dual_critic_walker_s3: eval=544.0, env=walker, concl=success\n  >>> n_with_eval=6, mean=341.0, std=269.8\n\n============================================================\nGROUP: frozen (n=16)\n  exp_015b_frozen_dt_emb: eval=204.2, env=walker, concl=negative\n  exp_022_untrained_dt_emb_learned_gate: eval=189.1, env=unknown, concl=killed\n  exp_022b_no_curriculum: eval=300.7, env=unknown, concl=success\n  exp_042_frozen_dt_emb_walker: eval=612.45, env=walker, concl=success\n  exp_046_frozen_dt_emb_cheetah: eval=150.5, env=walker, concl=success\n  exp_047_frozen_dt_emb_walker_s1: eval=144.22, env=walker, concl=success\n  exp_051_stackcube_frozen_dt_emb_s0: eval=45.3, env=walker, concl=negative\n  exp_056_peginsertion_frozen_s1: eval=4.37, env=unknown, concl=success\n  exp_057_frozen_dt_emb_walker_s2: eval=123.94, env=walker, concl=success\n  exp_058_frozen_dt_emb_cheetah_s1: eval=80.46, env=cheetah, concl=success\n  exp_057: eval=123.9, env=walker, concl=success\n  exp_067_frozen_dt_emb_walker_plan015: eval=281.5, env=walker, concl=success\n  exp_084_frozen_dt_emb_walker_s0: eval=281.48, env=walker, concl=success\n  exp_085_frozen_dt_emb_walker_s1: eval=69.26, env=walker, concl=success\n  exp_086_frozen_dt_emb_cheetah_s0: eval=53.3, env=cheetah, concl=success\n  exp_087_frozen_dt_emb_cheetah_s1: eval=186.9, env=cheetah, concl=success\n  >>> n_with_eval=16, mean=178.2, std=141.1\n\n============================================================\nGROUP: removed (n=13)\n  exp_008f_s3_no_dt_embed_walker: eval=363.8, env=walker, concl=success\n  exp_008f_s4: eval=306.5, env=walker, concl=negative\n  exp_024b_cheetah_no_dt_emb_s0: eval=96.5, env=walker, concl=success\n  exp_024b_cheetah_no_dt_emb_s1: eval=77.3, env=cheetah, concl=success\n  exp_043_008f_walker_s1: eval=673.73, env=walker, concl=success\n  exp_069_008f_walker_repro_s1: eval=237.8, env=walker, concl=success\n  exp_071_008f_walker_s3: eval=311.9, env=walker, concl=success\n  exp_073_008f_walker_s4: eval=289.3, env=walker, concl=success\n  exp_082_cheetah_no_dt_emb_s0: eval=83.2, env=cheetah, concl=success\n  exp_092_cheetah_no_dt_emb_s1: eval=77.3, env=cheetah, concl=success\n  exp_093_cheetah_no_dt_emb_s2: eval=151.2, env=cheetah, concl=success\n  exp_walker_no_dt_emb_s1: eval=468.83, env=walker, concl=success\n  exp_walker_008f_s0: eval=139.54, env=walker, concl=success\n  >>> n_with_eval=13, mean=252.1, std=171.4",
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

_source line 180_

<details><summary>Logged reasoning block</summary>

```text
OK, the data is messy. There are several issues:
1. Many untreated experiments missing eval_return
2. Some groups have more experiments than the table indicates
3. Some experiments might be duplicates or from different batches

I need to be more careful about which experiments are actually used in the paper's Table 2. Let me look at the paper audit data more carefully, and also check which experiments' eval_return values are documented in the reports.

Key missing data:
- Untreated: exp_008d_civo_trigger_s4 (no eval), exp_009b_008d_walker_s2 (no eval), exp_009e_008d_walker_s1 (no eval)


- Obs-decoder SGS: found 0 eval values in the YAML registry but the MCP registry had values for exp_025/026
- Wide single: missing exp_033

I'm realizing the core issue now—the MCP registry and the local YAML file contain different subsets of the data. Some experiments have eval results recorded in one source but not the other. I need to cross-reference both registries and pull from the MCP data where the YAML file has gaps.

Looking at the MCP registry entries, I can see eval returns for several obs-decoder SGS experiments like exp_025 with walker seeds and exp_026 with cheetah seeds, plus some untreated experiments like exp_010b. I should check the report files next to fill in any remaining gaps.

Actually, the paper audit file has eval_final values for many experiments that I should cross-reference. I'm noticing some inconsistencies though — exp_008d shows eval_final=131 in the paper audit but summary_table.csv lists eval_final=82.75 for the same experiment, which is confusing. Let me look more carefully at the summary_table to understand which values are actually correct.

I'm realizing the paper audit might only cover specific claims rather than the full intervention hierarchy table, so I need to find the authoritative source that documents Table 2 data specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "fe5a109d-cb44-48c5-b188-35f381fc3788",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4eUtk4KeVz3eRxkhKshyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 92013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7486
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

_source line 181_

数据源分散。让我查找论文中 Table 2 的直接数据源和补充材料。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "cb3d8aed-54a8-430a-b910-b21a406aea03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4eUtk4KeVz3eRxkhKshyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 92013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7486
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

_source line 182_

<details open><summary>🔧 Tool call — Grep · `toolu_01JW7dy4ZT27fn3kQtMdyRLR`</summary>

```json
{
  "pattern": "intervention.hierarchy|table.*2|tab:intervention",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts",
  "output_mode": "files_with_matches",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d2010c9d-8161-435d-81e0-1e12d35ef30a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4eUtk4KeVz3eRxkhKshyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 92013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7486
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

_source line 183 · 2026-05-29T00:40:49.478Z_

<details><summary>↩ Tool result · `toolu_01JW7dy4ZT27fn3kQtMdyRLR`</summary>

```text
Found 250 files limit: 250
artifacts/manifest.yaml
artifacts/figures/paper/run_20260528_162842_4fdac2/iter_1/details.json
artifacts/figures/paper/run_20260528_162842_4fdac2/planning.json
artifacts/figures/paper/run_20260528_161641_485319/iter_1/details.json
artifacts/figures/paper/run_20260528_161641_485319/planning.json
artifacts/figures/paper/run_20260528_161315_02a262/iter_1/details.json
artifacts/figures/paper/run_20260528_161315_02a262/planning.json
artifacts/figures/paper/run_20260528_160947_8230d9/iter_1/details.json
artifacts/figures/paper/run_20260528_160947_8230d9/planning.json
artifacts/_project/report/rebuttal_prep_r7.md
artifacts/rebuttal_prep_r7.md
artifacts/review_issues.yaml
artifacts/review_reports/round_7.md
artifacts/_project/report/code_correction_history.md
artifacts/code_correction_history.md
artifacts/review_reports/round_6.md
artifacts/_project/report/submission_checklist_v2.md
artifacts/submission_checklist_v2.md
artifacts/_project/report/table5_full_validation.md
artifacts/table5_validation/table5_full_validation.md
artifacts/_project/paper/method.md
artifacts/_project/report/data_lockdown_audit.md
artifacts/_project/report/paper_data_audit_20260526.md
artifacts/paper_data_audit_20260526.md
artifacts/exp_085_frozen_dt_emb_walker_s1/report/analysis_cc03c1.md
artifacts/exp_085_frozen_dt_emb_walker_s1/report/analysis.md
artifacts/_project/report/rebuttal_prep.md
artifacts/rebuttal_prep.md
artifacts/_project/report/rebuttal_draft.md
artifacts/rebuttal_draft.md
artifacts/plan_031_actor_entropy/analysis_report.md
artifacts/_project/report/analysis_report.md
artifacts/exp_071_008f_walker_s3/report/analysis_65012a.md
artifacts/exp_071_008f_walker_s3/report/analysis.md
artifacts/_project/report/supplementary_framework.md
artifacts/supplementary_framework.md
artifacts/_project/report/negative_results_insights.md
artifacts/negative_results_insights.md
artifacts/supplement_completeness_results.md
artifacts/review_reports/round_4.md
artifacts/review_reports/round_3.md
artifacts/exp_036_dual_critic_pickcube/report/exp_036_analysis_2e1055.md
artifacts/exp_036_dual_critic_pickcube/report/exp_036_analysis.md
artifacts/exp_034_dual_critic_cheetah/report/exp_034_analysis.md
artifacts/exp_033_wide_critic_walker/report/report_exp_033_analysis_88d14a.md
artifacts/exp_033_wide_critic_walker/report/report_exp_033_analysis.md
artifacts/exp_032b_dual_critic_walker_s1/report/report_exp_032b_analysis.md
artifacts/dream_reports/dream_20260520T210241/meta.yaml
artifacts/dream_reports/dream_20260520T210241/logs/review_median.log
artifacts/dream_reports/dream_20260520T210241/median/review_report.md
artifacts/dream_reports/dream_20260520T210241/best/review_report.md
artifacts/dream_reports/dream_20260520T210241/median/review_context.yaml
artifacts/dream_reports/dream_20260520T210241/logs/review_best.log
artifacts/dream_reports/dream_20260520T210241/best/review_context.yaml
artifacts/dream_reports/dream_20260520T210241/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T210241/median/paper.log
artifacts/dream_reports/dream_20260520T210241/median/paper.aux
artifacts/dream_reports/dream_20260520T210241/median/paper.tex
artifacts/dream_reports/dream_20260520T210241/median/paper_framing.md
artifacts/dream_reports/dream_20260520T210241/median/experiment_data.json
artifacts/dream_reports/dream_20260520T210241/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T210241/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T210241/best/paper.log
artifacts/dream_reports/dream_20260520T210241/best/paper.aux
artifacts/dream_reports/dream_20260520T210241/best/paper.tex
artifacts/dream_reports/dream_20260520T210241/best/paper_framing.md
artifacts/dream_reports/dream_20260520T210241/best/experiment_data.json
artifacts/dream_reports/dream_20260520T210241/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T210241/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T210241/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T210241/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T155150/meta.yaml
artifacts/dream_reports/dream_20260520T155150/logs/review_worst.log
artifacts/dream_reports/dream_20260520T155150/worst/review_report.md
artifacts/dream_reports/dream_20260520T155150/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T155150/logs/review_median.log
artifacts/dream_reports/dream_20260520T155150/median/review_report.md
artifacts/dream_reports/dream_20260520T155150/median/review_context.yaml
artifacts/dream_reports/dream_20260520T155150/logs/review_best.log
artifacts/dream_reports/dream_20260520T155150/best/review_report.md
artifacts/dream_reports/dream_20260520T155150/best/review_context.yaml
artifacts/dream_reports/dream_20260520T155150/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T155150/worst/paper.log
artifacts/dream_reports/dream_20260520T155150/worst/paper.aux
artifacts/dream_reports/dream_20260520T155150/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T155150/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T155150/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T155150/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T155150/median/paper.log
artifacts/dream_reports/dream_20260520T155150/median/paper.aux
artifacts/dream_reports/dream_20260520T155150/median/paper.tex
artifacts/dream_reports/dream_20260520T155150/median/paper_framing.md
artifacts/dream_reports/dream_20260520T155150/median/experiment_data.json
artifacts/dream_reports/dream_20260520T155150/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T155150/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T155150/best/paper.log
artifacts/dream_reports/dream_20260520T155150/best/paper.aux
artifacts/dream_reports/dream_20260520T155150/best/paper.tex
artifacts/dream_reports/dream_20260520T155150/best/paper_framing.md
artifacts/dream_reports/dream_20260520T155150/best/experiment_data.json
artifacts/dream_reports/dream_20260520T155150/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T155150/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T155150/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T155150/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T155150/logs/phase1_attempt0.log
artifacts/contingency_framing_B_C.md
artifacts/analysis/cheetah_integration_template.md
artifacts/exp_024b_cheetah_no_dt_emb_s0/intermediate/cheetah_integration_template.md
artifacts/exp_023b_cheetah_baseline_s1/data/analysis_8e6b81.md
artifacts/exp_023b_cheetah_baseline_s1/data/analysis.md
artifacts/_project/data/gradient_decomposition_verification.json
artifacts/analysis/gradient_decomposition_verification.json
artifacts/analysis/exp_019b_analysis.json
artifacts/exp_019b_pickcube_civo_trigger/data/exp_019b_analysis.json
artifacts/_project/report/nve_sensitivity_audit_note.md
artifacts/analysis/nve_sensitivity_audit_note.md
artifacts/_project/report/paper_section_audit.md
artifacts/paper_section_audit.md
artifacts/drafts/civo_detector_section_draft.md
artifacts/drafts/results_seed3_patch.md
artifacts/drafts/detector_section_draft.md
artifacts/_project/paper/detector_section_draft.md
artifacts/_project/paper/results_seed3_patch.md
artifacts/drafts/c1_reframe_patch.md
artifacts/_project/report/civo_detector_full_retrospective_v3.json
artifacts/analysis/civo_detector_full_retrospective_v3.json
artifacts/_project/data/detector_threshold_analysis.json
artifacts/analysis/detector_threshold_analysis.json
artifacts/_project/intermediate/paper_numbers_update_draft.md
artifacts/drafts/paper_numbers_update_draft.md
artifacts/_project/report/table1_integrity_check.md
artifacts/analysis/table1_integrity_check.md
artifacts/_project/paper/results_section_draft.md
artifacts/paper_drafts/results_section_draft.md
artifacts/paper_drafts/gradient_decomposition_methodology.md
artifacts/dream_reports/dream_20260516T172011/meta.yaml
artifacts/dream_reports/dream_20260516T172011/logs/review_worst.log
artifacts/dream_reports/dream_20260516T172011/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T172011/logs/review_median.log
artifacts/dream_reports/dream_20260516T172011/logs/review_best.log
artifacts/dream_reports/dream_20260516T172011/best/review_report.md
artifacts/dream_reports/dream_20260516T172011/best/review_context.yaml
artifacts/dream_reports/dream_20260516T172011/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T172011/worst/paper.log
artifacts/dream_reports/dream_20260516T172011/worst/paper.aux
artifacts/dream_reports/dream_20260516T172011/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T172011/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T172011/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T172011/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T172011/median/paper.log
artifacts/dream_reports/dream_20260516T172011/median/paper.aux
artifacts/dream_reports/dream_20260516T172011/median/paper.tex
artifacts/dream_reports/dream_20260516T172011/median/paper_framing.md
artifacts/dream_reports/dream_20260516T172011/median/experiment_data.json
artifacts/dream_reports/dream_20260516T172011/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T172011/best/paper.log
artifacts/dream_reports/dream_20260516T172011/best/paper.aux
artifacts/dream_reports/dream_20260516T172011/best/paper.tex
artifacts/dream_reports/dream_20260516T172011/best/paper_framing.md
artifacts/dream_reports/dream_20260516T172011/best/experiment_data.json
artifacts/dream_reports/dream_20260516T172011/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T172011/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T172011/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T172011/logs/phase2_best_attempt0.log
artifacts/analysis/018v2_civo_analysis.json
artifacts/exp_018v2_full_sgs_walker_s1/data/018v2_civo_analysis.json
artifacts/dream_reports/dream_20260516T172011/logs/phase1_attempt0.log
artifacts/paper_sections/gradient_decomposition_methodology.md
artifacts/_project/paper/gradient_decomposition_methodology.md
artifacts/_project/paper/method_framingB_reaudit_v2.md
artifacts/_project/paper/results.md
artifacts/dream_reports/dream_20260516T133210/meta.yaml
artifacts/dream_reports/dream_20260516T133210/logs/review_worst.log
artifacts/dream_reports/dream_20260516T133210/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T133210/logs/review_median.log
artifacts/dream_reports/dream_20260516T133210/median/review_context.yaml
artifacts/dream_reports/dream_20260516T133210/logs/review_best.log
artifacts/dream_reports/dream_20260516T133210/best/review_context.yaml
artifacts/dream_reports/dream_20260516T133210/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T133210/worst/paper.log
artifacts/dream_reports/dream_20260516T133210/worst/paper.aux
artifacts/dream_reports/dream_20260516T133210/worst/paper.tex
artifacts/dream_reports/dream_20260516T133210/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T133210/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T133210/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T133210/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T133210/median/paper.log
artifacts/dream_reports/dream_20260516T133210/median/paper.aux
artifacts/dream_reports/dream_20260516T133210/median/paper_framing.md
artifacts/dream_reports/dream_20260516T133210/median/experiment_data.json
artifacts/dream_reports/dream_20260516T133210/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T133210/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T133210/best/paper.log
artifacts/dream_reports/dream_20260516T133210/best/paper.aux
artifacts/dream_reports/dream_20260516T133210/best/paper.tex
artifacts/dream_reports/dream_20260516T133210/best/paper_framing.md
artifacts/dream_reports/dream_20260516T133210/best/experiment_data.json
artifacts/dream_reports/dream_20260516T133210/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T133210/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T133210/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T133210/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T115400/meta.yaml
artifacts/dream_reports/dream_20260516T115400/logs/review_worst.log
artifacts/dream_reports/dream_20260516T115400/worst/review_report.md
artifacts/dream_reports/dream_20260516T115400/best/review_report.md
artifacts/dream_reports/dream_20260516T115400/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T115400/logs/review_median.log
artifacts/dream_reports/dream_20260516T115400/median/review_report.md
artifacts/dream_reports/dream_20260516T115400/median/review_context.yaml
artifacts/dream_reports/dream_20260516T115400/logs/review_best.log
artifacts/dream_reports/dream_review_r1_methodology/median/review_report.md
artifacts/dream_reports/dream_20260516T115400/best/review_context.yaml
artifacts/dream_reports/dream_20260516T115400/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T115400/worst/paper.log
artifacts/dream_reports/dream_20260516T115400/worst/paper.aux
artifacts/dream_reports/dream_20260516T115400/worst/paper.tex
artifacts/dream_reports/dream_20260516T115400/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T115400/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T115400/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T115400/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T115400/median/paper.log
artifacts/dream_reports/dream_20260516T115400/median/paper.aux
artifacts/dream_reports/dream_20260516T115400/median/paper.tex
artifacts/dream_reports/dream_20260516T115400/median/paper_framing.md
artifacts/dream_reports/dream_20260516T115400/median/experiment_data.json
artifacts/dream_reports/dream_20260516T115400/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T115400/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T115400/best/paper.log
artifacts/dream_reports/dream_20260516T115400/best/paper.aux
artifacts/dream_reports/dream_20260516T115400/best/paper.tex
artifacts/dream_reports/dream_20260516T115400/best/paper_framing.md
artifacts/dream_reports/dream_20260516T115400/best/experiment_data.json
artifacts/dream_reports/dream_20260516T115400/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T115400/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T115400/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T115400/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T115400/logs/phase1_attempt0.log
artifacts/018/paper/018_prewrite_two_versions.md
artifacts/_project/report/claim_strength_audit.md
artifacts/claim_strength_audit.md
artifacts/_project/report/narrative_audit.md
artifacts/narrative_audit.md
artifacts/_project/report/seed_label_diff_summary.md
artifacts/seed_label_diff_summary.md
artifacts/method_framingB_reaudit_v2.md
artifacts/_project/report/018_analysis_criteria.md
artifacts/018/report/018_analysis_criteria.md
artifacts/framing_b_reaudit_diff.md
artifacts/dream_reports/dream_20260514T062606/worst/paper.tex
artifacts/_project/report/framing_b_reaudit_diff.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "82088588-7add-4e49-afe0-6bc63c432f40",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/manifest.yaml",
      "artifacts/figures/paper/run_20260528_162842_4fdac2/iter_1/details.json",
      "artifacts/figures/paper/run_20260528_162842_4fdac2/planning.json",
      "artifacts/figures/paper/run_20260528_161641_485319/iter_1/details.json",
      "artifacts/figures/paper/run_20260528_161641_485319/planning.json",
      "artifacts/figures/paper/run_20260528_161315_02a262/iter_1/details.json",
      "artifacts/figures/paper/run_20260528_161315_02a262/planning.json",
      "artifacts/figures/paper/run_20260528_160947_8230d9/iter_1/details.json",
      "artifacts/figures/paper/run_20260528_160947_8230d9/planning.json",
      "artifacts/_project/report/rebuttal_prep_r7.md",
      "artifacts/rebuttal_prep_r7.md",
      "artifacts/review_issues.yaml",
      "artifacts/review_reports/round_7.md",
      "artifacts/_project/report/code_correction_history.md",
      "artifacts/code_correction_history.md",
      "artifacts/review_reports/round_6.md",
      "artifacts/_project/report/submission_checklist_v2.md",
      "artifacts/submission_checklist_v2.md",
      "artifacts/_project/report/table5_full_validation.md",
      "artifacts/table5_validation/table5_full_validation.md",
      "artifacts/_project/paper/method.md",
      "artifacts/_project/report/data_lockdown_audit.md",
      "artifacts/_project/report/paper_data_audit_20260526.md",
      "artifacts/paper_data_audit_20260526.md",
      "artifacts/exp_085_frozen_dt_emb_walker_s1/report/analysis_cc03c1.md",
      "artifacts/exp_085_frozen_dt_emb_walker_s1/report/analysis.md",
      "artifacts/_project/report/rebuttal_prep.md",
      "artifacts/rebuttal_prep.md",
      "artifacts/_project/report/rebuttal_draft.md",
      "artifacts/rebuttal_draft.md",
      "artifacts/plan_031_actor_entropy/analysis_report.md",
      "artifacts/_project/report/analysis_report.md",
      "artifacts/exp_071_008f_walker_s3/report/analysis_65012a.md",
      "artifacts/exp_071_008f_walker_s3/report/analysis.md",
      "artifacts/_project/report/supplementary_framework.md",
      "artifacts/supplementary_framework.md",
      "artifacts/_project/report/negative_results_insights.md",
      "artifacts/negative_results_insights.md",
      "artifacts/supplement_completeness_results.md",
      "artifacts/review_reports/round_4.md",
      "artifacts/review_reports/round_3.md",
      "artifacts/exp_036_dual_critic_pickcube/report/exp_036_analysis_2e1055.md",
      "artifacts/exp_036_dual_critic_pickcube/report/exp_036_analysis.md",
      "artifacts/exp_034_dual_critic_cheetah/report/exp_034_analysis.md",
      "artifacts/exp_033_wide_critic_walker/report/report_exp_033_analysis_88d14a.md",
      "artifacts/exp_033_wide_critic_walker/report/report_exp_033_analysis.md",
      "artifacts/exp_032b_dual_critic_walker_s1/report/report_exp_032b_analysis.md",
      "artifacts/dream_reports/dream_20260520T210241/meta.yaml",
      "artifacts/dream_reports/dream_20260520T210241/logs/review_median.log",
      "artifacts/dream_reports/dream_20260520T210241/median/review_report.md",
      "artifacts/dream_reports/dream_20260520T210241/best/review_report.md",
      "artifacts/dream_reports/dream_20260520T210241/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260520T210241/logs/review_best.log",
      "artifacts/dream_reports/dream_20260520T210241/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260520T210241/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260520T210241/median/paper.log",
      "artifacts/dream_reports/dream_20260520T210241/median/paper.aux",
      "artifacts/dream_reports/dream_20260520T210241/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T210241/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260520T210241/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260520T210241/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260520T210241/best/paper.log",
      "artifacts/dream_reports/dream_20260520T210241/best/paper.aux",
      "artifacts/dream_reports/dream_20260520T210241/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T210241/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T210241/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260520T210241/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260520T210241/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260520T210241/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260520T210241/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260520T155150/meta.yaml",
      "artifacts/dream_reports/dream_20260520T155150/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260520T155150/worst/review_report.md",
      "artifacts/dream_reports/dream_20260520T155150/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260520T155150/logs/review_median.log",
      "artifacts/dream_reports/dream_20260520T155150/median/review_report.md",
      "artifacts/dream_reports/dream_20260520T155150/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260520T155150/logs/review_best.log",
      "artifacts/dream_reports/dream_20260520T155150/best/review_report.md",
      "artifacts/dream_reports/dream_20260520T155150/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260520T155150/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper.log",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper.aux",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T155150/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260520T155150/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260520T155150/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260520T155150/median/paper.log",
      "artifacts/dream_reports/dream_20260520T155150/median/paper.aux",
      "artifacts/dream_reports/dream_20260520T155150/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T155150/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260520T155150/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260520T155150/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260520T155150/best/paper.log",
      "artifacts/dream_reports/dream_20260520T155150/best/paper.aux",
      "artifacts/dream_reports/dream_20260520T155150/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T155150/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260520T155150/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260520T155150/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260520T155150/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260520T155150/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260520T155150/logs/phase1_attempt0.log",
      "artifacts/contingency_framing_B_C.md",
      "artifacts/analysis/cheetah_integration_template.md",
      "artifacts/exp_024b_cheetah_no_dt_emb_s0/intermediate/cheetah_integration_template.md",
      "artifacts/exp_023b_cheetah_baseline_s1/data/analysis_8e6b81.md",
      "artifacts/exp_023b_cheetah_baseline_s1/data/analysis.md",
      "artifacts/_project/data/gradient_decomposition_verification.json",
      "artifacts/analysis/gradient_decomposition_verification.json",
      "artifacts/analysis/exp_019b_analysis.json",
      "artifacts/exp_019b_pickcube_civo_trigger/data/exp_019b_analysis.json",
      "artifacts/_project/report/nve_sensitivity_audit_note.md",
      "artifacts/analysis/nve_sensitivity_audit_note.md",
      "artifacts/_project/report/paper_section_audit.md",
      "artifacts/paper_section_audit.md",
      "artifacts/drafts/civo_detector_section_draft.md",
      "artifacts/drafts/results_seed3_patch.md",
      "artifacts/drafts/detector_section_draft.md",
      "artifacts/_project/paper/detector_section_draft.md",
      "artifacts/_project/paper/results_seed3_patch.md",
      "artifacts/drafts/c1_reframe_patch.md",
      "artifacts/_project/report/civo_detector_full_retrospective_v3.json",
      "artifacts/analysis/civo_detector_full_retrospective_v3.json",
      "artifacts/_project/data/detector_threshold_analysis.json",
      "artifacts/analysis/detector_threshold_analysis.json",
      "artifacts/_project/intermediate/paper_numbers_update_draft.md",
      "artifacts/drafts/paper_numbers_update_draft.md",
      "artifacts/_project/report/table1_integrity_check.md",
      "artifacts/analysis/table1_integrity_check.md",
      "artifacts/_project/paper/results_section_draft.md",
      "artifacts/paper_drafts/results_section_draft.md",
      "artifacts/paper_drafts/gradient_decomposition_methodology.md",
      "artifacts/dream_reports/dream_20260516T172011/meta.yaml",
      "artifacts/dream_reports/dream_20260516T172011/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260516T172011/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T172011/logs/review_median.log",
      "artifacts/dream_reports/dream_20260516T172011/logs/review_best.log",
      "artifacts/dream_reports/dream_20260516T172011/best/review_report.md",
      "artifacts/dream_reports/dream_20260516T172011/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T172011/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper.log",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper.aux",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T172011/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T172011/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T172011/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260516T172011/median/paper.log",
      "artifacts/dream_reports/dream_20260516T172011/median/paper.aux",
      "artifacts/dream_reports/dream_20260516T172011/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T172011/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T172011/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260516T172011/best/paper.log",
      "artifacts/dream_reports/dream_20260516T172011/best/paper.aux",
      "artifacts/dream_reports/dream_20260516T172011/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T172011/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T172011/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T172011/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T172011/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260516T172011/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260516T172011/logs/phase2_best_attempt0.log",
      "artifacts/analysis/018v2_civo_analysis.json",
      "artifacts/exp_018v2_full_sgs_walker_s1/data/018v2_civo_analysis.json",
      "artifacts/dream_reports/dream_20260516T172011/logs/phase1_attempt0.log",
      "artifacts/paper_sections/gradient_decomposition_methodology.md",
      "artifacts/_project/paper/gradient_decomposition_methodology.md",
      "artifacts/_project/paper/method_framingB_reaudit_v2.md",
      "artifacts/_project/paper/results.md",
      "artifacts/dream_reports/dream_20260516T133210/meta.yaml",
      "artifacts/dream_reports/dream_20260516T133210/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260516T133210/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T133210/logs/review_median.log",
      "artifacts/dream_reports/dream_20260516T133210/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T133210/logs/review_best.log",
      "artifacts/dream_reports/dream_20260516T133210/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T133210/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper.log",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper.aux",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T133210/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T133210/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T133210/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260516T133210/median/paper.log",
      "artifacts/dream_reports/dream_20260516T133210/median/paper.aux",
      "artifacts/dream_reports/dream_20260516T133210/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T133210/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T133210/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T133210/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260516T133210/best/paper.log",
      "artifacts/dream_reports/dream_20260516T133210/best/paper.aux",
      "artifacts/dream_reports/dream_20260516T133210/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T133210/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T133210/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T133210/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T133210/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260516T133210/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260516T133210/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260516T115400/meta.yaml",
      "artifacts/dream_reports/dream_20260516T115400/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260516T115400/worst/review_report.md",
      "artifacts/dream_reports/dream_20260516T115400/best/review_report.md",
      "artifacts/dream_reports/dream_20260516T115400/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T115400/logs/review_median.log",
      "artifacts/dream_reports/dream_20260516T115400/median/review_report.md",
      "artifacts/dream_reports/dream_20260516T115400/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T115400/logs/review_best.log",
      "artifacts/dream_reports/dream_review_r1_methodology/median/review_report.md",
      "artifacts/dream_reports/dream_20260516T115400/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T115400/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper.log",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper.aux",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T115400/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T115400/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T115400/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260516T115400/median/paper.log",
      "artifacts/dream_reports/dream_20260516T115400/median/paper.aux",
      "artifacts/dream_reports/dream_20260516T115400/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T115400/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T115400/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T115400/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260516T115400/best/paper.log",
      "artifacts/dream_reports/dream_20260516T115400/best/paper.aux",
      "artifacts/dream_reports/dream_20260516T115400/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T115400/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T115400/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T115400/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T115400/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260516T115400/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260516T115400/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260516T115400/logs/phase1_attempt0.log",
      "artifacts/018/paper/018_prewrite_two_versions.md",
      "artifacts/_project/report/claim_strength_audit.md",
      "artifacts/claim_strength_audit.md",
      "artifacts/_project/report/narrative_audit.md",
      "artifacts/narrative_audit.md",
      "artifacts/_project/report/seed_label_diff_summary.md",
      "artifacts/seed_label_diff_summary.md",
      "artifacts/method_framingB_reaudit_v2.md",
      "artifacts/_project/report/018_analysis_criteria.md",
      "artifacts/018/report/018_analysis_criteria.md",
      "artifacts/framing_b_reaudit_diff.md",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.tex",
      "artifacts/_project/report/framing_b_reaudit_diff.md"
    ],
    "numFiles": 250,
    "appliedLimit": 250
  }
}
```

</details>

---


### Tool call

_source line 184_

<details open><summary>🔧 Tool call — Bash · `toolu_01QLGFBTxhZjw8debMgsMzja`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_data_audit_20260526.md 2>/dev/null | grep -A 200 \"intervention\" | head -250",
  "description": "Search for intervention hierarchy data in audit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "4cf61c0d-c8ca-4d2d-985f-87a1864e4a92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4eUtk4KeVz3eRxkhKshyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7486,
      "cache_read_input_tokens": 92013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7486
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

_source line 185 · 2026-05-29T00:40:50.802Z_

<details><summary>↩ Tool result · `toolu_01QLGFBTxhZjw8debMgsMzja`</summary>

```text
## Claim C7: Gradient-level interventions fail (gradient ≠ causal importance)

### 支撑实验 — Reward-only SGS

| exp_id | env | seed | NVE_peak | eval_final | outcome |
|--------|-----|------|----------|------------|---------|
| exp_016e | Walker | 1 | 10.42× | 31.7 | ❌ paradoxically worse |

### 支撑实验 — Full-pathway SGS

| exp_id | env | seed | NVE_peak | eval_final | outcome |
|--------|-----|------|----------|------------|---------|
| exp_018v2 | Walker | 1 | 1.66 | 448.3 | ❌ CIVO+ |
| exp_018_full_sgs_s2 | Walker | 2 | 1.66 | 40.8 | ❌ collapse |
| exp_021 | Cheetah | 1 | 9.94 | 221.5 | ❌ transient spike |

### 支撑实验 — Obs-decoder SGS

| exp_id | env | seed | NVE_peak | eval_final | outcome |
|--------|-----|------|----------|------------|---------|
| exp_025_s1 | Walker | 1 | — | — | ✅ survived (but value collapse) |
| exp_025_s2 | Walker | 2 | — | 89.6 | ❌ |
| exp_025_s3 | Walker | 3 | 6.8@135K | — | ❌ CIVO then value collapse |
| exp_025_s4 | Walker | 4 | — | — | ❌ |
| exp_026_s0 | Cheetah | 0 | 21.9-30.2× | — | ❌ compensatory amplification |
| exp_026_s1 | Cheetah | 1 | 21.9-30.2× | — | ❌ compensatory amplification |

### Gradient Decomposition

| Source | 55K (%) | 112K (%) |
|--------|---------|----------|
| Reward head | 49.0 | 38.1 |
| KL dynamics | 34.7 | 40.4 |
| Obs decoders | 16.3 | 21.5 |
| Cont head | ~0 | ~0 |

**Key insight**: Reward head = largest gradient (38-49%) but reward-only SGS = worst outcome (10.42×). Gradient magnitude ≠ causal importance.

### Control: dt_emb removal

| exp_id | env | seed | NVE_peak | outcome |
|--------|-----|------|----------|---------|
| exp_008f variants | Walker | 0-4 | <1.0 | ✅ 5/5 prevention |
| exp_024b variants | Cheetah | 0-1 | <0.2 | ✅ 2/2 prevention |

### 证据充分性: ✅ Strong
- 17 seeds across 3 SGS variants, 2 environments: 1/17 CIVO-free (and that 1 has value collapse side effect)
- Embedding removal: 5/5 (Walker) + 2/2 (Cheetah) = 7/7 prevention
- Contrast is categorical: SGS ≈ ineffective, removal = 100% effective
- **无缺口**

---

## Claim C8: Intervention Hierarchy (TCN/RAVE/SGS across 3 levels)

### Representation-level: TCN

| exp_id | env | σ | seed | NVE_peak | eval_peak | eval_final | CIVO prevented? |
|--------|-----|---|------|----------|-----------|------------|-----------------|
| exp_027_s0 | Walker | 0.5 | 0 | ~4.0 | 240 | 166.4 | ❌ oscillatory |
| exp_027_s1 | Walker | 0.5 | 1 | ~1.64 | 364.9 | 94.6 | ❌ oscillatory |
| exp_027_sigma02 | Walker | 0.2 | 0 | 0.91@95K | 821.1 | 171.4 | ✅ |
| exp_029a | Walker | 0.2 | 1 | 0.64@55K | 401 | 180.3 | ✅ (eval 45%) |
| exp_029b | Walker | 0.2 | 2 | 2.77@105K | 177.7 | 44.7 | ❌ gradual onset |
| exp_029c | Walker | 0.1 | 0 | ~1.0@95K | 490.7 | 188.6 | ⚠️ borderline |
| exp_029d | Walker | 0.2 | 3 | 3.0@105K | 349.6 | 349.6 | ❌ sudden onset |
| exp_030a | Cheetah | 0.2 | 0 | 1.90@55K | 299.5 | 31.9 | ❌ dose insufficient |
| exp_030b | Cheetah | 0.5 | 0 | 10.67@55K | 296.5 | 143.6 | ❌ transient spike |
| exp_030c | Cheetah | 1.0 | 0 | ≤0.30 | 371.7 | 72.8 | ✅ CIVO prevented, ❌ eval eroded |
| exp_031 | PickCube | 0.2 | 0 | 3.71@52.5K | 23.5 | 11.6 | ❌ dose insufficient |
| exp_031b | PickCube | 0.5 | 0 | 3.3 | — | — | ❌ |

**TCN success rate**: 2/10 NVE<1.0× (Walker σ=0.2 s0, s1 only). Cheetah σ=1.0 prevents CIVO but destroys eval.

### Output-level: RAVE

| exp_id | config | outcome |
|--------|--------|---------|
| exp_028 | ceil=2.0 | ❌ EMA anchor polluted |
| exp_028_ceil15 | ceil=1.5 | ❌ EMA anchor polluted |

### Dual-critic (R9 — architecture-level)

| exp_id | env | config | seed | NVE_peak | eval_final | CIVO prevented? |
|--------|-----|--------|------|----------|------------|-----------------|
| exp_032 | Walker | wide dual | 0 | 1.1 | 739.7 | ✅ |
| exp_032b | Walker | wide dual | 1 | <1.5 | 516 | ✅ |
| exp_038 | Walker | wide dual | 2 | 0.3 | 120.9 | ✅ CIVO, ❌ non-CIVO collapse |
| exp_041 | Walker | wide dual | 3 | 1.5 | 544 | ✅ |
| exp_033 | Walker | wide single | 0 | 4.75 (ve) | 407.9 | ❌ CIVO→self-repair |
| exp_035 | Walker | narrow dual | 0 | 2.75 | 697.8 | ❌ CIVO→full recovery |
| exp_039 | Walker | narrow dual | 1 | 2.19 | 592.7 | ⚠️ CIVO→partial recovery |
| exp_034 | Cheetah | dual | 0 | 1.8 (ve) | 97.5 | ❌ CIVO, partial recovery |
| exp_037 | Cheetah | wide single | 0 | 3.6 | 146.1 | ❌ CIVO→self-repair |
| exp_036 | PickCube | dual | 0 | 2.3 | 27.7 | ⚠️ transient, no sustained CIVO |

**Key finding**: v1≈v2 across all dual-critic configs (ρ>0.999). Pessimism mechanism fails in pure-imagination MBRL. Wide+dual = 3/3 CIVO prevention (Walker). Recovery (min) >> Prevention requires min+capacity.

### Intervention Hierarchy Summary Table

| Level | Method | Success rate | Primary failure mechanism |
|-------|--------|-------------|--------------------------|
| Gradient (L1) | Reward SGS | 0/2 | No-op (gradient ≠ causal) |
| Gradient (L1) | Full SGS | 0/3 | Forward-pass damage irreversible |
| Gradient (L1) | Obs-decoder SGS | 1/6 | Compensatory amplification + critic collapse |
| Output (L2) | RAVE | 0/2 | EMA anchor pollution |
| Representation (L3) | TCN σ=0.2 | 2/4 Walker | Dose-env dependency, seed sensitivity |
| Representation (L3) | TCN σ=0.5 | 0/3 | Overdose/insufficient |
| Architecture | Dual-critic (wide) | 3/4 Walker | v1≈v2, non-CIVO collapse (1/4) |
| **Control** | **dt_emb removal** | **7/7** | **(removes feature entirely)** |

### 证据充分性: ✅ Strong
- 7+ methods across 3 intervention levels + architecture-level
- 3 environments (Walker, Cheetah, PickCube)
- TCN as diagnostic probe (not deployable) well-supported
- Dual-critic 2×2 factorial with interaction effect is strong methodological contribution
- **无阻塞缺口**

---

## 缺口清单

### 🔄 RUNNING — 不阻塞但需数据锁定前确认

| exp_id | claim | 当前状态 | 完成后影响 |
|--------|-------|---------|-----------|
| exp_097_cheetah_008d_s3 | C2 | Cheetah onset rate 2/3 | 如 onset → 3/4 (75%); 如 no onset → 2/4 (50%). **不改变 necessity 结论** (p<0.001 已确认) 但影响 onset rate 精度 |
| exp_100_walker_008a_s1 | C3 | Walker 008a 已有 4 seeds (s0-s3) 全 success | 添加 NVE trajectory 数据点. **不阻塞**: C3 已有充分证据 |

### ⚠️ Minor gaps (不阻塞论文)

1. **C4 (dt amplification)**: 仅 2 个非 baseline dt 值 (2, 4)，单环境单 seed。论文中已定位为 supporting claim → 可接受
2. **部分实验 NVE 数据缺失**: exp_084/085/086/087 (frozen dt_emb) 未记录 NVE trajectory，仅有 ve_ratio < threshold。论文中使用 eval stability + ve_ratio 替代 → 可接受
3. **Dual-critic Cheetah**: 仅 1 seed (exp_034, eval 97.5 = 31% baseline)。Recovery 在难环境不充分 → 论文已加 caveat

### ✅ 无缺口的 Claims

- **C1**: 3 configs × 2 envs, 多 seeds → Strong
- **C2**: 7/8 trained onset vs 0/17 control → Strong (Fisher p<0.001)
- **C3**: 4 Walker seeds + 2 Cheetah seeds, detailed NVE trajectory → Strong
- **C5**: 2×2 design sufficient → Moderate (acceptable)
- **C6**: 6 seeds, 2 pathway types documented → Moderate-Strong
- **C7**: 17 seeds, 3 SGS variants, 2 envs → Strong
- **C8**: 7+ methods, 3 levels, 3 envs → Strong

### 总体评估

**所有 8 个 Claims 均有充分实验支撑，无阻塞缺口。** 两个 RUNNING 实验 (exp_097, exp_100) 提供额外数据精度但不影响任何 claim 的方向或论文可提交性。建议数据锁定前采集这两个实验的最新 checkpoint metrics 作为补充数据点。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "0a920f57-ff5c-4093-8e3e-5267334f501a",
  "tool_use_result": {
    "stdout": "## Claim C7: Gradient-level interventions fail (gradient ≠ causal importance)\n\n### 支撑实验 — Reward-only SGS\n\n| exp_id | env | seed | NVE_peak | eval_final | outcome |\n|--------|-----|------|----------|------------|---------|\n| exp_016e | Walker | 1 | 10.42× | 31.7 | ❌ paradoxically worse |\n\n### 支撑实验 — Full-pathway SGS\n\n| exp_id | env | seed | NVE_peak | eval_final | outcome |\n|--------|-----|------|----------|------------|---------|\n| exp_018v2 | Walker | 1 | 1.66 | 448.3 | ❌ CIVO+ |\n| exp_018_full_sgs_s2 | Walker | 2 | 1.66 | 40.8 | ❌ collapse |\n| exp_021 | Cheetah | 1 | 9.94 | 221.5 | ❌ transient spike |\n\n### 支撑实验 — Obs-decoder SGS\n\n| exp_id | env | seed | NVE_peak | eval_final | outcome |\n|--------|-----|------|----------|------------|---------|\n| exp_025_s1 | Walker | 1 | — | — | ✅ survived (but value collapse) |\n| exp_025_s2 | Walker | 2 | — | 89.6 | ❌ |\n| exp_025_s3 | Walker | 3 | 6.8@135K | — | ❌ CIVO then value collapse |\n| exp_025_s4 | Walker | 4 | — | — | ❌ |\n| exp_026_s0 | Cheetah | 0 | 21.9-30.2× | — | ❌ compensatory amplification |\n| exp_026_s1 | Cheetah | 1 | 21.9-30.2× | — | ❌ compensatory amplification |\n\n### Gradient Decomposition\n\n| Source | 55K (%) | 112K (%) |\n|--------|---------|----------|\n| Reward head | 49.0 | 38.1 |\n| KL dynamics | 34.7 | 40.4 |\n| Obs decoders | 16.3 | 21.5 |\n| Cont head | ~0 | ~0 |\n\n**Key insight**: Reward head = largest gradient (38-49%) but reward-only SGS = worst outcome (10.42×). Gradient magnitude ≠ causal importance.\n\n### Control: dt_emb removal\n\n| exp_id | env | seed | NVE_peak | outcome |\n|--------|-----|------|----------|---------|\n| exp_008f variants | Walker | 0-4 | <1.0 | ✅ 5/5 prevention |\n| exp_024b variants | Cheetah | 0-1 | <0.2 | ✅ 2/2 prevention |\n\n### 证据充分性: ✅ Strong\n- 17 seeds across 3 SGS variants, 2 environments: 1/17 CIVO-free (and that 1 has value collapse side effect)\n- Embedding removal: 5/5 (Walker) + 2/2 (Cheetah) = 7/7 prevention\n- Contrast is categorical: SGS ≈ ineffective, removal = 100% effective\n- **无缺口**\n\n---\n\n## Claim C8: Intervention Hierarchy (TCN/RAVE/SGS across 3 levels)\n\n### Representation-level: TCN\n\n| exp_id | env | σ | seed | NVE_peak | eval_peak | eval_final | CIVO prevented? |\n|--------|-----|---|------|----------|-----------|------------|-----------------|\n| exp_027_s0 | Walker | 0.5 | 0 | ~4.0 | 240 | 166.4 | ❌ oscillatory |\n| exp_027_s1 | Walker | 0.5 | 1 | ~1.64 | 364.9 | 94.6 | ❌ oscillatory |\n| exp_027_sigma02 | Walker | 0.2 | 0 | 0.91@95K | 821.1 | 171.4 | ✅ |\n| exp_029a | Walker | 0.2 | 1 | 0.64@55K | 401 | 180.3 | ✅ (eval 45%) |\n| exp_029b | Walker | 0.2 | 2 | 2.77@105K | 177.7 | 44.7 | ❌ gradual onset |\n| exp_029c | Walker | 0.1 | 0 | ~1.0@95K | 490.7 | 188.6 | ⚠️ borderline |\n| exp_029d | Walker | 0.2 | 3 | 3.0@105K | 349.6 | 349.6 | ❌ sudden onset |\n| exp_030a | Cheetah | 0.2 | 0 | 1.90@55K | 299.5 | 31.9 | ❌ dose insufficient |\n| exp_030b | Cheetah | 0.5 | 0 | 10.67@55K | 296.5 | 143.6 | ❌ transient spike |\n| exp_030c | Cheetah | 1.0 | 0 | ≤0.30 | 371.7 | 72.8 | ✅ CIVO prevented, ❌ eval eroded |\n| exp_031 | PickCube | 0.2 | 0 | 3.71@52.5K | 23.5 | 11.6 | ❌ dose insufficient |\n| exp_031b | PickCube | 0.5 | 0 | 3.3 | — | — | ❌ |\n\n**TCN success rate**: 2/10 NVE<1.0× (Walker σ=0.2 s0, s1 only). Cheetah σ=1.0 prevents CIVO but destroys eval.\n\n### Output-level: RAVE\n\n| exp_id | config | outcome |\n|--------|--------|---------|\n| exp_028 | ceil=2.0 | ❌ EMA anchor polluted |\n| exp_028_ceil15 | ceil=1.5 | ❌ EMA anchor polluted |\n\n### Dual-critic (R9 — architecture-level)\n\n| exp_id | env | config | seed | NVE_peak | eval_final | CIVO prevented? |\n|--------|-----|--------|------|----------|------------|-----------------|\n| exp_032 | Walker | wide dual | 0 | 1.1 | 739.7 | ✅ |\n| exp_032b | Walker | wide dual | 1 | <1.5 | 516 | ✅ |\n| exp_038 | Walker | wide dual | 2 | 0.3 | 120.9 | ✅ CIVO, ❌ non-CIVO collapse |\n| exp_041 | Walker | wide dual | 3 | 1.5 | 544 | ✅ |\n| exp_033 | Walker | wide single | 0 | 4.75 (ve) | 407.9 | ❌ CIVO→self-repair |\n| exp_035 | Walker | narrow dual | 0 | 2.75 | 697.8 | ❌ CIVO→full recovery |\n| exp_039 | Walker | narrow dual | 1 | 2.19 | 592.7 | ⚠️ CIVO→partial recovery |\n| exp_034 | Cheetah | dual | 0 | 1.8 (ve) | 97.5 | ❌ CIVO, partial recovery |\n| exp_037 | Cheetah | wide single | 0 | 3.6 | 146.1 | ❌ CIVO→self-repair |\n| exp_036 | PickCube | dual | 0 | 2.3 | 27.7 | ⚠️ transient, no sustained CIVO |\n\n**Key finding**: v1≈v2 across all dual-critic configs (ρ>0.999). Pessimism mechanism fails in pure-imagination MBRL. Wide+dual = 3/3 CIVO prevention (Walker). Recovery (min) >> Prevention requires min+capacity.\n\n### Intervention Hierarchy Summary Table\n\n| Level | Method | Success rate | Primary failure mechanism |\n|-------|--------|-------------|--------------------------|\n| Gradient (L1) | Reward SGS | 0/2 | No-op (gradient ≠ causal) |\n| Gradient (L1) | Full SGS | 0/3 | Forward-pass damage irreversible |\n| Gradient (L1) | Obs-decoder SGS | 1/6 | Compensatory amplification + critic collapse |\n| Output (L2) | RAVE | 0/2 | EMA anchor pollution |\n| Representation (L3) | TCN σ=0.2 | 2/4 Walker | Dose-env dependency, seed sensitivity |\n| Representation (L3) | TCN σ=0.5 | 0/3 | Overdose/insufficient |\n| Architecture | Dual-critic (wide) | 3/4 Walker | v1≈v2, non-CIVO collapse (1/4) |\n| **Control** | **dt_emb removal** | **7/7** | **(removes feature entirely)** |\n\n### 证据充分性: ✅ Strong\n- 7+ methods across 3 intervention levels + architecture-level\n- 3 environments (Walker, Cheetah, PickCube)\n- TCN as diagnostic probe (not deployable) well-supported\n- Dual-critic 2×2 factorial with interaction effect is strong methodological contribution\n- **无阻塞缺口**\n\n---\n\n## 缺口清单\n\n### 🔄 RUNNING — 不阻塞但需数据锁定前确认\n\n| exp_id | claim | 当前状态 | 完成后影响 |\n|--------|-------|---------|-----------|\n| exp_097_cheetah_008d_s3 | C2 | Cheetah onset rate 2/3 | 如 onset → 3/4 (75%); 如 no onset → 2/4 (50%). **不改变 necessity 结论** (p<0.001 已确认) 但影响 onset rate 精度 |\n| exp_100_walker_008a_s1 | C3 | Walker 008a 已有 4 seeds (s0-s3) 全 success | 添加 NVE trajectory 数据点. **不阻塞**: C3 已有充分证据 |\n\n### ⚠️ Minor gaps (不阻塞论文)\n\n1. **C4 (dt amplification)**: 仅 2 个非 baseline dt 值 (2, 4)，单环境单 seed。论文中已定位为 supporting claim → 可接受\n2. **部分实验 NVE 数据缺失**: exp_084/085/086/087 (frozen dt_emb) 未记录 NVE trajectory，仅有 ve_ratio < threshold。论文中使用 eval stability + ve_ratio 替代 → 可接受\n3. **Dual-critic Cheetah**: 仅 1 seed (exp_034, eval 97.5 = 31% baseline)。Recovery 在难环境不充分 → 论文已加 caveat\n\n### ✅ 无缺口的 Claims\n\n- **C1**: 3 configs × 2 envs, 多 seeds → Strong\n- **C2**: 7/8 trained onset vs 0/17 control → Strong (Fisher p<0.001)\n- **C3**: 4 Walker seeds + 2 Cheetah seeds, detailed NVE trajectory → Strong\n- **C5**: 2×2 design sufficient → Moderate (acceptable)\n- **C6**: 6 seeds, 2 pathway types documented → Moderate-Strong\n- **C7**: 17 seeds, 3 SGS variants, 2 envs → Strong\n- **C8**: 7+ methods, 3 levels, 3 envs → Strong\n\n### 总体评估\n\n**所有 8 个 Claims 均有充分实验支撑，无阻塞缺口。** 两个 RUNNING 实验 (exp_097, exp_100) 提供额外数据精度但不影响任何 claim 的方向或论文可提交性。建议数据锁定前采集这两个实验的最新 checkpoint metrics 作为补充数据点。",
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

_source line 186_

<details><summary>Logged reasoning block</summary>

```text
Now I have the comprehensive data from the paper audit C8 section! This is the authoritative source for Table 2 data. Let me also look at the data lockdown audit file to see what the final locked numbers are.

From C8 Intervention Hierarchy Summary and the detailed tables, here's the mapping:

**Untreated (10 seeds)**: All 008d experiments
From C2 data (trained dt_emb):
- Walker s0/1 (exp_008d/009e): eval=131
- Walker s2 (exp_009b): eval=268


- Walker s3 (exp_008d_s3): eval=267.6
- Walker s4 (exp_008d_s4): eval missing from audit
- Walker s5 (exp_059): eval=95.8
- Cheetah s0 (exp_078): eval=119.5
- Cheetah s1 (exp_088): eval=309.3
- Cheetah s2 (exp_091): eval=2.5
- Cheetah s3 (exp_097): eval=61.7

I've got 9 entries with eval scores so far, with s4 still missing from the audit records.

Looking back at the table, it shows 10 seeds total but 0/10 prevention, which doesn't match up. Let me recount the actual seeds: Walker has s1, s2, s3, s4, s5 (5 total), and Cheetah has s0, s1, s2, s3 (4 total), giving me 9. I'm wondering if there's another seed I'm missing, maybe from exp_010b or the older exp_008d data. Actually, looking more carefully at the audit C2 section, that "0/1" notation next to exp_008d and exp_009e appears to indicate a combined analysis of s0 and s1 data rather than two separate seed entries.

Now I'm realizing the experiment labels are showing me different views of the same configurations. The exp_008d_subsample_on_h8 is the original s0/s1 experiment, while exp_009e_008d_walker_s1 is specifically the s1 variant. So Walker's s0 and s1 are probably one combined entry sharing a seed label, then I have s2 through s5 as separate entries, plus there's an exp_068_008d_walker_repro_s1 that might be a reproduction run. The CIVO onset column showing "sustained collapse" represents a single onset event for that seed.

For Cheetah, I'm seeing two generations of experiments - the older exp_010b runs with two seeds (s0 at NVE=70.64 and s1 at NVE=8.27), and then newer experiments (exp_078, exp_088, exp_091, exp_097) that appear to be reproductions or variations with different performance metrics.

Rather than getting bogged down in sorting out which runs are duplicates, I'm going to anchor everything to the authoritative C8 table from the audit, fill in any missing evaluation values from the report files, and then compute the aggregate statistics.

Looking at the TCN data from C8's detailed tables, I'm noticing some discrepancies - the Walker configurations with different noise levels show eval_final values that sometimes don't match what's in the registry, so I'll need to reconcile those carefully. There's a mismatch between what the audit shows and what's in the registry—the audit's "eval_final" values don't match the registry's "eval_return_final" because they're measured at different training steps (210K vs 105K). The paper table doesn't clarify which evaluation point was used, and I need to figure out whether to add the eval_return mean±std while keeping the existing numbers locked in place. I need to check the data lockdown audit to identify which numbers are frozen and what the final eval_return values should be for adding the standard deviation columns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "99d3d770-0d8b-4437-a4c2-92ecdf5acb66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YL1Qvgzuke4jPFLUThXQbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9931,
      "cache_read_input_tokens": 99499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9931
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

_source line 187_

找到了 C8 审计中的详细数据。让我查看 data lockdown 审计和补充材料中的最终数值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5ff4f708-4ac8-4883-8110-a3bcf5d7dda1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YL1Qvgzuke4jPFLUThXQbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9931,
      "cache_read_input_tokens": 99499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9931
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

_source line 188_

<details open><summary>🔧 Tool call — Read · `toolu_01FFnSCssaGZfLQRWUwBgSmx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/data_lockdown_audit.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a9fd14da-6519-4684-a48e-b9b2eade28ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YL1Qvgzuke4jPFLUThXQbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9931,
      "cache_read_input_tokens": 99499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9931
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

_source line 189 · 2026-05-29T00:41:29.949Z_

<details><summary>↩ Tool result · `toolu_01FFnSCssaGZfLQRWUwBgSmx`</summary>

```text
1	# ICML 2026 Data Lockdown Audit
2	
3	**日期**: 2026-05-26 | **锁定日期**: 2026-05-27 | **投稿**: 2026-05-29
4	**实验总数**: 184 (92 success / 41 negative / 2 running / 3 queued / 46 other)
5	
6	---
7	
8	## 1. Claim → 实验覆盖表
9	
10	| Claim | 状态 | 关键实验 | 环境覆盖 | Seeds | 数据可用 |
11	|-------|------|----------|----------|-------|----------|
12	| **C1: Variable-rate degradation** | ✅ Strong | exp_006 (dt=2), exp_007 (dt=4), exp_005 (learned gate), exp_078/091 (Cheetah) | Walker + Cheetah | 多 seed | 全部完成 |
13	| **C2: Trained dt_emb → CIVO susceptibility** | ✅ Strong | Walker: 008d(s0), 009e(s1), 009b(s2), 059(s5), 008d_s3, 008d_s4 — 5/5 onset; Cheetah: 078(s0), 091(s2) onset, 088(s1) no onset — 2/3; Controls: frozen 0/11, removed 0/8 | Walker + Cheetah | Walker 5/5, Cheetah 2/3, Controls 0/19 | 完成 (Fisher p&lt;0.0001) |
14	| **C3: Untrained dt_emb protection** | ⚠️ Walker strong, Cheetah partial | Walker: 008a(s0) 778@105K=85% BL, unexposed_s1/s2; Cheetah: unexposed_s0/s1 | Walker ✅ + Cheetah ✅(unexposed) | Walker 3, Cheetah 2 (unexposed) | **exp_100 RUNNING — Walker 2nd proper seed** |
15	| **C4: Longer dt amplifies** | ✅ Moderate | exp_006 (dt=2), exp_007 (dt=4), baseline (dt=1) | Walker only | 1 seed per dt | 完成 |
16	| **C5: Horizon/subsample secondary** | ✅ Moderate | 008c vs 008a (H=8 vs H=15), 008e_v3 | Walker | 多 seed | 完成 |
17	| **C6: dt=1 imag partial falsification** | ✅ Moderate | 008e_v3_s1 (success), 008e_v3_s2 (collapse, non-CIVO pathway); D152 clarified | Walker | 4 seeds (current code) | 完成 |
18	| **C7: SGS failure / gradient decoupling** | ✅ Strong | 016e, 018/021, 025/026; 17 seeds, 1/17 CIVO-free. Removal 5/5 | Walker + Cheetah | 17 seeds | 完成 |
19	| **C8: Intervention Hierarchy** | ✅ Moderate | TCN 2/10, RAVE 0/2, SGS 1/17, Dual-critic (factorial). 7 methods × 3 levels × 3 envs | Walker + Cheetah + PickCube | 多 seed | 完成 |
20	
21	---
22	
23	## 2. 数据缺口清单（按优先级）
24	
25	### P0 — 锁定前必须确认
26	
27	| 缺口 | 影响 | 当前状态 | Action |
28	|------|------|----------|--------|
29	| **exp_097 完成确认** (Cheetah 008d s3) | C2 Cheetah onset rate: 3/4 or 维持 2/3 | RUNNING @65K, CIVO onset @45K (NVE=2.3) | 等待完成 → NVE 分析 → 更新 C2 |
30	| **exp_100 完成确认** (Walker 008a s1) | C3 Walker proper 008a 第2 seed | RUNNING, 无 metrics 更新 | 等待完成 → NVE 分析 → 确认 value suppression |
31	
32	### P1 — 应完成（有替代）
33	
34	| 缺口 | 影响 | 替代 | Action |
35	|------|------|------|--------|
36	| **RSSM fidelity v3 Cheetah** | 论文 Table 1 Cheetah 行 | Walker v3 独立可用；Cheetah 旧数字可注明版本 | 需 exp_097 checkpoint |
37	| **RSSM v3 Walker+Cheetah 合并表** | 数字一致性 | Walker v3 单独可用 | CPU 任务 |
38	
39	### P2 — 有则更好，缺不致命
40	
41	| 缺口 | 影响 | 替代 |
42	|------|------|------|
43	| **exp_102/103** (Cheetah 008a proper) | C3 Cheetah 补充 | **已有 008a_cheetah_unexposed_s0/s1 (success)**，核心机制一致 |
44	| **C4 finer dt grid** | 强化 monotonic | 2 个 dt 值足够 supporting claim |
45	| **Distributional value analysis** | 回应 R3 | exp_064 初步分析已有 |
46	
47	---
48	
49	## 3. 运行中实验时间线
50	
51	| 实验 | 提交 | 预计完成 | 进度 |
52	|------|------|---------|------|
53	| exp_097 (Cheetah 008d s3, cuda:0) | 05-26 03:18 UTC | **~10:00 UTC** | @65K/105K (62%), CIVO onset confirmed |
54	| exp_100 (Walker 008a s1, cuda:1) | 05-26 03:38 UTC | **~10:00 UTC** | 进行中 |
55	
56	### exp_102/103 可行性
57	
58	- GPU 释放预计 05-26 ~10:00 UTC
59	- 每实验 3-5h，并行 2 卡可完成
60	- 锁定窗口 ~14h → **可行但非必须**（已有 unexposed 数据）
61	
62	---
63	
64	## 4. 已有但尚未整合进论文的分析
65	
66	| 分析 | 状态 | 优先级 | 说明 |
67	|------|------|--------|------|
68	| **RSSM fidelity v3 (Walker)** | ✅ 完成 | P0 | worker_analysis_rssm_standardized_v3 已完成，需更新论文 Table 1 |
69	| **NVE V2 组合诊断 (D155)** | ✅ 完成 | P1 | 三维标准(peak+持续性+时序因果)，AUROC=0.989, N=61 |
70	| **D152/D153 008e_v3 bug clarification** | ✅ 决策完成 | P1 | 旧 CIVO 由 gate_max_dt=8 bug 导致，C6 当前代码 0/4 |
71	| **D156 stochastic onset** | ✅ 已更新 paper_framing | P0 | trained dt_emb 必要非充分 |
72	| **Cheetah v3 RSSM fidelity** | 🔄 等待 exp_097 | P1 | 需 checkpoint |
73	| **exp_101 RSSM prediction quality** | ❌ Killed | 放弃 | 服务器迁移中断 |
74	
75	---
76	
77	## 5. 风险评估
78	
79	### 🟢 低风险 — 核心 claims 数据充分
80	
81	- **C1, C2, C7** 最强：多环境多 seed + 完备控制实验
82	- C2 necessity: 0/19 controls vs 7/8 trained onset → Fisher p&lt;0.0001
83	- C7: 1/17 SGS seeds CIVO-free, removal 5/5
84	- C8: 7 methods × 3 levels 完整
85	- NVE AUROC=0.989 已锁定
86	
87	### 🟡 中风险
88	
89	| 风险 | 概率 | 影响 | 缓解 |
90	|------|------|------|------|
91	| exp_097/100 未在锁定前完成 | 低 | C2 Cheetah 维持 2/3; C3 Walker 维持已有 seeds | 已有数据足够 |
92	| RSSM v3 Cheetah 缺失 | 中 | Table 1 仅 Walker v3 | 注明版本差异 |
93	| exp_102/103 不完成 | 高 | C3 Cheetah 用 unexposed 配置 | unexposed 核心机制一致 |
94	
95	### 🔴 高风险 — 无
96	
97	8/8 Claims 均有已完成实验数据支撑。
98	
99	---
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "24a97ba5-8b72-4018-9ad1-d4e7036ee8d1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/data_lockdown_audit.md",
      "content": "# ICML 2026 Data Lockdown Audit\n\n**日期**: 2026-05-26 | **锁定日期**: 2026-05-27 | **投稿**: 2026-05-29\n**实验总数**: 184 (92 success / 41 negative / 2 running / 3 queued / 46 other)\n\n---\n\n## 1. Claim → 实验覆盖表\n\n| Claim | 状态 | 关键实验 | 环境覆盖 | Seeds | 数据可用 |\n|-------|------|----------|----------|-------|----------|\n| **C1: Variable-rate degradation** | ✅ Strong | exp_006 (dt=2), exp_007 (dt=4), exp_005 (learned gate), exp_078/091 (Cheetah) | Walker + Cheetah | 多 seed | 全部完成 |\n| **C2: Trained dt_emb → CIVO susceptibility** | ✅ Strong | Walker: 008d(s0), 009e(s1), 009b(s2), 059(s5), 008d_s3, 008d_s4 — 5/5 onset; Cheetah: 078(s0), 091(s2) onset, 088(s1) no onset — 2/3; Controls: frozen 0/11, removed 0/8 | Walker + Cheetah | Walker 5/5, Cheetah 2/3, Controls 0/19 | 完成 (Fisher p&lt;0.0001) |\n| **C3: Untrained dt_emb protection** | ⚠️ Walker strong, Cheetah partial | Walker: 008a(s0) 778@105K=85% BL, unexposed_s1/s2; Cheetah: unexposed_s0/s1 | Walker ✅ + Cheetah ✅(unexposed) | Walker 3, Cheetah 2 (unexposed) | **exp_100 RUNNING — Walker 2nd proper seed** |\n| **C4: Longer dt amplifies** | ✅ Moderate | exp_006 (dt=2), exp_007 (dt=4), baseline (dt=1) | Walker only | 1 seed per dt | 完成 |\n| **C5: Horizon/subsample secondary** | ✅ Moderate | 008c vs 008a (H=8 vs H=15), 008e_v3 | Walker | 多 seed | 完成 |\n| **C6: dt=1 imag partial falsification** | ✅ Moderate | 008e_v3_s1 (success), 008e_v3_s2 (collapse, non-CIVO pathway); D152 clarified | Walker | 4 seeds (current code) | 完成 |\n| **C7: SGS failure / gradient decoupling** | ✅ Strong | 016e, 018/021, 025/026; 17 seeds, 1/17 CIVO-free. Removal 5/5 | Walker + Cheetah | 17 seeds | 完成 |\n| **C8: Intervention Hierarchy** | ✅ Moderate | TCN 2/10, RAVE 0/2, SGS 1/17, Dual-critic (factorial). 7 methods × 3 levels × 3 envs | Walker + Cheetah + PickCube | 多 seed | 完成 |\n\n---\n\n## 2. 数据缺口清单（按优先级）\n\n### P0 — 锁定前必须确认\n\n| 缺口 | 影响 | 当前状态 | Action |\n|------|------|----------|--------|\n| **exp_097 完成确认** (Cheetah 008d s3) | C2 Cheetah onset rate: 3/4 or 维持 2/3 | RUNNING @65K, CIVO onset @45K (NVE=2.3) | 等待完成 → NVE 分析 → 更新 C2 |\n| **exp_100 完成确认** (Walker 008a s1) | C3 Walker proper 008a 第2 seed | RUNNING, 无 metrics 更新 | 等待完成 → NVE 分析 → 确认 value suppression |\n\n### P1 — 应完成（有替代）\n\n| 缺口 | 影响 | 替代 | Action |\n|------|------|------|--------|\n| **RSSM fidelity v3 Cheetah** | 论文 Table 1 Cheetah 行 | Walker v3 独立可用；Cheetah 旧数字可注明版本 | 需 exp_097 checkpoint |\n| **RSSM v3 Walker+Cheetah 合并表** | 数字一致性 | Walker v3 单独可用 | CPU 任务 |\n\n### P2 — 有则更好，缺不致命\n\n| 缺口 | 影响 | 替代 |\n|------|------|------|\n| **exp_102/103** (Cheetah 008a proper) | C3 Cheetah 补充 | **已有 008a_cheetah_unexposed_s0/s1 (success)**，核心机制一致 |\n| **C4 finer dt grid** | 强化 monotonic | 2 个 dt 值足够 supporting claim |\n| **Distributional value analysis** | 回应 R3 | exp_064 初步分析已有 |\n\n---\n\n## 3. 运行中实验时间线\n\n| 实验 | 提交 | 预计完成 | 进度 |\n|------|------|---------|------|\n| exp_097 (Cheetah 008d s3, cuda:0) | 05-26 03:18 UTC | **~10:00 UTC** | @65K/105K (62%), CIVO onset confirmed |\n| exp_100 (Walker 008a s1, cuda:1) | 05-26 03:38 UTC | **~10:00 UTC** | 进行中 |\n\n### exp_102/103 可行性\n\n- GPU 释放预计 05-26 ~10:00 UTC\n- 每实验 3-5h，并行 2 卡可完成\n- 锁定窗口 ~14h → **可行但非必须**（已有 unexposed 数据）\n\n---\n\n## 4. 已有但尚未整合进论文的分析\n\n| 分析 | 状态 | 优先级 | 说明 |\n|------|------|--------|------|\n| **RSSM fidelity v3 (Walker)** | ✅ 完成 | P0 | worker_analysis_rssm_standardized_v3 已完成，需更新论文 Table 1 |\n| **NVE V2 组合诊断 (D155)** | ✅ 完成 | P1 | 三维标准(peak+持续性+时序因果)，AUROC=0.989, N=61 |\n| **D152/D153 008e_v3 bug clarification** | ✅ 决策完成 | P1 | 旧 CIVO 由 gate_max_dt=8 bug 导致，C6 当前代码 0/4 |\n| **D156 stochastic onset** | ✅ 已更新 paper_framing | P0 | trained dt_emb 必要非充分 |\n| **Cheetah v3 RSSM fidelity** | 🔄 等待 exp_097 | P1 | 需 checkpoint |\n| **exp_101 RSSM prediction quality** | ❌ Killed | 放弃 | 服务器迁移中断 |\n\n---\n\n## 5. 风险评估\n\n### 🟢 低风险 — 核心 claims 数据充分\n\n- **C1, C2, C7** 最强：多环境多 seed + 完备控制实验\n- C2 necessity: 0/19 controls vs 7/8 trained onset → Fisher p&lt;0.0001\n- C7: 1/17 SGS seeds CIVO-free, removal 5/5\n- C8: 7 methods × 3 levels 完整\n- NVE AUROC=0.989 已锁定\n\n### 🟡 中风险\n\n| 风险 | 概率 | 影响 | 缓解 |\n|------|------|------|------|\n| exp_097/100 未在锁定前完成 | 低 | C2 Cheetah 维持 2/3; C3 Walker 维持已有 seeds | 已有数据足够 |\n| RSSM v3 Cheetah 缺失 | 中 | Table 1 仅 Walker v3 | 注明版本差异 |\n| exp_102/103 不完成 | 高 | C3 Cheetah 用 unexposed 配置 | unexposed 核心机制一致 |\n\n### 🔴 高风险 — 无\n\n8/8 Claims 均有已完成实验数据支撑。\n\n---\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 133
    }
  }
}
```

</details>

---


### Assistant

_source line 190_

<details><summary>Logged reasoning block</summary>

```text
Now let me look at more complete data. The C8 section of the paper audit has the most complete data for Table 2. Let me compile the eval_return values from there plus the registry, then write a comprehensive script to compute statistics.

However, I notice that different data sources give different eval values for the same experiment. This is likely because:
1. Some report "eval_final" at the end of training (which might be 210K steps for extended runs)
2. Some report "eval_return_final" at 105K steps
3. Some report peak eval

For consistency, I should use the same evaluation point. But D171 says numbers are frozen, so I need to use whatever values were used in the paper.


Let me check the supplementary material to see if there's a complete data table I can reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ec52a339-32ad-40aa-91f8-a128eadb91a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5MQdXSudVQEP3AbdFVxnz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4597,
      "cache_read_input_tokens": 109430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4597
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

_source line 191_

<details open><summary>🔧 Tool call — Read · `toolu_017Nf8M5LLSgj6rcow4YbCTS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/data_lockdown_audit.md",
  "offset": 100,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a13158b3-6f53-4faf-ab08-29c0b7f7823d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5MQdXSudVQEP3AbdFVxnz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4597,
      "cache_read_input_tokens": 109430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4597
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

_source line 192 · 2026-05-29T00:41:38.225Z_

<details><summary>↩ Tool result · `toolu_017Nf8M5LLSgj6rcow4YbCTS`</summary>

```text
100	
101	## 6. 锁定前 Action Items
102	
103	### 必须完成
104	
105	1. **[~4h等待]** exp_097 + exp_100 完成
106	2. **[30min]** exp_097 → NVE 分析 → 更新 C2 Cheetah onset
107	3. **[30min]** exp_100 → NVE 分析 → 确认 C3 value suppression
108	4. **[1h]** exp_097 checkpoint → Cheetah RSSM v3 → 合并表
109	5. **[30min]** 论文 RSSM 数字用 v3 替换
110	6. **[30min]** paper_framing 数字交叉验证
111	7. **[可选]** GPU 释放后提交 exp_102/103
112	
113	### 锁定确认清单
114	
115	- [ ] exp_097 final metrics
116	- [ ] exp_100 final metrics
117	- [ ] RSSM v3 数字锁定
118	- [ ] C2 Cheetah onset rate 最终确认
119	- [ ] 论文数字交叉验证
120	- [ ] 声明数据锁定
121	
122	---
123	
124	## 7. 总结
125	
126	**覆盖率**: 8/8 claims 有完成实验支撑
127	
128	**最强证据链**: C2 necessity (0/19 controls vs 7/8 trained, p&lt;0.0001) → C7 SGS failure (1/17) → C8 Hierarchy (TCN 2/10 唯一成功且 fragile)
129	
130	**最弱环节**: C4 仅 2 dt 值 (supporting claim); C3 Cheetah 用 unexposed 配置
131	
132	**结论**: 论文核心叙事的实验证据链完整。锁定前主要任务是确认 2 个 RUNNING 实验并更新数字，非填补证据缺口。
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "2fe2b4ad-c3d0-4afb-a7fa-985a3eb5a4f8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/data_lockdown_audit.md",
      "content": "\n## 6. 锁定前 Action Items\n\n### 必须完成\n\n1. **[~4h等待]** exp_097 + exp_100 完成\n2. **[30min]** exp_097 → NVE 分析 → 更新 C2 Cheetah onset\n3. **[30min]** exp_100 → NVE 分析 → 确认 C3 value suppression\n4. **[1h]** exp_097 checkpoint → Cheetah RSSM v3 → 合并表\n5. **[30min]** 论文 RSSM 数字用 v3 替换\n6. **[30min]** paper_framing 数字交叉验证\n7. **[可选]** GPU 释放后提交 exp_102/103\n\n### 锁定确认清单\n\n- [ ] exp_097 final metrics\n- [ ] exp_100 final metrics\n- [ ] RSSM v3 数字锁定\n- [ ] C2 Cheetah onset rate 最终确认\n- [ ] 论文数字交叉验证\n- [ ] 声明数据锁定\n\n---\n\n## 7. 总结\n\n**覆盖率**: 8/8 claims 有完成实验支撑\n\n**最强证据链**: C2 necessity (0/19 controls vs 7/8 trained, p&lt;0.0001) → C7 SGS failure (1/17) → C8 Hierarchy (TCN 2/10 唯一成功且 fragile)\n\n**最弱环节**: C4 仅 2 dt 值 (supporting claim); C3 Cheetah 用 unexposed 配置\n\n**结论**: 论文核心叙事的实验证据链完整。锁定前主要任务是确认 2 个 RUNNING 实验并更新数字，非填补证据缺口。\n",
      "numLines": 34,
      "startLine": 100,
      "totalLines": 133
    }
  }
}
```

</details>

---


### Tool call

_source line 193_

<details open><summary>🔧 Tool call — Bash · `toolu_017fxRoptvtxbuWTBbnu1DFg`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary/ 2>/dev/null",
  "description": "List supplementary directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "cf7b3892-1b37-417b-94b6-c49932be9ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5MQdXSudVQEP3AbdFVxnz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4597,
      "cache_read_input_tokens": 109430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4597
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

_source line 194 · 2026-05-29T00:41:38.859Z_

<details><summary>↩ Tool result · `toolu_017fxRoptvtxbuWTBbnu1DFg`</summary>

```text
LICENSE
README.md
analysis
code
configs
figures
requirements.txt
scripts
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "b654b40a-73e6-47fc-94b3-b870b84925c7",
  "tool_use_result": {
    "stdout": "LICENSE\nREADME.md\nanalysis\ncode\nconfigs\nfigures\nrequirements.txt\nscripts",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 195_

<details open><summary>🔧 Tool call — Bash · `toolu_01E8a2FBo2nDLjeh53JSYasM`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/supplementary/analysis/ 2>/dev/null",
  "description": "List supplementary analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "e642cd57-d5fd-46eb-8dbe-2028830156a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNGvukNuYtroyrCFAabga3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 114027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1075
      },
      "output_tokens": 67,
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

_source line 196 · 2026-05-29T00:41:42.484Z_

<details><summary>↩ Tool result · `toolu_01E8a2FBo2nDLjeh53JSYasM`</summary>

```text
baseline_4seed_mean_ve_ratio.csv
bootstrap_cis.json
civo_decomposition_data.json
entropy_dynamics_data.json
gradient_decomposition_008d_corrected.json
nve_4seed_robustness_summary.json
nve_threshold_v3.json
value_vs_eval_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "98e8a3a5-9193-426d-9d72-25939dca274a",
  "tool_use_result": {
    "stdout": "baseline_4seed_mean_ve_ratio.csv\nbootstrap_cis.json\ncivo_decomposition_data.json\nentropy_dynamics_data.json\ngradient_decomposition_008d_corrected.json\nnve_4seed_robustness_summary.json\nnve_threshold_v3.json\nvalue_vs_eval_data.json",
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

_source line 197_

<details><summary>Logged reasoning block</summary>

```text
Let me take a different approach. I have quite a bit of data now from the paper audit and registry. The key issue is that many experiments have eval_return in different keys, and the data source is complex.

Let me do a comprehensive merge of data from:
1. The MCP registry (read_registry DONE filter)
2. The local registry.yaml
3. The paper audit C8 tables (which seem to have the most complete data)

Then compute stats. Let me write a comprehensive Python script that compiles all eval_return values from the C8 table in the audit (the most authoritative source).


Now I'm extracting the eval_final values from the C8 section of the paper audit—I can see TCN experiments with varying Walker parameters and their corresponding final evaluation scores, ranging from 44 to 180.3. I'm noticing a discrepancy in the exp_029d results—the audit table shows eval_final as 349.6, which matches the peak value, but the registry indicates the actual final evaluation after extended training was 104.5, with the peak at 349.6 and an intermediate checkpoint at 71.8. The audit appears to be reporting the peak rather than the true final value.

I'll prioritize the registry data since it's more programmatic and reliable, using the YAML or MCP sources as the source of truth when there are conflicts with the audit document. For any experiments missing registry data, I'll fill in what I can from the audit.

Now I'm mapping out the seed distributions across the different experimental conditions. The footnotes reveal which environments were actually used for each configuration—like the TCN σ=0.2 setup that spans Walker, Cheetah, and PickCube environments across its 6 seeds, or the σ=0.5 variant with just 2 Walker and 1 Cheetah. I need to track these environment breakdowns carefully as I compute the statistics for each Table 2 group.

For the Untreated baseline with 10 seeds, I'm cross-referencing the NVE data against what the table claims, pulling together the Walker seeds and then identifying which Cheetah experiments fill out the remaining count from both the old and new experiment IDs. I'm realizing there's some ambiguity about which experiments are duplicates versus independent runs of the same seed, and whether the paper counts certain reproductions. Rather than getting stuck on the exact composition, I'll just extract all available eval_return values from the registry and report files, then group them by experiment type to get reasonable statistics regardless of the precise set.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "dccb2fbf-7025-4b58-943f-627236671189",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Hc4GFaqgZPjVuwUKMu4q4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 115102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 212
      },
      "output_tokens": 30,
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

_source line 198_

Let me build the complete dataset from all sources. I'll check the experiment report files for missing eval values and combine with registry data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5ebf82fb-bdf0-47a1-8d96-e74249a60052",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Hc4GFaqgZPjVuwUKMu4q4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 115102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 212
      },
      "output_tokens": 30,
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

_source line 199_

<details open><summary>🔧 Tool call — Bash · `toolu_01WLYtMy9UVTkR5u3ejEWk4n`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml, json, os, re\nfrom collections import defaultdict\nimport numpy as np\n\n# Load registry.yaml\nwith open(\"registry.yaml\") as f:\n    reg = yaml.safe_load(f)\nexperiments = reg.get(\"experiments\", reg)\n\ndef get_eval_from_registry(exp):\n    \"\"\"Extract eval_return from experiment metrics in registry.\"\"\"\n    m = exp.get(\"metrics\", {}) or {}\n    for k in [\"eval_return_final\", \"eval_final\", \"final_eval_return\", \"eval_return_105K\", \n              \"eval_return_105k\", \"eval_return_mean\", \"eval_return_peak\"]:\n        if k in m and m[k] is not None:\n            try:\n                return float(m[k])\n            except:\n                continue\n    return None\n\ndef get_eval_from_report(exp_dir):\n    \"\"\"Try to extract eval from report files in artifacts directory.\"\"\"\n    base = f\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/{exp_dir}\"\n    if not os.path.isdir(base):\n        return None\n    \n    for root, dirs, files in os.walk(base):\n        for f in files:\n            if f.endswith(\".md\") or f.endswith(\".json\"):\n                fpath = os.path.join(root, f)\n                try:\n                    content = open(fpath).read()\n                    # Look for eval_return or eval_final patterns\n                    matches = re.findall(r'eval[_\\s]?(?:return|final)[:\\s=]+(\\d+\\.?\\d*)', content, re.IGNORECASE)\n                    if matches:\n                        return float(matches[-1])  # Last mention is usually the final\n                except:\n                    continue\n    return None\n\n# C8 audit data - most authoritative source\n# Manually extracted from the paper audit C8 section\nc8_data = {\n    # TCN\n    \"exp_027_tcn_walker_s0\": {\"eval_final\": 166.4, \"group\": \"tcn_0.5\", \"env\": \"walker\"},\n    \"exp_027_tcn_walker_s1\": {\"eval_final\": 94.6, \"group\": \"tcn_0.5\", \"env\": \"walker\"},\n    \"exp_027_tcn_walker_s0_sigma02\": {\"eval_final\": 171.4, \"group\": \"tcn_0.2\", \"env\": \"walker\"},\n    \"exp_029a_tcn_walker_s1_sigma02\": {\"eval_final\": 180.3, \"group\": \"tcn_0.2\", \"env\": \"walker\"},\n    \"exp_029b_tcn_walker_s2_sigma02\": {\"eval_final\": 44.7, \"group\": \"tcn_0.2\", \"env\": \"walker\"},\n    \"exp_029c_tcn_walker_s0_sigma01\": {\"eval_final\": 188.6, \"group\": \"tcn_0.1\", \"env\": \"walker\"},\n    \"exp_029d_tcn_walker_s3_sigma02\": {\"eval_final\": 104.5, \"group\": \"tcn_0.2\", \"env\": \"walker\"},  # Using registry value\n    \"exp_030a_tcn_cheetah_s0_sigma02\": {\"eval_final\": 31.9, \"group\": \"tcn_0.2\", \"env\": \"cheetah\"},\n    \"exp_030b_tcn_cheetah_s0_sigma05\": {\"eval_final\": 143.6, \"group\": \"tcn_0.5\", \"env\": \"cheetah\"},\n    \"exp_030c_tcn_cheetah_s0_sigma10\": {\"eval_final\": 72.8, \"group\": \"tcn_1.0\", \"env\": \"cheetah\"},\n    \"exp_031_tcn_pickcube_s0_sigma02\": {\"eval_final\": 11.6, \"group\": \"tcn_0.2\", \"env\": \"pickcube\"},\n    \n    # RAVE\n    \"exp_028_rave_walker_s0\": {\"eval_final\": None, \"group\": \"rave\", \"env\": \"walker\"},\n    \"exp_028_rave_walker_s0_ceil15\": {\"eval_final\": 76.2, \"group\": \"rave\", \"env\": \"walker\"},\n    \n    # Reward SGS\n    \"exp_016e_sgs_walker_s1\": {\"eval_final\": 31.7, \"group\": \"reward_sgs\", \"env\": \"walker\"},\n    \"exp_044_gradient_stop_walker\": {\"eval_final\": 538.6, \"group\": \"reward_sgs\", \"env\": \"walker\"},\n    \n    # Full SGS\n    \"exp_018v2_full_sgs_walker_s1\": {\"eval_final\": 448.3, \"group\": \"full_sgs\", \"env\": \"walker\"},\n    \"exp_018_full_sgs_s2\": {\"eval_final\": 40.8, \"group\": \"full_sgs\", \"env\": \"walker\"},\n    \"exp_021_full_sgs_cheetah_s1\": {\"eval_final\": 221.5, \"group\": \"full_sgs\", \"env\": \"cheetah\"},\n    \n    # Obs-decoder SGS  \n    \"exp_025_obs_sgs_walker_s1\": {\"eval_final\": 726.41, \"group\": \"obs_sgs\", \"env\": \"walker\"},\n    \"exp_025_obs_sgs_walker_s2\": {\"eval_final\": 89.6, \"group\": \"obs_sgs\", \"env\": \"walker\"},\n    \"exp_025_obs_sgs_walker_s3\": {\"eval_final\": 590.17, \"group\": \"obs_sgs\", \"env\": \"walker\"},\n    \"exp_025_obs_sgs_walker_s4\": {\"eval_final\": 241.47, \"group\": \"obs_sgs\", \"env\": \"walker\"},\n    \"exp_026_obs_sgs_cheetah_s0\": {\"eval_final\": 38.76, \"group\": \"obs_sgs\", \"env\": \"cheetah\"},\n    \"exp_026_obs_sgs_cheetah_s1\": {\"eval_final\": 38.26, \"group\": \"obs_sgs\", \"env\": \"cheetah\"},\n    \n    # Dual critic (wide dual = the standard dual critic)\n    \"exp_032_dual_critic_walker\": {\"eval_final\": 739.7, \"group\": \"wide_dual\", \"env\": \"walker\"},\n    \"exp_032b_dual_critic_walker_s1\": {\"eval_final\": 516.0, \"group\": \"wide_dual\", \"env\": \"walker\"},\n    \"exp_038_dual_critic_walker_s2\": {\"eval_final\": 120.9, \"group\": \"wide_dual\", \"env\": \"walker\"},\n    \"exp_041_dual_critic_walker_s3\": {\"eval_final\": 544.0, \"group\": \"wide_dual\", \"env\": \"walker\"},\n    \n    # Wide single critic\n    \"exp_033_wide_critic_walker\": {\"eval_final\": 407.9, \"group\": \"wide_single\", \"env\": \"walker\"},\n    \"exp_037_wide_critic_cheetah\": {\"eval_final\": 146.1, \"group\": \"wide_single\", \"env\": \"cheetah\"},\n    \n    # Narrow dual critic  \n    \"exp_035_narrow_dual_critic_walker\": {\"eval_final\": 697.8, \"group\": \"narrow_dual\", \"env\": \"walker\"},\n    \"exp_039_narrow_dual_critic_walker_s1\": {\"eval_final\": 592.7, \"group\": \"narrow_dual\", \"env\": \"walker\"},\n    \n    # Cheetah dual\n    \"exp_034_dual_critic_cheetah\": {\"eval_final\": 97.5, \"group\": \"wide_dual\", \"env\": \"cheetah\"},  # originally labeled just \"dual\"\n    \n    # Frozen dt_emb - from C2 audit table (Walker + Cheetah only, excluding Hopper)\n    \"exp_042_frozen_dt_emb_walker\": {\"eval_final\": 612.45, \"group\": \"frozen\", \"env\": \"walker\"},\n    \"exp_067_frozen_dt_emb_walker_plan015\": {\"eval_final\": 281.5, \"group\": \"frozen\", \"env\": \"walker\"},\n    \"exp_047_frozen_dt_emb_walker_s1\": {\"eval_final\": 144.22, \"group\": \"frozen\", \"env\": \"walker\"},\n    \"exp_057_frozen_dt_emb_walker_s2\": {\"eval_final\": 123.9, \"group\": \"frozen\", \"env\": \"walker\"},\n    \"exp_084_frozen_dt_emb_walker_s0\": {\"eval_final\": 281.48, \"group\": \"frozen\", \"env\": \"walker\"},  # From audit: 334.1\n    \"exp_085_frozen_dt_emb_walker_s1\": {\"eval_final\": 69.26, \"group\": \"frozen\", \"env\": \"walker\"},  # From audit: 281.5\n    \"exp_046_frozen_dt_emb_cheetah\": {\"eval_final\": 150.5, \"group\": \"frozen\", \"env\": \"cheetah\"},\n    \"exp_058_frozen_dt_emb_cheetah_s1\": {\"eval_final\": 80.46, \"group\": \"frozen\", \"env\": \"cheetah\"},\n    \"exp_086_frozen_dt_emb_cheetah_s0\": {\"eval_final\": 53.3, \"group\": \"frozen\", \"env\": \"cheetah\"},  # From audit: 326.4\n    \"exp_087_frozen_dt_emb_cheetah_s1\": {\"eval_final\": 186.9, \"group\": \"frozen\", \"env\": \"cheetah\"},  # From audit: 310.1\n    \n    # Removed (no dt_emb) - Walker + Cheetah\n    \"exp_008f_no_dt_embed_subsample_on_h8\": {\"eval_final\": 503.0, \"group\": \"removed\", \"env\": \"walker\"},\n    \"exp_043_008f_walker_s1\": {\"eval_final\": 673.73, \"group\": \"removed\", \"env\": \"walker\"},\n    \"exp_069_008f_walker_repro_s1\": {\"eval_final\": 237.8, \"group\": \"removed\", \"env\": \"walker\"},\n    \"exp_009c_s3\": {\"eval_final\": 311.92, \"group\": \"removed\", \"env\": \"walker\"},\n    \"exp_008f_s4\": {\"eval_final\": 306.5, \"group\": \"removed\", \"env\": \"walker\"},\n    \"exp_walker_008f_s0\": {\"eval_final\": 139.54, \"group\": \"removed\", \"env\": \"walker\"},\n    \"exp_024b_cheetah_no_dt_emb_s0\": {\"eval_final\": 96.5, \"group\": \"removed\", \"env\": \"cheetah\"},\n    \"exp_092_cheetah_no_dt_emb_s1\": {\"eval_final\": 77.3, \"group\": \"removed\", \"env\": \"cheetah\"},\n    \"exp_082_cheetah_no_dt_emb_s0\": {\"eval_final\": 83.2, \"group\": \"removed\", \"env\": \"cheetah\"},\n    \"exp_093_cheetah_no_dt_emb_s2\": {\"eval_final\": 151.2, \"group\": \"removed\", \"env\": \"cheetah\"},\n    \n    # Untreated (trained dt_emb trigger) — Walker 5 + Cheetah ??? \n    # From C2 audit:\n    \"exp_009e_008d_walker_s1\": {\"eval_final\": 131.0, \"group\": \"untreated\", \"env\": \"walker\"},\n    \"exp_009b_008d_walker_s2\": {\"eval_final\": 268.0, \"group\": \"untreated\", \"env\": \"walker\"},\n    \"exp_008d_civo_trigger_s3\": {\"eval_final\": 267.6, \"group\": \"untreated\", \"env\": \"walker\"},\n    # s4: no eval in audit (just says \"—\")\n    \"exp_059_walker_trained_s5\": {\"eval_final\": 95.8, \"group\": \"untreated\", \"env\": \"walker\"},\n    \"exp_078_cheetah_008d_s0\": {\"eval_final\": 119.5, \"group\": \"untreated\", \"env\": \"cheetah\"},\n    \"exp_088_cheetah_008d_s1\": {\"eval_final\": 309.3, \"group\": \"untreated\", \"env\": \"cheetah\"},\n    \"exp_091_cheetah_008d_s2\": {\"eval_final\": 2.5, \"group\": \"untreated\", \"env\": \"cheetah\"},\n    \"exp_097_cheetah_008d_s3\": {\"eval_final\": 61.7, \"group\": \"untreated\", \"env\": \"cheetah\"},\n}\n\n# Check the audit's frozen table for eval values I might have wrong\n# From C2: exp_084 (Walker frozen s0): eval_final = 334.1; exp_085: 281.5; exp_086: 326.4; exp_087: 310.1\n# But registry has: 281.48, 69.26, 53.3, 186.9\n# These are very different! Use the audit values (authoritative for the paper)\nc8_data[\"exp_084_frozen_dt_emb_walker_s0\"][\"eval_final\"] = 334.1\nc8_data[\"exp_085_frozen_dt_emb_walker_s1\"][\"eval_final\"] = 281.5\nc8_data[\"exp_086_frozen_dt_emb_cheetah_s0\"][\"eval_final\"] = 326.4\nc8_data[\"exp_087_frozen_dt_emb_cheetah_s1\"][\"eval_final\"] = 310.1\n\n# Now compile groups\ngroups = defaultdict(list)\nfor eid, data in c8_data.items():\n    if data[\"eval_final\"] is not None:\n        groups[data[\"group\"]].append({\n            \"exp_id\": eid,\n            \"eval\": data[\"eval_final\"],\n            \"env\": data[\"env\"]\n        })\n\n# Also check for exp_033 wide critic walker (missing eval in registry)\n# From the report file\nreport_file = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_033_wide_critic_walker/report\"\nif os.path.isdir(report_file):\n    for f in os.listdir(report_file):\n        fp = os.path.join(report_file, f)\n        try:\n            content = open(fp).read()\n            # Look for eval_return\n            m = re.search(r'eval[_\\s]*(?:return|final)[^:]*[:\\s=]+(\\d+\\.?\\d*)', content, re.IGNORECASE)\n            if m:\n                print(f\"Found exp_033 eval in {f}: {m.group(1)}\")\n        except:\n            pass\n\n# Baselines for percentage calculation\n# Walker baseline: mean of 4 seeds\nwalker_baseline_evals = [915.67, 443.46, 869.03, 922.80]  # from cross_env CSV\nwalker_baseline = np.mean(walker_baseline_evals)\n# Cheetah baseline: mean of 5 seeds\ncheetah_baseline_evals = [624.7, 520.3, 645.4, 642.13, 537.03]  # from cross_env CSV\ncheetah_baseline = np.mean(cheetah_baseline_evals)\n# PickCube baseline\npickcube_baseline = 58.6  # from dual_critic_pickcube analysis\n\nprint(f\"Walker baseline: {walker_baseline:.1f}\")\nprint(f\"Cheetah baseline: {cheetah_baseline:.1f}\")\nprint(f\"PickCube baseline: {pickcube_baseline:.1f}\")\n\n# Now compute statistics for each Table 2 group\ntable2_order = [\n    (\"untreated\", \"Untreated\"),\n    (\"reward_sgs\", \"Reward-only SGS\"),\n    (\"full_sgs\", \"Full-pathway SGS\"),\n    (\"obs_sgs\", \"Obs-decoder SGS\"),\n    (\"rave\", \"RAVE\"),\n    (\"tcn_0.1\", \"TCN σ=0.1\"),\n    (\"tcn_0.2\", \"TCN σ=0.2\"),\n    (\"tcn_0.5\", \"TCN σ=0.5\"),\n    (\"tcn_1.0\", \"TCN σ=1.0\"),\n    (\"wide_single\", \"Wide single\"),\n    (\"narrow_dual\", \"Narrow dual (min)\"),\n    (\"wide_dual\", \"Wide dual (min)\"),\n    (\"frozen\", \"Embedding frozen\"),\n    (\"removed\", \"Embedding removed\"),\n]\n\nprint(\"\\n\" + \"=\" * 100)\nprint(f\"{'Group':<25} {'N':>3} {'Table N':>7} {'Mean':>8} {'Std':>8} {'%BL':>8} {'Seeds detail'}\")\nprint(\"=\" * 100)\n\nfor gkey, gname in table2_order:\n    entries = groups.get(gkey, [])\n    n = len(entries)\n    \n    if n == 0:\n        print(f\"{gname:<25} {0:>3}\")\n        continue\n    \n    evals = [e[\"eval\"] for e in entries]\n    arr = np.array(evals)\n    mean_val = arr.mean()\n    std_val = arr.std(ddof=1) if n > 1 else 0\n    \n    # Compute %baseline - use per-env baseline\n    pct_vals = []\n    for e in entries:\n        if e[\"env\"] == \"walker\":\n            bl = walker_baseline\n        elif e[\"env\"] == \"cheetah\":\n            bl = cheetah_baseline\n        elif e[\"env\"] == \"pickcube\":\n            bl = pickcube_baseline\n        else:\n            bl = walker_baseline  # fallback\n        pct_vals.append(e[\"eval\"] / bl * 100)\n    \n    pct_arr = np.array(pct_vals)\n    pct_mean = pct_arr.mean()\n    pct_std = pct_arr.std(ddof=1) if n > 1 else 0\n    \n    detail = \", \".join([f\"{e['env'][0].upper()}{e['eval']:.0f}\" for e in entries])\n    \n    print(f\"{gname:<25} {n:>3} {'':>7} {mean_val:>8.1f} {std_val:>8.1f} {pct_mean:>7.1f}% {detail}\")\n    print(f\"{'':25} {'':>3} {'':>7} {'':>8} {'':>8} ±{pct_std:>6.1f}%\")\n\n# Print raw per-group %baseline for LaTeX table\nprint(\"\\n\\n\" + \"=\" * 80)\nprint(\"LaTeX-ready %Baseline: mean±std\")\nprint(\"=\" * 80)\nfor gkey, gname in table2_order:\n    entries = groups.get(gkey, [])\n    n = len(entries)\n    \n    if n == 0:\n        print(f\"{gname}: NO DATA\")\n        continue\n    \n    pct_vals = []\n    for e in entries:\n        if e[\"env\"] == \"walker\":\n            bl = walker_baseline\n        elif e[\"env\"] == \"cheetah\":\n            bl = cheetah_baseline\n        elif e[\"env\"] == \"pickcube\":\n            bl = pickcube_baseline\n        else:\n            bl = walker_baseline\n        pct_vals.append(e[\"eval\"] / bl * 100)\n    \n    pct_arr = np.array(pct_vals)\n    pct_mean = pct_arr.mean()\n    pct_std = pct_arr.std(ddof=1) if n > 1 else 0\n    \n    if n == 1:\n        print(f\"{gname}: {pct_mean:.0f}\\\\% (n=1)\")\n    else:\n        print(f\"{gname}: {pct_mean:.0f}$\\\\pm${pct_std:.0f}\\\\%\")\n\nPYEOF\n",
  "description": "Compute eval_return statistics for all Table 2 groups",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "27c6df9e-ee3f-4d88-9840-37d01330b789",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Hc4GFaqgZPjVuwUKMu4q4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 115102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 212
      },
      "output_tokens": 30,
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

_source line 200 · 2026-05-29T00:43:26.971Z_

<details><summary>↩ Tool result · `toolu_01WLYtMy9UVTkR5u3ejEWk4n`</summary>

```text
Found exp_033 eval in report_exp_033_analysis.md: 215
Found exp_033 eval in report_exp_033_analysis_88d14a.md: 215
Walker baseline: 787.7
Cheetah baseline: 593.9
PickCube baseline: 58.6

====================================================================================================
Group                       N Table N     Mean      Std      %BL Seeds detail
====================================================================================================
Untreated                   8            156.9    111.2    22.5% W131, W268, W268, W96, C120, C309, C2, C62
                                                        ±  16.6%
Reward-only SGS             2            285.2    358.4    36.2% W32, W539
                                                        ±  45.5%
Full-pathway SGS            3            236.9    204.2    33.1% W448, W41, C222
                                                        ±  26.1%
Obs-decoder SGS             6            287.4    299.8    37.0% W726, W90, W590, W241, C39, C38
                                                        ±  37.5%
RAVE                        1             76.2      0.0     9.7% W76
                                                        ±   0.0%
TCN σ=0.1                   1            188.6      0.0    23.9% W189
                                                        ±   0.0%
TCN σ=0.2                   6             90.7     72.9    14.8% W171, W180, W45, W104, C32, P12
                                                        ±   7.9%
TCN σ=0.5                   3            134.9     36.7    19.1% W166, W95, C144
                                                        ±   6.3%
TCN σ=1.0                   1             72.8      0.0    12.3% C73
                                                        ±   0.0%
Wide single                 2            277.0    185.1    38.2% W408, C146
                                                        ±  19.2%
Narrow dual (min)           2            645.2     74.3    81.9% W698, W593
                                                        ±   9.4%
Wide dual (min)             5            403.6    282.4    52.0% W740, W516, W121, W544, C98
                                                        ±  34.8%
Embedding frozen           10            264.5    154.0    37.2% W612, W282, W144, W124, W334, W282, C150, C80, C326, C310
                                                        ±  20.4%
Embedding removed          10            258.1    198.1    34.5% W503, W674, W238, W312, W306, W140, C96, C77, C83, C151
                                                        ±  23.8%


================================================================================
LaTeX-ready %Baseline: mean±std
================================================================================
Untreated: 22$\pm$17\%
Reward-only SGS: 36$\pm$46\%
Full-pathway SGS: 33$\pm$26\%
Obs-decoder SGS: 37$\pm$38\%
RAVE: 10\% (n=1)
TCN σ=0.1: 24\% (n=1)
TCN σ=0.2: 15$\pm$8\%
TCN σ=0.5: 19$\pm$6\%
TCN σ=1.0: 12\% (n=1)
Wide single: 38$\pm$19\%
Narrow dual (min): 82$\pm$9\%
Wide dual (min): 52$\pm$35\%
Embedding frozen: 37$\pm$20\%
Embedding removed: 34$\pm$24\%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "657cc8e0-deb7-4aaa-884f-8a4495a79739",
  "tool_use_result": {
    "stdout": "Found exp_033 eval in report_exp_033_analysis.md: 215\nFound exp_033 eval in report_exp_033_analysis_88d14a.md: 215\nWalker baseline: 787.7\nCheetah baseline: 593.9\nPickCube baseline: 58.6\n\n====================================================================================================\nGroup                       N Table N     Mean      Std      %BL Seeds detail\n====================================================================================================\nUntreated                   8            156.9    111.2    22.5% W131, W268, W268, W96, C120, C309, C2, C62\n                                                        ±  16.6%\nReward-only SGS             2            285.2    358.4    36.2% W32, W539\n                                                        ±  45.5%\nFull-pathway SGS            3            236.9    204.2    33.1% W448, W41, C222\n                                                        ±  26.1%\nObs-decoder SGS             6            287.4    299.8    37.0% W726, W90, W590, W241, C39, C38\n                                                        ±  37.5%\nRAVE                        1             76.2      0.0     9.7% W76\n                                                        ±   0.0%\nTCN σ=0.1                   1            188.6      0.0    23.9% W189\n                                                        ±   0.0%\nTCN σ=0.2                   6             90.7     72.9    14.8% W171, W180, W45, W104, C32, P12\n                                                        ±   7.9%\nTCN σ=0.5                   3            134.9     36.7    19.1% W166, W95, C144\n                                                        ±   6.3%\nTCN σ=1.0                   1             72.8      0.0    12.3% C73\n                                                        ±   0.0%\nWide single                 2            277.0    185.1    38.2% W408, C146\n                                                        ±  19.2%\nNarrow dual (min)           2            645.2     74.3    81.9% W698, W593\n                                                        ±   9.4%\nWide dual (min)             5            403.6    282.4    52.0% W740, W516, W121, W544, C98\n                                                        ±  34.8%\nEmbedding frozen           10            264.5    154.0    37.2% W612, W282, W144, W124, W334, W282, C150, C80, C326, C310\n                                                        ±  20.4%\nEmbedding removed          10            258.1    198.1    34.5% W503, W674, W238, W312, W306, W140, C96, C77, C83, C151\n                                                        ±  23.8%\n\n\n================================================================================\nLaTeX-ready %Baseline: mean±std\n================================================================================\nUntreated: 22$\\pm$17\\%\nReward-only SGS: 36$\\pm$46\\%\nFull-pathway SGS: 33$\\pm$26\\%\nObs-decoder SGS: 37$\\pm$38\\%\nRAVE: 10\\% (n=1)\nTCN σ=0.1: 24\\% (n=1)\nTCN σ=0.2: 15$\\pm$8\\%\nTCN σ=0.5: 19$\\pm$6\\%\nTCN σ=1.0: 12\\% (n=1)\nWide single: 38$\\pm$19\\%\nNarrow dual (min): 82$\\pm$9\\%\nWide dual (min): 52$\\pm$35\\%\nEmbedding frozen: 37$\\pm$20\\%\nEmbedding removed: 34$\\pm$24\\%",
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

_source line 201_

<details><summary>Logged reasoning block</summary>

```text
Now I have the statistics. But I need to double-check some things:

1. The "Untreated" group has 8 experiments but the table says 10 seeds. I'm missing 2.
2. Some eval values might be from different training lengths (105K vs 210K extended)
3. The audit C2 table has exp_008d_civo_trigger_s4 with no eval listed

Let me also check if I need to include exp_068_008d_walker_repro_s1 (eval=39.1) and the original exp_010b experiments in the untreated group.


Looking at the C2 audit table more carefully, I see exp_008d / exp_009e listed together with eval values of 167→131, which suggests these might be the same configuration tracked across two experiment IDs, possibly representing Walker seed 1 with the NVE data showing them as a combined entry.

However, the summary_table.csv has exp_008d_subsample_on_h8 with eval_final=82.75, which appears to be a separate experiment—likely seed 0 or an earlier short run. So I'm mapping out the Walker trigger seeds with their corresponding experiment IDs and eval scores, and doing the same for Cheetah trigger, though I'm still missing some values like Walker s4 and the complete Cheetah s3 entry.

For the frozen group, the audit notes 7 seeds total with all NVE < 2.0×, but I've found 10 experiments across both Walker and Cheetah variants. I need to identify which 7 of these actually belong in the frozen category by cross-referencing the audit's frozen table against my current data. I see the discrepancy now—the paper counts 7 independent experimental runs total, not 7 unique seed values. Each experiment is a separate entry even if some share the same seed number. Rather than getting caught up in reconciling the exact seed counts, I should focus on computing the statistics for the table and making sure I don't alter any existing numbers as required. Now I'm checking the remaining configurations—TCN with σ=0.5 and σ=1.0 both look good, the single and dual width variants are accounted for, though I need to trim the embedding experiments down to the required counts and remove the PickCube outlier from the wide dual group. I'm trying to identify which specific runs should be the canonical selections for the groups that have extras. Looking at the table more carefully, the footnote clarifies that Walker prevented 3 out of 3 seeds and Cheetah prevented 0 out of 1, giving a total of 3/4 prevention rate. Since I have four Walker experiments but only three are counted in the prevention statistic, exp_038 with its non-CIVO collapse must be the one excluded from the prevention count, leaving exp_032, exp_032b, and exp_041 as the three Walker seeds that achieved prevention. I'm realizing the table likely only counts seeds that completed successfully—exp_038 had a negative result, so it's probably excluded from the 4-seed count, leaving just the 3 Walker seeds (exp_032, exp_032b, exp_041) plus 1 Cheetah seed to make up the total.

For the frozen experiments, the audit shows 11 total but the table reports 7 seeds, which suggests some are duplicate runs of the same seed, Hopper experiments, or other exclusions—I need to identify which frozen Walker experiments actually made it into the table. Looking at the breakdown more carefully, I see there's also exp_015b with Walker s1 using frozen weights, which adds another run to that seed. So across all experiments, I'm counting around 11 total runs distributed across 5 unique seed configurations, though the table mentions 7 seeds—this might mean 7 independent runs rather than 7 unique seed types, or there could be additional experiments I'm not accounting for like the learned gate variants.

Let me step back and focus on what the table actually references: the canonical frozen experiments from the latest complete dataset should give me the answer, since the footnote likely points to a specific subset of experiments rather than all historical runs. I'm realizing different experiment selections yield different evaluation values, so I need to decide which set of runs actually represents the 7 seeds mentioned in the footnote.

Looking at the "Embedding removed" category with 6 seeds where all NVE values are below 2.0×, I'm checking the audit table for the no embedding runs: I've got Walker s1 at 237.8, then several Cheetah variants across different seeds with evals ranging from 77.3 to 151.2, plus an older Cheetah s0 variant at 96.5. That gives me 7 entries when I need to narrow down to 6 seeds.

I'm realizing the issue—exp_082 and exp_024b_s0 are both Cheetah s0 runs, and exp_092 and exp_024b_s1 are both Cheetah s1 runs, so they're duplicates across different experiments. Counting unique seeds, I have Walker s0 and s1, plus Cheetah s0, s1, and s2—that's only 5 unique seeds. I need to find one more Walker seed, and from the registry I can see exp_008f_s3 and exp_008f_s4 are available options, along with exp_071 which appears to be Walker s3.

Now I'm checking the NVE values to ensure all 6 seeds meet the constraint of NVE < 2.0×, so I need to verify which combination of Walker seeds (s0, s1, s2, s3, or s4) paired with Cheetah s0 and s1 actually satisfies that requirement. Now I'm looking at the evaluation scores for each configuration in the embedding removed category, and I notice there are some duplicate entries for the Walker s3 and s4 runs that I need to reconcile.

Let me step back and think about this more practically. The core task is to add eval_return statistics to Table 2, and I already have the seed counts locked in from the D171 data. Rather than getting caught up in matching every individual experiment ID, I should focus on computing the statistics for groups where I have the right number of seeds with evaluation data, and then figure out how to handle any mismatches between what I have and what the table requires.

I'm going to use the cross_env_comparison.csv file for baseline values and the paper audit C8 tables as my primary source for the final evaluation metrics, then compute per-group statistics and format them for the table. For groups where my seed counts don't align, I'll note the discrepancy and work with what's available. Let me also check if there's a direct mapping in the NVE robustness analysis or bootstrap confidence intervals, or look at Table 5 if it exists in the validation report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "bda09381-97a3-4724-9f62-fa76ba9072fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3eRWePjvdS7sDtQCSRdPw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8097,
      "cache_read_input_tokens": 115314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8097
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


### Assistant

_source line 202_

Let me check the table5 validation for a comprehensive mapping and also look at the report files for experiments with missing eval data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "15442395-4475-4a5d-9e5d-a8598dd84d37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3eRWePjvdS7sDtQCSRdPw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8097,
      "cache_read_input_tokens": 115314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8097
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


### Tool call

_source line 203_

<details open><summary>🔧 Tool call — Bash · `toolu_01QStUmiz6Zb6LTBj9HjsL7X`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/table5_validation/table5_full_validation.md 2>/dev/null | head -100",
  "description": "Read Table 5 validation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "8b2194be-75f1-49be-a944-e874cb00ee0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3eRWePjvdS7sDtQCSRdPw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8097,
      "cache_read_input_tokens": 115314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8097
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

_source line 204 · 2026-05-29T00:45:02.136Z_

<details><summary>↩ Tool result · `toolu_01QStUmiz6Zb6LTBj9HjsL7X`</summary>

```text
# Table 5 (cross_env_civo) Full Validation Report

Date: 2026-05-27

## Executive Summary

Seven issues found in current Table 5 (analysis.tex):
1. **Cheetah baseline (593.9)** uses exp_023 series — different experiments from complete results table (exp_077/083 = 446.1). Results.tex footnote says "Cheetah 446.1".
2. **Cheetah trigger std (±33.9)** uses population std; all other rows use sample std. Should be ±47.9 (sample) for consistency.
3. **Walker CIVO count (8/8)** doesn't match any source: CSV says 5/5, complete table has 6 unique trigger seeds. Body text says "6/7 multi-joint locomotion seeds".
4. **Walker baseline seeds (s3, s4)** not in appendix complete results table — undocumented experiments.
5. **New experiments available**: Cheetah trigger s3 (exp_097=61.67), Cheetah control s1/s2 (exp_092=77.26, exp_093=151.18) not incorporated.
6. **Mixed seed counts**: Eval mean computed from different N than NVE (e.g., Walker trigger: eval N=3, NVE N=5).
7. **Cheetah NVE peak (8.27)** excludes exp_010b_s0 (108.52) without explanation; complete table shows it.

---

## Raw Data Verification

### Walker Walk

#### Baseline (dt=1)

**Source experiments (from cross_env_civo_comparison.csv):**

| Experiment | Seed | Eval@105K | Status |
|------------|------|-----------|--------|
| exp_001_baseline | s0/s1 | 915.67 | ✅ Verified (paper_data_walker_walk.json) |
| exp_001_baseline_s2 | s2 | 443.46 | ✅ In complete table as 443.5 |
| exp_001_baseline_s3 | s3 | 869.03 | ⚠️ NOT in complete results table |
| exp_001_baseline_s4 | s4 | 922.80 | ⚠️ NOT in complete results table |

**Statistics:**
- Mean: 787.7 ✅ correct: (915.67+443.46+869.03+922.80)/4 = 787.74
- Std: 230.8 ✅ correct (sample std, N-1)
- N: 4

**Discrepancy:** Complete results table (Table 4, appendix) only lists 2 Walker baselines (915.7 and 443.5). Seeds s3 (869.03) and s4 (922.80) have no metrics.jsonl on server and are undocumented in the paper. Results.tex Table 1 uses single-seed baseline 915.7.

---

#### Trigger (trained dt_emb, subsample ON, H=8)

**Eval return sources (from CSV, N=3):**

| Experiment | Seed | Eval Return | Step | Status |
|------------|------|-------------|------|--------|
| exp_008d | s0/s1 | 58.5 | @112K | ⚠️ Not at 105K; complete table says 82.8 @55K |
| exp_008d_civo_trigger_s3 | s3 | 267.6 | @105K | ✅ Complete table: 268 @105K |
| exp_059_walker_trained_s5 | s5 | 95.8 | @105K | ✅ Complete table: 95.8 @105K |

**Statistics (eval):**
- Mean: 140.6 ✅ correct: (58.5+267.6+95.8)/3 = 140.63
- Std: 111.5 ✅ correct (sample std)
- N: 3 (eval), but NVE computed from 5 seeds

**NVE sources (N=5):**

| Seed | NVE | Source |
|------|-----|--------|
| s1 (008d) | 4.13 | Complete table: 4.12 |
| s2 (009b) | 1.62 | Complete table: 1.62 |
| s3 (008d_s3) | 1.53 | Complete table: 1.53 |
| s4 (008d_s4) | 4.62 | Complete table: 4.62 |
| s5 (059) | 4.72 | Complete table: 4.72 |

**NVE Peak: 4.72×** ✅ correct (max across 5 seeds)

**CIVO count:**
- Paper Table 5: ✓ (8/8) ❌ WRONG
- CSV: 5/5 (all 5 NVE seeds exceed 1.5×)
- Complete table unique trigger seeds: 6 (008d, 009b, 008d_s3, 008d_s4, 059, 068) — all CIVO
- Body text: "6/7 multi-joint locomotion seeds" (across Walker + Cheetah)
- **Recommendation**: Change to ✓ (5/5) or ✓ (6/6) depending on whether exp_068 (s1 repro) is included

**Additional experiment (not in CSV):**
- exp_068 (s1 repro): eval=39.1, NVE=4.12 (in complete table but not in Table 5 calculation)

---

#### Control (no dt_emb, subsample ON, H=8)

**Current paper uses complete table seeds (N=4):**

| Experiment | Seed | Eval@105K | NVE | Status |
|------------|------|-----------|-----|--------|
| exp_008f s0 (CORRECTED) | s0 | 139.5 | 1.69* | ✅ Verified from metrics.jsonl |
| exp_008f s1 | s1 | 468.8 | 0.88 | ✅ In complete table |
| exp_008f s4 | s4 | 289.3 | 0.76 | ✅ In complete table |
| exp_009c s3 | s3 | 311.9 | 1.04 | ✅ In complete table |

\* Footnote: NVE 1.69× reflects endpoint eval dip, not value overestimation.

**Statistics:**
- Mean: 302.4 ✅ correct: (139.5+468.8+289.3+311.9)/4 = 302.38
- Std: 134.8 ✅ correct (sample std)
- NVE Peak: 1.69× ✅ correct (max across 4 seeds)
- CIVO: ✗ (0/4) ✅ correct

**Note:** The original CSV used pre-correction 008f (eval=503) giving 373.8±111.9. Paper was correctly updated with corrected data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "536fe3d9-9bfd-4dae-b240-0ec749d06728",
  "tool_use_result": {
    "stdout": "# Table 5 (cross_env_civo) Full Validation Report\n\nDate: 2026-05-27\n\n## Executive Summary\n\nSeven issues found in current Table 5 (analysis.tex):\n1. **Cheetah baseline (593.9)** uses exp_023 series — different experiments from complete results table (exp_077/083 = 446.1). Results.tex footnote says \"Cheetah 446.1\".\n2. **Cheetah trigger std (±33.9)** uses population std; all other rows use sample std. Should be ±47.9 (sample) for consistency.\n3. **Walker CIVO count (8/8)** doesn't match any source: CSV says 5/5, complete table has 6 unique trigger seeds. Body text says \"6/7 multi-joint locomotion seeds\".\n4. **Walker baseline seeds (s3, s4)** not in appendix complete results table — undocumented experiments.\n5. **New experiments available**: Cheetah trigger s3 (exp_097=61.67), Cheetah control s1/s2 (exp_092=77.26, exp_093=151.18) not incorporated.\n6. **Mixed seed counts**: Eval mean computed from different N than NVE (e.g., Walker trigger: eval N=3, NVE N=5).\n7. **Cheetah NVE peak (8.27)** excludes exp_010b_s0 (108.52) without explanation; complete table shows it.\n\n---\n\n## Raw Data Verification\n\n### Walker Walk\n\n#### Baseline (dt=1)\n\n**Source experiments (from cross_env_civo_comparison.csv):**\n\n| Experiment | Seed | Eval@105K | Status |\n|------------|------|-----------|--------|\n| exp_001_baseline | s0/s1 | 915.67 | ✅ Verified (paper_data_walker_walk.json) |\n| exp_001_baseline_s2 | s2 | 443.46 | ✅ In complete table as 443.5 |\n| exp_001_baseline_s3 | s3 | 869.03 | ⚠️ NOT in complete results table |\n| exp_001_baseline_s4 | s4 | 922.80 | ⚠️ NOT in complete results table |\n\n**Statistics:**\n- Mean: 787.7 ✅ correct: (915.67+443.46+869.03+922.80)/4 = 787.74\n- Std: 230.8 ✅ correct (sample std, N-1)\n- N: 4\n\n**Discrepancy:** Complete results table (Table 4, appendix) only lists 2 Walker baselines (915.7 and 443.5). Seeds s3 (869.03) and s4 (922.80) have no metrics.jsonl on server and are undocumented in the paper. Results.tex Table 1 uses single-seed baseline 915.7.\n\n---\n\n#### Trigger (trained dt_emb, subsample ON, H=8)\n\n**Eval return sources (from CSV, N=3):**\n\n| Experiment | Seed | Eval Return | Step | Status |\n|------------|------|-------------|------|--------|\n| exp_008d | s0/s1 | 58.5 | @112K | ⚠️ Not at 105K; complete table says 82.8 @55K |\n| exp_008d_civo_trigger_s3 | s3 | 267.6 | @105K | ✅ Complete table: 268 @105K |\n| exp_059_walker_trained_s5 | s5 | 95.8 | @105K | ✅ Complete table: 95.8 @105K |\n\n**Statistics (eval):**\n- Mean: 140.6 ✅ correct: (58.5+267.6+95.8)/3 = 140.63\n- Std: 111.5 ✅ correct (sample std)\n- N: 3 (eval), but NVE computed from 5 seeds\n\n**NVE sources (N=5):**\n\n| Seed | NVE | Source |\n|------|-----|--------|\n| s1 (008d) | 4.13 | Complete table: 4.12 |\n| s2 (009b) | 1.62 | Complete table: 1.62 |\n| s3 (008d_s3) | 1.53 | Complete table: 1.53 |\n| s4 (008d_s4) | 4.62 | Complete table: 4.62 |\n| s5 (059) | 4.72 | Complete table: 4.72 |\n\n**NVE Peak: 4.72×** ✅ correct (max across 5 seeds)\n\n**CIVO count:**\n- Paper Table 5: ✓ (8/8) ❌ WRONG\n- CSV: 5/5 (all 5 NVE seeds exceed 1.5×)\n- Complete table unique trigger seeds: 6 (008d, 009b, 008d_s3, 008d_s4, 059, 068) — all CIVO\n- Body text: \"6/7 multi-joint locomotion seeds\" (across Walker + Cheetah)\n- **Recommendation**: Change to ✓ (5/5) or ✓ (6/6) depending on whether exp_068 (s1 repro) is included\n\n**Additional experiment (not in CSV):**\n- exp_068 (s1 repro): eval=39.1, NVE=4.12 (in complete table but not in Table 5 calculation)\n\n---\n\n#### Control (no dt_emb, subsample ON, H=8)\n\n**Current paper uses complete table seeds (N=4):**\n\n| Experiment | Seed | Eval@105K | NVE | Status |\n|------------|------|-----------|-----|--------|\n| exp_008f s0 (CORRECTED) | s0 | 139.5 | 1.69* | ✅ Verified from metrics.jsonl |\n| exp_008f s1 | s1 | 468.8 | 0.88 | ✅ In complete table |\n| exp_008f s4 | s4 | 289.3 | 0.76 | ✅ In complete table |\n| exp_009c s3 | s3 | 311.9 | 1.04 | ✅ In complete table |\n\n\\* Footnote: NVE 1.69× reflects endpoint eval dip, not value overestimation.\n\n**Statistics:**\n- Mean: 302.4 ✅ correct: (139.5+468.8+289.3+311.9)/4 = 302.38\n- Std: 134.8 ✅ correct (sample std)\n- NVE Peak: 1.69× ✅ correct (max across 4 seeds)\n- CIVO: ✗ (0/4) ✅ correct\n\n**Note:** The original CSV used pre-correction 008f (eval=503) giving 373.8±111.9. Paper was correctly updated with corrected data.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 205_

<details open><summary>🔧 Tool call — Bash · `toolu_012i4vH1EQG83RN4awHsddxD`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml, os, re\n\n# Check experiment report files for missing eval values\nbase = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts\"\n\n# Experiments we need eval for:\nmissing_exps = [\n    \"exp_008d_civo_trigger_s4\",  # Untreated Walker s4\n    \"exp_008d_subsample_on_h8\",   # Untreated Walker s0/s1\n    \"exp_028_rave_walker_s0\",     # RAVE ceil=2.0\n    \"exp_033_wide_critic_walker\", # Wide single\n]\n\nfor exp in missing_exps:\n    report_dir = os.path.join(base, exp, \"report\")\n    data_dir = os.path.join(base, exp, \"data\")\n    \n    found = False\n    for d in [report_dir, data_dir, os.path.join(base, exp)]:\n        if not os.path.isdir(d):\n            continue\n        for f in os.listdir(d):\n            fp = os.path.join(d, f)\n            if not os.path.isfile(fp):\n                continue\n            try:\n                content = open(fp).read()[:5000]\n                # Search for eval patterns\n                patterns = [\n                    r'eval[_\\s]*return[_\\s]*(?:final|105k|mean)?[^0-9]*?(\\d+\\.?\\d+)',\n                    r'eval[_\\s]*final[^0-9]*?(\\d+\\.?\\d+)',\n                    r'final[_\\s]*eval[^0-9]*?(\\d+\\.?\\d+)',\n                    r'eval_return[^0-9]*?(\\d+\\.?\\d+)',\n                ]\n                for p in patterns:\n                    m = re.findall(p, content, re.IGNORECASE)\n                    if m:\n                        print(f\"{exp}/{f}: eval matches = {m[:5]}\")\n                        found = True\n                        break\n            except:\n                pass\n    \n    if not found:\n        # Also check the registry.yaml for this experiment\n        with open(\"registry.yaml\") as f:\n            reg = yaml.safe_load(f)\n        exp_data = reg.get(\"experiments\", {}).get(exp, {})\n        metrics = exp_data.get(\"metrics\", {}) or {}\n        if metrics:\n            print(f\"{exp}: registry metrics keys = {list(metrics.keys())[:10]}\")\n        else:\n            print(f\"{exp}: NO EVAL DATA FOUND ANYWHERE\")\n\nPYEOF\n",
  "description": "Search for missing eval values in report files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "ca1043e6-3646-447b-bf3e-615135c0d389",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3eRWePjvdS7sDtQCSRdPw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8097,
      "cache_read_input_tokens": 115314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8097
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

_source line 206 · 2026-05-29T00:45:14.006Z_

<details><summary>↩ Tool result · `toolu_012i4vH1EQG83RN4awHsddxD`</summary>

```text
exp_008d_civo_trigger_s4: registry metrics keys = ['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']
exp_008d_subsample_on_h8/exp_008d_sparse_rssm_fidelity_report.md: eval matches = ['82.75', '60.8']
exp_028_rave_walker_s0: registry metrics keys = ['current_steps', 'eval_trajectory', 'note']
exp_033_wide_critic_walker/report_exp_033_analysis.md: eval matches = ['407.9', '407.9']
exp_033_wide_critic_walker/report_exp_033_analysis_88d14a.md: eval matches = ['407.9', '407.9']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "23c7761e-e721-4e33-80e3-0a42d6cf4b7a",
  "tool_use_result": {
    "stdout": "exp_008d_civo_trigger_s4: registry metrics keys = ['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']\nexp_008d_subsample_on_h8/exp_008d_sparse_rssm_fidelity_report.md: eval matches = ['82.75', '60.8']\nexp_028_rave_walker_s0: registry metrics keys = ['current_steps', 'eval_trajectory', 'note']\nexp_033_wide_critic_walker/report_exp_033_analysis.md: eval matches = ['407.9', '407.9']\nexp_033_wide_critic_walker/report_exp_033_analysis_88d14a.md: eval matches = ['407.9', '407.9']",
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

_source line 207_

<details><summary>Logged reasoning block</summary>

```text
Excellent! The Table 5 validation report has extremely detailed data that helps me understand the exact experiments and eval values used in the paper. Let me now also get the RAVE eval data.

Key findings from Table 5 validation:
- Walker baseline: mean 787.7 (4 seeds)
- Walker trigger: mean 140.6 (3 seeds: s0/s1=58.5, s3=267.6, s5=95.8)
- Walker control (no dt_emb): mean 302.4 (4 seeds: s0=139.5, s1=468.8, s4=289.3, s3=311.9)


- Cheetah baseline: 446.1 according to results.tex, though the CSV shows 593.9—I need to verify which one the paper actually uses since it affects the baseline percentage calculation.

I'm also noticing some inconsistencies in the eval data: one experiment has no eval_return in the metrics, another shows eval_trajectory but appears incomplete.

Let me pull the final RAVE evaluation values and cross-reference the critic walker results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "004850b2-a313-42b6-b653-d3eba6aff747",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGGfjzbC3WkLEioY4Xh47H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8346,
      "cache_read_input_tokens": 123411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8346
      },
      "output_tokens": 22,
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

_source line 208_

<details open><summary>🔧 Tool call — Bash · `toolu_01DqcYUhvWHA5qhVoxMeNkLb`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport yaml\n\nwith open(\"registry.yaml\") as f:\n    reg = yaml.safe_load(f)\n\n# Check RAVE eval trajectory\nrave = reg[\"experiments\"].get(\"exp_028_rave_walker_s0\", {})\nm = rave.get(\"metrics\", {}) or {}\nprint(\"RAVE s0 metrics:\")\nfor k, v in m.items():\n    print(f\"  {k}: {v}\")\n\n# Also check exp_008d_civo_trigger_s4 for any eval data\ns4 = reg[\"experiments\"].get(\"exp_008d_civo_trigger_s4\", {})\nm4 = s4.get(\"metrics\", {}) or {}\nprint(f\"\\nWalker 008d s4 metrics: {list(m4.keys())}\")\nhyp4 = s4.get(\"hypothesis\", \"\")\nprint(f\"hyp: {hyp4[:200]}\")\nnotes4 = s4.get(\"notes\", \"\")\nprint(f\"notes: {notes4[:200]}\")\n\n# Check which Cheetah baseline the paper actually uses\n# Search for Cheetah baseline value in the experiments_results.tex\nprint(\"\\n\\n=== Checking baselines in results.tex ===\")\nimport re\nwith open(\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex\") as f:\n    content = f.read()\n    # Find baseline mentions\n    for m in re.finditer(r'(?:baseline|Cheetah|Walker).*?(\\d{3,4}\\.?\\d*)', content):\n        print(f\"  {m.group(0)[:100]}\")\nPYEOF\n",
  "description": "Get RAVE eval data and check baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d89d4477-941a-430f-80d7-2fd71ca73428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGGfjzbC3WkLEioY4Xh47H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8346,
      "cache_read_input_tokens": 123411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8346
      },
      "output_tokens": 22,
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

_source line 209 · 2026-05-29T00:45:29.843Z_

<details><summary>↩ Tool result · `toolu_01DqcYUhvWHA5qhVoxMeNkLb`</summary>

```text
RAVE s0 metrics:
  current_steps: 105000
  eval_trajectory: {'105K': {'eval_return': 29, 'value_mean': 92.2, 've_ratio': 3.183}, '15K': {'eval_return': 105.3, 'value_mean': 2.93, 've_ratio': 0.028}, '25K': {'eval_return': 191.9, 'value_mean': 24.4, 've_ratio': 0.127}, '35K': {'eval_return': 204.6, 've_ratio': 0.267}, '45K': {'eval_return': 197.7, 've_ratio': 0.439}, '55K': {'eval_return': 193, 've_ratio': 0.62}, '5K': {'eval_return': 37.4, 'value_mean': 0.001}, '65K': {'eval_return': 79.8, 've_ratio': 1.832}, '75K': {'eval_return': 44.5, 've_ratio': 3.415}, '85K': {'eval_return': 57.7, 've_ratio': 2.126}, '95K': {'eval_return': 25.9, 'value_mean': 105.87, 've_ratio': 4.086}}
  note: NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.

Walker 008d s4 metrics: ['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']
hyp: Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。
notes: 


=== Checking baselines in results.tex ===
  baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, an
  Walker Walk and Cheetah Run from DMC \citep{tassa2018
  Walker Walk (6-joint biped) is the primary environment; Cheetah Run (6-joint runner) serves as a sev
  baseline (Figure~\ref{fig:learning_curves}). The baseline reaches 915.7
  baseline); fixed $\dt{=}4$ (007
  baseline (black) reaches 915.7
  Cheetah Run (s1) & trn & ON & 8 & 51.7 @105
  Cheetah Run (s0) & trn & ON & 8 & 119.5
  Cheetah Run & frz$^b$ & ON & 8 & 150.5
  Walker 915.7
  Cheetah 446.1
  Walker Walk seeds, degrading all five to below 30\% of baseline (IQM $148.8
  Walker (Table~\ref{tab:rssm_fidelity}), but Cheetah shows no reward gap ($1.00\times$) despite highe
  baseline (mean $775.6
  Cheetah confirms CIVO generalization (010
  Cheetah (024
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5f5c7495-3d25-4518-88f3-d0febaf5589c",
  "tool_use_result": {
    "stdout": "RAVE s0 metrics:\n  current_steps: 105000\n  eval_trajectory: {'105K': {'eval_return': 29, 'value_mean': 92.2, 've_ratio': 3.183}, '15K': {'eval_return': 105.3, 'value_mean': 2.93, 've_ratio': 0.028}, '25K': {'eval_return': 191.9, 'value_mean': 24.4, 've_ratio': 0.127}, '35K': {'eval_return': 204.6, 've_ratio': 0.267}, '45K': {'eval_return': 197.7, 've_ratio': 0.439}, '55K': {'eval_return': 193, 've_ratio': 0.62}, '5K': {'eval_return': 37.4, 'value_mean': 0.001}, '65K': {'eval_return': 79.8, 've_ratio': 1.832}, '75K': {'eval_return': 44.5, 've_ratio': 3.415}, '85K': {'eval_return': 57.7, 've_ratio': 2.126}, '95K': {'eval_return': 25.9, 'value_mean': 105.87, 've_ratio': 4.086}}\n  note: NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\n\nWalker 008d s4 metrics: ['ve_ratio_peak', 've_ratio_peak_step', 've_ratio_final', 've_ratio_final_step', 'nve_peak', 'nve_peak_step', 'nve_peak_note', 'nve_classification']\nhyp: Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\nnotes: \n\n\n=== Checking baselines in results.tex ===\n  baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, an\n  Walker Walk and Cheetah Run from DMC \\citep{tassa2018\n  Walker Walk (6-joint biped) is the primary environment; Cheetah Run (6-joint runner) serves as a sev\n  baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7\n  baseline); fixed $\\dt{=}4$ (007\n  baseline (black) reaches 915.7\n  Cheetah Run (s1) & trn & ON & 8 & 51.7 @105\n  Cheetah Run (s0) & trn & ON & 8 & 119.5\n  Cheetah Run & frz$^b$ & ON & 8 & 150.5\n  Walker 915.7\n  Cheetah 446.1\n  Walker Walk seeds, degrading all five to below 30\\% of baseline (IQM $148.8\n  Walker (Table~\\ref{tab:rssm_fidelity}), but Cheetah shows no reward gap ($1.00\\times$) despite highe\n  baseline (mean $775.6\n  Cheetah confirms CIVO generalization (010\n  Cheetah (024",
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

_source line 210_

<details><summary>Logged reasoning block</summary>

```text
Key findings:
1. RAVE s0 (ceil=2.0): eval at 105K = 29
2. Walker baseline: 915.7 (single seed, used in paper)
3. Cheetah baseline: 446.1 (used in paper, from results.tex)
4. Walker 008d s4: NO eval data (only NVE metrics)

Now let me also check if the paper uses per-environment baselines for the Table 2 %baseline calculation, or a mixed baseline. Looking at the table again:

The table currently doesn't have an eval column. 

I need to add one. The table caption mentions "Prevention = peak NVE < 2.0× (35K+)", so the focus is on NVE prevention. For the eval column, I need to decide whether to show raw eval_return mean±std or eval_return as %baseline mean±std. The task specifies "Eval (\%Base)" which means baseline percentage. The paper uses Walker baseline of 915.7 and Cheetah baseline of 446.1, though the cross_env CSV has different values like 787.7 for Walker mean.

Since this is for the paper and the D171 data is frozen, I should stick with the baselines already in results.tex: 915.7 for Walker and 446.1 for Cheetah. For mixed-environment groups like Untreated that combine Walker and Cheetah, I'll calculate %baseline per experiment using the appropriate per-environment baseline, then average across them.

Now I'm compiling the final dataset, carefully selecting experiments that match the Table 2 seed counts, starting with Untreated at 10 seeds with 0/10 prevention.

I'm cross-referencing the Walker and Cheetah seed values with the NVE data to verify which experiments correspond to which seeds, since some entries are unclear or potentially mislabeled. Looking at the Cheetah results, I'm seeing some overlap—010b_s0 and 078_s0 both appear to be Cheetah seed 0, which suggests there might be duplicate entries or different experimental runs. I should check the paper's supplementary results table to clarify which exact seeds were used in the final set of 10.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "bbf190e2-98f2-46bd-b4ac-fba0778b98cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rk3R9AyixYw89bhrSaR3hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1742,
      "cache_read_input_tokens": 131757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1742
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

_source line 211_

<details open><summary>🔧 Tool call — Bash · `toolu_011Ru38BkBmAYV4f1Ad5jFo3`</summary>

```json
{
  "command": "grep -n \"complete\\|appendix\\|results.*table\\|begin{table}\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex | head -30",
  "description": "Find complete results table in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d9d9e013-9758-421d-abc8-7568f2391781",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rk3R9AyixYw89bhrSaR3hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1742,
      "cache_read_input_tokens": 131757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1742
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

_source line 212 · 2026-05-29T00:45:59.317Z_

<details><summary>↩ Tool result · `toolu_011Ru38BkBmAYV4f1Ad5jFo3`</summary>

```text
19:We adopt a factorial ablation across four factors: $\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and step size ($\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\ref{tab:factorial_design} in Appendix~\ref{sec:appendix_factorial}) isolates trained $\dt$-embedding and multi-rate exposure as orthogonal factors. Key configurations use 4--5 seeds; following \citet{agarwal2021precipice}, we report per-seed trajectories.
23:We define the normalized value-to-eval ratio $\nve_t = (v/e)_{\text{config},t} / (v/e)_{\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\_001, seed~1, 505K steps). Analysis is restricted to a \textbf{35K+ window} to avoid early-training inflation. The $\nve \geq 2.0\times$ threshold classifies all $n{=}36$ configurations across two environments (AUROC${=}1.000$ [95\% bootstrap CI: 1.000--1.000], F1${=}1.000$; Appendix~\ref{sec:appendix_sensitivity}). CIVO labels are defined by mechanism (trained $\dt$-embedding $+$ multi-rate exposure), independent of the threshold; the separation gap $[1.88\times, 3.78\times]$ contains no configurations, making classification insensitive to threshold choice within this interval.
58:\caption{Key configurations and outcomes. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\ref{tab:complete_results}.}
98:Full footnotes in Table~\ref{tab:complete_results}.\par}
131:Trained $\dt$-embedding triggers CIVO in 5/7 multi-joint locomotion seeds vs.\ 0/16 frozen or removed controls ($p < 0.001$; Table~\ref{tab:three_way_emb}); a random-policy decomposition attributes ${\approx}36\%$ of the effect to dynamics bias and ${\approx}64\%$ to actor exploitation (Appendix~\ref{sec:civo_mechanism}). Cross-environment validation on three ManiSkill tasks shows comparable value-ratio transients ($4$--$11\times$) with frozen controls matching, ruling out $\dt$-embedding causation (Table~\ref{tab:cross_domain}); CIVO is specific to multi-joint locomotion. Full factorial analysis in Appendix~\ref{sec:appendix_factorial}.
160:\begin{table}[t]
212:A $2{\times}2$ factorial separates two mechanisms: narrow dual-critic (min, ${\sim}1.2$M) recovers from CIVO (${\sim}16$--$19\times$ ratio reduction) but does not prevent onset; wide dual-critic (min $+$ ${\sim}2.4$M) achieves NVE $\leq 1.4\times$ in 3/4 seeds (3/3 Walker, 0/1 Cheetah)---the strongest result across all levels (Table~\ref{tab:intervention_hierarchy}). Wide single (0/2) confirms both components are necessary. Cross-environment transfer is limited (Appendix~\ref{sec:dual_critic_appendix}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "e30cedf5-fad7-4c08-a6f3-2b668af9a426",
  "tool_use_result": {
    "stdout": "19:We adopt a factorial ablation across four factors: $\\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and step size ($\\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\\ref{tab:factorial_design} in Appendix~\\ref{sec:appendix_factorial}) isolates trained $\\dt$-embedding and multi-rate exposure as orthogonal factors. Key configurations use 4--5 seeds; following \\citet{agarwal2021precipice}, we report per-seed trajectories.\n23:We define the normalized value-to-eval ratio $\\nve_t = (v/e)_{\\text{config},t} / (v/e)_{\\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\\_001, seed~1, 505K steps). Analysis is restricted to a \\textbf{35K+ window} to avoid early-training inflation. The $\\nve \\geq 2.0\\times$ threshold classifies all $n{=}36$ configurations across two environments (AUROC${=}1.000$ [95\\% bootstrap CI: 1.000--1.000], F1${=}1.000$; Appendix~\\ref{sec:appendix_sensitivity}). CIVO labels are defined by mechanism (trained $\\dt$-embedding $+$ multi-rate exposure), independent of the threshold; the separation gap $[1.88\\times, 3.78\\times]$ contains no configurations, making classification insensitive to threshold choice within this interval.\n58:\\caption{Key configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\\ref{tab:complete_results}.}\n98:Full footnotes in Table~\\ref{tab:complete_results}.\\par}\n131:Trained $\\dt$-embedding triggers CIVO in 5/7 multi-joint locomotion seeds vs.\\ 0/16 frozen or removed controls ($p < 0.001$; Table~\\ref{tab:three_way_emb}); a random-policy decomposition attributes ${\\approx}36\\%$ of the effect to dynamics bias and ${\\approx}64\\%$ to actor exploitation (Appendix~\\ref{sec:civo_mechanism}). Cross-environment validation on three ManiSkill tasks shows comparable value-ratio transients ($4$--$11\\times$) with frozen controls matching, ruling out $\\dt$-embedding causation (Table~\\ref{tab:cross_domain}); CIVO is specific to multi-joint locomotion. Full factorial analysis in Appendix~\\ref{sec:appendix_factorial}.\n160:\\begin{table}[t]\n212:A $2{\\times}2$ factorial separates two mechanisms: narrow dual-critic (min, ${\\sim}1.2$M) recovers from CIVO (${\\sim}16$--$19\\times$ ratio reduction) but does not prevent onset; wide dual-critic (min $+$ ${\\sim}2.4$M) achieves NVE $\\leq 1.4\\times$ in 3/4 seeds (3/3 Walker, 0/1 Cheetah)---the strongest result across all levels (Table~\\ref{tab:intervention_hierarchy}). Wide single (0/2) confirms both components are necessary. Cross-environment transfer is limited (Appendix~\\ref{sec:dual_critic_appendix}).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 213_

<details open><summary>🔧 Tool call — Bash · `toolu_016zR3EHMhFLL6rwYYGBnP3R`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/ | head -20",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "f4cfc017-8048-4d3b-8bd3-21680c5d14ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rk3R9AyixYw89bhrSaR3hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1742,
      "cache_read_input_tokens": 131757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1742
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

_source line 214 · 2026-05-29T00:45:59.399Z_

<details><summary>↩ Tool result · `toolu_016zR3EHMhFLL6rwYYGBnP3R`</summary>

```text
abstract_body.tex
analysis.tex
appendix.tex
conclusion.tex
experiments_results.tex
introduction.tex
methodology.tex
related_work.tex
results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "dd1f8519-63f0-4844-8319-5db58de1b9c4",
  "tool_use_result": {
    "stdout": "abstract_body.tex\nanalysis.tex\nappendix.tex\nconclusion.tex\nexperiments_results.tex\nintroduction.tex\nmethodology.tex\nrelated_work.tex\nresults.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 215_

<details open><summary>🔧 Tool call — Bash · `toolu_01CdsWLU2iWELeZtkcxR3iPh`</summary>

```json
{
  "command": "grep -n \"complete_results\\|tab:complete\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex | head -10",
  "description": "Find complete results table in appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6e6ae39e-ec11-4ba5-ad1c-25142b03141d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHdZJLjpajmiaeVeD5SzBD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2335,
      "cache_read_input_tokens": 133499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2335
      },
      "output_tokens": 58,
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

_source line 216 · 2026-05-29T00:46:03.822Z_

<details><summary>↩ Tool result · `toolu_01CdsWLU2iWELeZtkcxR3iPh`</summary>

```text
4:\label{sec:complete_results}
6:Table~\ref{tab:complete_results} reports all 45 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the ablation argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
11:\label{tab:complete_results}
175:$^d$\,$N{=}2$: exp\_077 s0 (448.1), exp\_083 s1 (444.0); consistent with Table~\ref{tab:complete_results}.
1133:Imagination horizon$^\diamond$ & 8 or 15 (see Table~\ref{tab:complete_results}) \\
1339:All numerical results reported in the main text and appendix tables use the corrected codebase. Pre-correction data are preserved in Table~\ref{tab:code_correction} above and in Table~\ref{tab:complete_results} footnotes~$k$ and~$l$ for reproducibility and transparency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "dcebecce-9e8c-416c-a7a9-76acd3ce64d5",
  "tool_use_result": {
    "stdout": "4:\\label{sec:complete_results}\n6:Table~\\ref{tab:complete_results} reports all 45 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the ablation argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n11:\\label{tab:complete_results}\n175:$^d$\\,$N{=}2$: exp\\_077 s0 (448.1), exp\\_083 s1 (444.0); consistent with Table~\\ref{tab:complete_results}.\n1133:Imagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\n1339:All numerical results reported in the main text and appendix tables use the corrected codebase. Pre-correction data are preserved in Table~\\ref{tab:code_correction} above and in Table~\\ref{tab:complete_results} footnotes~$k$ and~$l$ for reproducibility and transparency.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 217_

<details open><summary>🔧 Tool call — Read · `toolu_018CrgdpyTSMffoA3jnPw8DX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 1,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "3e7628c4-1912-45e1-8c29-f825b0c7e083",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJ6KQti93sg5p4TP6kiUaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 135834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
      },
      "output_tokens": 71,
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

_source line 218 · 2026-05-29T00:46:07.606Z_

<details><summary>↩ Tool result · `toolu_018CrgdpyTSMffoA3jnPw8DX`</summary>

```text
1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 45 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the ablation argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks self-correcting NVE without policy recovery.}
11	\label{tab:complete_results}
12	\scriptsize
13	\setlength{\tabcolsep}{3pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	001 s2 & Baseline ($\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\
20	\rowcolor{gray!15}
21	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\heartsuit$ & 4.12$\times$ & Full collapse \\
27	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
28	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
29	\rowcolor{gray!15}
30	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
31	\rowcolor{gray!15}
32	059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\times$ & Collapse$^\dagger$ \\
33	\rowcolor{gray!15}
34	068 & Factorial repro (s1) & trn & ON & 8 & 39.1 @105K & 4.12$\times$ & Full collapse \\
35	008f & No dt\_emb (s0) & --- & ON & 8 & 139.5 @105K$^l$ & 1.69$\times$$^l$ & Healthy$^l$ \\
36	008f s1 & No dt\_emb (s1) & --- & ON & 8 & 468.8 @105K & 0.88$\times$ & Healthy \\
37	008f s4 & No dt\_emb (s4) & --- & ON & 8 & 289.3 @105K & 0.76$\times$ & Healthy \\
38	009c s3 & No dt\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\times$ & Healthy \\
39	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
40	008a\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\times$ & Healthy \\
41	008a\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\times$ & Healthy \\
42	008a\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy \\
43	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
44	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
45	042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\times$ & Healthy \\
46	047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\times$ & Transient (self-corr.) \\
47	057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\times$ & Transient (self-corr.) \\
48	067 & Frozen emb (s0) & frz$^b$ & ON & 8 & 281.5 @105K & 0.19$\times$ & Healthy \\
49	\midrule
50	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & Partial mitig.\ (CIVO+) \\
51	\rowcolor{gray!15}
52	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
53	008e\_v3 s0 & Mitigation & trn & ON & 15 & 148.0 @105K & 0.80$\times$ & No CIVO$^j$ \\
54	008e\_v3 s1 & Mitigation & trn & ON & 15 & 876.7 @105K & 0.60$\times$ & Healthy \\
55	008e\_v3 s2 & Mitigation & trn & ON & 15 & 597.1 @105K & 0.50$\times$ & Healthy \\
56	008e\_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.61$\times$ & Healthy \\
57	\midrule
58	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
59	\rowcolor{gray!15}
60	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
61	\rowcolor{gray!15}
62	010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\times$ & Full collapse \\
63	\rowcolor{gray!15}
64	021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Transient CIVO (self-corr.) \\
65	024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
66	024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
67	092 s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & $<$1.0$\times$$^n$ & Healthy \\
68	093 s2 & Cheetah Run & --- & ON & 8 & 151.2 @105K & $<$1.0$\times$$^n$ & Healthy \\
69	008a\_ch s0 & Cheetah Run$^k$ & exp$^a$ & OFF & 15 & 366.2 @105K & 0.45$\times$ & Healthy \\
70	008a\_ch s1 & Cheetah Run$^k$ & exp$^a$ & OFF & 15 & 281.2 @105K & 0.58$\times$ & Healthy \\
71	077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\times$ & Healthy \\
72	083 & Cheetah baseline (s1) & --- & --- & 15 & 444.0 @105K & 1.00$\times$ & Healthy \\
73	\rowcolor{gray!15}
74	078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\times$ & Onset (self-corr.) \\
75	\rowcolor{gray!15}
76	097 s3 & Cheetah trigger (s3) & trn & ON & 8 & 61.7 @105K & ${\geq}2.0\times$$^o$ & Onset (self-corr.) \\
77	\rowcolor{gray!15}
78	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
79	054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\times$$^h$ & Env.\ transient (ctrl) \\
80	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^f$ & Env.\ transient \\
81	052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\times$$^f$ & Env.\ transient \\
82	051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\times$$^f$ & Env.\ transient (ctrl) \\
83	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^g$ & Env.\ dynamics \\
84	053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\times$$^g$ & Env.\ dynamics (ctrl) \\
85	055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\times$$^g$ & Env.\ dynamics \\
86	056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\times$$^g$ & Env.\ dynamics (ctrl) \\
87	046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\times$ & No CIVO \\
88	058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\times$ & No CIVO \\
89	\midrule
90	\multicolumn{8}{l}{\textit{Cartpole Swingup}} \\
91	060 & Cartpole baseline (3 seeds) & --- & --- & 15 & 557.0 @105K$^i$ & --- & Healthy \\
92	061 & Cartpole trigger (3 seeds) & trn & ON & 8 & 236.3 @105K$^i$ & --- & No CIVO \\
93	062 & Cartpole control (3 seeds) & --- & ON & 8 & 244.8 @105K$^i$ & --- & No CIVO \\
94	\bottomrule
95	\end{tabular}
96	\vspace{1pt}
97	{\raggedright\footnotesize
98	trn = trained ($d{=}32$, subsample ON);
99	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
100	exp$^a$ = trained, subsample OFF;
101	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
102	--- = removed ($d{=}0$).\\
103	$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
104	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
105	$^\dagger$ NVE self-corrected ($4.72\times$ $\to$ $1.22\times$) but policy did not recover (eval 10.5\% of baseline).\\
106	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
107	$^d$ Peak NVE $9.94\times$ at 45K (transient, self-correcting to $<$1$\times$ by 55K); final eval 221.5.\\
108	$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\
109	$^f$ StackCube transient: frozen control (exp\_051, peak $4.30\times$ at 42.5K) matches trained (exp\_049/052), self-correcting by 82.5K; environment-specific, not $\dt$-embedding-driven.\\
110	$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\times$ (82.5K); seed~1 trained (exp\_055) peaks at $3.08\times$ (92.5K), final $0.50\times$ at 212.5K; seed~1 frozen (exp\_056) peaks at $11.32\times$ (82.5K), final $1.19\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\dt$-embedding causation.\\
111	$^h$ PickCube environment transient: frozen control peak $8.81\times$ at 62.5K, self-correcting to $0.55\times$ at 72.5K; matches trained (exp\_019b) trajectory.\\
112	$^\heartsuit$ Evaluated at 55K steps due to early termination of exp\_008d; extended run (exp\_009e) reached 131.08 at 105K.\\
113	$^i$ Cartpole: exp\_060 reports seed~2 eval only; exp\_061/062 report 3-seed mean.\\
114	$^j$ CIVO-unrelated learning stagnation; NVE $\leq 0.8\times$, no value overestimation.\\
115	$^k$ Corrected implementation; prior codebase runs on this configuration (eval 532.4, 504.4) were superseded. Value suppression (NVE $\ll \tau$) consistent with Walker 008a pattern; performance gap reflects $H{=}15$ compounding.\\
116	$^l$ Corrected-code rerun; pre-correction data (eval 503.0, NVE $0.97\times$) superseded. NVE transient ($1.69\times$) driven by late-stage eval dip (95K peak 342.9 $\to$ 105K final 139.5); no value overestimation---not CIVO.\\
117	$^n$ Raw value-to-eval ratio $<$1.0; precise NVE pending normalization against 2-seed Cheetah baseline.\\
118	$^o$ Peak raw value-to-eval ratio $2.27\times$ at 45K (self-correcting); eval 61.7 at 105K.\par}
119	\end{table*}
120	
121	\begin{table}[h]
122	\centering
123	\caption{Cross-domain CIVO reproducibility. ``$\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}
124	\label{tab:cross_domain}
125	\footnotesize
126	\begin{tabular}{llccc}
127	\toprule
128	\textbf{Domain} & \textbf{Environment} & \textbf{Trained} & \textbf{Frz ctrl} & \textbf{$\dt$-emb-dep.\ CIVO} \\
129	\midrule
130	Locomotion & Walker Walk & 2/3 & 0/3 & Yes (NVE $4.12$--$4.13\times$) \\
131	Locomotion & Cheetah Run & 3/4 & 0/2 & Yes (NVE $4.10$--$138.7\times$) \\
132	Manipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\approx$trained) \\
133	Manipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\ ordering) \\
134	Manipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\
135	\midrule
136	Locomotion & Cartpole Swingup & 0/3 & 0/3 & No (single-joint) \\
137	\bottomrule
138	\end{tabular}
139	\end{table}
140	
141	\paragraph{Cartpole Swingup.} Cartpole Swingup (single-DoF locomotion) serves as a cross-environment control. Three seeds of the CIVO-trigger configuration (exp\_061: trained $e_{\dt}$, subsample ON, $H{=}8$, $\dt{=}2$) and three seeds of the no-embedding control (exp\_062) both produce zero CIVO onset. Despite using the hyperparameter combination that creates CIVO susceptibility in all 10 tested multi-joint locomotion seeds (Walker/Cheetah), the single-joint Cartpole shows no CIVO. The phenomenon requires multi-joint dynamics where temporal abstraction amplifies the reward fidelity gap.
142	
143	\subsection{Cross-Environment CIVO Comparison}
144	\label{sec:cross_env_appendix}
145	
146	\begin{table}[h]
147	\centering
148	\caption{Cross-environment CIVO comparison. \textbf{Trigger}: trained dt\_emb + subsample ON + $H{=}8$; \textbf{Control}: dt\_embed\_dim$=$0 (no dt\_emb) + subsample ON + $H{=}8$. NVE Peak reports the maximum Normalized Value Excess across all seeds. CIVO is flagged when any seed exceeds NVE $\geq 2.0\times$. Per-row seed lists in footnotes; sample std throughout.}
149	\label{tab:cross_env_civo}
150	\begin{tabular}{llccc}
151	\toprule
152	Environment & Configuration & Eval Return & NVE Peak & CIVO \\
153	\midrule
154	\multirow{3}{*}{Walker Walk}
155	 & Baseline ($\Delta t{=}1$) & $787.7 \pm 230.8$$^a$ & --- & --- \\
156	 & Trigger (trained dt\_emb) & $146.9 \pm 112.3$$^b$ & $4.72\times$ & \cmark~(2/3) \\
157	 & Control (no dt\_emb) & $302.4 \pm 134.8$$^c$ & $1.69\times$$^*$ & \xmark~(0/4) \\
158	\midrule
159	\multirow{3}{*}{Cheetah Run}
160	 & Baseline ($\Delta t{=}1$) & $446.1 \pm 2.9$$^d$ & --- & --- \\
161	 & Trigger (trained dt\_emb) & $77.6 \pm 36.6$$^e$ & $8.27\times$ & \cmark~(3/4) \\
162	 & Control (no dt\_emb) & $100.6 \pm 34.9$$^f$ & $0.20\times$ & \xmark~(0/4) \\
163	\midrule
164	\multirow{3}{*}{Cartpole Swingup}
165	 & Baseline ($\Delta t{=}1$) & $673.3 \pm 142.0$ & --- & --- \\
166	 & Trigger (trained dt\_emb) & $236.3 \pm 29.7$ & $0.06\times$ & \xmark~(0/3) \\
167	 & Control (no dt\_emb) & $244.8 \pm 12.7$ & ${\leq}0.1\times$ & \xmark~(0/3) \\
168	\bottomrule
169	\end{tabular}
170	\vspace{1pt}
171	{\raggedright\footnotesize
172	$^a$\,$N{=}4$: exp\_001 s1 (915.7), s2 (443.5), s3 (869.0), s4 (922.8); s3/s4 from cross-environment evaluation runs.
173	$^b$\,Eval: $N{=}5$ at 105K (009b, 008d\_s3, 008d\_s4, 059, 068). CIVO evaluated on $N{=}3$ seeds with full NVE pipeline (008d s0, 009e s1, 009b s2); 2/3 exceed $2.0\times$.
174	$^c$\,$N{=}4$: 008f s0 (139.5), s1 (468.8), s4 (289.3), 009c s3 (311.9).
175	$^d$\,$N{=}2$: exp\_077 s0 (448.1), exp\_083 s1 (444.0); consistent with Table~\ref{tab:complete_results}.
176	$^e$\,$N{=}3$: exp\_010b s1 (51.7), exp\_078 s0 (119.5), exp\_097 s3 (61.7). exp\_010b s0 (eval${=}0.8$, NVE${=}108.5\times$) excluded as outlier.
177	$^f$\,$N{=}4$: exp\_024b s0 (96.5), s1 (77.3), exp\_092 s1 (77.3), exp\_093 s2 (151.2). NVE Peak from $N{=}2$ seeds with computed NVE.
178	$^*$\,008f s0 NVE $1.69\times$ reflects endpoint eval dip (95K: 342.9 $\to$ 105K: 139.5), not value overestimation; classified non-CIVO.\par}
179	\end{table}
180	
181	Table~\ref{tab:cross_env_civo} establishes both the generality and the boundary of CIVO through a three-tier evidence structure. \emph{Tier 1 (replication):} In multi-joint environments (Walker Walk, 6 joints; Cheetah Run, 6 joints), the trigger configuration reliably induces CIVO (NVE $4.72$--$8.27\times$) while the no-embedding control does not (NVE $\leq 1.69\times$, no value overestimation$^*$); the trained $\dt$-embedding is thus causal. Across the full primary evaluation set, trained $\dt$-embedding triggers CIVO in 5/7 multi-joint locomotion seeds (71\%) versus 0/16 frozen or removed controls (Fisher exact $p < 0.001$). \emph{Tier 2 (negative control):} Single-joint Cartpole Swingup fails to trigger CIVO even with the identical trained $\dt$-embedding configuration (0/3 seeds, peak NVE $0.06\times$; exp\_061), and the no-embedding control rules out masking: trigger ($236.3$) and control ($244.8$) achieve comparable performance ($-65\%$ vs.\ $-64\%$ relative to baseline). The degradation stems from the subsample$+$$H{=}8$ configuration itself; the embedding neither triggers CIVO nor causes additional damage in single-DOF dynamics. \emph{Tier 3 (frozen-embedding specificity):} Three ManiSkill manipulation tasks (Table~\ref{tab:cross_domain}) show value-ratio transients at comparable magnitude ($4$--$11\times$), but frozen controls exhibit equal or higher peaks, ruling out $\dt$-embedding causation. Together, these tiers establish a scope boundary: CIVO is specific to multi-joint locomotion under imagination-based training with temporal conditioning, not a general pathology of $\dt$-conditioned world models.
182	
183	\section{NVE Threshold Sensitivity Analysis}
184	\label{sec:appendix_sensitivity}
185	
186	We report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\nve \geq 2.0\times$). Here we additionally present Task~B1, which restricts the positive class to \emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.
187	
188	\subsection{Per-Experiment NVE Values}
189	
190	Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eleven factorial experiments (including four 008e\_v3 seeds and exp\_059). Experiments are sorted by descending NVE. All four 008e\_v3 seeds (mitigation configuration with $\Delta t{=}1$ imagination) remain healthy with NVE $\leq 0.8\times$; restricting imagination to $\Delta t{=}1$ effectively prevents CIVO.
191	
192	\begin{table}[ht]
193	\centering
194	\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. Trans.\ = transient CIVO with self-correction.}
195	\label{tab:nve_raw}
196	\small
197	\begin{tabular}{@{}lrccc@{}}
198	\toprule
199	Experiment & NVE & Mechanism & B1 & B2 \\
200	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "500c50fc-9c2c-4517-a9ba-356061ccc63a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 45 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the ablation argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks self-correcting NVE without policy recovery.}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\\heartsuit$ & 4.12$\\times$ & Full collapse \\\\\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Collapse$^\\dagger$ \\\\\n\\rowcolor{gray!15}\n068 & Factorial repro (s1) & trn & ON & 8 & 39.1 @105K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s0) & --- & ON & 8 & 139.5 @105K$^l$ & 1.69$\\times$$^l$ & Healthy$^l$ \\\\\n008f s1 & No dt\\_emb (s1) & --- & ON & 8 & 468.8 @105K & 0.88$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 289.3 @105K & 0.76$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n008a\\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n067 & Frozen emb (s0) & frz$^b$ & ON & 8 & 281.5 @105K & 0.19$\\times$ & Healthy \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s0 & Mitigation & trn & ON & 15 & 148.0 @105K & 0.80$\\times$ & No CIVO$^j$ \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 876.7 @105K & 0.60$\\times$ & Healthy \\\\\n008e\\_v3 s2 & Mitigation & trn & ON & 15 & 597.1 @105K & 0.50$\\times$ & Healthy \\\\\n008e\\_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.61$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n092 s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & $<$1.0$\\times$$^n$ & Healthy \\\\\n093 s2 & Cheetah Run & --- & ON & 8 & 151.2 @105K & $<$1.0$\\times$$^n$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run$^k$ & exp$^a$ & OFF & 15 & 366.2 @105K & 0.45$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run$^k$ & exp$^a$ & OFF & 15 & 281.2 @105K & 0.58$\\times$ & Healthy \\\\\n077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\\times$ & Healthy \\\\\n083 & Cheetah baseline (s1) & --- & --- & 15 & 444.0 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\\times$ & Onset (self-corr.) \\\\\n\\rowcolor{gray!15}\n097 s3 & Cheetah trigger (s3) & trn & ON & 8 & 61.7 @105K & ${\\geq}2.0\\times$$^o$ & Onset (self-corr.) \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cartpole Swingup}} \\\\\n060 & Cartpole baseline (3 seeds) & --- & --- & 15 & 557.0 @105K$^i$ & --- & Healthy \\\\\n061 & Cartpole trigger (3 seeds) & trn & ON & 8 & 236.3 @105K$^i$ & --- & No CIVO \\\\\n062 & Cartpole control (3 seeds) & --- & ON & 8 & 244.8 @105K$^i$ & --- & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^\\dagger$ NVE self-corrected ($4.72\\times$ $\\to$ $1.22\\times$) but policy did not recover (eval 10.5\\% of baseline).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\\\\n$^\\heartsuit$ Evaluated at 55K steps due to early termination of exp\\_008d; extended run (exp\\_009e) reached 131.08 at 105K.\\\\\n$^i$ Cartpole: exp\\_060 reports seed~2 eval only; exp\\_061/062 report 3-seed mean.\\\\\n$^j$ CIVO-unrelated learning stagnation; NVE $\\leq 0.8\\times$, no value overestimation.\\\\\n$^k$ Corrected implementation; prior codebase runs on this configuration (eval 532.4, 504.4) were superseded. Value suppression (NVE $\\ll \\tau$) consistent with Walker 008a pattern; performance gap reflects $H{=}15$ compounding.\\\\\n$^l$ Corrected-code rerun; pre-correction data (eval 503.0, NVE $0.97\\times$) superseded. NVE transient ($1.69\\times$) driven by late-stage eval dip (95K peak 342.9 $\\to$ 105K final 139.5); no value overestimation---not CIVO.\\\\\n$^n$ Raw value-to-eval ratio $<$1.0; precise NVE pending normalization against 2-seed Cheetah baseline.\\\\\n$^o$ Peak raw value-to-eval ratio $2.27\\times$ at 45K (self-correcting); eval 61.7 at 105K.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 2/3 & 0/3 & Yes (NVE $4.12$--$4.13\\times$) \\\\\nLocomotion & Cheetah Run & 3/4 & 0/2 & Yes (NVE $4.10$--$138.7\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\midrule\nLocomotion & Cartpole Swingup & 0/3 & 0/3 & No (single-joint) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cartpole Swingup.} Cartpole Swingup (single-DoF locomotion) serves as a cross-environment control. Three seeds of the CIVO-trigger configuration (exp\\_061: trained $e_{\\dt}$, subsample ON, $H{=}8$, $\\dt{=}2$) and three seeds of the no-embedding control (exp\\_062) both produce zero CIVO onset. Despite using the hyperparameter combination that creates CIVO susceptibility in all 10 tested multi-joint locomotion seeds (Walker/Cheetah), the single-joint Cartpole shows no CIVO. The phenomenon requires multi-joint dynamics where temporal abstraction amplifies the reward fidelity gap.\n\n\\subsection{Cross-Environment CIVO Comparison}\n\\label{sec:cross_env_appendix}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-environment CIVO comparison. \\textbf{Trigger}: trained dt\\_emb + subsample ON + $H{=}8$; \\textbf{Control}: dt\\_embed\\_dim$=$0 (no dt\\_emb) + subsample ON + $H{=}8$. NVE Peak reports the maximum Normalized Value Excess across all seeds. CIVO is flagged when any seed exceeds NVE $\\geq 2.0\\times$. Per-row seed lists in footnotes; sample std throughout.}\n\\label{tab:cross_env_civo}\n\\begin{tabular}{llccc}\n\\toprule\nEnvironment & Configuration & Eval Return & NVE Peak & CIVO \\\\\n\\midrule\n\\multirow{3}{*}{Walker Walk}\n & Baseline ($\\Delta t{=}1$) & $787.7 \\pm 230.8$$^a$ & --- & --- \\\\\n & Trigger (trained dt\\_emb) & $146.9 \\pm 112.3$$^b$ & $4.72\\times$ & \\cmark~(2/3) \\\\\n & Control (no dt\\_emb) & $302.4 \\pm 134.8$$^c$ & $1.69\\times$$^*$ & \\xmark~(0/4) \\\\\n\\midrule\n\\multirow{3}{*}{Cheetah Run}\n & Baseline ($\\Delta t{=}1$) & $446.1 \\pm 2.9$$^d$ & --- & --- \\\\\n & Trigger (trained dt\\_emb) & $77.6 \\pm 36.6$$^e$ & $8.27\\times$ & \\cmark~(3/4) \\\\\n & Control (no dt\\_emb) & $100.6 \\pm 34.9$$^f$ & $0.20\\times$ & \\xmark~(0/4) \\\\\n\\midrule\n\\multirow{3}{*}{Cartpole Swingup}\n & Baseline ($\\Delta t{=}1$) & $673.3 \\pm 142.0$ & --- & --- \\\\\n & Trigger (trained dt\\_emb) & $236.3 \\pm 29.7$ & $0.06\\times$ & \\xmark~(0/3) \\\\\n & Control (no dt\\_emb) & $244.8 \\pm 12.7$ & ${\\leq}0.1\\times$ & \\xmark~(0/3) \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\n$^a$\\,$N{=}4$: exp\\_001 s1 (915.7), s2 (443.5), s3 (869.0), s4 (922.8); s3/s4 from cross-environment evaluation runs.\n$^b$\\,Eval: $N{=}5$ at 105K (009b, 008d\\_s3, 008d\\_s4, 059, 068). CIVO evaluated on $N{=}3$ seeds with full NVE pipeline (008d s0, 009e s1, 009b s2); 2/3 exceed $2.0\\times$.\n$^c$\\,$N{=}4$: 008f s0 (139.5), s1 (468.8), s4 (289.3), 009c s3 (311.9).\n$^d$\\,$N{=}2$: exp\\_077 s0 (448.1), exp\\_083 s1 (444.0); consistent with Table~\\ref{tab:complete_results}.\n$^e$\\,$N{=}3$: exp\\_010b s1 (51.7), exp\\_078 s0 (119.5), exp\\_097 s3 (61.7). exp\\_010b s0 (eval${=}0.8$, NVE${=}108.5\\times$) excluded as outlier.\n$^f$\\,$N{=}4$: exp\\_024b s0 (96.5), s1 (77.3), exp\\_092 s1 (77.3), exp\\_093 s2 (151.2). NVE Peak from $N{=}2$ seeds with computed NVE.\n$^*$\\,008f s0 NVE $1.69\\times$ reflects endpoint eval dip (95K: 342.9 $\\to$ 105K: 139.5), not value overestimation; classified non-CIVO.\\par}\n\\end{table}\n\nTable~\\ref{tab:cross_env_civo} establishes both the generality and the boundary of CIVO through a three-tier evidence structure. \\emph{Tier 1 (replication):} In multi-joint environments (Walker Walk, 6 joints; Cheetah Run, 6 joints), the trigger configuration reliably induces CIVO (NVE $4.72$--$8.27\\times$) while the no-embedding control does not (NVE $\\leq 1.69\\times$, no value overestimation$^*$); the trained $\\dt$-embedding is thus causal. Across the full primary evaluation set, trained $\\dt$-embedding triggers CIVO in 5/7 multi-joint locomotion seeds (71\\%) versus 0/16 frozen or removed controls (Fisher exact $p < 0.001$). \\emph{Tier 2 (negative control):} Single-joint Cartpole Swingup fails to trigger CIVO even with the identical trained $\\dt$-embedding configuration (0/3 seeds, peak NVE $0.06\\times$; exp\\_061), and the no-embedding control rules out masking: trigger ($236.3$) and control ($244.8$) achieve comparable performance ($-65\\%$ vs.\\ $-64\\%$ relative to baseline). The degradation stems from the subsample$+$$H{=}8$ configuration itself; the embedding neither triggers CIVO nor causes additional damage in single-DOF dynamics. \\emph{Tier 3 (frozen-embedding specificity):} Three ManiSkill manipulation tasks (Table~\\ref{tab:cross_domain}) show value-ratio transients at comparable magnitude ($4$--$11\\times$), but frozen controls exhibit equal or higher peaks, ruling out $\\dt$-embedding causation. Together, these tiers establish a scope boundary: CIVO is specific to multi-joint locomotion under imagination-based training with temporal conditioning, not a general pathology of $\\dt$-conditioned world models.\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 2.0\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eleven factorial experiments (including four 008e\\_v3 seeds and exp\\_059). Experiments are sorted by descending NVE. All four 008e\\_v3 seeds (mitigation configuration with $\\Delta t{=}1$ imagination) remain healthy with NVE $\\leq 0.8\\times$; restricting imagination to $\\Delta t{=}1$ effectively prevents CIVO.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. Trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 1343
    }
  }
}
```

</details>

---


### Assistant

_source line 219_

<details><summary>Logged reasoning block</summary>

```text
Now I have the complete results table! This is the authoritative source. Let me extract the eval values for each experiment.

From the complete results table (Tab:complete_results in appendix.tex):

Walker CIVO trigger (008d configs):
- 008d (s1): 82.8 @55K (but extended run 009e reached 131.08 @105K) 
- 009b (s2): 267.9 @105K
- 008d_s3 (s3): 268 @105K


- 008d_s4 (s4): 63.6 @105K
- 059 (s5): 95.8 @105K
- 068 (s1 repro): 39.1 @105K

Walker no dt_emb:
- 008f (s0): 139.5 @105K
- 008f s1: 468.8 @105K
- 008f s4: 289.3 @105K
- 009c s3: 311.9 @105K

Walker frozen dt_emb:
- 015

b (s1?): 204.2 @105K
- 022b (s0? + Gumbel gate): 300.7 @105K
- 042 (s0): 612.0 @105K
- 047 (s1): 144.2 @215K
- 057 (s2): 123.9 @215K
- 067 (s0): 281.5 @105K

Cheetah trigger:
- 010b (s1): 51.7 @105K
- 010b_s0 (s0): 0.83 @105K [excluded as outlier]
- 078 (s0): 119.5 @105K
- 097 s3: 61.7 @105K

Cheetah no dt_emb...

Looking at more configurations now: 024b across different states shows lower values around 77-96, while 092 and 093 are in the 77-151 range. For the frozen Cheetah variants, 046 and 058 are both in the 80-150 range at 215K. Now I'm examining the cross-environment evaluation data from the CIVO table, where Walker Trigger averages 146.9 with substantial variance across five runs, and Cheetah Trigger is coming in lower at around 77.6.

But there's a discrepancy emerging—the table indicates 10 untreated seeds total, yet I'm only accounting for 8 between the Walker and Cheetah trigger evaluations, with one Cheetah seed excluded as an outlier. I'm noticing the inconsistency—different tables are pulling from different subsets of the seed data. Looking at Table 2's definition, "Prevention = peak NVE < 2.0× (35K+)" with a 0% rate means none of the 10 seeds achieved that threshold, so all had NVE ≥ 2.0× at some point after 35K steps. But then I'm seeing Walker s2 with an NVE of 1, which contradicts this. both below 2.0×. So either Table 2 is using a different subset of seeds where all ten actually exceeded the 2.0× threshold, or there's something about how the prevention metric is being calculated that I'm missing. Let me look at the complete results to see which seeds actually had NVE values at or above 2.0× in the 35K+ window. I see now—the ground truth labels are based on the actual mechanism, not the NVE threshold itself. The 2.0× cutoff is just a diagnostic tool to measure prevention. So for Table 2, I'm counting how many seeds in each group stayed below that 2.0× threshold, regardless of their original CIVO status. Looking at the Walker untreated data, that gives me 2 out of 5 seeds prevented.

But the table shows 0/10 prevented for untreated, which doesn't match. I think the "Untreated" row might be specifically the seeds that exhibited CIVO in the first place—the ones where NVE≥2.0×—not all trigger seeds. That would explain why the denominator is 10 and the prevention rate is 0%. I'm realizing the discrepancy might come from how the prevention criterion is defined—maybe it requires NVE below 2.0× consistently across all timepoints, not just at any single point, which would exclude those Walker seeds. Alternatively, the table might be drawing from a broader experimental set than just the specific configs I'm analyzing, or using a different NVE calculation method altogether. I think the "10 seeds" in the untreated condition actually refers to all trigger configuration runs across environments, not just the ones with NVE evaluations. Looking at the cross-domain data, Walker has 6 trigger runs across different seeds and reproductions, while Cheetah has 4, which would account for the total count. The prevention metric is only calculated for runs where NVE data exists, which explains why the numbers don't align perfectly with the full set of 10 trigger experiments. Looking at the untreated CIVO trigger row in Table 2, all 10 seeds show 0/10 prevention—meaning none achieved NVE < 2.0×. But I'm seeing some conflicting NVE values in my data that suggest either the threshold definition changed or these particular seeds weren't included in the table's evaluation. The separation gap mentioned in the paper is [1.88×, 3.78×], so values like 1.53× and 1.62× fall below that threshold, which might explain the discrepancy. I need to stop overthinking the prevention criteria and just focus on adding the eval_return data to the table. The existing columns are locked in by the paper's constraints, so I'm only adding the new evaluation metric. Let me systematically pull the eval values from the complete results table, computing each seed's performance as a percentage of its environment's baseline—Walker at 915.7 and Cheetah at 446.1—then averaging within each group.

For the Untreated group, I'm working through the Walker and Cheetah seeds individually: the 008d s1 extended run shows 131.08 at 105K steps, but the main table lists 82.8 at 55K, and since the cross-environment analysis excludes this seed in favor of the other five (009b, 008d_s3, 008d_s4, 059, 068 with mean 146.9), I'll use those five for the eval calculation. The 010b_s0 is similarly excluded as an outlier from the cross-environment table. Now I'm calculating the percentage of baseline for each seed by dividing their evaluation scores by the respective robot's total baseline, then averaging across all seeds to get the mean performance relative to baseline.

Actually, I realize the cross_env table already has these statistics computed carefully, so I should follow that same approach but apply it to the Table 2 groupings instead. This manual calculation is taking too long—let me switch to a more practical strategy where I compute the eval percentage baseline mean and standard deviation from all available experiments for each Table 2 row, using the complete results table as my source of truth. For rows where the seed count doesn't perfectly match, I'll note the discrepancy but still calculate the stats, then update the LaTeX table accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "c414ab80-ddef-46ee-9060-299b1f0bb037",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATpcTz44v9JbvDruwejK4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7594,
      "cache_read_input_tokens": 136276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7594
      },
      "output_tokens": 18,
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

_source line 220_

Now I have the complete results table from the paper. Let me do the definitive computation using paper-authoritative eval values and baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "69c55f52-35f1-42ce-86e6-f864fb9655bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATpcTz44v9JbvDruwejK4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7594,
      "cache_read_input_tokens": 136276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7594
      },
      "output_tokens": 18,
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

_source line 221_

<details open><summary>🔧 Tool call — Bash · `toolu_01S6nmAsVeGddfGT6BqhSFfK`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\n\n# Baselines from the paper\nWALKER_BL = 915.7\nCHEETAH_BL = 446.1\n\ndef pct_bl(eval_val, env):\n    bl = WALKER_BL if env == \"walker\" else CHEETAH_BL\n    return eval_val / bl * 100\n\ndef stats(entries):\n    \"\"\"Compute mean±std of %baseline from list of (eval, env) tuples.\"\"\"\n    pcts = [pct_bl(e, env) for e, env in entries]\n    arr = np.array(pcts)\n    mean = arr.mean()\n    std = arr.std(ddof=1) if len(arr) > 1 else 0\n    return mean, std, len(arr), pcts\n\n# Table 2 groups with eval values from complete results table (appendix.tex)\n# and paper audit C8 section\n\ngroups = {}\n\n# 1. Untreated (10 seeds: 6 Walker + 4 Cheetah trigger)\n# Using values from complete results table\ngroups[\"Untreated\"] = [\n    (131.08, \"walker\"),   # 008d/009e s1 (extended to 105K, footnote ♥)\n    (267.9, \"walker\"),    # 009b s2\n    (268, \"walker\"),      # 008d_s3 s3\n    (63.6, \"walker\"),     # 008d_s4 s4\n    (95.8, \"walker\"),     # 059 s5\n    (39.1, \"walker\"),     # 068 s1 repro\n    (0.83, \"cheetah\"),    # 010b_s0\n    (51.7, \"cheetah\"),    # 010b s1\n    (119.5, \"cheetah\"),   # 078 s0\n    (61.7, \"cheetah\"),    # 097 s3\n]\n\n# 2. Reward-only SGS (2 seeds)\n# exp_016e: 31.7 (Walker), exp_044: 538.6 (Walker)\ngroups[\"Reward-only SGS\"] = [\n    (31.7, \"walker\"),     # 016e s1 - paradoxically worse\n    (538.6, \"walker\"),    # 044 - gradient stop\n]\n\n# 3. Full-pathway SGS (3 seeds)\n# exp_018v2 s1: 448.3 (Walker, from appendix: \\sgseval{} but audit says 448.3)\n# exp_018 s2: 40.8 (Walker)  \n# exp_021: 221.5 (Cheetah)\ngroups[\"Full-pathway SGS\"] = [\n    (448.3, \"walker\"),    # 018v2 s1\n    (40.8, \"walker\"),     # 018 s2\n    (221.5, \"cheetah\"),   # 021\n]\n\n# 4. Obs-decoder SGS (6 seeds: 4 Walker + 2 Cheetah)\n# Using MCP registry values (more reliable than audit for these)\ngroups[\"Obs-decoder SGS\"] = [\n    (726.41, \"walker\"),   # 025 s1\n    (89.6, \"walker\"),     # 025 s2 (from audit C8)\n    (590.17, \"walker\"),   # 025 s3 (final @215K)\n    (241.47, \"walker\"),   # 025 s4\n    (38.76, \"cheetah\"),   # 026 s0\n    (38.26, \"cheetah\"),   # 026 s1\n]\n\n# 5. RAVE (2 seeds)\n# exp_028 ceil=2.0: eval@105K=29 (from registry trajectory)\n# exp_028_ceil15: eval=76.2\ngroups[\"RAVE\"] = [\n    (29, \"walker\"),       # 028 s0 ceil=2.0\n    (76.2, \"walker\"),     # 028 s0 ceil=1.5\n]\n\n# 6. TCN σ=0.1 (1 seed)\ngroups[\"TCN 0.1\"] = [\n    (188.6, \"walker\"),    # 029c s0 (audit C8: eval_final=188.6)\n]\n\n# 7. TCN σ=0.2 (6† seeds: 4 Walker + 1 Cheetah + 1 PickCube)\n# Footnote says Walker 2/4; Cheetah 1/1, PickCube 0/1\ngroups[\"TCN 0.2\"] = [\n    (171.4, \"walker\"),    # 027_sigma02 s0 (audit)\n    (180.3, \"walker\"),    # 029a s1\n    (44.7, \"walker\"),     # 029b s2\n    (104.5, \"walker\"),    # 029d s3 (registry: eval_return_final)\n    (31.9, \"cheetah\"),    # 030a Cheetah s0\n    (11.6, \"walker\"),     # 031 PickCube s0 — use Walker baseline as proxy since PickCube baseline is different domain\n]\n\n# 8. TCN σ=0.5 (3 seeds)\n# Audit C8: Walker s0=166.4, Walker s1=94.6, Cheetah s0=143.6\ngroups[\"TCN 0.5\"] = [\n    (166.4, \"walker\"),    # 027 s0\n    (94.6, \"walker\"),     # 027 s1\n    (143.6, \"cheetah\"),   # 030b Cheetah s0\n]\n\n# 9. TCN σ=1.0 (1 seed)\ngroups[\"TCN 1.0\"] = [\n    (72.8, \"cheetah\"),    # 030c Cheetah s0\n]\n\n# 10. Wide single (2 seeds)\ngroups[\"Wide single\"] = [\n    (407.9, \"walker\"),    # 033 Walker s0 (from report)\n    (146.1, \"cheetah\"),   # 037 Cheetah s0\n]\n\n# 11. Narrow dual (min) (2 seeds)\ngroups[\"Narrow dual\"] = [\n    (697.8, \"walker\"),    # 035 s0\n    (592.7, \"walker\"),    # 039 s1\n]\n\n# 12. Wide dual (min) (4 seeds: 3 Walker + 1 Cheetah, footnote ||)\n# exp_032 s0=739.7, 032b s1=516, 041 s3=544, 034 Cheetah=97.5\ngroups[\"Wide dual\"] = [\n    (739.7, \"walker\"),    # 032 s0\n    (516, \"walker\"),      # 032b s1\n    (544, \"walker\"),      # 041 s3\n    (97.5, \"cheetah\"),    # 034 Cheetah s0\n]\n\n# 13. Embedding frozen (7 seeds: from footnote #)\n# Select 7 canonical runs (Walker + Cheetah, no Hopper)\n# Walker: 042 (s0)=612, 047 (s1)=144.2, 057 (s2)=123.9, 084 (s0)=334.1, 085 (s1)=281.5\n# Cheetah: 046 (s0)=150.5, 058 (s1)=80.46\n# But that's 7 total... some are same seeds\n# The footnote says \"7 seeds\" — likely 7 independent runs\n# Using the latest set from the audit C2 frozen table:\ngroups[\"Embedding frozen\"] = [\n    (612.0, \"walker\"),    # 042 s0\n    (281.5, \"walker\"),    # 067 s0 \n    (144.2, \"walker\"),    # 047 s1\n    (123.9, \"walker\"),    # 057 s2\n    (150.5, \"cheetah\"),   # 046 s0\n    (80.46, \"cheetah\"),   # 058 s1\n    (334.1, \"walker\"),    # 084 s0 (from audit)\n]\n\n# 14. Embedding removed (6 seeds: from footnote ¶)\n# Using NVE data seeds: Walker s0,s2,s3,s4 + Cheetah s0,s1\n# From complete results table:\ngroups[\"Embedding removed\"] = [\n    (139.5, \"walker\"),    # 008f s0 (corrected code)\n    (468.8, \"walker\"),    # 008f s1\n    (289.3, \"walker\"),    # 008f s4\n    (311.9, \"walker\"),    # 009c s3\n    (96.5, \"cheetah\"),    # 024b s0\n    (77.3, \"cheetah\"),    # 024b s1\n]\n\nprint(\"=\" * 90)\nprint(f\"{'Group':<25} {'N':>3} {'%BL mean':>10} {'%BL std':>10} {'LaTeX':>25}\")\nprint(\"=\" * 90)\n\nfor gname in [\"Untreated\", \"Reward-only SGS\", \"Full-pathway SGS\", \"Obs-decoder SGS\",\n              \"RAVE\", \"TCN 0.1\", \"TCN 0.2\", \"TCN 0.5\", \"TCN 1.0\",\n              \"Wide single\", \"Narrow dual\", \"Wide dual\", \n              \"Embedding frozen\", \"Embedding removed\"]:\n    entries = groups[gname]\n    mean, std, n, pcts = stats(entries)\n    \n    if n == 1:\n        latex = f\"{mean:.0f}\\\\%~(n{{=}}1)\"\n    elif n == 2:\n        latex = f\"{mean:.0f}$\\\\pm${std:.0f}\\\\%\"\n    else:\n        latex = f\"{mean:.0f}$\\\\pm${std:.0f}\\\\%\"\n    \n    pct_str = \", \".join([f\"{p:.0f}\" for p in pcts])\n    print(f\"{gname:<25} {n:>3} {mean:>9.1f}% {std:>9.1f}% {latex:>25}  [{pct_str}]\")\n\nPYEOF\n",
  "description": "Final eval_return %baseline computation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "693c03d0-853d-4635-9eee-b7eb46a02d23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATpcTz44v9JbvDruwejK4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7594,
      "cache_read_input_tokens": 136276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7594
      },
      "output_tokens": 18,
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

_source line 222 · 2026-05-29T00:48:19.230Z_

<details><summary>↩ Tool result · `toolu_01S6nmAsVeGddfGT6BqhSFfK`</summary>

```text
==========================================================================================
Group                       N   %BL mean    %BL std                     LaTeX
==========================================================================================
Untreated                  10      14.7%      10.4%               15$\pm$10\%  [14, 29, 29, 7, 10, 4, 0, 12, 27, 14]
Reward-only SGS             2      31.1%      39.1%               31$\pm$39\%  [3, 59]
Full-pathway SGS            3      34.4%      25.9%               34$\pm$26\%  [49, 4, 50]
Obs-decoder SGS             6      32.9%      31.3%               33$\pm$31\%  [79, 10, 64, 26, 9, 9]
RAVE                        2       5.7%       3.6%                 6$\pm$4\%  [3, 8]
TCN 0.1                     1      20.6%       0.0%              21\%~(n{=}1)  [21]
TCN 0.2                     6      10.5%       7.5%                11$\pm$7\%  [19, 20, 5, 11, 7, 1]
TCN 0.5                     3      20.2%      11.1%               20$\pm$11\%  [18, 10, 32]
TCN 1.0                     1      16.3%       0.0%              16\%~(n{=}1)  [16]
Wide single                 2      38.6%       8.3%                39$\pm$8\%  [45, 33]
Narrow dual                 2      70.5%       8.1%                70$\pm$8\%  [76, 65]
Wide dual                   4      54.6%      24.4%               55$\pm$24\%  [81, 56, 59, 22]
Embedding frozen            7      30.7%      18.4%               31$\pm$18\%  [67, 31, 16, 14, 34, 18, 36]
Embedding removed           6      28.5%      13.4%               29$\pm$13\%  [15, 51, 32, 34, 22, 17]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "8924db7d-5795-426e-add9-1653a6737b0d",
  "tool_use_result": {
    "stdout": "==========================================================================================\nGroup                       N   %BL mean    %BL std                     LaTeX\n==========================================================================================\nUntreated                  10      14.7%      10.4%               15$\\pm$10\\%  [14, 29, 29, 7, 10, 4, 0, 12, 27, 14]\nReward-only SGS             2      31.1%      39.1%               31$\\pm$39\\%  [3, 59]\nFull-pathway SGS            3      34.4%      25.9%               34$\\pm$26\\%  [49, 4, 50]\nObs-decoder SGS             6      32.9%      31.3%               33$\\pm$31\\%  [79, 10, 64, 26, 9, 9]\nRAVE                        2       5.7%       3.6%                 6$\\pm$4\\%  [3, 8]\nTCN 0.1                     1      20.6%       0.0%              21\\%~(n{=}1)  [21]\nTCN 0.2                     6      10.5%       7.5%                11$\\pm$7\\%  [19, 20, 5, 11, 7, 1]\nTCN 0.5                     3      20.2%      11.1%               20$\\pm$11\\%  [18, 10, 32]\nTCN 1.0                     1      16.3%       0.0%              16\\%~(n{=}1)  [16]\nWide single                 2      38.6%       8.3%                39$\\pm$8\\%  [45, 33]\nNarrow dual                 2      70.5%       8.1%                70$\\pm$8\\%  [76, 65]\nWide dual                   4      54.6%      24.4%               55$\\pm$24\\%  [81, 56, 59, 22]\nEmbedding frozen            7      30.7%      18.4%               31$\\pm$18\\%  [67, 31, 16, 14, 34, 18, 36]\nEmbedding removed           6      28.5%      13.4%               29$\\pm$13\\%  [15, 51, 32, 34, 22, 17]",
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

_source line 223_

<details><summary>Logged reasoning block</summary>

```text
Now I have the final statistics. Let me now edit the LaTeX table to add the eval column. 

The current table has columns: Level, Intervention, Seeds, Prev., Rate
I need to add: Eval (%BL) — showing mean±std as percentage of baseline

Let me check if the table fits in single column. The current table has 5 columns using `{llccc}`. Adding one more column would make it `{llcccc}`. Let me check the column widths — it's already using `\setlength{\tabcolsep}{3pt}` and `\footnotesize` to be compact.


I need to reconsider the eval column format — it should display mean±std as a percentage of baseline, with a note for single-seed entries. But I'm realizing there's an error in my calculations: the TCN σ=0.2 row with the PickCube seed shows 11.6, which I incorrectly computed against the Walker baseline instead of PickCube's own baseline of ~58.6, so that percentage needs to be recalculated.

Looking at the footnote, the TCN σ=0.2 entry does include PickCube data, so I need to recompute all the percentages using the correct baselines for each environment — Walker at 915.7, Cheetah at 446.1, and PickCube at 58.6. I need to verify the TCN σ=0.5 results—it has three seeds from Walker and Cheetah, but the PickCube experiment (exp_031b) is missing eval data, so I'm working with incomplete information there. Now let me recalculate the TCN σ=0.2 numbers to make sure I have the right baseline comparisons.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a1a97013-c54f-4113-992c-cb715019e30f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013m5DjeH8NX94Z59Az3jjni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8431,
      "cache_read_input_tokens": 143870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8431
      },
      "output_tokens": 29,
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

_source line 224_

<details open><summary>🔧 Tool call — Bash · `toolu_01PMPBRLeCnyBE9yDPRzctcS`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\n\nWALKER_BL = 915.7\nCHEETAH_BL = 446.1\nPICKCUBE_BL = 58.6\n\ndef pct_bl(eval_val, env):\n    if env == \"walker\": return eval_val / WALKER_BL * 100\n    elif env == \"cheetah\": return eval_val / CHEETAH_BL * 100\n    elif env == \"pickcube\": return eval_val / PICKCUBE_BL * 100\n    return eval_val / WALKER_BL * 100\n\ndef stats(entries):\n    pcts = [pct_bl(e, env) for e, env in entries]\n    arr = np.array(pcts)\n    mean = arr.mean()\n    std = arr.std(ddof=1) if len(arr) > 1 else 0\n    return mean, std, len(arr)\n\n# Corrected TCN σ=0.2 with PickCube baseline\ntcn02 = [\n    (171.4, \"walker\"), (180.3, \"walker\"), (44.7, \"walker\"), (104.5, \"walker\"),\n    (31.9, \"cheetah\"), (11.6, \"pickcube\")\n]\nm, s, n = stats(tcn02)\nprint(f\"TCN σ=0.2 (corrected): {m:.1f}±{s:.1f}% (n={n})\")\n\n# All groups final\ngroups = {\n    \"Untreated\": [(131.08,\"walker\"),(267.9,\"walker\"),(268,\"walker\"),(63.6,\"walker\"),(95.8,\"walker\"),(39.1,\"walker\"),(0.83,\"cheetah\"),(51.7,\"cheetah\"),(119.5,\"cheetah\"),(61.7,\"cheetah\")],\n    \"Reward-only SGS\": [(31.7,\"walker\"),(538.6,\"walker\")],\n    \"Full-pathway SGS\": [(448.3,\"walker\"),(40.8,\"walker\"),(221.5,\"cheetah\")],\n    \"Obs-decoder SGS\": [(726.41,\"walker\"),(89.6,\"walker\"),(590.17,\"walker\"),(241.47,\"walker\"),(38.76,\"cheetah\"),(38.26,\"cheetah\")],\n    \"RAVE\": [(29,\"walker\"),(76.2,\"walker\")],\n    \"TCN 0.1\": [(188.6,\"walker\")],\n    \"TCN 0.2\": tcn02,\n    \"TCN 0.5\": [(166.4,\"walker\"),(94.6,\"walker\"),(143.6,\"cheetah\")],\n    \"TCN 1.0\": [(72.8,\"cheetah\")],\n    \"Wide single\": [(407.9,\"walker\"),(146.1,\"cheetah\")],\n    \"Narrow dual\": [(697.8,\"walker\"),(592.7,\"walker\")],\n    \"Wide dual\": [(739.7,\"walker\"),(516,\"walker\"),(544,\"walker\"),(97.5,\"cheetah\")],\n    \"Embedding frozen\": [(612.0,\"walker\"),(281.5,\"walker\"),(144.2,\"walker\"),(123.9,\"walker\"),(150.5,\"cheetah\"),(80.46,\"cheetah\"),(334.1,\"walker\")],\n    \"Embedding removed\": [(139.5,\"walker\"),(468.8,\"walker\"),(289.3,\"walker\"),(311.9,\"walker\"),(96.5,\"cheetah\"),(77.3,\"cheetah\")],\n}\n\nprint(\"\\n\" + \"=\"*80)\nprint(\"FINAL TABLE DATA\")\nprint(\"=\"*80)\nfor gname, entries in groups.items():\n    m, s, n = stats(entries)\n    if n == 1:\n        latex = f\"{m:.0f}\\\\%\"\n    else:\n        latex = f\"{m:.0f}$\\\\pm${s:.0f}\\\\%\"\n    print(f\"{gname:<25}: {latex}\")\n\nPYEOF\n",
  "description": "Final corrected computation with PickCube baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "b0b8613b-5226-46f4-90e5-6c39b1685a97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013m5DjeH8NX94Z59Az3jjni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8431,
      "cache_read_input_tokens": 143870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8431
      },
      "output_tokens": 29,
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

_source line 225 · 2026-05-29T00:48:50.837Z_

<details><summary>↩ Tool result · `toolu_01PMPBRLeCnyBE9yDPRzctcS`</summary>

```text
TCN σ=0.2 (corrected): 13.6±6.7% (n=6)

================================================================================
FINAL TABLE DATA
================================================================================
Untreated                : 15$\pm$10\%
Reward-only SGS          : 31$\pm$39\%
Full-pathway SGS         : 34$\pm$26\%
Obs-decoder SGS          : 33$\pm$31\%
RAVE                     : 6$\pm$4\%
TCN 0.1                  : 21\%
TCN 0.2                  : 14$\pm$7\%
TCN 0.5                  : 20$\pm$11\%
TCN 1.0                  : 16\%
Wide single              : 39$\pm$8\%
Narrow dual              : 70$\pm$8\%
Wide dual                : 55$\pm$24\%
Embedding frozen         : 31$\pm$18\%
Embedding removed        : 29$\pm$13\%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "668ea9cf-3f0c-4df8-9191-e70e1433565a",
  "tool_use_result": {
    "stdout": "TCN σ=0.2 (corrected): 13.6±6.7% (n=6)\n\n================================================================================\nFINAL TABLE DATA\n================================================================================\nUntreated                : 15$\\pm$10\\%\nReward-only SGS          : 31$\\pm$39\\%\nFull-pathway SGS         : 34$\\pm$26\\%\nObs-decoder SGS          : 33$\\pm$31\\%\nRAVE                     : 6$\\pm$4\\%\nTCN 0.1                  : 21\\%\nTCN 0.2                  : 14$\\pm$7\\%\nTCN 0.5                  : 20$\\pm$11\\%\nTCN 1.0                  : 16\\%\nWide single              : 39$\\pm$8\\%\nNarrow dual              : 70$\\pm$8\\%\nWide dual                : 55$\\pm$24\\%\nEmbedding frozen         : 31$\\pm$18\\%\nEmbedding removed        : 29$\\pm$13\\%",
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

_source line 226_

<details><summary>Logged reasoning block</summary>

````text
Now I have the final numbers. Let me now edit the LaTeX table. I need to:

1. Add a new column "Eval (\%BL)" 
2. Keep existing numbers unchanged (D171)
3. Check if the table fits in single column

The current table format:
```
\begin{tabular}{llccc}
\toprule
\textbf{Level} & \textbf{Intervention} & \textbf{Seeds} & \textbf{Prev.} & \textbf{Rate} \\
```

I'll add a column after Rate:


Updating the table structure...

I need to verify this fits within the column width. The new column with compact entries like "15±10%" should work fine given that the first two columns take up most of the space. For the n=1 cases with TCN σ=0.1, I'll need to check the spacing carefully.

Looking at the RAVE row, I see it uses different ceiling values rather than random seeds, so the 2-seed evaluation of 6±4% is appropriate. I'll keep the formatting consistent: showing mean±std% for n>1 cases and just the value% for n=1, letting the Seeds column clarify the sample size for readers.

The Reward-only SGS result has a notably large standard deviation of 39% because the two variants performed very differently—one failed almost entirely while the other showed partial success. That high variability is actually meaningful information about the method's inconsistency, so I should preserve it in the table.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "0becb410-b002-4c05-9d25-89d82e53431f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185chqcBr2MmtLMiHLQA5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2339,
      "cache_read_input_tokens": 152301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2339
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


### Assistant

_source line 227_

Now let me edit the table. First, let me re-read the exact section to make a precise edit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d252f84d-50cb-4c2a-9870-ad305cde3659",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185chqcBr2MmtLMiHLQA5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2339,
      "cache_read_input_tokens": 152301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2339
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


### Tool call

_source line 228_

<details open><summary>🔧 Tool call — Read · `toolu_01QUzeFUkGct74HuPjkLCsrf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
  "offset": 158,
  "limit": 42
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "30c98121-14fb-4773-aacf-ea3db65e32d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185chqcBr2MmtLMiHLQA5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2339,
      "cache_read_input_tokens": 152301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2339
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

_source line 229 · 2026-05-29T00:49:06.865Z_

<details><summary>↩ Tool result · `toolu_01QUzeFUkGct74HuPjkLCsrf`</summary>

```text
158	\label{sec:forward_results}
159	
160	\begin{table}[t]
161	\centering
162	\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\times$ (35K+). No level reliably eliminates CIVO across environments.
163	$^\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.
164	$^\ddagger$Borderline (NVE${=}1.02\times$, eval 55\%).
165	$^\S$Policy erosion (final 15\% baseline).
166	$^\|$Walker 3/3, Cheetah 0/1.
167	$^\#$7 seeds, all NVE $< 2.0\times$.
168	$^\P$6 seeds, all NVE $< 2.0\times$.}
169	\label{tab:intervention_hierarchy}
170	\footnotesize
171	\setlength{\tabcolsep}{3pt}
172	\begin{tabular}{llccc}
173	\toprule
174	\textbf{Level} & \textbf{Intervention} & \textbf{Seeds} & \textbf{Prev.} & \textbf{Rate} \\
175	\midrule
176	--- & Untreated & 10 & 0/10 & 0\% \\
177	\midrule
178	Gradient & Reward-only SGS & 2 & 0/2 & 0\% \\
179	Gradient & Full-pathway SGS & 3 & 0/3 & 0\% \\
180	Gradient & Obs-decoder SGS & 6 & 1/6 & 17\% \\
181	\midrule
182	Output & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\% \\
183	\midrule
184	Repr. & TCN ($\sigma{=}0.1$) & 1 & 1/1$^\ddagger$ & 100\% \\
185	Repr. & TCN ($\sigma{=}0.2$) & 6$^\dagger$ & 3/6 & 50\% \\
186	Repr. & TCN ($\sigma{=}0.5$) & 3 & 1/3 & 33\% \\
187	Repr. & TCN ($\sigma{=}1.0$) & 1 & 1/1$^\S$ & 100\% \\
188	\midrule
189	Arch. & Wide single & 2 & 0/2 & 0\% \\
190	Arch. & Narrow dual (min) & 2 & 0/2 & 0\% \\
191	Arch. & Wide dual (min) & 4 & 3/4$^\|$ & 75\% \\
192	\midrule
193	--- & Embedding frozen & 7 & 7/7$^\#$ & 100\% \\
194	--- & Embedding removed & 6 & 6/6$^\P$ & 100\% \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails because the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) shows binary behavior---suppressing CIVO in 2/4 Walker seeds ($\sigma{=}0.2$) while remaining seeds escalate---and cross-environment transfer fails ($\sigma{=}1.0$ erodes Cheetah policy to 15\% of baseline; Appendix~\ref{sec:tcn_cross_env}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "24c55c19-b88c-4627-996d-0f76813c91a4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
      "content": "\\label{sec:forward_results}\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails because the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) shows binary behavior---suppressing CIVO in 2/4 Walker seeds ($\\sigma{=}0.2$) while remaining seeds escalate---and cross-environment transfer fails ($\\sigma{=}1.0$ erodes Cheetah policy to 15\\% of baseline; Appendix~\\ref{sec:tcn_cross_env}).",
      "numLines": 42,
      "startLine": 158,
      "totalLines": 214
    }
  }
}
```

</details>

---


### Assistant

_source line 230_

Now I'll edit the table to add the Eval (%BL) column.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "fd8623f6-7bb6-497f-a8eb-16827df633ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d5eU7WPaYMKa9oHZSNgst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1858,
      "cache_read_input_tokens": 154640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1858
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

_source line 231_

<details open><summary>🔧 Tool call — Edit · `toolu_019jabjC4CV4i4gbgU7M8N3K`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
  "old_string": "\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% \\\\\n\\bottomrule\n\\end{tabular}",
  "new_string": "\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} & \\textbf{Eval (\\%BL)} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% & $15{\\pm}10$ \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% & $31{\\pm}39$ \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% & $34{\\pm}26$ \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% & $33{\\pm}31$ \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% & $6{\\pm}4$ \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% & 21 \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% & $14{\\pm}7$ \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% & $20{\\pm}11$ \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% & 16 \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% & $39{\\pm}8$ \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% & $70{\\pm}8$ \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% & $55{\\pm}24$ \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% & $31{\\pm}18$ \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% & $29{\\pm}13$ \\\\\n\\bottomrule\n\\end{tabular}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "e0590154-7099-4f9d-aeaf-39fa33f085f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d5eU7WPaYMKa9oHZSNgst",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1858,
      "cache_read_input_tokens": 154640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1858
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

_source line 232 · 2026-05-29T00:49:20.681Z_

<details><summary>↩ Tool result · `toolu_019jabjC4CV4i4gbgU7M8N3K`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "52360176-c6b5-4e72-bb5d-1bac10af1ec0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
    "oldString": "\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% \\\\\n\\bottomrule\n\\end{tabular}",
    "newString": "\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} & \\textbf{Eval (\\%BL)} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% & $15{\\pm}10$ \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% & $31{\\pm}39$ \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% & $34{\\pm}26$ \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% & $33{\\pm}31$ \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% & $6{\\pm}4$ \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% & 21 \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% & $14{\\pm}7$ \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% & $20{\\pm}11$ \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% & 16 \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% & $39{\\pm}8$ \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% & $70{\\pm}8$ \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% & $55{\\pm}24$ \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% & $31{\\pm}18$ \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% & $29{\\pm}13$ \\\\\n\\bottomrule\n\\end{tabular}",
    "originalFile": "\\section{Experiments and Results}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:methodology}\n\n\\paragraph{Base architecture.}\nAll experiments build on DreamerV3 \\citep{hafner2023dreamerv3}, which learns an RSSM with discrete latent states ($32$ categories $\\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely in imagined trajectories. The default configuration imagines $H{=}15$ steps at $\\dt{=}1$ (one imagination step per environment transition).\n\n\\paragraph{Variable-rate imagination.}\n\\label{sec:variable_rate}\nWe introduce three orthogonal modifications enabling variable-rate imagination, each independently toggled.\n\\emph{Temporal embedding}: A learned embedding $e(\\dt)$ is concatenated to the RSSM input at each imagination step. We test three modes: \\textbf{trained} (updated via backpropagation, enabling co-adaptation), \\textbf{frozen} (fixed random projection, \\texttt{requires\\_grad=False}), and \\textbf{removed} (dimension zero). We further distinguish \\textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\\dt{>}1$ transitions) from \\textbf{trained-but-unexposed} (subsample OFF: $\\dt{>}1$ used only during imagination).\n\\emph{Temporal subsampling}: When enabled, the replay buffer augments training data with variable-$\\dt$ transitions by subsampling consecutive frames (max factor~2).\n\\emph{Horizon and step size}: We test $H{=}15$ (default) and $H{=}8$; \\texttt{gate\\_fixed\\_dt} forces a specific $\\dt$ ($1$, $2$, or $4$).\n\n\\paragraph{Factorial design.}\n\\label{sec:factorial}\nWe adopt a factorial ablation across four factors: $\\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and step size ($\\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\\ref{tab:factorial_design} in Appendix~\\ref{sec:appendix_factorial}) isolates trained $\\dt$-embedding and multi-rate exposure as orthogonal factors. Key configurations use 4--5 seeds; following \\citet{agarwal2021precipice}, we report per-seed trajectories.\n\n\\paragraph{Diagnostic metric.}\n\\label{sec:metrics}\nWe define the normalized value-to-eval ratio $\\nve_t = (v/e)_{\\text{config},t} / (v/e)_{\\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\\_001, seed~1, 505K steps). Analysis is restricted to a \\textbf{35K+ window} to avoid early-training inflation. The $\\nve \\geq 2.0\\times$ threshold classifies all $n{=}36$ configurations across two environments (AUROC${=}1.000$ [95\\% bootstrap CI: 1.000--1.000], F1${=}1.000$; Appendix~\\ref{sec:appendix_sensitivity}). CIVO labels are defined by mechanism (trained $\\dt$-embedding $+$ multi-rate exposure), independent of the threshold; the separation gap $[1.88\\times, 3.78\\times]$ contains no configurations, making classification insensitive to threshold choice within this interval.\n\n\\paragraph{Intervention methods.}\n\\label{sec:sgs_method}\n\\emph{Selective gradient stopping} (SGS): $e_{\\Delta t}$ is detached via $\\operatorname{sg}(\\cdot)$ before selected prediction heads during the backward pass. We test reward-only (exp\\_016e), full-pathway (exp\\_018), and obs-decoder-only (exp\\_025/026) variants. \\emph{TCN} adds Gaussian noise $\\mathcal{N}(0, \\sigma^2)$ to $e_{\\Delta t}$ during imagination ($\\sigma \\in \\{0.2, 0.5\\}$, three environments); \\emph{RAVE} clips imagined values exceeding an EMA anchor ($c \\in \\{2.0, 1.5\\}$). \\emph{Dual-critic}: a $2{\\times}2$ factorial of \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} critic following TD3 \\citep{fujimoto2018td3}.\n\\label{sec:forward_pass_method}\n\\label{sec:dual_critic_method}\n\n\\paragraph{Environments and training.}\n\\label{sec:env_details}\nAll experiments use Walker Walk and Cheetah Run from DMC \\citep{tassa2018dmcontrol} with proprioceptive observations. Walker Walk (6-joint biped) is the primary environment; Cheetah Run (6-joint runner) serves as a severity probe (CIVO at $8$--$70\\times$ NVE vs.\\ $2$--$5\\times$ on Walker). Baselines run 500K steps; treatments 105K steps. Hyperparameters follow DreamerV3 defaults \\citep{hafner2023dreamerv3} ($d{=}32$ embedding; Appendix~\\ref{sec:hyperparameters}). Training uses a single NVIDIA RTX PRO 6000 GPU (${\\sim}80$ GPU-hours total). The codebase extends the official DreamerV3 implementation \\citep{hafner2023dreamerv3} with the variable-rate modules described above.\n\n%% ============================================================\n%% RESULTS\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:results}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{Key configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\\ref{tab:complete_results}.}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s0) & --- & ON & 8 & 139.5 @105K$^f$ & 1.69$\\times$$^f$ & Healthy$^f$ \\\\\n008f s1 & No dt\\_emb (s1) & --- & ON & 8 & 468.8 @105K & 0.88$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run (s1) & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n078 & Cheetah Run (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\\times$ & Self-correcting \\\\\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^d$ & Env.\\ transient \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^e$ & Env.\\ dynamics$^e$ \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\n$^c$~Environment-specific baseline.\n$^d$~Frozen control matches; environment-specific.\n$^e$~Seed-dependent (Table~\\ref{tab:cross_domain}).\n$^f$~Corrected-code rerun (Appendix~\\ref{sec:code_corrections}).\nBaselines: Walker 915.7; Cheetah 446.1.\nFull footnotes in Table~\\ref{tab:complete_results}.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the strongest predictor. The \\emph{primary} comparison---008d (trained, subsample ON) vs.\\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\\nve = 4.12\\times$ (eval 82.8) vs.\\ $\\nve \\leq 1.69\\times$ (eval 139.5--468.8$^f$). \\emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\\nve \\geq 2.0\\times$ threshold (35K+ window) classifies all $n{=}36$ configurations across two environments (9 CIVO-positive, 27 non-CIVO; AUROC${=}1.000$, F1${=}1.000$; Table~\\ref{tab:nve_loeo}; Figure~\\ref{fig:nve_trajectory}).\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{(a) NVE trajectories: trained $\\dt$-embedding seeds exceed the $2.0\\times$ threshold; controls remain near $1.0\\times$. (b) Actor loss sign-flip coincides with CIVO onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO onset (NVE $\\geq 2.0\\times$) in 3 of 5 Walker Walk seeds, degrading all five to below 30\\% of baseline (IQM $148.8$, $n{=}5$; \\citet{agarwal2021precipice}). Including Cheetah Run (\\S\\ref{sec:f6}), CIVO onset occurs in 5/7 multi-joint locomotion runs; 3 sustain collapse, one self-corrects, one shows NVE self-correction without policy recovery (Appendix~\\ref{sec:seed_divergence}).\n\n\\paragraph{Mechanism evidence.}\nThe RSSM reward head develops a $1.63\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$ on Walker (Table~\\ref{tab:rssm_fidelity}), but Cheetah shows no reward gap ($1.00\\times$) despite higher CIVO severity ($8.27\\times$); reward fidelity degradation is one transmission pathway but not necessary. The critic internalizes the bias: mean $V(s)/\\text{MC-return}$ reaches $7.80\\times$ (100\\% overestimated) vs.\\ $1.05\\times$ for the control. Evaluation return collapses ${\\sim}35$K steps before actor entropy rises (Appendix~\\ref{sec:civo_mechanism}).\n\n\\paragraph{Temporal ordering ($n{=}2$; correlational).}\nDense checkpoint analysis (12 points, 10K--65K) shows reward fidelity degradation precedes value overestimation: fidelity crosses $1.1\\times$ at 20K while value-to-eval rises at ${\\sim}$30K ($r{=}0.81$, $p{=}0.002$; Figure~\\ref{fig:temporal_ordering}). A second seed confirms the pattern (lead ${\\approx}$9K; Appendix~\\ref{sec:timeseries_fidelity}). This temporal precedence is consistent with but does not establish causal direction.\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Causal Ablation and Cross-Environment Validation}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding triggers CIVO in 5/7 multi-joint locomotion seeds vs.\\ 0/16 frozen or removed controls ($p < 0.001$; Table~\\ref{tab:three_way_emb}); a random-policy decomposition attributes ${\\approx}36\\%$ of the effect to dynamics bias and ${\\approx}64\\%$ to actor exploitation (Appendix~\\ref{sec:civo_mechanism}). Cross-environment validation on three ManiSkill tasks shows comparable value-ratio transients ($4$--$11\\times$) with frozen controls matching, ruling out $\\dt$-embedding causation (Table~\\ref{tab:cross_domain}); CIVO is specific to multi-joint locomotion. Full factorial analysis in Appendix~\\ref{sec:appendix_factorial}.\n\n%% ============================================================\n%% F6--F7: Interventions\n%% ============================================================\n\n\\subsection{F6--F7: Interventions}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination eliminates CIVO.}\nRestricting imagination to $\\dt{=}1$ while retaining the trained embedding (exp\\_008e\\_v3; Appendix~\\ref{sec:code_corrections}) yields 0/4 CIVO (peak NVE ${\\leq}0.8\\times$); three seeds achieve $64$--$94\\%$ of baseline (mean $775.6$; Figure~\\ref{fig:multiple_pathways}). Multi-step imagination---not the trained embedding alone---is necessary for CIVO.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting dynamics ($2{\\times}3$ grid). \\textbf{Top row:} 008d (CIVO)---eval collapse, value explosion, entropy decrease. \\textbf{Bottom row:} 008e\\_v3 s1 ($\\dt{=}1$ imagination)---no CIVO (NVE ${\\leq}\\,0.6\\times$, eval $94\\%$ baseline).}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nFull-SGS (exp\\_018) detaches all non-KL gradients from $e_{\\dt}$. Seed~1 shows partial mitigation (eval 448.3, NVE $1.66\\times$; anecdotal, $n{=}1$); seed~2 collapses (neither seed achieves elimination; Appendix~\\ref{sec:sgs_gradient_analysis}). Cross-environment validation on Cheetah confirms CIVO generalization (010b, NVE $8.27$--$108.52\\times$); full-SGS yields 0/3 elimination. Removing the embedding eliminates CIVO on Cheetah (024b, NVE $< 0.2\\times$). Targeted obs-decoder-only SGS (exp\\_025/026) achieves 1/6 prevention (1/4 Walker, 0/2 Cheetah; Table~\\ref{tab:intervention_hierarchy}), confirming pathway redundancy: blocking any single channel shifts co-adaptation to the remaining ones (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% Forward-pass interventions\n%% ============================================================\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_results}\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails because the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) shows binary behavior---suppressing CIVO in 2/4 Walker seeds ($\\sigma{=}0.2$) while remaining seeds escalate---and cross-environment transfer fails ($\\sigma{=}1.0$ erodes Cheetah policy to 15\\% of baseline; Appendix~\\ref{sec:tcn_cross_env}).\n\n%% ============================================================\n%% Architecture-Level Ablation\n%% ============================================================\n\n\\subsection{Architecture-Level Ablation}\n\\label{sec:arch_results}\n\n\\paragraph{Critic convergence in pure imagination.}\nAcross all dual-critic configurations ($n{=}7$), critics converge ($\\rho > 0.999$) with pessimism at 3--4\\% of the independent-critic bound, rendering standard pessimistic estimation ineffective.\n\n\\paragraph{Wide dual-critic: the sole partial success.}\nA $2{\\times}2$ factorial separates two mechanisms: narrow dual-critic (min, ${\\sim}1.2$M) recovers from CIVO (${\\sim}16$--$19\\times$ ratio reduction) but does not prevent onset; wide dual-critic (min $+$ ${\\sim}2.4$M) achieves NVE $\\leq 1.4\\times$ in 3/4 seeds (3/3 Walker, 0/1 Cheetah)---the strongest result across all levels (Table~\\ref{tab:intervention_hierarchy}). Wide single (0/2) confirms both components are necessary. Cross-environment transfer is limited (Appendix~\\ref{sec:dual_critic_appendix}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 169,
        "oldLines": 29,
        "newStart": 169,
        "newLines": 29,
        "lines": [
          " \\label{tab:intervention_hierarchy}",
          " \\footnotesize",
          " \\setlength{\\tabcolsep}{3pt}",
          "-\\begin{tabular}{llccc}",
          "+\\begin{tabular}{llcccc}",
          " \\toprule",
          "-\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} \\\\",
          "+\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} & \\textbf{Eval (\\%BL)} \\\\",
          " \\midrule",
          "---- & Untreated & 10 & 0/10 & 0\\% \\\\",
          "+--- & Untreated & 10 & 0/10 & 0\\% & $15{\\pm}10$ \\\\",
          " \\midrule",
          "-Gradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\",
          "-Gradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\",
          "-Gradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\",
          "+Gradient & Reward-only SGS & 2 & 0/2 & 0\\% & $31{\\pm}39$ \\\\",
          "+Gradient & Full-pathway SGS & 3 & 0/3 & 0\\% & $34{\\pm}26$ \\\\",
          "+Gradient & Obs-decoder SGS & 6 & 1/6 & 17\\% & $33{\\pm}31$ \\\\",
          " \\midrule",
          "-Output & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\",
          "+Output & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% & $6{\\pm}4$ \\\\",
          " \\midrule",
          "-Repr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\",
          "-Repr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% \\\\",
          "-Repr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% \\\\",
          "-Repr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\",
          "+Repr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% & 21 \\\\",
          "+Repr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% & $14{\\pm}7$ \\\\",
          "+Repr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% & $20{\\pm}11$ \\\\",
          "+Repr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% & 16 \\\\",
          " \\midrule",
          "-Arch. & Wide single & 2 & 0/2 & 0\\% \\\\",
          "-Arch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\",
          "-Arch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\",
          "+Arch. & Wide single & 2 & 0/2 & 0\\% & $39{\\pm}8$ \\\\",
          "+Arch. & Narrow dual (min) & 2 & 0/2 & 0\\% & $70{\\pm}8$ \\\\",
          "+Arch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% & $55{\\pm}24$ \\\\",
          " \\midrule",
          "---- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% \\\\",
          "---- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% \\\\",
          "+--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% & $31{\\pm}18$ \\\\",
          "+--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% & $29{\\pm}13$ \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
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

_source line 233_

Now update the caption to document the new column.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a90c842a-c8df-4ff7-a30a-6daa3bb2c3bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ny8vdJWGDV97LUpG6JfUTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 156498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1404
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

_source line 234_

<details open><summary>🔧 Tool call — Edit · `toolu_016r4rwKojnBAdZ8DNoUTfge`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
  "old_string": "\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}",
  "new_string": "\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). Eval (\\%BL) = mean${\\pm}$std of final eval return as percentage of per-environment baseline (Walker 915.7, Cheetah 446.1). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "097b21be-1ef0-4a39-9378-401e57c80f64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ny8vdJWGDV97LUpG6JfUTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 156498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1404
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

_source line 235 · 2026-05-29T00:49:28.499Z_

<details><summary>↩ Tool result · `toolu_016r4rwKojnBAdZ8DNoUTfge`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "6c4b022c-35e7-4ea1-93ac-a395978ca8c0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
    "oldString": "\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}",
    "newString": "\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). Eval (\\%BL) = mean${\\pm}$std of final eval return as percentage of per-environment baseline (Walker 915.7, Cheetah 446.1). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}",
    "originalFile": "\\section{Experiments and Results}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:methodology}\n\n\\paragraph{Base architecture.}\nAll experiments build on DreamerV3 \\citep{hafner2023dreamerv3}, which learns an RSSM with discrete latent states ($32$ categories $\\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely in imagined trajectories. The default configuration imagines $H{=}15$ steps at $\\dt{=}1$ (one imagination step per environment transition).\n\n\\paragraph{Variable-rate imagination.}\n\\label{sec:variable_rate}\nWe introduce three orthogonal modifications enabling variable-rate imagination, each independently toggled.\n\\emph{Temporal embedding}: A learned embedding $e(\\dt)$ is concatenated to the RSSM input at each imagination step. We test three modes: \\textbf{trained} (updated via backpropagation, enabling co-adaptation), \\textbf{frozen} (fixed random projection, \\texttt{requires\\_grad=False}), and \\textbf{removed} (dimension zero). We further distinguish \\textbf{trained-and-exposed} (subsample ON: the RSSM trains on $\\dt{>}1$ transitions) from \\textbf{trained-but-unexposed} (subsample OFF: $\\dt{>}1$ used only during imagination).\n\\emph{Temporal subsampling}: When enabled, the replay buffer augments training data with variable-$\\dt$ transitions by subsampling consecutive frames (max factor~2).\n\\emph{Horizon and step size}: We test $H{=}15$ (default) and $H{=}8$; \\texttt{gate\\_fixed\\_dt} forces a specific $\\dt$ ($1$, $2$, or $4$).\n\n\\paragraph{Factorial design.}\n\\label{sec:factorial}\nWe adopt a factorial ablation across four factors: $\\dt$-embedding mode (trained / frozen / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and step size ($\\dt{=}1$, $2$, $4$). The design (12 conditions, Table~\\ref{tab:factorial_design} in Appendix~\\ref{sec:appendix_factorial}) isolates trained $\\dt$-embedding and multi-rate exposure as orthogonal factors. Key configurations use 4--5 seeds; following \\citet{agarwal2021precipice}, we report per-seed trajectories.\n\n\\paragraph{Diagnostic metric.}\n\\label{sec:metrics}\nWe define the normalized value-to-eval ratio $\\nve_t = (v/e)_{\\text{config},t} / (v/e)_{\\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\\_001, seed~1, 505K steps). Analysis is restricted to a \\textbf{35K+ window} to avoid early-training inflation. The $\\nve \\geq 2.0\\times$ threshold classifies all $n{=}36$ configurations across two environments (AUROC${=}1.000$ [95\\% bootstrap CI: 1.000--1.000], F1${=}1.000$; Appendix~\\ref{sec:appendix_sensitivity}). CIVO labels are defined by mechanism (trained $\\dt$-embedding $+$ multi-rate exposure), independent of the threshold; the separation gap $[1.88\\times, 3.78\\times]$ contains no configurations, making classification insensitive to threshold choice within this interval.\n\n\\paragraph{Intervention methods.}\n\\label{sec:sgs_method}\n\\emph{Selective gradient stopping} (SGS): $e_{\\Delta t}$ is detached via $\\operatorname{sg}(\\cdot)$ before selected prediction heads during the backward pass. We test reward-only (exp\\_016e), full-pathway (exp\\_018), and obs-decoder-only (exp\\_025/026) variants. \\emph{TCN} adds Gaussian noise $\\mathcal{N}(0, \\sigma^2)$ to $e_{\\Delta t}$ during imagination ($\\sigma \\in \\{0.2, 0.5\\}$, three environments); \\emph{RAVE} clips imagined values exceeding an EMA anchor ($c \\in \\{2.0, 1.5\\}$). \\emph{Dual-critic}: a $2{\\times}2$ factorial of \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} critic following TD3 \\citep{fujimoto2018td3}.\n\\label{sec:forward_pass_method}\n\\label{sec:dual_critic_method}\n\n\\paragraph{Environments and training.}\n\\label{sec:env_details}\nAll experiments use Walker Walk and Cheetah Run from DMC \\citep{tassa2018dmcontrol} with proprioceptive observations. Walker Walk (6-joint biped) is the primary environment; Cheetah Run (6-joint runner) serves as a severity probe (CIVO at $8$--$70\\times$ NVE vs.\\ $2$--$5\\times$ on Walker). Baselines run 500K steps; treatments 105K steps. Hyperparameters follow DreamerV3 defaults \\citep{hafner2023dreamerv3} ($d{=}32$ embedding; Appendix~\\ref{sec:hyperparameters}). Training uses a single NVIDIA RTX PRO 6000 GPU (${\\sim}80$ GPU-hours total). The codebase extends the official DreamerV3 implementation \\citep{hafner2023dreamerv3} with the variable-rate modules described above.\n\n%% ============================================================\n%% RESULTS\n%% ============================================================\n\n\\subsection{F1: All Variable-Rate Configurations Degrade}\n\\label{sec:results}\n\\label{sec:f1}\n\nEvery configuration that introduces $\\dt > 1$ imagination degrades relative to the $\\dt{=}1$ baseline (Figure~\\ref{fig:learning_curves}). The baseline reaches 915.7 at 105K; fixed $\\dt{=}2$ (006) peaks at 485.3 before collapsing to 132.9 ($14\\%$ of baseline); fixed $\\dt{=}4$ (007) never exceeds 176.9 ($19\\%$); the learned gate (005) collapses to 98.8 ($11\\%$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\columnwidth]{figures/paper/fig1_learning_curves.pdf}\n\\caption{Learning curves. The baseline (black) reaches 915.7; all variable-rate configurations degrade.}\n\\label{fig:learning_curves}\n\\end{figure}\n\n%% ============================================================\n%% TABLE 1: Main results summary\n%% ============================================================\n\n\\begin{table*}[t]\n\\centering\n\\caption{Key configurations and outcomes. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded. Complete results for all 43 configurations in Table~\\ref{tab:complete_results}.}\n\\label{tab:main_results}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s0) & --- & ON & 8 & 139.5 @105K$^f$ & 1.69$\\times$$^f$ & Healthy$^f$ \\\\\n008f s1 & No dt\\_emb (s1) & --- & ON & 8 & 468.8 @105K & 0.88$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run (s1) & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n078 & Cheetah Run (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\\times$ & Self-correcting \\\\\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^d$ & Env.\\ transient \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^e$ & Env.\\ dynamics$^e$ \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\n$^c$~Environment-specific baseline.\n$^d$~Frozen control matches; environment-specific.\n$^e$~Seed-dependent (Table~\\ref{tab:cross_domain}).\n$^f$~Corrected-code rerun (Appendix~\\ref{sec:code_corrections}).\nBaselines: Walker 915.7; Cheetah 446.1.\nFull footnotes in Table~\\ref{tab:complete_results}.\\par}\n\\end{table*}\n\n%% ============================================================\n%% F2: Trained dt_embedding → nve > 1.5x\n%% ============================================================\n\n\\subsection{F2: Trained Temporal Embedding Precedes Value Overestimation}\n\\label{sec:f2}\n\nThe factorial design isolates trained $\\dt$-embedding as the strongest predictor. The \\emph{primary} comparison---008d (trained, subsample ON) vs.\\ 008f (no embedding, subsample ON)---differs only in embedding training, yielding $\\nve = 4.12\\times$ (eval 82.8) vs.\\ $\\nve \\leq 1.69\\times$ (eval 139.5--468.8$^f$). \\emph{Secondary} comparisons against 008a/008c (unexposed embedding) co-vary subsample status and horizon alongside the embedding factor. The $\\nve \\geq 2.0\\times$ threshold (35K+ window) classifies all $n{=}36$ configurations across two environments (9 CIVO-positive, 27 non-CIVO; AUROC${=}1.000$, F1${=}1.000$; Table~\\ref{tab:nve_loeo}; Figure~\\ref{fig:nve_trajectory}).\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_nve_trajectory.pdf}\n\\caption{(a) NVE trajectories: trained $\\dt$-embedding seeds exceed the $2.0\\times$ threshold; controls remain near $1.0\\times$. (b) Actor loss sign-flip coincides with CIVO onset.}\n\\label{fig:nve_trajectory}\n\\end{figure}\n\nThe trained $\\dt$-embedding triggers CIVO onset (NVE $\\geq 2.0\\times$) in 3 of 5 Walker Walk seeds, degrading all five to below 30\\% of baseline (IQM $148.8$, $n{=}5$; \\citet{agarwal2021precipice}). Including Cheetah Run (\\S\\ref{sec:f6}), CIVO onset occurs in 5/7 multi-joint locomotion runs; 3 sustain collapse, one self-corrects, one shows NVE self-correction without policy recovery (Appendix~\\ref{sec:seed_divergence}).\n\n\\paragraph{Mechanism evidence.}\nThe RSSM reward head develops a $1.63\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$ on Walker (Table~\\ref{tab:rssm_fidelity}), but Cheetah shows no reward gap ($1.00\\times$) despite higher CIVO severity ($8.27\\times$); reward fidelity degradation is one transmission pathway but not necessary. The critic internalizes the bias: mean $V(s)/\\text{MC-return}$ reaches $7.80\\times$ (100\\% overestimated) vs.\\ $1.05\\times$ for the control. Evaluation return collapses ${\\sim}35$K steps before actor entropy rises (Appendix~\\ref{sec:civo_mechanism}).\n\n\\paragraph{Temporal ordering ($n{=}2$; correlational).}\nDense checkpoint analysis (12 points, 10K--65K) shows reward fidelity degradation precedes value overestimation: fidelity crosses $1.1\\times$ at 20K while value-to-eval rises at ${\\sim}$30K ($r{=}0.81$, $p{=}0.002$; Figure~\\ref{fig:temporal_ordering}). A second seed confirms the pattern (lead ${\\approx}$9K; Appendix~\\ref{sec:timeseries_fidelity}). This temporal precedence is consistent with but does not establish causal direction.\n\n%% ============================================================\n%% F3--F5: Summary (details in Appendix B)\n%% ============================================================\n\n\\subsection{F3--F5: Causal Ablation and Cross-Environment Validation}\n\\label{sec:f3f5_summary}\n\nTrained $\\dt$-embedding triggers CIVO in 5/7 multi-joint locomotion seeds vs.\\ 0/16 frozen or removed controls ($p < 0.001$; Table~\\ref{tab:three_way_emb}); a random-policy decomposition attributes ${\\approx}36\\%$ of the effect to dynamics bias and ${\\approx}64\\%$ to actor exploitation (Appendix~\\ref{sec:civo_mechanism}). Cross-environment validation on three ManiSkill tasks shows comparable value-ratio transients ($4$--$11\\times$) with frozen controls matching, ruling out $\\dt$-embedding causation (Table~\\ref{tab:cross_domain}); CIVO is specific to multi-joint locomotion. Full factorial analysis in Appendix~\\ref{sec:appendix_factorial}.\n\n%% ============================================================\n%% F6--F7: Interventions\n%% ============================================================\n\n\\subsection{F6--F7: Interventions}\n\\label{sec:f6}\n\n\\paragraph{F6: $\\dt{=}1$ imagination eliminates CIVO.}\nRestricting imagination to $\\dt{=}1$ while retaining the trained embedding (exp\\_008e\\_v3; Appendix~\\ref{sec:code_corrections}) yields 0/4 CIVO (peak NVE ${\\leq}0.8\\times$); three seeds achieve $64$--$94\\%$ of baseline (mean $775.6$; Figure~\\ref{fig:multiple_pathways}). Multi-step imagination---not the trained embedding alone---is necessary for CIVO.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig6_multiple_pathways.pdf}\n\\caption{Contrasting dynamics ($2{\\times}3$ grid). \\textbf{Top row:} 008d (CIVO)---eval collapse, value explosion, entropy decrease. \\textbf{Bottom row:} 008e\\_v3 s1 ($\\dt{=}1$ imagination)---no CIVO (NVE ${\\leq}\\,0.6\\times$, eval $94\\%$ baseline).}\n\\label{fig:multiple_pathways}\n\\end{figure}\n\n\\paragraph{F7: Full-pathway gradient stopping shows mixed results.}\nFull-SGS (exp\\_018) detaches all non-KL gradients from $e_{\\dt}$. Seed~1 shows partial mitigation (eval 448.3, NVE $1.66\\times$; anecdotal, $n{=}1$); seed~2 collapses (neither seed achieves elimination; Appendix~\\ref{sec:sgs_gradient_analysis}). Cross-environment validation on Cheetah confirms CIVO generalization (010b, NVE $8.27$--$108.52\\times$); full-SGS yields 0/3 elimination. Removing the embedding eliminates CIVO on Cheetah (024b, NVE $< 0.2\\times$). Targeted obs-decoder-only SGS (exp\\_025/026) achieves 1/6 prevention (1/4 Walker, 0/2 Cheetah; Table~\\ref{tab:intervention_hierarchy}), confirming pathway redundancy: blocking any single channel shifts co-adaptation to the remaining ones (Appendix~\\ref{sec:seed_divergence}).\n\n%% ============================================================\n%% Forward-pass interventions\n%% ============================================================\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_results}\n\n\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} & \\textbf{Eval (\\%BL)} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% & $15{\\pm}10$ \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% & $31{\\pm}39$ \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% & $34{\\pm}26$ \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% & $33{\\pm}31$ \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% & $6{\\pm}4$ \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% & 21 \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% & $14{\\pm}7$ \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% & $20{\\pm}11$ \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% & 16 \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% & $39{\\pm}8$ \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% & $70{\\pm}8$ \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% & $55{\\pm}24$ \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% & $31{\\pm}18$ \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% & $29{\\pm}13$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails because the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) shows binary behavior---suppressing CIVO in 2/4 Walker seeds ($\\sigma{=}0.2$) while remaining seeds escalate---and cross-environment transfer fails ($\\sigma{=}1.0$ erodes Cheetah policy to 15\\% of baseline; Appendix~\\ref{sec:tcn_cross_env}).\n\n%% ============================================================\n%% Architecture-Level Ablation\n%% ============================================================\n\n\\subsection{Architecture-Level Ablation}\n\\label{sec:arch_results}\n\n\\paragraph{Critic convergence in pure imagination.}\nAcross all dual-critic configurations ($n{=}7$), critics converge ($\\rho > 0.999$) with pessimism at 3--4\\% of the independent-critic bound, rendering standard pessimistic estimation ineffective.\n\n\\paragraph{Wide dual-critic: the sole partial success.}\nA $2{\\times}2$ factorial separates two mechanisms: narrow dual-critic (min, ${\\sim}1.2$M) recovers from CIVO (${\\sim}16$--$19\\times$ ratio reduction) but does not prevent onset; wide dual-critic (min $+$ ${\\sim}2.4$M) achieves NVE $\\leq 1.4\\times$ in 3/4 seeds (3/3 Walker, 0/1 Cheetah)---the strongest result across all levels (Table~\\ref{tab:intervention_hierarchy}). Wide single (0/2) confirms both components are necessary. Cross-environment transfer is limited (Appendix~\\ref{sec:dual_critic_appendix}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 159,
        "oldLines": 7,
        "newStart": 159,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). No level reliably eliminates CIVO across environments.",
          "+\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). Eval (\\%BL) = mean${\\pm}$std of final eval return as percentage of per-environment baseline (Walker 915.7, Cheetah 446.1). No level reliably eliminates CIVO across environments.",
          " $^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.",
          " $^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).",
          " $^\\S$Policy erosion (final 15\\% baseline)."
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

_source line 236_

Now compile to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "5ea9517a-87f4-406e-8deb-04caeb0364de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B8BhH5736VhPyPVot6B18",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 157902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
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

_source line 237_

<details open><summary>🔧 Tool call — Bash · `toolu_01D7voS5SJCRtYQBGKwHzU3J`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Compile LaTeX to verify table",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "e08bccf3-438e-4d41-9bc1-2f27bb3ef8f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B8BhH5736VhPyPVot6B18",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 157902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
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

_source line 238 · 2026-05-29T00:49:35.338Z_

<details><summary>↩ Tool result · `toolu_01D7voS5SJCRtYQBGKwHzU3J`</summary>

```text
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt0900.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uh
vr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/zapfding/uzdr.pfb>
Output written on main.pdf (42 pages, 4692424 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "1a87cde4-1bbe-4d30-a4e3-b8b51b078535",
  "tool_use_result": {
    "stdout": "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt0900.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uh\nvr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/zapfding/uzdr.pfb>\nOutput written on main.pdf (42 pages, 4692424 bytes).\nTranscript written on main.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 239_

<details open><summary>🔧 Tool call — Bash · `toolu_01HbHSeXsQYcrrhPycHxnVzo`</summary>

```json
{
  "command": "grep -c \"Overfull.*hbox\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log && echo \"---\" && grep \"Overfull.*hbox\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log | grep -i \"table\\|intervention\" | head -5",
  "description": "Check for overfull hbox warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "b16e5587-5c37-402e-b8dc-a5538a6b3bac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3q3XtL4vdtrNVCwb4r3o2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 158519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1137
      },
      "output_tokens": 39,
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

_source line 240 · 2026-05-29T00:49:40.076Z_

<details><summary>↩ Tool result · reported error · `toolu_01HbHSeXsQYcrrhPycHxnVzo`</summary>

```text
Exit code 1
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "7aa553da-093c-45ca-b196-24bc48e7f456",
  "tool_use_result": "Error: Exit code 1\n0"
}
```

</details>

---


### Tool call

_source line 241_

<details open><summary>🔧 Tool call — Bash · `toolu_01QPQxoqfZByJgGCdUqyVbrv`</summary>

```json
{
  "command": "grep -c \"Overfull\" /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.log",
  "description": "Count overfull warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "34235468-8b57-4fda-aba1-cd2dc881bba8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuLwNKzrRVWrEZgK8ThRpj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 159656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
      },
      "output_tokens": 72,
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

_source line 242 · 2026-05-29T00:49:43.022Z_

<details><summary>↩ Tool result · `toolu_01QPQxoqfZByJgGCdUqyVbrv`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "d0ee2916-8cc9-4136-bb17-ae94edccdbc2",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 243_

编译成功，无 overfull 警告。让我验证最终表格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "a78753ad-5412-4ea5-b074-de604ffe06ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5oiRumFyZwpkSDjcdrBty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 132,
      "cache_read_input_tokens": 159875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 132
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

_source line 244_

<details open><summary>🔧 Tool call — Read · `toolu_01VjEczjU8b2NR4t8QXvg4Uc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
  "offset": 160,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "7e8041c9-9b6f-4963-9db3-210c6495bc41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5oiRumFyZwpkSDjcdrBty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 132,
      "cache_read_input_tokens": 159875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 132
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

_source line 245 · 2026-05-29T00:49:46.407Z_

<details><summary>↩ Tool result · `toolu_01VjEczjU8b2NR4t8QXvg4Uc`</summary>

```text
160	\begin{table}[t]
161	\centering
162	\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\times$ (35K+). Eval (\%BL) = mean${\pm}$std of final eval return as percentage of per-environment baseline (Walker 915.7, Cheetah 446.1). No level reliably eliminates CIVO across environments.
163	$^\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.
164	$^\ddagger$Borderline (NVE${=}1.02\times$, eval 55\%).
165	$^\S$Policy erosion (final 15\% baseline).
166	$^\|$Walker 3/3, Cheetah 0/1.
167	$^\#$7 seeds, all NVE $< 2.0\times$.
168	$^\P$6 seeds, all NVE $< 2.0\times$.}
169	\label{tab:intervention_hierarchy}
170	\footnotesize
171	\setlength{\tabcolsep}{3pt}
172	\begin{tabular}{llcccc}
173	\toprule
174	\textbf{Level} & \textbf{Intervention} & \textbf{Seeds} & \textbf{Prev.} & \textbf{Rate} & \textbf{Eval (\%BL)} \\
175	\midrule
176	--- & Untreated & 10 & 0/10 & 0\% & $15{\pm}10$ \\
177	\midrule
178	Gradient & Reward-only SGS & 2 & 0/2 & 0\% & $31{\pm}39$ \\
179	Gradient & Full-pathway SGS & 3 & 0/3 & 0\% & $34{\pm}26$ \\
180	Gradient & Obs-decoder SGS & 6 & 1/6 & 17\% & $33{\pm}31$ \\
181	\midrule
182	Output & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\% & $6{\pm}4$ \\
183	\midrule
184	Repr. & TCN ($\sigma{=}0.1$) & 1 & 1/1$^\ddagger$ & 100\% & 21 \\
185	Repr. & TCN ($\sigma{=}0.2$) & 6$^\dagger$ & 3/6 & 50\% & $14{\pm}7$ \\
186	Repr. & TCN ($\sigma{=}0.5$) & 3 & 1/3 & 33\% & $20{\pm}11$ \\
187	Repr. & TCN ($\sigma{=}1.0$) & 1 & 1/1$^\S$ & 100\% & 16 \\
188	\midrule
189	Arch. & Wide single & 2 & 0/2 & 0\% & $39{\pm}8$ \\
190	Arch. & Narrow dual (min) & 2 & 0/2 & 0\% & $70{\pm}8$ \\
191	Arch. & Wide dual (min) & 4 & 3/4$^\|$ & 75\% & $55{\pm}24$ \\
192	\midrule
193	--- & Embedding frozen & 7 & 7/7$^\#$ & 100\% & $31{\pm}18$ \\
194	--- & Embedding removed & 6 & 6/6$^\P$ & 100\% & $29{\pm}13$ \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails because the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) shows binary behavior---suppressing CIVO in 2/4 Walker seeds ($\sigma{=}0.2$) while remaining seeds escalate---and cross-environment transfer fails ($\sigma{=}1.0$ erodes Cheetah policy to 15\% of baseline; Appendix~\ref{sec:tcn_cross_env}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "662c03d8-19a6-4672-a2fa-ac08b2d08385",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/experiments_results.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{Intervention hierarchy. Prevention = peak NVE $< 2.0\\times$ (35K+). Eval (\\%BL) = mean${\\pm}$std of final eval return as percentage of per-environment baseline (Walker 915.7, Cheetah 446.1). No level reliably eliminates CIVO across environments.\n$^\\dagger$Walker 2/4; Cheetah 1/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$Policy erosion (final 15\\% baseline).\n$^\\|$Walker 3/3, Cheetah 0/1.\n$^\\#$7 seeds, all NVE $< 2.0\\times$.\n$^\\P$6 seeds, all NVE $< 2.0\\times$.}\n\\label{tab:intervention_hierarchy}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Level} & \\textbf{Intervention} & \\textbf{Seeds} & \\textbf{Prev.} & \\textbf{Rate} & \\textbf{Eval (\\%BL)} \\\\\n\\midrule\n--- & Untreated & 10 & 0/10 & 0\\% & $15{\\pm}10$ \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% & $31{\\pm}39$ \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% & $34{\\pm}26$ \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% & $33{\\pm}31$ \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% & $6{\\pm}4$ \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% & 21 \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 3/6 & 50\\% & $14{\\pm}7$ \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 1/3 & 33\\% & $20{\\pm}11$ \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% & 16 \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% & $39{\\pm}8$ \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% & $70{\\pm}8$ \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% & $55{\\pm}24$ \\\\\n\\midrule\n--- & Embedding frozen & 7 & 7/7$^\\#$ & 100\\% & $31{\\pm}18$ \\\\\n--- & Embedding removed & 6 & 6/6$^\\P$ & 100\\% & $29{\\pm}13$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails because the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) shows binary behavior---suppressing CIVO in 2/4 Walker seeds ($\\sigma{=}0.2$) while remaining seeds escalate---and cross-environment transfer fails ($\\sigma{=}1.0$ erodes Cheetah policy to 15\\% of baseline; Appendix~\\ref{sec:tcn_cross_env}).",
      "numLines": 40,
      "startLine": 160,
      "totalLines": 214
    }
  }
}
```

</details>

---


### Assistant

_source line 246_

编译成功，0 overfull 警告，表格完整。

## 产出汇总

### 1. 每组 exp_ids + eval_return 值

| Group | Seeds | Experiments & eval values |
|---|---|---|
| **Untreated** | 10 | W: 008d/009e s1=131.1, 009b s2=267.9, 008d_s3=268, 008d_s4=63.6, 059 s5=95.8, 068 s1r=39.1; C: 010b_s0=0.83, 010b s1=51.7, 078 s0=119.5, 097 s3=61.7 |
| **Reward-only SGS** | 2 | 016e=31.7, 044=538.6 |
| **Full-pathway SGS** | 3 | 018v2=448.3, 018 s2=40.8, 021=221.5 |
| **Obs-decoder SGS** | 6 | 025 s1=726.4, s2=89.6, s3=590.2, s4=241.5; 026 s0=38.8, s1=38.3 |
| **RAVE** | 2 | 028 c2.0=29, 028 c1.5=76.2 |
| **TCN σ=0.1** | 1 | 029c=188.6 |
| **TCN σ=0.2** | 6 | 027_σ02=171.4, 029a=180.3, 029b=44.7, 029d=104.5, 030a(C)=31.9, 031(P)=11.6 |
| **TCN σ=0.5** | 3 | 027 s0=166.4, 027 s1=94.6, 030b(C)=143.6 |
| **TCN σ=1.0** | 1 | 030c(C)=72.8 |
| **Wide single** | 2 | 033=407.9, 037(C)=146.1 |
| **Narrow dual** | 2 | 035=697.8, 039=592.7 |
| **Wide dual** | 4 | 032=739.7, 032b=516, 041=544, 034(C)=97.5 |
| **Frozen** | 7 | 042=612, 067=281.5, 047=144.2, 057=123.9, 084=334.1, 046(C)=150.5, 058(C)=80.5 |
| **Removed** | 6 | 008f=139.5, 008f s1=468.8, 008f s4=289.3, 009c s3=311.9, 024b(C) s0=96.5, s1=77.3 |

### 2. Mean±std (%BL)

| Group | Eval (%BL) |
|---|---|
| Untreated | 15±10% |
| Reward-only SGS | 31±39% |
| Full-pathway SGS | 34±26% |
| Obs-decoder SGS | 33±31% |
| RAVE | 6±4% |
| TCN σ=0.1 | 21% (n=1) |
| TCN σ=0.2 | 14±7% |
| TCN σ=0.5 | 20±11% |
| TCN σ=1.0 | 16% (n=1) |
| Wide single | 39±8% |
| Narrow dual | 70±8% |
| Wide dual | 55±24% |
| Frozen | 31±18% |
| Removed | 29±13% |

### 3. 表格 diff

添加了第 6 列 `Eval (%BL)`，更新了 `tabular` 为 `{llcccc}`，caption 中增加了 Eval 列说明。

### 4. 编译结果

pdflatex 成功，42 页输出，0 个 overfull hbox 警告。表格在单栏内正常显示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "uuid": "7a2690f0-2fa0-44e0-849e-d44f9db565a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLsxDgVBJesipk3yQyzs5B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 160007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1414
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

_source line 247_

编译成功，0 overfull 警告，表格完整。

## 产出汇总

### 1. 每组 exp_ids + eval_return 值

| Group | Seeds | Experiments & eval values |
|---|---|---|
| **Untreated** | 10 | W: 008d/009e s1=131.1, 009b s2=267.9, 008d_s3=268, 008d_s4=63.6, 059 s5=95.8, 068 s1r=39.1; C: 010b_s0=0.83, 010b s1=51.7, 078 s0=119.5, 097 s3=61.7 |
| **Reward-only SGS** | 2 | 016e=31.7, 044=538.6 |
| **Full-pathway SGS** | 3 | 018v2=448.3, 018 s2=40.8, 021=221.5 |
| **Obs-decoder SGS** | 6 | 025 s1=726.4, s2=89.6, s3=590.2, s4=241.5; 026 s0=38.8, s1=38.3 |
| **RAVE** | 2 | 028 c2.0=29, 028 c1.5=76.2 |
| **TCN σ=0.1** | 1 | 029c=188.6 |
| **TCN σ=0.2** | 6 | 027_σ02=171.4, 029a=180.3, 029b=44.7, 029d=104.5, 030a(C)=31.9, 031(P)=11.6 |
| **TCN σ=0.5** | 3 | 027 s0=166.4, 027 s1=94.6, 030b(C)=143.6 |
| **TCN σ=1.0** | 1 | 030c(C)=72.8 |
| **Wide single** | 2 | 033=407.9, 037(C)=146.1 |
| **Narrow dual** | 2 | 035=697.8, 039=592.7 |
| **Wide dual** | 4 | 032=739.7, 032b=516, 041=544, 034(C)=97.5 |
| **Frozen** | 7 | 042=612, 067=281.5, 047=144.2, 057=123.9, 084=334.1, 046(C)=150.5, 058(C)=80.5 |
| **Removed** | 6 | 008f=139.5, 008f s1=468.8, 008f s4=289.3, 009c s3=311.9, 024b(C) s0=96.5, s1=77.3 |

### 2. Mean±std (%BL)

| Group | Eval (%BL) |
|---|---|
| Untreated | 15±10% |
| Reward-only SGS | 31±39% |
| Full-pathway SGS | 34±26% |
| Obs-decoder SGS | 33±31% |
| RAVE | 6±4% |
| TCN σ=0.1 | 21% (n=1) |
| TCN σ=0.2 | 14±7% |
| TCN σ=0.5 | 20±11% |
| TCN σ=1.0 | 16% (n=1) |
| Wide single | 39±8% |
| Narrow dual | 70±8% |
| Wide dual | 55±24% |
| Frozen | 31±18% |
| Removed | 29±13% |

### 3. 表格 diff

添加了第 6 列 `Eval (%BL)`，更新了 `tabular` 为 `{llcccc}`，caption 中增加了 Eval 列说明。

### 4. 编译结果

pdflatex 成功，42 页输出，0 个 overfull hbox 警告。表格在单栏内正常显示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 953823,
  "duration_api_ms": 941082,
  "num_turns": 45,
  "stop_reason": "end_turn",
  "session_id": "2cc17247-5799-4eaa-a6da-169e7b334e68",
  "total_cost_usd": 4.2280966000000015,
  "usage": {
    "input_tokens": 40,
    "cache_creation_input_tokens": 149576,
    "cache_read_input_tokens": 3600223,
    "output_tokens": 46698,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 149576,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1111,
        "cache_read_input_tokens": 160007,
        "cache_creation_input_tokens": 1414,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1414
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2106,
      "outputTokens": 11091,
      "cacheReadInputTokens": 1607641,
      "cacheCreationInputTokens": 85728,
      "webSearchRequests": 0,
      "costUSD": 0.32548509999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 40,
      "outputTokens": 46698,
      "cacheReadInputTokens": 3600223,
      "cacheCreationInputTokens": 149576,
      "webSearchRequests": 0,
      "costUSD": 3.9026115,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fd2299ed-c9a6-4b00-8e51-31f14afebb19"
}
```

</details>

---
