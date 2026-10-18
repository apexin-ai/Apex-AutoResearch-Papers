# code wrapper rewrite from server source

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wrapper-rewrite-from-server-source_20260515T123209_result.json`
- **Structured JSON:** [`d3f6775217bcbcabcab2.json`](../../sessions/d3/d3f6775217bcbcabcab2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`IMMTotalLoss.__init__` accepts `lambda_margin, delta, warmup_steps, temperature, method` — and `train.py` passes exactly `k_ratio` (popped by the wrapper) plus these kwargs. The only extra param is `k_ratio` which the wrapper pops before passing to `IMMTotalLoss`. But wait — `train.py` also passes `selector_temperature`? Let me re-check.

Looking at `train.py`'s `wrap_with_imm`:
```python
imm_kwargs = {
    "lambda_margin": ..., "delta": ..., "warmup_steps": ...,
    "temperature": ..., "method": ..., "k_ratio": ...,
}
```

And in the wrapper's `__init__`:
```python
self.k_ratio = imm_config.pop("k_ratio", 0.5)
selector_temp = imm_config.pop("selector_temperature", 1.0)
self.imm_loss = IMMTotalLoss(**imm_config)
```

After popping `k_ratio`, the remaining keys are `lambda_margin, delta, warmup_steps, temperature, method` — all valid for `IMMTotalLoss`. `selector_temperature` is not in the dict so the pop defaults to 1.0. This is correct.

All verification passed. Here's the deliverable report:

---

## Deliverable Report

### 1. Server lerobot version
**lerobot 0.5.1** — module paths are `lerobot.policies.*` and `lerobot.datasets.*` (not `lerobot.common.*`).

### 2. `embed_image` existence
**Confirmed exists** at `SmolVLMWithExpertModel.embed_image()`. It runs `vision_model(pixel_values) → connector(hidden_states)` and returns `(B, N_patches, vlm_hidden_size)` visual token embeddings.

### 3. API differences found
| Item | Expected (old wrapper) | Actual (lerobot 0.5.1) |
|------|----------------------|----------------------|
| Import paths | `lerobot.common.policies.*` | `lerobot.policies.*` |
| `SmolVLAPolicy.forward` return | `dict` | `(loss, loss_dict)` tuple |
| `action_feature` | attribute | `@property` (depends on `output_features`) |
| `prefix_length` default | positive int | `-1` (no padding) |
| `add_image_special_tokens` default | True | False |
| `embed_prefix` scaling | none | `* sqrt(dim)` on image and language embeddings |
| `embed_suffix` | simple proj | `action_in_proj + sinusoidal_time → concat → action_time_mlp_in → SiLU → action_time_mlp_out` |

### 4. Design decisions
- **Auto-detect ACIS dimensions**: Reads `vlm_with_expert.config.text_config.hidden_size` (960) and `expert_hidden_size` (720) instead of hardcoding
- **Faithful `embed_prefix` replication**: `_build_prefix_with_vis_tokens` replicates the full prefix construction including optional special tokens, `sqrt(dim)` scaling, state projection, and att_mask convention (0=bidirectional, 1=causal)
- **prefix_length=-1 handling**: Padding block is naturally skipped since `shape[1] < -1` is always False
- **PeftModel unwrapping**: `_unwrap_to_vla` handles LoRA-wrapped models (`PeftModel → LoraModel → VLAFlowMatching`)
- **Mock classes**: Accurately mirror real dimensions (hidden=960, expert=720, action=32) and API surface for offline testing

### 5. Verification results
| Test | Status |
|------|--------|
| Import verification (`from imm.smolvla_wrapper import IMMSmolVLAWrapper`) | PASS |
| Mock test (`python -m imm.smolvla_wrapper`) | PASS — `total_loss=2.3318, k=64` |
| lerobot integration imports (`SmolVLAPolicy`, `SmolVLMWithExpertModel`) | PASS |
| `embed_image` attribute check | PASS |
| `train.py` + `evaluate.py` import chain | PASS |
| Config loading (`configs/imm_anchor.yaml`) | PASS — `imm.enabled=True` |
| `wrap_with_imm` constructor compatibility | PASS — `acis_config` / `imm_config` separation matches YAML structure |

No pretrained SmolVLA model weights are on disk, so the real end-to-end integration test (with actual VLM forward pass) was not run. That requires downloading `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` (~1GB).

---
