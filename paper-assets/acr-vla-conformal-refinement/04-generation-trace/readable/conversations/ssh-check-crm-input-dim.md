# ssh check crm input dim

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_ssh_check-crm-input-dim_20260516T234450.jsonl`
- **Structured JSON:** [`818972c7217272fa1e50.json`](../../sessions/81/818972c7217272fa1e50.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-16T23:45:55.269439+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T23:45:55.269758+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T23:45:55.269925+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/src/ -type f -name \"*.py\" | head -50",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/src/ -type f -name \"*.py\" | head -50",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T23:45:55.270075+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/src/__init__.py\\n/root/acr-vla-conformal-refinement/src/aci.py\\n/root/acr-vla-conformal-refinement/src/cgs.py\\n/root/acr-vla-conformal-refinement/src/compute_norm_stats.py\\n/root/acr-vla-conformal-refinement/src/crm.py\\n/root/acr-vla-conformal-refinement/src/evaluate.py\\n/root/acr-vla-conformal-refinement/src/gated_crm.py\\n/root/acr-vla-conformal-refinement/src/reconvla_baseline.py\\n/root/acr-vla-conformal-refinement/src/smolvla_wrapper.py\\n/root/acr-vla-conformal-refinement/src/train_crm.py\\n/root/acr-vla-conformal-refinement/src/utils.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T23:45:55.270228+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/src/crm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/src/crm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T23:45:55.270431+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nConformal Refinement Module (CRM).\\n\\nInput: base_action (30D, argmin-selected) + uncertainty_features (40D) + obs_features (960D from VLM)\\nOutput: refined_action (30D) = base_action + clipped_delta\\n\\nArchitecture: 2 hidden layers, dim 256, ReLU, residual connection.\\n\\\"\\\"\\\"\\nimport torch\\nimport torch.nn as nn\\n\\n\\nclass ConformalRefinementModule(nn.Module):\\n    \\\"\\\"\\\"Learn to refine VLA action predictions using structured uncertainty.\\\"\\\"\\\"\\n\\n    def __init__(self, action_dim: int = 30, uncertainty_dim: int = 40,\\n                 obs_dim: int = 960, hidden_dim: int = 256,\\n                 max_correction_norm: float = 1.42):\\n        \\\"\\\"\\\"\\n        Args:\\n            action_dim: flattened action dim (H_eff * D = 5 * 6 = 30)\\n            uncertainty_dim: CGS output dim (30 + 5 + 5 = 40), 0 for obs_only\\n            obs_dim: VLM encoder frozen output dim (960)\\n            hidden_dim: hidden layer dim\\n        \\\"\\\"\\\"\\n        super().__init__()\\n\\n        self.max_correction_norm = max_correction_norm\\n        self.uncertainty_dim = uncertainty_dim\\n        input_dim = action_dim + uncertainty_dim + obs_dim\\n\\n        self.register_buffer('input_mean', torch.zeros(input_dim))\\n        self.register_buffer('input_std', torch.ones(input_dim))\\n\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, hidden_dim),\\n            nn.ReLU(),\\n            nn.Linear(hidden_dim, hidden_dim),\\n            nn.ReLU(),\\n            nn.Linear(hidden_dim, action_dim),\\n        )\\n\\n        # Residual: output = base_action + delta. Init last layer near zero.\\n        nn.init.zeros_(self.net[-1].weight)\\n        nn.init.zeros_(self.net[-1].bias)\\n\\n    def forward(self, base_action: torch.Tensor, uncertainty_features: torch.Tensor,\\n                obs_features: torch.Tensor) -> torch.Tensor:\\n        \\\"\\\"\\\"\\n    
…[truncated 1279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T23:45:55.270594+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/src/cgs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/src/cgs.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T23:45:55.270788+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nConformalized Gaussian Scoring (CGS) module.\\n\\nInput: K flow-matching samples, shape (K, H_eff, D) where D=CORRECTION_DIM=6, H_eff=5.\\n       Accepts (K, chunk_size, D') and auto-truncates to (K, H_eff, action_dim).\\n\\nOutput:\\n  - uncertainty_features: (action_dim*H_eff + H_eff + H_eff) tensor\\n    [per_dof_std(30), conformal_radius(5), log_volume(5)]\\n  - mean_action: (H_eff*action_dim) tensor (K samples mean, flattened)\\n\\\"\\\"\\\"\\nimport torch\\nimport numpy as np\\nfrom sklearn.covariance import LedoitWolf\\n\\ntry:\\n    from utils import CORRECTION_DIM\\nexcept ImportError:\\n    from .utils import CORRECTION_DIM\\n\\n\\nclass ConformilizedGaussianScoring:\\n    \\\"\\\"\\\"Compute structured uncertainty features from K flow-matching samples (pose only).\\\"\\\"\\\"\\n\\n    def __init__(self, K: int = 10, horizon: int = 5, action_dim: int = CORRECTION_DIM,\\n                 alpha: float = 0.5, chunk_size: int = 50):  # BugFix W3: 0.1→0.5, K=10时0.1导致quantile=max\\n        self.K = K\\n        self.horizon = horizon       # H_eff = 5\\n        self.action_dim = action_dim  # 6D pose (no gripper)\\n        self.alpha = alpha\\n        self.chunk_size = chunk_size\\n\\n    def compute_features(self, samples: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:\\n        \\\"\\\"\\\"\\n        Args:\\n            samples: (K, T, D') where T >= H_eff and D' >= action_dim.\\n                     Auto-truncates to (K, H_eff, action_dim).\\n        Returns:\\n            uncertainty_features: (action_dim*H_eff + H_eff + H_eff,)\\n            mean_action: (H_eff * action_dim,) — flattened mean over K samples\\n        \\\"\\\"\\\"\\n        if samples.shape[1] > self.horizon:\\n            samples = samples[:, :self.horizon, :]\\n        if samples.shape[2] > self.action_dim:\\n            samples = samples[:, :, :self.action_dim]\\n\\n        assert samples.shape == (self.K, self.hor
…[truncated 2531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T23:45:55.270949+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/src/train_crm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/src/train_crm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T23:45:55.271219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nCRM training script.\\n\\nTwo-phase approach:\\n  Phase 1 (--precompute): Run frozen SmolVLA on LIBERO demos, cache\\n      (obs_features, K_samples, expert_action) to disk.\\n  Phase 2 (default): Load cached features, train CRM with MSE loss +\\n      synthetic augmentation.\\n\\nUsage:\\n  # Phase 1: precompute features (slow, GPU-heavy)\\n  python train_crm.py --precompute --benchmark object\\n\\n  # Phase 2: train CRM (fast)\\n  python train_crm.py --benchmark object --epochs 50\\n\\n  # End-to-end (precompute if cache missing, then train)\\n  python train_crm.py --benchmark object --epochs 50 --auto\\n\\\"\\\"\\\"\\nimport argparse\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\nfrom pathlib import Path\\n\\nimport torch\\nimport torch.nn as nn\\nfrom torch.utils.data import Dataset, DataLoader\\nimport numpy as np\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom cgs import ConformilizedGaussianScoring\\nfrom crm import ConformalRefinementModule\\nfrom utils import (\\n    set_seed, load_libero_demos, build_training_samples,\\n    synthetic_augmentation, CheckpointManager,\\n    CORRECTION_DIM, H_EFF, OBS_DIM, CHUNK_SIZE,\\n)\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Train CRM on LIBERO demos\\\")\\n    p.add_argument(\\\"--benchmark\\\", type=str, nargs='+', default=[\\\"spatial\\\"],\\n                   choices=[\\\"object\\\", \\\"spatial\\\", \\\"goal\\\", \\\"long\\\", \\\"90\\\"])\\n    p.add_argument(\\\"--epochs\\\", type=int, default=50)\\n    p.add_argument(\\\"--batch_size\\\", type=int, default=32)\\n    p.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--output_dir\\\"
…[truncated 7102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T23:45:55.271410+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -n \"CORRECTION_DIM\\|H_EFF\\|OBS_DIM\\|CHUNK_SIZE\\|input_mode\\|obs_only\\|scalar_unc\\|perdof\\|_to_scalar\" /root/acr-vla-conformal-refinement/src/utils.py | head -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -n \"CORRECTION_DIM\\|H_EFF\\|OBS_DIM\\|CHUNK_SIZE\\|input_mode\\|obs_only\\|scalar_unc\\|perdof\\|_to_scalar\" /root/acr-vla-conformal-refinement/src/utils.py | head -30",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T23:45:55.271568+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"16:CORRECTION_DIM = 6   # 6D pose — CRM corrects only pose, not gripper\\n18:H_EFF = 5            # effective horizon (truncated from chunk_size=50)\\n19:CHUNK_SIZE = 50      # SmolVLA native chunk_size\\n20:OBS_DIM = 960        # VLM hidden_size\\n93:def build_training_samples(trajectories: list, h_eff: int = H_EFF,\\n94:                           action_dim: int = CORRECTION_DIM):\\n98:    expert_action is sliced to action_dim (default CORRECTION_DIM=6, pose only).\\n127:        noise = torch.randn_like(expert_action) * noise_scale.repeat(H_EFF).unsqueeze(0)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T23:45:55.271706+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -n \"_to_scalar_uf\\|scalar_unc\\|obs_only\\|input_mode\\|uncertainty_dim\" /root/acr-vla-conformal-refinement/src/train_crm.py | head -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "grep -n \"_to_scalar_uf\\|scalar_unc\\|obs_only\\|input_mode\\|uncertainty_dim\" /root/acr-vla-conformal-refinement/src/train_crm.py | head -30",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T23:45:55.271850+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"81:    p.add_argument(\\\"--input_mode\\\", type=str, default=\\\"full\\\",\\n82:                   choices=[\\\"full\\\", \\\"obs_only\\\", \\\"scalar_unc\\\"],\\n83:                   help=\\\"full=all features, obs_only=no conformal, scalar_unc=scalar uncertainty\\\")\\n346:    # uncertainty_dim depends on input_mode\\n348:                   \\\"obs_only\\\": 0,\\n349:                   \\\"scalar_unc\\\": 3}\\n350:    unc_dim = unc_dim_map[args.input_mode]\\n351:    obs_only = (args.input_mode == \\\"obs_only\\\")\\n352:    scalar_unc = (args.input_mode == \\\"scalar_unc\\\")\\n356:        uncertainty_dim=unc_dim,\\n374:    def _to_scalar_uf(uf):\\n394:            if scalar_unc:\\n395:                _uf = _to_scalar_uf(_uf)\\n397:            if obs_only:\\n427:            if scalar_unc:\\n428:                uf = _to_scalar_uf(uf)\\n433:            refined = crm(ba, None if obs_only else uf, obs_feat)\\n442:                aug_refined = crm(aug_ba, None if obs_only else aug_uf, obs_feat[:n_aug])\\n473:                if scalar_unc:\\n474:                    uf = _to_scalar_uf(uf)\\n478:                refined = crm(ba, None if obs_only else uf, obs_feat)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T23:45:55.271989+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "sed -n '340,380p' /root/acr-vla-conformal-refinement/src/train_crm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "sed -n '340,380p' /root/acr-vla-conformal-refinement/src/train_crm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T23:45:55.272187+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                            shuffle=False, num_workers=2, pin_memory=True)\\n\\n    # CGS + CRM — operate on 6D pose only (CORRECTION_DIM)\\n    cgs = ConformilizedGaussianScoring(\\n        K=manifest[\\\"K\\\"], horizon=H_EFF, action_dim=CORRECTION_DIM\\n    )\\n    # uncertainty_dim depends on input_mode\\n    unc_dim_map = {\\\"full\\\": CORRECTION_DIM * H_EFF + H_EFF + H_EFF,  # 40\\n                   \\\"obs_only\\\": 0,\\n                   \\\"scalar_unc\\\": 3}\\n    unc_dim = unc_dim_map[args.input_mode]\\n    obs_only = (args.input_mode == \\\"obs_only\\\")\\n    scalar_unc = (args.input_mode == \\\"scalar_unc\\\")\\n\\n    crm = ConformalRefinementModule(\\n        action_dim=H_EFF * CORRECTION_DIM,  # 30\\n        uncertainty_dim=unc_dim,\\n        obs_dim=manifest[\\\"obs_dim\\\"],\\n        hidden_dim=args.hidden_dim,\\n    ).to(device)\\n\\n    print(f\\\"[train] CRM parameters: {crm.count_parameters():,}\\\")\\n\\n    optimizer = torch.optim.Adam(crm.parameters(), lr=args.lr)\\n    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(\\n        optimizer, T_max=args.epochs\\n    )\\n    loss_fn = nn.MSELoss()\\n    ckpt_mgr = CheckpointManager(args.output_dir, max_keep=5)\\n\\n    noise_scale = torch.linspace(\\n        args.aug_noise_min, args.aug_noise_max, CORRECTION_DIM\\n    ).to(device)\\n\\n    def _to_scalar_uf(uf):\\n        \\\"\\\"\\\"Compress 40D CGS features to 3D: (norm_std, mean_radius, mean_logvol).\\\"\\\"\\\"\\n        return torch.stack([\\n            uf[:, :30].norm(dim=1),\\n            uf[:, 30:35].mean(dim=1),\\n            uf[:, 35:40].mean(dim=1),\\n        ], dim=1)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T23:45:55.272443+00:00_

结果汇总：

## 维度确认

**文件**: `/root/acr-vla-conformal-refinement/src/crm.py`

| 组件 | 维度 | 来源 |
|------|------|------|
| obs_dim | **960** | VLM hidden_size (`utils.py:20`) |
| action_dim | **30** | 5 steps × 6 DOF (`H_EFF=5, CORRECTION_DIM=6`) |

## 各 variant 的 input_dim

定义于 `train_crm.py:347-349`：

| input_mode | uncertainty_dim | **总 input_dim** | 计算 |
|---|---|---|---|
| `full` | 40 (30 per_dof_std + 5 conformal_radius + 5 log_volume) | **1030** | 30 + 40 + 960 |
| `obs_only` | 0 (uncertainty_features=None) | **990** | 30 + 0 + 960 |
| `scalar_unc` | 3 (norm_std, mean_radius, mean_logvol) | **993** | 30 + 3 + 960 |

注意：代码中没有名为 `perdof` 的 variant。现有的 `full` mode 已包含 per-DOF std（30维），这可能就是你指的 "perdof"。

## 协方差计算方式

**文件**: `/root/acr-vla-conformal-refinement/src/cgs.py`

协方差是 **per-step (6×6)** 计算的，不是 full 30×30：

```python
for h in range(self.horizon):          # 逐 step 循环
    step_samples = samples[:, h, :]    # (K, 6) — 单步的 K 个样本
    cov_matrix = self._ledoit_wolf_cov(step_samples)  # (6, 6)
```

每个 step 独立用 Ledoit-Wolf 估计一个 6×6 协方差矩阵，产出该 step 的 per_dof_std(6)、conformal_radius(1)、log_volume(1)。5 个 step 拼接得到 40D uncertainty features。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_check-crm-input-dim_20260516T234450"
}
```

</details>

---
