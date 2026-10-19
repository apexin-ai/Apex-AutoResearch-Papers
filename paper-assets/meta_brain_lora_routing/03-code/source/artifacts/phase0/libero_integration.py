"""
OpenPI/LIBERO-Plus integration for pi0 activation collection.

Bridges LIBERO-Plus simulation environments with the pi0 model, handling
observation preprocessing, action chunking, and perturbation-specific
task selection. Designed for direct model inference (no WebSocket server)
so that ActivationCollector hooks fire during forward passes.

Input:
    LIBERO-Plus env observations: agentview_image [256,256,3],
    robot0_eye_in_hand_image [256,256,3], robot0_eef_pos [3],
    robot0_eef_quat [4], robot0_gripper_qpos [2], plus task language.

Output:
    Per-episode activation dict (via ActivationCollector hooks on the
    underlying PI0Pytorch model) and task metadata.

Integration with collect_activations.py:
    from libero_integration import load_pi0_for_collection, run_episode

    policy, model = load_pi0_for_collection(checkpoint_path, device)
    collector = ActivationCollector(model)
    collector.register_hooks()
    result = run_episode(policy, collector, "camera_viewpoints", device)
"""

import collections
import logging
import math
import re
import random
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn as nn

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants (from OpenPI's examples/libero/main.py)
# ---------------------------------------------------------------------------

LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
LIBERO_ENV_RESOLUTION = 256
MODEL_INPUT_RESOLUTION = 224
DEFAULT_REPLAN_STEPS = 5
DEFAULT_NUM_STEPS_WAIT = 10

MAX_STEPS = {
    "libero_spatial": 220,
    "libero_object": 280,
    "libero_goal": 300,
    "libero_10": 520,
    "libero_90": 400,
}

VALID_PERTURBATION_TYPES = [
    "camera_viewpoints",
    "light_conditions",
    "background_textures",
    "objects_layout",
    "robot_initial_states",
    "sensor_noise",
]


# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------

def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
    """Quaternion [x,y,z,w] -> axis-angle [ax,ay,az]."""
    q = np.asarray(quat, dtype=np.float64)
    norm = np.linalg.norm(q)
    if norm < 1e-8:
        return np.zeros(3, dtype=np.float32)
    q /= norm
    sin_half = np.linalg.norm(q[:3])
    if sin_half < 1e-8:
        return np.zeros(3, dtype=np.float32)
    angle = 2.0 * math.atan2(sin_half, q[3])
    axis = q[:3] / sin_half
    return (axis * angle).astype(np.float32)


# ---------------------------------------------------------------------------
# Image preprocessing
# ---------------------------------------------------------------------------

def _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:
    """Resize image with aspect-preserving padding to (size, size, 3) uint8."""
    try:
        from openpi_client.image_tools import resize_with_pad, convert_to_uint8
        return convert_to_uint8(resize_with_pad(img, size, size))
    except ImportError:
        from PIL import Image as PILImage
        h, w = img.shape[:2]
        scale = min(size / h, size / w)
        new_h, new_w = int(h * scale), int(w * scale)
        resized = np.array(
            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)
        )
        canvas = np.zeros((size, size, 3), dtype=np.uint8)
        y0, x0 = (size - new_h) // 2, (size - new_w) // 2
        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
        return canvas


# ---------------------------------------------------------------------------
# Observation -> model input
# ---------------------------------------------------------------------------

def obs_to_model_input(
    obs: dict,
    task_description: str,
    resize_size: int = MODEL_INPUT_RESOLUTION,
) -> dict:
    """Convert LIBERO observation to the dict format expected by policy.infer().

    LIBERO obs keys used:
        agentview_image          [H, W, 3] uint8
        robot0_eye_in_hand_image [H, W, 3] uint8
        robot0_eef_pos           [3] float
        robot0_eef_quat          [4] float (x,y,z,w)
        robot0_gripper_qpos      [2] float

    Returns dict with keys:
        observation/image        [224, 224, 3] uint8
        observation/wrist_image  [224, 224, 3] uint8
        observation/state        [8] float32
        prompt                   str

    Note: sensor noise is applied by the LIBERO-Plus environment itself
    (motion_blur, gaussian_blur, zoom_blur, fog, glass_blur at various
    severity levels), not at the observation preprocessing stage.
    """
    # Flip images 180 degrees (OpenPI training convention)
    base_img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])

    base_img = _resize_with_pad(base_img, resize_size)
    wrist_img = _resize_with_pad(wrist_img, resize_size)

    state = np.concatenate([
        obs["robot0_eef_pos"].astype(np.float32),
        _quat2axisangle(obs["robot0_eef_quat"]),
        obs["robot0_gripper_qpos"].astype(np.float32),
    ])  # [8]

    return {
        "observation/image": base_img,
        "observation/wrist_image": wrist_img,
        "observation/state": state,
        "prompt": task_description,
    }


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def _extract_model(policy: object) -> nn.Module:
    """Extract the underlying PI0Pytorch nn.Module from an OpenPI Policy."""
    for attr in ("_model", "model", "_network", "network"):
        candidate = getattr(policy, attr, None)
        if isinstance(candidate, nn.Module):
            return candidate

    for attr in dir(policy):
        if attr.startswith("__"):
            continue
        try:
            candidate = getattr(policy, attr)
            if isinstance(candidate, nn.Module):
                log.warning(
                    "Found model at policy.%s (unexpected attribute name)", attr
                )
                return candidate
        except Exception:
            continue

    raise AttributeError(
        "Cannot find nn.Module in Policy object. "
        "Inspect the OpenPI Policy class and update _extract_model()."
    )


