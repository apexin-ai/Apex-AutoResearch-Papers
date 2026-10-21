# ssh verify evaluate inference mode

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_ssh_verify-evaluate-inference-mode_20260520T061415.jsonl`
- **Structured JSON:** [`42a03d8d82714c7614e9.json`](../../sessions/42/42a03d8d82714c7614e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-20T06:15:31.258913+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T06:15:31.259259+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T06:15:31.259526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat -n /root/acr-vla-conformal-refinement/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat -n /root/acr-vla-conformal-refinement/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T06:15:31.259687+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/acr-vla-conformal-refinement/evaluate.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.19}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T06:15:31.259827+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T06:15:31.259972+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/mvp/run_mvp.py\\n/root/acr-vla-conformal-refinement/src/__init__.py\\n/root/acr-vla-conformal-refinement/src/cgs.py\\n/root/acr-vla-conformal-refinement/src/aci.py\\n/root/acr-vla-conformal-refinement/src/crm.py\\n/root/acr-vla-conformal-refinement/src/train_crm.py\\n/root/acr-vla-conformal-refinement/src/evaluate.py\\n/root/acr-vla-conformal-refinement/src/utils.py\\n/root/acr-vla-conformal-refinement/src/smolvla_wrapper.py\\n/root/acr-vla-conformal-refinement/src/reconvla_baseline.py\\n/root/acr-vla-conformal-refinement/src/gated_crm.py\\n/root/acr-vla-conformal-refinement/src/compute_norm_stats.py\\n/root/acr-vla-conformal-refinement/src/calibrate_threshold.py\\n/root/acr-vla-conformal-refinement/src/calibrate_crm_signal.py\\n/root/acr-vla-conformal-refinement/scripts/verify_pipeline.py\\n/root/acr-vla-conformal-refinement/scripts/parse_log_to_json.py\\n/root/acr-vla-conformal-refinement/tests/test_aci_sign.py\\n/root/acr-vla-conformal-refinement/verify_batched.py\\n/root/acr-vla-conformal-refinement/benchmark_batched.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T06:15:31.260128+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat -n /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat -n /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T06:15:31.260487+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\tLIBERO evaluation script for ACR-VLA.\\n     3\\t\\n     4\\tRollout loop:\\n     5\\t  1. Load LIBERO env + task suite\\n     6\\t  2. Load SmolVLA (frozen) + CRM\\n     7\\t  3. For each task, rollout N times:\\n     8\\t     a. Reset env\\n     9\\t     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n    10\\t        → combine refined pose with gripper → execute 7D action\\n    11\\t     c. Record success/failure\\n    12\\t  4. Report per-task and overall success rate\\n    13\\t\\n    14\\tBaselines:\\n    15\\t  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n    16\\t  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n    17\\t  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n    18\\t  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n    19\\t  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n    20\\t  - \\\"adaptive_k\\\": Adaptive K — K=2 L2 probe, expand to K=10 + CRM obs_only if uncertain\\n    21\\t\\n    22\\tAdaptive K mode (--mode adaptive_k):\\n    23\\t  Each step: generate K=2 samples, compute pairwise L2 distance.\\n    24\\t  If L2 > threshold (high uncertainty): generate 8 more (total K=10),\\n    25\\t    select argmin(L2 to mean), apply CRM obs_only correction (epsilon=0.2).\\n    26\\t  If L2 <= threshold (low uncertainty): use mean of K=2, skip CRM.\\n    27\\t\\n    28\\tUsage:\\n    29\\t  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n    30\\t  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n    31\\t  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n    32\\t  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n    33\\t\\\"\\\"\\\"\\n    34\\timport argparse\\n    35
…[truncated 7469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T06:15:31.260729+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -n 250 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -n 250 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T06:15:31.261001+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n  2. Load SmolVLA (frozen) + CRM\\n  3. For each task, rollout N times:\\n     a. Reset env\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n        → combine refined pose with gripper → execute 7D action\\n     c. Record success/failure\\n  4. Report per-task and overall success rate\\n\\nBaselines:\\n  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n  - \\\"adaptive_k\\\": Adaptive K — K=2 L2 probe, expand to K=10 + CRM obs_only if uncertain\\n\\nAdaptive K mode (--mode adaptive_k):\\n  Each step: generate K=2 samples, compute pairwise L2 distance.\\n  If L2 > threshold (high uncertainty): generate 8 more (total K=10),\\n    select argmin(L2 to mean), apply CRM obs_only correction (epsilon=0.2).\\n  If L2 <= threshold (low uncertainty): use mean of K=2, skip CRM.\\n\\nUsage:\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n\\\"\\\"\\\"\\nimport argparse\\nimport functools\\nbuiltins_print = print\\nprint = functools.partial(builtins_print, flush=True)\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\n
…[truncated 7070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T06:15:31.261172+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "tail -n +250 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "tail -n +250 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T06:15:31.261459+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    k_full = samples[0, :, :H_EFF, :]  # (K, H_eff, 7)\\n    idx = np.random.randint(0, k_full.shape[0])\\n    return k_full[idx, 0].cpu().numpy()\\n\\n\\n\\ndef select_action_crm_adaptive(wrapper, obs, task_name, cgs_map, crm, device, mode,\\n                                threshold, k_init, k_full, step_metadata):\\n    \\\"\\\"\\\"ACR-VLA with adaptive K sampling.\\\"\\\"\\\"\\n    agentview = obs[\\\"agentview_image\\\"]\\n    eye_in_hand = obs.get(\\\"robot0_eye_in_hand_image\\\", None)\\n    robot_state = get_robot_state(obs)\\n\\n    obs_feat, samples, meta = wrapper.get_obs_features_and_samples_adaptive(\\n        agentview_rgb=agentview,\\n        task_name=task_name,\\n        robot_state=robot_state,\\n        eye_in_hand_rgb=eye_in_hand,\\n        threshold=threshold,\\n        k_init=k_init,\\n        k_full=k_full,\\n    )\\n    step_metadata.append(meta)\\n\\n    actual_k = meta['actual_k']\\n    k_actions = samples[0, :, :H_EFF, :]\\n    k_pose = k_actions[:, :, :CORRECTION_DIM]\\n\\n    cgs = cgs_map[actual_k]\\n    uf, _mean = cgs.compute_features(k_pose)\\n    uf = uf.unsqueeze(0).to(device)\\n    if mode == \\\"crm_scalar\\\":\\n        uf = _to_scalar_uf(uf)\\n\\n    k_pose_flat = k_pose.reshape(k_pose.shape[0], -1)\\n    mean_pose = k_pose_flat.mean(dim=0)\\n    distances = ((k_pose_flat - mean_pose) ** 2).sum(dim=-1)\\n    best_idx = distances.argmin()\\n    base_action = k_pose_flat[best_idx].unsqueeze(0).to(device)\\n\\n    obs_feat = obs_feat.to(device)\\n    uf_input = None if mode == \\\"crm_obs_only\\\" else uf\\n    with torch.no_grad():\\n        refined_pose = crm(base_action, uf_input, obs_feat)\\n\\n    refined_pose = refined_pose[0].reshape(H_EFF, CORRECTION_DIM)\\n    mean_gripper = k_actions[:, :, CORRECTION_DIM:].mean(dim=0)\\n    refined_full = torch.cat([refined_pose, mean_gripper], dim=-1)\\n    return refined_full[0].cpu().numpy()\\n\\n\\n\\ndef select_action_adaptive_
…[truncated 7058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T06:15:31.261656+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat -n /root/acr-vla-conformal-refinement/src/smolvla_wrapper.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat -n /root/acr-vla-conformal-refinement/src/smolvla_wrapper.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T06:15:31.261898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\tSmolVLA wrapper for ACR-VLA.\\n     3\\t\\n     4\\tProvides:\\n     5\\t  1. obs_features extraction (mean-pooled VLM hidden states, 960D)\\n     6\\t  2. K-sample flow-matching generation with shared KV cache\\n     7\\t  3. LIBERO data preprocessing (image, language, state → SmolVLA inputs)\\n     8\\t\\n     9\\tPreprocessing follows the official lerobot pipeline:\\n    10\\t  - Images: flip H+W → resize_with_pad 512×512 → normalize [-1,1]\\n    11\\t  - State: 8D (eef_pos + axisangle + gripper_qpos) → MEAN_STD normalize → pad 32D\\n    12\\t  - Action output: unnormalize with MEAN_STD stats\\n    13\\t\\\"\\\"\\\"\\n    14\\timport math\\n    15\\tfrom pathlib import Path\\n    16\\t\\n    17\\timport torch\\n    18\\timport torch.nn.functional as F\\n    19\\timport numpy as np\\n    20\\tfrom PIL import Image\\n    21\\tfrom torchvision import transforms as T\\n    22\\tfrom safetensors.torch import load_file\\n    23\\t\\n    24\\tfrom lerobot.policies.smolvla.modeling_smolvla import (\\n    25\\t    SmolVLAPolicy,\\n    26\\t    VLAFlowMatching,\\n    27\\t    make_att_2d_masks,\\n    28\\t    resize_with_pad,\\n    29\\t)\\n    30\\t\\n    31\\ttry:\\n    32\\t    from utils import FULL_ACTION_DIM, CORRECTION_DIM\\n    33\\texcept ImportError:\\n    34\\t    from .utils import FULL_ACTION_DIM, CORRECTION_DIM\\n    35\\t\\n    36\\tNORM_EPS = 1e-8\\n    37\\t\\n    38\\t\\n    39\\tdef split_action(action_7d):\\n    40\\t    \\\"\\\"\\\"Split LIBERO 7D action into 6D pose and 1D gripper.\\n    41\\t\\n    42\\t    Works with numpy arrays and torch tensors, including batched inputs.\\n    43\\t    \\\"\\\"\\\"\\n    44\\t    return action_7d[..., :CORRECTION_DIM], action_7d[..., CORRECTION_DIM:FULL_ACTION_DIM]\\n    45\\t\\n    46\\t\\n    47\\tclass SmolVLAWrapper:\\n    48\\t    \\\"\\\"\\\"Frozen SmolVLA for obs_features and K-sample generation.\\\"\\\"\\\"\\n    49\\
…[truncated 7036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T06:15:31.262061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat -n /root/acr-vla-conformal-refinement/verify_batched.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat -n /root/acr-vla-conformal-refinement/verify_batched.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T06:15:31.262249+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"Numerical verification: sequential vs batched K-sample generation.\\\"\\\"\\\"\\n     2\\timport sys\\n     3\\tsys.path.insert(0, \\\"/root/acr-vla-conformal-refinement/src\\\")\\n     4\\t\\n     5\\timport torch\\n     6\\tfrom smolvla_wrapper import SmolVLAWrapper\\n     7\\tfrom utils import load_libero_demos, FULL_ACTION_DIM\\n     8\\t\\n     9\\tprint(\\\"Loading model...\\\")\\n    10\\tmodel = SmolVLAWrapper()\\n    11\\t\\n    12\\tprint(\\\"Loading demo data...\\\")\\n    13\\tdemos = load_libero_demos(\\\"object\\\", max_demos_per_task=1)\\n    14\\tdemo = demos[0]\\n    15\\t\\n    16\\tprint(\\\"Encoding prefix...\\\")\\n    17\\tobs_feat, kv_cache, pad_masks = model.encode_prefix(\\n    18\\t    *model.preprocess_obs(\\n    19\\t        demo[\\\"agentview_rgb\\\"][0],\\n    20\\t        demo[\\\"task_name\\\"],\\n    21\\t        demo[\\\"ee_states\\\"][0],\\n    22\\t        demo[\\\"eye_in_hand_rgb\\\"][0],\\n    23\\t    )\\n    24\\t)\\n    25\\t\\n    26\\tK = 5\\n    27\\tB = pad_masks.shape[0]\\n    28\\tchunk_size = model.config.chunk_size\\n    29\\tmax_act_dim = model.config.max_action_dim\\n    30\\tnum_steps = model.config.num_steps\\n    31\\tdt = -1.0 / num_steps\\n    32\\t\\n    33\\tprint(f\\\"B={B}, K={K}, chunk_size={chunk_size}, max_act_dim={max_act_dim}, num_steps={num_steps}\\\")\\n    34\\t\\n    35\\t# Generate shared noise (K tensors of shape (B, chunk_size, max_act_dim))\\n    36\\ttorch.manual_seed(42)\\n    37\\tnoise_list = [model.flow.sample_noise((B, chunk_size, max_act_dim), model.device) for _ in range(K)]\\n    38\\t\\n    39\\t# --- Sequential ---\\n    40\\tprint(\\\"Running sequential...\\\")\\n    41\\tall_samples = []\\n    42\\tfor k in range(K):\\n    43\\t    x_t = noise_list[k].clone()\\n    44\\t    for step in range(num_steps):\\n    45\\t        time_val = 1.0 + step * dt\\n    46\\t        time_tensor = torch.full((B,), time_val
…[truncated 2139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T06:15:31.262462+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -n 305 /root/acr-vla-conformal-refinement/src/smolvla_wrapper.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -n 305 /root/acr-vla-conformal-refinement/src/smolvla_wrapper.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T06:15:31.262697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nSmolVLA wrapper for ACR-VLA.\\n\\nProvides:\\n  1. obs_features extraction (mean-pooled VLM hidden states, 960D)\\n  2. K-sample flow-matching generation with shared KV cache\\n  3. LIBERO data preprocessing (image, language, state → SmolVLA inputs)\\n\\nPreprocessing follows the official lerobot pipeline:\\n  - Images: flip H+W → resize_with_pad 512×512 → normalize [-1,1]\\n  - State: 8D (eef_pos + axisangle + gripper_qpos) → MEAN_STD normalize → pad 32D\\n  - Action output: unnormalize with MEAN_STD stats\\n\\\"\\\"\\\"\\nimport math\\nfrom pathlib import Path\\n\\nimport torch\\nimport torch.nn.functional as F\\nimport numpy as np\\nfrom PIL import Image\\nfrom torchvision import transforms as T\\nfrom safetensors.torch import load_file\\n\\nfrom lerobot.policies.smolvla.modeling_smolvla import (\\n    SmolVLAPolicy,\\n    VLAFlowMatching,\\n    make_att_2d_masks,\\n    resize_with_pad,\\n)\\n\\ntry:\\n    from utils import FULL_ACTION_DIM, CORRECTION_DIM\\nexcept ImportError:\\n    from .utils import FULL_ACTION_DIM, CORRECTION_DIM\\n\\nNORM_EPS = 1e-8\\n\\n\\ndef split_action(action_7d):\\n    \\\"\\\"\\\"Split LIBERO 7D action into 6D pose and 1D gripper.\\n\\n    Works with numpy arrays and torch tensors, including batched inputs.\\n    \\\"\\\"\\\"\\n    return action_7d[..., :CORRECTION_DIM], action_7d[..., CORRECTION_DIM:FULL_ACTION_DIM]\\n\\n\\nclass SmolVLAWrapper:\\n    \\\"\\\"\\\"Frozen SmolVLA for obs_features and K-sample generation.\\\"\\\"\\\"\\n\\n    def __init__(self, pretrained_path: str = \\\"/root/autodl-tmp/models/smolvla_libero/\\\",\\n                 device: str = \\\"cuda\\\"):\\n        self.device = torch.device(device)\\n        self.policy = SmolVLAPolicy.from_pretrained(pretrained_path)\\n        self.policy.to(self.device)\\n        self.policy.eval()\\n        for p in self.policy.parameters():\\n            p.requires_grad = False\\n\\n        self.flow: VLAF
…[truncated 6821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-20T06:15:31.262903+00:00_

信息已经足够了。

---

```
推理模式: batched（共享 KV cache）
证据代码行: smolvla_wrapper.py:319, 227-268
KV cache: 有，encode_prefix 一次，KV cache repeat_interleave(K) 后所有 K 个 sample 并行去噪
```

### 详细分析

**1. VLA action sampling：batched，共享 KV cache**

核心调用链（`smolvla_wrapper.py`）：

- **L316-319** `get_obs_features_and_samples()`：
  ```python
  obs_feat, kv_cache, pad_masks = self.encode_prefix(...)   # 一次 VLM forward
  samples = self.generate_k_samples_batched(kv_cache, pad_masks, K=K)
  ```

- **L227-268** `generate_k_samples_batched()`：
  - L238-242: KV cache 通过 `repeat_interleave(K, dim=0)` 从 `(B, ...)` 扩展到 `(B*K, ...)`
  - L245: noise shape = `(B*K, chunk_size, max_act_dim)`
  - L247-255: **单个去噪循环**（不是 K 个循环），`B*K` 个 sample 同时走完所有 denoising steps
  - L258: reshape 回 `(B, K, chunk_size, FULL_ACTION_DIM)`

代码中也保留了老版本的 sequential 实现 `generate_k_samples()`（L194-225，`for _ in range(K)` 循环），但 **evaluate.py 调用的是 `_batched` 版本**。

**2. KV cache 复用：有**

`encode_prefix()`（L168-190）做一次 VLM forward pass 并返回 `past_key_values`。`generate_k_samples_batched()` 把这个 cache `repeat_interleave` 到 K 份，所有 K 个 sample 共享同一份 prefix encoding。VLM 编码只做 1 次，不是 K 次。

**3. 各 mode 的调用路径**

| Mode | 采样方式 | CRM | 具体路径 |
|------|----------|-----|----------|
| `vla_only` | `get_obs_features_and_samples(K)` → batched → mean of K samples | 无 | `select_action_vla_only` (evaluate.py ~L155) |
| `crm_perdof` / `acr_vla` / `crm_scalar` / `crm_obs_only` | 同上 batched K=10 → CGS → argmin → CRM refine | 有 | `select_action_crm` (evaluate.py ~L170) |
| `reconvla` | 同上 batched K=10 → scalar Euclidean argmin | 无 CRM | `select_action_reconvla` (evaluate.py ~L200) |
| `random_selection` | 同上 batched K=10 → random pick 1 | 无 | `select_action_random` (evaluate.py ~L215) |
| `adaptive_k` | `get_obs_features_and_samples_adaptive(k_init=2, k_full=10)` → 先 batched 生成 2 个，L2 > threshold 则再 batched 生成 8 个 → fast path: mean of 2; full path: argmin + CRM obs_only | 条件触发 | `select_action_adaptive_k` (evaluate.py ~L295) |

**adaptive_k 细节**：`generate_adaptive_k_samples()`（wrapper L332-366）先调 `generate_k_samples_batched(K=2)`，判断 L2；若超阈值，再调 `generate_k_samples_batched(K=8)` 并 `torch.cat`。两次都复用同一个 KV cache，不重新编码。

**结论：所有 mode 均为 batched + shared KV cache。** 论文中声明的延迟计算可以基于"VLM encode 1 次 + batched denoising"来分析，不需要乘以 K 倍的 VLM forward cost。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_verify-evaluate-inference-mode_20260520T061415"
}
```

</details>

---
