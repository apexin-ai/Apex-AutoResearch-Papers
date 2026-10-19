# validate libero integration — Part 2 of 2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../validate-libero-integration.md) · [Structured JSON](../../../sessions/68/68f91d7adeed68e06ae6.json)

## Before a recorded user message

### Tool result

_source line 175 · 2026-05-15T12:01:18.570Z_

<details><summary>↩ Tool result · `toolu_01NdcaYZ8LCb75tf7gqBNGMK`</summary>

```text
1	"""
2	Collect frozen π₀ activations from LIBERO-Plus rollouts.
3	
4	Registers forward hooks on PaliGemma LLM layers and Action Expert layers,
5	runs episodes under each perturbation type (or nominal), and saves per-layer
6	activations with 4 pooling strategies in fp16.
7	
8	Usage:
9	    # Collect camera perturbation episodes
10	    python collect_activations.py \
11	        --checkpoint /path/to/pi0_base \
12	        --output_dir ./activations \
13	        --perturbation_type camera_viewpoints \
14	        --num_episodes 50 \
15	        --device cuda:0
16	
17	    # Collect all perturbation types
18	    python collect_activations.py \
19	        --checkpoint /path/to/pi0_base \
20	        --output_dir ./activations \
21	        --perturbation_type all \
22	        --num_episodes 50
23	
24	    # Collect nominal (no perturbation) baseline
25	    python collect_activations.py \
26	        --checkpoint /path/to/pi0_base \
27	        --output_dir ./activations \
28	        --perturbation_type nominal \
29	        --num_episodes 100
30	
31	Dependencies:
32	    torch, safetensors, openpi (for model loading), libero
33	"""
34	
35	import argparse
36	import logging
37	import os
38	from pathlib import Path
39	from typing import Any
40	
41	import torch
42	import torch.nn as nn
43	
44	from configs import (
45	    CLASS_6_TO_3_MAPPING,
46	    EXPERT_LAYER_TEMPLATE,
47	    EXPERT_LAYERS,
48	    PALIGEMMA_LAYER_TEMPLATE,
49	    PALIGEMMA_LAYERS,
50	    PERTURBATION_TYPES_6CLASS,
51	    POOLING_STRATEGIES,
52	)
53	from libero_integration import (
54	    load_pi0_for_collection,
55	    obs_to_model_input,
56	    run_episode,
57	)
58	
59	log = logging.getLogger(__name__)
60	
61	
62	# ---------------------------------------------------------------------------
63	# Pooling helpers
64	# ---------------------------------------------------------------------------
65	
66	def pool_activation(hidden_states: torch.Tensor, strategy: str) -> torch.Tensor:
67	    """Pool a (batch, seq_len, hidden_dim) tensor into (batch, D).
68	
69	    Strategies:
70	        mean       — mean over seq_len → (batch, hidden_dim)
71	        first      — first token       → (batch, hidden_dim)
72	        last       — last token        → (batch, hidden_dim)
73	        first_last — concat first+last → (batch, hidden_dim*2)
74	    """
75	    if strategy == "mean":
76	        return hidden_states.mean(dim=1)
77	    elif strategy == "first":
78	        return hidden_states[:, 0]
79	    elif strategy == "last":
80	        return hidden_states[:, -1]
81	    elif strategy == "first_last":
82	        return torch.cat([hidden_states[:, 0], hidden_states[:, -1]], dim=-1)
83	    raise ValueError(f"Unknown pooling strategy: {strategy}")
84	
85	
86	# ---------------------------------------------------------------------------
87	# Hook manager
88	# ---------------------------------------------------------------------------
89	
90	class ActivationCollector:
91	    """Registers hooks on specified layers and stores pooled activations."""
92	
93	    def __init__(self, model: nn.Module):
94	        self.model = model
95	        self._hooks: list[torch.utils.hooks.RemovableHook] = []
96	        self._raw: dict[str, torch.Tensor] = {}  # layer_name -> last hidden_states
97	
98	    def register_hooks(self) -> None:
99	        for i in PALIGEMMA_LAYERS:
100	            name = f"paligemma_layer_{i}"
101	            module_path = PALIGEMMA_LAYER_TEMPLATE.format(i=i)
102	            module = _get_submodule(self.model, module_path)
103	            self._hooks.append(
104	                module.register_forward_hook(self._make_hook(name))
105	            )
106	            log.info("Hooked %s -> %s", name, module_path)
107	
108	        for i in EXPERT_LAYERS:
109	            name = f"expert_layer_{i}"
110	            module_path = EXPERT_LAYER_TEMPLATE.format(i=i)
111	            module = _get_submodule(self.model, module_path)
112	            self._hooks.append(
113	                module.register_forward_hook(self._make_hook(name))
114	            )
115	            log.info("Hooked %s -> %s", name, module_path)
116	
117	    def _make_hook(self, name: str):
118	        def hook_fn(_module, _input, output):
119	            # Gemma layers return (hidden_states, ...) or just hidden_states
120	            if isinstance(output, tuple):
121	                h = output[0]
122	            else:
123	                h = output
124	            self._raw[name] = h.detach()
125	        return hook_fn
126	
127	    def get_pooled(self) -> dict[str, dict[str, torch.Tensor]]:
128	        """Return {layer_name: {pooling_strategy: tensor(fp16)}} from last forward."""
129	        result = {}
130	        for name, h in self._raw.items():
131	            result[name] = {}
132	            for strat in POOLING_STRATEGIES:
133	                pooled = pool_activation(h, strat)
134	                result[name][strat] = pooled.half().cpu()
135	        return result
136	
137	    def clear(self) -> None:
138	        self._raw.clear()
139	
140	    def remove_hooks(self) -> None:
141	        for h in self._hooks:
142	            h.remove()
143	        self._hooks.clear()
144	
145	
146	def _get_submodule(model: nn.Module, path: str) -> nn.Module:
147	    parts = path.split(".")
148	    m = model
149	    for p in parts:
150	        if p.isdigit():
151	            m = m[int(p)]
152	        else:
153	            m = getattr(m, p)
154	    return m
155	
156	
157	# load_pi0_model, rollout_episode, _obs_to_model_input replaced by
158	# load_pi0_for_collection, run_episode, obs_to_model_input from libero_integration
159	
160	
161	# ---------------------------------------------------------------------------
162	# Data saving
163	# ---------------------------------------------------------------------------
164	
165	def save_episodes(
166	    episodes: list[dict[str, Any]],
167	    perturbation_type: str,
168	    output_dir: Path,
169	) -> None:
170	    output_dir.mkdir(parents=True, exist_ok=True)
171	    out_path = output_dir / f"{perturbation_type}.pt"
172	
173	    # Support incremental collection: append to existing file
174	    if out_path.exists():
175	        existing = torch.load(out_path, weights_only=False)
176	        log.info("Appending %d episodes to existing %d in %s",
177	                 len(episodes), len(existing), out_path)
178	        episodes = existing + episodes
179	
180	    torch.save(episodes, out_path)
181	    log.info("Saved %d episodes to %s", len(episodes), out_path)
182	
183	
184	# ---------------------------------------------------------------------------
185	# Main
186	# ---------------------------------------------------------------------------
187	
188	def make_labels(perturbation_type: str) -> dict[str, int]:
189	    if perturbation_type == "nominal":
190	        return {"label_6class": -1, "label_3class": -1, "label_binary": 0}
191	
192	    label_6 = PERTURBATION_TYPES_6CLASS[perturbation_type]
193	    label_3 = CLASS_6_TO_3_MAPPING[label_6]
194	    return {"label_6class": label_6, "label_3class": label_3, "label_binary": 1}
195	
196	
197	def _set_seed(seed: int) -> None:
198	    import random
199	    import numpy as np
200	    random.seed(seed)
201	    np.random.seed(seed)
202	    torch.manual_seed(seed)
203	    if torch.cuda.is_available():
204	        torch.cuda.manual_seed_all(seed)
205	
206	
207	def collect(args: argparse.Namespace) -> None:
208	    _set_seed(args.seed)
209	    device = args.device
210	    output_dir = Path(args.output_dir)
211	
212	    log.info("Seed=%d, loading model from %s", args.seed, args.checkpoint)
213	    policy, model = load_pi0_for_collection(args.checkpoint, device)
214	
215	    collector = ActivationCollector(model)
216	    collector.register_hooks()
217	
218	    perturbation_types: list[str]
219	    if args.perturbation_type == "all":
220	        perturbation_types = list(PERTURBATION_TYPES_6CLASS.keys())
221	    else:
222	        perturbation_types = [args.perturbation_type]
223	
224	    for ptype in perturbation_types:
225	        is_nominal = ptype == "nominal"
226	        log.info("Collecting %d episodes for %s", args.num_episodes, ptype)
227	
228	        episodes = []
229	        for ep_idx in range(args.num_episodes):
230	            log.info("  Episode %d/%d", ep_idx + 1, args.num_episodes)
231	            try:
232	                result = run_episode(
233	                    policy, collector,
234	                    perturbation_type=None if is_nominal else ptype,
235	                    device=device,
236	                    task_suite=args.task_suite,
237	                    seed=args.seed + ep_idx,
238	                )
239	            except Exception:
240	                log.exception("Episode %d failed, skipping", ep_idx)
241	                continue
242	
243	            labels = make_labels(ptype)
244	            episode_data = {
245	                "activations": result["activations"],
246	                **labels,
247	                "metadata": {
248	                    "perturbation_type": ptype,
249	                    "task_name": result["task_name"],
250	                    "num_steps": result["num_steps"],
251	                    "success": result["success"],
252	                    "episode_idx": ep_idx,
253	                },
254	            }
255	            episodes.append(episode_data)
256	
257	        save_episodes(episodes, ptype, output_dir)
258	
259	    collector.remove_hooks()
260	    log.info("Collection complete.")
261	
262	
263	def parse_args() -> argparse.Namespace:
264	    p = argparse.ArgumentParser(
265	        description="Collect π₀ activations from LIBERO-Plus rollouts"
266	    )
267	    p.add_argument(
268	        "--checkpoint", type=str, required=True,
269	        help="Path to π₀ checkpoint directory (with .safetensors files)",
270	    )
271	    p.add_argument(
272	        "--output_dir", type=str, default="./activations",
273	        help="Directory to save activation .pt files",
274	    )
275	    valid_types = list(PERTURBATION_TYPES_6CLASS.keys()) + ["all", "nominal"]
276	    p.add_argument(
277	        "--perturbation_type", type=str, default="all",
278	        choices=valid_types,
279	        help="Perturbation type to collect, 'all' for all 6, or 'nominal'",
280	    )
281	    p.add_argument(
282	        "--num_episodes", type=int, default=50,
283	        help="Number of episodes per perturbation type",
284	    )
285	    p.add_argument(
286	        "--task_suite", type=str, default="libero_spatial",
287	        choices=["libero_spatial", "libero_object", "libero_goal", "libero_10", "libero_90"],
288	        help="LIBERO-Plus suite (libero_90 has no perturbation variants)",
289	    )
290	    p.add_argument(
291	        "--device", type=str, default="cuda:0",
292	        help="Device for model inference",
293	    )
294	    p.add_argument(
295	        "--seed", type=int, default=42,
296	        help="Global random seed for reproducibility",
297	    )
298	    return p.parse_args()
299	
300	
301	if __name__ == "__main__":
302	    logging.basicConfig(
303	        level=logging.INFO,
304	        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
305	    )
306	    args = parse_args()
307	    collect(args)
308	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "99c194d5-a48d-4cd7-991d-e3e69fac32c5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0/collect_activations.py",
      "content": "\"\"\"\nCollect frozen π₀ activations from LIBERO-Plus rollouts.\n\nRegisters forward hooks on PaliGemma LLM layers and Action Expert layers,\nruns episodes under each perturbation type (or nominal), and saves per-layer\nactivations with 4 pooling strategies in fp16.\n\nUsage:\n    # Collect camera perturbation episodes\n    python collect_activations.py \\\n        --checkpoint /path/to/pi0_base \\\n        --output_dir ./activations \\\n        --perturbation_type camera_viewpoints \\\n        --num_episodes 50 \\\n        --device cuda:0\n\n    # Collect all perturbation types\n    python collect_activations.py \\\n        --checkpoint /path/to/pi0_base \\\n        --output_dir ./activations \\\n        --perturbation_type all \\\n        --num_episodes 50\n\n    # Collect nominal (no perturbation) baseline\n    python collect_activations.py \\\n        --checkpoint /path/to/pi0_base \\\n        --output_dir ./activations \\\n        --perturbation_type nominal \\\n        --num_episodes 100\n\nDependencies:\n    torch, safetensors, openpi (for model loading), libero\n\"\"\"\n\nimport argparse\nimport logging\nimport os\nfrom pathlib import Path\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\n\nfrom configs import (\n    CLASS_6_TO_3_MAPPING,\n    EXPERT_LAYER_TEMPLATE,\n    EXPERT_LAYERS,\n    PALIGEMMA_LAYER_TEMPLATE,\n    PALIGEMMA_LAYERS,\n    PERTURBATION_TYPES_6CLASS,\n    POOLING_STRATEGIES,\n)\nfrom libero_integration import (\n    load_pi0_for_collection,\n    obs_to_model_input,\n    run_episode,\n)\n\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Pooling helpers\n# ---------------------------------------------------------------------------\n\ndef pool_activation(hidden_states: torch.Tensor, strategy: str) -> torch.Tensor:\n    \"\"\"Pool a (batch, seq_len, hidden_dim) tensor into (batch, D).\n\n    Strategies:\n        mean       — mean over seq_len → (batch, hidden_dim)\n        first      — first token       → (batch, hidden_dim)\n        last       — last token        → (batch, hidden_dim)\n        first_last — concat first+last → (batch, hidden_dim*2)\n    \"\"\"\n    if strategy == \"mean\":\n        return hidden_states.mean(dim=1)\n    elif strategy == \"first\":\n        return hidden_states[:, 0]\n    elif strategy == \"last\":\n        return hidden_states[:, -1]\n    elif strategy == \"first_last\":\n        return torch.cat([hidden_states[:, 0], hidden_states[:, -1]], dim=-1)\n    raise ValueError(f\"Unknown pooling strategy: {strategy}\")\n\n\n# ---------------------------------------------------------------------------\n# Hook manager\n# ---------------------------------------------------------------------------\n\nclass ActivationCollector:\n    \"\"\"Registers hooks on specified layers and stores pooled activations.\"\"\"\n\n    def __init__(self, model: nn.Module):\n        self.model = model\n        self._hooks: list[torch.utils.hooks.RemovableHook] = []\n        self._raw: dict[str, torch.Tensor] = {}  # layer_name -> last hidden_states\n\n    def register_hooks(self) -> None:\n        for i in PALIGEMMA_LAYERS:\n            name = f\"paligemma_layer_{i}\"\n            module_path = PALIGEMMA_LAYER_TEMPLATE.format(i=i)\n            module = _get_submodule(self.model, module_path)\n            self._hooks.append(\n                module.register_forward_hook(self._make_hook(name))\n            )\n            log.info(\"Hooked %s -> %s\", name, module_path)\n\n        for i in EXPERT_LAYERS:\n            name = f\"expert_layer_{i}\"\n            module_path = EXPERT_LAYER_TEMPLATE.format(i=i)\n            module = _get_submodule(self.model, module_path)\n            self._hooks.append(\n                module.register_forward_hook(self._make_hook(name))\n            )\n            log.info(\"Hooked %s -> %s\", name, module_path)\n\n    def _make_hook(self, name: str):\n        def hook_fn(_module, _input, output):\n            # Gemma layers return (hidden_states, ...) or just hidden_states\n            if isinstance(output, tuple):\n                h = output[0]\n            else:\n                h = output\n            self._raw[name] = h.detach()\n        return hook_fn\n\n    def get_pooled(self) -> dict[str, dict[str, torch.Tensor]]:\n        \"\"\"Return {layer_name: {pooling_strategy: tensor(fp16)}} from last forward.\"\"\"\n        result = {}\n        for name, h in self._raw.items():\n            result[name] = {}\n            for strat in POOLING_STRATEGIES:\n                pooled = pool_activation(h, strat)\n                result[name][strat] = pooled.half().cpu()\n        return result\n\n    def clear(self) -> None:\n        self._raw.clear()\n\n    def remove_hooks(self) -> None:\n        for h in self._hooks:\n            h.remove()\n        self._hooks.clear()\n\n\ndef _get_submodule(model: nn.Module, path: str) -> nn.Module:\n    parts = path.split(\".\")\n    m = model\n    for p in parts:\n        if p.isdigit():\n            m = m[int(p)]\n        else:\n            m = getattr(m, p)\n    return m\n\n\n# load_pi0_model, rollout_episode, _obs_to_model_input replaced by\n# load_pi0_for_collection, run_episode, obs_to_model_input from libero_integration\n\n\n# ---------------------------------------------------------------------------\n# Data saving\n# ---------------------------------------------------------------------------\n\ndef save_episodes(\n    episodes: list[dict[str, Any]],\n    perturbation_type: str,\n    output_dir: Path,\n) -> None:\n    output_dir.mkdir(parents=True, exist_ok=True)\n    out_path = output_dir / f\"{perturbation_type}.pt\"\n\n    # Support incremental collection: append to existing file\n    if out_path.exists():\n        existing = torch.load(out_path, weights_only=False)\n        log.info(\"Appending %d episodes to existing %d in %s\",\n                 len(episodes), len(existing), out_path)\n        episodes = existing + episodes\n\n    torch.save(episodes, out_path)\n    log.info(\"Saved %d episodes to %s\", len(episodes), out_path)\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef make_labels(perturbation_type: str) -> dict[str, int]:\n    if perturbation_type == \"nominal\":\n        return {\"label_6class\": -1, \"label_3class\": -1, \"label_binary\": 0}\n\n    label_6 = PERTURBATION_TYPES_6CLASS[perturbation_type]\n    label_3 = CLASS_6_TO_3_MAPPING[label_6]\n    return {\"label_6class\": label_6, \"label_3class\": label_3, \"label_binary\": 1}\n\n\ndef _set_seed(seed: int) -> None:\n    import random\n    import numpy as np\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    if torch.cuda.is_available():\n        torch.cuda.manual_seed_all(seed)\n\n\ndef collect(args: argparse.Namespace) -> None:\n    _set_seed(args.seed)\n    device = args.device\n    output_dir = Path(args.output_dir)\n\n    log.info(\"Seed=%d, loading model from %s\", args.seed, args.checkpoint)\n    policy, model = load_pi0_for_collection(args.checkpoint, device)\n\n    collector = ActivationCollector(model)\n    collector.register_hooks()\n\n    perturbation_types: list[str]\n    if args.perturbation_type == \"all\":\n        perturbation_types = list(PERTURBATION_TYPES_6CLASS.keys())\n    else:\n        perturbation_types = [args.perturbation_type]\n\n    for ptype in perturbation_types:\n        is_nominal = ptype == \"nominal\"\n        log.info(\"Collecting %d episodes for %s\", args.num_episodes, ptype)\n\n        episodes = []\n        for ep_idx in range(args.num_episodes):\n            log.info(\"  Episode %d/%d\", ep_idx + 1, args.num_episodes)\n            try:\n                result = run_episode(\n                    policy, collector,\n                    perturbation_type=None if is_nominal else ptype,\n                    device=device,\n                    task_suite=args.task_suite,\n                    seed=args.seed + ep_idx,\n                )\n            except Exception:\n                log.exception(\"Episode %d failed, skipping\", ep_idx)\n                continue\n\n            labels = make_labels(ptype)\n            episode_data = {\n                \"activations\": result[\"activations\"],\n                **labels,\n                \"metadata\": {\n                    \"perturbation_type\": ptype,\n                    \"task_name\": result[\"task_name\"],\n                    \"num_steps\": result[\"num_steps\"],\n                    \"success\": result[\"success\"],\n                    \"episode_idx\": ep_idx,\n                },\n            }\n            episodes.append(episode_data)\n\n        save_episodes(episodes, ptype, output_dir)\n\n    collector.remove_hooks()\n    log.info(\"Collection complete.\")\n\n\ndef parse_args() -> argparse.Namespace:\n    p = argparse.ArgumentParser(\n        description=\"Collect π₀ activations from LIBERO-Plus rollouts\"\n    )\n    p.add_argument(\n        \"--checkpoint\", type=str, required=True,\n        help=\"Path to π₀ checkpoint directory (with .safetensors files)\",\n    )\n    p.add_argument(\n        \"--output_dir\", type=str, default=\"./activations\",\n        help=\"Directory to save activation .pt files\",\n    )\n    valid_types = list(PERTURBATION_TYPES_6CLASS.keys()) + [\"all\", \"nominal\"]\n    p.add_argument(\n        \"--perturbation_type\", type=str, default=\"all\",\n        choices=valid_types,\n        help=\"Perturbation type to collect, 'all' for all 6, or 'nominal'\",\n    )\n    p.add_argument(\n        \"--num_episodes\", type=int, default=50,\n        help=\"Number of episodes per perturbation type\",\n    )\n    p.add_argument(\n        \"--task_suite\", type=str, default=\"libero_spatial\",\n        choices=[\"libero_spatial\", \"libero_object\", \"libero_goal\", \"libero_10\", \"libero_90\"],\n        help=\"LIBERO-Plus suite (libero_90 has no perturbation variants)\",\n    )\n    p.add_argument(\n        \"--device\", type=str, default=\"cuda:0\",\n        help=\"Device for model inference\",\n    )\n    p.add_argument(\n        \"--seed\", type=int, default=42,\n        help=\"Global random seed for reproducibility\",\n    )\n    return p.parse_args()\n\n\nif __name__ == \"__main__\":\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    )\n    args = parse_args()\n    collect(args)\n",
      "numLines": 308,
      "startLine": 1,
      "totalLines": 308
    }
  }
}
```