def _ensure_openpi_imports():
    """Stub out lerobot (training-only dep) before importing OpenPI inference code."""
    import sys
    import types
    for mod in [
        "lerobot", "lerobot.common", "lerobot.common.datasets",
        "lerobot.common.datasets.lerobot_dataset",
    ]:
        if mod not in sys.modules:
            sys.modules[mod] = types.ModuleType(mod)


def load_pi0_for_collection(
    checkpoint_path: str,
    device: str,
    config_name: str = "pi0_libero",
) -> tuple[object, nn.Module]:
    """Load pi0 via OpenPI's policy system for activation collection.

    Uses create_trained_policy() so all transforms (LiberoInputs, Normalize,
    TokenizePrompt, PadStatesAndActions, ResizeImages) and normalization
    statistics are applied correctly.

    Returns:
        (policy, model) where
        - policy: OpenPI Policy; call policy.infer(obs_dict)
        - model:  PI0Pytorch nn.Module; pass to ActivationCollector
    """
    _ensure_openpi_imports()

    try:
        from openpi.training import config as _config
        from openpi.policies import policy_config
    except ImportError:
        raise ImportError(
            "openpi package required. "
            "Clone https://github.com/Physical-Intelligence/openpi "
            "and install with: pip install -e ."
        )

    train_config = _config.get_config(config_name)
    policy = policy_config.create_trained_policy(
        train_config, checkpoint_path, pytorch_device=device
    )

    model = _extract_model(policy)
    log.info("Loaded pi0 policy (config=%s) on %s", config_name, device)
    return policy, model


# ---------------------------------------------------------------------------
# LIBERO-Plus environment
# ---------------------------------------------------------------------------

def _classify_task(task_name: str) -> str | None:
    """Classify a LIBERO-Plus task name into its perturbation type.

    LIBERO-Plus task naming conventions:
      Compound: {base}_[language_N_]view_{H}_{V}_{S}_{R}_{E}_initstate_{I}[_noise_{N}]
        - camera_viewpoints:    (H,V,S,R,E) != (0,0,100,0,0), I==0, no noise
        - robot_initial_states: default view, I != 0, no noise
        - sensor_noise:         default view, I==0, N > 0
        - base (nominal):       all defaults
      Simple suffixes:
        - light_conditions:     _light_\\d+
        - background_textures:  _table_\\d+ or _tb_\\d+
        - objects_layout:       _add_\\d+ or _level\\d+

    Returns perturbation type string, or None for base/nominal tasks.
    """
    if "_view_" in task_name:
        m = re.search(
            r"_view_(-?\d+)_(-?\d+)_(\d+)_(-?\d+)_(-?\d+)_initstate_(\d+)(?:_noise_(\d+))?",
            task_name,
        )
        if not m:
            return None
        H, V, S, R, E = int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])
        initstate = int(m[6])
        noise = int(m[7]) if m[7] else 0

        if noise > 0:
            return "sensor_noise"
        if (H, V, S, R, E) != (0, 0, 100, 0, 0):
            return "camera_viewpoints"
        if initstate != 0:
            return "robot_initial_states"
        return None

    if re.search(r"_light_\d+$", task_name):
        return "light_conditions"
    if re.search(r"_(?:table|tb)_\d+$", task_name):
        return "background_textures"
    if re.search(r"_add_\d+$", task_name) or re.search(r"_level\d+", task_name):
        return "objects_layout"

    return None


