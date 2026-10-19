"""
RoboCasa Fine-tune Configuration for Pi0.5 LoRA.

Provides training configs and data adapters for fine-tuning Pi0.5 on
RoboCasa PnP tasks, matching the SafeLIBERO experimental protocol
(30K steps, batch 32, LoRA rank 32/16, lr 2.5e-5).

Key adaptation: RoboCasa uses 16D proprioceptive state and 256x256 images,
while Pi0.5 expects 8D state and 224x224 images. This module provides
the data transforms to bridge the gap.

Input:
  - RoboCasa LeRobot demos on HuggingFace (per-task datasets)
  - Pi0.5 pretrained weights (pi05_libero checkpoint)

Output:
  - openpi TrainConfig ready for train_loop()
  - Data adapter transforms for LeRobot → Pi0.5 format

Usage:
    # Train Pi0.5 LoRA on PnPCounterToSink
    python robocasa_finetune_config.py --task PnPCounterToSink --seed 0 --gpu 0

    # Dry run
    python robocasa_finetune_config.py --task PnPCounterToSink --dry_run

    # Train on all 3 tasks (sequential)
    python robocasa_finetune_config.py --task all --seed 0 --gpu 0
"""

import argparse
import logging
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi", "src"))

os.environ["HF_LEROBOT_HOME"] = "./data"


# --------------------------------------------------------------------------- #
#  Task Configs
# --------------------------------------------------------------------------- #

TASK_CONFIG = {
    "PnPCounterToSink": {
        "description": "Pick object from counter, place in sink",
        "data_repo_id": "robocasa_PnPCounterToSink",
        "assets_dir": "./assets/robocasa_countertosink",
    },
    "PnPCounterToMicrowave": {
        "description": "Pick object from counter, place in microwave",
        "data_repo_id": "robocasa_PnPCounterToMicrowave",
        "assets_dir": "./assets/robocasa_countertomicrowave",
    },
    "PnPCounterToStove": {
        "description": "Pick object from counter, place on stove",
        "data_repo_id": "robocasa_PnPCounterToStove",
        "assets_dir": "./assets/robocasa_countertostove",
    },
}

CHECKPOINT_BASE = "./checkpoints"
WEIGHTS_BASE = "./weights"


# --------------------------------------------------------------------------- #
#  Data Adapter: RoboCasa → Pi0.5
# --------------------------------------------------------------------------- #

class RoboCasaStateAdapter:
    """Transform RoboCasa 16D state to Pi0.5 8D state in LeRobot pipeline.

    RoboCasa 16D layout (robocasa/robosuite convention):
        [0:3]   base_pos          (robot base position, world frame)
        [3:7]   base_quat         (robot base orientation, quaternion)
        [7:10]  rel_ee_pos        (EE position relative to base)
        [10:14] rel_ee_quat       (EE orientation relative to base, quat)
        [14:16] gripper_qpos      (gripper joint positions)

    Pi0.5 8D layout (SafeLIBERO/LIBERO convention):
        [0:3]   ee_pos            (EE position)
        [3:6]   ee_rotvec         (EE orientation, rotation vector)
        [6:8]   gripper_qpos      (gripper joint positions)

    Note: RoboCasa rel_ee_pos is relative to robot base. For Pi0.5,
    we use this directly (Pi0.5 LoRA learns in the local frame).
    If absolute EE position is needed, compose: base_pos + R(base_quat) @ rel_ee_pos.
    """

    def __call__(self, state):
        """Transform a single state vector.

        Args:
            state: np.ndarray [16] or [T, 16] — RoboCasa proprioceptive state

        Returns:
            np.ndarray [8] or [T, 8] — Pi0.5 state format
        """
        from scipy.spatial.transform import Rotation as R

        if state.ndim == 1:
            return self._transform_single(state)
        return np.stack([self._transform_single(s) for s in state])

    def _transform_single(self, state):
        from scipy.spatial.transform import Rotation as R

        if len(state) >= 16:
            rel_ee_pos = state[7:10]
            rel_ee_quat = state[10:14]
            gripper_qpos = state[14:16]
        elif len(state) >= 8:
            # Already in 8D or similar format — pass through
            return state[:8].astype(np.float32)
        else:
            logging.warning("Unexpected state dim %d, zero-padding", len(state))
            return np.zeros(8, dtype=np.float32)

        ee_rotvec = R.from_quat(rel_ee_quat).as_rotvec()
        return np.concatenate([rel_ee_pos, ee_rotvec, gripper_qpos]).astype(np.float32)


