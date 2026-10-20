"""Evaluate GAR (Goal Attention Ratio) recovery after training.

Measures per-turn GAR across multi-turn conversations to assess whether
ThreadGate prevents the natural decay of goal-directed attention.
Supports both teacher-forced evaluation on held-out conversations and
built-in diagnostic conversations.
"""

import argparse
import json
import os
import sys

import torch
import torch.nn as nn
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForCausalLM

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from threadgate import TurnEmbedding, GateNetwork, UniformGateNetwork
from gar import GARMeasurer
from turn_utils import detect_turn_boundaries, build_turn_features
from config import MODEL_NAME


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


def _find_hf_model(model):
    if hasattr(model, "model") and hasattr(model.model, "layers"):
        return model
    try:
        inner = model.base_model.model
        if hasattr(inner, "model") and hasattr(inner.model, "layers"):
            return inner
    except AttributeError:
        pass
    raise ValueError("Cannot find HF model with .model.layers")


def load_model_for_eval(checkpoint_dir, gate_type, model_name, eval_data=False):
    """Load model + gates + measurer for GAR evaluation."""
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

    model.eval()

    hf_model = _find_hf_model(model)
    hidden_dim = hf_model.config.hidden_size
    num_layers = hf_model.config.num_hidden_layers

    gates = None
    turn_embedding = None
    hooks = []
    gate_values = {}

    if checkpoint_dir and gate_type in ("threadgate", "uniform"):
        gate_path = os.path.join(checkpoint_dir, "gate_params.pt")
        if os.path.exists(gate_path):
            if gate_type == "threadgate":
                turn_embedding = TurnEmbedding()
                gates = nn.ModuleList([
                    GateNetwork(hidden_dim, turn_embedding, init_bias=5.0)
                    for _ in range(num_layers)
                ])
            else:
                gates = nn.ModuleList([
                    UniformGateNetwork(hidden_dim, init_bias=5.0)
                    for _ in range(num_layers)
                ])

            gate_state = torch.load(gate_path, map_location="cpu", weights_only=True)
            gates.load_state_dict(gate_state["gates"])
            if gate_type == "threadgate" and "turn_embedding" in gate_state:
                turn_embedding.load_state_dict(gate_state["turn_embedding"])

            layers = hf_model.model.layers
            turn_features_ref = [None]

            for i, layer in enumerate(layers):
                device = next(layer.parameters()).device
                gates[i].to(device=device, dtype=torch.bfloat16)
            if turn_embedding is not None:
                device0 = next(layers[0].parameters()).device
                turn_embedding.to(device=device0, dtype=torch.bfloat16)

            def make_hook(layer_idx):
                def hook(module, input, output):
                    layer_input = input[0]
                    layer_output = output[0] if isinstance(output, tuple) else output
                    tf = turn_features_ref[0]
                    if gate_type == "threadgate" and tf is not None:
                        g = gates[layer_idx](layer_input, tf)
                    elif gate_type == "threadgate":
                        return output
                    else:
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
        else:
            turn_features_ref = [None]
    else:
        turn_features_ref = [None]

    measurer = GARMeasurer(hf_model, measure_only=True)

    return model, tokenizer, measurer, hooks, turn_features_ref, gate_values, num_layers


def measure_conversation_gar(model, tokenizer, measurer, messages, device,
                             turn_features_ref=None, gate_values=None,
                             gate_type="threadgate", gar_variant="ours",
                             gate_profile=False, num_layers=28):
    """Teacher-force a conversation and measure per-turn GAR."""
    full_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
    input_ids = tokenizer(full_text, return_tensors="pt").input_ids.squeeze(0)

    if input_ids.shape[0] > 2048:
        input_ids = input_ids[:2048]

    boundaries = detect_turn_boundaries(input_ids, tokenizer, gar_variant=gar_variant)
    goal_positions = boundaries["goal_token_positions"]
    assistant_positions = boundaries["assistant_last_token_positions"]

    if not goal_positions or len(assistant_positions) < 2:
        return None

    if gate_type == "threadgate" and turn_features_ref is not None:
        tf = build_turn_features(input_ids, tokenizer)
        turn_features_ref[0] = {
            k: v.to(device) if isinstance(v, torch.Tensor) else v
            for k, v in tf.items()
        }

    input_batch = input_ids.unsqueeze(0).to(device)

    with measurer.measure():
        with torch.no_grad():
            outputs = model(input_batch, output_attentions=True)

    gar_per_turn = []
    for pos in assistant_positions:
        result = measurer.compute_gar(goal_positions, [pos])
        gar_per_turn.append(result["mean_gar"])

    gate_profile_data = None
    if gate_profile and gate_values:
        gate_profile_data = {}
        for layer_idx in sorted(gate_values.keys()):
            g = gate_values[layer_idx]
            gate_profile_data[f"layer_{layer_idx}"] = {
                "mean": g.mean().item(),
                "std": g.std().item(),
            }

    ntp_loss = outputs.loss.item() if outputs.loss is not None else None
    ppl = np.exp(ntp_loss) if ntp_loss is not None else None

    return {
        "gar_per_turn": gar_per_turn,
        "gate_profile": gate_profile_data,
        "ntp_loss": ntp_loss,
        "ppl": ppl,
        "num_turns": len(assistant_positions),
    }


