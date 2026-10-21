"""Evaluate inference-time attention steering on GAR recovery.

Injects pre-softmax bias beta at goal-token positions and measures whether
GAR recovers from its inference-time collapse (~0.015 -> >0.1).

Modes:
  tf:  Teacher-forcing on pre-generated conversations. Same text, vary beta.
  gen: Generate conversations with beta active, then teacher-force to measure GAR.

Input:  model checkpoint + conversation data + beta values
Output: JSON with beta vs GAR vs PPL table
"""

import argparse
import json
import os
import sys

import torch
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import MODEL_NAME
from gar import GARMeasurer
from turn_utils import detect_turn_boundaries, build_turn_features
from attention_steering import AttentionSteering, _find_hf_model
from model_loader import load_gates, GateContext, TurnFeaturesTracker


CONVERSATIONS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "standard_conversations.json")

SYSTEM_PROMPTS = [
    "You are a knowledgeable science tutor. Always explain concepts step by step. Use analogies when possible. Never give direct answers without explanation. If the student makes an error, gently correct them and guide them to the right answer.",
    "You are a professional code reviewer. Focus on code quality, security, and performance. Point out potential bugs and suggest improvements. Always explain why a change is needed, not just what to change. Be constructive and specific.",
    "You are a creative writing coach. Help users improve their storytelling skills. Focus on character development, plot structure, and vivid descriptions. Give specific feedback with examples. Encourage experimentation with different styles.",
    "You are a math problem solver. Show all steps clearly. Explain the reasoning behind each step. If there are multiple approaches, mention them. Check your work by verifying the answer. Use LaTeX notation for formulas.",
    "You are a debate coach who helps users argue both sides of issues. Present balanced perspectives. Challenge weak arguments constructively. Teach logical reasoning and evidence evaluation. Avoid personal opinions.",
]

CONVERSATIONS_DATA = [
    ["Why is the sky blue?", "What about sunsets being red?", "How does a rainbow form?",
     "Why do stars twinkle?", "What causes thunder?", "How do magnets work?",
     "Why is water wet?", "What is gravity?", "How do airplanes fly?", "Why is space dark?"],
    ["Review this: def add(a,b): return a+b", "What about error handling?", "How should I write tests for it?",
     "Is recursion better than iteration?", "When should I use async/await?", "How to handle memory leaks?",
     "Best practices for API design?", "How to optimize database queries?", "When to use microservices?", "How to handle rate limiting?"],
    ["Help me start a mystery story", "How do I create a compelling villain?", "What makes good dialogue?",
     "How to build suspense?", "Should I use first or third person?", "How to write a plot twist?",
     "Tips for describing settings?", "How to end a chapter with a cliffhanger?", "How to avoid cliches?", "How to write an epilogue?"],
    ["Solve: 3x + 7 = 22", "What is the derivative of x^3?", "Explain the Pythagorean theorem",
     "What is a prime number?", "How to calculate compound interest?", "What is the area of a circle?",
     "Explain matrix multiplication", "What is a logarithm?", "How to solve quadratic equations?", "What is calculus used for?"],
    ["Should AI be regulated?", "Is remote work better than office work?", "Should college be free?",
     "Is social media harmful?", "Should voting be mandatory?", "Is nuclear energy safe?",
     "Should animals have legal rights?", "Is space exploration worth the cost?", "Should there be a universal basic income?", "Is genetic engineering ethical?"],
]


