# code plan004 asv envelope smalltau

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_code_plan004-asv-envelope-smalltau_20260520T131037.log`
- **Structured JSON:** [`dc4067458632cbbd9c93.json`](../../sessions/dc/dc4067458632cbbd9c93.json)

## Before a recorded user message

31 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "b57a2d90-126a-4bcb-a423-c84def3e2cf7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
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
    "resetsAt": 1779299400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f6820bcd-e762-48fc-b2b3-6a545068307d",
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e"
}
```

---

### Assistant

_source line 4_

Looking at the task, I need to:
1. Read the current script on the server
2. Create a new v3 script with envelope monotonicity and small-τ support
3. Run it and collect results

Let me start by reading the current code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "45ca164a-f55f-4e9f-8a80-1046706d3517",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgXKuWoJJSG3Y2dYv1Zgp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13365,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13365
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JAfJJmpB6MUHhhWAFDt9av`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "e557d0c6-b8cf-40d2-b42e-632c61af820b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgXKuWoJJSG3Y2dYv1Zgp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13365,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13365
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

_source line 6 · 2026-05-20T13:10:50.588Z_

<details><summary>↩ Tool result · `toolu_01JAfJJmpB6MUHhhWAFDt9av`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "a65f37c1-24fa-4863-a9b7-e459789650f9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
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
Let me read the current script on the server first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "6d17d3ba-1dba-4c7b-a03c-0fdee5de88a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRo964z96eEZxqpUkkYBwm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2036,
      "cache_read_input_tokens": 25206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2036
      },
      "output_tokens": 43,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KZRYFEAniN6QLC9nq4UunG`</summary>

