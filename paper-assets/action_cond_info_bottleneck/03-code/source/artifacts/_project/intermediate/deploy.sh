#!/bin/bash
# ACIB 一键部署脚本 — 环境搭建 + 代码部署 + 模型数据下载 + baseline eval 启动
# 适用于 AutoDL westb-13953 (aml-train 镜像, 2× RTX PRO 6000 96GB)
#
# 用法（在服务器上执行）：
#   bash deploy.sh
#
# 或从本地通过 SSH 执行：
#   ssh -p 13953 root@connect.westb.seetacloud.com 'bash -s' < deploy.sh

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

step() { echo -e "\n${GREEN}[$(date +%H:%M:%S)] ▶ $1${NC}"; }
warn() { echo -e "${YELLOW}[$(date +%H:%M:%S)] ⚠ $1${NC}"; }
fail() { echo -e "${RED}[$(date +%H:%M:%S)] ✗ $1${NC}"; exit 1; }
ok()   { echo -e "${GREEN}[$(date +%H:%M:%S)] ✓ $1${NC}"; }

# ============================================================
# Phase 1: AutoDL 环境初始化
# ============================================================
step "Phase 1/6: AutoDL 环境初始化"

# conda 环境（aml-train 镜像标准）
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
ok "Conda 环境激活"

# AutoDL 网络加速 + SSL 证书
source /etc/network_turbo 2>/dev/null || warn "network_turbo 不可用，继续"
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export MUJOCO_GL=egl
ok "网络加速 + 环境变量设置完成"

# GPU 检查
echo "--- GPU 信息 ---"
nvidia-smi --query-gpu=index,name,memory.total,driver_version --format=csv,noheader
echo "--- Python/CUDA ---"
python --version
nvcc --version 2>/dev/null | grep release || echo "nvcc 不可用（正常，torch 自带 CUDA runtime）"
echo "--- 磁盘空间 ---"
df -h / /root/autodl-tmp/ 2>/dev/null || df -h /
ok "系统信息收集完成"

# ============================================================
# Phase 2: 依赖安装
# ============================================================
step "Phase 2/6: 安装依赖"

# 检查已有包
echo "已安装的 ML 包："
pip list --format=freeze 2>/dev/null | grep -iE "torch|transformers|lerobot|flash|libero|mujoco" || echo "(无)"

# LeRobot + SmolVLA
step "安装 LeRobot[smolvla]..."
pip install "lerobot[smolvla]" 2>&1 | tail -5 || {
    warn "lerobot[smolvla] 安装失败，尝试分步安装"
    pip install lerobot 2>&1 | tail -3
    pip install smolvlm 2>&1 | tail -3
}
ok "LeRobot 安装完成"

# 额外依赖
step "安装额外依赖..."
pip install wandb einops accelerate torchvision 2>&1 | tail -3
ok "额外依赖安装完成"

# LIBERO + MuJoCo
step "安装 LIBERO + MuJoCo..."
pip install mujoco 2>&1 | tail -3
pip install libero 2>&1 | tail -3 || {
    warn "pip install libero 失败，从 GitHub 安装"
    pip install "git+https://github.com/Lifelong-Robot-Learning/LIBERO.git" 2>&1 | tail -3
}
ok "LIBERO 安装完成"

# 验证关键包
step "验证安装..."
python -c "
import torch
print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')
for i in range(torch.cuda.device_count()):
    print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')
import transformers; print(f'transformers={transformers.__version__}')
import lerobot; print(f'lerobot={lerobot.__version__}')
" || fail "关键包验证失败"
ok "所有依赖安装验证通过"

# ============================================================
# Phase 3: ACIB 代码部署
# ============================================================
step "Phase 3/6: 部署 ACIB v2 代码到 /root/acib/"

mkdir -p /root/acib/{acib,scripts,configs,outputs,results,logs}