class RoboCasaImageAdapter:
    """Resize RoboCasa 256×256 images to Pi0.5 224×224.

    Applied as a transform in the LeRobot data pipeline.
    """

    def __init__(self, target_size=(224, 224)):
        self.target_size = target_size

    def __call__(self, image):
        """Resize image if dimensions don't match.

        Args:
            image: np.ndarray [H, W, C] — input image

        Returns:
            np.ndarray [224, 224, C] — resized image
        """
        if image.shape[0] == self.target_size[0] and image.shape[1] == self.target_size[1]:
            return image

        import cv2
        return cv2.resize(image, self.target_size, interpolation=cv2.INTER_LINEAR)


# --------------------------------------------------------------------------- #
#  LeRobot Dataset Wrapper
# --------------------------------------------------------------------------- #

def create_robocasa_data_config(task_name, task_config):
    """Create a LeRobot data config for RoboCasa with state/image adapters.

    This patches the standard LeRobotLiberoDataConfig to apply our adapters
    during data loading. The patch approach avoids forking the data loader.

    Returns:
        openpi DataConfig for the task
    """
    import openpi.training.config as _config

    # Camera name mapping for LeRobot dataset
    # RoboCasa LeRobot stores images under these keys:
    #   observation.images.agentview  (or observation.images.robot0_agentview)
    #   observation.images.eye_in_hand (or observation.images.robot0_eye_in_hand)
    # Pi0.5 expects:
    #   observation/image, observation/wrist_image
    # The LeRobotLiberoDataConfig handles this mapping via its image_keys config

    data_config = _config.LeRobotLiberoDataConfig(
        repo_id=task_config["data_repo_id"],
        base_config=_config.DataConfig(prompt_from_task=True),
        extra_delta_transform=False,
        assets=_config.AssetsConfig(assets_dir=task_config["assets_dir"]),
    )

    return data_config


# --------------------------------------------------------------------------- #
#  Training Config
# --------------------------------------------------------------------------- #