```json
{
  "server": "home-1x5090",
  "command": "cat /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "2e98f790-b6e5-47f4-a8dd-65b19945b1f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRo964z96eEZxqpUkkYBwm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2036,
      "cache_read_input_tokens": 25206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2036
      },
      "output_tokens": 43,
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

_source line 9 · 2026-05-20T13:10:56.271Z_

<details><summary>↩ Tool result · `toolu_01KZRYFEAniN6QLC9nq4UunG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 23704 字符] ...\\n\\nbeta_med = np.array([0.0, 1.0, -0.5])\\n\\n    print(header)\\n    print(\\\"  \\\" + \\\"-\\\" * 54)\\n\\n    for cname, C0 in C_list.items():\\n        for h_label, tau_val in [(\\\"H0\\\", 0.0), (\\\"H1\\\", 0.5)]:\\n            seed_ctr += 1\\n            dmin, dmax = param.delta_range(C0)\\n            deltas = np.linspace(dmin, dmax, 1000)\\n            tau_curve = np.array([\\n                plim_mediation(param(C0, d), beta_med, tau_val)[1]\\n                for d in deltas])\\n\\n            rng = np.random.default_rng(seed_ctr)\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\n\\n            for mc in range(n_mc):\\n                Td, Yd, _, Asd = gen_mediation_data(\\n                    N_sample, beta_med, tau_val, C0, rng)\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\n                tau_hat = bh[1]; se_tau = seh[1]\\n\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\n                if reject:\\n                    naive_rej += 1\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\n                asv_vals.append(asv_val)\\n                if reject and (asv_val is None or asv_val > 1.0):\\n                    asv_rej += 1\\n\\n            asv_fin = [a for a in asv_vals if a is not None]\\n            asv_m = f\\\"{np.mean(asv_fin):.2f}\\\" if asv_fin else \\\"N/A\\\"\\n            print(f\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\")\\n\\n    # === Collider ===\\n    print(\\\"\\\\n  [Collider]\\\")\\n    print(header)\\n    print(\\\"  \\\" + \\\"-\\\" * 54)\\n\\n    for h_label, tau_val in [(\\\"H0\\\", 0.0), (\\\"H1\\\", 1.0)]:\\n        params_h = dict(COLLIDER_PARAMS)\\n        params_h['tau'] = tau_val\\n        print(f\\\"    precomputing collider moments for {h_label} (tau={tau_val})...\\\")\\n        st_h = precomp_collider(params=params_h, N=1_000_000)\\n\\n        for cname, C0 in C_list.items():\\n            seed_ctr += 1\\n            dmin, dmax = param.delta_range(C0)\\n            deltas = np.linspace(dmin, dmax, 1000)\\n            tau_curve = np.array([\\n                plim_collider(param(C0, d), st_h)[1] for d in deltas])\\n\\n            rng = np.random.default_rng(seed_ctr)\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\n\\n            for mc in range(n_mc):\\n                Td, Yd, _, Asd = gen_collider_data(\\n                    N_sample, params_h, C0, rng)\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\n                tau_hat = bh[1]; se_tau = seh[1]\\n\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\n                if reject:\\n                    naive_rej += 1\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\n                asv_vals.append(asv_val)\\n                if reject and (asv_val is None or asv_val > 1.0):\\n                    asv_rej += 1\\n\\n            asv_fin = [a for a in asv_vals if a is not None]\\n            asv_m = f\\\"{np.mean(asv_fin):.2f}\\\" if asv_fin else \\\"N/A\\\"\\n            print(f\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\")\\n\\n    print(f\\\"\\\\n  Total time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Main\\n# ============================================================================\\n\\nif __name__ == \\\"__main__\\\":\\n    np.set_printoptions(precision=6, suppress=True)\\n    print(\\\"plan_004 ASV Framework v2 -- Full Run\\\")\\n    print(\\\"Scheme A: Linear Interpolation + Vulnerability/Protection\\\")\\n    print(\\\"=\\\" * 70)\\n    t_total = time.time()\\n\\n    print(\\\"Precomputing collider sufficient statistics (N=2M)...\\\")\\n    st = precomp_collider()\\n    print(f\\\"  Done ({time.time()-t_total:.1f}s)\\\")\\n\\n    part1_verify(st)\\n    part2_asv_table(st)\\n    part3_monotonicity(st, n_C0=1000, n_delta=100)\\n    part4_sharpness(st)\\n    part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100)\\n    part6_type_errors(n_mc=2000, N_sample=1000)\\n\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    elapsed = time.time() - t_total\\n    print(f\\\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\\\")\\n    print(\\\"=\\\" * 70)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.21}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "ab131b95-f526-41a9-9c2f-8ea5cf044d23",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nplan_004: ASV Framework v2\\\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\\\n\\\\n双方向:\\\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport time\\\\nfrom abc import ABC, abstractmethod\\\\n\\\\n\\\\n# ============================================================================\\\\n# Utilities\\\\n# ============================================================================\\\\n\\\\ndef softmax(x):\\\\n    e = np.exp(x - x.max())\\\\n    return e / e.sum()\\\\n\\\\n\\\\ndef p_cat(t, g, d):\\\\n    return softmax(g + d * t)\\\\n\\\\n\\\\ndef generate_Astar(A, C, rng):\\\\n    probs = C[:, A]\\\\n    cum = np.cumsum(probs, axis=0)\\\\n    u = rng.uniform(size=len(A))\\\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\\\n\\\\n\\\\ndef softmax_sample(logits, rng):\\\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\\\n    cum = np.cumsum(probs, axis=1)\\\\n    u = rng.uniform(size=logits.shape[0])\\\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\\\n\\\\n\\\\ndef check_column_stochastic(C, tol=1e-6):\\\\n    assert np.all(C >= -tol), f\\\\\\\"Negative entries in C: min={C.min()}\\\\\\\"\\\\n    col_sums = C.sum(axis=0)\\\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\\\\\"Column sums != 1: {col_sums}\\\\\\\"\\\\n\\\\n\\\\ndef ols_with_dummies(Y, T, Astar, K=3):\\\\n    N = len(Y)\\\\n    D = np.zeros((N, K - 1))\\\\n    for k in range(1, K):\\\\n        D[:, k - 1] = (Astar == k).astype(float)\\\\n    X = np.column_stack([np.ones(N), T, D])\\\\n    try:\\\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\\\n        resid = Y - X @ beta\\\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\\\n        XtX_inv = np.linalg.inv(X.T @ X)\\\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\\\n    except np.linalg.LinAlgError:\\\\n        beta = np.full(X.shape[1], np.nan)\\\\n        se = np.full(X.shape[1], np.nan)\\\\n    return beta, se\\\\n\\\\n\\\\n# ============================================================================\\\\n# C(delta) Parameterization\\\\n# ============================================================================\\\\n\\\\nclass ConfusionParameterization(ABC):\\\\n    @abstractmethod\\\\n    def __call__(self, C0, delta):\\\\n        pass\\\\n\\\\n    @abstractmethod\\\\n    def delta_range(self, C0=None):\\\\n        pass\\\\n\\\\n\\\\nclass LinearInterpolation(ConfusionParameterization):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\n    def __call__(self, C0, delta):\\\\n        K = C0.shape[0]\\\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\\\n        C_d = np.maximum(C_d, 0.0)\\\\n        col_sums = C_d.sum(axis=0)\\\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\\\n        C_d = C_d / col_sums\\\\n        return C_d\\\\n\\\\n    def delta_range(self, C0=None):\\\\n        if C0 is None:\\\\n            return (0.0, 5.0)\\\\n        min_diag = np.diag(C0).min()\\\\n        if min_diag >= 1.0:\\\\n            return (0.0, 10.0)\\\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\\\n        return (0.0, delta_max)\\\\n\\\\n\\\\n# ============================================================================\\\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\\\n# ============================================================================\\\\n\\\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\\\n    mu = sigma_T\\\\n    ET = np.sum(p_A * mu)\\\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\\\n    q = C @ p_A\\\\n    qt = C @ (p_A * mu)\\\\n    EZZ = np.array([\\\\n        [1,    ET,    q[1],   q[2]  ],\\\\n        [ET,   ET2,   qt[1],  qt[2] ],\\\\n        [q[1], qt[1], q[1],   0     ],\\\\n        [q[2], qt[2], 0,      q[2]  ]])\\\\n    EZX = np.array([\\\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\\\n    try:\\\\n        retur\\\\n\\\\n... [截断: 输出过长，省略 23704 字符] ...\\\\n\\\\nbeta_med = np.array([0.0, 1.0, -0.5])\\\\n\\\\n    print(header)\\\\n    print(\\\\\\\"  \\\\\\\" + \\\\\\\"-\\\\\\\" * 54)\\\\n\\\\n    for cname, C0 in C_list.items():\\\\n        for h_label, tau_val in [(\\\\\\\"H0\\\\\\\", 0.0), (\\\\\\\"H1\\\\\\\", 0.5)]:\\\\n            seed_ctr += 1\\\\n            dmin, dmax = param.delta_range(C0)\\\\n            deltas = np.linspace(dmin, dmax, 1000)\\\\n            tau_curve = np.array([\\\\n                plim_mediation(param(C0, d), beta_med, tau_val)[1]\\\\n                for d in deltas])\\\\n\\\\n            rng = np.random.default_rng(seed_ctr)\\\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\\\n\\\\n            for mc in range(n_mc):\\\\n                Td, Yd, _, Asd = gen_mediation_data(\\\\n                    N_sample, beta_med, tau_val, C0, rng)\\\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\\\n                tau_hat = bh[1]; se_tau = seh[1]\\\\n\\\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\\\n                if reject:\\\\n                    naive_rej += 1\\\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\\\n                asv_vals.append(asv_val)\\\\n                if reject and (asv_val is None or asv_val > 1.0):\\\\n                    asv_rej += 1\\\\n\\\\n            asv_fin = [a for a in asv_vals if a is not None]\\\\n            asv_m = f\\\\\\\"{np.mean(asv_fin):.2f}\\\\\\\" if asv_fin else \\\\\\\"N/A\\\\\\\"\\\\n            print(f\\\\\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\\\\\")\\\\n\\\\n    # === Collider ===\\\\n    print(\\\\\\\"\\\\\\\\n  [Collider]\\\\\\\")\\\\n    print(header)\\\\n    print(\\\\\\\"  \\\\\\\" + \\\\\\\"-\\\\\\\" * 54)\\\\n\\\\n    for h_label, tau_val in [(\\\\\\\"H0\\\\\\\", 0.0), (\\\\\\\"H1\\\\\\\", 1.0)]:\\\\n        params_h = dict(COLLIDER_PARAMS)\\\\n        params_h['tau'] = tau_val\\\\n        print(f\\\\\\\"    precomputing collider moments for {h_label} (tau={tau_val})...\\\\\\\")\\\\n        st_h = precomp_collider(params=params_h, N=1_000_000)\\\\n\\\\n        for cname, C0 in C_list.items():\\\\n            seed_ctr += 1\\\\n            dmin, dmax = param.delta_range(C0)\\\\n            deltas = np.linspace(dmin, dmax, 1000)\\\\n            tau_curve = np.array([\\\\n                plim_collider(param(C0, d), st_h)[1] for d in deltas])\\\\n\\\\n            rng = np.random.default_rng(seed_ctr)\\\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\\\n\\\\n            for mc in range(n_mc):\\\\n                Td, Yd, _, Asd = gen_collider_data(\\\\n                    N_sample, params_h, C0, rng)\\\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\\\n                tau_hat = bh[1]; se_tau = seh[1]\\\\n\\\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\\\n                if reject:\\\\n                    naive_rej += 1\\\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\\\n                asv_vals.append(asv_val)\\\\n                if reject and (asv_val is None or asv_val > 1.0):\\\\n                    asv_rej += 1\\\\n\\\\n            asv_fin = [a for a in asv_vals if a is not None]\\\\n            asv_m = f\\\\\\\"{np.mean(asv_fin):.2f}\\\\\\\" if asv_fin else \\\\\\\"N/A\\\\\\\"\\\\n            print(f\\\\\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n  Total time: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n\\\\n# ============================================================================\\\\n# Main\\\\n# ============================================================================\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    np.set_printoptions(precision=6, suppress=True)\\\\n    print(\\\\\\\"plan_004 ASV Framework v2 -- Full Run\\\\\\\")\\\\n    print(\\\\\\\"Scheme A: Linear Interpolation + Vulnerability/Protection\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n    t_total = time.time()\\\\n\\\\n    print(\\\\\\\"Precomputing collider sufficient statistics (N=2M)...\\\\\\\")\\\\n    st = precomp_collider()\\\\n    print(f\\\\\\\"  Done ({time.time()-t_total:.1f}s)\\\\\\\")\\\\n\\\\n    part1_verify(st)\\\\n    part2_asv_table(st)\\\\n    part3_monotonicity(st, n_C0=1000, n_delta=100)\\\\n    part4_sharpness(st)\\\\n    part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100)\\\\n    part6_type_errors(n_mc=2000, N_sample=1000)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    elapsed = time.time() - t_total\\\\n    print(f\\\\\\\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.21}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 23704 字符] ...\\n\\nbeta_med = np.array([0.0, 1.0, -0.5])\\n\\n    print(header)\\n    print(\\\"  \\\" + \\\"-\\\" * 54)\\n\\n    for cname, C0 in C_list.items():\\n        for h_label, tau_val in [(\\\"H0\\\", 0.0), (\\\"H1\\\", 0.5)]:\\n            seed_ctr += 1\\n            dmin, dmax = param.delta_range(C0)\\n            deltas = np.linspace(dmin, dmax, 1000)\\n            tau_curve = np.array([\\n                plim_mediation(param(C0, d), beta_med, tau_val)[1]\\n                for d in deltas])\\n\\n            rng = np.random.default_rng(seed_ctr)\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\n\\n            for mc in range(n_mc):\\n                Td, Yd, _, Asd = gen_mediation_data(\\n                    N_sample, beta_med, tau_val, C0, rng)\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\n                tau_hat = bh[1]; se_tau = seh[1]\\n\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\n                if reject:\\n                    naive_rej += 1\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\n                asv_vals.append(asv_val)\\n                if reject and (asv_val is None or asv_val > 1.0):\\n                    asv_rej += 1\\n\\n            asv_fin = [a for a in asv_vals if a is not None]\\n            asv_m = f\\\"{np.mean(asv_fin):.2f}\\\" if asv_fin else \\\"N/A\\\"\\n            print(f\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\")\\n\\n    # === Collider ===\\n    print(\\\"\\\\n  [Collider]\\\")\\n    print(header)\\n    print(\\\"  \\\" + \\\"-\\\" * 54)\\n\\n    for h_label, tau_val in [(\\\"H0\\\", 0.0), (\\\"H1\\\", 1.0)]:\\n        params_h = dict(COLLIDER_PARAMS)\\n        params_h['tau'] = tau_val\\n        print(f\\\"    precomputing collider moments for {h_label} (tau={tau_val})...\\\")\\n        st_h = precomp_collider(params=params_h, N=1_000_000)\\n\\n        for cname, C0 in C_list.items():\\n            seed_ctr += 1\\n            dmin, dmax = param.delta_range(C0)\\n            deltas = np.linspace(dmin, dmax, 1000)\\n            tau_curve = np.array([\\n                plim_collider(param(C0, d), st_h)[1] for d in deltas])\\n\\n            rng = np.random.default_rng(seed_ctr)\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\n\\n            for mc in range(n_mc):\\n                Td, Yd, _, Asd = gen_collider_data(\\n                    N_sample, params_h, C0, rng)\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\n                tau_hat = bh[1]; se_tau = seh[1]\\n\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\n                if reject:\\n                    naive_rej += 1\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\n                asv_vals.append(asv_val)\\n                if reject and (asv_val is None or asv_val > 1.0):\\n                    asv_rej += 1\\n\\n            asv_fin = [a for a in asv_vals if a is not None]\\n            asv_m = f\\\"{np.mean(asv_fin):.2f}\\\" if asv_fin else \\\"N/A\\\"\\n            print(f\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\")\\n\\n    print(f\\\"\\\\n  Total time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Main\\n# ============================================================================\\n\\nif __name__ == \\\"__main__\\\":\\n    np.set_printoptions(precision=6, suppress=True)\\n    print(\\\"plan_004 ASV Framework v2 -- Full Run\\\")\\n    print(\\\"Scheme A: Linear Interpolation + Vulnerability/Protection\\\")\\n    print(\\\"=\\\" * 70)\\n    t_total = time.time()\\n\\n    print(\\\"Precomputing collider sufficient statistics (N=2M)...\\\")\\n    st = precomp_collider()\\n    print(f\\\"  Done ({time.time()-t_total:.1f}s)\\\")\\n\\n    part1_verify(st)\\n    part2_asv_table(st)\\n    part3_monotonicity(st, n_C0=1000, n_delta=100)\\n    part4_sharpness(st)\\n    part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100)\\n    part6_type_errors(n_mc=2000, N_sample=1000)\\n\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    elapsed = time.time() - t_total\\n    print(f\\\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\\\")\\n    print(\\\"=\\\" * 70)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.21}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated. Let me read it in sections to get the full code. Let me get the middle part that was truncated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "399d0c33-c247-4c7f-bdee-0291d0a96146",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUrQ3anjxs2JLopFVGbjb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 27242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
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

_source line 11_

The output was truncated. Let me read the file in sections to get the full code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "2749b4f0-d8e0-4dbe-b279-50fff049326a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUrQ3anjxs2JLopFVGbjb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 27242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0154zQpfPiMge1bYAEPYT1Gg`</summary>

```json
{
  "server": "home-1x5090",
  "command": "wc -l /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "12688d1f-856c-4144-9eda-22a84da213d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUrQ3anjxs2JLopFVGbjb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3770,
      "cache_read_input_tokens": 27242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3770
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

_source line 13 · 2026-05-20T13:11:01.900Z_

<details><summary>↩ Tool result · `toolu_0154zQpfPiMge1bYAEPYT1Gg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"873 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "b3e6e64b-19d2-41b6-9805-63d7678a9184",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"873 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"873 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013x24ZPC2utdKtgqtikCzR3`</summary>

```json
{
  "server": "home-1x5090",
  "command": "head -200 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "73e65439-3088-4041-884d-2041ca0c5d58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016E2KWPp96bf2sqgqcjwijP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 31012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
      },
      "output_tokens": 64,
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

_source line 15 · 2026-05-20T13:11:07.242Z_

<details><summary>↩ Tool result · `toolu_013x24ZPC2utdKtgqtikCzR3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        return np.linalg.solve(EZZ, EZX @ b)\\n    except np.linalg.LinAlgError:\\n        return np.full(4, np.nan)\\n\\n\\n# ============================================================================\\n# DAG 2: MEDIATION  T -> A -> Y\\n# ============================================================================\\n\\nGAMMA_MED = np.array([0.0, 0.5, -0.3])\\nDELTA_MED = np.array([0.0, 0.8, -0.6])\\n\\n\\ndef plim_mediation(C, beta, tau, gamma=GAMMA_MED, delta=DELTA_MED):\\n    p0, p1 = p_cat(0, gamma, delta), p_cat(1, gamma, delta)\\n    q0, q1 = C @ p0, C @ p1\\n    pm = .5 * (p0 + p1)\\n    qm = .5 * (q0 + q1)\\n    EZZ = np.array([\\n        [1,      .5,        qm[1],      qm[2]     ],\\n        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],\\n        [qm[1],  .5*q1[1],  qm[1],      0         ],\\n        [qm[2],  .5*q1[2],  0,          qm[2]     ]])\\n    EZX = np.array([\\n        [1,      .5,        pm[1],           pm[2]          ],\\n        [.5,     .5,        .5*p1[1],        .5*p1[2]       ],\\n        [qm[1],  .5*q1[1],  C[1,1]*pm[1],   C[1,2]*pm[2]  ],\\n        [qm[2],  .5*q1[2],  C[2,1]*pm[1],   C[2,2]*pm[2]  ]])\\n    b = np.array([beta[0], tau, beta[1], beta[2]])\\n    try:\\n        return np.linalg.solve(EZZ, EZX @ b)\\n    except np.linalg.LinAlgError:\\n        return np.full(4, np.nan)\\n\\n\\n# ============================================================================\\n# DAG 3: COLLIDER  T -> A <- Y\\n# ============================================================================\\n\\nCOLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0,\\n                       dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)\\n\\n\\ndef precomp_collider(params=None, N=2_000_000, seed=999):\\n    if params is None:\\n        params = COLLIDER_PARAMS\\n    rng = np.random.default_rng(seed)\\n    T = rng.normal(0, 1, N)\\n    eps = rng.normal(0, 1, N)\\n    Y = params['tau'] * T + eps\\n    logits = np.column_stack([\\n        np.zeros(N),\\n        params['g1'] + params['dT'] * T + params['dY'] * Y,\\n        params['g2'] + params['dT2'] * T + params['dY2'] * Y,\\n    ])\\n    A = softmax_sample(logits, rng)\\n    K = 3\\n    DM = np.zeros((N, K))\\n    for k in range(K):\\n        DM[:, k] = (A == k).astype(float)\\n    return dict(\\n        E_T=T.mean(), E_T2=(T**2).mean(),\\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\\n        E_DM=DM.mean(0),\\n        E_DM_T=(DM * T[:, None]).mean(0),\\n        E_DM_Y=(DM * Y[:, None]).mean(0),\\n    )\\n\\n\\ndef plim_collider(C, precomp):\\n    ds = C @ precomp['E_DM']\\n    dst = C @ precomp['E_DM_T']\\n    dsy = C @ precomp['E_DM_Y']\\n    ET, ET2 = precomp['E_T'], precomp['E_T2']\\n    EY, ETY = precomp['E_Y'], precomp['E_TY']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "c37491df-5bad-49fe-8eeb-5e08cda75890",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nplan_004: ASV Framework v2\\\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\\\n\\\\n双方向:\\\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport time\\\\nfrom abc import ABC, abstractmethod\\\\n\\\\n\\\\n# ============================================================================\\\\n# Utilities\\\\n# ============================================================================\\\\n\\\\ndef softmax(x):\\\\n    e = np.exp(x - x.max())\\\\n    return e / e.sum()\\\\n\\\\n\\\\ndef p_cat(t, g, d):\\\\n    return softmax(g + d * t)\\\\n\\\\n\\\\ndef generate_Astar(A, C, rng):\\\\n    probs = C[:, A]\\\\n    cum = np.cumsum(probs, axis=0)\\\\n    u = rng.uniform(size=len(A))\\\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\\\n\\\\n\\\\ndef softmax_sample(logits, rng):\\\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\\\n    cum = np.cumsum(probs, axis=1)\\\\n    u = rng.uniform(size=logits.shape[0])\\\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\\\n\\\\n\\\\ndef check_column_stochastic(C, tol=1e-6):\\\\n    assert np.all(C >= -tol), f\\\\\\\"Negative entries in C: min={C.min()}\\\\\\\"\\\\n    col_sums = C.sum(axis=0)\\\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\\\\\"Column sums != 1: {col_sums}\\\\\\\"\\\\n\\\\n\\\\ndef ols_with_dummies(Y, T, Astar, K=3):\\\\n    N = len(Y)\\\\n    D = np.zeros((N, K - 1))\\\\n    for k in range(1, K):\\\\n        D[:, k - 1] = (Astar == k).astype(float)\\\\n    X = np.column_stack([np.ones(N), T, D])\\\\n    try:\\\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\\\n        resid = Y - X @ beta\\\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\\\n        XtX_inv = np.linalg.inv(X.T @ X)\\\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\\\n    except np.linalg.LinAlgError:\\\\n        beta = np.full(X.shape[1], np.nan)\\\\n        se = np.full(X.shape[1], np.nan)\\\\n    return beta, se\\\\n\\\\n\\\\n# ============================================================================\\\\n# C(delta) Parameterization\\\\n# ============================================================================\\\\n\\\\nclass ConfusionParameterization(ABC):\\\\n    @abstractmethod\\\\n    def __call__(self, C0, delta):\\\\n        pass\\\\n\\\\n    @abstractmethod\\\\n    def delta_range(self, C0=None):\\\\n        pass\\\\n\\\\n\\\\nclass LinearInterpolation(ConfusionParameterization):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\n    def __call__(self, C0, delta):\\\\n        K = C0.shape[0]\\\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\\\n        C_d = np.maximum(C_d, 0.0)\\\\n        col_sums = C_d.sum(axis=0)\\\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\\\n        C_d = C_d / col_sums\\\\n        return C_d\\\\n\\\\n    def delta_range(self, C0=None):\\\\n        if C0 is None:\\\\n            return (0.0, 5.0)\\\\n        min_diag = np.diag(C0).min()\\\\n        if min_diag >= 1.0:\\\\n            return (0.0, 10.0)\\\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\\\n        return (0.0, delta_max)\\\\n\\\\n\\\\n# ============================================================================\\\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\\\n# ============================================================================\\\\n\\\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\\\n    mu = sigma_T\\\\n    ET = np.sum(p_A * mu)\\\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\\\n    q = C @ p_A\\\\n    qt = C @ (p_A * mu)\\\\n    EZZ = np.array([\\\\n        [1,    ET,    q[1],   q[2]  ],\\\\n        [ET,   ET2,   qt[1],  qt[2] ],\\\\n        [q[1], qt[1], q[1],   0     ],\\\\n        [q[2], qt[2], 0,      q[2]  ]])\\\\n    EZX = np.array([\\\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\\\n    try:\\\\n        return np.linalg.solve(EZZ, EZX @ b)\\\\n    except np.linalg.LinAlgError:\\\\n        return np.full(4, np.nan)\\\\n\\\\n\\\\n# ============================================================================\\\\n# DAG 2: MEDIATION  T -> A -> Y\\\\n# ============================================================================\\\\n\\\\nGAMMA_MED = np.array([0.0, 0.5, -0.3])\\\\nDELTA_MED = np.array([0.0, 0.8, -0.6])\\\\n\\\\n\\\\ndef plim_mediation(C, beta, tau, gamma=GAMMA_MED, delta=DELTA_MED):\\\\n    p0, p1 = p_cat(0, gamma, delta), p_cat(1, gamma, delta)\\\\n    q0, q1 = C @ p0, C @ p1\\\\n    pm = .5 * (p0 + p1)\\\\n    qm = .5 * (q0 + q1)\\\\n    EZZ = np.array([\\\\n        [1,      .5,        qm[1],      qm[2]     ],\\\\n        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],\\\\n        [qm[1],  .5*q1[1],  qm[1],      0         ],\\\\n        [qm[2],  .5*q1[2],  0,          qm[2]     ]])\\\\n    EZX = np.array([\\\\n        [1,      .5,        pm[1],           pm[2]          ],\\\\n        [.5,     .5,        .5*p1[1],        .5*p1[2]       ],\\\\n        [qm[1],  .5*q1[1],  C[1,1]*pm[1],   C[1,2]*pm[2]  ],\\\\n        [qm[2],  .5*q1[2],  C[2,1]*pm[1],   C[2,2]*pm[2]  ]])\\\\n    b = np.array([beta[0], tau, beta[1], beta[2]])\\\\n    try:\\\\n        return np.linalg.solve(EZZ, EZX @ b)\\\\n    except np.linalg.LinAlgError:\\\\n        return np.full(4, np.nan)\\\\n\\\\n\\\\n# ============================================================================\\\\n# DAG 3: COLLIDER  T -> A <- Y\\\\n# ============================================================================\\\\n\\\\nCOLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0,\\\\n                       dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)\\\\n\\\\n\\\\ndef precomp_collider(params=None, N=2_000_000, seed=999):\\\\n    if params is None:\\\\n        params = COLLIDER_PARAMS\\\\n    rng = np.random.default_rng(seed)\\\\n    T = rng.normal(0, 1, N)\\\\n    eps = rng.normal(0, 1, N)\\\\n    Y = params['tau'] * T + eps\\\\n    logits = np.column_stack([\\\\n        np.zeros(N),\\\\n        params['g1'] + params['dT'] * T + params['dY'] * Y,\\\\n        params['g2'] + params['dT2'] * T + params['dY2'] * Y,\\\\n    ])\\\\n    A = softmax_sample(logits, rng)\\\\n    K = 3\\\\n    DM = np.zeros((N, K))\\\\n    for k in range(K):\\\\n        DM[:, k] = (A == k).astype(float)\\\\n    return dict(\\\\n        E_T=T.mean(), E_T2=(T**2).mean(),\\\\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\\\\n        E_DM=DM.mean(0),\\\\n        E_DM_T=(DM * T[:, None]).mean(0),\\\\n        E_DM_Y=(DM * Y[:, None]).mean(0),\\\\n    )\\\\n\\\\n\\\\ndef plim_collider(C, precomp):\\\\n    ds = C @ precomp['E_DM']\\\\n    dst = C @ precomp['E_DM_T']\\\\n    dsy = C @ precomp['E_DM_Y']\\\\n    ET, ET2 = precomp['E_T'], precomp['E_T2']\\\\n    EY, ETY = precomp['E_Y'], precomp['E_TY']\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.04}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        return np.linalg.solve(EZZ, EZX @ b)\\n    except np.linalg.LinAlgError:\\n        return np.full(4, np.nan)\\n\\n\\n# ============================================================================\\n# DAG 2: MEDIATION  T -> A -> Y\\n# ============================================================================\\n\\nGAMMA_MED = np.array([0.0, 0.5, -0.3])\\nDELTA_MED = np.array([0.0, 0.8, -0.6])\\n\\n\\ndef plim_mediation(C, beta, tau, gamma=GAMMA_MED, delta=DELTA_MED):\\n    p0, p1 = p_cat(0, gamma, delta), p_cat(1, gamma, delta)\\n    q0, q1 = C @ p0, C @ p1\\n    pm = .5 * (p0 + p1)\\n    qm = .5 * (q0 + q1)\\n    EZZ = np.array([\\n        [1,      .5,        qm[1],      qm[2]     ],\\n        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],\\n        [qm[1],  .5*q1[1],  qm[1],      0         ],\\n        [qm[2],  .5*q1[2],  0,          qm[2]     ]])\\n    EZX = np.array([\\n        [1,      .5,        pm[1],           pm[2]          ],\\n        [.5,     .5,        .5*p1[1],        .5*p1[2]       ],\\n        [qm[1],  .5*q1[1],  C[1,1]*pm[1],   C[1,2]*pm[2]  ],\\n        [qm[2],  .5*q1[2],  C[2,1]*pm[1],   C[2,2]*pm[2]  ]])\\n    b = np.array([beta[0], tau, beta[1], beta[2]])\\n    try:\\n        return np.linalg.solve(EZZ, EZX @ b)\\n    except np.linalg.LinAlgError:\\n        return np.full(4, np.nan)\\n\\n\\n# ============================================================================\\n# DAG 3: COLLIDER  T -> A <- Y\\n# ============================================================================\\n\\nCOLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0,\\n                       dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)\\n\\n\\ndef precomp_collider(params=None, N=2_000_000, seed=999):\\n    if params is None:\\n        params = COLLIDER_PARAMS\\n    rng = np.random.default_rng(seed)\\n    T = rng.normal(0, 1, N)\\n    eps = rng.normal(0, 1, N)\\n    Y = params['tau'] * T + eps\\n    logits = np.column_stack([\\n        np.zeros(N),\\n        params['g1'] + params['dT'] * T + params['dY'] * Y,\\n        params['g2'] + params['dT2'] * T + params['dY2'] * Y,\\n    ])\\n    A = softmax_sample(logits, rng)\\n    K = 3\\n    DM = np.zeros((N, K))\\n    for k in range(K):\\n        DM[:, k] = (A == k).astype(float)\\n    return dict(\\n        E_T=T.mean(), E_T2=(T**2).mean(),\\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\\n        E_DM=DM.mean(0),\\n        E_DM_T=(DM * T[:, None]).mean(0),\\n        E_DM_Y=(DM * Y[:, None]).mean(0),\\n    )\\n\\n\\ndef plim_collider(C, precomp):\\n    ds = C @ precomp['E_DM']\\n    dst = C @ precomp['E_DM_T']\\n    dsy = C @ precomp['E_DM_Y']\\n    ET, ET2 = precomp['E_T'], precomp['E_T2']\\n    EY, ETY = precomp['E_Y'], precomp['E_TY']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GRUBpPq7K8vbzZTcCrrhnb`</summary>

```json
{
  "server": "home-1x5090",
  "command": "head -400 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "0c9d2a93-4ac0-479e-815b-a0c8b41c5e16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016E2KWPp96bf2sqgqcjwijP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 31012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
      },
      "output_tokens": 64,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PWvsi4R6MjLuwWEphUwhQ8`</summary>

```json
{
  "server": "home-1x5090",
  "command": "head -600 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "f87fe371-1db3-4700-929c-61ced8e6e361",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016E2KWPp96bf2sqgqcjwijP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 31012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
      },
      "output_tokens": 64,
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

_source line 18 · 2026-05-20T13:11:11.622Z_

<details><summary>↩ Tool result · `toolu_01GRUBpPq7K8vbzZTcCrrhnb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 5455 字符] ...\\n\\n01\\\": np.array([\\n            [0.70, 0.25, 0.05],\\n            [0.25, 0.70, 0.05],\\n            [0.05, 0.05, 0.90]]),\\n        \\\"one_weak\\\": np.array([\\n            [0.90, 0.05, 0.30],\\n            [0.05, 0.90, 0.30],\\n            [0.05, 0.05, 0.40]]),\\n        \\\"near_perfect\\\": np.array([\\n            [0.95, 0.025, 0.025],\\n            [0.025, 0.95, 0.025],\\n            [0.025, 0.025, 0.95]]),\\n        \\\"heavy_offdiag\\\": np.array([\\n            [0.50, 0.30, 0.20],\\n            [0.30, 0.50, 0.30],\\n            [0.20, 0.20, 0.50]]),\\n    }\\n\\n\\ndef random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):\\n    C = np.zeros((K, K))\\n    for k in range(K):\\n        alphas = np.full(K, offdiag_alpha)\\n        alphas[k] = diag_alpha\\n        C[:, k] = rng.dirichlet(alphas)\\n    return C\\n\\n\\n# ============================================================================\\n# DGP Data Generators (for MC)\\n# ============================================================================\\n\\ndef gen_confounding_data(N, p_A, alpha_val, beta_T, beta_A, sigma_T, C0, rng):\\n    A = rng.choice(len(p_A), size=N, p=p_A)\\n    T = rng.normal(sigma_T[A], 1.0)\\n    Y = alpha_val + beta_T * T + rng.normal(0, 1, N)\\n    for k in range(len(beta_A)):\\n        Y = Y + beta_A[k] * (A == k + 1).astype(float)\\n    Astar = generate_Astar(A, C0, rng)\\n    return T, Y, A, Astar\\n\\n\\ndef gen_mediation_data(N, beta, tau, C0, rng, gamma=GAMMA_MED, delta_coef=DELTA_MED):\\n    T = rng.binomial(1, 0.5, N).astype(float)\\n    logits = np.outer(T, delta_coef) + gamma[np.newaxis, :]\\n    A = softmax_sample(logits, rng)\\n    Y = beta[0] + tau * T + rng.normal(0, 1, N)\\n    for k in range(1, len(beta)):\\n        Y = Y + beta[k] * (A == k).astype(float)\\n    Astar = generate_Astar(A, C0, rng)\\n    return T, Y, A, Astar\\n\\n\\ndef gen_collider_data(N, params, C0, rng):\\n    T = rng.normal(0, 1, N)\\n    eps = rng.normal(0, 1, N)\\n    Y = params['tau'] * T + eps\\n    logits = np.column_stack([\\n        np.zeros(N),\\n        params['g1'] + params['dT'] * T + params['dY'] * Y,\\n        params['g2'] + params['dT2'] * T + params['dY2'] * Y,\\n    ])\\n    A = softmax_sample(logits, rng)\\n    Astar = generate_Astar(A, C0, rng)\\n    return T, Y, A, Astar\\n\\n\\n# ============================================================================\\n# Part 1: Verify Fixes\\n# ============================================================================\\n\\ndef part1_verify(st):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"PART 1: Verify delta_range fix + direction parameter\\\")\\n    print(\\\"=\\\" * 70)\\n\\n    param = LinearInterpolation()\\n    K = 3\\n\\n    C0_80 = np.array([[0.80, 0.10, 0.10],\\n                       [0.10, 0.80, 0.10],\\n                       [0.10, 0.10, 0.80]])\\n    C0_90 = np.array([[0.90, 0.05, 0.05],\\n                       [0.05, 0.90, 0.05],\\n                       [0.05, 0.05, 0.90]])\\n\\n    print(f\\\"  delta_range(None):     {param.delta_range(None)}\\\")\\n    print(f\\\"  delta_range(diag=0.8): {param.delta_range(C0_80)}  (expect ~5.0)\\\")\\n    print(f\\\"  delta_range(diag=0.9): {param.delta_range(C0_90)}  (expect ~10.0 capped)\\\")\\n\\n    _, dmax_80 = param.delta_range(C0_80)\\n    C_dmax = param(C0_80, dmax_80 - 0.01)\\n    check_column_stochastic(C_dmax)\\n    print(f\\\"  C(delta_max-0.01) column-stochastic OK\\\")\\n\\n    C_2 = param(C0_80, 2.0)\\n    check_column_stochastic(C_2)\\n    print(f\\\"  C(delta=2.0) column-stochastic OK, diag={np.diag(C_2)}\\\")\\n\\n    rng = np.random.default_rng(42)\\n    U = rng.dirichlet(np.ones(K), size=K).T\\n    C0_test = 0.8 * np.eye(K) + 0.2 * U\\n    C0_test = C0_test / C0_test.sum(axis=0)\\n    drange_test = param.delta_range(C0_test)\\n    print(f\\\"  C0=0.8I+0.2U: diag={np.diag(C0_test).round(3)}, delta_range={drange_test}\\\")\\n\\n    for d in [0, 0.5, 1.0, 2.0, 3.0, min(4.5, drange_test[1] - 0.01)]:\\n        C_d = param(C0_test, d)\\n        check_column_stochastic(C_d)\\n    print(f\\\"  All tested deltas column-stochastic OK\\\")\\n\\n    # Test compute_asv with extended range (confounding, vulnerability)\\n    p_A = np.array([0.4, 0.35, 0.25])\\n    alpha_cf = 0.5; beta_T = 1.0\\n    beta_A = np.array([0.8, -0.3])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.03}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "22ecab85-1d0b-4e2f-a95b-4b5bf1e32db4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nplan_004: ASV Framework v2\\\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\\\n\\\\n双方向:\\\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport time\\\\nfrom abc import ABC, abstractmethod\\\\n\\\\n\\\\n# ============================================================================\\\\n# Utilities\\\\n# ============================================================================\\\\n\\\\ndef softmax(x):\\\\n    e = np.exp(x - x.max())\\\\n    return e / e.sum()\\\\n\\\\n\\\\ndef p_cat(t, g, d):\\\\n    return softmax(g + d * t)\\\\n\\\\n\\\\ndef generate_Astar(A, C, rng):\\\\n    probs = C[:, A]\\\\n    cum = np.cumsum(probs, axis=0)\\\\n    u = rng.uniform(size=len(A))\\\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\\\n\\\\n\\\\ndef softmax_sample(logits, rng):\\\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\\\n    cum = np.cumsum(probs, axis=1)\\\\n    u = rng.uniform(size=logits.shape[0])\\\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\\\n\\\\n\\\\ndef check_column_stochastic(C, tol=1e-6):\\\\n    assert np.all(C >= -tol), f\\\\\\\"Negative entries in C: min={C.min()}\\\\\\\"\\\\n    col_sums = C.sum(axis=0)\\\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\\\\\"Column sums != 1: {col_sums}\\\\\\\"\\\\n\\\\n\\\\ndef ols_with_dummies(Y, T, Astar, K=3):\\\\n    N = len(Y)\\\\n    D = np.zeros((N, K - 1))\\\\n    for k in range(1, K):\\\\n        D[:, k - 1] = (Astar == k).astype(float)\\\\n    X = np.column_stack([np.ones(N), T, D])\\\\n    try:\\\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\\\n        resid = Y - X @ beta\\\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\\\n        XtX_inv = np.linalg.inv(X.T @ X)\\\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\\\n    except np.linalg.LinAlgError:\\\\n        beta = np.full(X.shape[1], np.nan)\\\\n        se = np.full(X.shape[1], np.nan)\\\\n    return beta, se\\\\n\\\\n\\\\n# ============================================================================\\\\n# C(delta) Parameterization\\\\n# ============================================================================\\\\n\\\\nclass ConfusionParameterization(ABC):\\\\n    @abstractmethod\\\\n    def __call__(self, C0, delta):\\\\n        pass\\\\n\\\\n    @abstractmethod\\\\n    def delta_range(self, C0=None):\\\\n        pass\\\\n\\\\n\\\\nclass LinearInterpolation(ConfusionParameterization):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\n    def __call__(self, C0, delta):\\\\n        K = C0.shape[0]\\\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\\\n        C_d = np.maximum(C_d, 0.0)\\\\n        col_sums = C_d.sum(axis=0)\\\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\\\n        C_d = C_d / col_sums\\\\n        return C_d\\\\n\\\\n    def delta_range(self, C0=None):\\\\n        if C0 is None:\\\\n            return (0.0, 5.0)\\\\n        min_diag = np.diag(C0).min()\\\\n        if min_diag >= 1.0:\\\\n            return (0.0, 10.0)\\\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\\\n        return (0.0, delta_max)\\\\n\\\\n\\\\n# ============================================================================\\\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\\\n# ============================================================================\\\\n\\\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\\\n    mu = sigma_T\\\\n    ET = np.sum(p_A * mu)\\\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\\\n    q = C @ p_A\\\\n    qt = C @ (p_A * mu)\\\\n    EZZ = np.array([\\\\n        [1,    ET,    q[1],   q[2]  ],\\\\n        [ET,   ET2,   qt[1],  qt[2] ],\\\\n        [q[1], qt[1], q[1],   0     ],\\\\n        [q[2], qt[2], 0,      q[2]  ]])\\\\n    EZX = np.array([\\\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\\\n    try:\\\\n        retur\\\\n\\\\n... [截断: 输出过长，省略 5455 字符] ...\\\\n\\\\n01\\\\\\\": np.array([\\\\n            [0.70, 0.25, 0.05],\\\\n            [0.25, 0.70, 0.05],\\\\n            [0.05, 0.05, 0.90]]),\\\\n        \\\\\\\"one_weak\\\\\\\": np.array([\\\\n            [0.90, 0.05, 0.30],\\\\n            [0.05, 0.90, 0.30],\\\\n            [0.05, 0.05, 0.40]]),\\\\n        \\\\\\\"near_perfect\\\\\\\": np.array([\\\\n            [0.95, 0.025, 0.025],\\\\n            [0.025, 0.95, 0.025],\\\\n            [0.025, 0.025, 0.95]]),\\\\n        \\\\\\\"heavy_offdiag\\\\\\\": np.array([\\\\n            [0.50, 0.30, 0.20],\\\\n            [0.30, 0.50, 0.30],\\\\n            [0.20, 0.20, 0.50]]),\\\\n    }\\\\n\\\\n\\\\ndef random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):\\\\n    C = np.zeros((K, K))\\\\n    for k in range(K):\\\\n        alphas = np.full(K, offdiag_alpha)\\\\n        alphas[k] = diag_alpha\\\\n        C[:, k] = rng.dirichlet(alphas)\\\\n    return C\\\\n\\\\n\\\\n# ============================================================================\\\\n# DGP Data Generators (for MC)\\\\n# ============================================================================\\\\n\\\\ndef gen_confounding_data(N, p_A, alpha_val, beta_T, beta_A, sigma_T, C0, rng):\\\\n    A = rng.choice(len(p_A), size=N, p=p_A)\\\\n    T = rng.normal(sigma_T[A], 1.0)\\\\n    Y = alpha_val + beta_T * T + rng.normal(0, 1, N)\\\\n    for k in range(len(beta_A)):\\\\n        Y = Y + beta_A[k] * (A == k + 1).astype(float)\\\\n    Astar = generate_Astar(A, C0, rng)\\\\n    return T, Y, A, Astar\\\\n\\\\n\\\\ndef gen_mediation_data(N, beta, tau, C0, rng, gamma=GAMMA_MED, delta_coef=DELTA_MED):\\\\n    T = rng.binomial(1, 0.5, N).astype(float)\\\\n    logits = np.outer(T, delta_coef) + gamma[np.newaxis, :]\\\\n    A = softmax_sample(logits, rng)\\\\n    Y = beta[0] + tau * T + rng.normal(0, 1, N)\\\\n    for k in range(1, len(beta)):\\\\n        Y = Y + beta[k] * (A == k).astype(float)\\\\n    Astar = generate_Astar(A, C0, rng)\\\\n    return T, Y, A, Astar\\\\n\\\\n\\\\ndef gen_collider_data(N, params, C0, rng):\\\\n    T = rng.normal(0, 1, N)\\\\n    eps = rng.normal(0, 1, N)\\\\n    Y = params['tau'] * T + eps\\\\n    logits = np.column_stack([\\\\n        np.zeros(N),\\\\n        params['g1'] + params['dT'] * T + params['dY'] * Y,\\\\n        params['g2'] + params['dT2'] * T + params['dY2'] * Y,\\\\n    ])\\\\n    A = softmax_sample(logits, rng)\\\\n    Astar = generate_Astar(A, C0, rng)\\\\n    return T, Y, A, Astar\\\\n\\\\n\\\\n# ============================================================================\\\\n# Part 1: Verify Fixes\\\\n# ============================================================================\\\\n\\\\ndef part1_verify(st):\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    print(\\\\\\\"PART 1: Verify delta_range fix + direction parameter\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n\\\\n    param = LinearInterpolation()\\\\n    K = 3\\\\n\\\\n    C0_80 = np.array([[0.80, 0.10, 0.10],\\\\n                       [0.10, 0.80, 0.10],\\\\n                       [0.10, 0.10, 0.80]])\\\\n    C0_90 = np.array([[0.90, 0.05, 0.05],\\\\n                       [0.05, 0.90, 0.05],\\\\n                       [0.05, 0.05, 0.90]])\\\\n\\\\n    print(f\\\\\\\"  delta_range(None):     {param.delta_range(None)}\\\\\\\")\\\\n    print(f\\\\\\\"  delta_range(diag=0.8): {param.delta_range(C0_80)}  (expect ~5.0)\\\\\\\")\\\\n    print(f\\\\\\\"  delta_range(diag=0.9): {param.delta_range(C0_90)}  (expect ~10.0 capped)\\\\\\\")\\\\n\\\\n    _, dmax_80 = param.delta_range(C0_80)\\\\n    C_dmax = param(C0_80, dmax_80 - 0.01)\\\\n    check_column_stochastic(C_dmax)\\\\n    print(f\\\\\\\"  C(delta_max-0.01) column-stochastic OK\\\\\\\")\\\\n\\\\n    C_2 = param(C0_80, 2.0)\\\\n    check_column_stochastic(C_2)\\\\n    print(f\\\\\\\"  C(delta=2.0) column-stochastic OK, diag={np.diag(C_2)}\\\\\\\")\\\\n\\\\n    rng = np.random.default_rng(42)\\\\n    U = rng.dirichlet(np.ones(K), size=K).T\\\\n    C0_test = 0.8 * np.eye(K) + 0.2 * U\\\\n    C0_test = C0_test / C0_test.sum(axis=0)\\\\n    drange_test = param.delta_range(C0_test)\\\\n    print(f\\\\\\\"  C0=0.8I+0.2U: diag={np.diag(C0_test).round(3)}, delta_range={drange_test}\\\\\\\")\\\\n\\\\n    for d in [0, 0.5, 1.0, 2.0, 3.0, min(4.5, drange_test[1] - 0.01)]:\\\\n        C_d = param(C0_test, d)\\\\n        check_column_stochastic(C_d)\\\\n    print(f\\\\\\\"  All tested deltas column-stochastic OK\\\\\\\")\\\\n\\\\n    # Test compute_asv with extended range (confounding, vulnerability)\\\\n    p_A = np.array([0.4, 0.35, 0.25])\\\\n    alpha_cf = 0.5; beta_T = 1.0\\\\n    beta_A = np.array([0.8, -0.3])\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.03}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 5455 字符] ...\\n\\n01\\\": np.array([\\n            [0.70, 0.25, 0.05],\\n            [0.25, 0.70, 0.05],\\n            [0.05, 0.05, 0.90]]),\\n        \\\"one_weak\\\": np.array([\\n            [0.90, 0.05, 0.30],\\n            [0.05, 0.90, 0.30],\\n            [0.05, 0.05, 0.40]]),\\n        \\\"near_perfect\\\": np.array([\\n            [0.95, 0.025, 0.025],\\n            [0.025, 0.95, 0.025],\\n            [0.025, 0.025, 0.95]]),\\n        \\\"heavy_offdiag\\\": np.array([\\n            [0.50, 0.30, 0.20],\\n            [0.30, 0.50, 0.30],\\n            [0.20, 0.20, 0.50]]),\\n    }\\n\\n\\ndef random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):\\n    C = np.zeros((K, K))\\n    for k in range(K):\\n        alphas = np.full(K, offdiag_alpha)\\n        alphas[k] = diag_alpha\\n        C[:, k] = rng.dirichlet(alphas)\\n    return C\\n\\n\\n# ============================================================================\\n# DGP Data Generators (for MC)\\n# ============================================================================\\n\\ndef gen_confounding_data(N, p_A, alpha_val, beta_T, beta_A, sigma_T, C0, rng):\\n    A = rng.choice(len(p_A), size=N, p=p_A)\\n    T = rng.normal(sigma_T[A], 1.0)\\n    Y = alpha_val + beta_T * T + rng.normal(0, 1, N)\\n    for k in range(len(beta_A)):\\n        Y = Y + beta_A[k] * (A == k + 1).astype(float)\\n    Astar = generate_Astar(A, C0, rng)\\n    return T, Y, A, Astar\\n\\n\\ndef gen_mediation_data(N, beta, tau, C0, rng, gamma=GAMMA_MED, delta_coef=DELTA_MED):\\n    T = rng.binomial(1, 0.5, N).astype(float)\\n    logits = np.outer(T, delta_coef) + gamma[np.newaxis, :]\\n    A = softmax_sample(logits, rng)\\n    Y = beta[0] + tau * T + rng.normal(0, 1, N)\\n    for k in range(1, len(beta)):\\n        Y = Y + beta[k] * (A == k).astype(float)\\n    Astar = generate_Astar(A, C0, rng)\\n    return T, Y, A, Astar\\n\\n\\ndef gen_collider_data(N, params, C0, rng):\\n    T = rng.normal(0, 1, N)\\n    eps = rng.normal(0, 1, N)\\n    Y = params['tau'] * T + eps\\n    logits = np.column_stack([\\n        np.zeros(N),\\n        params['g1'] + params['dT'] * T + params['dY'] * Y,\\n        params['g2'] + params['dT2'] * T + params['dY2'] * Y,\\n    ])\\n    A = softmax_sample(logits, rng)\\n    Astar = generate_Astar(A, C0, rng)\\n    return T, Y, A, Astar\\n\\n\\n# ============================================================================\\n# Part 1: Verify Fixes\\n# ============================================================================\\n\\ndef part1_verify(st):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"PART 1: Verify delta_range fix + direction parameter\\\")\\n    print(\\\"=\\\" * 70)\\n\\n    param = LinearInterpolation()\\n    K = 3\\n\\n    C0_80 = np.array([[0.80, 0.10, 0.10],\\n                       [0.10, 0.80, 0.10],\\n                       [0.10, 0.10, 0.80]])\\n    C0_90 = np.array([[0.90, 0.05, 0.05],\\n                       [0.05, 0.90, 0.05],\\n                       [0.05, 0.05, 0.90]])\\n\\n    print(f\\\"  delta_range(None):     {param.delta_range(None)}\\\")\\n    print(f\\\"  delta_range(diag=0.8): {param.delta_range(C0_80)}  (expect ~5.0)\\\")\\n    print(f\\\"  delta_range(diag=0.9): {param.delta_range(C0_90)}  (expect ~10.0 capped)\\\")\\n\\n    _, dmax_80 = param.delta_range(C0_80)\\n    C_dmax = param(C0_80, dmax_80 - 0.01)\\n    check_column_stochastic(C_dmax)\\n    print(f\\\"  C(delta_max-0.01) column-stochastic OK\\\")\\n\\n    C_2 = param(C0_80, 2.0)\\n    check_column_stochastic(C_2)\\n    print(f\\\"  C(delta=2.0) column-stochastic OK, diag={np.diag(C_2)}\\\")\\n\\n    rng = np.random.default_rng(42)\\n    U = rng.dirichlet(np.ones(K), size=K).T\\n    C0_test = 0.8 * np.eye(K) + 0.2 * U\\n    C0_test = C0_test / C0_test.sum(axis=0)\\n    drange_test = param.delta_range(C0_test)\\n    print(f\\\"  C0=0.8I+0.2U: diag={np.diag(C0_test).round(3)}, delta_range={drange_test}\\\")\\n\\n    for d in [0, 0.5, 1.0, 2.0, 3.0, min(4.5, drange_test[1] - 0.01)]:\\n        C_d = param(C0_test, d)\\n        check_column_stochastic(C_d)\\n    print(f\\\"  All tested deltas column-stochastic OK\\\")\\n\\n    # Test compute_asv with extended range (confounding, vulnerability)\\n    p_A = np.array([0.4, 0.35, 0.25])\\n    alpha_cf = 0.5; beta_T = 1.0\\n    beta_A = np.array([0.8, -0.3])\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.03}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GdWUNtK4Q8CavX8UCJfhbu`</summary>