# --- acib/__init__.py ---
cat << 'PYEOF' > /root/acib/acib/__init__.py
# ACIB: Action-Conditioned Information Bottleneck for VLA robustness.
from acib.config import ACIBConfig
from acib.scorer import ACIBScorer
from acib.losses import ACIBLoss
PYEOF

# --- acib/config.py ---
cat << 'PYEOF' > /root/acib/acib/config.py
from dataclasses import dataclass
from typing import Literal


@dataclass
class ACIBConfig:
    visual_dim: int = 960
    condition_dim: int = 960
    hidden_dim: int = 64
    num_visual_tokens: int = 64
    mode: Literal["soft", "hard"] = "soft"
    top_k_ratio: float = 0.8
    alpha: float = 0.01
    beta: float = 0.1
    freeze_vlm: bool = True
    freeze_action_expert: bool = False
    train_scorer_only: bool = False
    condition_source: Literal["language", "state", "both"] = "language"
PYEOF

# --- acib/scorer.py ---
cat << 'PYEOF' > /root/acib/acib/scorer.py
import torch
import torch.nn as nn
import torch.nn.functional as F
from acib.config import ACIBConfig


class ACIBScorer(nn.Module):
    def __init__(self, config: ACIBConfig):
        super().__init__()
        self.config = config
        self.mode = config.mode
        input_dim = config.visual_dim + config.condition_dim
        self.mlp = nn.Sequential(
            nn.Linear(input_dim, config.hidden_dim),
            nn.GELU(),
            nn.Linear(config.hidden_dim, 1),
        )

    def forward(self, visual_tokens: torch.Tensor, condition: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        B, N, D_v = visual_tokens.shape
        condition_expanded = condition.unsqueeze(1).expand(-1, N, -1)
        combined = torch.cat([visual_tokens, condition_expanded], dim=-1)
        logits = self.mlp(combined).squeeze(-1)
        if self.mode == "soft":
            weights = torch.sigmoid(logits)
        elif self.mode == "hard":
            weights = self._hard_topk(logits)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")
        return weights, logits

    def _hard_topk(self, logits: torch.Tensor) -> torch.Tensor:
        B, N = logits.shape
        k = max(1, int(N * self.config.top_k_ratio))
        _, topk_indices = logits.topk(k, dim=-1)
        mask = torch.zeros_like(logits)
        mask.scatter_(-1, topk_indices, 1.0)
        soft = torch.sigmoid(logits)
        return mask - soft.detach() + soft

    def apply_weights(self, visual_tokens: torch.Tensor, weights: torch.Tensor) -> torch.Tensor:
        return visual_tokens * weights.unsqueeze(-1)
PYEOF

# --- acib/losses.py ---
cat << 'PYEOF' > /root/acib/acib/losses.py
import torch
import torch.nn as nn
import torch.nn.functional as F
from acib.config import ACIBConfig


class ACIBLoss(nn.Module):
    def __init__(self, config: ACIBConfig):
        super().__init__()
        self.alpha = config.alpha
        self.beta = config.beta
        self.target_rate = config.top_k_ratio

    def forward(self, task_loss: torch.Tensor, scores_clean: torch.Tensor, scores_perturbed: torch.Tensor | None = None) -> dict[str, torch.Tensor]:
        ib_loss = self.information_bottleneck_loss(scores_clean, self.target_rate)
        if scores_perturbed is not None:
            consistency_loss = self.consistency_loss(scores_clean, scores_perturbed)
        else:
            consistency_loss = torch.tensor(0.0, device=task_loss.device)
        total = task_loss + self.alpha * consistency_loss + self.beta * ib_loss
        return {"total": total, "task": task_loss.detach(), "consistency": consistency_loss.detach(), "ib": ib_loss.detach()}

    @staticmethod
    def information_bottleneck_loss(logits: torch.Tensor, target_rate: float = 0.8) -> torch.Tensor:
        p = torch.sigmoid(logits)
        q = target_rate
        kl = p * torch.log(p / (q + 1e-8) + 1e-8) + (1 - p) * torch.log((1 - p) / (1 - q + 1e-8) + 1e-8)
        return kl.mean()

    @staticmethod
    def consistency_loss(logits_clean: torch.Tensor, logits_perturbed: torch.Tensor) -> torch.Tensor:
        return F.mse_loss(logits_clean, logits_perturbed)
PYEOF

# --- acib/acib_policy.py (v2 — with torchvision augmentation) ---
cat << 'PYEOF' > /root/acib/acib/acib_policy.py
import torch
import torch.nn as nn
import torchvision.transforms.v2 as T
from acib.config import ACIBConfig
from acib.scorer import ACIBScorer
from acib.losses import ACIBLoss


class ACIBPolicy(nn.Module):
    """SmolVLA + Action-Conditioned Information Bottleneck.

    Module hierarchy (verified from lerobot source):
        base_policy.model                          -> VLAFlowMatching
        base_policy.model.vlm_with_expert          -> SmolVLMWithExpertModel
        base_policy.model.vlm_with_expert.vlm      -> SmolVLMForConditionalGeneration
        base_policy.model.vlm_with_expert.vlm.model.vision_model  -> SigLIP
        base_policy.model.vlm_with_expert.vlm.model.connector     -> PixelShuffle + Linear
        base_policy.model.vlm_with_expert.vlm.model.text_model    -> LM backbone
        base_policy.model.vlm_with_expert.lm_expert               -> Action expert

    Hook target: connector (fires once per camera in embed_prefix loop).
    Conditioning: visual token mean pooling (self-conditioning, MVP).
    """

    def __init__(self, base_policy: nn.Module, acib_config: ACIBConfig):
        super().__init__()
        self.base_policy = base_policy
        self.acib_config = acib_config
        self.scorer = ACIBScorer(acib_config)
        self.acib_loss_fn = ACIBLoss(acib_config)
        self.acib_enabled = True
        self._cached_logits: list[torch.Tensor] = []
        self._hook_handles: list = []
        self._perturb_transform = self._build_perturb_transform()
        self._setup_freeze(acib_config)
        self._install_hooks()

    @property
    def _vlm_with_expert(self):
        return self.base_policy.model.vlm_with_expert

    @property
    def _connector(self) -> nn.Module:
        return self._vlm_with_expert.vlm.model.connector

    @property
    def _vision_encoder(self) -> nn.Module:
        return self._vlm_with_expert.vlm.model.vision_model

    def _install_hooks(self) -> None:
        handle = self._connector.register_forward_hook(self._connector_hook)
        self._hook_handles.append(handle)

    def _connector_hook(self, module, input, output):
        if not self.acib_enabled:
            return output
        condition = output.mean(dim=1)
        weights, logits = self.scorer(output, condition)
        self._cached_logits.append(logits)
        return self.scorer.apply_weights(output, weights)

    def forward(self, batch: dict[str, torch.Tensor]) -> tuple[torch.Tensor, dict]:
        self._cached_logits = []
        task_loss, loss_dict = self.base_policy.forward(batch)
        if not self.acib_enabled or not self._cached_logits:
            return task_loss, loss_dict
        scores_clean = torch.cat(self._cached_logits, dim=1)
        scores_perturbed = None
        if self.training:
            scores_perturbed = self._score_perturbed(batch)
        acib_losses = self.acib_loss_fn(task_loss, scores_clean, scores_perturbed)
        loss_dict["acib_task"] = acib_losses["task"]
        loss_dict["acib_consistency"] = acib_losses["consistency"]
        loss_dict["acib_ib"] = acib_losses["ib"]
        return acib_losses["total"], loss_dict

    @staticmethod
    def _build_perturb_transform() -> T.Transform:
        return T.RandomChoice([
            T.RandomAffine(degrees=15, translate=(0.05, 0.05)),
            T.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3, hue=0.1),
            T.GaussianBlur(kernel_size=7, sigma=(0.5, 2.0)),
        ])

    def _score_perturbed(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        image_keys = sorted(
            k for k in batch
            if k.startswith("observation.images.") and isinstance(batch[k], torch.Tensor)
            and batch[k].dim() == 4
        )
        if not image_keys:
            return None
        prev = self.acib_enabled
        self.acib_enabled = False
        all_logits = []
        try:
            for key in image_keys:
                img = batch[key]
                if torch.rand(1).item() < 0.75:
                    perturbed = self._perturb_transform(img)
                else:
                    perturbed = img + torch.randn_like(img) * 0.1
                with torch.no_grad():
                    tokens = self._vlm_with_expert.embed_image(perturbed)
                condition = tokens.mean(dim=1)
                _, logits = self.scorer(tokens, condition)
                all_logits.append(logits)
        finally:
            self.acib_enabled = prev
        return torch.cat(all_logits, dim=1) if all_logits else None

    def _setup_freeze(self, config: ACIBConfig) -> None:
        if config.freeze_vlm:
            for param in self._vlm_with_expert.vlm.parameters():
                param.requires_grad = False
        if config.freeze_action_expert:
            for param in self._vlm_with_expert.lm_expert.parameters():
                param.requires_grad = False
        if config.train_scorer_only:
            for param in self.base_policy.parameters():
                param.requires_grad = False
        for param in self.scorer.parameters():
            param.requires_grad = True

    def select_action(self, batch: dict[str, torch.Tensor], **kwargs) -> torch.Tensor:
        return self.base_policy.select_action(batch, **kwargs)

    def reset(self):
        self.base_policy.reset()

    def get_optim_params(self) -> dict:
        base_params = self.base_policy.get_optim_params()
        scorer_params = {"params": list(self.scorer.parameters()), "lr": base_params.get("lr", 1e-4)}
        if isinstance(base_params, dict):
            return [base_params, scorer_params]
        elif isinstance(base_params, list):
            return base_params + [scorer_params]
        return [scorer_params]

    def get_scorer_stats(self) -> dict[str, float]:
        if not self._cached_logits:
            return {}
        logits = torch.cat(self._cached_logits, dim=1)
        w = torch.sigmoid(logits)
        return {
            "scorer/mean": w.mean().item(),
            "scorer/std": w.std().item(),
            "scorer/min": w.min().item(),
            "scorer/max": w.max().item(),
            "scorer/sparsity": (w < 0.5).float().mean().item(),
        }

    def toggle_acib(self, enabled: bool) -> None:
        self.acib_enabled = enabled

    def remove_hooks(self):
        for h in self._hook_handles:
            h.remove()
        self._hook_handles.clear()

    @classmethod
    def from_pretrained(cls, model_id: str, acib_config: ACIBConfig | None = None):
        from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
        base_policy = SmolVLAPolicy.from_pretrained(model_id)
        if acib_config is None:
            vlm_hidden = base_policy.model.vlm_with_expert.config.text_config.hidden_size
            acib_config = ACIBConfig(visual_dim=vlm_hidden, condition_dim=vlm_hidden)
        return cls(base_policy, acib_config)
PYEOF

# --- scripts/train_acib.py ---
cat << 'PYEOF' > /root/acib/scripts/train_acib.py
#!/usr/bin/env python3
"""ACIB-S training: fine-tune SmolVLA with action-conditioned information bottleneck."""
import argparse, json, os, sys, time
from pathlib import Path
import torch, torch.nn as nn
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from acib.config import ACIBConfig
from acib.acib_policy import ACIBPolicy

def parse_args():
    parser = argparse.ArgumentParser(description="ACIB-S training")
    parser.add_argument("--model_id", type=str, default="lerobot/smolvla_base")
    parser.add_argument("--dataset_id", type=str, default="lerobot/libero")
    parser.add_argument("--hidden_dim", type=int, default=64, choices=[64, 128])
    parser.add_argument("--alpha", type=float, default=0.01)
    parser.add_argument("--beta", type=float, default=0.1)
    parser.add_argument("--mode", type=str, default="soft", choices=["soft", "hard"])
    parser.add_argument("--top_k_ratio", type=float, default=0.8)
    parser.add_argument("--condition_source", type=str, default="language", choices=["language", "state", "both"])
    parser.add_argument("--steps", type=int, default=20000)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--warmup_steps", type=int, default=1000)
    parser.add_argument("--grad_clip", type=float, default=1.0)
    parser.add_argument("--eval_freq", type=int, default=2000)
    parser.add_argument("--save_freq", type=int, default=5000)
    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float32", "bfloat16", "float16"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="outputs/acib_s")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb_project", type=str, default="")
    parser.add_argument("--wandb_run_name", type=str, default="")
    return parser.parse_args()