</details>

---


### Assistant

_source line 176_

代码验证完毕。现在部署到远程并运行 _classify_task 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "014b9541-c69b-411d-9866-d8e60082b63f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YWXvcx4CFa4B9jSF1bCZK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9752,
      "cache_read_input_tokens": 108433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9752
      },
      "output_tokens": 1,
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

_source line 177_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Q13DsC3CoQnLksKeEW5p4U`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "cat > /root/meta_brain_lora_routing/phase0/libero_integration.py << 'ENDOFFILE'\n\"\"\"\nOpenPI/LIBERO-Plus integration for pi0 activation collection.\n\nBridges LIBERO-Plus simulation environments with the pi0 model, handling\nobservation preprocessing, action chunking, and perturbation-specific\ntask selection. Designed for direct model inference (no WebSocket server)\nso that ActivationCollector hooks fire during forward passes.\n\nInput:\n    LIBERO-Plus env observations: agentview_image [256,256,3],\n    robot0_eye_in_hand_image [256,256,3], robot0_eef_pos [3],\n    robot0_eef_quat [4], robot0_gripper_qpos [2], plus task language.\n\nOutput:\n    Per-episode activation dict (via ActivationCollector hooks on the\n    underlying PI0Pytorch model) and task metadata.\n\nIntegration with collect_activations.py:\n    from libero_integration import load_pi0_for_collection, run_episode\n\n    policy, model = load_pi0_for_collection(checkpoint_path, device)\n    collector = ActivationCollector(model)\n    collector.register_hooks()\n    result = run_episode(policy, collector, \"camera_viewpoints\", device)\n\"\"\"\n\nimport collections\nimport logging\nimport math\nimport re\nimport random\nfrom pathlib import Path\nfrom typing import Any\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\n\nlog = logging.getLogger(__name__)\n\n# ---------------------------------------------------------------------------\n# Constants (from OpenPI's examples/libero/main.py)\n# ---------------------------------------------------------------------------\n\nLIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]\nLIBERO_ENV_RESOLUTION = 256\nMODEL_INPUT_RESOLUTION = 224\nDEFAULT_REPLAN_STEPS = 5\nDEFAULT_NUM_STEPS_WAIT = 10\n\nMAX_STEPS = {\n    \"libero_spatial\": 220,\n    \"libero_object\": 280,\n    \"libero_goal\": 300,\n    \"libero_10\": 520,\n    \"libero_90\": 400,\n}\n\nVALID_PERTURBATION_TYPES = [\n    \"camera_viewpoints\",\n    \"light_conditions\",\n    \"background_textures\",\n    \"objects_layout\",\n    \"robot_initial_states\",\n    \"sensor_noise\",\n]\n\n\n# ---------------------------------------------------------------------------\n# Geometry helpers\n# ---------------------------------------------------------------------------\n\ndef _quat2axisangle(quat: np.ndarray) -> np.ndarray:\n    \"\"\"Quaternion [x,y,z,w] -> axis-angle [ax,ay,az].\"\"\"\n    q = np.asarray(quat, dtype=np.float64)\n    norm = np.linalg.norm(q)\n    if norm < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    q /= norm\n    sin_half = np.linalg.norm(q[:3])\n    if sin_half < 1e-8:\n        return np.zeros(3, dtype=np.float32)\n    angle = 2.0 * math.atan2(sin_half, q[3])\n    axis = q[:3] / sin_half\n    return (axis * angle).astype(np.float32)\n\n\n# ---------------------------------------------------------------------------\n# Image preprocessing\n# ---------------------------------------------------------------------------\n\ndef _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:\n    \"\"\"Resize image with aspect-preserving padding to (size, size, 3) uint8.\"\"\"\n    try:\n        from openpi_client.image_tools import resize_with_pad, convert_to_uint8\n        return convert_to_uint8(resize_with_pad(img, size, size))\n    except ImportError:\n        from PIL import Image as PILImage\n        h, w = img.shape[:2]\n        scale = min(size / h, size / w)\n        new_h, new_w = int(h * scale), int(w * scale)\n        resized = np.array(\n            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)\n        )\n        canvas = np.zeros((size, size, 3), dtype=np.uint8)\n        y0, x0 = (size - new_h) // 2, (size - new_w) // 2\n        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized\n        return canvas\n\n\n# ---------------------------------------------------------------------------\n# Observation -> model input\n# ---------------------------------------------------------------------------\n\ndef obs_to_model_input(\n    obs: dict,\n    task_description: str,\n    resize_size: int = MODEL_INPUT_RESOLUTION,\n) -> dict:\n    \"\"\"Convert LIBERO observation to the dict format expected by policy.infer().\n\n    LIBERO obs keys used:\n        agentview_image          [H, W, 3] uint8\n        robot0_eye_in_hand_image [H, W, 3] uint8\n        robot0_eef_pos           [3] float\n        robot0_eef_quat          [4] float (x,y,z,w)\n        robot0_gripper_qpos      [2] float\n\n    Returns dict with keys:\n        observation/image        [224, 224, 3] uint8\n        observation/wrist_image  [224, 224, 3] uint8\n        observation/state        [8] float32\n        prompt                   str\n\n    Note: sensor noise is applied by the LIBERO-Plus environment itself\n    (motion_blur, gaussian_blur, zoom_blur, fog, glass_blur at various\n    severity levels), not at the observation preprocessing stage.\n    \"\"\"\n    # Flip images 180 degrees (OpenPI training convention)\n    base_img = np.ascontiguousarray(obs[\"agentview_image\"][::-1, ::-1])\n    wrist_img = np.ascontiguousarray(obs[\"robot0_eye_in_hand_image\"][::-1, ::-1])\n\n    base_img = _resize_with_pad(base_img, resize_size)\n    wrist_img = _resize_with_pad(wrist_img, resize_size)\n\n    state = np.concatenate([\n        obs[\"robot0_eef_pos\"].astype(np.float32),\n        _quat2axisangle(obs[\"robot0_eef_quat\"]),\n        obs[\"robot0_gripper_qpos\"].astype(np.float32),\n    ])  # [8]\n\n    return {\n        \"observation/image\": base_img,\n        \"observation/wrist_image\": wrist_img,\n        \"observation/state\": state,\n        \"prompt\": task_description,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Model loading\n# ---------------------------------------------------------------------------\n\ndef _extract_model(policy: object) -> nn.Module:\n    \"\"\"Extract the underlying PI0Pytorch nn.Module from an OpenPI Policy.\"\"\"\n    for attr in (\"_model\", \"model\", \"_network\", \"network\"):\n        candidate = getattr(policy, attr, None)\n        if isinstance(candidate, nn.Module):\n            return candidate\n\n    for attr in dir(policy):\n        if attr.startswith(\"__\"):\n            continue\n        try:\n            candidate = getattr(policy, attr)\n            if isinstance(candidate, nn.Module):\n                log.warning(\n                    \"Found model at policy.%s (unexpected attribute name)\", attr\n                )\n                return candidate\n        except Exception:\n            continue\n\n    raise AttributeError(\n        \"Cannot find nn.Module in Policy object. \"\n        \"Inspect the OpenPI Policy class and update _extract_model().\"\n    )\n\n\ndef _ensure_openpi_imports():\n    \"\"\"Stub out lerobot (training-only dep) before importing OpenPI inference code.\"\"\"\n    import sys\n    import types\n    for mod in [\n        \"lerobot\", \"lerobot.common\", \"lerobot.common.datasets\",\n        \"lerobot.common.datasets.lerobot_dataset\",\n    ]:\n        if mod not in sys.modules:\n            sys.modules[mod] = types.ModuleType(mod)\n\n\ndef load_pi0_for_collection(\n    checkpoint_path: str,\n    device: str,\n    config_name: str = \"pi0_libero\",\n) -> tuple[object, nn.Module]:\n    \"\"\"Load pi0 via OpenPI's policy system for activation collection.\n\n    Uses create_trained_policy() so all transforms (LiberoInputs, Normalize,\n    TokenizePrompt, PadStatesAndActions, ResizeImages) and normalization\n    statistics are applied correctly.\n\n    Returns:\n        (policy, model) where\n        - policy: OpenPI Policy; call policy.infer(obs_dict)\n        - model:  PI0Pytorch nn.Module; pass to ActivationCollector\n    \"\"\"\n    _ensure_openpi_imports()\n\n    try:\n        from openpi.training import config as _config\n        from openpi.policies import policy_config\n    except ImportError:\n        raise ImportError(\n            \"openpi package required. \"\n            \"Clone https://github.com/Physical-Intelligence/openpi \"\n            \"and install with: pip install -e .\"\n        )\n\n    train_config = _config.get_config(config_name)\n    policy = policy_config.create_trained_policy(\n        train_config, checkpoint_path, pytorch_device=device\n    )\n\n    model = _extract_model(policy)\n    log.info(\"Loaded pi0 policy (config=%s) on %s\", config_name, device)\n    return policy, model\n\n\n# ---------------------------------------------------------------------------\n# LIBERO-Plus environment\n# ---------------------------------------------------------------------------\n\ndef _classify_task(task_name: str) -> str | None:\n    \"\"\"Classify a LIBERO-Plus task name into its perturbation type.\n\n    LIBERO-Plus task naming conventions:\n      Compound: {base}_[language_N_]view_{H}_{V}_{S}_{R}_{E}_initstate_{I}[_noise_{N}]\n        - camera_viewpoints:    (H,V,S,R,E) != (0,0,100,0,0), I==0, no noise\n        - robot_initial_states: default view, I != 0, no noise\n        - sensor_noise:         default view, I==0, N > 0\n        - base (nominal):       all defaults\n      Simple suffixes:\n        - light_conditions:     _light_\\\\d+\n        - background_textures:  _table_\\\\d+ or _tb_\\\\d+\n        - objects_layout:       _add_\\\\d+ or _level\\\\d+\n\n    Returns perturbation type string, or None for base/nominal tasks.\n    \"\"\"\n    if \"_view_\" in task_name:\n        m = re.search(\n            r\"_view_(-?\\d+)_(-?\\d+)_(\\d+)_(-?\\d+)_(-?\\d+)_initstate_(\\d+)(?:_noise_(\\d+))?\",\n            task_name,\n        )\n        if not m:\n            return None\n        H, V, S, R, E = int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])\n        initstate = int(m[6])\n        noise = int(m[7]) if m[7] else 0\n\n        if noise > 0:\n            return \"sensor_noise\"\n        if (H, V, S, R, E) != (0, 0, 100, 0, 0):\n            return \"camera_viewpoints\"\n        if initstate != 0:\n            return \"robot_initial_states\"\n        return None\n\n    if re.search(r\"_light_\\d+$\", task_name):\n        return \"light_conditions\"\n    if re.search(r\"_(?:table|tb)_\\d+$\", task_name):\n        return \"background_textures\"\n    if re.search(r\"_add_\\d+$\", task_name) or re.search(r\"_level\\d+\", task_name):\n        return \"objects_layout\"\n\n    return None\n\n\ndef _get_task_indices(\n    suite: object,\n    perturbation_type: str | None,\n    num_tasks: int,\n) -> list[int]:\n    \"\"\"Return task indices matching the requested perturbation type.\"\"\"\n    if perturbation_type is not None and perturbation_type not in VALID_PERTURBATION_TYPES:\n        raise ValueError(\n            f\"Unknown perturbation_type={perturbation_type!r}. \"\n            f\"Valid: {VALID_PERTURBATION_TYPES}\"\n        )\n\n    indices = []\n    matched_names = []\n    for i in range(num_tasks):\n        task = suite.get_task(i)\n        name = getattr(task, \"name\", \"\") or getattr(task, \"bddl_file\", \"\")\n        classified = _classify_task(name)\n\n        if perturbation_type is None:\n            if classified is None:\n                indices.append(i)\n                matched_names.append(name)\n        elif classified == perturbation_type:\n            indices.append(i)\n            matched_names.append(name)\n\n    if not indices:\n        raise RuntimeError(\n            f\"No tasks match perturbation_type={perturbation_type!r} \"\n            f\"among {num_tasks} tasks. Verify the suite contains \"\n            f\"LIBERO-Plus perturbation variants (not base libero_90).\"\n        )\n\n    log.info(\n        \"%s: matched %d/%d tasks (e.g. %s)\",\n        perturbation_type or \"nominal\",\n        len(indices),\n        num_tasks,\n        matched_names[:3],\n    )\n    return indices\n\n\ndef create_libero_env(\n    task_suite_name: str = \"libero_spatial\",\n    perturbation_type: str | None = None,\n    task_idx: int | None = None,\n    seed: int = 42,\n) -> tuple[Any, str, np.ndarray, int]:\n    \"\"\"Create a LIBERO / LIBERO-Plus evaluation environment.\n\n    Returns:\n        (env, task_description, init_states, selected_task_idx)\n    \"\"\"\n    from libero.libero import benchmark, get_libero_path\n    from libero.libero.envs import OffScreenRenderEnv\n\n    benchmark_dict = benchmark.get_benchmark_dict()\n    suite = benchmark_dict[task_suite_name]()\n    num_tasks = suite.n_tasks\n\n    valid_indices = _get_task_indices(suite, perturbation_type, num_tasks)\n\n    if task_idx is not None and task_idx in valid_indices:\n        selected_idx = task_idx\n    else:\n        selected_idx = random.choice(valid_indices)\n\n    task = suite.get_task(selected_idx)\n    task_description = task.language\n\n    task_bddl_file = (\n        Path(get_libero_path(\"bddl_files\")) / task.problem_folder / task.bddl_file\n    )\n    env = OffScreenRenderEnv(\n        bddl_file_name=str(task_bddl_file),\n        camera_heights=LIBERO_ENV_RESOLUTION,\n        camera_widths=LIBERO_ENV_RESOLUTION,\n    )\n    env.seed(seed)\n\n    init_states = suite.get_task_init_states(selected_idx)\n    return env, task_description, init_states, selected_idx\n\n\n# ---------------------------------------------------------------------------\n# Episode rollout\n# ---------------------------------------------------------------------------\n\ndef run_episode(\n    policy: object,\n    collector: object,\n    perturbation_type: str | None,\n    device: str,\n    task_suite: str = \"libero_spatial\",\n    seed: int = 42,\n    replan_steps: int = DEFAULT_REPLAN_STEPS,\n    num_steps_wait: int = DEFAULT_NUM_STEPS_WAIT,\n) -> dict[str, Any]:\n    \"\"\"Run one LIBERO-Plus episode, collecting activations at each replan point.\n\n    Every replan_steps env steps, the policy is queried for a new action chunk.\n    ActivationCollector hooks capture layer outputs during each policy.infer()\n    call. Activations are averaged across all replan points.\n\n    Sensor noise is applied by the LIBERO-Plus environment itself (via task\n    name suffix _noise_N), not at the observation level.\n\n    Returns dict with keys: activations, task_name, task_description,\n    num_steps, success.\n    \"\"\"\n    env, task_description, init_states, task_idx = create_libero_env(\n        task_suite_name=task_suite,\n        perturbation_type=perturbation_type,\n        seed=seed,\n    )\n\n    max_steps = MAX_STEPS.get(task_suite, 400)\n\n    step = 0\n    success = False\n\n    try:\n        trial_idx = random.randint(0, len(init_states) - 1)\n        obs = env.set_init_state(init_states[trial_idx])\n\n        for _ in range(num_steps_wait):\n            obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)\n\n        action_plan: collections.deque = collections.deque()\n        step_activations: list[dict] = []\n        done = False\n\n        while not done and step < max_steps:\n            if len(action_plan) == 0:\n                collector.clear()\n\n                obs_dict = obs_to_model_input(obs, task_description)\n                result = policy.infer(obs_dict)\n                action_chunk = result[\"actions\"]  # [horizon, 7]\n                action_plan.extend(action_chunk[:replan_steps])\n\n                pooled = collector.get_pooled()\n                if pooled:\n                    step_activations.append(pooled)\n\n            action = action_plan.popleft()\n            if isinstance(action, torch.Tensor):\n                action = action.cpu().numpy()\n            obs, reward, done, info = env.step(\n                action.tolist() if hasattr(action, \"tolist\") else list(action)\n            )\n            step += 1\n\n            if done or reward > 0:\n                success = info.get(\"success\", reward > 0)\n    finally:\n        env.close()\n\n    return {\n        \"activations\": _average_activations(step_activations),\n        \"task_name\": f\"{task_suite}/task_{task_idx}\",\n        \"task_description\": task_description,\n        \"num_steps\": step,\n        \"success\": success,\n    }\n\n\ndef _average_activations(\n    step_activations: list[dict[str, dict[str, torch.Tensor]]],\n) -> dict[str, dict[str, torch.Tensor]]:\n    \"\"\"Average activation tensors across replan steps.\"\"\"\n    if not step_activations:\n        return {}\n    result: dict[str, dict[str, torch.Tensor]] = {}\n    for layer in step_activations[0]:\n        result[layer] = {}\n        for strat in step_activations[0][layer]:\n            tensors = [sa[layer][strat] for sa in step_activations]\n            result[layer][strat] = torch.stack(tensors).mean(dim=0)\n    return result\nENDOFFILE\necho \"libero_integration.py deployed\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "bcf9702d-7e58-4851-b02b-17ee04d4cedd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YWXvcx4CFa4B9jSF1bCZK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9752,
      "cache_read_input_tokens": 108433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9752
      },
      "output_tokens": 1,
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

_source line 178 · 2026-05-15T12:02:50.652Z_

<details><summary>↩ Tool result · `toolu_01Q13DsC3CoQnLksKeEW5p4U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"libero_integration.py deployed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "c4c2b9f0-b1e2-4fa5-a072-b2d467dcc867",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"libero_integration.py deployed\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"libero_integration.py deployed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 179_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01AP18eZ32VoSDYkBBFCnUuD`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "cat > /root/meta_brain_lora_routing/phase0/collect_activations.py << 'ENDOFFILE'\n\"\"\"\nCollect frozen π₀ activations from LIBERO-Plus rollouts.\n\nRegisters forward hooks on PaliGemma LLM layers and Action Expert layers,\nruns episodes under each perturbation type (or nominal), and saves per-layer\nactivations with 4 pooling strategies in fp16.\n\nUsage:\n    # Collect camera perturbation episodes\n    python collect_activations.py \\\n        --checkpoint /path/to/pi0_base \\\n        --output_dir ./activations \\\n        --perturbation_type camera_viewpoints \\\n        --num_episodes 50 \\\n        --device cuda:0\n\n    # Collect all perturbation types\n    python collect_activations.py \\\n        --checkpoint /path/to/pi0_base \\\n        --output_dir ./activations \\\n        --perturbation_type all \\\n        --num_episodes 50\n\n    # Collect nominal (no perturbation) baseline\n    python collect_activations.py \\\n        --checkpoint /path/to/pi0_base \\\n        --output_dir ./activations \\\n        --perturbation_type nominal \\\n        --num_episodes 100\n\nDependencies:\n    torch, safetensors, openpi (for model loading), libero\n\"\"\"\n\nimport argparse\nimport logging\nimport os\nfrom pathlib import Path\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\n\nfrom configs import (\n    CLASS_6_TO_3_MAPPING,\n    EXPERT_LAYER_TEMPLATE,\n    EXPERT_LAYERS,\n    PALIGEMMA_LAYER_TEMPLATE,\n    PALIGEMMA_LAYERS,\n    PERTURBATION_TYPES_6CLASS,\n    POOLING_STRATEGIES,\n)\nfrom libero_integration import (\n    load_pi0_for_collection,\n    obs_to_model_input,\n    run_episode,\n)\n\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Pooling helpers\n# ---------------------------------------------------------------------------\n\ndef pool_activation(hidden_states: torch.Tensor, strategy: str) -> torch.Tensor:\n    \"\"\"Pool a (batch, seq_len, hidden_dim) tensor into (batch, D).\n\n    Strategies:\n        mean       — mean over seq_len → (batch, hidden_dim)\n        first      — first token       → (batch, hidden_dim)\n        last       — last token        → (batch, hidden_dim)\n        first_last — concat first+last → (batch, hidden_dim*2)\n    \"\"\"\n    if strategy == \"mean\":\n        return hidden_states.mean(dim=1)\n    elif strategy == \"first\":\n        return hidden_states[:, 0]\n    elif strategy == \"last\":\n        return hidden_states[:, -1]\n    elif strategy == \"first_last\":\n        return torch.cat([hidden_states[:, 0], hidden_states[:, -1]], dim=-1)\n    raise ValueError(f\"Unknown pooling strategy: {strategy}\")\n\n\n# ---------------------------------------------------------------------------\n# Hook manager\n# ---------------------------------------------------------------------------\n\nclass ActivationCollector:\n    \"\"\"Registers hooks on specified layers and stores pooled activations.\"\"\"\n\n    def __init__(self, model: nn.Module):\n        self.model = model\n        self._hooks: list[torch.utils.hooks.RemovableHook] = []\n        self._raw: dict[str, torch.Tensor] = {}  # layer_name -> last hidden_states\n\n    def register_hooks(self) -> None:\n        for i in PALIGEMMA_LAYERS:\n            name = f\"paligemma_layer_{i}\"\n            module_path = PALIGEMMA_LAYER_TEMPLATE.format(i=i)\n            module = _get_submodule(self.model, module_path)\n            self._hooks.append(\n                module.register_forward_hook(self._make_hook(name))\n            )\n            log.info(\"Hooked %s -> %s\", name, module_path)\n\n        for i in EXPERT_LAYERS:\n            name = f\"expert_layer_{i}\"\n            module_path = EXPERT_LAYER_TEMPLATE.format(i=i)\n            module = _get_submodule(self.model, module_path)\n            self._hooks.append(\n                module.register_forward_hook(self._make_hook(name))\n            )\n            log.info(\"Hooked %s -> %s\", name, module_path)\n\n    def _make_hook(self, name: str):\n        def hook_fn(_module, _input, output):\n            # Gemma layers return (hidden_states, ...) or just hidden_states\n            if isinstance(output, tuple):\n                h = output[0]\n            else:\n                h = output\n            self._raw[name] = h.detach()\n        return hook_fn\n\n    def get_pooled(self) -> dict[str, dict[str, torch.Tensor]]:\n        \"\"\"Return {layer_name: {pooling_strategy: tensor(fp16)}} from last forward.\"\"\"\n        result = {}\n        for name, h in self._raw.items():\n            result[name] = {}\n            for strat in POOLING_STRATEGIES:\n                pooled = pool_activation(h, strat)\n                result[name][strat] = pooled.half().cpu()\n        return result\n\n    def clear(self) -> None:\n        self._raw.clear()\n\n    def remove_hooks(self) -> None:\n        for h in self._hooks:\n            h.remove()\n        self._hooks.clear()\n\n\ndef _get_submodule(model: nn.Module, path: str) -> nn.Module:\n    parts = path.split(\".\")\n    m = model\n    for p in parts:\n        if p.isdigit():\n            m = m[int(p)]\n        else:\n            m = getattr(m, p)\n    return m\n\n\n# load_pi0_model, rollout_episode, _obs_to_model_input replaced by\n# load_pi0_for_collection, run_episode, obs_to_model_input from libero_integration\n\n\n# ---------------------------------------------------------------------------\n# Data saving\n# ---------------------------------------------------------------------------\n\ndef save_episodes(\n    episodes: list[dict[str, Any]],\n    perturbation_type: str,\n    output_dir: Path,\n) -> None:\n    output_dir.mkdir(parents=True, exist_ok=True)\n    out_path = output_dir / f\"{perturbation_type}.pt\"\n\n    # Support incremental collection: append to existing file\n    if out_path.exists():\n        existing = torch.load(out_path, weights_only=False)\n        log.info(\"Appending %d episodes to existing %d in %s\",\n                 len(episodes), len(existing), out_path)\n        episodes = existing + episodes\n\n    torch.save(episodes, out_path)\n    log.info(\"Saved %d episodes to %s\", len(episodes), out_path)\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef make_labels(perturbation_type: str) -> dict[str, int]:\n    if perturbation_type == \"nominal\":\n        return {\"label_6class\": -1, \"label_3class\": -1, \"label_binary\": 0}\n\n    label_6 = PERTURBATION_TYPES_6CLASS[perturbation_type]\n    label_3 = CLASS_6_TO_3_MAPPING[label_6]\n    return {\"label_6class\": label_6, \"label_3class\": label_3, \"label_binary\": 1}\n\n\ndef _set_seed(seed: int) -> None:\n    import random\n    import numpy as np\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    if torch.cuda.is_available():\n        torch.cuda.manual_seed_all(seed)\n\n\ndef collect(args: argparse.Namespace) -> None:\n    _set_seed(args.seed)\n    device = args.device\n    output_dir = Path(args.output_dir)\n\n    log.info(\"Seed=%d, loading model from %s\", args.seed, args.checkpoint)\n    policy, model = load_pi0_for_collection(args.checkpoint, device)\n\n    collector = ActivationCollector(model)\n    collector.register_hooks()\n\n    perturbation_types: list[str]\n    if args.perturbation_type == \"all\":\n        perturbation_types = list(PERTURBATION_TYPES_6CLASS.keys())\n    else:\n        perturbation_types = [args.perturbation_type]\n\n    for ptype in perturbation_types:\n        is_nominal = ptype == \"nominal\"\n        log.info(\"Collecting %d episodes for %s\", args.num_episodes, ptype)\n\n        episodes = []\n        for ep_idx in range(args.num_episodes):\n            log.info(\"  Episode %d/%d\", ep_idx + 1, args.num_episodes)\n            try:\n                result = run_episode(\n                    policy, collector,\n                    perturbation_type=None if is_nominal else ptype,\n                    device=device,\n                    task_suite=args.task_suite,\n                    seed=args.seed + ep_idx,\n                )\n            except Exception:\n                log.exception(\"Episode %d failed, skipping\", ep_idx)\n                continue\n\n            labels = make_labels(ptype)\n            episode_data = {\n                \"activations\": result[\"activations\"],\n                **labels,\n                \"metadata\": {\n                    \"perturbation_type\": ptype,\n                    \"task_name\": result[\"task_name\"],\n                    \"num_steps\": result[\"num_steps\"],\n                    \"success\": result[\"success\"],\n                    \"episode_idx\": ep_idx,\n                },\n            }\n            episodes.append(episode_data)\n\n        save_episodes(episodes, ptype, output_dir)\n\n    collector.remove_hooks()\n    log.info(\"Collection complete.\")\n\n\ndef parse_args() -> argparse.Namespace:\n    p = argparse.ArgumentParser(\n        description=\"Collect π₀ activations from LIBERO-Plus rollouts\"\n    )\n    p.add_argument(\n        \"--checkpoint\", type=str, required=True,\n        help=\"Path to π₀ checkpoint directory (with .safetensors files)\",\n    )\n    p.add_argument(\n        \"--output_dir\", type=str, default=\"./activations\",\n        help=\"Directory to save activation .pt files\",\n    )\n    valid_types = list(PERTURBATION_TYPES_6CLASS.keys()) + [\"all\", \"nominal\"]\n    p.add_argument(\n        \"--perturbation_type\", type=str, default=\"all\",\n        choices=valid_types,\n        help=\"Perturbation type to collect, 'all' for all 6, or 'nominal'\",\n    )\n    p.add_argument(\n        \"--num_episodes\", type=int, default=50,\n        help=\"Number of episodes per perturbation type\",\n    )\n    p.add_argument(\n        \"--task_suite\", type=str, default=\"libero_spatial\",\n        choices=[\"libero_spatial\", \"libero_object\", \"libero_goal\", \"libero_10\", \"libero_90\"],\n        help=\"LIBERO-Plus suite (libero_90 has no perturbation variants)\",\n    )\n    p.add_argument(\n        \"--device\", type=str, default=\"cuda:0\",\n        help=\"Device for model inference\",\n    )\n    p.add_argument(\n        \"--seed\", type=int, default=42,\n        help=\"Global random seed for reproducibility\",\n    )\n    return p.parse_args()\n\n\nif __name__ == \"__main__\":\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    )\n    args = parse_args()\n    collect(args)\nENDOFFILE\necho \"collect_activations.py deployed\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "946a755f-d368-40b7-a9a7-3e4708a2494d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YWXvcx4CFa4B9jSF1bCZK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9752,
      "cache_read_input_tokens": 108433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9752
      },
      "output_tokens": 1,
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

