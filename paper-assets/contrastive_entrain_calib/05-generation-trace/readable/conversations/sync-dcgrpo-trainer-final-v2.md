# sync dcgrpo trainer final v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_sync_dcgrpo_trainer_final_v2_20260518T125951.jsonl`
- **Structured JSON:** [`cdfe529d52f160447487.json`](../../sessions/cd/cdfe529d52f160447487.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-18T13:02:27.448198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/dcgrpo_trainer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/dcgrpo_trainer.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T13:02:27.448679+00:00_

1	"""DCGRPOTrainer: Direction-Contrastive GRPO for sycophancy calibration.
2	
3	Inherits trl.GRPOTrainer, overrides reward computation to inject three signals:
4	  R1 (Direction Alignment)     -- dot(h, d_syc) at critical-turn hidden state
5	  R2 (Contrastive Consistency) -- sigmoid(R1_valid - R1_invalid) - 0.5
6	  R3 (Behavioral NLI)          -- DeBERTa entailment probability
7	
8	Overrides completion generation to support multi-turn dialogue with activation caching.
9	
10	Input:  Dataset with columns: prompt (3-turn dialogue), condition, pair_id
11	Output: LoRA-tuned policy model with reduced sycophantic capitulation
12	
13	Dependencies: trl>=0.15, transformers>=4.45, peft, torch
14	"""
15	
16	from __future__ import annotations
17	
18	import logging
19	from dataclasses import dataclass, field
20	from typing import Any
21	
22	import torch
23	import torch.nn as nn
24	import torch.nn.functional as F
25	from trl import GRPOConfig, GRPOTrainer
26	
27	logger = logging.getLogger(__name__)
28	
29	
30	# =====================================================================
31	# Activation Cache
32	# =====================================================================
33	
34	def _resolve_transformer_layers(model: nn.Module) -> nn.ModuleList:
35	    """Find transformer decoder layers, handling PEFT wrappers.
36	
37	    Supports Qwen/Llama/Mistral (model.model.layers layout).
38	    Unwraps PEFT indirection and handles transformers>=5.x where
39	    model.base_model returns the inner model directly.
40	    """
41	    candidate = model
42	    # PEFT wrapping: model.base_model.model.model.layers
43	    if hasattr(candidate, "base_model"):
44	        candidate = candidate.base_model
45	    if hasattr(candidate, "layers"):
46	        return candidate.layers
47	    if hasattr(candidate, "model"):
48	        inner = candidate.model
49	        if hasattr(inner, "layers"):
50	            return inner.layers
51	        if hasattr(inner, "model") and hasattr(inner.model, "layers"):
52	
…[truncated 31046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T13:02:27.448940+00:00_

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
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
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

_source line 4 · 2026-05-18T13:02:27.449104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T13:02:27.449264+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29046",
  "command": "mkdir -p /root/mvp_v2_1_expanded/training/ && ls -la /root/mvp_v2_1_expanded/training/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29046",
    "command": "mkdir -p /root/mvp_v2_1_expanded/training/ && ls -la /root/mvp_v2_1_expanded/training/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T13:02:27.449414+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 44\\ndrwxr-xr-x 3 root root    91 May 18 20:36 .\\ndrwxr-xr-x 5 root root   148 May 18 19:54 ..\\ndrwxr-xr-x 2 root root    52 May 18 20:35 __pycache__\\n-rw-r--r-- 1 root root 29006 May 18 20:35 dcgrpo_trainer.py\\n-rw-r--r-- 1 root root  8536 May 18 20:36 gpu_smoke_test.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T13:02:27.449650+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29046",
  "command": "cat > /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py << 'HEREDOC_EOF'\n\"\"\"DCGRPOTrainer: Direction-Contrastive GRPO for sycophancy calibration.\n\nInherits trl.GRPOTrainer, overrides reward computation to inject three signals:\n  R1 (Direction Alignment)     -- dot(h, d_syc) at critical-turn hidden state\n  R2 (Contrastive Consistency) -- sigmoid(R1_valid - R1_invalid) - 0.5\n  R3 (Behavioral NLI)          -- DeBERTa entailment probability\n\nOverrides completion generation to support multi-turn dialogue with activation caching.\n\nInput:  Dataset with columns: prompt (3-turn dialogue), condition, pair_id\nOutput: LoRA-tuned policy model with reduced sycophantic capitulation\n\nDependencies: trl>=0.15, transformers>=4.45, peft, torch\n\"\"\"\n\nfrom __future__ import annotations\n\nimport logging\nfrom dataclasses import dataclass, field\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogger = logging.getLogger(__name__)\n\n\n# =====================================================================\n# Activation Cache\n# =====================================================================\n\ndef _resolve_transformer_layers(model: nn.Module) -> nn.ModuleList:\n    \"\"\"Find transformer decoder layers, handling PEFT wrappers.\n\n    Supports Qwen/Llama/Mistral (model.model.layers layout).\n    Unwraps PEFT indirection and handles transformers>=5.x where\n    model.base_model returns the inner model directly.\n    \"\"\"\n    candidate = model\n    # PEFT wrapping: model.base_model.model.model.layers\n    if hasattr(candidate, \"base_model\"):\n        candidate = candidate.base_model\n    if hasattr(candidate, \"layers\"):\n        return candidate.layers\n    if hasattr(candidate, \"model\"):\n        inner = candidate.model\n        if hasattr(inner, \"layers\"):\n            return inner.layers\n        if hasattr(inner, \"model\") and hasattr(inner.model, \"layers\"):\n            return inner.model.layers\n    raise AttributeError(\n        f\"Cannot locate transformer layers on {type(model).__name__}. \"\n        \"Expected model.model.layers or model.base_model.model.model.layers.\"\n    )\n\n\nclass ActivationCache:\n    \"\"\"Forward hook to cache hidden states at specified layers during generation.\"\"\"\n\n    def __init__(self, target_layers: list[int]):\n        self.target_layers = set(target_layers)\n        self.cache: dict[int, torch.Tensor] = {}\n        self.hooks: list = []\n\n    def register(self, model: nn.Module) -> None:\n        \"\"\"Attach forward hooks to target transformer layers.\"\"\"\n        self.remove()\n        layers = _resolve_transformer_layers(model)\n        for idx in sorted(self.target_layers):\n            if idx >= len(layers):\n                raise ValueError(\n                    f\"Layer {idx} out of range (model has {len(layers)} layers)\"\n                )\n            self.hooks.append(\n                layers[idx].register_forward_hook(self._make_hook(idx))\n            )\n        logger.info(\n            \"Activation hooks registered on layers %s\", sorted(self.target_layers)\n        )\n\n    def _make_hook(self, layer_idx: int):\n        def fn(module, input, output):\n            hidden = output[0] if isinstance(output, tuple) else output\n            self.cache[layer_idx] = hidden.detach()\n        return fn\n\n    def clear(self):\n        self.cache = {}\n\n    def remove(self):\n        for h in self.hooks:\n            h.remove()\n        self.hooks.clear()\n        self.cache.clear()\n\n\n# =====================================================================\n# Configuration\n# =====================================================================\n\n@dataclass\nclass DCGRPOConfig(GRPOConfig):\n    \"\"\"GRPOConfig extended with DC-GRPO reward and direction parameters.\n\n    Additional fields control the direction-contrastive reward mechanism:\n    direction_path points to directions.pt from compute_directions.py,\n    reward_layers selects which transformer layers to probe (default 19-27,\n    the highest-AUROC range from MVP), and r1/r2/r3 weights set the\n    relative contribution of each reward component.\n    \"\"\"\n\n    direction_path: str = \"\"\n    reward_layers: list[int] = field(\n        default_factory=lambda: list(range(19, 36))\n    )\n    reward_position: str = \"asst_first\"\n\n    r1_weight: float = 1.0\n    r2_weight: float = 0.5\n    r3_weight: float = 0.3\n\n    r3_model_name: str = \"microsoft/deberta-v3-base\"\n    nli_batch_size: int = 16\n\n\n# =====================================================================\n# Placeholder reward for GRPOTrainer constructor\n# =====================================================================\n\ndef _noop_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"Placeholder passed to super().__init__; actual rewards computed in override.\"\"\"\n    return [0.0] * len(completions)\n\n\nclass _DCRewardCallable:\n    \"\"\"Callable that computes combined R1+R2+R3 DC-GRPO rewards.\n\n    Plugged into TRL's reward_funcs after super().__init__. Receives prompts,\n    completions, and dataset columns (condition, pair_id) from TRL's\n    _calculate_rewards via **reward_kwargs. Runs a forward pass with hooks\n    to extract activations for R1/R2.\n    \"\"\"\n\n    __name__ = \"dc_grpo_reward\"\n\n    def __init__(self, trainer: \"DCGRPOTrainer\"):\n        self.trainer = trainer\n\n    def __call__(self, prompts, completions, **kwargs):\n        conditions = kwargs.get(\"condition\", [\"unknown\"] * len(completions))\n        pair_ids = kwargs.get(\"pair_id\", [str(i) for i in range(len(completions))])\n\n        t = self.trainer\n        if t.d_syc is None:\n            logger.warning(\"d_syc not loaded; returning R3-only rewards\")\n            r3 = t.compute_r3(completions, conditions)\n            return [t._r3_w * s for s in r3]\n\n        tokenizer = t.processing_class\n        t._prompt_lengths = [\n            len(tokenizer.encode(p, add_special_tokens=False))\n            for p in prompts\n        ]\n        full_texts = [p + c for p, c in zip(prompts, completions)]\n        encoded = tokenizer(\n            full_texts,\n            padding=True,\n            truncation=True,\n            return_tensors=\"pt\",\n        ).to(t.model.device)\n        positions = t._find_asst_first_positions(encoded.input_ids, tokenizer)\n        batch_acts = t._extract_activations(\n            encoded.input_ids, encoded.attention_mask, positions\n        )\n\n        rewards, components = t.compute_rewards(\n            completions, conditions, pair_ids, batch_acts\n        )\n\n        t._reward_step += 1\n        step = t._reward_step\n\n        if step <= 10:\n            import statistics\n            for name, values in components.items():\n                if values:\n                    mu = sum(values) / len(values)\n                    sd = statistics.stdev(values) if len(values) > 1 else 0.0\n                    logger.info(\n                        \"[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f\",\n                        step, name, mu, sd, min(values), max(values),\n                    )\n            if rewards:\n                mu = sum(rewards) / len(rewards)\n                sd = statistics.stdev(rewards) if len(rewards) > 1 else 0.0\n                logger.info(\n                    \"[step %d] reward/combined  mean=%.4f  std=%.4f\",\n                    step, mu, sd,\n                )\n        else:\n            for name, values in components.items():\n                if values:\n                    logger.info(\"reward/%s_mean=%.4f\", name, sum(values) / len(values))\n            if rewards:\n                logger.info(\n                    \"reward/combined_mean=%.4f\", sum(rewards) / len(rewards)\n                )\n\n        return rewards\n\n\n# =====================================================================\n# DCGRPOTrainer\n# =====================================================================\n\nclass DCGRPOTrainer(GRPOTrainer):\n    \"\"\"Direction-Contrastive GRPO trainer for sycophancy calibration.\n\n    Reward signals:\n      R1 = sign(condition) * dot(h, d_syc)         (direction alignment)\n      R2 = sigmoid(R1_valid - R1_invalid) - 0.5    (contrastive consistency)\n      R3 = NLI_entailment(completion, expected)     (behavioral appropriateness)\n      R  = w1*R1 + w2*R2 + w3*R3\n\n    Data flow:\n      generate_completions() caches activations via forward hooks.\n      compute_rewards() reads cached activations for R1/R2, runs NLI for R3.\n\n    Expected dataset columns beyond \"prompt\":\n      condition  -- \"valid_correction\" or \"invalid_pressure\"\n      pair_id    -- links the two conditions of the same calibration pair\n    \"\"\"\n\n    def __init__(\n        self,\n        model: str | nn.Module,\n        args: DCGRPOConfig,\n        train_dataset: Any,\n        eval_dataset: Any | None = None,\n        processing_class: Any | None = None,\n        peft_config: Any | None = None,\n        **kwargs,\n    ):\n        # Store config before super().__init__ (which sets self.model)\n        self._direction_path = args.direction_path\n        self._reward_layers = args.reward_layers\n        self._pos_idx = 1 if args.reward_position == \"asst_first\" else 0\n        self._r1_w = args.r1_weight\n        self._r2_w = args.r2_weight\n        self._r3_w = args.r3_weight\n        self._r3_model_name = args.r3_model_name\n        self._nli_batch_size = args.nli_batch_size\n\n        # Populated after super().__init__\n        self.d_syc: torch.Tensor | None = None\n        self._act_cache: ActivationCache | None = None\n        self._step_acts: list[dict[int, torch.Tensor]] | None = []\n        self._nli_model: nn.Module | None = None\n        self._nli_tokenizer: Any = None\n        self._extraction_failures: int = 0\n        self._prompt_lengths: list[int] = []\n        self._reward_step: int = 0\n\n        super().__init__(\n            model=model,\n            reward_funcs=[_noop_reward_fn],\n            args=args,\n            train_dataset=train_dataset,\n            eval_dataset=eval_dataset,\n            processing_class=processing_class,\n            peft_config=peft_config,\n            **kwargs,\n        )\n\n        # Post-init: self.model now exists\n        self._load_directions()\n        self._act_cache = ActivationCache(self._reward_layers)\n        self._act_cache.register(self.model)\n\n        # Replace noop placeholder with actual DC-GRPO reward function\n        self.reward_funcs = [_DCRewardCallable(self)]\n        if hasattr(self, \"reward_func_names\"):\n            self.reward_func_names = [\"dc_grpo_reward\"]\n\n    # -----------------------------------------------------------------\n    # Direction loading\n    # -----------------------------------------------------------------\n\n    def _load_directions(self) -> None:\n        \"\"\"Load d_syc direction vectors from directions.pt.\"\"\"\n        if not self._direction_path:\n            logger.warning(\"No direction_path provided; R1/R2 will return 0.0\")\n            return\n        data = torch.load(\n            self._direction_path, map_location=\"cpu\", weights_only=True\n        )\n        self.d_syc = data[\"d_syc\"]  # (num_layers, 2, hidden_dim)\n        logger.info(\n            \"Loaded d_syc shape=%s from %s\",\n            self.d_syc.shape,\n            self._direction_path,\n        )\n\n    def reload_directions(self, path: str) -> None:\n        \"\"\"Hot-reload directions after periodic recalibration.\n\n        Logs a warning per layer if cosine similarity between old and new\n        directions drops below 0.7 (potential direction drift under LoRA).\n        \"\"\"\n        old_d = self.d_syc\n        self._direction_path = path\n        self._load_directions()\n\n        if old_d is not None and self.d_syc is not None:\n            for layer_idx in self._reward_layers:\n                if layer_idx >= min(old_d.shape[0], self.d_syc.shape[0]):\n                    continue\n                cos = F.cosine_similarity(\n                    old_d[layer_idx, self._pos_idx].unsqueeze(0),\n                    self.d_syc[layer_idx, self._pos_idx].unsqueeze(0),\n                ).item()\n                if cos < 0.7:\n                    logger.warning(\n                        \"Direction drift at layer %d: cosine=%.3f\", layer_idx, cos\n                    )\n\n    # -----------------------------------------------------------------\n    # NLI model (lazy)\n    # -----------------------------------------------------------------\n\n    def _ensure_nli_model(self) -> None:\n        \"\"\"Lazy-load DeBERTa NLI model for R3 scoring.\"\"\"\n        if self._nli_model is not None:\n            return\n        from transformers import (\n            AutoModelForSequenceClassification,\n            AutoTokenizer,\n        )\n\n        self._nli_tokenizer = AutoTokenizer.from_pretrained(self._r3_model_name)\n        self._nli_model = (\n            AutoModelForSequenceClassification.from_pretrained(self._r3_model_name)\n            .eval()\n        )\n        logger.info(\"Loaded NLI model: %s\", self._r3_model_name)\n\n    # -----------------------------------------------------------------\n    # Position finding\n    # -----------------------------------------------------------------\n\n    def _find_asst_first_positions(\n        self,\n        input_ids: torch.Tensor,\n        tokenizer: Any,\n    ) -> list[int]:\n        \"\"\"Locate asst_first position using tokenize-based method.\n\n        Matches extract_activations_v2.py: asst_first = len(prompt_tokens) - 1,\n        the last prompt token whose hidden state predicts the first generated\n        content token. Uses self._prompt_lengths when available (set by\n        generate_completions or _DCRewardCallable before calling this method).\n        Falls back to scanning for the <|im_start|> assistant marker.\n        \"\"\"\n        positions: list[int] = []\n        for i in range(input_ids.shape[0]):\n            seq_len = input_ids.shape[1]\n            if self._prompt_lengths and i < len(self._prompt_lengths):\n                pos = self._prompt_lengths[i] - 1\n            else:\n                im_start_id = tokenizer.convert_tokens_to_ids(\"<|im_start|>\")\n                ids_list = input_ids[i].tolist()\n                pos = seq_len - 1\n                for j in range(len(ids_list) - 1, -1, -1):\n                    if ids_list[j] == im_start_id:\n                        candidate = j + 2\n                        if candidate < seq_len:\n                            pos = candidate\n                        break\n            positions.append(min(pos, seq_len - 1))\n        return positions\n\n    # -----------------------------------------------------------------\n    # Activation extraction\n    # -----------------------------------------------------------------\n\n    def _extract_activations(\n        self,\n        input_ids: torch.Tensor,\n        attention_mask: torch.Tensor,\n        positions: list[int],\n    ) -> list[dict[int, torch.Tensor]]:\n        \"\"\"Forward pass to extract hidden states at asst_first positions.\n\n        Runs the full sequence through the model with hooks enabled, then\n        reads the cached hidden state at each sample's designated position.\n        This is a separate pass from generation (generate() uses KV cache\n        and only exposes the latest-token hidden state per step).\n\n        Args:\n            input_ids: (batch, seq_len) full sequences (prompt + completion).\n            attention_mask: (batch, seq_len).\n            positions: Per-sample token position for extraction.\n\n        Returns:\n            List of per-sample dicts: {layer_idx: Tensor(hidden_dim,)}.\n        \"\"\"\n        self._act_cache.clear()\n        with torch.no_grad():\n            self.model(input_ids=input_ids, attention_mask=attention_mask)\n\n        batch_acts: list[dict[int, torch.Tensor]] = []\n        for sample_idx, pos in enumerate(positions):\n            acts: dict[int, torch.Tensor] = {}\n            for layer_idx in self._reward_layers:\n                cached = self._act_cache.cache.get(layer_idx)\n                if cached is not None:\n                    acts[layer_idx] = cached[sample_idx, pos]\n            batch_acts.append(acts)\n\n        self._act_cache.clear()\n        return batch_acts\n\n    # -----------------------------------------------------------------\n    # R1: Direction Alignment\n    # -----------------------------------------------------------------\n\n    def compute_r1(\n        self,\n        activations: dict[int, torch.Tensor],\n        condition: str,\n    ) -> float:\n        \"\"\"Direction alignment reward for a single completion.\n\n        R1 = +dot(h, d_syc) for valid_correction   (reward genuine revision)\n        R1 = -dot(h, d_syc) for invalid_pressure    (penalize capitulation)\n\n        Direction vectors are L2-normalized per the compute_directions.py\n        convention, so dot product magnitude scales with activation norm\n        (stronger internal signal produces stronger reward).\n        Averaged across all reward_layers.\n\n        Args:\n            activations: {layer_idx: Tensor(hidden_dim,)} at asst_first position.\n            condition: \"valid_correction\" or \"invalid_pressure\".\n\n        Returns:\n            Scalar R1 reward.\n        \"\"\"\n        if self.d_syc is None:\n            return 0.0\n\n        sign = 1.0 if condition == \"valid_correction\" else -1.0\n        scores: list[float] = []\n        for layer_idx in self._reward_layers:\n            h = activations.get(layer_idx)\n            if h is None:\n                continue\n            d = self.d_syc[layer_idx, self._pos_idx].to(h)\n            scores.append(sign * torch.dot(h, d).item())\n\n        if not scores:\n            return 0.0\n        raw = sum(scores) / len(scores)\n        return torch.tanh(torch.tensor(raw / 20.0)).item()\n\n    def compute_r1_batch(\n        self,\n        batch_activations: list[dict[int, torch.Tensor]],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"R1 for a batch of completions.\"\"\"\n        return [\n            self.compute_r1(acts, cond)\n            for acts, cond in zip(batch_activations, conditions)\n        ]\n\n    # -----------------------------------------------------------------\n    # R2: Contrastive Consistency\n    # -----------------------------------------------------------------\n\n    def compute_r2(self, r1_valid: float, r1_invalid: float) -> float:\n        \"\"\"Rank-based contrastive reward for a condition pair.\n\n        R2 = sigmoid(R1_valid - R1_invalid) - 0.5\n\n        Positive when valid_correction R1 exceeds invalid_pressure R1 within\n        the same calibration pair. S1 rank-based design avoids the\n        d_gen = -d_syc degeneracy (see skeleton section 8).\n\n        Args:\n            r1_valid: R1 from the valid_correction completion.\n            r1_invalid: R1 from the invalid_pressure completion.\n\n        Returns:\n            Scalar R2 in (-0.5, 0.5).\n        \"\"\"\n        return torch.sigmoid(torch.tensor(r1_valid - r1_invalid)).item() - 0.5\n\n    def compute_r2_for_group(\n        self,\n        r1_scores: list[float],\n        conditions: list[str],\n        pair_ids: list[str],\n    ) -> list[float]:\n        \"\"\"R2 for all completions in a training step, paired by pair_id.\n\n        Aggregates mean R1 per (pair_id, condition), then applies R2.\n        All completions from the same pair receive the same R2 score.\n        Completions without a paired counterpart get R2 = 0.\n\n        Args:\n            r1_scores: R1 per completion (same order as conditions/pair_ids).\n            conditions: Per-completion condition label.\n            pair_ids: Per-completion pair identifier.\n\n        Returns:\n            List of R2 scores, same length as input.\n        \"\"\"\n        # Aggregate R1 by (pair_id, condition)\n        pair_r1: dict[str, dict[str, list[float]]] = {}\n        for r1, cond, pid in zip(r1_scores, conditions, pair_ids):\n            pair_r1.setdefault(pid, {}).setdefault(cond, []).append(r1)\n\n        pair_means: dict[str, dict[str, float]] = {}\n        for pid, cond_map in pair_r1.items():\n            pair_means[pid] = {\n                c: sum(vs) / len(vs) for c, vs in cond_map.items()\n            }\n\n        r2_scores: list[float] = []\n        for cond, pid in zip(conditions, pair_ids):\n            means = pair_means.get(pid, {})\n            r1_v = means.get(\"valid_correction\")\n            r1_i = means.get(\"invalid_pressure\")\n            if r1_v is not None and r1_i is not None:\n                r2_scores.append(self.compute_r2(r1_v, r1_i))\n            else:\n                r2_scores.append(0.0)\n        return r2_scores\n\n    # -----------------------------------------------------------------\n    # R3: Behavioral NLI\n    # -----------------------------------------------------------------\n\n    def compute_r3(\n        self,\n        completions: list[str],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"Behavioral NLI reward for a batch of completions.\n\n        Constructs (premise, hypothesis) pairs per completion:\n          premise:    \"The model said: {completion}\"\n          hypothesis: condition-dependent expected behavior\n\n        R3 = P(entailment) from DeBERTa-v3-base NLI.\n        Processed in batches of nli_batch_size. Does not participate\n        in gradient computation.\n\n        Args:\n            completions: Generated response texts.\n            conditions: Per-completion condition labels.\n\n        Returns:\n            List of R3 scores (entailment probabilities in [0, 1]).\n        \"\"\"\n        self._ensure_nli_model()\n\n        premises: list[str] = []\n        hypotheses: list[str] = []\n        for text, cond in zip(completions, conditions):\n            premises.append(f\"The model said: {text}\")\n            if cond == \"valid_correction\":\n                hypotheses.append(\n                    \"The model revised its answer after receiving valid correction.\"\n                )\n            else:\n                hypotheses.append(\n                    \"The model maintained its answer despite invalid pressure.\"\n                )\n\n        scores: list[float] = []\n        for i in range(0, len(premises), self._nli_batch_size):\n            batch_p = premises[i : i + self._nli_batch_size]\n            batch_h = hypotheses[i : i + self._nli_batch_size]\n            inputs = self._nli_tokenizer(\n                batch_p,\n                batch_h,\n                padding=True,\n                truncation=True,\n                max_length=512,\n                return_tensors=\"pt\",\n            ).to(self._nli_model.device)\n\n            with torch.no_grad():\n                logits = self._nli_model(**inputs).logits\n                probs = F.softmax(logits, dim=-1)\n                # DeBERTa NLI label order: contradiction=0, neutral=1, entailment=2\n                scores.extend(probs[:, 2].tolist())\n\n        return scores\n\n    # -----------------------------------------------------------------\n    # Combined reward\n    # -----------------------------------------------------------------\n\n    def compute_rewards(\n        self,\n        completions: list[str],\n        conditions: list[str],\n        pair_ids: list[str],\n        batch_activations: list[dict[int, torch.Tensor]],\n    ) -> tuple[list[float], dict[str, list[float]]]:\n        \"\"\"Compute combined R = w1*R1 + w2*R2 + w3*R3 for a batch.\n\n        Args:\n            completions: Generated response texts.\n            conditions: Per-completion condition labels.\n            pair_ids: Per-completion pair identifiers for R2 pairing.\n            batch_activations: Per-completion activation dicts from\n                _extract_activations.\n\n        Returns:\n            (combined_rewards, component_dict) where component_dict maps\n            \"r1\", \"r2\", \"r3\" to their respective score lists.\n        \"\"\"\n        r1 = self.compute_r1_batch(batch_activations, conditions)\n        r2 = self.compute_r2_for_group(r1, conditions, pair_ids)\n        r3 = self.compute_r3(completions, conditions)\n\n        combined = [\n            self._r1_w * s1 + self._r2_w * s2 + self._r3_w * s3\n            for s1, s2, s3 in zip(r1, r2, r3)\n        ]\n\n        components = {\"r1\": r1, \"r2\": r2, \"r3\": r3}\n        return combined, components\n\n    # -----------------------------------------------------------------\n    # GRPOTrainer override: generate_completions\n    # -----------------------------------------------------------------\n\n    def generate_completions(self, prompts, **kwargs):\n        \"\"\"Override to cache activations alongside standard generation.\n\n        Multi-turn prompts (3-turn dialogues formatted via chat template)\n        are handled natively by the parent's generation logic. After\n        completions are produced, a separate forward pass extracts hidden\n        states at the asst_first position for R1/R2 computation.\n\n        The extra forward pass adds ~5-10% overhead per training step.\n        Cached activations are stored in self._step_acts for retrieval\n        in _compute_step_rewards().\n        \"\"\"\n        tokenizer = self.processing_class\n        if isinstance(prompts, (list, tuple)) and len(prompts) > 0:\n            if isinstance(prompts[0], str):\n                self._prompt_lengths = [\n                    len(tokenizer.encode(p, add_special_tokens=False))\n                    for p in prompts\n                ]\n            elif isinstance(prompts[0], torch.Tensor):\n                pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\n                self._prompt_lengths = [\n                    (p != pad_id).sum().item() for p in prompts\n                ]\n\n        completions = super().generate_completions(prompts, **kwargs)\n\n        try:\n            if isinstance(prompts, (list, tuple)) and len(prompts) > 0:\n                if isinstance(prompts[0], str):\n                    comp_texts = (\n                        completions\n                        if isinstance(completions[0], str)\n                        else [tokenizer.decode(c, skip_special_tokens=False) for c in completions]\n                    )\n                    full_texts = [p + c for p, c in zip(prompts, comp_texts)]\n                    encoded = tokenizer(\n                        full_texts,\n                        padding=True,\n                        truncation=True,\n                        return_tensors=\"pt\",\n                    ).to(self.model.device)\n                    input_ids = encoded.input_ids\n                    attention_mask = encoded.attention_mask\n                elif isinstance(prompts[0], torch.Tensor):\n                    comp_ids = (\n                        completions\n                        if isinstance(completions, torch.Tensor)\n                        else torch.stack(completions)\n                    )\n                    input_ids = torch.cat(\n                        [torch.stack(prompts), comp_ids], dim=-1\n                    )\n                    pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id\n                    attention_mask = (input_ids != pad_id).long()\n                else:\n                    return completions\n\n                positions = self._find_asst_first_positions(\n                    input_ids, tokenizer\n                )\n                self._step_acts = self._extract_activations(\n                    input_ids, attention_mask, positions\n                )\n                self._extraction_failures = 0\n        except Exception as e:\n            self._step_acts = None\n            self._extraction_failures += 1\n            logger.warning(\n                \"Activation extraction failed (attempt %d): %s\",\n                self._extraction_failures,\n                e,\n            )\n            if self._extraction_failures >= 10:\n                raise RuntimeError(\n                    \"Activation extraction failed 10 consecutive times, aborting training\"\n                ) from e\n\n        return completions\n\n    # -----------------------------------------------------------------\n    # GRPOTrainer integration: step-level reward computation\n    # -----------------------------------------------------------------\n\n    def _compute_step_rewards(\n        self,\n        prompts: list[str],\n        completions: list[str],\n        conditions: list[str],\n        pair_ids: list[str],\n    ) -> list[float]:\n        \"\"\"Entry point for per-step reward computation.\n\n        Called during the training loop after generate_completions().\n        Reads self._step_acts (populated by generate_completions),\n        computes R1+R2+R3, logs component statistics, and clears the cache.\n\n        Wire this into the training loop by having the reward_funcs wrapper\n        delegate here, or by overriding _generate_and_score_completions\n        (TRL internal method name may vary by version).\n\n        Args:\n            prompts: Prompt texts for this step.\n            completions: Generated completion texts.\n            conditions: Per-completion condition labels from dataset.\n            pair_ids: Per-completion pair identifiers from dataset.\n\n        Returns:\n            List of combined reward scalars, one per completion.\n        \"\"\"\n        if self._step_acts is None:\n            logger.warning(\n                \"step_acts is None (extraction failed); returning zero rewards\"\n            )\n            return [0.0] * len(completions)\n\n        batch_acts = self._step_acts if self._step_acts else [{}] * len(completions)\n\n        rewards, components = self.compute_rewards(\n            completions, conditions, pair_ids, batch_acts\n        )\n\n        for name, values in components.items():\n            if values:\n                avg = sum(values) / len(values)\n                logger.info(\"reward/%s_mean=%.4f\", name, avg)\n        if rewards:\n            logger.info(\n                \"reward/combined_mean=%.4f\", sum(rewards) / len(rewards)\n            )\n\n        self._step_acts.clear()\n        return rewards\n\n    # -----------------------------------------------------------------\n    # Cleanup\n    # -----------------------------------------------------------------\n\n    def cleanup(self) -> None:\n        \"\"\"Remove hooks and free NLI model memory.\"\"\"\n        if self._act_cache is not None:\n            self._act_cache.remove()\n        self._nli_model = None\n        self._nli_tokenizer = None\n        torch.cuda.empty_cache()\nHEREDOC_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29046",
    "command": "cat > /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py << 'HEREDOC_EOF'\n\"\"\"DCGRPOTrainer: Direction-Contrastive GRPO for sycophancy calibration.\n\nInherits trl.GRPOTrainer, overrides reward computation to inject three signals:\n  R1 (Direction Alignment)     -- dot(h, d_syc) at critical-turn hidden state\n  R2 (Contrastive Consistency) -- sigmoid(R1_valid - R1_invalid) - 0.5\n  R3 (Behavioral NLI)          -- DeBERTa entailment probability\n\nOverrides completion generation to support multi-turn dialogue with activation caching.\n\nInput:  Dataset with columns: prompt (3-turn dialogue), condition, pair_id\nOutput: LoRA-tuned policy model with reduced sycophantic capitulation\n\nDependencies: trl>=0.15, transformers>=4.45, peft, torch\n\"\"\"\n\nfrom __future__ import annotations\n\nimport logging\nfrom dataclasses import dataclass, field\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogger = logging.getLogger(__name__)\n\n\n# =====================================================================\n# Activation Cache\n# =====================================================================\n\ndef _resolve_transformer_layers(model: nn.Module) -> nn.ModuleList:\n    \"\"\"Find transformer decoder layers, handling PEFT wrappers.\n\n    Supports Qwen/Llama/Mistral (model.model.layers layout).\n    Unwraps PEFT indirection and handles transformers>=5.x where\n    model.base_model returns the inner model directly.\n    \"\"\"\n    candidate = model\n    # PEFT wrapping: model.base_model.model.model.layers\n    if hasattr(candidate, \"base_model\"):\n        candidate = candidate.base_model\n    if hasattr(candidate, \"layers\"):\n        return candidate.layers\n    if hasattr(candidate, \"model\"):\n        inner = candidate.model\n        if hasattr(inner, \"layers\"):\n            return inner.layers\n        if hasattr(inner, \"model\") and hasattr(inner.model, \"layers\"):\n            return inner.model.layers\n    raise AttributeError(\n        f\"Cannot locate transformer layers on {type(model).__name__}. \"\n        \"Expected model.model.layers or model.base_model.model.model.layers.\"\n    )\n\n\nclass ActivationCache:\n    \"\"\"Forward hook to cache hidden states at specified layers during generation.\"\"\"\n\n    def __init__(self, target_layers: list[int]):\n        self.target_layers = set(target_layers)\n        self.cache: dict[int, torch.Tensor] = {}\n        self.hooks: list = []\n\n    def register(self, model: nn.Module) -> None:\n        \"\"\"Attach forward hooks to target transformer layers.\"\"\"\n        self.remove()\n        layers = _resolve_transformer_layers(model)\n        for idx in sorted(self.target_layers):\n            if idx >= len(layers):\n                raise ValueError(\n                    f\"Layer {idx} out of range (model has {len(layers)} layers)\"\n                )\n            self.hooks.append(\n                layers[idx].register_forward_hook(self._make_hook(idx))\n            )\n        logger.info(\n            \"Activation hooks registered on layers %s\", sorted(self.target_layers)\n        )\n\n    def _make_hook(self, layer_idx: int):\n        def fn(module, input, output):\n            hidden = output[0] if isinstance(output, tuple) else output\n            self.cache[layer_idx] = hidden.detach()\n        return fn\n\n    def clear(self):\n        self.cache = {}\n\n    def remove(self):\n        for h in self.hooks:\n            h.remove()\n        self.hooks.clear()\n        self.cache.clear()\n\n\n# =====================================================================\n# Configuration\n# =====================================================================\n\n@dataclass\nclass DCGRPOConfig(GRPOConfig):\n    \"\"\"GRPOConfig extended with DC-GRPO reward and direction parameters.\n\n    Additional fields control the direction-contrastive reward mechanism:\n    direction_path points to directions.pt from compute_directions.py,\n    reward_layers selects which transformer layers to probe (default 19-27,\n    the highest-AUROC range from MVP), and r1/r2/r3 weights set the\n    relative contribution of each reward component.\n    \"\"\"\n\n    direction_path: str = \"\"\n    reward_layers: list[int] = field(\n        default_factory=lambda: list(range(19, 36))\n    )\n    reward_position: str = \"asst_first\"\n\n    r1_weight: float = 1.0\n    r2_weight: float = 0.5\n    r3_weight: float = 0.3\n\n    r3_model_name: str = \"microsoft/deberta-v3-base\"\n    nli_batch_size: int = 16\n\n\n# =====================================================================\n# Placeholder reward for GRPOTrainer constructor\n# =====================================================================\n\ndef _noop_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"Placeholder passed to super().__init__; actual rewards computed in override.\"\"\"\n    return [0.0] * len(completions)\n\n\nclass _DCRewardCallable:\n    \"\"\"Callable that computes combined R1+R2+R3 DC-GRPO rewards.\n\n    Plugged into TRL's reward_funcs after super().__init__. Receives prompts,\n    completions, and dataset columns (condition, pair_id) from TRL's\n    _calculate_rewards via **reward_kwargs. Runs a forward pass with hooks\n    to extract activations for R1/R2.\n    \"\"\"\n\n    __name__ = \"dc_grpo_reward\"\n\n    def __init__(self, trainer: \"DCGRPOTrainer\"):\n        self.trainer = trainer\n\n    def __call__(self, prompts, completions, **kwargs):\n        conditions = kwargs.get(\"condition\", [\"unknown\"] * len(completions))\n        pair_ids = kwargs.get(\"pair_id\", [str(i) for i in range(len(completions))])\n\n        t = self.trainer\n        if t.d_syc is None:\n            logger.warning(\"d_syc not loaded; returning R3-only rewards\")\n            r3 = t.compute_r3(completions, conditions)\n            return [t._r3_w * s for s in r3]\n\n        tokenizer = t.processing_class\n        t._prompt_lengths = [\n            len(tokenizer.encode(p, add_special_tokens=False))\n            for p in prompts\n        ]\n        full_texts = [p + c for p, c in zip(prompts, completions)]\n        encoded = tokenizer(\n            full_texts,\n            padding=True,\n            truncation=True,\n            return_tensors=\"pt\",\n        ).to(t.model.device)\n        positions = t._find_asst_first_positions(encoded.input_ids, tokenizer)\n        batch_acts = t._extract_activations(\n            encoded.input_ids, encoded.attention_mask, positions\n        )\n\n        rewards, components = t.compute_rewards(\n            completions, conditions, pair_ids, batch_acts\n        )\n\n        t._reward_step += 1\n        step = t._reward_step\n\n        if step <= 10:\n            import statistics\n            for name, values in components.items():\n                if values:\n                    mu = sum(values) / len(values)\n                    sd = statistics.stdev(values) if len(values) > 1 else 0.0\n                    logger.info(\n                        \"[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f\",\n                        step, name, mu, sd, min(values), max(values),\n                    )\n            if rewards:\n                mu = sum(rewards) / len(rewards)\n                sd = statistics.stdev(rewards) if len(rewards) > 1 else 0.0\n                logger.info(\n                    \"[step %d] reward/combined  mean=%.4f  std=%.4f\",\n                    step, mu, sd,\n                )\n        else:\n            for name, values in components.items():\n                if values:\n                    logger.info(\"reward/%s_mean=%.4f\", name, sum(values) / len(values))\n            if rewards:\n                logger.info(\n                    \"reward/combined_mean=%.4f\", sum(rewards) / len(rewards)\n                )\n\n        return rewards\n\n\n# =====================================================================\n# DCGRPOTrainer\n# =====================================================================\n\nclass DCGRPOTrainer(GRPOTrainer):\n    \"\"\"Direction-Contrastive GRPO trainer for sycophancy calibration.\n\n    Reward signals:\n      R1 = sign(condition) * dot(h, d_syc)         (direction alignment)\n      R2 = sigmoid(R1_valid - R1_invalid) - 0.5    (contrastive consistency)\n      R3 = NLI_entailment(completion, expected)     (behavioral appropriateness)\n      R  = w1*R1 + w2*R2 + w3*R3\n\n    Data flow:\n      generate_completions() caches activations via forward hooks.\n      compute_rewards() reads cached activations for R1/R2, runs NLI for R3.\n\n    Expected dataset columns beyond \"prompt\":\n      condition  -- \"valid_correction\" or \"invalid_pressure\"\n      pair_id    -- links the two conditions of the same calibration pair\n    \"\"\"\n\n    def __init__(\n        self,\n        model: str | nn.Module,\n        args: DCGRPOConfig,\n        train_dataset: Any,\n        eval_dataset: Any | None = None,\n        processing_class: Any | None = None,\n        peft_config: Any | None = None,\n        **kwargs,\n    ):\n        # Store config before super().__init__ (which sets self.model)\n        self._direction_path = args.direction_path\n        self._reward_layers = args.reward_layers\n        self._pos_idx = 1 if args.reward_position == \"asst_first\" else 0\n        self._r1_w = args.r1_weight\n        self._r2_w = args.r2_weight\n        self._r3_w = args.r3_weight\n        self._r3_model_name = args.r3_model_name\n        self._nli_batch_size = args.nli_batch_size\n\n        # Populated after super().__init__\n        self.d_syc: torch.Tensor | None = None\n        self._act_cache: ActivationCache | None = None\n        self._step_acts: list[dict[int, torch.Tensor]] | None = []\n        self._nli_model: nn.Module | None = None\n        self._nli_tokenizer: Any = None\n        self._extraction_failures: int = 0\n        self._prompt_lengths: list[int] = []\n        self._reward_step: int = 0\n\n        super().__init__(\n            model=model,\n            reward_funcs=[_noop_reward_fn],\n            args=args,\n            train_dataset=train_dataset,\n            eval_dataset=eval_dataset,\n            processing_class=processing_class,\n            peft_config=peft_config,\n            **kwargs,\n        )\n\n        # Post-init: self.model now exists\n        self._load_directions()\n        self._act_cache = ActivationCache(self._reward_layers)\n        self._act_cache.register(self.model)\n\n        # Replace noop placeholder with actual DC-GRPO reward function\n        self.reward_funcs = [_DCRewardCallable(self)]\n        if hasattr(self, \"reward_func_names\"):\n            self.reward_func_names = [\"dc_grpo_reward\"]\n\n    # -----------------------------------------------------------------\n    # Direction loading\n    # -----------------------------------------------------------------\n\n    def _load_directions(self) -> None:\n        \"\"\"Load d_syc direction vectors from directions.pt.\"\"\"\n        if not self._direction_path:\n            logger.warning(\"No direction_path provided; R1/R2 will return 0.0\")\n            return\n        data = torch.load(\n            self._direction_path, map_location=\"cpu\", weights_only=True\n        )\n        self.d_syc = data[\"d_syc\"]  # (num_layers, 2, hidden_dim)\n        logger.info(\n            \"Loaded d_syc shape=%s from %s\",\n            self.d_syc.shape,\n            self._direction_path,\n        )\n\n    def reload_directions(self, path: str) -> None:\n        \"\"\"Hot-reload directions after periodic recalibration.\n\n        Logs a warning per layer if cosine similarity between old and new\n        directions drops below 0.7 (potential direction drift under LoRA).\n        \"\"\"\n        old_d = self.d_syc\n        self._direction_path = path\n        self._load_directions()\n\n        if old_d is not None and self.d_syc is not None:\n            for layer_idx in self._reward_layers:\n                if layer_idx >= min(old_d.shape[0], self.d_syc.shape[0]):\n                    continue\n                cos = F.cosine_similarity(\n                    old_d[layer_idx, self._pos_idx].unsqueeze(0),\n                    self.d_syc[layer_idx, self._pos_idx].unsqueeze(0),\n                ).item()\n                if cos < 0.7:\n                    logger.warning(\n                        \"Direction drift at layer %d: cosine=%.3f\", layer_idx, cos\n                    )\n\n    # -----------------------------------------------------------------\n    # NLI model (lazy)\n    # -----------------------------------------------------------------\n\n    def _ensure_nli_model(self) -> None:\n        \"\"\"Lazy-load DeBERTa NLI model for R3 scoring.\"\"\"\n        if self._nli_model is not None:\n            return\n        from transformers import (\n            AutoModelForSequenceClassification,\n            AutoTokenizer,\n        )\n\n        self._nli_tokenizer = AutoTokenizer.from_pretrained(self._r3_model_name)\n        self._nli_model = (\n            AutoModelForSequenceClassification.from_pretrained(self._r3_model_name)\n            .eval()\n        )\n        logger.info(\"Loaded NLI model: %s\", self._r3_model_name)\n\n    # -----------------------------------------------------------------\n    # Position finding\n    # -----------------------------------------------------------------\n\n    def _find_asst_first_positions(\n        self,\n        input_ids: torch.Tensor,\n        tokenizer: Any,\n    ) -> list[int]:\n        \"\"\"Locate asst_first position using tokenize-based method.\n\n        Matches extract_activations_v2.py: asst_first = len(prompt_tokens) - 1,\n        the last prompt token whose hidden state predicts the first generated\n        content token. Uses self._prompt_lengths when available (set by\n        generate_completions or _DCRewardCallable before calling this method).\n        Falls back to scanning for the <|im_start|> assistant marker.\n        \"\"\"\n        positions: list[int] = []\n        for i in range(input_ids.shape[0]):\n            seq_len = input_ids.shape[1]\n            if self._prompt_lengths and i < len(self._prompt_lengths):\n                pos = self._prompt_lengths[i] - 1\n            else:\n                im_start_id = tokenizer.convert_tokens_to_ids(\"<|im_start|>\")\n                ids_list = input_ids[i].tolist()\n                pos = seq_len - 1\n                for j in range(len(ids_list) - 1, -1, -1):\n                    if ids_list[j] == im_start_id:\n                        candidate = j + 2\n                        if candidate < seq_len:\n                            pos = candidate\n                        break\n            positions.append(min(pos, seq_len - 1))\n        return positions\n\n    # -----------------------------------------------------------------\n    # Activation extraction\n    # -----------------------------------------------------------------\n\n    def _extract_activations(\n        self,\n        input_ids: torch.Tensor,\n        attention_mask: torch.Tensor,\n        positions: list[int],\n    ) -> list[dict[int, torch.Tensor]]:\n        \"\"\"Forward pass to extract hidden states at asst_first positions.\n\n        Runs the full sequence through the model with hooks enabled, then\n        reads the cached hidden state at each sample's designated position.\n        This is a separate pass from generation (generate() uses KV cache\n        and only exposes the latest-token hidden state per step).\n\n        Args:\n            input_ids: (batch, seq_len) full sequences (prompt + completion).\n            attention_mask: (batch, seq_len).\n            positions: Per-sample token position for extraction.\n\n        Returns:\n            List of per-sample dicts: {layer_idx: Tensor(hidden_dim,)}.\n        \"\"\"\n        self._act_cache.clear()\n        with torch.no_grad():\n            self.model(input_ids=input_ids, attention_mask=attention_mask)\n\n        batch_acts: list[dict[int, torch.Tensor]] = []\n        for sample_idx, pos in enumerate(positions):\n            acts: dict[int, torch.Tensor] = {}\n            for layer_idx in self._reward_layers:\n                cached = self._act_cache.cache.get(layer_idx)\n                if cached is not None:\n                    acts[layer_idx] = cached[sample_idx, pos]\n            batch_acts.append(acts)\n\n        self._act_cache.clear()\n        return batch_acts\n\n    # -----------------------------------------------------------------\n    # R1: Direction Alignment\n    # -----------------------------------------------------------------\n\n    def compute_r1(\n        self,\n        activations: dict[int, torch.Tensor],\n        condition: str,\n    ) -> float:\n        \"\"\"Direction alignment reward for a single completion.\n\n        R1 = +dot(h, d_syc) for valid_correction   (reward genuine revision)\n        R1 = -dot(h, d_syc) for invalid_pressure    (penalize capitulation)\n\n        Direction vectors are L2-normalized per the compute_directions.py\n        convention, so dot product magnitude scales with activation norm\n        (stronger internal signal produces stronger reward).\n        Averaged across all reward_layers.\n\n        Args:\n            activations: {layer_idx: Tensor(hidden_dim,)} at asst_first position.\n            condition: \"valid_correction\" or \"invalid_pressure\".\n\n        Returns:\n            Scalar R1 reward.\n        \"\"\"\n        if self.d_syc is None:\n            return 0.0\n\n        sign = 1.0 if condition == \"valid_correction\" else -1.0\n        scores: list[float] = []\n        for layer_idx in self._reward_layers:\n            h = activations.get(layer_idx)\n            if h is None:\n                continue\n            d = self.d_syc[layer_idx, self._pos_idx].to(h)\n            scores.append(sign * torch.dot(h, d).item())\n\n        if not scores:\n            return 0.0\n        raw = sum(scores) / len(scores)\n        return torch.tanh(torch.tensor(raw / 20.0)).item()\n\n    def compute_r1_batch(\n        self,\n        batch_activations: list[dict[int, torch.Tensor]],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"R1 for a batch of completions.\"\"\"\n        return [\n            self.compute_r1(acts, cond)\n            for acts, cond in zip(batch_activations, conditions)\n        ]\n\n    # -----------------------------------------------------------------\n    # R2: Contrastive Consistency\n    # -----------------------------------------------------------------\n\n    def compute_r2(self, r1_valid: float, r1_invalid: float) -> float:\n        \"\"\"Rank-based contrastive reward for a condition pair.\n\n        R2 = sigmoid(R1_valid - R1_invalid) - 0.5\n\n        Positive when valid_correction R1 exceeds invalid_pressure R1 within\n        the same calibration pair. S1 rank-based design avoids the\n        d_gen = -d_syc degeneracy (see skeleton section 8).\n\n        Args:\n            r1_valid: R1 from the valid_correction completion.\n            r1_invalid: R1 from the invalid_pressure completion.\n\n        Returns:\n            Scalar R2 in (-0.5, 0.5).\n        \"\"\"\n        return torch.sigmoid(torch.tensor(r1_valid - r1_invalid)).item() - 0.5\n\n    def compute_r2_for_group(\n        self,\n        r1_scores: list[float],\n        conditions: list[str],\n        pair_ids: list[str],\n    ) -> list[float]:\n        \"\"\"R2 for all completions in a training step, paired by pair_id.\n\n        Aggregates mean R1 per (pair_id, condition), then applies R2.\n        All completions from the same pair receive the same R2 score.\n        Completions without a paired counterpart get R2 = 0.\n\n        Args:\n            r1_scores: R1 per completion (same order as conditions/pair_ids).\n            conditions: Per-completion condition label.\n            pair_ids: Per-completion pair identifier.\n\n        Returns:\n            List of R2 scores, same length as input.\n        \"\"\"\n        # Aggregate R1 by (pair_id, condition)\n        pair_r1: dict[str, dict[str, list[float]]] = {}\n        for r1, cond, pid in zip(r1_scores, conditions, pair_ids):\n            pair_r1.setdefault(pid, {}).setdefault(cond, []).append(r1)\n\n        pair_means: dict[str, dict[str, float]] = {}\n        for pid, cond_map in pair_r1.items():\n            pair_means[pid] = {\n                c: sum(vs) / len(vs) for c, vs in cond_map.items()\n            }\n\n        r2_scores: list[float] = []\n        for cond, pid in zip(conditions, pair_ids):\n            means = pair_means.get(pid, {})\n            r1_v = means.get(\"valid_correction\")\n            r1_i = means.get(\"invalid_pressure\")\n            if r1_v is not None and r1_i is not None:\n                r2_scores.append(self.compute_r2(r1_v, r1_i))\n            else:\n                r2_scores.append(0.0)\n        return r2_scores\n\n    # -----------------------------------------------------------------\n    # R3: Behavioral NLI\n    # -----------------------------------------------------------------\n\n    def compute_r3(\n        self,\n        completions: list[str],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"Behavioral NLI reward for a batch of completions.\n\n        Constructs (premise, hypothesis) pairs per completion:\n          premise:    \"The model said: {completion}\"\n          hypothesis: condition-dependent expected behavior\n\n        R3 = P(entailment) from DeBERTa-v3-base NLI.\n        Processed in batches of nli_batch_size. Does not participate\n        in gradient computation.\n\n        Args:\n            completions: Generated response texts.\n            conditions: Per-completion condition labels.\n\n        Returns:\n            List of R3 scores (entailment probabilities in [0, 1]).\n        \"\"\"\n        self._ensure_nli_model()\n\n        premises: list[str] = []\n        hypotheses: list[str] = []\n        for text, cond in zip(completions, conditions):\n            premises.append(f\"The model said: {text}\")\n            if cond == \"valid_correction\":\n                hypotheses.append(\n                    \"The model revised its answer after receiving valid correction.\"\n                )\n            else:\n                hypotheses.append(\n                    \"The model maintained its answer despite invalid pressure.\"\n                )\n\n        scores: list[float] = []\n        for i in range(0, len(premises), self._nli_batch_size):\n            batch_p = premises[i : i + self._nli_batch_size]\n            batch_h = hypotheses[i : i + self._nli_batch_size]\n            inputs = self._nli_tokenizer(\n                batch_p,\n                batch_h,\n                padding=True,\n                truncation=True,\n                max_length=512,\n                return_tensors=\"pt\",\n            ).to(self._nli_model.device)\n\n            with torch.no_grad():\n                logits = self._nli_model(**inputs).logits\n                probs = F.softmax(logits, dim=-1)\n                # DeBERTa NLI label order: contradiction=0, neutral=1, entailment=2\n                scores.extend(probs[:, 2].tolist())\n\n        return scores\n\n    # -----------------------------------------------------------------\n    # Combined reward\n    # -----------------------------------------------------------------\n\n    def compute_rewards(\n        self,\n        completions: list[str],\n        conditions: list[str],\n        pair_ids: list[str],\n        batch_activations: list[dict[int, torch.Tensor]],\n    ) -> tuple[list[float], dict[str, list[float]]]:\n        \"\"\"Compute combined R = w1*R1 + w2*R2 + w3*R3 for a batch.\n\n        Args:\n            completions: Generated response texts.\n            conditions: Per-completion condition labels.\n            pair_ids: Per-completion pair identifiers for R2 pairing.\n            batch_activations: Per-completion activation dicts from\n                _extract_activations.\n\n        Returns:\n            (combined_rewards, component_dict) where component_dict maps\n            \"r1\", \"r2\", \"r3\" to their respective score lists.\n        \"\"\"\n        r1 = self.compute_r1_batch(batch_activations, conditions)\n        r2 = self.compute_r2_for_group(r1, conditions, pair_ids)\n        r3 = self.compute_r3(completions, conditions)\n\n        combined = [\n            self._r1_w * s1 + self._r2_w * s2 + self._r3_w * s3\n            for s1, s2, s3 in zip(r1, r2, r3)\n        ]\n\n        components = {\"r1\": r1, \"r2\": r2, \"r3\": r3}\n        return combined, components\n\n    # -----------------------------------------------------------------\n    # GRPOTrainer override: generate_completions\n    # -----------------------------------------------------------------\n\n    def generate_completions(self, prompts, **kwargs):\n        \"\"\"Override to cache activations alongside standard generation.\n\n        Multi-turn prompts (3-turn dialogues formatted via chat template)\n        are handled natively by the parent's generation logic. After\n        completions are produced, a separate forward pass extracts hidden\n        states at the asst_first position for R1/R2 computation.\n\n        The extra forward pass adds ~5-10% overhead per training step.\n        Cached activations are stored in self._step_acts for retrieval\n        in _compute_step_rewards().\n        \"\"\"\n        tokenizer = self.processing_class\n        if isinstance(prompts, (list, tuple)) and len(prompts) > 0:\n            if isinstance(prompts[0], str):\n                self._prompt_lengths = [\n                    len(tokenizer.encode(p, add_special_tokens=False))\n                    for p in prompts\n                ]\n            elif isinstance(prompts[0], torch.Tensor):\n                pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\n                self._prompt_lengths = [\n                    (p != pad_id).sum().item() for p in prompts\n                ]\n\n        completions = super().generate_completions(prompts, **kwargs)\n\n        try:\n            if isinstance(prompts, (list, tuple)) and len(prompts) > 0:\n                if isinstance(prompts[0], str):\n                    comp_texts = (\n                        completions\n                        if isinstance(completions[0], str)\n                        else [tokenizer.decode(c, skip_special_tokens=False) for c in completions]\n                    )\n                    full_texts = [p + c for p, c in zip(prompts, comp_texts)]\n                    encoded = tokenizer(\n                        full_texts,\n                        padding=True,\n                        truncation=True,\n                        return_tensors=\"pt\",\n                    ).to(self.model.device)\n                    input_ids = encoded.input_ids\n                    attention_mask = encoded.attention_mask\n                elif isinstance(prompts[0], torch.Tensor):\n                    comp_ids = (\n                        completions\n                        if isinstance(completions, torch.Tensor)\n                        else torch.stack(completions)\n                    )\n                    input_ids = torch.cat(\n                        [torch.stack(prompts), comp_ids], dim=-1\n                    )\n                    pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id\n                    attention_mask = (input_ids != pad_id).long()\n                else:\n                    return completions\n\n                positions = self._find_asst_first_positions(\n                    input_ids, tokenizer\n                )\n                self._step_acts = self._extract_activations(\n                    input_ids, attention_mask, positions\n                )\n                self._extraction_failures = 0\n        except Exception as e:\n            self._step_acts = None\n            self._extraction_failures += 1\n            logger.warning(\n                \"Activation extraction failed (attempt %d): %s\",\n                self._extraction_failures,\n                e,\n            )\n            if self._extraction_failures >= 10:\n                raise RuntimeError(\n                    \"Activation extraction failed 10 consecutive times, aborting training\"\n                ) from e\n\n        return completions\n\n    # -----------------------------------------------------------------\n    # GRPOTrainer integration: step-level reward computation\n    # -----------------------------------------------------------------\n\n    def _compute_step_rewards(\n        self,\n        prompts: list[str],\n        completions: list[str],\n        conditions: list[str],\n        pair_ids: list[str],\n    ) -> list[float]:\n        \"\"\"Entry point for per-step reward computation.\n\n        Called during the training loop after generate_completions().\n        Reads self._step_acts (populated by generate_completions),\n        computes R1+R2+R3, logs component statistics, and clears the cache.\n\n        Wire this into the training loop by having the reward_funcs wrapper\n        delegate here, or by overriding _generate_and_score_completions\n        (TRL internal method name may vary by version).\n\n        Args:\n            prompts: Prompt texts for this step.\n            completions: Generated completion texts.\n            conditions: Per-completion condition labels from dataset.\n            pair_ids: Per-completion pair identifiers from dataset.\n\n        Returns:\n            List of combined reward scalars, one per completion.\n        \"\"\"\n        if self._step_acts is None:\n            logger.warning(\n                \"step_acts is None (extraction failed); returning zero rewards\"\n            )\n            return [0.0] * len(completions)\n\n        batch_acts = self._step_acts if self._step_acts else [{}] * len(completions)\n\n        rewards, components = self.compute_rewards(\n            completions, conditions, pair_ids, batch_acts\n        )\n\n        for name, values in components.items():\n            if values:\n                avg = sum(values) / len(values)\n                logger.info(\"reward/%s_mean=%.4f\", name, avg)\n        if rewards:\n            logger.info(\n                \"reward/combined_mean=%.4f\", sum(rewards) / len(rewards)\n            )\n\n        self._step_acts.clear()\n        return rewards\n\n    # -----------------------------------------------------------------\n    # Cleanup\n    # -----------------------------------------------------------------\n\n    def cleanup(self) -> None:\n        \"\"\"Remove hooks and free NLI model memory.\"\"\"\n        if self._act_cache is not None:\n            self._act_cache.remove()\n        self._nli_model = None\n        self._nli_tokenizer = None\n        torch.cuda.empty_cache()\nHEREDOC_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T13:02:27.450053+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T13:02:27.450205+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29046",
  "command": "grep -n \"\\.to(h)\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"tanh\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"_reward_step\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"step %d\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && wc -l /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29046",
    "command": "grep -n \"\\.to(h)\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"tanh\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"_reward_step\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && grep -n \"step %d\" /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py && echo \"---\" && wc -l /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T13:02:27.450343+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"460:            d = self.d_syc[layer_idx, self._pos_idx].to(h)\\n---\\n466:        return torch.tanh(torch.tensor(raw / 20.0)).item()\\n---\\n182:        t._reward_step += 1\\n183:        step = t._reward_step\\n264:        self._reward_step: int = 0\\n---\\n192:                        \\\"[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f\\\",\\n199:                    \\\"[step %d] reward/combined  mean=%.4f  std=%.4f\\\",\\n---\\n789 /root/mvp_v2_1_expanded/training/dcgrpo_trainer.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T13:02:27.450501+00:00_

同步完成。远程文件 789 行（本地 790 行，差 1 行是末尾换行差异，正常），四个关键修复点全部验证通过：

- `.to(h)` — 行 460
- `tanh` — 行 466
- `_reward_step` — 行 182/183/264
- `step %d` — 行 192/199

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_sync_dcgrpo_trainer_final_v2_20260518T125951"
}
```

</details>

---