def setup_wandb(args):
    if not args.wandb_project: return None
    try:
        import wandb
        run_name = args.wandb_run_name or f"acib-{args.mode}-h{args.hidden_dim}-a{args.alpha}-b{args.beta}-s{args.seed}"
        return wandb.init(project=args.wandb_project, name=run_name, config=vars(args))
    except ImportError:
        print("wandb not installed, skipping logging"); return None

def build_acib_policy(args):
    acib_config = ACIBConfig(hidden_dim=args.hidden_dim, alpha=args.alpha, beta=args.beta, mode=args.mode, top_k_ratio=args.top_k_ratio, condition_source=args.condition_source, freeze_vlm=True)
    print(f"Loading base model: {args.model_id}")
    policy = ACIBPolicy.from_pretrained(args.model_id, acib_config)
    trainable = sum(p.numel() for p in policy.parameters() if p.requires_grad)
    total = sum(p.numel() for p in policy.parameters())
    print(f"Parameters: {total:,} total, {trainable:,} trainable ({trainable/total:.1%})")
    return policy

def build_dataloader(args):
    from lerobot.datasets.lerobot_dataset import LeRobotDataset
    print(f"Loading dataset: {args.dataset_id}")
    dataset = LeRobotDataset(args.dataset_id)
    print(f"Dataset: {len(dataset)} frames")
    return torch.utils.data.DataLoader(dataset, batch_size=args.batch_size, shuffle=True, num_workers=4, pin_memory=True, drop_last=True)