_source line 180 · 2026-05-15T12:03:29.658Z_

<details><summary>↩ Tool result · `toolu_01AP18eZ32VoSDYkBBFCnUuD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"collect_activations.py deployed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "ca4b1820-af6e-4c43-8bb3-9ec6af67135c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"collect_activations.py deployed\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"collect_activations.py deployed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 181_

两文件已部署。现在并行执行：_classify_task 验证 + 语法检查 + 模型加载验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "1926af77-c5ec-45c6-873f-736c859f2059",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4RCCCJ1utNPv7w3Zmw5yu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8232,
      "cache_read_input_tokens": 118185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8232
      },
      "output_tokens": 1,
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

_source line 182_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JzE9xczszpGvzPa1dkNbT5`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport importlib.util, collections, re\n\n# Load task map directly\nspec = importlib.util.spec_from_file_location('task_map', '/root/LIBERO-plus/libero/libero/benchmark/libero_suite_task_map.py')\nmod = importlib.util.module_from_spec(spec)\nspec.loader.exec_module(mod)\nlibero_task_map = mod.libero_task_map\n\n# Import our classifier\nimport sys; sys.path.insert(0, '/root/meta_brain_lora_routing/phase0')\nfrom libero_integration import _classify_task\n\nfor suite_name in ['libero_spatial', 'libero_object', 'libero_goal', 'libero_10']:\n    tasks = libero_task_map[suite_name]\n    counts = collections.Counter()\n    examples = collections.defaultdict(list)\n    for t in tasks:\n        cls = _classify_task(t)\n        label = cls or 'nominal'\n        counts[label] += 1\n        if len(examples[label]) < 1:\n            examples[label].append(t[-60:])\n    print(f'=== {suite_name} ({len(tasks)} tasks) ===')\n    total_classified = 0\n    for label in ['nominal', 'camera_viewpoints', 'robot_initial_states', 'sensor_noise', 'light_conditions', 'background_textures', 'objects_layout']:\n        c = counts.get(label, 0)\n        total_classified += c\n        ex = examples.get(label, [''])[0]\n        print(f'  {label:25s}: {c:4d}  e.g. ...{ex}')\n    print(f'  TOTAL: {total_classified} / {len(tasks)}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "c53fda2b-ded0-4d41-a396-292ba50e9c23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4RCCCJ1utNPv7w3Zmw5yu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8232,
      "cache_read_input_tokens": 118185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8232
      },
      "output_tokens": 1,
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

