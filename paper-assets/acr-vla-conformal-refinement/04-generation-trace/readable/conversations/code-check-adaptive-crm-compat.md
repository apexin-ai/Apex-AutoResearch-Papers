# code check adaptive crm compat

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_code_check-adaptive-crm-compat_20260522T191036.jsonl`
- **Structured JSON:** [`2704d9cf993f64854aa7.json`](../../sessions/27/2704d9cf993f64854aa7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-22T19:12:23.791077+00:00_

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
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
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

_source line 2 · 2026-05-22T19:12:23.791441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T19:12:23.791635+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T19:12:23.791772+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/src/ -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/src/ -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T19:12:23.792060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n  2. Load SmolVLA (frozen) + CRM\\n  3. For each task, rollout N times:\\n     a. Reset env\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n        → combine refined pose with gripper → execute 7D action\\n     c. Record success/failure\\n  4. Report per-task and overall success rate\\n\\nBaselines:\\n  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n  - \\\"adaptive_k\\\": Adaptive K — K=2 L2 probe, expand to K=10 + CRM obs_only if uncertain\\n\\nAdaptive K mode (--mode adaptive_k):\\n  Each step: generate K=2 samples, compute pairwise L2 distance.\\n  If L2 > threshold (high uncertainty): generate 8 more (total K=10),\\n    select argmin(L2 to mean), apply CRM obs_only correction (epsilon=0.2).\\n  If L2 <= threshold (low uncertainty): use mean of K=2, skip CRM.\\n\\nUsage:\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n\\\"\\\"\\\"\\nimport argparse\\nimport functools\\nbuiltins_print = print\\nprint = functools.partial(builtins_print, flush=True)\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\n
…[truncated 7295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T19:12:23.792386+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/src/__init__.py\\n/root/acr-vla-conformal-refinement/src/cgs.py\\n/root/acr-vla-conformal-refinement/src/aci.py\\n/root/acr-vla-conformal-refinement/src/crm.py\\n/root/acr-vla-conformal-refinement/src/train_crm.py\\n/root/acr-vla-conformal-refinement/src/evaluate.py\\n/root/acr-vla-conformal-refinement/src/utils.py\\n/root/acr-vla-conformal-refinement/src/smolvla_wrapper.py\\n/root/acr-vla-conformal-refinement/src/reconvla_baseline.py\\n/root/acr-vla-conformal-refinement/src/gated_crm.py\\n/root/acr-vla-conformal-refinement/src/compute_norm_stats.py\\n/root/acr-vla-conformal-refinement/src/calibrate_threshold.py\\n/root/acr-vla-conformal-refinement/src/calibrate_crm_signal.py\\n/root/acr-vla-conformal-refinement/src/pi05_wrapper.py\\n/root/acr-vla-conformal-refinement/src/openvla_oft_wrapper.py\\n/root/acr-vla-conformal-refinement/src/lerobot/__init__.py\\n/root/acr-vla-conformal-refinement/src/lerobot/__version__.py\\n/root/acr-vla-conformal-refinement/src/lerobot/types.py\\n/root/acr-vla-conformal-refinement/src/lerobot/async_inference/__init__.py\\n/root/acr-vla-conformal-refinement/src/lerobot/async_inference/configs.py\\n/root/acr-vla-conformal-refinement/src/lerobot/async_inference/constants.py\\n/root/acr-vla-conformal-refinement/src/lerobot/async_inference/helpers.py\\n/root/acr-vla-conformal-refinement/src/lerobot/async_inference/policy_server.py\\n/root/acr-vla-conformal-refinement/src/lerobot/async_inference/robot_client.py\\n/root/acr-vla-conformal-refinement/src/lerobot/cameras/__init__.py\\n/root/acr-vla-conformal-refinement/src/lerobot/cameras/camera.py\\n/root/acr-vla-conformal-refinement/src/lerobot/cameras/configs.py\\n/root/acr-vla-conformal-refinement/src/lerobot/cameras/utils.py\\n/root/acr-vla-conformal-refinement/src/lerobot/cameras/opencv/__init__.py\\n/root/acr-vla-conformal-refinement/src/lerobot/cameras/opencv/camera_opencv.py\\n/root/acr-vla-conform
…[truncated 6422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T19:12:23.792616+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"adaptive_conformal_crm\\|conformal_threshold\\|unc_head\\|uf_input\\|unc_dim\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"adaptive_conformal_crm\\|conformal_threshold\\|unc_head\\|uf_input\\|unc_dim\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T19:12:23.792761+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T19:12:23.792890+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/src/crm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/acr-vla-conformal-refinement/src/crm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T19:12:23.793060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nConformal Refinement Module (CRM).\\n\\nInput: base_action (30D, argmin-selected) + uncertainty_features (40D) + obs_features (960D from VLM)\\nOutput: refined_action (30D) = base_action + clipped_delta\\n\\nArchitecture: 2 hidden layers, dim 256, ReLU, residual connection.\\n\\\"\\\"\\\"\\nimport torch\\nimport torch.nn as nn\\n\\n\\nclass ConformalRefinementModule(nn.Module):\\n    \\\"\\\"\\\"Learn to refine VLA action predictions using structured uncertainty.\\\"\\\"\\\"\\n\\n    def __init__(self, action_dim: int = 30, uncertainty_dim: int = 40,\\n                 obs_dim: int = 960, hidden_dim: int = 256,\\n                 max_correction_norm: float = 1.42):\\n        \\\"\\\"\\\"\\n        Args:\\n            action_dim: flattened action dim (H_eff * D = 5 * 6 = 30)\\n            uncertainty_dim: CGS output dim (30 + 5 + 5 = 40), 0 for obs_only\\n            obs_dim: VLM encoder frozen output dim (960)\\n            hidden_dim: hidden layer dim\\n        \\\"\\\"\\\"\\n        super().__init__()\\n\\n        self.max_correction_norm = max_correction_norm\\n        self.uncertainty_dim = uncertainty_dim\\n        input_dim = action_dim + uncertainty_dim + obs_dim\\n\\n        self.register_buffer('input_mean', torch.zeros(input_dim))\\n        self.register_buffer('input_std', torch.ones(input_dim))\\n\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, hidden_dim),\\n            nn.ReLU(),\\n            nn.Linear(hidden_dim, hidden_dim),\\n            nn.ReLU(),\\n            nn.Linear(hidden_dim, action_dim),\\n        )\\n\\n        # Residual: output = base_action + delta. Init last layer near zero.\\n        nn.init.zeros_(self.net[-1].weight)\\n        nn.init.zeros_(self.net[-1].bias)\\n\\n    def forward(self, base_action: torch.Tensor, uncertainty_features: torch.Tensor,\\n                obs_features: torch.Tensor) -> torch.Tensor:\\n        \\\"\\\"\\\"\\n    
…[truncated 1279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T19:12:23.793216+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/src/aci.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/acr-vla-conformal-refinement/src/aci.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T19:12:23.793438+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nAdaptive Conformal Inference (ACI) 模块。\\n\\n在线更新 conformal coverage level alpha，使得实际覆盖率逼近目标覆盖率。\\n同时计算 COC (Change of Conformity) 信号，用于检测分布偏移。\\n\\n核心公式:\\n  alpha_{t+1} = alpha_t + gamma * (alpha_target - err_t)\\n  其中 err_t = 1 if ||a_expert - a_mean||_Mahal > q_t else 0\\n\\nCOC 信号:\\n  COC_t = |alpha_t - alpha_{t-w:t}.mean()| / alpha_{t-w:t}.std()\\n  高 COC → 分布正在快速变化 → CRM 应更激进地校正\\n\\\"\\\"\\\"\\nimport torch\\nimport numpy as np\\nfrom collections import deque\\n\\n\\nclass AdaptiveConformalInference:\\n    \\\"\\\"\\\"在线自适应 conformal prediction，维护动态 alpha 和 COC 信号。\\\"\\\"\\\"\\n    \\n    def __init__(self, alpha_target: float = 0.1, gamma: float = 0.005, window_size: int = 50):\\n        \\\"\\\"\\\"\\n        Args:\\n            alpha_target: 目标 miscoverage rate (1-alpha_target = coverage)\\n            gamma: alpha 更新步长\\n            window_size: COC 信号的滑动窗口大小\\n        \\\"\\\"\\\"\\n        self.alpha_target = alpha_target\\n        self.gamma = gamma\\n        self.window_size = window_size\\n        \\n        self.alpha = alpha_target  # 当前 alpha\\n        self.alpha_history = deque(maxlen=window_size)\\n        self.alpha_history.append(self.alpha)\\n    \\n    def update(self, expert_action: torch.Tensor, mean_action: torch.Tensor, \\n               cov_matrix: torch.Tensor, conformal_radius: float) -> dict:\\n        \\\"\\\"\\\"\\n        用一个新观测更新 alpha 并计算 COC。\\n        \\n        更新规则 (Gibbs & Candès 2021):\\n          alpha_{t+1} = alpha_t + gamma * (alpha_target - err_t)\\n          - err=1 (miss): alpha 减小 -> 降低 miscoverage 容忍 -> 放大 conformal set\\n          - err=0 (cover): alpha 增大 -> 提高 miscoverage 容忍 -> 缩小 conformal set\\n        \\n        Args:\\n            expert_action: (D,) 专家动作（训练时可用）\\n            mean_action: (D,) 预测均值动作\\n            cov_matrix: (D, D) 协方差矩阵\\n            conformal_radius: 当前 conformal radius q_t\\n            \\n        Returns:\\n       
…[truncated 1747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T19:12:23.793638+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"adaptive_conformal_crm\\|conformal_threshold\\|unc_head_crm\\|uf_input\\|unc_dim\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"adaptive_conformal_crm\\|conformal_threshold\\|unc_head_crm\\|uf_input\\|unc_dim\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T19:12:23.793775+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T19:12:23.793899+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "cat /root/acr-vla-conformal-refinement/src/gated_crm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "cat /root/acr-vla-conformal-refinement/src/gated_crm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T19:12:23.794087+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nGated Conformal Refinement Module (GatedCRM).\\n\\nExtends CRM with per-DOF uncertainty gating: correction is zeroed out on\\ndimensions where per-DOF std (from CGS) is below a threshold, preventing\\nover-correction on confident dimensions.\\n\\nArchitecture: identical MLP to CRM (2 hidden layers, dim 256, ReLU).\\nCompatible with existing CRM checkpoints — gate parameters are new, MLP\\nweights load directly via state_dict.\\n\\\"\\\"\\\"\\nimport torch\\nimport torch.nn as nn\\n\\n\\nclass GatedCRM(nn.Module):\\n    \\\"\\\"\\\"CRM with per-DOF uncertainty gating.\\n\\n    When per_dof_std[d] < gate_threshold for dimension d,\\n    correction[d] → 0 (pass-through base action).\\n    Only applies correction on high-uncertainty dimensions.\\n    \\\"\\\"\\\"\\n\\n    def __init__(self, action_dim: int = 30, uncertainty_dim: int = 40,\\n                 obs_dim: int = 960, hidden_dim: int = 256,\\n                 max_correction_norm: float = 1.42,\\n                 gate_threshold: float = 0.1,\\n                 gate_mode: str = 'hard',\\n                 gate_temperature: float = 0.05):\\n        \\\"\\\"\\\"\\n        Args:\\n            action_dim: flattened action dim (H_eff * D = 5 * 6 = 30)\\n            uncertainty_dim: CGS output dim (30 + 5 + 5 = 40)\\n            obs_dim: VLM encoder frozen output dim (960)\\n            hidden_dim: hidden layer dim\\n            max_correction_norm: L2 clipping bound for delta\\n            gate_threshold: per-DOF std below which correction is zeroed\\n            gate_mode: 'hard' (binary 0/1) or 'soft' (sigmoid scaling)\\n            gate_temperature: controls sigmoid sharpness in soft mode\\n        \\\"\\\"\\\"\\n        super().__init__()\\n\\n        self.action_dim = action_dim\\n        self.max_correction_norm = max_correction_norm\\n        self.uncertainty_dim = uncertainty_dim\\n        self.gate_threshold = gate_threshold\\n        self.
…[truncated 2542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T19:12:23.794279+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"adaptive_conformal_crm\\|conformal_threshold\\|uf_input\\|unc_dim\\|unc_head\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"adaptive_conformal_crm\\|conformal_threshold\\|uf_input\\|unc_dim\\|unc_head\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T19:12:23.794419+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T19:12:23.794558+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n -E \"adaptive_conformal_crm|conformal_threshold|uf_input|unc_dim|unc_head\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n -E \"adaptive_conformal_crm|conformal_threshold|uf_input|unc_dim|unc_head\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T19:12:23.794685+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T19:12:23.794819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"adaptive_conformal_crm\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"adaptive_conformal_crm\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T19:12:23.794969+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"78:                   choices=[\\\"vla_only\\\", \\\"crm_scalar\\\", \\\"crm_perdof\\\", \\\"acr_vla\\\", \\\"crm_obs_only\\\", \\\"reconvla\\\", \\\"random_selection\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"])\\n535:    if args.mode in (\\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\") and args.checkpoint is None:\\n576:    if args.mode in (\\\"crm_scalar\\\", \\\"crm_perdof\\\", \\\"acr_vla\\\", \\\"crm_obs_only\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"):\\n580:        if args.mode in (\\\"crm_obs_only\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"):\\n603:    if args.mode in (\\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\") and args.max_correction_norm is None:\\n669:            elif args.mode == \\\"adaptive_conformal_crm\\\":\\n707:                if args.mode in (\\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"):\\n787:    if args.mode == \\\"adaptive_conformal_crm\\\" and all_unc_head_meta:\\n829:        elif args.mode == \\\"adaptive_conformal_crm\\\":\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T19:12:23.795108+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"conformal_threshold\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"conformal_threshold\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T19:12:23.795242+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"115:    p.add_argument(\\\"--conformal_threshold\\\", type=float, default=0.074855,\\n451:                                 conformal_threshold, step_metadata, obs_proj=None):\\n477:    triggered = uncertainty > conformal_threshold\\n672:                    args.conformal_threshold, rollout_meta, obs_proj=obs_proj\\n793:            \\\"tau\\\": args.conformal_threshold,\\n830:            adaptive_tag = f\\\"_tau{args.conformal_threshold}\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T19:12:23.795391+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n \"unc_dim\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n \"unc_dim\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T19:12:23.795516+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"581:            unc_dim = 0\\n583:            unc_dim = 3\\n585:            unc_dim = CORRECTION_DIM * H_EFF + H_EFF + H_EFF  # 40\\n592:            uncertainty_dim=unc_dim,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T19:12:23.795653+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "sed -n '440,510p' /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "sed -n '440,510p' /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T19:12:23.795775+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T19:12:23.795891+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "sed -n '570,620p' /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "sed -n '570,620p' /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T19:12:23.796007+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T19:12:23.796121+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "sed -n '650,730p' /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "sed -n '650,730p' /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T19:12:23.796282+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T19:12:23.796428+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "head -n 510 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "head -n 510 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T19:12:23.796681+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n  2. Load SmolVLA (frozen) + CRM\\n  3. For each task, rollout N times:\\n     a. Reset env\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n        → combine refined pose with gripper → execute 7D action\\n     c. Record success/failure\\n  4. Report per-task and overall success rate\\n\\nBaselines:\\n  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n  - \\\"adaptive_k\\\": Adaptive K — K=2 L2 probe, expand to K=10 + CRM obs_only if uncertain\\n\\nAdaptive K mode (--mode adaptive_k):\\n  Each step: generate K=2 samples, compute pairwise L2 distance.\\n  If L2 > threshold (high uncertainty): generate 8 more (total K=10),\\n    select argmin(L2 to mean), apply CRM obs_only correction (epsilon=0.2).\\n  If L2 <= threshold (low uncertainty): use mean of K=2, skip CRM.\\n\\nUsage:\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n\\\"\\\"\\\"\\nimport argparse\\nimport functools\\nbuiltins_print = print\\nprint = functools.partial(builtins_print, flush=True)\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\n
…[truncated 7071 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T19:12:23.796867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "tail -n +570 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "tail -n +570 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T19:12:23.797148+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"            K=args.k_full, horizon=H_EFF, action_dim=CORRECTION_DIM)\\n        print(f\\\"[eval] Adaptive K: k_init={args.k_init}, k_full={args.k_full}, \\\"\\n              f\\\"threshold={args.adaptive_threshold}\\\")\\n\\n    # CRM (if needed)\\n    crm = None\\n    if args.mode in (\\\"crm_scalar\\\", \\\"crm_perdof\\\", \\\"acr_vla\\\", \\\"crm_obs_only\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"):\\n        if args.checkpoint is None:\\n            raise ValueError(\\\"--checkpoint required for CRM modes\\\")\\n\\n        if args.mode in (\\\"crm_obs_only\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"):\\n            unc_dim = 0\\n        elif args.mode == \\\"crm_scalar\\\":\\n            unc_dim = 3\\n        else:  # crm_perdof or acr_vla\\n            unc_dim = CORRECTION_DIM * H_EFF + H_EFF + H_EFF  # 40\\n\\n        global _UNIFIED_OBS_DIM\\n        _UNIFIED_OBS_DIM = args.unified_obs_dim\\n\\n        crm = ConformalRefinementModule(\\n            action_dim=H_EFF * CORRECTION_DIM,\\n            uncertainty_dim=unc_dim,\\n            obs_dim=args.unified_obs_dim or args.obs_dim,\\n            hidden_dim=args.hidden_dim,\\n        ).to(device)\\n        crm.load_state_dict(torch.load(args.checkpoint, map_location=device,\\n                                        weights_only=True))\\n        crm.eval()\\n        print(f\\\"[eval] CRM loaded from {args.checkpoint} \\\"\\n              f\\\"({crm.count_parameters():,} params)\\\")\\n\\n    # Default max_correction_norm=0.2 for adaptive_k mode\\n    if args.mode in (\\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\") and args.max_correction_norm is None:\\n        args.max_correction_norm = 0.2\\n\\n    # Override max_correction_norm if specified\\n    if args.max_correction_norm is not None and crm is not None:\\n        crm.max_correction_norm = args.
…[truncated 7161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T19:12:23.797368+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -n -A 5 \"adaptive_conformal_crm\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "grep -n -A 5 \"adaptive_conformal_crm\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T19:12:23.797571+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"78:                   choices=[\\\"vla_only\\\", \\\"crm_scalar\\\", \\\"crm_perdof\\\", \\\"acr_vla\\\", \\\"crm_obs_only\\\", \\\"reconvla\\\", \\\"random_selection\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"])\\n79-    p.add_argument(\\\"--baseline_mode\\\", type=str, default=\\\"single\\\",\\n80-                   choices=[\\\"single\\\", \\\"mean\\\"],\\n81-                   help=\\\"vla_only baseline: single (K=1) or mean (K=10 avg)\\\")\\n82-    p.add_argument(\\\"--smolvla_path\\\", type=str, default=\\\"/root/autodl-tmp/models/smolvla_libero/\\\")\\n83-    p.add_argument(\\\"--model\\\", type=str, default=\\\"smolvla\\\",\\n--\\n535:    if args.mode in (\\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\") and args.checkpoint is None:\\n536-        args.checkpoint = \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\"\\n537-        print(f\\\"[eval] {args.mode}: using default CRM checkpoint {args.checkpoint}\\\")\\n538-\\n539-    print(f\\\"[eval] Mode: {args.mode}, benchmark: {args.benchmark}\\\")\\n540-\\n--\\n576:    if args.mode in (\\\"crm_scalar\\\", \\\"crm_perdof\\\", \\\"acr_vla\\\", \\\"crm_obs_only\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"):\\n577-        if args.checkpoint is None:\\n578-            raise ValueError(\\\"--checkpoint required for CRM modes\\\")\\n579-\\n580:        if args.mode in (\\\"crm_obs_only\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"):\\n581-            unc_dim = 0\\n582-        elif args.mode == \\\"crm_scalar\\\":\\n583-            unc_dim = 3\\n584-        else:  # crm_perdof or acr_vla\\n585-            unc_dim = CORRECTION_DIM * H_EFF + H_EFF + H_EFF  # 40\\n--\\n603:    if args.mode in (\\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\") and args.max_correction_norm is None:\
…[truncated 1910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-22T19:12:23.797778+00:00_

已获取完整信息。以下是分析结果：

---

## 报告

### 1. `adaptive_conformal_crm` 模式完整逻辑流程

**函数**: `select_action_conformal_crm()` (evaluate.py:451-508)

每一步执行流程：
1. 生成 **K=2** 个 VLA 样本
2. 提取两个样本的 6D pose (各 30 维 = H_eff×6)
3. 计算 uncertainty = `||a1 - a2||₂`（两个样本的 L2 距离）
4. 选取离 centroid 更近的样本作为 base_action
5. **判定 gate**: `triggered = uncertainty > conformal_threshold`
   - **uncertain** (triggered=True): 调用 `crm(base_action, None, obs_features)` 做 CRM 修正
   - **confident** (triggered=False): 直接用 selected_pose，跳过 CRM

**CRM 加载**: unc_dim=0，CRM 以 `(base_action, None, obs_features)` 调用 — uncertainty_features 传 None。

### 2. 是否兼容 obs_only (unc_dim=0)

**完全兼容。**

原因：
- CRM 加载时 `adaptive_conformal_crm` 走的分支和 `crm_obs_only` 完全相同：`unc_dim = 0` (evaluate.py:580-581)
- `select_action_conformal_crm()` 调用 CRM 时传 `uncertainty_features=None` (evaluate.py:498)
- `ConformalRefinementModule.forward()` 处理 `uncertainty_features=None` 的逻辑已实现 (crm.py:47-50)：当 None 时直接 cat `[base_action, obs_features]`，input_dim = 30+960 = 990，与 unc_dim=0 的 checkpoint 匹配
- **uncertainty 的计算完全基于 K=2 样本的 L2 距离**（外部计算），不依赖 CRM 的 uncertainty head 输出

### 3. 结论

**无需修复。** `adaptive_conformal_crm` 模式的 adaptive gate 基于 K=2 样本 disagreement（L2 距离），不使用 CRM 内部的 uncertainty 输出。CRM 以 obs_only 模式 (unc_dim=0) 加载，checkpoint 完全匹配。代码路径已正确实现，可以直接用于评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_check-adaptive-crm-compat_20260522T191036"
}
```

</details>

---