def train(args):
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    torch.manual_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype = {"float32": torch.float32, "bfloat16": torch.bfloat16, "float16": torch.float16}[args.dtype]
    output_dir = Path(args.output_dir); output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_dir / "config.json", "w") as f: json.dump(vars(args), f, indent=2)
    wandb_run = setup_wandb(args)
    policy = build_acib_policy(args).to(device)
    dataloader = build_dataloader(args)
    trainable_params = [p for p in policy.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(trainable_params, lr=args.lr, betas=(0.9, 0.95))
    def lr_lambda(step):
        if step < args.warmup_steps: return step / max(1, args.warmup_steps)
        progress = (step - args.warmup_steps) / max(1, args.steps - args.warmup_steps)
        return 0.5 * (1.0 + torch.cos(torch.tensor(progress * 3.14159)).item())
    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
    print(f"\nStarting ACIB-{args.mode.upper()} training")
    print(f"  Hidden dim: {args.hidden_dim}, Alpha: {args.alpha}, Beta: {args.beta}")
    print(f"  Steps: {args.steps}, Batch: {args.batch_size}, Device: {device}, dtype: {args.dtype}")
    global_step = 0; data_iter = iter(dataloader); t0 = time.time()
    while global_step < args.steps:
        try: batch = next(data_iter)
        except StopIteration: data_iter = iter(dataloader); batch = next(data_iter)
        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
        with torch.autocast(device_type="cuda", dtype=dtype): total_loss, loss_dict = policy(batch)
        optimizer.zero_grad(); total_loss.backward()
        if args.grad_clip > 0: nn.utils.clip_grad_norm_(trainable_params, args.grad_clip)
        optimizer.step(); scheduler.step(); global_step += 1
        if global_step % 100 == 0:
            elapsed = time.time() - t0; sps = global_step / elapsed
            scorer_stats = policy.get_scorer_stats()
            log_dict = {"train/total_loss": loss_dict["total"].item(), "train/task_loss": loss_dict["task"].item(), "train/consistency_loss": loss_dict.get("consistency", torch.tensor(0)).item(), "train/ib_loss": loss_dict.get("ib", torch.tensor(0)).item(), "train/lr": scheduler.get_last_lr()[0], "train/steps_per_sec": sps, **{f"train/{k}": v for k, v in scorer_stats.items()}}
            print(f"Step {global_step}/{args.steps} | loss={loss_dict['total'].item():.4f} task={loss_dict['task'].item():.4f} ib={loss_dict.get('ib', torch.tensor(0)).item():.4f} | {sps:.1f} steps/s")
            if wandb_run: import wandb; wandb.log(log_dict, step=global_step)
        if global_step % args.save_freq == 0 or global_step == args.steps:
            ckpt_dir = output_dir / f"checkpoint-{global_step}"; ckpt_dir.mkdir(exist_ok=True)
            torch.save({"step": global_step, "policy_state_dict": policy.state_dict(), "optimizer_state_dict": optimizer.state_dict(), "config": vars(args)}, ckpt_dir / "checkpoint.pt")
            print(f"  Saved checkpoint to {ckpt_dir}")
    print(f"\nTraining complete: {args.steps} steps in {(time.time()-t0)/3600:.1f}h")
    if wandb_run: wandb_run.finish()

if __name__ == "__main__": train(parse_args())
PYEOF

# --- scripts/eval_baseline.py ---
cat << 'PYEOF' > /root/acib/scripts/eval_baseline.py
#!/usr/bin/env python3
"""SmolVLA baseline evaluation on LIBERO and LIBERO-Plus."""
import argparse, json, os, sys, time
from pathlib import Path
import torch

def parse_args():
    parser = argparse.ArgumentParser(description="SmolVLA baseline evaluation")
    parser.add_argument("--model_id", type=str, default="lerobot/smolvla_base")
    parser.add_argument("--env_type", type=str, default="libero", choices=["libero", "libero_plus"])
    parser.add_argument("--suites", nargs="+", default=["libero_spatial", "libero_object", "libero_goal", "libero_10"])
    parser.add_argument("--n_episodes", type=int, default=50)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="results/baseline")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max_steps", type=int, default=600)
    return parser.parse_args()

