"""
HTTP client mimicking Pi05Wrapper's interface, talking to pi05_server.

Drop-in replacement for Pi05Wrapper in evaluate.py: instantiate with
`Pi05Client(server_url=...)` instead of `Pi05Wrapper(path)`. Same methods
return torch tensors on a configurable device (default cpu, since the
server already detached + CPU-copied).

Per-instance action_queue is maintained client-side: server is stateless.
"""
from collections import deque

import msgpack
import numpy as np
import requests
import torch

try:
    from utils import FULL_ACTION_DIM
except ImportError:
    from .utils import FULL_ACTION_DIM


def _encode_nd(a: np.ndarray) -> dict:
    return {"_nd": True, "dtype": str(a.dtype), "shape": list(a.shape), "data": a.tobytes()}


def _pack(obj):
    if isinstance(obj, np.ndarray):
        return _encode_nd(obj)
    if isinstance(obj, dict):
        return {k: _pack(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_pack(v) for v in obj]
    return obj


def _unpack(obj):
    if isinstance(obj, dict):
        if obj.get("_nd"):
            return np.frombuffer(obj["data"], dtype=np.dtype(obj["dtype"])).reshape(obj["shape"])
        return {k: _unpack(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_unpack(v) for v in obj]
    return obj


class Pi05Client:
    """HTTP client mirroring Pi05Wrapper's API."""

    VLM_HIDDEN_SIZE = 2048

    def __init__(self, server_url: str = "http://localhost:8000",
                 device: str = "cpu", timeout: float = 60.0):
        self.server_url = server_url.rstrip("/")
        self.device = torch.device(device)
        self.timeout = timeout
        self._action_queue: deque = deque()
        self.vlm_hidden_size = self.VLM_HIDDEN_SIZE
        self._session = requests.Session()
        self._verify_server()

    def _verify_server(self):
        try:
            r = self._session.get(f"{self.server_url}/health", timeout=5.0)
            r.raise_for_status()
            info = r.json()
            if info.get("status") != "ready":
                raise RuntimeError(f"Server not ready: {info}")
            print(f"[pi05_client] Connected to {self.server_url}: {info}",
                  flush=True)
        except Exception as e:
            raise RuntimeError(
                f"Cannot reach pi05_server at {self.server_url}: {e}"
            )

    def _post_predict(self, agentview_rgb, task_name, robot_state,
                       eye_in_hand_rgb, K, mode="kfull",
                       threshold=0.1, k_init=2, k_full=5,
                       batched_k=True):
        if not isinstance(agentview_rgb, np.ndarray):
            agentview_rgb = np.asarray(agentview_rgb)
        if eye_in_hand_rgb is not None and not isinstance(eye_in_hand_rgb, np.ndarray):
            eye_in_hand_rgb = np.asarray(eye_in_hand_rgb)
        robot_state_np = np.asarray(robot_state, dtype=np.float32)

        req = {
            "agentview_rgb": agentview_rgb,
            "task_name": task_name,
            "robot_state": robot_state_np,
            "eye_in_hand_rgb": eye_in_hand_rgb,
            "K": int(K),
            "mode": mode,
            "batched_k": bool(batched_k),
            "threshold": float(threshold),
            "k_init": int(k_init),
            "k_full": int(k_full),
        }
        body = msgpack.packb(_pack(req), use_bin_type=True)
        r = self._session.post(
            f"{self.server_url}/predict",
            data=body,
            headers={"Content-Type": "application/x-msgpack"},
            timeout=self.timeout,
        )
        r.raise_for_status()
        resp = _unpack(msgpack.unpackb(r.content, raw=False))
        return resp

    def get_obs_features_and_samples(self, agentview_rgb, task_name,
                                      robot_state, eye_in_hand_rgb=None,
                                      K=10):
        resp = self._post_predict(
            agentview_rgb, task_name, robot_state, eye_in_hand_rgb,
            K=K, mode="kfull",
        )
        obs_feat = torch.from_numpy(resp["obs_features"]).to(self.device)
        samples = torch.from_numpy(resp["samples"]).to(self.device)
        return obs_feat, samples

    def get_obs_features_and_samples_adaptive(self, agentview_rgb, task_name,
                                               robot_state, eye_in_hand_rgb=None,
                                               threshold=0.1, k_init=2,
                                               k_full=5):
        resp = self._post_predict(
            agentview_rgb, task_name, robot_state, eye_in_hand_rgb,
            K=k_full, mode="adaptive",
            threshold=threshold, k_init=k_init, k_full=k_full,
        )
        obs_feat = torch.from_numpy(resp["obs_features"]).to(self.device)
        samples = torch.from_numpy(resp["samples"]).to(self.device)
        return obs_feat, samples, resp["metadata"]

    def reset_action_queue(self):
        self._action_queue.clear()

    def predict_action(self, agentview_rgb, task_name, robot_state,
                       eye_in_hand_rgb=None, K: int = 1):
        if not self._action_queue:
            _obs_feat, samples = self.get_obs_features_and_samples(
                agentview_rgb=agentview_rgb,
                task_name=task_name,
                robot_state=robot_state,
                eye_in_hand_rgb=eye_in_hand_rgb,
                K=K,
            )
            chunk = samples[0].mean(dim=0)
            chunk_np = chunk.detach().cpu().numpy()
            for i in range(chunk_np.shape[0]):
                self._action_queue.append(chunk_np[i])
        return self._action_queue.popleft()
