#!/usr/bin/env python3
"""Extract hidden-state activations at critical turns from Qwen3-8B.

Input:  Phase 1 calibration JSONL — each line has fields:
        {id, condition, domain, evidence_strength, correction_turn, turns, ...}
        where turns = [{"role": "user"|"assistant", "content": "..."}, ...]
Output: activations.pt         — list[dict] with metadata + (num_layers, 2, hidden_dim) tensor
        activations_meta.jsonl  — metadata only (no tensors), for quick inspection
Deps:   transformers, torch, tqdm
"""

import argparse
import json
import logging
import sys
from pathlib import Path

import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)


def load_samples(path: str, max_samples: int | None = None) -> list[dict]:
    """Load calibration samples from JSONL file."""
    samples = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            samples.append(json.loads(line))
            if max_samples and len(samples) >= max_samples:
                break
    return samples


def _apply_template(tokenizer, messages: list[dict], **kwargs) -> list[int]:
    """apply_chat_template with Qwen3 thinking mode disabled when supported."""
    try:
        return tokenizer.apply_chat_template(
            messages, enable_thinking=False, tokenize=True, return_dict=False, **kwargs
        )
    except TypeError:
        return tokenizer.apply_chat_template(messages, tokenize=True, return_dict=False, **kwargs)


def find_critical_positions(
    tokenizer, turns: list[dict], correction_turn: int
) -> tuple[int, int, list[int]]:
    """Locate user-last-token and assistant-first-token positions in the tokenized conversation.

    Token boundary detection strategy:
      Step 1: Tokenize through end of the critical user turn                    -> ids_A
      Step 2: Tokenize same messages + assistant generation prompt              -> ids_B
      Step 3: Tokenize through end of the assistant response (the model input)  -> ids_C

      User last content token  = last token in ids_A before the trailing <|im_end|>
      Asst first content token = len(ids_B), i.e. right after the role marker

    Args:
        tokenizer: HuggingFace tokenizer with chat template.
        turns: Message list from the calibration sample.
        correction_turn: 1-indexed turn number of the critical user turn.
            turns[correction_turn - 1] is the user correction/challenge,
            turns[correction_turn]     is the assistant response.

    Returns:
        (user_last_pos, asst_first_pos, full_input_ids)
    """
    user_idx = len(turns) - 2
    asst_idx = len(turns) - 1

    if len(turns) < 2:
        raise ValueError(
            f"Need at least 2 turns, got {len(turns)}"
        )
    if turns[user_idx]["role"] != "user":
        raise ValueError(
            f"Expected user role at turn index {user_idx}, "
            f"got '{turns[user_idx]['role']}'"
        )

    msgs_through_user = [
        {"role": t["role"], "content": t["content"]} for t in turns[: user_idx + 1]
    ]
    msgs_through_asst = [
        {"role": t["role"], "content": t["content"]} for t in turns[: asst_idx + 1]
    ]

    # ids_A: ends with ...user_content <|im_end|> [\n]
    ids_through_user = _apply_template(
        tokenizer, msgs_through_user, add_generation_prompt=False
    )
    # ids_B: ids_A + assistant role marker tokens (<|im_start|> assistant \n)
    ids_with_gen = _apply_template(
        tokenizer, msgs_through_user, add_generation_prompt=True
    )
    # ids_C: full model input through assistant response
    ids_through_asst = _apply_template(
        tokenizer, msgs_through_asst, add_generation_prompt=False
    )

    # ---- User last content token ----
    # Scan backwards in ids_A for <|im_end|>; the token right before it is the last
    # content token of the user turn.
    im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    user_last_pos = None
    if im_end_id is not None and im_end_id != getattr(tokenizer, "unk_token_id", -1):
        for pos in range(len(ids_through_user) - 1, -1, -1):
            if ids_through_user[pos] == im_end_id:
                user_last_pos = pos - 1
                break
    if user_last_pos is None or user_last_pos < 0:
        user_last_pos = len(ids_through_user) - 1
        logger.warning(
            "Could not locate <|im_end|> in user turn; falling back to pos %d",
            user_last_pos,
        )

    # ---- Assistant first content token ----
    # ids_B = ids_A + role_marker_tokens.  ids_C should start with ids_B followed by
    # the assistant's content tokens and closing markers.
    # Verify prefix alignment before trusting the boundary.
    gen_len = len(ids_with_gen)
    if ids_through_asst[:gen_len] == ids_with_gen:
        asst_first_pos = gen_len
    else:
        # Fallback: the generation prompt may include extra tokens (e.g., <think> in
        # Qwen3 thinking mode) that are absent from the actual assistant message.
        # Estimate role-marker length by subtracting ids_A from ids_C and stripping
        # the known content + end tokens.
        logger.warning(
            "Generation-prompt prefix does not match full-sequence prefix; "
            "probing role-marker length with minimal assistant content"
        )
        probe_msgs = msgs_through_user + [{"role": "assistant", "content": "OK"}]
        ids_probe = _apply_template(tokenizer, probe_msgs, add_generation_prompt=False)
        ok_ids = tokenizer.encode("OK", add_special_tokens=False)
        # Probe structure after ids_through_user: role_marker + "OK" + <|im_end|> [+ \n]
        # role_marker_len = total_new_tokens - len(ok_ids) - num_end_tokens
        new_section = ids_probe[len(ids_through_user) :]
        # Count trailing end tokens (everything at/after the last <|im_end|>)
        end_count = 0
        if im_end_id is not None and im_end_id != getattr(tokenizer, "unk_token_id", -1):
            for tok in reversed(new_section):
                end_count += 1
                if tok == im_end_id:
                    break
        role_marker_len = len(new_section) - len(ok_ids) - end_count
        asst_first_pos = len(ids_through_user) + max(role_marker_len, 0)

    if not (0 <= user_last_pos < len(ids_through_asst)):
        raise ValueError(
            f"user_last_pos={user_last_pos} out of bounds (seq_len={len(ids_through_asst)})"
        )
    if not (0 <= asst_first_pos < len(ids_through_asst)):
        raise ValueError(
            f"asst_first_pos={asst_first_pos} out of bounds (seq_len={len(ids_through_asst)})"
        )

    return user_last_pos, asst_first_pos, ids_through_asst