```json
{
  "server": "home-1x5090",
  "command": "tail -273 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "8f650371-58d6-41e6-b485-664c254ef3d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016E2KWPp96bf2sqgqcjwijP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 31012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
      },
      "output_tokens": 64,
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

_source line 20 · 2026-05-20T13:11:12.744Z_

<details><summary>↩ Tool result · `toolu_01PWvsi4R6MjLuwWEphUwhQ8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 13723 字符] ...\\n\\nx, n_delta)\\n\\n        # Confounding: |bias| should increase\\n        tau_cf = np.array([plim_confounding(param(C0, d), p_A, alpha_cf,\\n                           beta_T, beta_A, sigma_T)[1] for d in deltas])\\n        bias_cf = np.abs(tau_cf - beta_T)\\n        diffs_cf = np.diff(bias_cf)\\n        if np.any(diffs_cf < -1e-8):\\n            violations[\\\"confounding\\\"].append((s, np.min(diffs_cf)))\\n\\n        # Mediation: |bias| should increase\\n        tau_m = np.array([plim_mediation(param(C0, d), beta_med, tau_med)[1]\\n                          for d in deltas])\\n        bias_m = np.abs(tau_m - tau_med)\\n        diffs_m = np.diff(bias_m)\\n        if np.any(diffs_m < -1e-8):\\n            violations[\\\"mediation\\\"].append((s, np.min(diffs_m)))\\n\\n        # Collider: |collider_bias| should decrease\\n        tau_c = np.array([plim_collider(param(C0, d), st)[1] for d in deltas])\\n        bias_c = np.abs(tau_c - tau_true_col)\\n        diffs_c = np.diff(bias_c)\\n        if np.any(diffs_c > 1e-8):\\n            violations[\\\"collider\\\"].append((s, np.max(diffs_c)))\\n\\n        if (s + 1) % 200 == 0:\\n            print(f\\\"  ... {s+1}/{n_C0}\\\")\\n\\n    for topo in [\\\"confounding\\\", \\\"mediation\\\", \\\"collider\\\"]:\\n        v = violations[topo]\\n        direction = \\\"increasing\\\" if topo != \\\"collider\\\" else \\\"decreasing\\\"\\n        print(f\\\"  {topo}: {len(v)}/{n_C0} violations (expected |bias| {direction})\\\")\\n        if v:\\n            worst = max(v, key=lambda x: abs(x[1]))\\n            print(f\\\"    worst: scenario {worst[0]}, max|delta_bias|={worst[1]:.2e}\\\")\\n\\n    print(f\\\"  Time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Part 4: Sharpness Verification\\n# ============================================================================\\n\\ndef part4_sharpness(st):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"PART 4: Sharpness -- ASV bound is tight\\\")\\n    print(\\\"=\\\" * 70)\\n\\n    param = LinearInterpolation()\\n\\n    p_A = np.array([0.4, 0.35, 0.25])\\n    alpha_cf = 0.5; beta_T = 1.0\\n    beta_A = np.array([0.8, -0.3])\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\n    tau_true_col = COLLIDER_PARAMS['tau']\\n\\n    structures = make_named_C_structures()\\n\\n    configs = [\\n        (\\\"confounding\\\", plim_confounding,\\n         dict(p_A=p_A, alpha=alpha_cf, beta_T=beta_T, beta_A=beta_A, sigma_T=sigma_T),\\n         \\\"vulnerability\\\", None),\\n        (\\\"mediation\\\", plim_mediation,\\n         dict(beta=beta_med, tau=tau_med), \\\"vulnerability\\\", None),\\n        (\\\"collider\\\", plim_collider,\\n         dict(precomp=st), \\\"protection\\\", tau_true_col),\\n    ]\\n\\n    print(f\\\"\\\\n{'C_struct':<16} {'Topology':<12} {'ASV':>8} {'tau(ASV-e)':>11} {'tau(ASV+e)':>11} {'tau_base':>10}\\\")\\n    print(\\\"-\\\" * 74)\\n\\n    for name, C0 in structures.items():\\n        for topo, plim_func, kwargs, direction, tau_true in configs:\\n            r = compute_asv(plim_func, kwargs, C0, param,\\n                            direction=direction, tau_true=tau_true, n_grid=5000)\\n            asv = r['asv']\\n            if asv is not None and asv > 0.001:\\n                step = r['deltas'][1] - r['deltas'][0]\\n                idx = np.searchsorted(r['deltas'], asv)\\n                tau_before = r['tau_curve'][max(idx - 1, 0)]\\n                tau_after = r['tau_curve'][min(idx + 1, len(r['tau_curve']) - 1)]\\n                print(f\\\"{name:<16} {topo:<12} {asv:>8.3f} {tau_before:>11.5f} {tau_after:>11.5f} {r['tau_baseline']:>10.5f}\\\")\\n            else:\\n                asv_s = f\\\"{asv:.3f}\\\" if asv is not None else \\\"None\\\"\\n                print(f\\\"{name:<16} {topo:<12} {asv_s:>8} {'---':>11} {'---':>11} {r['tau_baseline']:>10.5f}\\\")\\n\\n\\n# ============================================================================\\n# Part 5: MC Coverage\\n# ============================================================================\\n\\ndef part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(f\\\"PART 5: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})\\\")\\n    print(\\\"=\\\" * 70)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "544ae261-88ca-48a7-b8cb-edb06fafacfb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nplan_004: ASV Framework v2\\\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\\\n\\\\n双方向:\\\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport time\\\\nfrom abc import ABC, abstractmethod\\\\n\\\\n\\\\n# ============================================================================\\\\n# Utilities\\\\n# ============================================================================\\\\n\\\\ndef softmax(x):\\\\n    e = np.exp(x - x.max())\\\\n    return e / e.sum()\\\\n\\\\n\\\\ndef p_cat(t, g, d):\\\\n    return softmax(g + d * t)\\\\n\\\\n\\\\ndef generate_Astar(A, C, rng):\\\\n    probs = C[:, A]\\\\n    cum = np.cumsum(probs, axis=0)\\\\n    u = rng.uniform(size=len(A))\\\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\\\n\\\\n\\\\ndef softmax_sample(logits, rng):\\\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\\\n    cum = np.cumsum(probs, axis=1)\\\\n    u = rng.uniform(size=logits.shape[0])\\\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\\\n\\\\n\\\\ndef check_column_stochastic(C, tol=1e-6):\\\\n    assert np.all(C >= -tol), f\\\\\\\"Negative entries in C: min={C.min()}\\\\\\\"\\\\n    col_sums = C.sum(axis=0)\\\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\\\\\"Column sums != 1: {col_sums}\\\\\\\"\\\\n\\\\n\\\\ndef ols_with_dummies(Y, T, Astar, K=3):\\\\n    N = len(Y)\\\\n    D = np.zeros((N, K - 1))\\\\n    for k in range(1, K):\\\\n        D[:, k - 1] = (Astar == k).astype(float)\\\\n    X = np.column_stack([np.ones(N), T, D])\\\\n    try:\\\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\\\n        resid = Y - X @ beta\\\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\\\n        XtX_inv = np.linalg.inv(X.T @ X)\\\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\\\n    except np.linalg.LinAlgError:\\\\n        beta = np.full(X.shape[1], np.nan)\\\\n        se = np.full(X.shape[1], np.nan)\\\\n    return beta, se\\\\n\\\\n\\\\n# ============================================================================\\\\n# C(delta) Parameterization\\\\n# ============================================================================\\\\n\\\\nclass ConfusionParameterization(ABC):\\\\n    @abstractmethod\\\\n    def __call__(self, C0, delta):\\\\n        pass\\\\n\\\\n    @abstractmethod\\\\n    def delta_range(self, C0=None):\\\\n        pass\\\\n\\\\n\\\\nclass LinearInterpolation(ConfusionParameterization):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\n    def __call__(self, C0, delta):\\\\n        K = C0.shape[0]\\\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\\\n        C_d = np.maximum(C_d, 0.0)\\\\n        col_sums = C_d.sum(axis=0)\\\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\\\n        C_d = C_d / col_sums\\\\n        return C_d\\\\n\\\\n    def delta_range(self, C0=None):\\\\n        if C0 is None:\\\\n            return (0.0, 5.0)\\\\n        min_diag = np.diag(C0).min()\\\\n        if min_diag >= 1.0:\\\\n            return (0.0, 10.0)\\\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\\\n        return (0.0, delta_max)\\\\n\\\\n\\\\n# ============================================================================\\\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\\\n# ============================================================================\\\\n\\\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\\\n    mu = sigma_T\\\\n    ET = np.sum(p_A * mu)\\\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\\\n    q = C @ p_A\\\\n    qt = C @ (p_A * mu)\\\\n    EZZ = np.array([\\\\n        [1,    ET,    q[1],   q[2]  ],\\\\n        [ET,   ET2,   qt[1],  qt[2] ],\\\\n        [q[1], qt[1], q[1],   0     ],\\\\n        [q[2], qt[2], 0,      q[2]  ]])\\\\n    EZX = np.array([\\\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\\\n    try:\\\\n        retur\\\\n\\\\n... [截断: 输出过长，省略 13723 字符] ...\\\\n\\\\nx, n_delta)\\\\n\\\\n        # Confounding: |bias| should increase\\\\n        tau_cf = np.array([plim_confounding(param(C0, d), p_A, alpha_cf,\\\\n                           beta_T, beta_A, sigma_T)[1] for d in deltas])\\\\n        bias_cf = np.abs(tau_cf - beta_T)\\\\n        diffs_cf = np.diff(bias_cf)\\\\n        if np.any(diffs_cf < -1e-8):\\\\n            violations[\\\\\\\"confounding\\\\\\\"].append((s, np.min(diffs_cf)))\\\\n\\\\n        # Mediation: |bias| should increase\\\\n        tau_m = np.array([plim_mediation(param(C0, d), beta_med, tau_med)[1]\\\\n                          for d in deltas])\\\\n        bias_m = np.abs(tau_m - tau_med)\\\\n        diffs_m = np.diff(bias_m)\\\\n        if np.any(diffs_m < -1e-8):\\\\n            violations[\\\\\\\"mediation\\\\\\\"].append((s, np.min(diffs_m)))\\\\n\\\\n        # Collider: |collider_bias| should decrease\\\\n        tau_c = np.array([plim_collider(param(C0, d), st)[1] for d in deltas])\\\\n        bias_c = np.abs(tau_c - tau_true_col)\\\\n        diffs_c = np.diff(bias_c)\\\\n        if np.any(diffs_c > 1e-8):\\\\n            violations[\\\\\\\"collider\\\\\\\"].append((s, np.max(diffs_c)))\\\\n\\\\n        if (s + 1) % 200 == 0:\\\\n            print(f\\\\\\\"  ... {s+1}/{n_C0}\\\\\\\")\\\\n\\\\n    for topo in [\\\\\\\"confounding\\\\\\\", \\\\\\\"mediation\\\\\\\", \\\\\\\"collider\\\\\\\"]:\\\\n        v = violations[topo]\\\\n        direction = \\\\\\\"increasing\\\\\\\" if topo != \\\\\\\"collider\\\\\\\" else \\\\\\\"decreasing\\\\\\\"\\\\n        print(f\\\\\\\"  {topo}: {len(v)}/{n_C0} violations (expected |bias| {direction})\\\\\\\")\\\\n        if v:\\\\n            worst = max(v, key=lambda x: abs(x[1]))\\\\n            print(f\\\\\\\"    worst: scenario {worst[0]}, max|delta_bias|={worst[1]:.2e}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"  Time: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n\\\\n# ============================================================================\\\\n# Part 4: Sharpness Verification\\\\n# ============================================================================\\\\n\\\\ndef part4_sharpness(st):\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    print(\\\\\\\"PART 4: Sharpness -- ASV bound is tight\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n\\\\n    param = LinearInterpolation()\\\\n\\\\n    p_A = np.array([0.4, 0.35, 0.25])\\\\n    alpha_cf = 0.5; beta_T = 1.0\\\\n    beta_A = np.array([0.8, -0.3])\\\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\\\n    tau_true_col = COLLIDER_PARAMS['tau']\\\\n\\\\n    structures = make_named_C_structures()\\\\n\\\\n    configs = [\\\\n        (\\\\\\\"confounding\\\\\\\", plim_confounding,\\\\n         dict(p_A=p_A, alpha=alpha_cf, beta_T=beta_T, beta_A=beta_A, sigma_T=sigma_T),\\\\n         \\\\\\\"vulnerability\\\\\\\", None),\\\\n        (\\\\\\\"mediation\\\\\\\", plim_mediation,\\\\n         dict(beta=beta_med, tau=tau_med), \\\\\\\"vulnerability\\\\\\\", None),\\\\n        (\\\\\\\"collider\\\\\\\", plim_collider,\\\\n         dict(precomp=st), \\\\\\\"protection\\\\\\\", tau_true_col),\\\\n    ]\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n{'C_struct':<16} {'Topology':<12} {'ASV':>8} {'tau(ASV-e)':>11} {'tau(ASV+e)':>11} {'tau_base':>10}\\\\\\\")\\\\n    print(\\\\\\\"-\\\\\\\" * 74)\\\\n\\\\n    for name, C0 in structures.items():\\\\n        for topo, plim_func, kwargs, direction, tau_true in configs:\\\\n            r = compute_asv(plim_func, kwargs, C0, param,\\\\n                            direction=direction, tau_true=tau_true, n_grid=5000)\\\\n            asv = r['asv']\\\\n            if asv is not None and asv > 0.001:\\\\n                step = r['deltas'][1] - r['deltas'][0]\\\\n                idx = np.searchsorted(r['deltas'], asv)\\\\n                tau_before = r['tau_curve'][max(idx - 1, 0)]\\\\n                tau_after = r['tau_curve'][min(idx + 1, len(r['tau_curve']) - 1)]\\\\n                print(f\\\\\\\"{name:<16} {topo:<12} {asv:>8.3f} {tau_before:>11.5f} {tau_after:>11.5f} {r['tau_baseline']:>10.5f}\\\\\\\")\\\\n            else:\\\\n                asv_s = f\\\\\\\"{asv:.3f}\\\\\\\" if asv is not None else \\\\\\\"None\\\\\\\"\\\\n                print(f\\\\\\\"{name:<16} {topo:<12} {asv_s:>8} {'---':>11} {'---':>11} {r['tau_baseline']:>10.5f}\\\\\\\")\\\\n\\\\n\\\\n# ============================================================================\\\\n# Part 5: MC Coverage\\\\n# ============================================================================\\\\n\\\\ndef part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100):\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    print(f\\\\\\\"PART 5: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.11}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 13723 字符] ...\\n\\nx, n_delta)\\n\\n        # Confounding: |bias| should increase\\n        tau_cf = np.array([plim_confounding(param(C0, d), p_A, alpha_cf,\\n                           beta_T, beta_A, sigma_T)[1] for d in deltas])\\n        bias_cf = np.abs(tau_cf - beta_T)\\n        diffs_cf = np.diff(bias_cf)\\n        if np.any(diffs_cf < -1e-8):\\n            violations[\\\"confounding\\\"].append((s, np.min(diffs_cf)))\\n\\n        # Mediation: |bias| should increase\\n        tau_m = np.array([plim_mediation(param(C0, d), beta_med, tau_med)[1]\\n                          for d in deltas])\\n        bias_m = np.abs(tau_m - tau_med)\\n        diffs_m = np.diff(bias_m)\\n        if np.any(diffs_m < -1e-8):\\n            violations[\\\"mediation\\\"].append((s, np.min(diffs_m)))\\n\\n        # Collider: |collider_bias| should decrease\\n        tau_c = np.array([plim_collider(param(C0, d), st)[1] for d in deltas])\\n        bias_c = np.abs(tau_c - tau_true_col)\\n        diffs_c = np.diff(bias_c)\\n        if np.any(diffs_c > 1e-8):\\n            violations[\\\"collider\\\"].append((s, np.max(diffs_c)))\\n\\n        if (s + 1) % 200 == 0:\\n            print(f\\\"  ... {s+1}/{n_C0}\\\")\\n\\n    for topo in [\\\"confounding\\\", \\\"mediation\\\", \\\"collider\\\"]:\\n        v = violations[topo]\\n        direction = \\\"increasing\\\" if topo != \\\"collider\\\" else \\\"decreasing\\\"\\n        print(f\\\"  {topo}: {len(v)}/{n_C0} violations (expected |bias| {direction})\\\")\\n        if v:\\n            worst = max(v, key=lambda x: abs(x[1]))\\n            print(f\\\"    worst: scenario {worst[0]}, max|delta_bias|={worst[1]:.2e}\\\")\\n\\n    print(f\\\"  Time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Part 4: Sharpness Verification\\n# ============================================================================\\n\\ndef part4_sharpness(st):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"PART 4: Sharpness -- ASV bound is tight\\\")\\n    print(\\\"=\\\" * 70)\\n\\n    param = LinearInterpolation()\\n\\n    p_A = np.array([0.4, 0.35, 0.25])\\n    alpha_cf = 0.5; beta_T = 1.0\\n    beta_A = np.array([0.8, -0.3])\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\n    tau_true_col = COLLIDER_PARAMS['tau']\\n\\n    structures = make_named_C_structures()\\n\\n    configs = [\\n        (\\\"confounding\\\", plim_confounding,\\n         dict(p_A=p_A, alpha=alpha_cf, beta_T=beta_T, beta_A=beta_A, sigma_T=sigma_T),\\n         \\\"vulnerability\\\", None),\\n        (\\\"mediation\\\", plim_mediation,\\n         dict(beta=beta_med, tau=tau_med), \\\"vulnerability\\\", None),\\n        (\\\"collider\\\", plim_collider,\\n         dict(precomp=st), \\\"protection\\\", tau_true_col),\\n    ]\\n\\n    print(f\\\"\\\\n{'C_struct':<16} {'Topology':<12} {'ASV':>8} {'tau(ASV-e)':>11} {'tau(ASV+e)':>11} {'tau_base':>10}\\\")\\n    print(\\\"-\\\" * 74)\\n\\n    for name, C0 in structures.items():\\n        for topo, plim_func, kwargs, direction, tau_true in configs:\\n            r = compute_asv(plim_func, kwargs, C0, param,\\n                            direction=direction, tau_true=tau_true, n_grid=5000)\\n            asv = r['asv']\\n            if asv is not None and asv > 0.001:\\n                step = r['deltas'][1] - r['deltas'][0]\\n                idx = np.searchsorted(r['deltas'], asv)\\n                tau_before = r['tau_curve'][max(idx - 1, 0)]\\n                tau_after = r['tau_curve'][min(idx + 1, len(r['tau_curve']) - 1)]\\n                print(f\\\"{name:<16} {topo:<12} {asv:>8.3f} {tau_before:>11.5f} {tau_after:>11.5f} {r['tau_baseline']:>10.5f}\\\")\\n            else:\\n                asv_s = f\\\"{asv:.3f}\\\" if asv is not None else \\\"None\\\"\\n                print(f\\\"{name:<16} {topo:<12} {asv_s:>8} {'---':>11} {'---':>11} {r['tau_baseline']:>10.5f}\\\")\\n\\n\\n# ============================================================================\\n# Part 5: MC Coverage\\n# ============================================================================\\n\\ndef part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(f\\\"PART 5: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})\\\")\\n    print(\\\"=\\\" * 70)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T13:11:13.994Z_