_source line 183_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01XuRESu4HnM1sgXvWmH5F9D`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing/phase0 && python3 -m py_compile libero_integration.py && echo \"libero_integration.py OK\" && python3 -m py_compile collect_activations.py && echo \"collect_activations.py OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "d47c2bb7-0760-4031-a19d-3ad91d72ce02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4RCCCJ1utNPv7w3Zmw5yu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8232,
      "cache_read_input_tokens": 118185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8232
      },
      "output_tokens": 1,
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

_source line 184 · 2026-05-15T12:03:53.789Z_

<details><summary>↩ Tool result · `toolu_01JzE9xczszpGvzPa1dkNbT5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== libero_spatial (2402 tasks) ===\\n  nominal                  :  390  e.g. ...lace_it_on_the_plate_language_1_view_0_0_100_0_0_initstate_0\\n  camera_viewpoints        :  376  e.g. ...kin_and_place_it_on_the_plate_view_0_0_100_2_352_initstate_0\\n  robot_initial_states     :  350  e.g. ...mekin_and_place_it_on_the_plate_view_0_0_100_0_0_initstate_1\\n  sensor_noise             :  351  e.g. ...d_place_it_on_the_plate_view_0_0_100_0_0_initstate_0_noise_3\\n  light_conditions         :  292  e.g. ..._the_plate_and_the_ramekin_and_place_it_on_the_plate_light_1\\n  background_textures      :  258  e.g. ..._the_plate_and_the_ramekin_and_place_it_on_the_plate_table_1\\n  objects_layout           :  385  e.g. ...n_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10\\n  TOTAL: 2402 / 2402\\n=== libero_object (2518 tasks) ===\\n  nominal                  :  354  e.g. ...ace_it_in_the_basket_language_2_view_0_0_100_0_0_initstate_0\\n  camera_viewpoints        :  396  e.g. ...soup_and_place_it_in_the_basket_view_0_0_100_2_4_initstate_0\\n  robot_initial_states     :  398  e.g. ...oup_and_place_it_in_the_basket_view_0_0_100_0_0_initstate_11\\n  sensor_noise             :  422  e.g. ..._place_it_in_the_basket_view_0_0_100_0_0_initstate_0_noise_2\\n  light_conditions         :  297  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_light_1\\n  background_textures      :  248  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_table_1\\n  objects_layout           :  403  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_add_10\\n  TOTAL: 2518 / 2518\\n=== libero_goal (2591 tasks) ===\\n  nominal                  :  410  e.g. ...rawer_of_the_cabinet_language_1_view_0_0_100_0_0_initstate_0\\n  camera_viewpoints        :  408  e.g. ...he_middle_drawer_of_the_cabinet_view_0_0_100_2_4_initstate_0\\n  robot_initial_states     :  409  e.g. ...he_middle_drawer_of_the_cabinet_view_0_0_100_0_0_initstate_1\\n  sensor_noise             :  379  e.g. ...e_drawer_of_the_cabinet_view_0_0_100_0_0_initstate_0_noise_1\\n  light_conditions         :  279  e.g. ...open_the_middle_drawer_of_the_cabinet_light_1\\n  background_textures      :  281  e.g. ...open_the_middle_drawer_of_the_cabinet_table_1\\n  objects_layout           :  425  e.g. ...open_the_middle_drawer_of_the_cabinet_add_10\\n  TOTAL: 2591 / 2591\\n=== libero_10 (2519 tasks) ===\\n  nominal                  :  383  e.g. ..._sauce_in_the_basket_language_1_view_0_0_100_0_0_initstate_0\\n  camera_viewpoints        :  419  e.g. ..._the_tomato_sauce_in_the_basket_view_0_0_100_2_6_initstate_0\\n  robot_initial_states     :  393  e.g. ..._the_tomato_sauce_in_the_basket_view_0_0_100_0_0_initstate_1\\n  sensor_noise             :  449  e.g. ...ato_sauce_in_the_basket_view_0_0_100_0_0_initstate_0_noise_1\\n  light_conditions         :  274  e.g. ..._SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_light_1\\n  background_textures      :  289  e.g. ..._SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_table_1\\n  objects_layout           :  312  e.g. ...N_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_14\\n  TOTAL: 2519 / 2519\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.83}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "0a56fff8-16d0-4a75-bf09-214b9baf4c79",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== libero_spatial (2402 tasks) ===\\\\n  nominal                  :  390  e.g. ...lace_it_on_the_plate_language_1_view_0_0_100_0_0_initstate_0\\\\n  camera_viewpoints        :  376  e.g. ...kin_and_place_it_on_the_plate_view_0_0_100_2_352_initstate_0\\\\n  robot_initial_states     :  350  e.g. ...mekin_and_place_it_on_the_plate_view_0_0_100_0_0_initstate_1\\\\n  sensor_noise             :  351  e.g. ...d_place_it_on_the_plate_view_0_0_100_0_0_initstate_0_noise_3\\\\n  light_conditions         :  292  e.g. ..._the_plate_and_the_ramekin_and_place_it_on_the_plate_light_1\\\\n  background_textures      :  258  e.g. ..._the_plate_and_the_ramekin_and_place_it_on_the_plate_table_1\\\\n  objects_layout           :  385  e.g. ...n_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10\\\\n  TOTAL: 2402 / 2402\\\\n=== libero_object (2518 tasks) ===\\\\n  nominal                  :  354  e.g. ...ace_it_in_the_basket_language_2_view_0_0_100_0_0_initstate_0\\\\n  camera_viewpoints        :  396  e.g. ...soup_and_place_it_in_the_basket_view_0_0_100_2_4_initstate_0\\\\n  robot_initial_states     :  398  e.g. ...oup_and_place_it_in_the_basket_view_0_0_100_0_0_initstate_11\\\\n  sensor_noise             :  422  e.g. ..._place_it_in_the_basket_view_0_0_100_0_0_initstate_0_noise_2\\\\n  light_conditions         :  297  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_light_1\\\\n  background_textures      :  248  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_table_1\\\\n  objects_layout           :  403  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_add_10\\\\n  TOTAL: 2518 / 2518\\\\n=== libero_goal (2591 tasks) ===\\\\n  nominal                  :  410  e.g. ...rawer_of_the_cabinet_language_1_view_0_0_100_0_0_initstate_0\\\\n  camera_viewpoints        :  408  e.g. ...he_middle_drawer_of_the_cabinet_view_0_0_100_2_4_initstate_0\\\\n  robot_initial_states     :  409  e.g. ...he_middle_drawer_of_the_cabinet_view_0_0_100_0_0_initstate_1\\\\n  sensor_noise             :  379  e.g. ...e_drawer_of_the_cabinet_view_0_0_100_0_0_initstate_0_noise_1\\\\n  light_conditions         :  279  e.g. ...open_the_middle_drawer_of_the_cabinet_light_1\\\\n  background_textures      :  281  e.g. ...open_the_middle_drawer_of_the_cabinet_table_1\\\\n  objects_layout           :  425  e.g. ...open_the_middle_drawer_of_the_cabinet_add_10\\\\n  TOTAL: 2591 / 2591\\\\n=== libero_10 (2519 tasks) ===\\\\n  nominal                  :  383  e.g. ..._sauce_in_the_basket_language_1_view_0_0_100_0_0_initstate_0\\\\n  camera_viewpoints        :  419  e.g. ..._the_tomato_sauce_in_the_basket_view_0_0_100_2_6_initstate_0\\\\n  robot_initial_states     :  393  e.g. ..._the_tomato_sauce_in_the_basket_view_0_0_100_0_0_initstate_1\\\\n  sensor_noise             :  449  e.g. ...ato_sauce_in_the_basket_view_0_0_100_0_0_initstate_0_noise_1\\\\n  light_conditions         :  274  e.g. ..._SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_light_1\\\\n  background_textures      :  289  e.g. ..._SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_table_1\\\\n  objects_layout           :  312  e.g. ...N_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_14\\\\n  TOTAL: 2519 / 2519\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.83}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== libero_spatial (2402 tasks) ===\\n  nominal                  :  390  e.g. ...lace_it_on_the_plate_language_1_view_0_0_100_0_0_initstate_0\\n  camera_viewpoints        :  376  e.g. ...kin_and_place_it_on_the_plate_view_0_0_100_2_352_initstate_0\\n  robot_initial_states     :  350  e.g. ...mekin_and_place_it_on_the_plate_view_0_0_100_0_0_initstate_1\\n  sensor_noise             :  351  e.g. ...d_place_it_on_the_plate_view_0_0_100_0_0_initstate_0_noise_3\\n  light_conditions         :  292  e.g. ..._the_plate_and_the_ramekin_and_place_it_on_the_plate_light_1\\n  background_textures      :  258  e.g. ..._the_plate_and_the_ramekin_and_place_it_on_the_plate_table_1\\n  objects_layout           :  385  e.g. ...n_the_plate_and_the_ramekin_and_place_it_on_the_plate_add_10\\n  TOTAL: 2402 / 2402\\n=== libero_object (2518 tasks) ===\\n  nominal                  :  354  e.g. ...ace_it_in_the_basket_language_2_view_0_0_100_0_0_initstate_0\\n  camera_viewpoints        :  396  e.g. ...soup_and_place_it_in_the_basket_view_0_0_100_2_4_initstate_0\\n  robot_initial_states     :  398  e.g. ...oup_and_place_it_in_the_basket_view_0_0_100_0_0_initstate_11\\n  sensor_noise             :  422  e.g. ..._place_it_in_the_basket_view_0_0_100_0_0_initstate_0_noise_2\\n  light_conditions         :  297  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_light_1\\n  background_textures      :  248  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_table_1\\n  objects_layout           :  403  e.g. ...pick_up_the_alphabet_soup_and_place_it_in_the_basket_add_10\\n  TOTAL: 2518 / 2518\\n=== libero_goal (2591 tasks) ===\\n  nominal                  :  410  e.g. ...rawer_of_the_cabinet_language_1_view_0_0_100_0_0_initstate_0\\n  camera_viewpoints        :  408  e.g. ...he_middle_drawer_of_the_cabinet_view_0_0_100_2_4_initstate_0\\n  robot_initial_states     :  409  e.g. ...he_middle_drawer_of_the_cabinet_view_0_0_100_0_0_initstate_1\\n  sensor_noise             :  379  e.g. ...e_drawer_of_the_cabinet_view_0_0_100_0_0_initstate_0_noise_1\\n  light_conditions         :  279  e.g. ...open_the_middle_drawer_of_the_cabinet_light_1\\n  background_textures      :  281  e.g. ...open_the_middle_drawer_of_the_cabinet_table_1\\n  objects_layout           :  425  e.g. ...open_the_middle_drawer_of_the_cabinet_add_10\\n  TOTAL: 2591 / 2591\\n=== libero_10 (2519 tasks) ===\\n  nominal                  :  383  e.g. ..._sauce_in_the_basket_language_1_view_0_0_100_0_0_initstate_0\\n  camera_viewpoints        :  419  e.g. ..._the_tomato_sauce_in_the_basket_view_0_0_100_2_6_initstate_0\\n  robot_initial_states     :  393  e.g. ..._the_tomato_sauce_in_the_basket_view_0_0_100_0_0_initstate_1\\n  sensor_noise             :  449  e.g. ...ato_sauce_in_the_basket_view_0_0_100_0_0_initstate_0_noise_1\\n  light_conditions         :  274  e.g. ..._SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_light_1\\n  background_textures      :  289  e.g. ..._SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_table_1\\n  objects_layout           :  312  e.g. ...N_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it_add_14\\n  TOTAL: 2519 / 2519\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.83}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-15T12:03:54.447Z_