def run_lerobot_eval(args):
    import subprocess
    suites_str = ",".join(args.suites)
    cmd = ["lerobot-eval", f"--policy.path={args.model_id}", f"--env.type={args.env_type}", f"--env.task={suites_str}", "--eval.batch_size=1", f"--eval.n_episodes={args.n_episodes}", "--env.max_parallel_tasks=1", f"--output_dir={args.output_dir}"]
    env = os.environ.copy(); env["CUDA_VISIBLE_DEVICES"] = str(args.gpu); env["MUJOCO_GL"] = env.get("MUJOCO_GL", "egl")
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env, capture_output=False)
    return result.returncode

def run_manual_eval(args):
    from lerobot.policies.smolvla import SmolVLAPolicy
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Loading model: {args.model_id}")
    policy = SmolVLAPolicy.from_pretrained(args.model_id).to(device).eval()
    results = {}
    for suite in args.suites:
        print(f"\nEvaluating suite: {suite}")
        results[suite] = {"avg_success_rate": 0.0, "n_episodes": args.n_episodes, "note": "Placeholder — verify lerobot eval API"}
    output_path = Path(args.output_dir); output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / "results.json", "w") as f: json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path / 'results.json'}")

if __name__ == "__main__":
    args = parse_args()
    print(f"SmolVLA Baseline Eval — {args.env_type}")
    ret = run_lerobot_eval(args)
    if ret != 0:
        print(f"\nlerobot-eval exited with code {ret}, trying manual eval...")
        run_manual_eval(args)