<details><summary>↩ Tool result · `toolu_01GdWUNtK4Q8CavX8UCJfhbu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    t0 = time.time()\\n\\n    rng = np.random.default_rng(42)\\n    K = 3\\n\\n    # --- Confounding ---\\n    print(\\\"\\\\n  [Confounding]\\\")\\n    plim_ok = 0; bias_ok = 0\\n\\n    for s in range(n_scenarios):\\n        C0 = random_C0(K, rng)\\n        p_A = rng.dirichlet(np.ones(K) * 2)\\n        tau = rng.uniform(0.2, 2.0) * rng.choice([-1, 1])\\n        bA = rng.normal(0, 0.5, K - 1)\\n        sT = rng.normal(0, 0.5, K)\\n        a_val = rng.normal(0, 0.5)\\n\\n        tau_plim = plim_confounding(C0, p_A, a_val, tau, bA, sT)[1]\\n        bias_theory = abs(tau_plim - tau)\\n\\n        tau_mc = np.zeros(reps)\\n        for r in range(reps):\\n            Td, Yd, _, Asd = gen_confounding_data(N_mc, p_A, a_val, tau, bA, sT, C0, rng)\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\n            tau_mc[r] = bh[1]\\n\\n        mc_mean = tau_mc.mean()\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\n\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\n            plim_ok += 1\\n        if abs(mc_mean - tau) <= bias_theory + 3 * mc_se + 0.02:\\n            bias_ok += 1\\n\\n        if (s + 1) % 100 == 0:\\n            print(f\\\"    ... {s+1}/{n_scenarios}\\\")\\n\\n    print(f\\\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\\\")\\n    print(f\\\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\\\")\\n\\n    # --- Mediation ---\\n    print(\\\"\\\\n  [Mediation]\\\")\\n    plim_ok_m = 0; bias_ok_m = 0\\n\\n    for s in range(n_scenarios):\\n        C0 = random_C0(K, rng)\\n        tau = rng.uniform(0.2, 2.0) * rng.choice([-1, 1])\\n        beta = np.array([rng.normal(0, 0.5), rng.normal(0, 1), rng.normal(0, 1)])\\n\\n        tau_plim = plim_mediation(C0, beta, tau)[1]\\n        bias_theory = abs(tau_plim - tau)\\n\\n        tau_mc = np.zeros(reps)\\n        for r in range(reps):\\n            Td, Yd, _, Asd = gen_mediation_data(N_mc, beta, tau, C0, rng)\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\n            tau_mc[r] = bh[1]\\n\\n        mc_mean = tau_mc.mean()\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\n\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\n            plim_ok_m += 1\\n        if abs(mc_mean - tau) <= bias_theory + 3 * mc_se + 0.02:\\n            bias_ok_m += 1\\n\\n        if (s + 1) % 100 == 0:\\n            print(f\\\"    ... {s+1}/{n_scenarios}\\\")\\n\\n    print(f\\\"    plim accuracy: {plim_ok_m}/{n_scenarios} = {plim_ok_m/n_scenarios*100:.1f}%\\\")\\n    print(f\\\"    bias bounded:  {bias_ok_m}/{n_scenarios} = {bias_ok_m/n_scenarios*100:.1f}%\\\")\\n\\n    # --- Collider ---\\n    print(\\\"\\\\n  [Collider]\\\")\\n    plim_ok_c = 0; bias_ok_c = 0\\n    tau_I_col = plim_collider(np.eye(K), st)[1]\\n\\n    for s in range(n_scenarios):\\n        C0 = random_C0(K, rng)\\n        tau_plim = plim_collider(C0, st)[1]\\n        bias_theory = abs(tau_plim - tau_I_col)\\n\\n        tau_mc = np.zeros(reps)\\n        for r in range(reps):\\n            Td, Yd, _, Asd = gen_collider_data(N_mc, COLLIDER_PARAMS, C0, rng)\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\n            tau_mc[r] = bh[1]\\n\\n        mc_mean = tau_mc.mean()\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\n\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\n            plim_ok_c += 1\\n        bias_mc = abs(mc_mean - tau_I_col)\\n        if bias_mc <= bias_theory + 3 * mc_se + 0.02:\\n            bias_ok_c += 1\\n\\n        if (s + 1) % 100 == 0:\\n            print(f\\\"    ... {s+1}/{n_scenarios}\\\")\\n\\n    print(f\\\"    plim accuracy: {plim_ok_c}/{n_scenarios} = {plim_ok_c/n_scenarios*100:.1f}%\\\")\\n    print(f\\\"    bias bounded:  {bias_ok_c}/{n_scenarios} = {bias_ok_c/n_scenarios*100:.1f}%\\\")\\n\\n    print(f\\\"\\\\n  Total time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Part 6: Type I/II Error Rate\\n# ============================================================================\\n\\ndef part6_type_errors(n_mc=2000, N_sample=1000):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(f\\\"PART 6: Type I/II Error Rate ({n_mc} MC x N={N_sample})\\\")\\n    print(\\\"=\\\" * 70)\\n    t0 = time.time()\\n\\n    param = LinearInterpolation()\\n    K = 3\\n\\n    C_list = {\\n        \\\"sym_mi\\n\\n... [截断: 输出过长，省略 1981 字符] ...\\n\\nbeta_med = np.array([0.0, 1.0, -0.5])\\n\\n    print(header)\\n    print(\\\"  \\\" + \\\"-\\\" * 54)\\n\\n    for cname, C0 in C_list.items():\\n        for h_label, tau_val in [(\\\"H0\\\", 0.0), (\\\"H1\\\", 0.5)]:\\n            seed_ctr += 1\\n            dmin, dmax = param.delta_range(C0)\\n            deltas = np.linspace(dmin, dmax, 1000)\\n            tau_curve = np.array([\\n                plim_mediation(param(C0, d), beta_med, tau_val)[1]\\n                for d in deltas])\\n\\n            rng = np.random.default_rng(seed_ctr)\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\n\\n            for mc in range(n_mc):\\n                Td, Yd, _, Asd = gen_mediation_data(\\n                    N_sample, beta_med, tau_val, C0, rng)\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\n                tau_hat = bh[1]; se_tau = seh[1]\\n\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\n                if reject:\\n                    naive_rej += 1\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\n                asv_vals.append(asv_val)\\n                if reject and (asv_val is None or asv_val > 1.0):\\n                    asv_rej += 1\\n\\n            asv_fin = [a for a in asv_vals if a is not None]\\n            asv_m = f\\\"{np.mean(asv_fin):.2f}\\\" if asv_fin else \\\"N/A\\\"\\n            print(f\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\")\\n\\n    # === Collider ===\\n    print(\\\"\\\\n  [Collider]\\\")\\n    print(header)\\n    print(\\\"  \\\" + \\\"-\\\" * 54)\\n\\n    for h_label, tau_val in [(\\\"H0\\\", 0.0), (\\\"H1\\\", 1.0)]:\\n        params_h = dict(COLLIDER_PARAMS)\\n        params_h['tau'] = tau_val\\n        print(f\\\"    precomputing collider moments for {h_label} (tau={tau_val})...\\\")\\n        st_h = precomp_collider(params=params_h, N=1_000_000)\\n\\n        for cname, C0 in C_list.items():\\n            seed_ctr += 1\\n            dmin, dmax = param.delta_range(C0)\\n            deltas = np.linspace(dmin, dmax, 1000)\\n            tau_curve = np.array([\\n                plim_collider(param(C0, d), st_h)[1] for d in deltas])\\n\\n            rng = np.random.default_rng(seed_ctr)\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\n\\n            for mc in range(n_mc):\\n                Td, Yd, _, Asd = gen_collider_data(\\n                    N_sample, params_h, C0, rng)\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\n                tau_hat = bh[1]; se_tau = seh[1]\\n\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\n                if reject:\\n                    naive_rej += 1\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\n                asv_vals.append(asv_val)\\n                if reject and (asv_val is None or asv_val > 1.0):\\n                    asv_rej += 1\\n\\n            asv_fin = [a for a in asv_vals if a is not None]\\n            asv_m = f\\\"{np.mean(asv_fin):.2f}\\\" if asv_fin else \\\"N/A\\\"\\n            print(f\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\")\\n\\n    print(f\\\"\\\\n  Total time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Main\\n# ============================================================================\\n\\nif __name__ == \\\"__main__\\\":\\n    np.set_printoptions(precision=6, suppress=True)\\n    print(\\\"plan_004 ASV Framework v2 -- Full Run\\\")\\n    print(\\\"Scheme A: Linear Interpolation + Vulnerability/Protection\\\")\\n    print(\\\"=\\\" * 70)\\n    t_total = time.time()\\n\\n    print(\\\"Precomputing collider sufficient statistics (N=2M)...\\\")\\n    st = precomp_collider()\\n    print(f\\\"  Done ({time.time()-t_total:.1f}s)\\\")\\n\\n    part1_verify(st)\\n    part2_asv_table(st)\\n    part3_monotonicity(st, n_C0=1000, n_delta=100)\\n    part4_sharpness(st)\\n    part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100)\\n    part6_type_errors(n_mc=2000, N_sample=1000)\\n\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    elapsed = time.time() - t_total\\n    print(f\\\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\\\")\\n    print(\\\"=\\\" * 70)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "7ee44b87-3f5b-4988-897b-0ab3bd89344f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    t0 = time.time()\\\\n\\\\n    rng = np.random.default_rng(42)\\\\n    K = 3\\\\n\\\\n    # --- Confounding ---\\\\n    print(\\\\\\\"\\\\\\\\n  [Confounding]\\\\\\\")\\\\n    plim_ok = 0; bias_ok = 0\\\\n\\\\n    for s in range(n_scenarios):\\\\n        C0 = random_C0(K, rng)\\\\n        p_A = rng.dirichlet(np.ones(K) * 2)\\\\n        tau = rng.uniform(0.2, 2.0) * rng.choice([-1, 1])\\\\n        bA = rng.normal(0, 0.5, K - 1)\\\\n        sT = rng.normal(0, 0.5, K)\\\\n        a_val = rng.normal(0, 0.5)\\\\n\\\\n        tau_plim = plim_confounding(C0, p_A, a_val, tau, bA, sT)[1]\\\\n        bias_theory = abs(tau_plim - tau)\\\\n\\\\n        tau_mc = np.zeros(reps)\\\\n        for r in range(reps):\\\\n            Td, Yd, _, Asd = gen_confounding_data(N_mc, p_A, a_val, tau, bA, sT, C0, rng)\\\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\\\n            tau_mc[r] = bh[1]\\\\n\\\\n        mc_mean = tau_mc.mean()\\\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\\\n\\\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\\\n            plim_ok += 1\\\\n        if abs(mc_mean - tau) <= bias_theory + 3 * mc_se + 0.02:\\\\n            bias_ok += 1\\\\n\\\\n        if (s + 1) % 100 == 0:\\\\n            print(f\\\\\\\"    ... {s+1}/{n_scenarios}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\\\\\\\")\\\\n    print(f\\\\\\\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\\\\\\\")\\\\n\\\\n    # --- Mediation ---\\\\n    print(\\\\\\\"\\\\\\\\n  [Mediation]\\\\\\\")\\\\n    plim_ok_m = 0; bias_ok_m = 0\\\\n\\\\n    for s in range(n_scenarios):\\\\n        C0 = random_C0(K, rng)\\\\n        tau = rng.uniform(0.2, 2.0) * rng.choice([-1, 1])\\\\n        beta = np.array([rng.normal(0, 0.5), rng.normal(0, 1), rng.normal(0, 1)])\\\\n\\\\n        tau_plim = plim_mediation(C0, beta, tau)[1]\\\\n        bias_theory = abs(tau_plim - tau)\\\\n\\\\n        tau_mc = np.zeros(reps)\\\\n        for r in range(reps):\\\\n            Td, Yd, _, Asd = gen_mediation_data(N_mc, beta, tau, C0, rng)\\\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\\\n            tau_mc[r] = bh[1]\\\\n\\\\n        mc_mean = tau_mc.mean()\\\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\\\n\\\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\\\n            plim_ok_m += 1\\\\n        if abs(mc_mean - tau) <= bias_theory + 3 * mc_se + 0.02:\\\\n            bias_ok_m += 1\\\\n\\\\n        if (s + 1) % 100 == 0:\\\\n            print(f\\\\\\\"    ... {s+1}/{n_scenarios}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"    plim accuracy: {plim_ok_m}/{n_scenarios} = {plim_ok_m/n_scenarios*100:.1f}%\\\\\\\")\\\\n    print(f\\\\\\\"    bias bounded:  {bias_ok_m}/{n_scenarios} = {bias_ok_m/n_scenarios*100:.1f}%\\\\\\\")\\\\n\\\\n    # --- Collider ---\\\\n    print(\\\\\\\"\\\\\\\\n  [Collider]\\\\\\\")\\\\n    plim_ok_c = 0; bias_ok_c = 0\\\\n    tau_I_col = plim_collider(np.eye(K), st)[1]\\\\n\\\\n    for s in range(n_scenarios):\\\\n        C0 = random_C0(K, rng)\\\\n        tau_plim = plim_collider(C0, st)[1]\\\\n        bias_theory = abs(tau_plim - tau_I_col)\\\\n\\\\n        tau_mc = np.zeros(reps)\\\\n        for r in range(reps):\\\\n            Td, Yd, _, Asd = gen_collider_data(N_mc, COLLIDER_PARAMS, C0, rng)\\\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\\\n            tau_mc[r] = bh[1]\\\\n\\\\n        mc_mean = tau_mc.mean()\\\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\\\n\\\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\\\n            plim_ok_c += 1\\\\n        bias_mc = abs(mc_mean - tau_I_col)\\\\n        if bias_mc <= bias_theory + 3 * mc_se + 0.02:\\\\n            bias_ok_c += 1\\\\n\\\\n        if (s + 1) % 100 == 0:\\\\n            print(f\\\\\\\"    ... {s+1}/{n_scenarios}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"    plim accuracy: {plim_ok_c}/{n_scenarios} = {plim_ok_c/n_scenarios*100:.1f}%\\\\\\\")\\\\n    print(f\\\\\\\"    bias bounded:  {bias_ok_c}/{n_scenarios} = {bias_ok_c/n_scenarios*100:.1f}%\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n  Total time: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n\\\\n# ============================================================================\\\\n# Part 6: Type I/II Error Rate\\\\n# ============================================================================\\\\n\\\\ndef part6_type_errors(n_mc=2000, N_sample=1000):\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    print(f\\\\\\\"PART 6: Type I/II Error Rate ({n_mc} MC x N={N_sample})\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n    t0 = time.time()\\\\n\\\\n    param = LinearInterpolation()\\\\n    K = 3\\\\n\\\\n    C_list = {\\\\n        \\\\\\\"sym_mi\\\\n\\\\n... [截断: 输出过长，省略 1981 字符] ...\\\\n\\\\nbeta_med = np.array([0.0, 1.0, -0.5])\\\\n\\\\n    print(header)\\\\n    print(\\\\\\\"  \\\\\\\" + \\\\\\\"-\\\\\\\" * 54)\\\\n\\\\n    for cname, C0 in C_list.items():\\\\n        for h_label, tau_val in [(\\\\\\\"H0\\\\\\\", 0.0), (\\\\\\\"H1\\\\\\\", 0.5)]:\\\\n            seed_ctr += 1\\\\n            dmin, dmax = param.delta_range(C0)\\\\n            deltas = np.linspace(dmin, dmax, 1000)\\\\n            tau_curve = np.array([\\\\n                plim_mediation(param(C0, d), beta_med, tau_val)[1]\\\\n                for d in deltas])\\\\n\\\\n            rng = np.random.default_rng(seed_ctr)\\\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\\\n\\\\n            for mc in range(n_mc):\\\\n                Td, Yd, _, Asd = gen_mediation_data(\\\\n                    N_sample, beta_med, tau_val, C0, rng)\\\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\\\n                tau_hat = bh[1]; se_tau = seh[1]\\\\n\\\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\\\n                if reject:\\\\n                    naive_rej += 1\\\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\\\n                asv_vals.append(asv_val)\\\\n                if reject and (asv_val is None or asv_val > 1.0):\\\\n                    asv_rej += 1\\\\n\\\\n            asv_fin = [a for a in asv_vals if a is not None]\\\\n            asv_m = f\\\\\\\"{np.mean(asv_fin):.2f}\\\\\\\" if asv_fin else \\\\\\\"N/A\\\\\\\"\\\\n            print(f\\\\\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\\\\\")\\\\n\\\\n    # === Collider ===\\\\n    print(\\\\\\\"\\\\\\\\n  [Collider]\\\\\\\")\\\\n    print(header)\\\\n    print(\\\\\\\"  \\\\\\\" + \\\\\\\"-\\\\\\\" * 54)\\\\n\\\\n    for h_label, tau_val in [(\\\\\\\"H0\\\\\\\", 0.0), (\\\\\\\"H1\\\\\\\", 1.0)]:\\\\n        params_h = dict(COLLIDER_PARAMS)\\\\n        params_h['tau'] = tau_val\\\\n        print(f\\\\\\\"    precomputing collider moments for {h_label} (tau={tau_val})...\\\\\\\")\\\\n        st_h = precomp_collider(params=params_h, N=1_000_000)\\\\n\\\\n        for cname, C0 in C_list.items():\\\\n            seed_ctr += 1\\\\n            dmin, dmax = param.delta_range(C0)\\\\n            deltas = np.linspace(dmin, dmax, 1000)\\\\n            tau_curve = np.array([\\\\n                plim_collider(param(C0, d), st_h)[1] for d in deltas])\\\\n\\\\n            rng = np.random.default_rng(seed_ctr)\\\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\\\n\\\\n            for mc in range(n_mc):\\\\n                Td, Yd, _, Asd = gen_collider_data(\\\\n                    N_sample, params_h, C0, rng)\\\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\\\n                tau_hat = bh[1]; se_tau = seh[1]\\\\n\\\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\\\n                if reject:\\\\n                    naive_rej += 1\\\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\\\n                asv_vals.append(asv_val)\\\\n                if reject and (asv_val is None or asv_val > 1.0):\\\\n                    asv_rej += 1\\\\n\\\\n            asv_fin = [a for a in asv_vals if a is not None]\\\\n            asv_m = f\\\\\\\"{np.mean(asv_fin):.2f}\\\\\\\" if asv_fin else \\\\\\\"N/A\\\\\\\"\\\\n            print(f\\\\\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n  Total time: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n\\\\n# ============================================================================\\\\n# Main\\\\n# ============================================================================\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    np.set_printoptions(precision=6, suppress=True)\\\\n    print(\\\\\\\"plan_004 ASV Framework v2 -- Full Run\\\\\\\")\\\\n    print(\\\\\\\"Scheme A: Linear Interpolation + Vulnerability/Protection\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n    t_total = time.time()\\\\n\\\\n    print(\\\\\\\"Precomputing collider sufficient statistics (N=2M)...\\\\\\\")\\\\n    st = precomp_collider()\\\\n    print(f\\\\\\\"  Done ({time.time()-t_total:.1f}s)\\\\\\\")\\\\n\\\\n    part1_verify(st)\\\\n    part2_asv_table(st)\\\\n    part3_monotonicity(st, n_C0=1000, n_delta=100)\\\\n    part4_sharpness(st)\\\\n    part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100)\\\\n    part6_type_errors(n_mc=2000, N_sample=1000)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    elapsed = time.time() - t_total\\\\n    print(f\\\\\\\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.24}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    t0 = time.time()\\n\\n    rng = np.random.default_rng(42)\\n    K = 3\\n\\n    # --- Confounding ---\\n    print(\\\"\\\\n  [Confounding]\\\")\\n    plim_ok = 0; bias_ok = 0\\n\\n    for s in range(n_scenarios):\\n        C0 = random_C0(K, rng)\\n        p_A = rng.dirichlet(np.ones(K) * 2)\\n        tau = rng.uniform(0.2, 2.0) * rng.choice([-1, 1])\\n        bA = rng.normal(0, 0.5, K - 1)\\n        sT = rng.normal(0, 0.5, K)\\n        a_val = rng.normal(0, 0.5)\\n\\n        tau_plim = plim_confounding(C0, p_A, a_val, tau, bA, sT)[1]\\n        bias_theory = abs(tau_plim - tau)\\n\\n        tau_mc = np.zeros(reps)\\n        for r in range(reps):\\n            Td, Yd, _, Asd = gen_confounding_data(N_mc, p_A, a_val, tau, bA, sT, C0, rng)\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\n            tau_mc[r] = bh[1]\\n\\n        mc_mean = tau_mc.mean()\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\n\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\n            plim_ok += 1\\n        if abs(mc_mean - tau) <= bias_theory + 3 * mc_se + 0.02:\\n            bias_ok += 1\\n\\n        if (s + 1) % 100 == 0:\\n            print(f\\\"    ... {s+1}/{n_scenarios}\\\")\\n\\n    print(f\\\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\\\")\\n    print(f\\\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\\\")\\n\\n    # --- Mediation ---\\n    print(\\\"\\\\n  [Mediation]\\\")\\n    plim_ok_m = 0; bias_ok_m = 0\\n\\n    for s in range(n_scenarios):\\n        C0 = random_C0(K, rng)\\n        tau = rng.uniform(0.2, 2.0) * rng.choice([-1, 1])\\n        beta = np.array([rng.normal(0, 0.5), rng.normal(0, 1), rng.normal(0, 1)])\\n\\n        tau_plim = plim_mediation(C0, beta, tau)[1]\\n        bias_theory = abs(tau_plim - tau)\\n\\n        tau_mc = np.zeros(reps)\\n        for r in range(reps):\\n            Td, Yd, _, Asd = gen_mediation_data(N_mc, beta, tau, C0, rng)\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\n            tau_mc[r] = bh[1]\\n\\n        mc_mean = tau_mc.mean()\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\n\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\n            plim_ok_m += 1\\n        if abs(mc_mean - tau) <= bias_theory + 3 * mc_se + 0.02:\\n            bias_ok_m += 1\\n\\n        if (s + 1) % 100 == 0:\\n            print(f\\\"    ... {s+1}/{n_scenarios}\\\")\\n\\n    print(f\\\"    plim accuracy: {plim_ok_m}/{n_scenarios} = {plim_ok_m/n_scenarios*100:.1f}%\\\")\\n    print(f\\\"    bias bounded:  {bias_ok_m}/{n_scenarios} = {bias_ok_m/n_scenarios*100:.1f}%\\\")\\n\\n    # --- Collider ---\\n    print(\\\"\\\\n  [Collider]\\\")\\n    plim_ok_c = 0; bias_ok_c = 0\\n    tau_I_col = plim_collider(np.eye(K), st)[1]\\n\\n    for s in range(n_scenarios):\\n        C0 = random_C0(K, rng)\\n        tau_plim = plim_collider(C0, st)[1]\\n        bias_theory = abs(tau_plim - tau_I_col)\\n\\n        tau_mc = np.zeros(reps)\\n        for r in range(reps):\\n            Td, Yd, _, Asd = gen_collider_data(N_mc, COLLIDER_PARAMS, C0, rng)\\n            bh, _ = ols_with_dummies(Yd, Td, Asd, K)\\n            tau_mc[r] = bh[1]\\n\\n        mc_mean = tau_mc.mean()\\n        mc_se = tau_mc.std() / np.sqrt(reps)\\n\\n        if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\\n            plim_ok_c += 1\\n        bias_mc = abs(mc_mean - tau_I_col)\\n        if bias_mc <= bias_theory + 3 * mc_se + 0.02:\\n            bias_ok_c += 1\\n\\n        if (s + 1) % 100 == 0:\\n            print(f\\\"    ... {s+1}/{n_scenarios}\\\")\\n\\n    print(f\\\"    plim accuracy: {plim_ok_c}/{n_scenarios} = {plim_ok_c/n_scenarios*100:.1f}%\\\")\\n    print(f\\\"    bias bounded:  {bias_ok_c}/{n_scenarios} = {bias_ok_c/n_scenarios*100:.1f}%\\\")\\n\\n    print(f\\\"\\\\n  Total time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Part 6: Type I/II Error Rate\\n# ============================================================================\\n\\ndef part6_type_errors(n_mc=2000, N_sample=1000):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(f\\\"PART 6: Type I/II Error Rate ({n_mc} MC x N={N_sample})\\\")\\n    print(\\\"=\\\" * 70)\\n    t0 = time.time()\\n\\n    param = LinearInterpolation()\\n    K = 3\\n\\n    C_list = {\\n        \\\"sym_mi\\n\\n... [截断: 输出过长，省略 1981 字符] ...\\n\\nbeta_med = np.array([0.0, 1.0, -0.5])\\n\\n    print(header)\\n    print(\\\"  \\\" + \\\"-\\\" * 54)\\n\\n    for cname, C0 in C_list.items():\\n        for h_label, tau_val in [(\\\"H0\\\", 0.0), (\\\"H1\\\", 0.5)]:\\n            seed_ctr += 1\\n            dmin, dmax = param.delta_range(C0)\\n            deltas = np.linspace(dmin, dmax, 1000)\\n            tau_curve = np.array([\\n                plim_mediation(param(C0, d), beta_med, tau_val)[1]\\n                for d in deltas])\\n\\n            rng = np.random.default_rng(seed_ctr)\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\n\\n            for mc in range(n_mc):\\n                Td, Yd, _, Asd = gen_mediation_data(\\n                    N_sample, beta_med, tau_val, C0, rng)\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\n                tau_hat = bh[1]; se_tau = seh[1]\\n\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\n                if reject:\\n                    naive_rej += 1\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\n                asv_vals.append(asv_val)\\n                if reject and (asv_val is None or asv_val > 1.0):\\n                    asv_rej += 1\\n\\n            asv_fin = [a for a in asv_vals if a is not None]\\n            asv_m = f\\\"{np.mean(asv_fin):.2f}\\\" if asv_fin else \\\"N/A\\\"\\n            print(f\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\")\\n\\n    # === Collider ===\\n    print(\\\"\\\\n  [Collider]\\\")\\n    print(header)\\n    print(\\\"  \\\" + \\\"-\\\" * 54)\\n\\n    for h_label, tau_val in [(\\\"H0\\\", 0.0), (\\\"H1\\\", 1.0)]:\\n        params_h = dict(COLLIDER_PARAMS)\\n        params_h['tau'] = tau_val\\n        print(f\\\"    precomputing collider moments for {h_label} (tau={tau_val})...\\\")\\n        st_h = precomp_collider(params=params_h, N=1_000_000)\\n\\n        for cname, C0 in C_list.items():\\n            seed_ctr += 1\\n            dmin, dmax = param.delta_range(C0)\\n            deltas = np.linspace(dmin, dmax, 1000)\\n            tau_curve = np.array([\\n                plim_collider(param(C0, d), st_h)[1] for d in deltas])\\n\\n            rng = np.random.default_rng(seed_ctr)\\n            naive_rej = 0; asv_rej = 0; asv_vals = []\\n\\n            for mc in range(n_mc):\\n                Td, Yd, _, Asd = gen_collider_data(\\n                    N_sample, params_h, C0, rng)\\n                bh, seh = ols_with_dummies(Yd, Td, Asd, K)\\n                tau_hat = bh[1]; se_tau = seh[1]\\n\\n                reject = abs(tau_hat / se_tau) > 1.96 if se_tau > 1e-10 else False\\n                if reject:\\n                    naive_rej += 1\\n                asv_val = compute_asv_fast(tau_curve, deltas, se_tau)\\n                asv_vals.append(asv_val)\\n                if reject and (asv_val is None or asv_val > 1.0):\\n                    asv_rej += 1\\n\\n            asv_fin = [a for a in asv_vals if a is not None]\\n            asv_m = f\\\"{np.mean(asv_fin):.2f}\\\" if asv_fin else \\\"N/A\\\"\\n            print(f\\\"  {cname:<14} {h_label:<5} {naive_rej/n_mc:>10.3f} {asv_rej/n_mc:>10.3f} {asv_m:>10}\\\")\\n\\n    print(f\\\"\\\\n  Total time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Main\\n# ============================================================================\\n\\nif __name__ == \\\"__main__\\\":\\n    np.set_printoptions(precision=6, suppress=True)\\n    print(\\\"plan_004 ASV Framework v2 -- Full Run\\\")\\n    print(\\\"Scheme A: Linear Interpolation + Vulnerability/Protection\\\")\\n    print(\\\"=\\\" * 70)\\n    t_total = time.time()\\n\\n    print(\\\"Precomputing collider sufficient statistics (N=2M)...\\\")\\n    st = precomp_collider()\\n    print(f\\\"  Done ({time.time()-t_total:.1f}s)\\\")\\n\\n    part1_verify(st)\\n    part2_asv_table(st)\\n    part3_monotonicity(st, n_C0=1000, n_delta=100)\\n    part4_sharpness(st)\\n    part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100)\\n    part6_type_errors(n_mc=2000, N_sample=1000)\\n\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    elapsed = time.time() - t_total\\n    print(f\\\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\\\")\\n    print(\\\"=\\\" * 70)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"
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
I still need to see some critical middle sections - especially the `compute_asv` and `compute_asv_fast` functions, part2 and part3. Let me get lines 200-400 more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "980db7af-cf78-4ed5-bb8c-037250aea57e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdxPh7daJaUR3JpBgJmJcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14704,
      "cache_read_input_tokens": 31314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14704
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

I need to see the critical middle section with `compute_asv` and `compute_asv_fast`. Let me get the missing parts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "f90727ca-59ea-4b7f-bec0-1f5ce5f2f166",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdxPh7daJaUR3JpBgJmJcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14704,
      "cache_read_input_tokens": 31314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14704
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016thyY3q4bMUWQn7B8Yo6nf`</summary>