def load_model_eager(model_name, checkpoint_dir, gate_type):
    """Load model with eager attention, LoRA adapter, and gate hooks.

    Uses TurnFeaturesTracker-based hooks so the same setup works for both
    teacher-forcing (tracker.prepare with max_new_tokens=0) and autoregressive
    generation (tracker.prepare with max_new_tokens>0).
    """
    from transformers import AutoTokenizer, AutoModelForCausalLM

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        attn_implementation="eager",
    )

    if checkpoint_dir:
        lora_path = os.path.join(checkpoint_dir, "lora")
        if os.path.isdir(lora_path):
            from peft import PeftModel
            model = PeftModel.from_pretrained(model, lora_path)
            print(f"  Loaded LoRA from {lora_path}")

    model.eval()

    if gate_type in ("none", "baseline") or not checkpoint_dir:
        return model, tokenizer, GateContext([], gate_type)

    hf_model = _find_hf_model(model)
    hidden_dim = hf_model.config.hidden_size
    num_layers = hf_model.config.num_hidden_layers

    gate_path = os.path.join(checkpoint_dir, "gate_params.pt")
    if not os.path.exists(gate_path):
        print(f"  WARNING: gate_params.pt not found, running without gates")
        return model, tokenizer, GateContext([], gate_type)

    gates, turn_embedding = load_gates(checkpoint_dir, gate_type, hidden_dim, num_layers)

    layers = hf_model.model.layers
    hooks = []
    gate_values = {}
    model_device = next(layers[0].parameters()).device

    for i in range(num_layers):
        gates[i].to(device=model_device, dtype=torch.bfloat16)
    if gate_type == "threadgate" and turn_embedding is not None:
        turn_embedding.to(device=model_device, dtype=torch.bfloat16)

    tracker = TurnFeaturesTracker(num_layers) if gate_type == "threadgate" else None

    if gate_type == "threadgate":
        def make_hook(layer_idx):
            def hook(module, input, output):
                if tracker.full_td is None:
                    return output
                layer_input = input[0]
                layer_output = output[0] if isinstance(output, tuple) else output
                tf = tracker.get_features(layer_input.shape[1], layer_idx)
                g = gates[layer_idx](layer_input, tf)
                f_x = layer_output - layer_input
                gated = layer_input + g * f_x
                gate_values[layer_idx] = g.detach()
                if isinstance(output, tuple):
                    return (gated,) + output[1:]
                return gated
            return hook
    else:
        def make_hook(layer_idx):
            def hook(module, input, output):
                layer_input = input[0]
                layer_output = output[0] if isinstance(output, tuple) else output
                g = gates[layer_idx](layer_input)
                f_x = layer_output - layer_input
                gated = layer_input + g * f_x
                gate_values[layer_idx] = g.detach()
                if isinstance(output, tuple):
                    return (gated,) + output[1:]
                return gated
            return hook

    for i, layer in enumerate(layers):
        hooks.append(layer.register_forward_hook(make_hook(i)))

    print(f"  Loaded {gate_type} gates from {gate_path}")

    return model, tokenizer, GateContext(
        hooks, gate_type, tracker=tracker, gate_values=gate_values,
    )


def load_conversations(path):
    with open(path) as f:
        data = json.load(f)
    return [conv["messages"] for conv in data]



def load_gen_data_from_file(path, max_convs=None):
    """Load conversations from external JSON for gen mode.
    Returns list of (sys_prompt, user_questions) tuples.
    Format: list of dicts with "messages" containing role/content pairs.
    Conversations without a system message get a default system prompt.
    """
    with open(path) as f:
        data = json.load(f)
    if max_convs is not None:
        data = data[:max_convs]

    DEFAULT_SYS_PROMPT = "You are a helpful assistant."
    result = []
    for conv in data:
        messages = conv["messages"]
        sys_prompt = DEFAULT_SYS_PROMPT
        user_qs = []
        for msg in messages:
            if msg["role"] == "system":
                sys_prompt = msg["content"]
            elif msg["role"] == "user":
                user_qs.append(msg["content"])
        if user_qs:
            result.append((sys_prompt, user_qs))
    return result