PYEOF

# --- requirements.txt ---
cat << 'PYEOF' > /root/acib/requirements.txt
torch>=2.7
transformers>=5.4.0
accelerate>=1.10.0
einops>=0.8.0
wandb>=0.24.0
PYEOF

ok "ACIB v2 代码部署完成 ($(find /root/acib -name '*.py' | wc -l) Python 文件)"

# 验证 ACIB import
cd /root/acib && python -c "
import sys; sys.path.insert(0, '.')
from acib import ACIBConfig, ACIBScorer, ACIBLoss
import torch
scorer = ACIBScorer(ACIBConfig())
x = torch.randn(2, 64, 960)
c = torch.randn(2, 960)
w, l = scorer(x, c)
print(f'Scorer test: weights={w.shape}, logits={l.shape}')
assert w.shape == (2, 64) and l.shape == (2, 64)
print('ACIB import + smoke test PASSED')
" || fail "ACIB 代码验证失败"
ok "ACIB 代码验证通过"

# ============================================================
# Phase 4: 模型 + 数据下载
# ============================================================
step "Phase 4/6: 下载 SmolVLA 模型 + LIBERO 数据集"

mkdir -p /root/autodl-tmp/.hf_cache

# SmolVLA 模型下载（后台）
nohup python -c "
import os; os.environ['HF_HOME'] = '/root/autodl-tmp/.hf_cache'; os.environ['HF_HUB_DISABLE_XET'] = '1'
from huggingface_hub import snapshot_download
print('Downloading SmolVLA model...')
path = snapshot_download('lerobot/smolvla_base', cache_dir='/root/autodl-tmp/.hf_cache')
print(f'MODEL_DOWNLOAD_DONE: {path}')
" > /tmp/download_model.log 2>&1 &
MODEL_PID=$!
echo "SmolVLA 模型下载 PID: $MODEL_PID"