<details><summary>↩ Tool result · `toolu_01XuRESu4HnM1sgXvWmH5F9D`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"libero_integration.py OK\\ncollect_activations.py OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "c295216a-f17a-4ae4-abdd-bc8bd0e33c82",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"libero_integration.py OK\\\\ncollect_activations.py OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.65}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"libero_integration.py OK\\ncollect_activations.py OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 186_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_011tfJPmKkbhgZFKXk2qB1us`</summary>

```json
{
  "server": "westd-34142",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/meta_brain_lora_routing/phase0 && python3 -c \"\nimport sys, types\nfor mod in ['lerobot', 'lerobot.common', 'lerobot.common.datasets', 'lerobot.common.datasets.lerobot_dataset']:\n    if mod not in sys.modules:\n        sys.modules[mod] = types.ModuleType(mod)\nfrom libero_integration import load_pi0_for_collection, run_episode, obs_to_model_input\nprint('Import OK')\nprint('load_pi0_for_collection:', load_pi0_for_collection)\nprint('run_episode:', run_episode)\nprint('obs_to_model_input:', obs_to_model_input)\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "3dc24730-04ee-484a-864e-1fe113ccec5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4RCCCJ1utNPv7w3Zmw5yu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8232,
      "cache_read_input_tokens": 118185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8232
      },
      "output_tokens": 1,
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

_source line 187 · 2026-05-15T12:03:58.596Z_

<details><summary>↩ Tool result · `toolu_011tfJPmKkbhgZFKXk2qB1us`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Import OK\\nload_pi0_for_collection: &lt;function load_pi0_for_collection at 0x7fea47e44360>\\nrun_episode: &lt;function run_episode at 0x7fea47cd0180>\\nobs_to_model_input: &lt;function obs_to_model_input at 0x7fea47cc6d40>\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "2a8db8d2-6b54-480b-ac7d-8454828581e0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Import OK\\\\nload_pi0_for_collection: &lt;function load_pi0_for_collection at 0x7fea47e44360>\\\\nrun_episode: &lt;function run_episode at 0x7fea47cd0180>\\\\nobs_to_model_input: &lt;function obs_to_model_input at 0x7fea47cc6d40>\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Import OK\\nload_pi0_for_collection: &lt;function load_pi0_for_collection at 0x7fea47e44360>\\nrun_episode: &lt;function run_episode at 0x7fea47cd0180>\\nobs_to_model_input: &lt;function obs_to_model_input at 0x7fea47cc6d40>\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 188_

<details><summary>Logged reasoning block</summary>

```text
All three verifications passed:

