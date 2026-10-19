"""
FastAPI server wrapping Pi05Wrapper for shared-GPU inference.

Stateless: each /predict request is independent (no client session). Client
receives the full K action chunks; chunk replay + queue are client-side
responsibilities.

Batched K-sample: K samples are stacked along the batch dimension and
denoised in one forward pass per ODE step (num_inference_steps total)
instead of K * num_inference_steps sequential calls. The batched method is
attached to the wrapper instance at startup, so pi05_wrapper.py is not
modified.

Protocol: msgpack (binary) over HTTP. NumPy arrays are encoded as
{"_nd": True, "dtype": str, "shape": list, "data": bytes}.

Usage:
    CUDA_VISIBLE_DEVICES=3 python src/pi05_server.py \\
        --model_path /root/autodl-tmp/models/pi05_libero_finetuned/ \\
        --host 0.0.0.0 --port 8000
"""
import argparse
import os
import sys
import time
from types import MethodType

import msgpack
import numpy as np
import torch
import uvicorn
from fastapi import FastAPI, Request, Response

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _encode_nd(a: np.ndarray) -> dict:
    return {"_nd": True, "dtype": str(a.dtype), "shape": list(a.shape), "data": a.tobytes()}


def _decode_nd(obj):
    if isinstance(obj, dict) and obj.get("_nd"):
        return np.frombuffer(obj["data"], dtype=np.dtype(obj["dtype"])).reshape(obj["shape"])
    return obj


def _unpack_obj(obj):
    if isinstance(obj, dict):
        if obj.get("_nd"):
            return _decode_nd(obj)
        return {k: _unpack_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_unpack_obj(v) for v in obj]
    return obj


def _pack_obj(obj):
    if isinstance(obj, np.ndarray):
        return _encode_nd(obj)
    if isinstance(obj, dict):
        return {k: _pack_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_pack_obj(v) for v in obj]
    return obj


# --- Batched K-sample generation -------------------------------------------
def _generate_k_samples_batched(self, past_key_values, prefix_pad_masks,
                                  K: int) -> torch.Tensor:
    """Single forward pass per ODE step over K samples stacked in batch dim.

    HuggingFace DynamicCache exposes `batch_repeat_interleave(K)`. Since
    denoise_step() inside lerobot's PI05 deep-copies past_key_values per
    call, the expanded cache is safe to reuse across all denoise steps and
    will not pollute the original prefix cache.
    """
    try:
        from utils import FULL_ACTION_DIM
    except ImportError:
        from .utils import FULL_ACTION_DIM
    import copy as _copy

    B = prefix_pad_masks.shape[0]
    if B != 1:
        raise NotImplementedError(
            "generate_k_samples_batched only supports B=1 (single observation)"
        )
    chunk_size = self.config.chunk_size
    max_act_dim = self.config.max_action_dim
    num_steps = self.config.num_inference_steps
    dt = -1.0 / num_steps

    # Expand prefix to K. Use deep-copy + batch_repeat_interleave so the
    # original prefix cache is untouched (allowing the caller to invoke
    # multiple generations from the same prefix, e.g. adaptive K).
    kv_K = _copy.deepcopy(past_key_values)
    kv_K.batch_repeat_interleave(K)
    pad_masks_K = prefix_pad_masks.repeat_interleave(K, dim=0).contiguous()

    noise = self.model.sample_noise((K, chunk_size, max_act_dim), self.device)
    x_t = noise
    for step in range(num_steps):
        time_val = 1.0 + step * dt
        time_tensor = torch.full(
            (K,), time_val, dtype=torch.float32, device=self.device
        )
        v_t = self.model.denoise_step(
            prefix_pad_masks=pad_masks_K,
            past_key_values=kv_K,
            x_t=x_t,
            timestep=time_tensor,
        )
        x_t = x_t + dt * v_t

    raw_action = x_t[:, :, :FULL_ACTION_DIM]
    unnorm_action = self._unnormalize_action(raw_action)
    # Reshape to (B, K, chunk_size, FULL_ACTION_DIM) — same layout as
    # sequential generate_k_samples.
    return unnorm_action.unsqueeze(0)


def _get_obs_features_and_samples_batched(self, agentview_rgb, task_name,
                                            robot_state, eye_in_hand_rgb=None,
                                            K: int = 10):
    """End-to-end batched K: prefix-encode once, denoise K times in parallel."""
    imgs, img_masks, lt, lm = self.preprocess_obs(
        agentview_rgb, task_name, robot_state, eye_in_hand_rgb
    )
    obs_feat, kv_cache, pad_masks = self.encode_prefix(
        imgs, img_masks, lt, lm
    )
    samples = self.generate_k_samples_batched(kv_cache, pad_masks, K=K)
    return obs_feat, samples