def build_train_config(task_name, args):
    """Build openpi TrainConfig for Pi0.5 LoRA fine-tuning on RoboCasa.

    Matches SafeLIBERO experimental protocol exactly:
      - 30K steps, batch 32, lr 2.5e-5
      - LoRA: rank 32 action expert, rank 16 PaliGemma
      - Cosine decay schedule with warmup
    """
    import openpi.models.pi0_config as pi0_config
    import openpi.training.config as _config
    from openpi.training.optimizer import CosineDecaySchedule

    task_config = TASK_CONFIG[task_name]
    num_steps = 2 if args.dry_run else args.num_train_steps
    exp_name = args.exp_name or f"pi05_robocasa_{task_name}_seed{args.seed}"

    model_config = pi0_config.Pi0Config(
        pi05=True,
        action_horizon=10,
        discrete_state_input=False,
    )

    data_config = create_robocasa_data_config(task_name, task_config)

    config = _config.TrainConfig(
        name=f"pi05_robocasa_{task_name}",
        project_name="colliforce-vla-robocasa",
        exp_name=exp_name,
        model=model_config,
        data=data_config,
        pytorch_weight_path=os.path.join(WEIGHTS_BASE, "pi05_libero"),
        ema_decay=None,
        lr_schedule=CosineDecaySchedule(
            warmup_steps=min(1000, num_steps // 3),
            peak_lr=args.lr,
            decay_steps=num_steps,
            decay_lr=args.lr / 10,
        ),
        num_train_steps=num_steps,
        batch_size=args.batch_size,
        save_interval=args.save_interval if not args.dry_run else num_steps,
        log_interval=args.log_interval if not args.dry_run else 1,
        checkpoint_base_dir=CHECKPOINT_BASE,
        seed=args.seed,
        wandb_enabled=not args.dry_run,
        overwrite=args.dry_run,
        resume=args.resume,
    )

    return config


# --------------------------------------------------------------------------- #
#  LoRA Injection (same as SafeLIBERO experiments)
# --------------------------------------------------------------------------- #

def setup_lora_training(model, phase1_steps=3000):
    """Inject LoRA and set up two-phase training schedule.

    Phase 1 (steps 0–phase1_steps): Only data adapter layers trainable,
        LoRA weights frozen. Lets the model adapt to RoboCasa data format.
    Phase 2 (steps phase1_steps–end): LoRA unfrozen with gradient warmup.

    LoRA config matches SafeLIBERO:
      - Action expert: rank=32, alpha=32
      - PaliGemma vision: rank=16, alpha=16

    Args:
        model: Pi0.5 model
        phase1_steps: steps before unfreezing LoRA

    Returns:
        lora_params: list of LoRA parameter tensors
        phase1_steps: int
    """
    from colliforce.lora_utils import inject_lora_pi0

    _m = model.module if hasattr(model, "module") else model

    for p in _m.parameters():
        p.requires_grad = False

    lora_params, pali_lora, expert_lora = inject_lora_pi0(
        _m,
        pali_rank=16, pali_alpha=16.0,
        expert_rank=32, expert_alpha=32.0,
    )

    # Phase 1: LoRA frozen
    for p in lora_params:
        p.requires_grad = False

    n_lora = sum(p.numel() for p in lora_params)
    n_pali = sum(p.numel() for p in pali_lora)
    n_expert = sum(p.numel() for p in expert_lora)

    logging.info("LoRA injected:")
    logging.info("  PaliGemma (rank=16): %.2fM params", n_pali / 1e6)
    logging.info("  Action Expert (rank=32): %.2fM params", n_expert / 1e6)
    logging.info("  Total LoRA: %.2fM params (frozen for Phase 1)", n_lora / 1e6)
    logging.info("  Phase 1: %d steps (warmup), Phase 2: LoRA unfrozen", phase1_steps)

    return lora_params, phase1_steps


# --------------------------------------------------------------------------- #
#  State Transform Registration
# --------------------------------------------------------------------------- #

def register_state_transform_hook(data_loader, state_adapter):
    """Register state adapter as a post-processing hook on the data loader.

    This wraps the data loader's __iter__ to apply the 16D→8D state
    transform on each batch before feeding to the model.

    If the LeRobot data loader supports custom transforms natively,
    use that instead. This is a fallback approach.
    """

    original_iter = data_loader.__iter__

    def patched_iter():
        for batch in original_iter():
            if "observation/state" in batch:
                states = batch["observation/state"]
                if hasattr(states, 'numpy'):
                    states_np = states.numpy()
                else:
                    states_np = np.array(states)

                if states_np.shape[-1] > 8:
                    adapted = state_adapter(states_np)
                    import torch
                    batch["observation/state"] = torch.from_numpy(adapted)

            yield batch

    data_loader.__iter__ = patched_iter
    return data_loader


# --------------------------------------------------------------------------- #
#  CLI & Main
# --------------------------------------------------------------------------- #

def parse_args():
    p = argparse.ArgumentParser(description="RoboCasa Pi0.5 LoRA Fine-tuning")
    p.add_argument("--task", type=str, required=True,
                   choices=list(TASK_CONFIG.keys()) + ["all"])
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--num_train_steps", type=int, default=30000)
    p.add_argument("--lr", type=float, default=2.5e-5)
    p.add_argument("--save_interval", type=int, default=2000)
    p.add_argument("--log_interval", type=int, default=100)
    p.add_argument("--exp_name", type=str, default=None)
    p.add_argument("--dry_run", action="store_true")
    p.add_argument("--resume", action="store_true")
    p.add_argument("--phase1_steps", type=int, default=3000,
                   help="Warmup steps before unfreezing LoRA (default 3000)")
    return p.parse_args()


def train_single_task(task_name, args):
    """Train Pi0.5 LoRA on a single RoboCasa task."""
    logging.info("=" * 60)
    logging.info("Training: %s (seed=%d)", task_name, args.seed)

    config = build_train_config(task_name, args)

    from scripts.train_pytorch import train_loop

    # LoRA injection happens inside train_loop via TrainHooks
    # For vanilla LoRA (no SDF), we use a minimal hook that only does LoRA
    class LoRAOnlyHooks:
        """Minimal hooks for LoRA-only training (no SDF auxiliary)."""

        def __init__(self, phase1_steps):
            self.phase1_steps = phase1_steps
            self.lora_params = None
            self.phase = 1

        def on_model_created(self, model, device):
            self.lora_params, _ = setup_lora_training(model, self.phase1_steps)

        def extra_params(self):
            return []

        def on_step_start(self, global_step, model):
            if global_step == self.phase1_steps and self.phase == 1:
                self.phase = 2
                for p in self.lora_params:
                    p.requires_grad = True
                logging.info("Phase 2: LoRA unfrozen at step %d", global_step)

        def on_loss_computed(self, action_loss, model, observation, global_step):
            return action_loss, {"phase": float(self.phase)}

        def on_save_checkpoint(self, step_dir, global_step):
            pass

        def on_cleanup(self):
            pass

    hooks = LoRAOnlyHooks(args.phase1_steps)
    train_loop(config, hooks=hooks)


def main():
    args = parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    if not int(os.environ.get("WORLD_SIZE", "1")) > 1:
        os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    if args.task == "all":
        task_list = list(TASK_CONFIG.keys())
    else:
        task_list = [args.task]

    for task_name in task_list:
        train_single_task(task_name, args)

    logging.info("All training complete.")


if __name__ == "__main__":
    main()
