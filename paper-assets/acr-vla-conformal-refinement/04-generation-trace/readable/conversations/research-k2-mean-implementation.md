# research k2 mean implementation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_research_k2-mean-implementation_20260523T064126.jsonl`
- **Structured JSON:** [`ee551796890d2f9822b6.json`](../../sessions/ee/ee551796890d2f9822b6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T06:42:30.421084+00:00_

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
  "session": "worker_research_k2-mean-implementation_20260523T064126",
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

_source line 2 · 2026-05-23T06:42:30.421560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:42:30.421807+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "wc -l /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "wc -l /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T06:42:30.422029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"843 /root/acr-vla-conformal-refinement/src/evaluate.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.95}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T06:42:30.422232+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"add_argument\\|argparse\\|baseline_mode\\|eval_mode\\|--K\\|--mode\\|--num_samples\\|--baseline\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"add_argument\\|argparse\\|baseline_mode\\|eval_mode\\|--K\\|--mode\\|--num_samples\\|--baseline\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:42:30.422473+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:42:30.422676+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"mode.*==\\|mode.*in\\|if.*mode\\|elif.*mode\\|mean\\|average\\|argmin\\|centroid\\|reconvla\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"mode.*==\\|mode.*in\\|if.*mode\\|elif.*mode\\|mean\\|average\\|argmin\\|centroid\\|reconvla\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:42:30.422881+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T06:42:30.423100+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -200 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -200 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:42:30.423576+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n  2. Load SmolVLA (frozen) + CRM\\n  3. For each task, rollout N times:\\n     a. Reset env\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n        → combine refined pose with gripper → execute 7D action\\n     c. Record success/failure\\n  4. Report per-task and overall success rate\\n\\nBaselines:\\n  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n  - \\\"adaptive_k\\\": Adaptive K — K=2 L2 probe, expand to K=10 + CRM obs_only if uncertain\\n\\nAdaptive K mode (--mode adaptive_k):\\n  Each step: generate K=2 samples, compute pairwise L2 distance.\\n  If L2 > threshold (high uncertainty): generate 8 more (total K=10),\\n    select argmin(L2 to mean), apply CRM obs_only correction (epsilon=0.2).\\n  If L2 <= threshold (low uncertainty): use mean of K=2, skip CRM.\\n\\nUsage:\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n\\\"\\\"\\\"\\nimport argparse\\nimport functools\\nbuiltins_print = print\\nprint = functools.partial(builtins_print, flush=True)\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\n
…[truncated 7277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:42:30.423866+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"mean\\|average\\|argmin\\|centroid\\|reconvla\\|baseline\\|mode\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"mean\\|average\\|argmin\\|centroid\\|reconvla\\|baseline\\|mode\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T06:42:30.424088+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T06:42:30.424354+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "tail -n +200 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "tail -n +200 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T06:42:30.424791+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    )\\n    # samples: (1, K, chunk_size, FULL_ACTION_DIM)\\n    k_trunc = samples[0, :, :H_EFF, :]  # (K, H_eff, 7)\\n    mean_action = k_trunc.mean(dim=0)  # (H_eff, 7)\\n    return mean_action[0].cpu().numpy()\\n\\n\\ndef _to_scalar_uf(uf):\\n    return torch.stack([\\n        uf[:, :30].norm(dim=1),\\n        uf[:, 30:35].mean(dim=1),\\n        uf[:, 35:40].mean(dim=1),\\n    ], dim=1)\\n\\n\\n\\n# ── Unified obs_dim padding ─────────────────────────────────────────\\n_UNIFIED_OBS_DIM = None  # set from args in main()\\n\\ndef _pad_obs(obs_feat):\\n    \\\"\\\"\\\"Zero-pad obs_feat to _UNIFIED_OBS_DIM if needed.\\\"\\\"\\\"\\n    if _UNIFIED_OBS_DIM is None:\\n        return obs_feat\\n    current_dim = obs_feat.shape[-1]\\n    if current_dim < _UNIFIED_OBS_DIM:\\n        pad_size = _UNIFIED_OBS_DIM - current_dim\\n        return F.pad(obs_feat, (0, pad_size))\\n    return obs_feat\\n\\ndef select_action_crm(wrapper, obs, task_name, K, cgs, crm, device, mode=\\\"crm_perdof\\\", obs_proj=None):\\n    \\\"\\\"\\\"ACR-VLA: CGS on 6D pose → argmin base → CRM refinement → combine with mean gripper.\\\"\\\"\\\"\\n    agentview = obs[\\\"agentview_image\\\"]\\n    eye_in_hand = obs.get(\\\"robot0_eye_in_hand_image\\\", None)\\n    robot_state = get_robot_state(obs)\\n\\n    obs_feat, samples = wrapper.get_obs_features_and_samples(\\n        agentview_rgb=agentview,\\n        task_name=task_name,\\n        robot_state=robot_state,\\n        eye_in_hand_rgb=eye_in_hand,\\n        K=K,\\n    )\\n    k_full = samples[0, :, :H_EFF, :]  # (K, H_eff, 7)\\n    k_pose = k_full[:, :, :CORRECTION_DIM]  # (K, H_eff, 6)\\n\\n    uf, _mean = cgs.compute_features(k_pose)\\n    uf = uf.unsqueeze(0).to(device)\\n    if mode == \\\"crm_scalar\\\":\\n        uf = _to_scalar_uf(uf)\\n\\n    # Argmin-selected base action instead of mean (avoids invalid inter-mode regions)\\n    k_pose_flat = k_pose.reshape(k_pose.shape[0], -1)  # (K, 
…[truncated 7086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T06:42:30.425100+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/src/reconvla_baseline.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/acr-vla-conformal-refinement/src/reconvla_baseline.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T06:42:30.425364+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nReconVLA baseline (plan_014).\\n\\nScalar Euclidean nonconformity score + argmin selection over K flow-matching samples.\\nNo learned CRM, no per-DOF features — the simplest conformal selection baseline.\\n\\\"\\\"\\\"\\nimport torch\\n\\n\\ndef reconvla_select(k_samples, calibration_mean=None):\\n    \\\"\\\"\\\"\\n    Select the best action from K samples via scalar Euclidean nonconformity.\\n\\n    Args:\\n        k_samples: (K, H_EFF, ACTION_DIM) — K flow-matching action samples\\n        calibration_mean: (H_EFF, ACTION_DIM) — reference mean.\\n            If None, uses mean of k_samples (online estimation, consistent with ReconVLA).\\n\\n    Returns:\\n        selected_action: (H_EFF, ACTION_DIM) — sample with minimum nonconformity score\\n    \\\"\\\"\\\"\\n    K = k_samples.shape[0]\\n    if calibration_mean is None:\\n        calibration_mean = k_samples.mean(dim=0)\\n\\n    flat_samples = k_samples.reshape(K, -1)\\n    flat_mean = calibration_mean.reshape(1, -1)\\n\\n    scores = torch.norm(flat_samples - flat_mean, p=2, dim=1)\\n    best_idx = scores.argmin()\\n    return k_samples[best_idx]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_k2-mean-implementation_20260523T064126",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T06:42:30.425694+00:00_

信息完整，给出报告。

---

## 报告

### 1. K=2 mean 是否已支持？

**已支持。** 用 `vla_only` mode + `--baseline_mode mean` 即可。

但当前实现有一个问题：`--baseline_mode mean` 会强制 K=10（见 `main()` 第 815 行）：

```python
if args.mode == "vla_only":
    if args.baseline_mode == "single":
        args.K = 1
    elif args.baseline_mode == "mean":
        args.K = 10
```

所以 **K=2 mean 不是开箱即用的**——`--baseline_mode mean` 会覆盖用户传的 `--K 2`。

**调用方式（需要微调）：**

当前想跑 K=2 mean，`--mode vla_only --baseline_mode mean --K 2` 不行，因为 K 会被覆盖成 10。

### 2. 最小改动方案

改 `main()` 中那 4 行，让 `--baseline_mode mean` 不覆盖用户显式指定的 K：

```python
# 改前：
if args.mode == "vla_only":
    if args.baseline_mode == "single":
        args.K = 1
    elif args.baseline_mode == "mean":
        args.K = 10

# 改后：
if args.mode == "vla_only":
    if args.baseline_mode == "single":
        args.K = 1
    # baseline_mode == "mean" 时保留用户指定的 --K 值
```

改完后调用：
```bash
python evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --n_rollouts 20
```

`select_action_vla_only` 的逻辑已经是正确的——它对 K 个 sample 取 mean（第 202-204 行），K=2 时就是 2 个 sample 取均值。

### 3. reconvla --K 2 的实际行为

`reconvla_select` 逻辑：
1. 计算 K 个 sample 的 mean（centroid）
2. 计算每个 sample 到 centroid 的 L2 距离
3. 选距离最小的那个

**K=2 时**：两个 sample 到它们均值的距离是**对称的**（距离相等），所以 `argmin()` 总是返回 index 0（PyTorch tie-breaking 行为）。这意味着 **reconvla K=2 等价于总是选第一个 sample，不具备有意义的选择能力**。这不是 bug，是 K=2 下 argmin-to-centroid 的数学必然。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_k2-mean-implementation_20260523T064126"
}
```

</details>

---
