import sys
import os
import json

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gar import GARMeasurer, compute_gar_loss
from turn_utils import detect_turn_boundaries
from config import MODEL_NAME


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    print(f"Loading model: {MODEL_NAME}")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        attn_implementation="eager",
        torch_dtype=torch.float16,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    with open("/root/turn_residual_gating/data/standard_conversations.json") as f:
        conversations = json.load(f)

    print(f"Loaded {len(conversations)} conversations")
    print("=" * 60)

    for conv_idx, conv in enumerate(conversations[:2]):
        messages = conv["messages"]
        print(f"\n{'='*60}")
        print(f"Conversation {conv_idx}: {len(messages)} messages, {conv.get('num_turns', '?')} turns")

        text = tokenizer.apply_chat_template(messages, tokenize=False)
        encoding = tokenizer(text, truncation=True, max_length=2048, return_tensors="pt")
        input_ids = encoding.input_ids.squeeze(0)
        print(f"Tokenized length: {len(input_ids)}")

        boundaries = detect_turn_boundaries(input_ids, tokenizer)
        goal_pos = boundaries["goal_token_positions"]
        assistant_pos = boundaries["assistant_last_token_positions"]

        print(f"Goal positions: {len(goal_pos)}")
        print(f"Assistant turns: {len(assistant_pos)}")

        if len(assistant_pos) < 2 or len(goal_pos) == 0:
            print("Not enough turns for GAR analysis, skipping.")
            continue

        measurer = GARMeasurer(model, measure_only=True)
        input_ids_device = input_ids.unsqueeze(0).to(device)

        with measurer.measure():
            with torch.no_grad():
                outputs = model(input_ids_device, output_attentions=True)

            result = measurer.compute_gar(goal_pos, assistant_pos)

        gar_values = result["gar_per_query"]
        for turn_idx, (pos, gar_val) in enumerate(zip(assistant_pos, gar_values)):
            print(f"  Turn {turn_idx}: GAR = {gar_val:.6f} (pos={pos})")

        print(f"\n--- Adjacent turn GAR differences ---")
        for i in range(1, len(gar_values)):
            diff = gar_values[i-1] - gar_values[i]
            loss_eps002 = max(0, diff - 0.02)
            loss_eps001 = max(0, diff - 0.001)
            print(f"  GAR(t{i-1}) - GAR(t{i}) = {diff:.6f}")
            print(f"    max(0, diff - 0.02)  = {loss_eps002:.6f}")
            print(f"    max(0, diff - 0.001) = {loss_eps001:.6f}")

        all_diffs = [gar_values[i-1] - gar_values[i] for i in range(1, len(gar_values))]
        print(f"\n  Max diff: {max(all_diffs):.6f}")
        print(f"  Min diff: {min(all_diffs):.6f}")
        print(f"  All diffs < 0.02: {all(d < 0.02 for d in all_diffs)}")
        print(f"  All diffs < 0.001: {all(d < 0.001 for d in all_diffs)}")

    print(f"\n{'='*60}")
    print("Verifying attention weight gradient chain...")

    conv = conversations[0]
    messages = conv["messages"]
    text = tokenizer.apply_chat_template(messages, tokenize=False)
    encoding = tokenizer(text, truncation=True, max_length=2048, return_tensors="pt")
    input_ids = encoding.input_ids.squeeze(0).to(device)

    measurer = GARMeasurer(model, measure_only=False)
    with measurer.measure():
        outputs = model(input_ids.unsqueeze(0), output_attentions=True)

    for layer_idx, attn_w in measurer._attention_weights.items():
        grad_info = attn_w.requires_grad if attn_w is not None else 'None'
        print(f"Layer {layer_idx}: requires_grad={grad_info}")
        if layer_idx >= 2:
            break

    print("\nDiagnosis complete.")


if __name__ == "__main__":
    main()
