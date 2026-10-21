# research p3 mode equivalence

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_research_p3-mode-equivalence_20260515T033506.jsonl`
- **Structured JSON:** [`56379fa26ae55101ae95.json`](../../sessions/56/56379fa26ae55101ae95.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-15T03:36:45.438903+00:00_

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
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
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

_source line 2 · 2026-05-15T03:36:45.439234+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T03:36:45.439491+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/src -type f -name \"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/src -type f -name \"*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T03:36:45.439647+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T03:36:45.439789+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/src/__init__.py\\n/root/acr-vla-conformal-refinement/src/cgs.py\\n/root/acr-vla-conformal-refinement/src/aci.py\\n/root/acr-vla-conformal-refinement/src/crm.py\\n/root/acr-vla-conformal-refinement/src/utils.py\\n/root/acr-vla-conformal-refinement/src/smolvla_wrapper.py\\n/root/acr-vla-conformal-refinement/src/train_crm.py\\n/root/acr-vla-conformal-refinement/src/evaluate.py\\n/root/acr-vla-conformal-refinement/src/reconvla_baseline.py\\n/root/acr-vla-conformal-refinement/src/sanity_check_reset.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T03:36:45.440045+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n  2. Load SmolVLA (frozen) + CRM\\n  3. For each task, rollout N times:\\n     a. Reset env\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n        → combine refined pose with gripper → execute 7D action\\n     c. Record success/failure\\n  4. Report per-task and overall success rate\\n\\nBaselines:\\n  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n\\nUsage:\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n\\\"\\\"\\\"\\nimport argparse\\nimport functools\\nbuiltins_print = print\\nprint = functools.partial(builtins_print, flush=True)\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\nfrom pathlib import Path\\n\\nimport torch\\nimport numpy as np\\nfrom robosuite.utils.transform_utils import quat2axisangle\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom cgs import ConformilizedGaussianScoring\\nfrom crm import ConformalRefinementModule\\nfrom aci import AdaptiveConformalInference\\nfrom utils import set_seed, CORRECTION_DIM, FULL_ACTION_DIM, H_EFF, OBS_DIM\\nfrom reconvla_b
…[truncated 7206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T03:36:45.440328+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "head -250 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "head -250 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T03:36:45.440601+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n  2. Load SmolVLA (frozen) + CRM\\n  3. For each task, rollout N times:\\n     a. Reset env\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n        → combine refined pose with gripper → execute 7D action\\n     c. Record success/failure\\n  4. Report per-task and overall success rate\\n\\nBaselines:\\n  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n\\nUsage:\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n\\\"\\\"\\\"\\nimport argparse\\nimport functools\\nbuiltins_print = print\\nprint = functools.partial(builtins_print, flush=True)\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\nfrom pathlib import Path\\n\\nimport torch\\nimport numpy as np\\nfrom robosuite.utils.transform_utils import quat2axisangle\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom cgs import ConformilizedGaussianScoring\\nfrom crm import ConformalRefinementModule\\nfrom aci import AdaptiveConformalInference\\nfrom utils import set_seed, CORRECTION_DIM, FULL_ACTION_DIM, H_EFF, OBS_DIM\\nfrom reconvla_b
…[truncated 7083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T03:36:45.440795+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -n +250 /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -n +250 /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T03:36:45.441014+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        args.checkpoint = args.crm_checkpoint\\n\\n    print(f\\\"[eval] Mode: {args.mode}, benchmark: {args.benchmark}\\\")\\n\\n    # Load SmolVLA\\n    from smolvla_wrapper import SmolVLAWrapper\\n    print(f\\\"[eval] Loading SmolVLA from {args.smolvla_path}...\\\")\\n    wrapper = SmolVLAWrapper(args.smolvla_path, device=str(device))\\n\\n    # CGS — operates on 6D pose only (CORRECTION_DIM)\\n    cgs = ConformilizedGaussianScoring(K=args.K, horizon=H_EFF, action_dim=CORRECTION_DIM)\\n\\n    # CRM (if needed)\\n    crm = None\\n    if args.mode in (\\\"crm_scalar\\\", \\\"crm_perdof\\\", \\\"acr_vla\\\", \\\"crm_obs_only\\\"):\\n        if args.checkpoint is None:\\n            raise ValueError(\\\"--checkpoint required for CRM modes\\\")\\n\\n        if args.mode == \\\"crm_obs_only\\\":\\n            unc_dim = 0\\n        elif args.mode == \\\"crm_scalar\\\":\\n            unc_dim = 3\\n        else:  # crm_perdof or acr_vla\\n            unc_dim = CORRECTION_DIM * H_EFF + H_EFF + H_EFF  # 40\\n\\n        crm = ConformalRefinementModule(\\n            action_dim=H_EFF * CORRECTION_DIM,\\n            uncertainty_dim=unc_dim,\\n            obs_dim=args.obs_dim,\\n            hidden_dim=args.hidden_dim,\\n        ).to(device)\\n        crm.load_state_dict(torch.load(args.checkpoint, map_location=device,\\n                                        weights_only=True))\\n        crm.eval()\\n        print(f\\\"[eval] CRM loaded from {args.checkpoint} \\\"\\n              f\\\"({crm.count_parameters():,} params)\\\")\\n\\n    # Override max_correction_norm if specified\\n    if args.max_correction_norm is not None and crm is not None:\\n        crm.max_correction_norm = args.max_correction_norm\\n        print(f\\\"[eval] Override max_correction_norm = {args.max_correction_norm}\\\")\\n\\n    # ACI for online alpha tracking\\n    aci = AdaptiveConformalInference()\\n\\n    # Load LIBERO envs\\n    print(f\\\"[eva
…[truncated 3736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T03:36:45.441176+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/src/crm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/src/crm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T03:36:45.441380+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nConformal Refinement Module (CRM).\\n\\nInput: base_action (30D, argmin-selected) + uncertainty_features (40D) + obs_features (960D from VLM)\\nOutput: refined_action (30D) = base_action + clipped_delta\\n\\nArchitecture: 2 hidden layers, dim 256, ReLU, residual connection.\\n\\\"\\\"\\\"\\nimport torch\\nimport torch.nn as nn\\n\\n\\nclass ConformalRefinementModule(nn.Module):\\n    \\\"\\\"\\\"Learn to refine VLA action predictions using structured uncertainty.\\\"\\\"\\\"\\n\\n    def __init__(self, action_dim: int = 30, uncertainty_dim: int = 40,\\n                 obs_dim: int = 960, hidden_dim: int = 256,\\n                 max_correction_norm: float = 1.42):\\n        \\\"\\\"\\\"\\n        Args:\\n            action_dim: flattened action dim (H_eff * D = 5 * 6 = 30)\\n            uncertainty_dim: CGS output dim (30 + 5 + 5 = 40), 0 for obs_only\\n            obs_dim: VLM encoder frozen output dim (960)\\n            hidden_dim: hidden layer dim\\n        \\\"\\\"\\\"\\n        super().__init__()\\n\\n        self.max_correction_norm = max_correction_norm\\n        self.uncertainty_dim = uncertainty_dim\\n        input_dim = action_dim + uncertainty_dim + obs_dim\\n\\n        self.register_buffer('input_mean', torch.zeros(input_dim))\\n        self.register_buffer('input_std', torch.ones(input_dim))\\n\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, hidden_dim),\\n            nn.ReLU(),\\n            nn.Linear(hidden_dim, hidden_dim),\\n            nn.ReLU(),\\n            nn.Linear(hidden_dim, action_dim),\\n        )\\n\\n        # Residual: output = base_action + delta. Init last layer near zero.\\n        nn.init.zeros_(self.net[-1].weight)\\n        nn.init.zeros_(self.net[-1].bias)\\n\\n    def forward(self, base_action: torch.Tensor, uncertainty_features: torch.Tensor,\\n                obs_features: torch.Tensor) -> torch.Tensor:\\n        \\\"\\\"\\\"\\n    
…[truncated 1279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T03:36:45.441550+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/src/utils.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/src/utils.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T03:36:45.441789+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nACR-VLA utility functions.\\n\\n- LIBERO dataset loading\\n- Synthetic augmentation (known noise injection for OOD simulation)\\n- Evaluation metrics\\n- Checkpoint management\\n\\\"\\\"\\\"\\nimport torch\\nimport numpy as np\\nfrom pathlib import Path\\nimport h5py\\nimport glob\\n\\n\\nCORRECTION_DIM = 6   # 6D pose — CRM corrects only pose, not gripper\\nFULL_ACTION_DIM = 7  # 6D pose + 1D gripper (LIBERO env action space)\\nH_EFF = 5            # effective horizon (truncated from chunk_size=50)\\nCHUNK_SIZE = 50      # SmolVLA native chunk_size\\nOBS_DIM = 960        # VLM hidden_size\\nMAX_STATE_DIM = 32\\nMAX_ACTION_DIM = 32\\n\\nBENCHMARK_MAP = {\\n    \\\"spatial\\\": \\\"libero_spatial\\\",\\n    \\\"object\\\": \\\"libero_object\\\",\\n    \\\"goal\\\": \\\"libero_goal\\\",\\n    \\\"long\\\": \\\"libero_10\\\",\\n    \\\"90\\\": \\\"libero_90\\\",\\n}\\n\\n\\ndef set_seed(seed: int):\\n    torch.manual_seed(seed)\\n    np.random.seed(seed)\\n    if torch.cuda.is_available():\\n        torch.cuda.manual_seed_all(seed)\\n        torch.backends.cudnn.deterministic = True\\n        torch.backends.cudnn.benchmark = False\\n\\n\\ndef load_libero_demos(benchmark_name: str,\\n                      data_dir: str = \\\"/root/autodl-tmp/libero_data/\\\",\\n                      max_demos_per_task: int = 50):\\n    \\\"\\\"\\\"\\n    Load LIBERO demo trajectories from HDF5 files.\\n\\n    Returns:\\n        list of dicts with keys:\\n            - \\\"agentview_rgb\\\": (T, 128, 128, 3) uint8\\n            - \\\"eye_in_hand_rgb\\\": (T, 128, 128, 3) uint8\\n            - \\\"joint_states\\\": (T, 7) float\\n            - \\\"ee_states\\\": (T, 8) float — eef_pos(3) + eef_axisangle(3) + gripper_qpos(2)\\n            - \\\"actions\\\": (T, 7) float (6D pose + 1D gripper)\\n            - \\\"task_name\\\": str\\n    \\\"\\\"\\\"\\n    folder = BENCHMARK_MAP.get(benchmark_name, benchmark_name)\\n    
…[truncated 5773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T03:36:45.441971+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/src/cgs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/src/cgs.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T03:36:45.442159+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nConformalized Gaussian Scoring (CGS) module.\\n\\nInput: K flow-matching samples, shape (K, H_eff, D) where D=CORRECTION_DIM=6, H_eff=5.\\n       Accepts (K, chunk_size, D') and auto-truncates to (K, H_eff, action_dim).\\n\\nOutput:\\n  - uncertainty_features: (action_dim*H_eff + H_eff + H_eff) tensor\\n    [per_dof_std(30), conformal_radius(5), log_volume(5)]\\n  - mean_action: (H_eff*action_dim) tensor (K samples mean, flattened)\\n\\\"\\\"\\\"\\nimport torch\\nimport numpy as np\\nfrom sklearn.covariance import LedoitWolf\\n\\ntry:\\n    from utils import CORRECTION_DIM\\nexcept ImportError:\\n    from .utils import CORRECTION_DIM\\n\\n\\nclass ConformilizedGaussianScoring:\\n    \\\"\\\"\\\"Compute structured uncertainty features from K flow-matching samples (pose only).\\\"\\\"\\\"\\n\\n    def __init__(self, K: int = 10, horizon: int = 5, action_dim: int = CORRECTION_DIM,\\n                 alpha: float = 0.5, chunk_size: int = 50):  # BugFix W3: 0.1→0.5, K=10时0.1导致quantile=max\\n        self.K = K\\n        self.horizon = horizon       # H_eff = 5\\n        self.action_dim = action_dim  # 6D pose (no gripper)\\n        self.alpha = alpha\\n        self.chunk_size = chunk_size\\n\\n    def compute_features(self, samples: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:\\n        \\\"\\\"\\\"\\n        Args:\\n            samples: (K, T, D') where T >= H_eff and D' >= action_dim.\\n                     Auto-truncates to (K, H_eff, action_dim).\\n        Returns:\\n            uncertainty_features: (action_dim*H_eff + H_eff + H_eff,)\\n            mean_action: (H_eff * action_dim,) — flattened mean over K samples\\n        \\\"\\\"\\\"\\n        if samples.shape[1] > self.horizon:\\n            samples = samples[:, :self.horizon, :]\\n        if samples.shape[2] > self.action_dim:\\n            samples = samples[:, :, :self.action_dim]\\n\\n        assert samples.shape == (self.K, self.hor
…[truncated 2531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_p3-mode-equivalence_20260515T033506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T03:36:45.442411+00:00_

全部代码已读完，以下是分析报告。

---

## 各 mode 代码路径对比

### 路由逻辑

`evaluate()` 中的分派：

| mode | action function | 进入条件 |
|------|----------------|---------|
| `vla_only` | `select_action_vla_only()` | `== "vla_only"` |
| `reconvla` | `select_action_reconvla()` | `== "reconvla"` |
| `crm_perdof` / `acr_vla` / `crm_scalar` / `crm_obs_only` | `select_action_crm(…, mode)` | `else` 分支 |

### CRM 实例化时的 `uncertainty_dim`

```python
if args.mode == "crm_obs_only":
    unc_dim = 0