```json
{
  "server": "home-1x5090",
  "command": "head -300 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "b524c99b-707e-4b44-839f-f56e1e1c63a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdxPh7daJaUR3JpBgJmJcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14704,
      "cache_read_input_tokens": 31314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14704
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

_source line 25 · 2026-05-20T13:11:22.704Z_

<details><summary>↩ Tool result · `toolu_016thyY3q4bMUWQn7B8Yo6nf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 1937 字符] ...\\n\\n['dT2'] * T + params['dY2'] * Y,\\n    ])\\n    A = softmax_sample(logits, rng)\\n    K = 3\\n    DM = np.zeros((N, K))\\n    for k in range(K):\\n        DM[:, k] = (A == k).astype(float)\\n    return dict(\\n        E_T=T.mean(), E_T2=(T**2).mean(),\\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\\n        E_DM=DM.mean(0),\\n        E_DM_T=(DM * T[:, None]).mean(0),\\n        E_DM_Y=(DM * Y[:, None]).mean(0),\\n    )\\n\\n\\ndef plim_collider(C, precomp):\\n    ds = C @ precomp['E_DM']\\n    dst = C @ precomp['E_DM_T']\\n    dsy = C @ precomp['E_DM_Y']\\n    ET, ET2 = precomp['E_T'], precomp['E_T2']\\n    EY, ETY = precomp['E_Y'], precomp['E_TY']\\n    EZZ = np.array([\\n        [1,     ET,     ds[1],   ds[2]  ],\\n        [ET,    ET2,    dst[1],  dst[2] ],\\n        [ds[1], dst[1], ds[1],   0      ],\\n        [ds[2], dst[2], 0,       ds[2]  ]])\\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\\n    try:\\n        return np.linalg.solve(EZZ, EZY)\\n    except np.linalg.LinAlgError:\\n        return np.full(4, np.nan)\\n\\n\\n# ============================================================================\\n# ASV Computation\\n# ============================================================================\\n\\ndef compute_asv(plim_func, plim_kwargs, C0, param, tau_index=1,\\n                direction=\\\"vulnerability\\\", threshold=0.0, se=None,\\n                alpha=0.05, n_grid=1000, tau_true=None):\\n    delta_min, delta_max = param.delta_range(C0)\\n    deltas = np.linspace(delta_min, delta_max, n_grid)\\n    K = C0.shape[0]\\n    plim_I = plim_func(np.eye(K), **plim_kwargs)\\n    tau_baseline = plim_I[tau_index]\\n\\n    tau_curve = np.zeros(n_grid)\\n    for i, d in enumerate(deltas):\\n        C_d = param(C0, d)\\n        plim_d = plim_func(C_d, **plim_kwargs)\\n        tau_curve[i] = plim_d[tau_index]\\n\\n    asv = None\\n    if direction == \\\"vulnerability\\\":\\n        baseline_sign = np.sign(tau_baseline)\\n        if se is not None:\\n            z_crit = 1.96\\n            for i, d in enumerate(deltas):\\n                if abs(tau_curve[i]) < z_crit * se:\\n                    asv = d\\n                    break\\n        else:\\n            for i, d in enumerate(deltas):\\n                if np.isnan(tau_curve[i]):\\n                    continue\\n                if np.sign(tau_curve[i]) != baseline_sign:\\n                    asv = d\\n                    break\\n    elif direction == \\\"protection\\\":\\n        tau_ref = tau_true if tau_true is not None else tau_curve[-1]\\n        for i, d in enumerate(deltas):\\n            if np.isnan(tau_curve[i]):\\n                continue\\n            bias_d = abs(tau_curve[i] - tau_ref)\\n            if bias_d < max(threshold, 0.01):\\n                asv = d\\n                break\\n\\n    return {\\\"asv\\\": asv, \\\"direction\\\": direction, \\\"deltas\\\": deltas,\\n            \\\"tau_curve\\\": tau_curve, \\\"tau_baseline\\\": tau_baseline}\\n\\n\\ndef compute_asv_fast(tau_curve, deltas, se):\\n    z_crit = 1.96\\n    for i in range(len(deltas)):\\n        if np.isnan(tau_curve[i]):\\n            continue\\n        if abs(tau_curve[i]) < z_crit * se:\\n            return deltas[i]\\n    return None\\n\\n\\n# ============================================================================\\n# Named C0 structures + random generator\\n# ============================================================================\\n\\ndef make_named_C_structures():\\n    return {\\n        \\\"sym_mild\\\": np.array([\\n            [0.80, 0.10, 0.10],\\n            [0.10, 0.80, 0.10],\\n            [0.10, 0.10, 0.80]]),\\n        \\\"sym_severe\\\": np.array([\\n            [0.60, 0.20, 0.20],\\n            [0.20, 0.60, 0.20],\\n            [0.20, 0.20, 0.60]]),\\n        \\\"asym_01\\\": np.array([\\n            [0.70, 0.25, 0.05],\\n            [0.25, 0.70, 0.05],\\n            [0.05, 0.05, 0.90]]),\\n        \\\"one_weak\\\": np.array([\\n            [0.90, 0.05, 0.30],\\n            [0.05, 0.90, 0.30],\\n            [0.05, 0.05, 0.40]]),\\n        \\\"near_perfect\\\": np.array([\\n            [0.95, 0.025, 0.025],\\n            [0.025, 0.95, 0.025],\\n            [0.025, 0.025, 0.95]]),\\n        \\\"heavy_offdiag\\\": np.array([\\n            [0.50, 0.30, 0.20],\\n            [0.30, 0.50, 0.30],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "ffa01729-b9b4-40d8-bf59-b0a63340f8c4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nplan_004: ASV Framework v2\\\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\\\n\\\\n双方向:\\\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport time\\\\nfrom abc import ABC, abstractmethod\\\\n\\\\n\\\\n# ============================================================================\\\\n# Utilities\\\\n# ============================================================================\\\\n\\\\ndef softmax(x):\\\\n    e = np.exp(x - x.max())\\\\n    return e / e.sum()\\\\n\\\\n\\\\ndef p_cat(t, g, d):\\\\n    return softmax(g + d * t)\\\\n\\\\n\\\\ndef generate_Astar(A, C, rng):\\\\n    probs = C[:, A]\\\\n    cum = np.cumsum(probs, axis=0)\\\\n    u = rng.uniform(size=len(A))\\\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\\\n\\\\n\\\\ndef softmax_sample(logits, rng):\\\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\\\n    cum = np.cumsum(probs, axis=1)\\\\n    u = rng.uniform(size=logits.shape[0])\\\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\\\n\\\\n\\\\ndef check_column_stochastic(C, tol=1e-6):\\\\n    assert np.all(C >= -tol), f\\\\\\\"Negative entries in C: min={C.min()}\\\\\\\"\\\\n    col_sums = C.sum(axis=0)\\\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\\\\\"Column sums != 1: {col_sums}\\\\\\\"\\\\n\\\\n\\\\ndef ols_with_dummies(Y, T, Astar, K=3):\\\\n    N = len(Y)\\\\n    D = np.zeros((N, K - 1))\\\\n    for k in range(1, K):\\\\n        D[:, k - 1] = (Astar == k).astype(float)\\\\n    X = np.column_stack([np.ones(N), T, D])\\\\n    try:\\\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\\\n        resid = Y - X @ beta\\\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\\\n        XtX_inv = np.linalg.inv(X.T @ X)\\\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\\\n    except np.linalg.LinAlgError:\\\\n        beta = np.full(X.shape[1], np.nan)\\\\n        se = np.full(X.shape[1], np.nan)\\\\n    return beta, se\\\\n\\\\n\\\\n# ============================================================================\\\\n# C(delta) Parameterization\\\\n# ============================================================================\\\\n\\\\nclass ConfusionParameterization(ABC):\\\\n    @abstractmethod\\\\n    def __call__(self, C0, delta):\\\\n        pass\\\\n\\\\n    @abstractmethod\\\\n    def delta_range(self, C0=None):\\\\n        pass\\\\n\\\\n\\\\nclass LinearInterpolation(ConfusionParameterization):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\n    def __call__(self, C0, delta):\\\\n        K = C0.shape[0]\\\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\\\n        C_d = np.maximum(C_d, 0.0)\\\\n        col_sums = C_d.sum(axis=0)\\\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\\\n        C_d = C_d / col_sums\\\\n        return C_d\\\\n\\\\n    def delta_range(self, C0=None):\\\\n        if C0 is None:\\\\n            return (0.0, 5.0)\\\\n        min_diag = np.diag(C0).min()\\\\n        if min_diag >= 1.0:\\\\n            return (0.0, 10.0)\\\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\\\n        return (0.0, delta_max)\\\\n\\\\n\\\\n# ============================================================================\\\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\\\n# ============================================================================\\\\n\\\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\\\n    mu = sigma_T\\\\n    ET = np.sum(p_A * mu)\\\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\\\n    q = C @ p_A\\\\n    qt = C @ (p_A * mu)\\\\n    EZZ = np.array([\\\\n        [1,    ET,    q[1],   q[2]  ],\\\\n        [ET,   ET2,   qt[1],  qt[2] ],\\\\n        [q[1], qt[1], q[1],   0     ],\\\\n        [q[2], qt[2], 0,      q[2]  ]])\\\\n    EZX = np.array([\\\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\\\n    try:\\\\n        retur\\\\n\\\\n... [截断: 输出过长，省略 1937 字符] ...\\\\n\\\\n['dT2'] * T + params['dY2'] * Y,\\\\n    ])\\\\n    A = softmax_sample(logits, rng)\\\\n    K = 3\\\\n    DM = np.zeros((N, K))\\\\n    for k in range(K):\\\\n        DM[:, k] = (A == k).astype(float)\\\\n    return dict(\\\\n        E_T=T.mean(), E_T2=(T**2).mean(),\\\\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\\\\n        E_DM=DM.mean(0),\\\\n        E_DM_T=(DM * T[:, None]).mean(0),\\\\n        E_DM_Y=(DM * Y[:, None]).mean(0),\\\\n    )\\\\n\\\\n\\\\ndef plim_collider(C, precomp):\\\\n    ds = C @ precomp['E_DM']\\\\n    dst = C @ precomp['E_DM_T']\\\\n    dsy = C @ precomp['E_DM_Y']\\\\n    ET, ET2 = precomp['E_T'], precomp['E_T2']\\\\n    EY, ETY = precomp['E_Y'], precomp['E_TY']\\\\n    EZZ = np.array([\\\\n        [1,     ET,     ds[1],   ds[2]  ],\\\\n        [ET,    ET2,    dst[1],  dst[2] ],\\\\n        [ds[1], dst[1], ds[1],   0      ],\\\\n        [ds[2], dst[2], 0,       ds[2]  ]])\\\\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\\\\n    try:\\\\n        return np.linalg.solve(EZZ, EZY)\\\\n    except np.linalg.LinAlgError:\\\\n        return np.full(4, np.nan)\\\\n\\\\n\\\\n# ============================================================================\\\\n# ASV Computation\\\\n# ============================================================================\\\\n\\\\ndef compute_asv(plim_func, plim_kwargs, C0, param, tau_index=1,\\\\n                direction=\\\\\\\"vulnerability\\\\\\\", threshold=0.0, se=None,\\\\n                alpha=0.05, n_grid=1000, tau_true=None):\\\\n    delta_min, delta_max = param.delta_range(C0)\\\\n    deltas = np.linspace(delta_min, delta_max, n_grid)\\\\n    K = C0.shape[0]\\\\n    plim_I = plim_func(np.eye(K), **plim_kwargs)\\\\n    tau_baseline = plim_I[tau_index]\\\\n\\\\n    tau_curve = np.zeros(n_grid)\\\\n    for i, d in enumerate(deltas):\\\\n        C_d = param(C0, d)\\\\n        plim_d = plim_func(C_d, **plim_kwargs)\\\\n        tau_curve[i] = plim_d[tau_index]\\\\n\\\\n    asv = None\\\\n    if direction == \\\\\\\"vulnerability\\\\\\\":\\\\n        baseline_sign = np.sign(tau_baseline)\\\\n        if se is not None:\\\\n            z_crit = 1.96\\\\n            for i, d in enumerate(deltas):\\\\n                if abs(tau_curve[i]) < z_crit * se:\\\\n                    asv = d\\\\n                    break\\\\n        else:\\\\n            for i, d in enumerate(deltas):\\\\n                if np.isnan(tau_curve[i]):\\\\n                    continue\\\\n                if np.sign(tau_curve[i]) != baseline_sign:\\\\n                    asv = d\\\\n                    break\\\\n    elif direction == \\\\\\\"protection\\\\\\\":\\\\n        tau_ref = tau_true if tau_true is not None else tau_curve[-1]\\\\n        for i, d in enumerate(deltas):\\\\n            if np.isnan(tau_curve[i]):\\\\n                continue\\\\n            bias_d = abs(tau_curve[i] - tau_ref)\\\\n            if bias_d < max(threshold, 0.01):\\\\n                asv = d\\\\n                break\\\\n\\\\n    return {\\\\\\\"asv\\\\\\\": asv, \\\\\\\"direction\\\\\\\": direction, \\\\\\\"deltas\\\\\\\": deltas,\\\\n            \\\\\\\"tau_curve\\\\\\\": tau_curve, \\\\\\\"tau_baseline\\\\\\\": tau_baseline}\\\\n\\\\n\\\\ndef compute_asv_fast(tau_curve, deltas, se):\\\\n    z_crit = 1.96\\\\n    for i in range(len(deltas)):\\\\n        if np.isnan(tau_curve[i]):\\\\n            continue\\\\n        if abs(tau_curve[i]) < z_crit * se:\\\\n            return deltas[i]\\\\n    return None\\\\n\\\\n\\\\n# ============================================================================\\\\n# Named C0 structures + random generator\\\\n# ============================================================================\\\\n\\\\ndef make_named_C_structures():\\\\n    return {\\\\n        \\\\\\\"sym_mild\\\\\\\": np.array([\\\\n            [0.80, 0.10, 0.10],\\\\n            [0.10, 0.80, 0.10],\\\\n            [0.10, 0.10, 0.80]]),\\\\n        \\\\\\\"sym_severe\\\\\\\": np.array([\\\\n            [0.60, 0.20, 0.20],\\\\n            [0.20, 0.60, 0.20],\\\\n            [0.20, 0.20, 0.60]]),\\\\n        \\\\\\\"asym_01\\\\\\\": np.array([\\\\n            [0.70, 0.25, 0.05],\\\\n            [0.25, 0.70, 0.05],\\\\n            [0.05, 0.05, 0.90]]),\\\\n        \\\\\\\"one_weak\\\\\\\": np.array([\\\\n            [0.90, 0.05, 0.30],\\\\n            [0.05, 0.90, 0.30],\\\\n            [0.05, 0.05, 0.40]]),\\\\n        \\\\\\\"near_perfect\\\\\\\": np.array([\\\\n            [0.95, 0.025, 0.025],\\\\n            [0.025, 0.95, 0.025],\\\\n            [0.025, 0.025, 0.95]]),\\\\n        \\\\\\\"heavy_offdiag\\\\\\\": np.array([\\\\n            [0.50, 0.30, 0.20],\\\\n            [0.30, 0.50, 0.30],\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.97}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 1937 字符] ...\\n\\n['dT2'] * T + params['dY2'] * Y,\\n    ])\\n    A = softmax_sample(logits, rng)\\n    K = 3\\n    DM = np.zeros((N, K))\\n    for k in range(K):\\n        DM[:, k] = (A == k).astype(float)\\n    return dict(\\n        E_T=T.mean(), E_T2=(T**2).mean(),\\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\\n        E_DM=DM.mean(0),\\n        E_DM_T=(DM * T[:, None]).mean(0),\\n        E_DM_Y=(DM * Y[:, None]).mean(0),\\n    )\\n\\n\\ndef plim_collider(C, precomp):\\n    ds = C @ precomp['E_DM']\\n    dst = C @ precomp['E_DM_T']\\n    dsy = C @ precomp['E_DM_Y']\\n    ET, ET2 = precomp['E_T'], precomp['E_T2']\\n    EY, ETY = precomp['E_Y'], precomp['E_TY']\\n    EZZ = np.array([\\n        [1,     ET,     ds[1],   ds[2]  ],\\n        [ET,    ET2,    dst[1],  dst[2] ],\\n        [ds[1], dst[1], ds[1],   0      ],\\n        [ds[2], dst[2], 0,       ds[2]  ]])\\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\\n    try:\\n        return np.linalg.solve(EZZ, EZY)\\n    except np.linalg.LinAlgError:\\n        return np.full(4, np.nan)\\n\\n\\n# ============================================================================\\n# ASV Computation\\n# ============================================================================\\n\\ndef compute_asv(plim_func, plim_kwargs, C0, param, tau_index=1,\\n                direction=\\\"vulnerability\\\", threshold=0.0, se=None,\\n                alpha=0.05, n_grid=1000, tau_true=None):\\n    delta_min, delta_max = param.delta_range(C0)\\n    deltas = np.linspace(delta_min, delta_max, n_grid)\\n    K = C0.shape[0]\\n    plim_I = plim_func(np.eye(K), **plim_kwargs)\\n    tau_baseline = plim_I[tau_index]\\n\\n    tau_curve = np.zeros(n_grid)\\n    for i, d in enumerate(deltas):\\n        C_d = param(C0, d)\\n        plim_d = plim_func(C_d, **plim_kwargs)\\n        tau_curve[i] = plim_d[tau_index]\\n\\n    asv = None\\n    if direction == \\\"vulnerability\\\":\\n        baseline_sign = np.sign(tau_baseline)\\n        if se is not None:\\n            z_crit = 1.96\\n            for i, d in enumerate(deltas):\\n                if abs(tau_curve[i]) < z_crit * se:\\n                    asv = d\\n                    break\\n        else:\\n            for i, d in enumerate(deltas):\\n                if np.isnan(tau_curve[i]):\\n                    continue\\n                if np.sign(tau_curve[i]) != baseline_sign:\\n                    asv = d\\n                    break\\n    elif direction == \\\"protection\\\":\\n        tau_ref = tau_true if tau_true is not None else tau_curve[-1]\\n        for i, d in enumerate(deltas):\\n            if np.isnan(tau_curve[i]):\\n                continue\\n            bias_d = abs(tau_curve[i] - tau_ref)\\n            if bias_d < max(threshold, 0.01):\\n                asv = d\\n                break\\n\\n    return {\\\"asv\\\": asv, \\\"direction\\\": direction, \\\"deltas\\\": deltas,\\n            \\\"tau_curve\\\": tau_curve, \\\"tau_baseline\\\": tau_baseline}\\n\\n\\ndef compute_asv_fast(tau_curve, deltas, se):\\n    z_crit = 1.96\\n    for i in range(len(deltas)):\\n        if np.isnan(tau_curve[i]):\\n            continue\\n        if abs(tau_curve[i]) < z_crit * se:\\n            return deltas[i]\\n    return None\\n\\n\\n# ============================================================================\\n# Named C0 structures + random generator\\n# ============================================================================\\n\\ndef make_named_C_structures():\\n    return {\\n        \\\"sym_mild\\\": np.array([\\n            [0.80, 0.10, 0.10],\\n            [0.10, 0.80, 0.10],\\n            [0.10, 0.10, 0.80]]),\\n        \\\"sym_severe\\\": np.array([\\n            [0.60, 0.20, 0.20],\\n            [0.20, 0.60, 0.20],\\n            [0.20, 0.20, 0.60]]),\\n        \\\"asym_01\\\": np.array([\\n            [0.70, 0.25, 0.05],\\n            [0.25, 0.70, 0.05],\\n            [0.05, 0.05, 0.90]]),\\n        \\\"one_weak\\\": np.array([\\n            [0.90, 0.05, 0.30],\\n            [0.05, 0.90, 0.30],\\n            [0.05, 0.05, 0.40]]),\\n        \\\"near_perfect\\\": np.array([\\n            [0.95, 0.025, 0.025],\\n            [0.025, 0.95, 0.025],\\n            [0.025, 0.025, 0.95]]),\\n        \\\"heavy_offdiag\\\": np.array([\\n            [0.50, 0.30, 0.20],\\n            [0.30, 0.50, 0.30],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"
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
Now I have a good understanding of the existing code. Let me also read the part around lines 200-280 more carefully where `compute_asv` is defined. I can see it was in the output above. Let me also get the part2 ASV table function.