def _get_task_indices(
    suite: object,
    perturbation_type: str | None,
    num_tasks: int,
) -> list[int]:
    """Return task indices matching the requested perturbation type."""
    if perturbation_type is not None and perturbation_type not in VALID_PERTURBATION_TYPES:
        raise ValueError(
            f"Unknown perturbation_type={perturbation_type!r}. "
            f"Valid: {VALID_PERTURBATION_TYPES}"
        )

    indices = []
    matched_names = []
    for i in range(num_tasks):
        task = suite.get_task(i)
        name = getattr(task, "name", "") or getattr(task, "bddl_file", "")
        classified = _classify_task(name)

        if perturbation_type is None:
            if classified is None:
                indices.append(i)
                matched_names.append(name)
        elif classified == perturbation_type:
            indices.append(i)
            matched_names.append(name)

    if not indices:
        raise RuntimeError(
            f"No tasks match perturbation_type={perturbation_type!r} "
            f"among {num_tasks} tasks. Verify the suite contains "
            f"LIBERO-Plus perturbation variants (not base libero_90)."
        )

    log.info(
        "%s: matched %d/%d tasks (e.g. %s)",
        perturbation_type or "nominal",
        len(indices),
        num_tasks,
        matched_names[:3],
    )
    return indices


def create_libero_env(
    task_suite_name: str = "libero_spatial",
    perturbation_type: str | None = None,
    task_idx: int | None = None,
    seed: int = 42,
) -> tuple[Any, str, np.ndarray, int]:
    """Create a LIBERO / LIBERO-Plus evaluation environment.

    Returns:
        (env, task_description, init_states, selected_task_idx)
    """
    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    benchmark_dict = benchmark.get_benchmark_dict()
    suite = benchmark_dict[task_suite_name]()
    num_tasks = suite.n_tasks

    valid_indices = _get_task_indices(suite, perturbation_type, num_tasks)

    if task_idx is not None and task_idx in valid_indices:
        selected_idx = task_idx
    else:
        selected_idx = random.choice(valid_indices)

    task = suite.get_task(selected_idx)
    task_description = task.language

    task_bddl_file = (
        Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
    )
    env = OffScreenRenderEnv(
        bddl_file_name=str(task_bddl_file),
        camera_heights=LIBERO_ENV_RESOLUTION,
        camera_widths=LIBERO_ENV_RESOLUTION,
    )
    env.seed(seed)

    init_states = suite.get_task_init_states(selected_idx)
    return env, task_description, init_states, selected_idx


# ---------------------------------------------------------------------------
# Episode rollout
# ---------------------------------------------------------------------------

def run_episode(
    policy: object,
    collector: object,
    perturbation_type: str | None,
    device: str,
    task_suite: str = "libero_spatial",
    seed: int = 42,
    replan_steps: int = DEFAULT_REPLAN_STEPS,
    num_steps_wait: int = DEFAULT_NUM_STEPS_WAIT,
) -> dict[str, Any]:
    """Run one LIBERO-Plus episode, collecting activations at each replan point.

    Every replan_steps env steps, the policy is queried for a new action chunk.
    ActivationCollector hooks capture layer outputs during each policy.infer()
    call. Activations are averaged across all replan points.

    Sensor noise is applied by the LIBERO-Plus environment itself (via task
    name suffix _noise_N), not at the observation level.

    Returns dict with keys: activations, task_name, task_description,
    num_steps, success.
    """
    env, task_description, init_states, task_idx = create_libero_env(
        task_suite_name=task_suite,
        perturbation_type=perturbation_type,
        seed=seed,
    )

    max_steps = MAX_STEPS.get(task_suite, 400)

    step = 0
    success = False

    try:
        trial_idx = random.randint(0, len(init_states) - 1)
        obs = env.set_init_state(init_states[trial_idx])

        for _ in range(num_steps_wait):
            obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)

        action_plan: collections.deque = collections.deque()
        step_activations: list[dict] = []
        done = False

        while not done and step < max_steps:
            if len(action_plan) == 0:
                collector.clear()

                obs_dict = obs_to_model_input(obs, task_description)
                result = policy.infer(obs_dict)
                action_chunk = result["actions"]  # [horizon, 7]
                action_plan.extend(action_chunk[:replan_steps])

                pooled = collector.get_pooled()
                if pooled:
                    step_activations.append(pooled)

            action = action_plan.popleft()
            if isinstance(action, torch.Tensor):
                action = action.cpu().numpy()
            obs, reward, done, info = env.step(
                action.tolist() if hasattr(action, "tolist") else list(action)
            )
            step += 1

            if done or reward > 0:
                success = info.get("success", reward > 0)
    finally:
        env.close()

    return {
        "activations": _average_activations(step_activations),
        "task_name": f"{task_suite}/task_{task_idx}",
        "task_description": task_description,
        "num_steps": step,
        "success": success,
    }


def _average_activations(
    step_activations: list[dict[str, dict[str, torch.Tensor]]],
) -> dict[str, dict[str, torch.Tensor]]:
    """Average activation tensors across replan steps."""
    if not step_activations:
        return {}
    result: dict[str, dict[str, torch.Tensor]] = {}
    for layer in step_activations[0]:
        result[layer] = {}
        for strat in step_activations[0][layer]:
            tensors = [sa[layer][strat] for sa in step_activations]
            result[layer][strat] = torch.stack(tensors).mean(dim=0)
    return result