elif args.mode == "crm_scalar":
    unc_dim = 3
else:  # crm_perdof or acr_vla
    unc_dim = CORRECTION_DIM * H_EFF + H_EFF + H_EFF  # 6*5+5+5 = 40
```

### `select_action_crm()` 内部 mode 分支

```python
# 全部 mode 共享：CGS 计算 40D uncertainty features
uf, _mean = cgs.compute_features(k_pose)  # uf: 40D

# mode 特化：
if mode == "crm_scalar":
    uf = _to_scalar_uf(uf)   # 40D → 3D (norm/mean 压缩)

uf_input = None if mode == "crm_obs_only" else uf
refined_pose = crm(base_action, uf_input, obs_feat)
```

### 核心对比表

| 维度 | `acr_vla` / `crm_perdof` | `crm_obs_only` | `crm_scalar` | `reconvla` |
|------|--------------------------|----------------|--------------|------------|
| UF 输入 | 40D (per-DOF std 30 + radius 5 + logvol 5) | None | 3D (scalar 压缩) | 无 CRM |
| CRM input_dim | 30+40+960=**1030** | 30+0+960=**990** | 30+3+960=**993** | N/A |
| Base action | argmin to mean | argmin to mean | argmin to mean | Euclidean argmin |
| Correction | CRM residual `base + Δ` | CRM residual (obs-only) | CRM residual | 无 (直接 pass-through) |

---

## 关键结论

### 1. `acr_vla` ≡ `crm_perdof`，完全等价

代码中 `acr_vla` 和 `crm_perdof` 在**所有路径**上走完全相同的逻辑：
- 同一个 `else` 分支 → `unc_dim = 40`
- `select_action_crm()` 中不触发任何特化 (`crm_scalar` / `crm_obs_only` 的 if 都不命中)
- 文档注释也明确写了：`"acr_vla": alias for crm_perdof`

**不存在隐藏差异。** 唯一区别是输出 JSON 里的 `"mode"` 字符串不同。

### 2. 不同 mode 的 checkpoint 不可互换

由于各 mode 的 CRM `input_dim` 不同（1030 / 990 / 993），**每个 mode 必须用对应 mode 训练出的 checkpoint**。用 perdof checkpoint 跑 obs_only mode 会直接报 shape mismatch 错误。

### 3. 跨 benchmark 结果可直接比较

只要 spatial 和 object 上的同一 mode 使用的是**同一类型（同 unc_dim）的 checkpoint**，结果就可以直接比较。代码路径无 benchmark-specific 分支，mode 的行为与 benchmark 无关。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_p3-mode-equivalence_20260515T033506"
}
```

</details>

---