def measure_gar_and_ppl(model, tokenizer, hf_model, measurer, gate_ctx,
                         messages, beta, device, gar_variant="ours",
                         layer_range=None):
    """Teacher-force a conversation with steering at given beta, measure GAR and PPL."""
    full_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=False,
    )
    input_ids = tokenizer(full_text, return_tensors="pt").input_ids.squeeze(0)
    if input_ids.shape[0] > 2048:
        input_ids = input_ids[:2048]

    boundaries = detect_turn_boundaries(input_ids, tokenizer, gar_variant=gar_variant)
    goal_positions = boundaries["goal_token_positions"]
    if gar_variant == "dongre":
        query_groups = boundaries["assistant_all_token_positions"]
    else:
        query_groups = [[p] for p in boundaries["assistant_last_token_positions"]]

    if not goal_positions or not query_groups:
        return None

    # Prepare gate turn features for teacher-forcing (max_new_tokens=0)
    if gate_ctx.tracker is not None:
        gate_ctx.tracker.prepare(input_ids, tokenizer, max_new_tokens=0, device=device)

    steering = AttentionSteering(model, beta, goal_positions, layer_range=layer_range)
    steering.activate()

    input_batch = input_ids.unsqueeze(0).to(device)

    # Labels: only compute loss on assistant tokens
    labels = torch.full_like(input_batch, -100)
    for turn in boundaries["turns"]:
        if turn["role"] == "assistant":
            labels[0, turn["content_start"]:turn["content_end"]] = \
                input_batch[0, turn["content_start"]:turn["content_end"]]

    # Single forward for both GAR (via measurer hooks) and PPL (via labels)
    with measurer.measure():
        with torch.no_grad():
            outputs = model(input_batch, labels=labels, output_attentions=True)

    gar_per_turn = []
    for qpositions in query_groups:
        result = measurer.compute_gar(goal_positions, qpositions)
        gar_per_turn.append(result["mean_gar"])

    ntp_loss = outputs.loss.item() if outputs.loss is not None else None
    ppl = float(np.exp(ntp_loss)) if ntp_loss is not None else None

    steering.deactivate()

    return {
        "gar_per_turn": gar_per_turn,
        "num_turns": len(gar_per_turn),
        "ppl": ppl,
        "ntp_loss": ntp_loss,
        "num_goal_tokens": len(goal_positions),
    }


def generate_conversation(model, tokenizer, gate_ctx, sys_prompt, user_qs,
                           beta, goal_positions, device, layer_range=None,
                           max_new_tokens=100):
    """Generate a multi-turn conversation with attention steering active."""
    steering = AttentionSteering(model, beta, goal_positions, layer_range=layer_range)
    steering.activate()

    messages = [{"role": "system", "content": sys_prompt}]
    for q in user_qs:
        messages.append({"role": "user", "content": q})
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )
        input_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)

        if input_ids.shape[1] > 1800:
            messages.pop()
            break

        gate_ctx.prepare_generation(input_ids, tokenizer, max_new_tokens, device)

        with torch.no_grad():
            output = model.generate(
                input_ids, max_new_tokens=max_new_tokens, do_sample=False,
            )

        new_tokens = output[0][input_ids.shape[1]:]
        response = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        messages.append({"role": "assistant", "content": response})

    steering.deactivate()
    return messages


def get_initial_goal_positions(tokenizer, sys_prompt, first_user_q, gar_variant="ours"):
    """Compute goal token positions from system prompt + first user message."""
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": first_user_q},
    ]
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True,
    )
    input_ids = tokenizer(text, return_tensors="pt").input_ids.squeeze(0)
    boundaries = detect_turn_boundaries(input_ids, tokenizer, gar_variant=gar_variant)
    return boundaries["goal_token_positions"]