1. **_classify_task validation**: ALL tasks across ALL suites are correctly classified — TOTAL matches exactly:
   - libero_spatial: 2402/2402 ✓
   - libero_object: 2518/2518 ✓
   - libero_goal: 2591/2591 ✓
   - libero_10: 2519/2519 ✓

2. **Syntax check**: Both files compile successfully ✓

3. **Import check**: All functions import correctly ✓

Now let me check the sensor_noise implementation in LIBERO-Plus more carefully and verify the OpenPI model loading.


Looking at the env_wrapper.py, I see the noise types are actually applied at the environment level during the step method — noise 1-10 applies motion blur, 11-20 applies gaussian blur, 21-30 applies zoom blur, 31-40 applies fog, and 41-50 applies glass blur. So when a task with a `_noise_N` suffix is selected, the environment automatically applies these effects to observations. My `_apply_sensor_noise()` implementation was incorrect since it was just adding simple Gaussian noise and brightness adjustments instead of these five specific blur and fog effects.

I've already verified that the OpenPI model imports work at the module level, though actually loading a checkpoint would require having the file available. The import chain and config retrieval are functional though.

Now I'm noticing a discrepancy in the noise counts — the spatial category shows 351 for sensor_noise which matches what `_classify_task` returns, but when I look at the background_textures count, the previous analysis showed 346 total (251 TABLE + 95 TB) while `_classify_task` gives 258. That's a significant difference and I need to figure out what's causing it.