# LIBERO 数据下载（后台）
nohup python -c "
import os; os.environ['HF_HOME'] = '/root/autodl-tmp/.hf_cache'; os.environ['HF_HUB_DISABLE_XET'] = '1'
from huggingface_hub import snapshot_download
print('Downloading LIBERO dataset...')
path = snapshot_download('lerobot/libero', cache_dir='/root/autodl-tmp/.hf_cache', repo_type='dataset')
print(f'DATA_DOWNLOAD_DONE: {path}')
" > /tmp/download_data.log 2>&1 &
DATA_PID=$!
echo "LIBERO 数据下载 PID: $DATA_PID"

# 等待下载完成（最长 60 分钟）
step "等待下载完成（每 30 秒检查一次）..."
MAX_WAIT=3600
ELAPSED=0
while [ $ELAPSED -lt $MAX_WAIT ]; do
    MODEL_ALIVE=$(ps -p $MODEL_PID -o pid= 2>/dev/null | wc -l)
    DATA_ALIVE=$(ps -p $DATA_PID -o pid= 2>/dev/null | wc -l)

    if [ "$MODEL_ALIVE" -eq 0 ] && [ "$DATA_ALIVE" -eq 0 ]; then
        break
    fi

    echo "[$(date +%H:%M:%S)] 下载中... model=$([ $MODEL_ALIVE -gt 0 ] && echo 'running' || echo 'done') data=$([ $DATA_ALIVE -gt 0 ] && echo 'running' || echo 'done') (${ELAPSED}s elapsed)"
    sleep 30
    ELAPSED=$((ELAPSED + 30))
done

# 检查下载结果
echo "--- Model download log (last 5 lines) ---"
tail -5 /tmp/download_model.log 2>/dev/null || echo "No log"
echo "--- Data download log (last 5 lines) ---"
tail -5 /tmp/download_data.log 2>/dev/null || echo "No log"

grep -q "MODEL_DOWNLOAD_DONE" /tmp/download_model.log 2>/dev/null && ok "SmolVLA 模型下载完成" || warn "SmolVLA 模型下载可能未完成，检查 /tmp/download_model.log"
grep -q "DATA_DOWNLOAD_DONE" /tmp/download_data.log 2>/dev/null && ok "LIBERO 数据下载完成" || warn "LIBERO 数据下载可能未完成，检查 /tmp/download_data.log"