def main():
    parser = argparse.ArgumentParser(
        description="Attention steering GAR evaluation",
    )
    parser.add_argument("--model", default=MODEL_NAME)
    parser.add_argument("--checkpoint", default=None,
                        help="Checkpoint dir with LoRA + gates")
    parser.add_argument("--gate-type", default="threadgate",
                        choices=["threadgate", "uniform", "none", "baseline"])
    parser.add_argument("--mode", default="tf", choices=["tf", "gen"],
                        help="tf=teacher-forcing on existing convs, gen=generate then measure")
    parser.add_argument("--conversations", default=CONVERSATIONS_PATH,
                        help="Pre-generated conversations JSON (for tf mode)")
    parser.add_argument("--data-dir", default=None,
                        help="Data directory (reserved for future use)")
    parser.add_argument("--data-file", default=None,
                        help="External conversation JSON for gen mode (overrides hardcoded prompts)")
    parser.add_argument("--max-convs", type=int, default=None,
                        help="Max conversations to use (default: all)")
    parser.add_argument("--conversations-source", default="dataset",
                        choices=["dataset", "hardcoded"],
                        help="Gen mode data source: 'dataset' loads from UltraChat heldout (default), 'hardcoded' uses built-in prompts")
    parser.add_argument("--beta", nargs="+", type=float,
                        default=[0.0, 0.5, 1.0, 2.0, 5.0, 10.0])
    parser.add_argument("--gar-variant", default="ours", choices=["ours", "dongre"])
    parser.add_argument("--layer-range", nargs=2, type=int, default=None,
                        metavar=("START", "END"),
                        help="Only steer layers [START, END)")
    parser.add_argument("--n-convs", type=int, default=5)
    parser.add_argument("--output-dir",
                        default="results/attention_steering/")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-name", default=None, help="Custom output filename (without .json)")
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Ensure beta=0 baseline is always included
    if 0.0 not in args.beta:
        args.beta = [0.0] + args.beta

    print("Loading model (eager attention)...")
    model, tokenizer, gate_ctx = load_model_eager(
        args.model, args.checkpoint, args.gate_type,
    )
    hf_model = _find_hf_model(model)
    measurer = GARMeasurer(hf_model)

    print(f"Device: {device}")
    print(f"Gate type: {args.gate_type}")
    print(f"Mode: {args.mode}")
    print(f"Beta values: {args.beta}")
    if args.layer_range:
        print(f"Layer range: [{args.layer_range[0]}, {args.layer_range[1]})")

    layer_range = tuple(args.layer_range) if args.layer_range else None
    gen_data = None
    if args.mode == "gen":
        if args.data_file:
            gen_data = load_gen_data_from_file(args.data_file, args.max_convs)
            print(f"Loaded {len(gen_data)} conversations from {args.data_file}")
        elif args.conversations_source == "dataset":
            dataset_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "data", "ultrachat_eval_heldout.json",
            )
            gen_data = load_gen_data_from_file(dataset_path, args.max_convs)
            print(f"Loaded {len(gen_data)} conversations from ultrachat_eval_heldout.json")

        if gen_data is not None:
            n_convs = len(gen_data)
        else:
            n_convs = min(args.n_convs, len(SYSTEM_PROMPTS))
    else:
        n_convs = args.n_convs

    # Load conversations for TF mode
    if args.mode == "tf":
        if os.path.exists(args.conversations):
            print(f"Loading conversations from {args.conversations}")
            conversations = load_conversations(args.conversations)[:n_convs]
        else:
            print(f"ERROR: {args.conversations} not found for TF mode")
            sys.exit(1)
        print(f"  {len(conversations)} conversations loaded")

    all_results = {}

    for beta in args.beta:
        print(f"\n{'='*50}")
        print(f"Beta = {beta}")
        print(f"{'='*50}")

        beta_gar_curves = []
        beta_ppl = []

        if args.mode == "tf":
            for i, messages in enumerate(conversations):
                result = measure_gar_and_ppl(
                    model, tokenizer, hf_model, measurer, gate_ctx,
                    messages, beta, device,
                    gar_variant=args.gar_variant, layer_range=layer_range,
                )
                if result:
                    gar_str = " ".join(f"{g:.4f}" for g in result["gar_per_turn"])
                    ppl_str = f"PPL={result['ppl']:.2f}" if result["ppl"] else ""
                    print(f"  Conv {i+1}: GAR=[{gar_str}]  {ppl_str}")
                    beta_gar_curves.append(result["gar_per_turn"])
                    if result["ppl"] is not None:
                        beta_ppl.append(result["ppl"])
                else:
                    print(f"  Conv {i+1}: no valid GAR positions")

        else:  # model-gen
            for i in range(n_convs):
                if gen_data is not None:
                    sys_prompt, user_qs = gen_data[i]
                else:
                    sys_prompt = SYSTEM_PROMPTS[i]
                    user_qs = CONVERSATIONS_DATA[i]
                print(f"  Conv {i+1}/{n_convs}: generating...")

                goal_positions = get_initial_goal_positions(
                    tokenizer, sys_prompt, user_qs[0],
                    gar_variant=args.gar_variant,
                )

                messages = generate_conversation(
                    model, tokenizer, gate_ctx, sys_prompt, user_qs,
                    beta, goal_positions, device, layer_range=layer_range,
                )
                num_turns = sum(1 for m in messages if m["role"] == "assistant")
                print(f"    {num_turns} turns generated")

                # Teacher-force the generated conversation to measure GAR
                result = measure_gar_and_ppl(
                    model, tokenizer, hf_model, measurer, gate_ctx,
                    messages, beta, device,
                    gar_variant=args.gar_variant, layer_range=layer_range,
                )
                if result:
                    gar_str = " ".join(f"{g:.4f}" for g in result["gar_per_turn"])
                    ppl_str = f"PPL={result['ppl']:.2f}" if result["ppl"] else ""
                    print(f"    GAR=[{gar_str}]  {ppl_str}")
                    beta_gar_curves.append(result["gar_per_turn"])
                    if result["ppl"] is not None:
                        beta_ppl.append(result["ppl"])
                else:
                    print(f"    WARNING: no valid GAR")

        # Aggregate results for this beta
        if beta_gar_curves:
            # Per-turn average (legacy, kept for backward compat)
            max_turns = max(len(c) for c in beta_gar_curves)
            padded_avg_gar = []
            for t in range(max_turns):
                vals = [c[t] for c in beta_gar_curves if t < len(c)]
                padded_avg_gar.append(float(np.mean(vals)))
            avg_gar = padded_avg_gar

            # Per-conversation mid_gar: only convs with >= 3 turns
            per_conv_mid_gar = []
            for curve in beta_gar_curves:
                if len(curve) >= 3:
                    per_conv_mid_gar.append(float(np.mean(curve[2:min(8, len(curve))])))

            if per_conv_mid_gar:
                mid_gar = float(np.mean(per_conv_mid_gar))
                mid_gar_std = float(np.std(per_conv_mid_gar))
                n_valid = len(per_conv_mid_gar)
            else:
                mid_gar = float('nan')
                mid_gar_std = float('nan')
                n_valid = 0
        else:
            avg_gar = []
            mid_gar = 0.0
            mid_gar_std = 0.0
            n_valid = 0
            per_conv_mid_gar = []

        avg_ppl = float(np.mean(beta_ppl)) if beta_ppl else None

        print(f"\n  Avg GAR (padded): {[f'{g:.4f}' for g in avg_gar[:10]]}")
        print(f"  Mid-GAR (per-conv): {mid_gar:.4f} ± {mid_gar_std:.4f}  (n={n_valid}/{len(beta_gar_curves)})")
        if avg_ppl:
            print(f"  Avg PPL: {avg_ppl:.2f}")

        all_results[f"beta_{beta}"] = {
            "beta": beta,
            "avg_gar_per_turn": avg_gar,
            "mid_turns_avg_gar": mid_gar,
            "mid_gar_std": mid_gar_std,
            "n_valid_convs": n_valid,
            "per_conv_mid_gar": per_conv_mid_gar,
            "avg_ppl": avg_ppl,
            "gar_curves": beta_gar_curves,
            "ppl_per_conversation": beta_ppl,
        }

    # Cleanup gate hooks
    gate_ctx.cleanup()

    # Summary table
    print(f"\n{'='*60}")
    print(f"  ATTENTION STEERING RESULTS ({args.gate_type}, GAR-{args.gar_variant})")
    print(f"{'='*60}")
    print(f"{'Beta':>8} | {'Mid-GAR':>10} | {'PPL':>8}")
    print(f"{'-'*40}")
    for key in sorted(all_results.keys(), key=lambda k: all_results[k]["beta"]):
        r = all_results[key]
        ppl_str = f"{r['avg_ppl']:.2f}" if r["avg_ppl"] else "N/A"
        print(f"{r['beta']:8.1f} | {r['mid_turns_avg_gar']:10.4f} | {ppl_str:>8}")

    # Save results
    ckpt_name = os.path.basename(args.checkpoint.rstrip("/")) if args.checkpoint else "base_model"
    output = {
        "checkpoint": args.checkpoint,
        "gate_type": args.gate_type,
        "mode": args.mode,
        "gar_variant": args.gar_variant,
        "model": args.model,
        "layer_range": args.layer_range,
        "betas": args.beta,
        "conversations_source": args.data_file if (args.mode == "gen" and args.data_file) else (
            "ultrachat_eval_heldout" if (args.mode == "gen" and gen_data is not None) else (
                args.conversations if args.mode == "tf" else "hardcoded"
            )
        ),
        "num_conversations": n_convs,
        "results": all_results,
    }

    fname = f"{args.output_name}.json" if args.output_name else f"{ckpt_name}_attention_steering.json"
    output_path = os.path.join(args.output_dir, fname)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