Looking at the classification logic more carefully, the issue is that my `_classify_task` function checks for `_view_` patterns first, which means tasks containing both `_table_` in the description and a view suffix won't be counted as table tasks. The previous script used a simpler substring check that would match `_table_` anywhere, including in descriptions like `from_table_center`, whereas my regex-based approach with the suffix pattern `_(?:table|tb)_\d+$` is more restrictive and only catches the actual perturbation suffix. I'm noticing a discrepancy between my previous counts and what `_classify_task` is producing for libero_spatial. The old analysis showed TABLE at 251 and TB at 95 (totaling 346), but my new classification is only getting 258 for background_textures combined. The light_conditions and objects_layout counts are also shifting—292 vs 242 for lights, and 385 vs 347 for object layout—so something in my regex matching logic isn't aligning with the original categorization. These don't match. Let me think about why...

Actually, I think I see the issue. The previous analysis used separate categories TABLE=251 and TB=95, total = 346. But _classify_task gives background_textures=258. That's 346 vs 258 — difference of 88.

Meanwhile, light_conditions was 242 before, now 292 — difference of +50.
objects_layout was 347 before, now 385 — difference of +38.

And the nominal count: BASE_VIEW was 390 before, now 390 — same!
VIEW was 376, now 376 — same!
INIT was 350, now 350 — same!
NOISE was 351, now 351 — same!