def plot_gar_comparison(baseline_gar, trained_gar, output_path, gate_type):
    """Plot baseline vs trained GAR curves."""
    fig, ax = plt.subplots(figsize=(8, 5))
    turns = range(1, len(baseline_gar) + 1)
    ax.plot(turns, baseline_gar[:len(turns)], 'o-', label='Base model', color='#888888')
    trained_turns = range(1, len(trained_gar) + 1)
    ax.plot(trained_turns, trained_gar[:len(trained_turns)], 's-', label=gate_type, color='#2196F3')
    ax.set_xlabel("Assistant Turn")
    ax.set_ylabel("GAR")
    ax.set_title("Goal Attention Ratio per Turn")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Evaluate GAR recovery")
    parser.add_argument("--checkpoint-dir", default=None)
    parser.add_argument("--gate-type", default="threadgate",
                        choices=["threadgate", "uniform", "baseline", "none"])
    parser.add_argument("--model", default=MODEL_NAME)
    parser.add_argument("--output-dir", default="./results/")
    parser.add_argument("--conversations-path", default=None,
                        help="JSON file with conversations for eval")
    parser.add_argument("--baseline-results", default="results/base_model_gar.json")
    parser.add_argument("--gar-variant", default="ours", choices=["ours", "dongre"])
    parser.add_argument("--gate-profile", action="store_true")
    parser.add_argument("--max-conversations", type=int, default=None)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    model, tokenizer, measurer, hooks, turn_features_ref, gate_values, num_layers = \
        load_model_for_eval(args.checkpoint_dir, args.gate_type, args.model)

    # Load conversations
    conversations_source = "hardcoded"
    if args.conversations_path and os.path.exists(args.conversations_path):
        with open(args.conversations_path) as f:
            conv_data = json.load(f)
        conversations = [c["messages"] for c in conv_data]
        conversations_source = args.conversations_path
    else:
        conversations = []
        for sys_prompt, user_qs in zip(SYSTEM_PROMPTS, CONVERSATIONS_DATA):
            msgs = [{"role": "system", "content": sys_prompt}]
            for q in user_qs:
                msgs.append({"role": "user", "content": q})
                msgs.append({"role": "assistant", "content": "(placeholder)"})
            conversations.append(msgs)

    if args.max_conversations:
        conversations = conversations[:args.max_conversations]

    print(f"\nEvaluating {len(conversations)} conversations...")

    all_gar_curves = []
    all_gate_profiles = []
    all_ppl = []
    all_ntp_loss = []

    for i, messages in enumerate(conversations):
        result = measure_conversation_gar(
            model, tokenizer, measurer, messages, device,
            turn_features_ref=turn_features_ref,
            gate_values=gate_values,
            gate_type=args.gate_type,
            gar_variant=args.gar_variant,
            gate_profile=args.gate_profile,
            num_layers=num_layers,
        )

        if result is None:
            continue

        all_gar_curves.append(result["gar_per_turn"])
        if result["gate_profile"]:
            all_gate_profiles.append(result["gate_profile"])
        if result["ppl"] is not None:
            all_ppl.append(result["ppl"])
            all_ntp_loss.append(result["ntp_loss"])

        if i % 10 == 0:
            gar_str = " ".join(f"{g:.4f}" for g in result["gar_per_turn"][:5])
            print(f"  Conv {i}: turns={result['num_turns']} GAR=[{gar_str} ...]")

    # Cleanup hooks
    for h in hooks:
        h.remove()

    if not all_gar_curves:
        print("No valid GAR data collected.")
        return

    # Compute averages
    min_turns = min(len(c) for c in all_gar_curves)
    max_turns = max(len(c) for c in all_gar_curves)
    avg_gar = []
    for t in range(max_turns):
        vals = [c[t] for c in all_gar_curves if t < len(c)]
        avg_gar.append(float(np.mean(vals)))

    turn1_gar = avg_gar[0] if avg_gar else 0.0
    mid_turns_gar = float(np.mean(avg_gar[2:8])) if len(avg_gar) > 2 else 0.0
    avg_ppl = float(np.mean(all_ppl)) if all_ppl else None
    avg_ntp_loss = float(np.mean(all_ntp_loss)) if all_ntp_loss else None

    print(f"\n{'='*50}")
    print(f"GAR Evaluation ({args.gate_type}, GAR-{args.gar_variant})")
    print(f"{'='*50}")
    print(f"Turn 1 avg GAR:     {turn1_gar:.4f}")
    print(f"Mid-turns avg GAR:  {mid_turns_gar:.4f}")
    if avg_ppl is not None:
        print(f"Avg PPL:            {avg_ppl:.2f}")

    # Save results
    ckpt_name = os.path.basename(args.checkpoint_dir.rstrip("/")) if args.checkpoint_dir else "base_model"
    if args.gar_variant == "dongre":
        ckpt_name += "_dongre"

    results = {
        "checkpoint_dir": args.checkpoint_dir,
        "gate_type": args.gate_type,
        "gar_variant": args.gar_variant,
        "model": args.model,
        "num_conversations": len(all_gar_curves),
        "avg_gar_per_turn": avg_gar,
        "turn1_avg_gar": turn1_gar,
        "mid_turns_avg_gar": mid_turns_gar,
        "conversations_source": conversations_source,
        "avg_ppl": avg_ppl,
        "avg_ntp_loss": avg_ntp_loss,
    }

    results_path = os.path.join(args.output_dir, f"{ckpt_name}_gar.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {results_path}")

    # Baseline comparison plot
    if os.path.exists(args.baseline_results):
        with open(args.baseline_results) as f:
            baseline = json.load(f)
        baseline_gar = baseline["avg_gar_per_turn"]
        plot_path = os.path.join(args.output_dir, f"{ckpt_name}_gar_comparison.png")
        plot_gar_comparison(baseline_gar, avg_gar, plot_path, args.gate_type)
        print(f"Plot saved to {plot_path}")


if __name__ == "__main__":
    main()
