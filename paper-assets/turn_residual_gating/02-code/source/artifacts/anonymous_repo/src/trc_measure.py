"""TRC (Turn-level Representation Coherence) measurement.

Measures cosine similarity of adjacent assistant turns' final-layer hidden
states at their last content token positions.
"""

import torch
import torch.nn.functional as F
import numpy as np

from turn_utils import detect_turn_boundaries


def compute_trc(hidden_states_last, assistant_last_positions):
    if len(assistant_last_positions) < 2:
        return None

    vecs = hidden_states_last[0, assistant_last_positions, :].float()
    per_pair = []
    for i in range(len(assistant_last_positions) - 1):
        sim = F.cosine_similarity(vecs[i : i + 1], vecs[i + 1 : i + 2]).item()
        per_pair.append(sim)

    return {
        "per_pair": per_pair,
        "mean": float(np.mean(per_pair)),
        "std": float(np.std(per_pair)),
    }


def compute_tbp(logits, input_ids, turns):
    positions = [t["start"] for t in turns[1:] if t["start"] > 0]
    if not positions:
        return {"per_position": [], "mean": None, "ppl": None}

    ce_values = []
    for p in positions:
        logit = logits[0, p - 1].float()
        target = input_ids[0, p]
        ce = F.cross_entropy(logit.unsqueeze(0), target.unsqueeze(0)).item()
        ce_values.append(ce)

    mean_ce = float(np.mean(ce_values))
    return {
        "per_position": ce_values,
        "mean": mean_ce,
        "ppl": float(np.exp(mean_ce)),
    }


def measure_trc_and_tbp(model, tokenizer, messages, device, gate_ctx=None):
    full_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=False,
    )
    input_ids = tokenizer(full_text, return_tensors="pt").input_ids.squeeze(0)
    if input_ids.shape[0] > 2048:
        input_ids = input_ids[:2048]

    boundaries = detect_turn_boundaries(input_ids, tokenizer)
    assistant_positions = boundaries["assistant_last_token_positions"]

    if len(assistant_positions) < 2:
        return None

    if gate_ctx is not None and getattr(gate_ctx, "tracker", None) is not None:
        gate_ctx.tracker.prepare(
            input_ids, tokenizer, max_new_tokens=0, device=device
        )

    input_batch = input_ids.unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(input_batch, output_hidden_states=True)

    trc = compute_trc(outputs.hidden_states[-1], assistant_positions)
    tbp = compute_tbp(outputs.logits, input_batch, boundaries["turns"])

    return {
        "trc": trc,
        "tbp": tbp,
        "num_assistant_turns": len(assistant_positions),
    }