So the difference is only in the simple-suffix categories (light/table/tb/add/level). This suggests some tasks are being reclassified between these categories.

I think the problem is that the previous script checked categories in order — `_view_` first, then `_table_`, then `_tb_`, then `_light_`, then `_add_`/`_level` — so a task like `pick_up_the_black_bowl_from_table_center_...` with `_table_` in the description would get counted as TABLE even if the actual perturbation suffix was `_light_`. My _classify_task uses regex anchored to the end of the string, which correctly identifies the actual suffix instead of matching partial words in the task description. The totals match across both classification approaches at 2402 tasks, confirming the regex-based method is working correctly by avoiding false positives from intermediate `_table_` patterns in task names. Now I'm ready to put together the final report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "58501063-d33a-425b-b02f-20ff07d6aac4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCxFn4TCpQKuKW3tkZg3Aw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2858,
      "cache_read_input_tokens": 126417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2858
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

_source line 189_

全部验证通过。汇总结果：

---

## 产出报告

### 1. PERTURBATION_SUFFIXES 匹配报告

旧的简单后缀匹配已替换为 **正则解析**（`_classify_task()`），100% 覆盖所有 4 个 LIBERO-Plus 套件：

| 扰动类型 | libero_spatial | libero_object | libero_goal | libero_10 |
|---|---|---|---|---|
| **nominal** (base) | 390 | 354 | 410 | 383 |
| **camera_viewpoints** | 376 | 396 | 408 | 419 |
| **robot_initial_states** | 350 | 398 | 409 | 393 |
| **sensor_noise** | 351 | 422 | 379 | 449 |
| **light_conditions** | 292 | 297 | 279 | 274 |
| **background_textures** | 258 | 248 | 281 | 289 |
| **objects_layout** | 385 | 403 | 425 | 312 |
| **TOTAL** | **2402/2402** | **2518/2518** | **2591/2591** | **2519/2519** |

命名格式解析：
- 复合后缀：`{base}_view_{H}_{V}_{S}_{R}_{E}_initstate_{I}[_noise_{N}]` → 通过参数值判断类型
- 简单后缀：`_light_\d+`, `_table_\d+`/`_tb_\d+`, `_add_\d+`/`_level\d+` → 末尾正则匹配

### 2. sensor_noise 实现确认

**LIBERO-Plus 内置**，非自实现。已删除 `_apply_sensor_noise()`。

环境层应用（`env_wrapper.py` L288-342），5 种噪声 × 10 级 severity = 50 级别：
| noise 值 | 类型 | 参数 |
|---|---|---|
| 1-10 | motion_blur | radius/sigma 递增 |
| 11-20 | gaussian_blur | sigma 1-10 |
| 21-30 | zoom_blur | zoom range 递增 |
| 31-40 | fog | plasma fractal |
| 41-50 | glass_blur | sigma/delta/iter |

通过任务名后缀 `_noise_N` 选择，env.step() 自动对 agentview 和 wrist 图像施加噪声。

### 3. 模型加载修复

原始报错 `openpi.models_pytorch.model_config.get_model_config` 不存在 — 因为该 API 根本不存在。正确 API：
```python
from openpi.training.config import get_config         # config_name="pi0_libero"
from openpi.policies.policy_config import create_trained_policy
```

已修复：
- `load_pi0_for_collection()` 使用正确的 API 路径（本就正确）
- 添加 `_ensure_openpi_imports()` stub 掉 lerobot（训练依赖，推理不需要）
- 安装缺失依赖：augmax, chex, tqdm-loggable, openpi-client, lerobot 等
- 升级 orbax-checkpoint 到 0.11.39（兼容 jax 0.10.0）
- OpenPI config 获取验证通过：`get_config("pi0_libero")` → OK

### 4. 代码部署状态

| 文件 | 远程路径 | 语法 | 导入 |
|---|---|---|---|
| libero_integration.py | `/root/meta_brain_lora_routing/phase0/` | ✓ | ✓ |
| collect_activations.py | `/root/meta_brain_lora_routing/phase0/` | ✓ | ✓ |

关键变更：
- 删除 `PERTURBATION_SUFFIXES` → 替换为 `_classify_task()` 正则解析
- 删除 `_apply_sensor_noise()` → env 内置
- `obs_to_model_input()` 移除 `sensor_noise`/`rng` 参数
- 默认 task_suite 从 `libero_90` 改为 `libero_spatial`（libero_90 无扰动变体）
- `collect_activations.py` 新增 `--task_suite` 参数

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "uuid": "d042da34-678a-477f-86c3-1e4da6418b65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCxFn4TCpQKuKW3tkZg3Aw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2858,
      "cache_read_input_tokens": 126417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2858
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


### Task result

_source line 190_

全部验证通过。汇总结果：

---

## 产出报告

### 1. PERTURBATION_SUFFIXES 匹配报告

旧的简单后缀匹配已替换为 **正则解析**（`_classify_task()`），100% 覆盖所有 4 个 LIBERO-Plus 套件：

| 扰动类型 | libero_spatial | libero_object | libero_goal | libero_10 |
|---|---|---|---|---|
| **nominal** (base) | 390 | 354 | 410 | 383 |
| **camera_viewpoints** | 376 | 396 | 408 | 419 |
| **robot_initial_states** | 350 | 398 | 409 | 393 |
| **sensor_noise** | 351 | 422 | 379 | 449 |
| **light_conditions** | 292 | 297 | 279 | 274 |
| **background_textures** | 258 | 248 | 281 | 289 |
| **objects_layout** | 385 | 403 | 425 | 312 |
| **TOTAL** | **2402/2402** | **2518/2518** | **2591/2591** | **2519/2519** |

命名格式解析：
- 复合后缀：`{base}_view_{H}_{V}_{S}_{R}_{E}_initstate_{I}[_noise_{N}]` → 通过参数值判断类型
- 简单后缀：`_light_\d+`, `_table_\d+`/`_tb_\d+`, `_add_\d+`/`_level\d+` → 末尾正则匹配

### 2. sensor_noise 实现确认

**LIBERO-Plus 内置**，非自实现。已删除 `_apply_sensor_noise()`。

环境层应用（`env_wrapper.py` L288-342），5 种噪声 × 10 级 severity = 50 级别：
| noise 值 | 类型 | 参数 |
|---|---|---|
| 1-10 | motion_blur | radius/sigma 递增 |
| 11-20 | gaussian_blur | sigma 1-10 |
| 21-30 | zoom_blur | zoom range 递增 |
| 31-40 | fog | plasma fractal |
| 41-50 | glass_blur | sigma/delta/iter |

通过任务名后缀 `_noise_N` 选择，env.step() 自动对 agentview 和 wrist 图像施加噪声。

### 3. 模型加载修复

原始报错 `openpi.models_pytorch.model_config.get_model_config` 不存在 — 因为该 API 根本不存在。正确 API：
```python
from openpi.training.config import get_config         # config_name="pi0_libero"
from openpi.policies.policy_config import create_trained_policy
```

已修复：
- `load_pi0_for_collection()` 使用正确的 API 路径（本就正确）
- 添加 `_ensure_openpi_imports()` stub 掉 lerobot（训练依赖，推理不需要）
- 安装缺失依赖：augmax, chex, tqdm-loggable, openpi-client, lerobot 等
- 升级 orbax-checkpoint 到 0.11.39（兼容 jax 0.10.0）
- OpenPI config 获取验证通过：`get_config("pi0_libero")` → OK

### 4. 代码部署状态

| 文件 | 远程路径 | 语法 | 导入 |
|---|---|---|---|
| libero_integration.py | `/root/meta_brain_lora_routing/phase0/` | ✓ | ✓ |
| collect_activations.py | `/root/meta_brain_lora_routing/phase0/` | ✓ | ✓ |

关键变更：
- 删除 `PERTURBATION_SUFFIXES` → 替换为 `_classify_task()` 正则解析
- 删除 `_apply_sensor_noise()` → env 内置
- `obs_to_model_input()` 移除 `sensor_noise`/`rng` 参数
- 默认 task_suite 从 `libero_90` 改为 `libero_spatial`（libero_90 无扰动变体）
- `collect_activations.py` 新增 `--task_suite` 参数

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1016598,
  "duration_api_ms": 834371,
  "num_turns": 68,
  "stop_reason": "end_turn",
  "session_id": "7fb1a7e9-8182-485d-9b07-0eab8188118b",
  "total_cost_usd": 3.5410695,
  "usage": {
    "input_tokens": 46,
    "cache_creation_input_tokens": 117828,
    "cache_read_input_tokens": 3534975,
    "output_tokens": 41367,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 117828,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3228,
        "cache_read_input_tokens": 126417,
        "cache_creation_input_tokens": 2858,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2858
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2652,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0027519999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 46,
      "outputTokens": 41367,
      "cacheReadInputTokens": 3534975,
      "cacheCreationInputTokens": 117828,
      "webSearchRequests": 0,
      "costUSD": 3.5383175,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "80397c8e-0d39-4da7-8453-bef2812d8cf3"
}
```

</details>

---