Let me get the remaining middle sections I'm missing - specifically part1_verify (around line 340-430), part2_asv_table (around line 430-530), and part3_monotonicity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "58e29161-f659-4ddc-86f7-709f60b6e833",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPUDMfT3A4ExdUDTxdcAaB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3869,
      "cache_read_input_tokens": 46018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3869
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

Now I have a clear picture of the existing code. Let me also see parts 2-3 which I need for the structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "d7e84926-8c0e-481d-904d-dd859802ed55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPUDMfT3A4ExdUDTxdcAaB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3869,
      "cache_read_input_tokens": 46018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3869
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Ry55AzE4sUxe94cpewNcXH`</summary>

```json
{
  "server": "home-1x5090",
  "command": "grep -n \"def part\" /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "0b849988-6688-4565-862c-1dcd9eb95680",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPUDMfT3A4ExdUDTxdcAaB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3869,
      "cache_read_input_tokens": 46018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3869
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

_source line 29 · 2026-05-20T13:11:30.302Z_

<details><summary>↩ Tool result · `toolu_01Ry55AzE4sUxe94cpewNcXH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"357:def part1_verify(st):\\n435:def part2_asv_table(st):\\n483:def part3_monotonicity(st, n_C0=1000, n_delta=100):\\n548:def part4_sharpness(st):\\n597:def part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100):\\n711:def part6_type_errors(n_mc=2000, N_sample=1000):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "4235670a-b1de-4aca-8959-15b8bb4eea93",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"357:def part1_verify(st):\\\\n435:def part2_asv_table(st):\\\\n483:def part3_monotonicity(st, n_C0=1000, n_delta=100):\\\\n548:def part4_sharpness(st):\\\\n597:def part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100):\\\\n711:def part6_type_errors(n_mc=2000, N_sample=1000):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"357:def part1_verify(st):\\n435:def part2_asv_table(st):\\n483:def part3_monotonicity(st, n_C0=1000, n_delta=100):\\n548:def part4_sharpness(st):\\n597:def part5_mc_coverage(st, n_scenarios=500, N_mc=5000, reps=100):\\n711:def part6_type_errors(n_mc=2000, N_sample=1000):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Tf2uwQMGCteMQP4p4KC8jF`</summary>

```json
{
  "server": "home-1x5090",
  "command": "head -545 /home/sonny/causal_annot_error_attrib/plan_004_asv_framework.py",
  "account": "sonny"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "c706baad-8a96-494a-be15-414d3dda650e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKHQrFrrHi9p7ACscpKQDL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 487,
      "cache_read_input_tokens": 49887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 487
      },
      "output_tokens": 64,
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

_source line 31 · 2026-05-20T13:11:38.761Z_

<details><summary>↩ Tool result · `toolu_01Tf2uwQMGCteMQP4p4KC8jF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 11393 字符] ...\\n\\nbeta_T = 1.0\\n    beta_A = np.array([0.8, -0.3])\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\n    tau_true_col = COLLIDER_PARAMS['tau']\\n\\n    print(f\\\"\\\\n{'C_structure':<18} {'Conf(V)':>10} {'Med(V)':>10} {'Coll(P)':>10}  {'d_max':>8}\\\")\\n    print(\\\"-\\\" * 62)\\n\\n    for name, C0 in structures.items():\\n        check_column_stochastic(C0)\\n        _, dmax = param.delta_range(C0)\\n\\n        r_cf = compute_asv(plim_confounding,\\n                           dict(p_A=p_A, alpha=alpha_cf, beta_T=beta_T,\\n                                beta_A=beta_A, sigma_T=sigma_T),\\n                           C0, param, direction=\\\"vulnerability\\\")\\n\\n        r_med = compute_asv(plim_mediation,\\n                            dict(beta=beta_med, tau=tau_med),\\n                            C0, param, direction=\\\"vulnerability\\\")\\n\\n        r_col = compute_asv(plim_collider, dict(precomp=st),\\n                            C0, param, direction=\\\"protection\\\",\\n                            tau_true=tau_true_col)\\n\\n        def fmt(v):\\n            return f\\\"{v:.3f}\\\" if v is not None else \\\"None\\\"\\n\\n        asv_col_str = fmt(r_col['asv']) if r_col['asv'] is not None else \\\"None*\\\"\\n        print(f\\\"{name:<18} {fmt(r_cf['asv']):>10} {fmt(r_med['asv']):>10} {asv_col_str:>10}  {dmax:>8.1f}\\\")\\n\\n    print(\\\"\\\\n* Collider ASV=None: protection -- collider bias persists across full delta range\\\")\\n\\n\\n# ============================================================================\\n# Part 3: Monotonicity Verification\\n# ============================================================================\\n\\ndef part3_monotonicity(st, n_C0=1000, n_delta=100):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(f\\\"PART 3: Monotonicity verification ({n_C0} random C0 x {n_delta} deltas)\\\")\\n    print(\\\"=\\\" * 70)\\n    t0 = time.time()\\n\\n    param = LinearInterpolation()\\n    rng = np.random.default_rng(123)\\n    K = 3\\n\\n    p_A = np.array([0.4, 0.35, 0.25])\\n    alpha_cf = 0.5; beta_T = 1.0\\n    beta_A = np.array([0.8, -0.3])\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\n    tau_true_col = COLLIDER_PARAMS['tau']\\n\\n    violations = {\\\"confounding\\\": [], \\\"mediation\\\": [], \\\"collider\\\": []}\\n\\n    for s in range(n_C0):\\n        C0 = random_C0(K, rng)\\n        dmin, dmax = param.delta_range(C0)\\n        deltas = np.linspace(dmin, dmax, n_delta)\\n\\n        # Confounding: |bias| should increase\\n        tau_cf = np.array([plim_confounding(param(C0, d), p_A, alpha_cf,\\n                           beta_T, beta_A, sigma_T)[1] for d in deltas])\\n        bias_cf = np.abs(tau_cf - beta_T)\\n        diffs_cf = np.diff(bias_cf)\\n        if np.any(diffs_cf < -1e-8):\\n            violations[\\\"confounding\\\"].append((s, np.min(diffs_cf)))\\n\\n        # Mediation: |bias| should increase\\n        tau_m = np.array([plim_mediation(param(C0, d), beta_med, tau_med)[1]\\n                          for d in deltas])\\n        bias_m = np.abs(tau_m - tau_med)\\n        diffs_m = np.diff(bias_m)\\n        if np.any(diffs_m < -1e-8):\\n            violations[\\\"mediation\\\"].append((s, np.min(diffs_m)))\\n\\n        # Collider: |collider_bias| should decrease\\n        tau_c = np.array([plim_collider(param(C0, d), st)[1] for d in deltas])\\n        bias_c = np.abs(tau_c - tau_true_col)\\n        diffs_c = np.diff(bias_c)\\n        if np.any(diffs_c > 1e-8):\\n            violations[\\\"collider\\\"].append((s, np.max(diffs_c)))\\n\\n        if (s + 1) % 200 == 0:\\n            print(f\\\"  ... {s+1}/{n_C0}\\\")\\n\\n    for topo in [\\\"confounding\\\", \\\"mediation\\\", \\\"collider\\\"]:\\n        v = violations[topo]\\n        direction = \\\"increasing\\\" if topo != \\\"collider\\\" else \\\"decreasing\\\"\\n        print(f\\\"  {topo}: {len(v)}/{n_C0} violations (expected |bias| {direction})\\\")\\n        if v:\\n            worst = max(v, key=lambda x: abs(x[1]))\\n            print(f\\\"    worst: scenario {worst[0]}, max|delta_bias|={worst[1]:.2e}\\\")\\n\\n    print(f\\\"  Time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Part 4: Sharpness Verification\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fac64bd-392f-434b-be90-8d03378b810e",
  "uuid": "b8397329-a503-45ab-a7e0-45df5e173c28",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nplan_004: ASV Framework v2\\\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\\\n\\\\n双方向:\\\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport time\\\\nfrom abc import ABC, abstractmethod\\\\n\\\\n\\\\n# ============================================================================\\\\n# Utilities\\\\n# ============================================================================\\\\n\\\\ndef softmax(x):\\\\n    e = np.exp(x - x.max())\\\\n    return e / e.sum()\\\\n\\\\n\\\\ndef p_cat(t, g, d):\\\\n    return softmax(g + d * t)\\\\n\\\\n\\\\ndef generate_Astar(A, C, rng):\\\\n    probs = C[:, A]\\\\n    cum = np.cumsum(probs, axis=0)\\\\n    u = rng.uniform(size=len(A))\\\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\\\n\\\\n\\\\ndef softmax_sample(logits, rng):\\\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\\\n    cum = np.cumsum(probs, axis=1)\\\\n    u = rng.uniform(size=logits.shape[0])\\\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\\\n\\\\n\\\\ndef check_column_stochastic(C, tol=1e-6):\\\\n    assert np.all(C >= -tol), f\\\\\\\"Negative entries in C: min={C.min()}\\\\\\\"\\\\n    col_sums = C.sum(axis=0)\\\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\\\\\"Column sums != 1: {col_sums}\\\\\\\"\\\\n\\\\n\\\\ndef ols_with_dummies(Y, T, Astar, K=3):\\\\n    N = len(Y)\\\\n    D = np.zeros((N, K - 1))\\\\n    for k in range(1, K):\\\\n        D[:, k - 1] = (Astar == k).astype(float)\\\\n    X = np.column_stack([np.ones(N), T, D])\\\\n    try:\\\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\\\n        resid = Y - X @ beta\\\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\\\n        XtX_inv = np.linalg.inv(X.T @ X)\\\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\\\n    except np.linalg.LinAlgError:\\\\n        beta = np.full(X.shape[1], np.nan)\\\\n        se = np.full(X.shape[1], np.nan)\\\\n    return beta, se\\\\n\\\\n\\\\n# ============================================================================\\\\n# C(delta) Parameterization\\\\n# ============================================================================\\\\n\\\\nclass ConfusionParameterization(ABC):\\\\n    @abstractmethod\\\\n    def __call__(self, C0, delta):\\\\n        pass\\\\n\\\\n    @abstractmethod\\\\n    def delta_range(self, C0=None):\\\\n        pass\\\\n\\\\n\\\\nclass LinearInterpolation(ConfusionParameterization):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\n    def __call__(self, C0, delta):\\\\n        K = C0.shape[0]\\\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\\\n        C_d = np.maximum(C_d, 0.0)\\\\n        col_sums = C_d.sum(axis=0)\\\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\\\n        C_d = C_d / col_sums\\\\n        return C_d\\\\n\\\\n    def delta_range(self, C0=None):\\\\n        if C0 is None:\\\\n            return (0.0, 5.0)\\\\n        min_diag = np.diag(C0).min()\\\\n        if min_diag >= 1.0:\\\\n            return (0.0, 10.0)\\\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\\\n        return (0.0, delta_max)\\\\n\\\\n\\\\n# ============================================================================\\\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\\\n# ============================================================================\\\\n\\\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\\\n    mu = sigma_T\\\\n    ET = np.sum(p_A * mu)\\\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\\\n    q = C @ p_A\\\\n    qt = C @ (p_A * mu)\\\\n    EZZ = np.array([\\\\n        [1,    ET,    q[1],   q[2]  ],\\\\n        [ET,   ET2,   qt[1],  qt[2] ],\\\\n        [q[1], qt[1], q[1],   0     ],\\\\n        [q[2], qt[2], 0,      q[2]  ]])\\\\n    EZX = np.array([\\\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\\\n    try:\\\\n        retur\\\\n\\\\n... [截断: 输出过长，省略 11393 字符] ...\\\\n\\\\nbeta_T = 1.0\\\\n    beta_A = np.array([0.8, -0.3])\\\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\\\n    tau_true_col = COLLIDER_PARAMS['tau']\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n{'C_structure':<18} {'Conf(V)':>10} {'Med(V)':>10} {'Coll(P)':>10}  {'d_max':>8}\\\\\\\")\\\\n    print(\\\\\\\"-\\\\\\\" * 62)\\\\n\\\\n    for name, C0 in structures.items():\\\\n        check_column_stochastic(C0)\\\\n        _, dmax = param.delta_range(C0)\\\\n\\\\n        r_cf = compute_asv(plim_confounding,\\\\n                           dict(p_A=p_A, alpha=alpha_cf, beta_T=beta_T,\\\\n                                beta_A=beta_A, sigma_T=sigma_T),\\\\n                           C0, param, direction=\\\\\\\"vulnerability\\\\\\\")\\\\n\\\\n        r_med = compute_asv(plim_mediation,\\\\n                            dict(beta=beta_med, tau=tau_med),\\\\n                            C0, param, direction=\\\\\\\"vulnerability\\\\\\\")\\\\n\\\\n        r_col = compute_asv(plim_collider, dict(precomp=st),\\\\n                            C0, param, direction=\\\\\\\"protection\\\\\\\",\\\\n                            tau_true=tau_true_col)\\\\n\\\\n        def fmt(v):\\\\n            return f\\\\\\\"{v:.3f}\\\\\\\" if v is not None else \\\\\\\"None\\\\\\\"\\\\n\\\\n        asv_col_str = fmt(r_col['asv']) if r_col['asv'] is not None else \\\\\\\"None*\\\\\\\"\\\\n        print(f\\\\\\\"{name:<18} {fmt(r_cf['asv']):>10} {fmt(r_med['asv']):>10} {asv_col_str:>10}  {dmax:>8.1f}\\\\\\\")\\\\n\\\\n    print(\\\\\\\"\\\\\\\\n* Collider ASV=None: protection -- collider bias persists across full delta range\\\\\\\")\\\\n\\\\n\\\\n# ============================================================================\\\\n# Part 3: Monotonicity Verification\\\\n# ============================================================================\\\\n\\\\ndef part3_monotonicity(st, n_C0=1000, n_delta=100):\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    print(f\\\\\\\"PART 3: Monotonicity verification ({n_C0} random C0 x {n_delta} deltas)\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n    t0 = time.time()\\\\n\\\\n    param = LinearInterpolation()\\\\n    rng = np.random.default_rng(123)\\\\n    K = 3\\\\n\\\\n    p_A = np.array([0.4, 0.35, 0.25])\\\\n    alpha_cf = 0.5; beta_T = 1.0\\\\n    beta_A = np.array([0.8, -0.3])\\\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\\\n    tau_true_col = COLLIDER_PARAMS['tau']\\\\n\\\\n    violations = {\\\\\\\"confounding\\\\\\\": [], \\\\\\\"mediation\\\\\\\": [], \\\\\\\"collider\\\\\\\": []}\\\\n\\\\n    for s in range(n_C0):\\\\n        C0 = random_C0(K, rng)\\\\n        dmin, dmax = param.delta_range(C0)\\\\n        deltas = np.linspace(dmin, dmax, n_delta)\\\\n\\\\n        # Confounding: |bias| should increase\\\\n        tau_cf = np.array([plim_confounding(param(C0, d), p_A, alpha_cf,\\\\n                           beta_T, beta_A, sigma_T)[1] for d in deltas])\\\\n        bias_cf = np.abs(tau_cf - beta_T)\\\\n        diffs_cf = np.diff(bias_cf)\\\\n        if np.any(diffs_cf < -1e-8):\\\\n            violations[\\\\\\\"confounding\\\\\\\"].append((s, np.min(diffs_cf)))\\\\n\\\\n        # Mediation: |bias| should increase\\\\n        tau_m = np.array([plim_mediation(param(C0, d), beta_med, tau_med)[1]\\\\n                          for d in deltas])\\\\n        bias_m = np.abs(tau_m - tau_med)\\\\n        diffs_m = np.diff(bias_m)\\\\n        if np.any(diffs_m < -1e-8):\\\\n            violations[\\\\\\\"mediation\\\\\\\"].append((s, np.min(diffs_m)))\\\\n\\\\n        # Collider: |collider_bias| should decrease\\\\n        tau_c = np.array([plim_collider(param(C0, d), st)[1] for d in deltas])\\\\n        bias_c = np.abs(tau_c - tau_true_col)\\\\n        diffs_c = np.diff(bias_c)\\\\n        if np.any(diffs_c > 1e-8):\\\\n            violations[\\\\\\\"collider\\\\\\\"].append((s, np.max(diffs_c)))\\\\n\\\\n        if (s + 1) % 200 == 0:\\\\n            print(f\\\\\\\"  ... {s+1}/{n_C0}\\\\\\\")\\\\n\\\\n    for topo in [\\\\\\\"confounding\\\\\\\", \\\\\\\"mediation\\\\\\\", \\\\\\\"collider\\\\\\\"]:\\\\n        v = violations[topo]\\\\n        direction = \\\\\\\"increasing\\\\\\\" if topo != \\\\\\\"collider\\\\\\\" else \\\\\\\"decreasing\\\\\\\"\\\\n        print(f\\\\\\\"  {topo}: {len(v)}/{n_C0} violations (expected |bias| {direction})\\\\\\\")\\\\n        if v:\\\\n            worst = max(v, key=lambda x: abs(x[1]))\\\\n            print(f\\\\\\\"    worst: scenario {worst[0]}, max|delta_bias|={worst[1]:.2e}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"  Time: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n\\\\n# ============================================================================\\\\n# Part 4: Sharpness Verification\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.24}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nplan_004: ASV Framework v2\\n方案A: C(delta) = (1-delta)I + delta*C0, delta in [0, delta_max]\\ndelta_max = min(1/(1-min_diag(C0)), 10)  -- supports delta>1\\n\\n双方向:\\n  - Vulnerability (confounding, mediation): |bias| increases with delta, ASV = sign-flip delta\\n  - Protection (collider): collider bias decreases with delta, ASV = delta where bias < threshold\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nimport time\\nfrom abc import ABC, abstractmethod\\n\\n\\n# ============================================================================\\n# Utilities\\n# ============================================================================\\n\\ndef softmax(x):\\n    e = np.exp(x - x.max())\\n    return e / e.sum()\\n\\n\\ndef p_cat(t, g, d):\\n    return softmax(g + d * t)\\n\\n\\ndef generate_Astar(A, C, rng):\\n    probs = C[:, A]\\n    cum = np.cumsum(probs, axis=0)\\n    u = rng.uniform(size=len(A))\\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\\n\\n\\ndef softmax_sample(logits, rng):\\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\\n    cum = np.cumsum(probs, axis=1)\\n    u = rng.uniform(size=logits.shape[0])\\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\\n\\n\\ndef check_column_stochastic(C, tol=1e-6):\\n    assert np.all(C >= -tol), f\\\"Negative entries in C: min={C.min()}\\\"\\n    col_sums = C.sum(axis=0)\\n    assert np.allclose(col_sums, 1.0, atol=tol), f\\\"Column sums != 1: {col_sums}\\\"\\n\\n\\ndef ols_with_dummies(Y, T, Astar, K=3):\\n    N = len(Y)\\n    D = np.zeros((N, K - 1))\\n    for k in range(1, K):\\n        D[:, k - 1] = (Astar == k).astype(float)\\n    X = np.column_stack([np.ones(N), T, D])\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\\n    except np.linalg.LinAlgError:\\n        beta = np.full(X.shape[1], np.nan)\\n        se = np.full(X.shape[1], np.nan)\\n    return beta, se\\n\\n\\n# ============================================================================\\n# C(delta) Parameterization\\n# ============================================================================\\n\\nclass ConfusionParameterization(ABC):\\n    @abstractmethod\\n    def __call__(self, C0, delta):\\n        pass\\n\\n    @abstractmethod\\n    def delta_range(self, C0=None):\\n        pass\\n\\n\\nclass LinearInterpolation(ConfusionParameterization):\\n    \\\"\\\"\\\"C(delta) = (1-delta)I + delta*C0. delta>1 = error worse than observed.\\\"\\\"\\\"\\n\\n    def __call__(self, C0, delta):\\n        K = C0.shape[0]\\n        C_d = (1 - delta) * np.eye(K) + delta * C0\\n        C_d = np.maximum(C_d, 0.0)\\n        col_sums = C_d.sum(axis=0)\\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\\n        C_d = C_d / col_sums\\n        return C_d\\n\\n    def delta_range(self, C0=None):\\n        if C0 is None:\\n            return (0.0, 5.0)\\n        min_diag = np.diag(C0).min()\\n        if min_diag >= 1.0:\\n            return (0.0, 10.0)\\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\\n        return (0.0, delta_max)\\n\\n\\n# ============================================================================\\n# DAG 1: CONFOUNDING  A -> T, A -> Y, T -> Y\\n# ============================================================================\\n\\ndef plim_confounding(C, p_A, alpha, beta_T, beta_A, sigma_T):\\n    mu = sigma_T\\n    ET = np.sum(p_A * mu)\\n    ET2 = np.sum(p_A * (mu**2 + 1))\\n    q = C @ p_A\\n    qt = C @ (p_A * mu)\\n    EZZ = np.array([\\n        [1,    ET,    q[1],   q[2]  ],\\n        [ET,   ET2,   qt[1],  qt[2] ],\\n        [q[1], qt[1], q[1],   0     ],\\n        [q[2], qt[2], 0,      q[2]  ]])\\n    EZX = np.array([\\n        [1,    ET,           p_A[1],         p_A[2]        ],\\n        [ET,   ET2,          p_A[1]*mu[1],   p_A[2]*mu[2]  ],\\n        [q[1], qt[1],        C[1,1]*p_A[1],  C[1,2]*p_A[2] ],\\n        [q[2], qt[2],        C[2,1]*p_A[1],  C[2,2]*p_A[2] ]])\\n    b = np.array([alpha, beta_T, beta_A[0], beta_A[1]])\\n    try:\\n        retur\\n\\n... [截断: 输出过长，省略 11393 字符] ...\\n\\nbeta_T = 1.0\\n    beta_A = np.array([0.8, -0.3])\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\n    tau_true_col = COLLIDER_PARAMS['tau']\\n\\n    print(f\\\"\\\\n{'C_structure':<18} {'Conf(V)':>10} {'Med(V)':>10} {'Coll(P)':>10}  {'d_max':>8}\\\")\\n    print(\\\"-\\\" * 62)\\n\\n    for name, C0 in structures.items():\\n        check_column_stochastic(C0)\\n        _, dmax = param.delta_range(C0)\\n\\n        r_cf = compute_asv(plim_confounding,\\n                           dict(p_A=p_A, alpha=alpha_cf, beta_T=beta_T,\\n                                beta_A=beta_A, sigma_T=sigma_T),\\n                           C0, param, direction=\\\"vulnerability\\\")\\n\\n        r_med = compute_asv(plim_mediation,\\n                            dict(beta=beta_med, tau=tau_med),\\n                            C0, param, direction=\\\"vulnerability\\\")\\n\\n        r_col = compute_asv(plim_collider, dict(precomp=st),\\n                            C0, param, direction=\\\"protection\\\",\\n                            tau_true=tau_true_col)\\n\\n        def fmt(v):\\n            return f\\\"{v:.3f}\\\" if v is not None else \\\"None\\\"\\n\\n        asv_col_str = fmt(r_col['asv']) if r_col['asv'] is not None else \\\"None*\\\"\\n        print(f\\\"{name:<18} {fmt(r_cf['asv']):>10} {fmt(r_med['asv']):>10} {asv_col_str:>10}  {dmax:>8.1f}\\\")\\n\\n    print(\\\"\\\\n* Collider ASV=None: protection -- collider bias persists across full delta range\\\")\\n\\n\\n# ============================================================================\\n# Part 3: Monotonicity Verification\\n# ============================================================================\\n\\ndef part3_monotonicity(st, n_C0=1000, n_delta=100):\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(f\\\"PART 3: Monotonicity verification ({n_C0} random C0 x {n_delta} deltas)\\\")\\n    print(\\\"=\\\" * 70)\\n    t0 = time.time()\\n\\n    param = LinearInterpolation()\\n    rng = np.random.default_rng(123)\\n    K = 3\\n\\n    p_A = np.array([0.4, 0.35, 0.25])\\n    alpha_cf = 0.5; beta_T = 1.0\\n    beta_A = np.array([0.8, -0.3])\\n    sigma_T = np.array([0.0, 1.0, -0.5])\\n    beta_med = np.array([0.0, 1.0, -0.5]); tau_med = 0.5\\n    tau_true_col = COLLIDER_PARAMS['tau']\\n\\n    violations = {\\\"confounding\\\": [], \\\"mediation\\\": [], \\\"collider\\\": []}\\n\\n    for s in range(n_C0):\\n        C0 = random_C0(K, rng)\\n        dmin, dmax = param.delta_range(C0)\\n        deltas = np.linspace(dmin, dmax, n_delta)\\n\\n        # Confounding: |bias| should increase\\n        tau_cf = np.array([plim_confounding(param(C0, d), p_A, alpha_cf,\\n                           beta_T, beta_A, sigma_T)[1] for d in deltas])\\n        bias_cf = np.abs(tau_cf - beta_T)\\n        diffs_cf = np.diff(bias_cf)\\n        if np.any(diffs_cf < -1e-8):\\n            violations[\\\"confounding\\\"].append((s, np.min(diffs_cf)))\\n\\n        # Mediation: |bias| should increase\\n        tau_m = np.array([plim_mediation(param(C0, d), beta_med, tau_med)[1]\\n                          for d in deltas])\\n        bias_m = np.abs(tau_m - tau_med)\\n        diffs_m = np.diff(bias_m)\\n        if np.any(diffs_m < -1e-8):\\n            violations[\\\"mediation\\\"].append((s, np.min(diffs_m)))\\n\\n        # Collider: |collider_bias| should decrease\\n        tau_c = np.array([plim_collider(param(C0, d), st)[1] for d in deltas])\\n        bias_c = np.abs(tau_c - tau_true_col)\\n        diffs_c = np.diff(bias_c)\\n        if np.any(diffs_c > 1e-8):\\n            violations[\\\"collider\\\"].append((s, np.max(diffs_c)))\\n\\n        if (s + 1) % 200 == 0:\\n            print(f\\\"  ... {s+1}/{n_C0}\\\")\\n\\n    for topo in [\\\"confounding\\\", \\\"mediation\\\", \\\"collider\\\"]:\\n        v = violations[topo]\\n        direction = \\\"increasing\\\" if topo != \\\"collider\\\" else \\\"decreasing\\\"\\n        print(f\\\"  {topo}: {len(v)}/{n_C0} violations (expected |bias| {direction})\\\")\\n        if v:\\n            worst = max(v, key=lambda x: abs(x[1]))\\n            print(f\\\"    worst: scenario {worst[0]}, max|delta_bias|={worst[1]:.2e}\\\")\\n\\n    print(f\\\"  Time: {time.time()-t0:.1f}s\\\")\\n\\n\\n# ============================================================================\\n# Part 4: Sharpness Verification\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"
    }
  }
}
```

</details>

---