def _attach_batched_methods(wrapper):
    wrapper.generate_k_samples_batched = MethodType(
        _generate_k_samples_batched, wrapper
    )
    wrapper.get_obs_features_and_samples_batched = MethodType(
        _get_obs_features_and_samples_batched, wrapper
    )
    return wrapper


# --- FastAPI app -----------------------------------------------------------
app = FastAPI()
STATE: dict = {}


def _vram_gb() -> float:
    if not torch.cuda.is_available():
        return 0.0
    return torch.cuda.memory_allocated() / 1024**3


def _vram_reserved_gb() -> float:
    if not torch.cuda.is_available():
        return 0.0
    return torch.cuda.memory_reserved() / 1024**3


@app.get("/health")
def health():
    if STATE.get("wrapper") is None:
        return {"status": "loading"}
    return {
        "status": "ready",
        "model_path": STATE["model_path"],
        "device": STATE["device"],
        "vram_allocated_gb": _vram_gb(),
        "vram_reserved_gb": _vram_reserved_gb(),
        "supports_batched_k": True,
    }


@app.post("/predict")
async def predict(request: Request):
    raw = await request.body()
    req = _unpack_obj(msgpack.unpackb(raw, raw=False))

    agentview = req["agentview_rgb"]
    if not isinstance(agentview, np.ndarray):
        raise ValueError("agentview_rgb must be ndarray")
    task_name = req["task_name"]
    robot_state = np.asarray(req["robot_state"], dtype=np.float32)
    eye_in_hand = req.get("eye_in_hand_rgb")
    K = int(req.get("K", 1))
    mode = req.get("mode", "kfull")  # "kfull" or "adaptive"
    batched_k = bool(req.get("batched_k", STATE.get("batched_k_default", True)))

    t0 = time.perf_counter()
    wrapper = STATE["wrapper"]

    if mode == "adaptive":
        threshold = float(req.get("threshold", 0.1))
        k_init = int(req.get("k_init", 2))
        k_full = int(req.get("k_full", 5))
        obs_feat, samples, meta = wrapper.get_obs_features_and_samples_adaptive(
            agentview_rgb=agentview,
            task_name=task_name,
            robot_state=robot_state,
            eye_in_hand_rgb=eye_in_hand,
            threshold=threshold,
            k_init=k_init,
            k_full=k_full,
        )
        metadata = dict(meta)
    else:
        if batched_k and K > 1:
            obs_feat, samples = wrapper.get_obs_features_and_samples_batched(
                agentview_rgb=agentview,
                task_name=task_name,
                robot_state=robot_state,
                eye_in_hand_rgb=eye_in_hand,
                K=K,
            )
        else:
            obs_feat, samples = wrapper.get_obs_features_and_samples(
                agentview_rgb=agentview,
                task_name=task_name,
                robot_state=robot_state,
                eye_in_hand_rgb=eye_in_hand,
                K=K,
            )
        metadata = {}

    elapsed_ms = (time.perf_counter() - t0) * 1000.0

    obs_feat_np = obs_feat.detach().to(dtype=torch.float32).cpu().numpy()
    samples_np = samples.detach().to(dtype=torch.float32).cpu().numpy()

    payload = {
        "obs_features": obs_feat_np,
        "samples": samples_np,
        "metadata": metadata,
        "latency_ms": elapsed_ms,
    }
    body = msgpack.packb(_pack_obj(payload), use_bin_type=True)
    return Response(content=body, media_type="application/x-msgpack")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str,
                        default="/root/autodl-tmp/models/pi05_libero_finetuned/")
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--batched_k_default", action="store_true", default=True,
                        help="Use batched K-sample generation by default")
    parser.add_argument("--no_batched_k", dest="batched_k_default",
                        action="store_false")
    args = parser.parse_args()

    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

    from pi05_wrapper import Pi05Wrapper

    print(f"[pi05_server] Loading PI05 from {args.model_path} on {args.device}...",
          flush=True)
    t0 = time.perf_counter()
    wrapper = Pi05Wrapper(args.model_path, device=args.device)
    _attach_batched_methods(wrapper)
    load_t = time.perf_counter() - t0

    STATE["wrapper"] = wrapper
    STATE["model_path"] = args.model_path
    STATE["device"] = args.device
    STATE["batched_k_default"] = args.batched_k_default

    print(f"[pi05_server] Model loaded in {load_t:.1f}s, "
          f"VRAM allocated={_vram_gb():.2f} GB, "
          f"reserved={_vram_reserved_gb():.2f} GB", flush=True)
    print(f"[pi05_server] Listening on {args.host}:{args.port} "
          f"(batched_k_default={args.batched_k_default})", flush=True)

    uvicorn.run(app, host=args.host, port=args.port, log_level="warning",
                access_log=False)


if __name__ == "__main__":
    main()