def process_batch(
    model,
    tokenizer,
    samples: list[dict],
    device: torch.device,
) -> list[dict]:
    """Run a forward pass on a batch and extract per-sample activation tensors.

    Returns list of dicts, each containing metadata fields and an 'activations'
    tensor of shape (num_layers, 2, hidden_dim).
    """
    batch_positions = []
    batch_input_ids = []

    for sample in samples:
        user_pos, asst_pos, input_ids = find_critical_positions(
            tokenizer, sample["turns"], sample["correction_turn"]
        )
        batch_positions.append((user_pos, asst_pos))
        batch_input_ids.append(input_ids)

    # Right-pad to uniform length (causal mask ensures padding doesn't affect earlier positions)
    max_len = max(len(ids) for ids in batch_input_ids)
    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else 0

    padded_ids = []
    attention_masks = []
    for ids in batch_input_ids:
        pad_len = max_len - len(ids)
        padded_ids.append(ids + [pad_id] * pad_len)
        attention_masks.append([1] * len(ids) + [0] * pad_len)

    input_tensor = torch.tensor(padded_ids, dtype=torch.long, device=device)
    mask_tensor = torch.tensor(attention_masks, dtype=torch.long, device=device)

    with torch.no_grad():
        outputs = model(
            input_ids=input_tensor,
            attention_mask=mask_tensor,
            output_hidden_states=True,
        )

    # hidden_states is a tuple of (num_layers + 1) tensors:
    #   [0] = embedding output, [1..num_layers] = transformer layer outputs
    hidden_states = outputs.hidden_states[1:]  # skip embedding layer
    num_layers = len(hidden_states)

    results = []
    for i, sample in enumerate(samples):
        user_pos, asst_pos = batch_positions[i]

        layer_acts = []
        for layer_idx in range(num_layers):
            h = hidden_states[layer_idx]  # (batch, seq_len, hidden_dim)
            user_vec = h[i, user_pos, :]
            asst_vec = h[i, asst_pos, :]
            layer_acts.append(torch.stack([user_vec, asst_vec], dim=0))  # (2, hidden_dim)

        # (num_layers, 2, hidden_dim) — convert to float32 for downstream probing
        activations = torch.stack(layer_acts, dim=0).float().cpu()

        results.append({
            "pair_id": sample["id"],
            "condition": sample["condition"],
            "domain": sample["domain"],
            "evidence_strength": sample["evidence_strength"],
            "correction_turn": sample["correction_turn"],
            "activations": activations,
        })

    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract critical-turn hidden-state activations from Qwen3-8B."
    )
    parser.add_argument(
        "input", help="Path to calibration JSONL file (Phase 1 output)"
    )
    parser.add_argument(
        "--model-path",
        required=True,
        help="HuggingFace model ID or local path for Qwen3-8B",
    )
    parser.add_argument(
        "--output-dir", required=True, help="Directory for output files"
    )
    parser.add_argument(
        "--batch-size", type=int, default=4, help="Batch size (default: 4)"
    )
    parser.add_argument(
        "--device", default="cuda:0", help="Torch device (default: cuda:0)"
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        default=None,
        help="Process at most N samples (for debugging)",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    pt_path = out_dir / "activations.pt"
    meta_path = out_dir / "activations_meta.jsonl"

    logger.info("Loading samples from %s", args.input)
    samples = load_samples(args.input, args.max_samples)
    logger.info("Loaded %d samples", len(samples))
    if not samples:
        logger.error("No samples found in %s", args.input)
        sys.exit(1)

    device = torch.device(args.device)
    logger.info("Loading tokenizer from %s", args.model_path)
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    logger.info("Loading model from %s", args.model_path)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        torch_dtype=torch.bfloat16,
        device_map=args.device,
        trust_remote_code=True,
    )
    model.eval()

    all_results: list[dict] = []
    batch_size = args.batch_size
    pbar = tqdm(total=len(samples), desc="Extracting activations")
    i = 0

    while i < len(samples):
        batch = samples[i : i + batch_size]
        try:
            results = process_batch(model, tokenizer, batch, device)
            all_results.extend(results)
            pbar.update(len(batch))
            i += batch_size
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            if batch_size > 1:
                batch_size = max(1, batch_size // 2)
                logger.warning(
                    "CUDA OOM — reducing batch_size to %d and retrying", batch_size
                )
            else:
                logger.error(
                    "CUDA OOM with batch_size=1 at sample %d (id=%s); skipping",
                    i,
                    samples[i].get("id", "?"),
                )
                pbar.update(1)
                i += 1

    pbar.close()

    logger.info("Saving %d activation records to %s", len(all_results), pt_path)
    torch.save(all_results, pt_path)

    logger.info("Saving metadata to %s", meta_path)
    with open(meta_path, "w") as f:
        for r in all_results:
            meta = {k: v for k, v in r.items() if k != "activations"}
            meta["activation_shape"] = list(r["activations"].shape)
            f.write(json.dumps(meta, ensure_ascii=False) + "\n")

    if all_results:
        shape = all_results[0]["activations"].shape
        logger.info(
            "Done: %d samples, %d layers, hidden_dim=%d",
            len(all_results),
            shape[0],
            shape[2],
        )
    else:
        logger.warning("No activations extracted")


if __name__ == "__main__":
    main()