# ============================================================
# Phase 5: 完整验证
# ============================================================
step "Phase 5/6: 完整环境验证"

cd /root/acib && python -c "
import os; os.environ['HF_HOME'] = '/root/autodl-tmp/.hf_cache'
import torch
print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')
for i in range(torch.cuda.device_count()):
    print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')
import transformers; print(f'transformers={transformers.__version__}')
import lerobot; print(f'lerobot={lerobot.__version__}')

# Test SmolVLA load
print('Loading SmolVLA (this may take a minute)...')
from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
policy = SmolVLAPolicy.from_pretrained('lerobot/smolvla_base')
print(f'SmolVLA loaded: {sum(p.numel() for p in policy.parameters()):,} params')

# Test ACIB wrapper
import sys; sys.path.insert(0, '/root/acib')
from acib.acib_policy import ACIBPolicy
from acib.config import ACIBConfig
acib = ACIBPolicy(policy, ACIBConfig())
print(f'ACIB wrapper: scorer params = {sum(p.numel() for p in acib.scorer.parameters()):,}')
print('FULL_VERIFICATION_PASSED')
" || warn "完整验证部分失败，检查上方输出"
ok "环境验证完成"

# ============================================================
# Phase 6: 启动 MVP-1 Baseline Eval
# ============================================================
step "Phase 6/6: 启动 MVP-1 Baseline Eval（两张卡并行）"

mkdir -p /root/acib/logs

# GPU 0: spatial + object suites
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache \
nohup python /root/acib/scripts/eval_baseline.py \
    --model_id lerobot/smolvla_base \
    --env_type libero \
    --suites libero_spatial libero_object \
    --n_episodes 50 \
    --gpu 0 \
    --output_dir /root/acib/results/baseline_spatial_object \
    --seed 42 \
    > /root/acib/logs/baseline_gpu0.log 2>&1 &
GPU0_PID=$!
echo "GPU 0 (spatial+object) PID: $GPU0_PID"

# GPU 1: goal + long suites
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache \
nohup python /root/acib/scripts/eval_baseline.py \
    --model_id lerobot/smolvla_base \
    --env_type libero \
    --suites libero_goal libero_10 \
    --n_episodes 50 \
    --gpu 0 \
    --output_dir /root/acib/results/baseline_goal_long \
    --seed 42 \
    > /root/acib/logs/baseline_gpu1.log 2>&1 &
GPU1_PID=$!
echo "GPU 1 (goal+long) PID: $GPU1_PID"

# 检查进程启动
sleep 2
ps -p $GPU0_PID -o pid= >/dev/null 2>&1 && ok "GPU 0 eval 已启动 (PID $GPU0_PID)" || warn "GPU 0 eval 启动失败"
ps -p $GPU1_PID -o pid= >/dev/null 2>&1 && ok "GPU 1 eval 已启动 (PID $GPU1_PID)" || warn "GPU 1 eval 启动失败"

# ============================================================
# 完成
# ============================================================
echo ""
echo "============================================================"
echo -e "${GREEN}部署完成！${NC}"
echo "============================================================"
echo ""
echo "查看 baseline eval 进度："
echo "  GPU 0: tail -f /root/acib/logs/baseline_gpu0.log"
echo "  GPU 1: tail -f /root/acib/logs/baseline_gpu1.log"
echo ""
echo "查看 GPU 使用："
echo "  watch -n 5 nvidia-smi"
echo ""
echo "查看结果："
echo "  cat /root/acib/results/baseline_spatial_object/results.json"
echo "  cat /root/acib/results/baseline_goal_long/results.json"
echo ""
echo "下载日志："
echo "  cat /tmp/download_model.log"
echo "  cat /tmp/download_data.log"
echo ""
echo "ACIB 代码目录: /root/acib/"
echo "HF 缓存: /root/autodl-tmp/.hf_cache/"
echo "============================================================"
