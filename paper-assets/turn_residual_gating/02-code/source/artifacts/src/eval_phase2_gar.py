# eval_phase2_gar.py — 评估训练后模型的 GAR 恢复效果
# 用法: python eval_phase2_gar.py --checkpoint-dir /root/turn_residual_gating/checkpoints/tg_s42 --gate-type threadgate
# GAR-Dongre 模式: python eval_phase2_gar.py --checkpoint-dir ... --gate-type threadgate --gar-variant dongre
# 输出: JSON 结果 + GAR 对比曲线图

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
    """Find the HF CausalLM model (with .model.layers) in the model hierarchy."""
    if hasattr(model, "model") and hasattr(model.model, "layers"):
        return model
    try:
        inner = model.base_model.model
        if hasattr(inner, "model") and hasattr(inner.model, "layers"):
            return inner
    except AttributeError:
        pass
    raise ValueError("Cannot find HF model with .model.layers in hierarchy")


def _find_layers(model):
    return _find_hf_model(model).model.layers


def _extract_per_turn_gates(gate_values, turns):
    num_layers = len(gate_values)
    result = {}
    for t_idx, turn in enumerate(turns):
        start = turn["content_start"]
        end = turn["content_end"]
        if end <= start:
            continue
        turn_key = f"turn_{t_idx + 1}"
        layer_gates = {}
        for layer_idx in range(num_layers):
            g = gate_values[layer_idx]
            turn_g = g[0, start:end, 0].float()
            layer_gates[f"L{layer_idx}"] = round(float(turn_g.mean().item()), 4)
        result[turn_key] = layer_gates
    return result


def _compute_gate_dynamic_range(all_gate_profiles, num_layers):
    dynamic_range = {}
    for layer_idx in range(num_layers):
        lk = f"L{layer_idx}"
        first_vals = []
        last_vals = []
        last_turn_num = 0
        for profile in all_gate_profiles:
            turn_keys = sorted(profile.keys(), key=lambda k: int(k.split("_")[1]))
            if len(turn_keys) >= 2:
                first_vals.append(profile[turn_keys[0]][lk])
                last_vals.append(profile[turn_keys[-1]][lk])
                last_turn_num = max(last_turn_num, int(turn_keys[-1].split("_")[1]))
        if first_vals and last_vals:
            avg_f = round(float(np.mean(first_vals)), 4)
            avg_l = round(float(np.mean(last_vals)), 4)
            dynamic_range[lk] = {
                "turn1": avg_f,
                f"turn{last_turn_num}": avg_l,
                "diff": round(avg_f - avg_l, 4),
            }
    return dynamic_range


def load_gates(checkpoint_dir, gate_type, hidden_dim, num_layers):
    """Load gate networks and trained parameters from checkpoint."""
    if gate_type == "threadgate":
        turn_embedding = TurnEmbedding()
        gates = nn.ModuleList([
            GateNetwork(hidden_dim, turn_embedding, init_bias=5.0)
            for _ in range(num_layers)
        ])
    else:
        turn_embedding = None
        gates = nn.ModuleList([
            UniformGateNetwork(hidden_dim, init_bias=5.0)
            for _ in range(num_layers)
        ])

    gate_path = os.path.join(checkpoint_dir, "gate_params.pt")
    if not os.path.exists(gate_path):
        raise FileNotFoundError(f"Gate parameters not found: {gate_path}")
    gate_state = torch.load(gate_path, map_location="cpu", weights_only=True)
    gates.load_state_dict(gate_state["gates"])
    if gate_type == "threadgate" and "turn_embedding" in gate_state:
        turn_embedding.load_state_dict(gate_state["turn_embedding"])

    return gates, turn_embedding


def register_gating_hooks(model, gates, gate_type, turn_embedding=None, device=None):
    """Register forward hooks on transformer layers for residual gating."""
    layers = _find_layers(model)
    hooks = []
    gate_values = {}
    turn_features_ref = [None]

    if device is None:
        device = next(layers[0].parameters()).device

    for i in range(len(layers)):
        gates[i].to(device=device, dtype=torch.bfloat16)
    if gate_type == "threadgate" and turn_embedding is not None:
        turn_embedding.to(device=device, dtype=torch.bfloat16)

    def make_hook(layer_idx):
        def hook(module, input, output):
            if gate_type == "threadgate" and turn_features_ref[0] is None:
                return output

            layer_input = input[0]
            layer_output = output[0] if isinstance(output, tuple) else output

            if gate_type == "threadgate":
                g = gates[layer_idx](layer_input, turn_features_ref[0])
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

    return hooks, turn_features_ref, gate_values


def build_conversation(tokenizer, model, system_prompt, user_questions, device, max_new_tokens=100):
    """Generate a multi-turn conversation (same logic as Phase 1)."""
    messages = [{"role": "system", "content": system_prompt}]
    for q in user_questions:
        messages.append({"role": "user", "content": q})
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        input_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)

        if input_ids.shape[1] > 1800:
            messages.pop()
            break

        with torch.no_grad():
            output = model.generate(input_ids, max_new_tokens=max_new_tokens, do_sample=False)

        new_tokens = output[0][input_ids.shape[1]:]
        response = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        messages.append({"role": "assistant", "content": response})

    return messages


def measure_gar_per_turn(model, tokenizer, measurer, messages, device, turn_features_ref, gate_type, gar_variant="ours", gate_values_ref=None, gate_profile=False):
    """Measure GAR at each assistant turn with gating active."""
    full_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
    input_ids = tokenizer(full_text, return_tensors="pt").input_ids.squeeze(0)

    if input_ids.shape[0] > 2048:
        input_ids = input_ids[:2048]

    boundaries = detect_turn_boundaries(input_ids, tokenizer, gar_variant=gar_variant)
    goal_positions = boundaries["goal_token_positions"]
    assistant_positions = boundaries["assistant_last_token_positions"]

    if not goal_positions or not assistant_positions:
        return None

    if gate_type == "threadgate":
        tf = build_turn_features(input_ids, tokenizer)
        turn_features_ref[0] = {
            "turn_distance": tf["turn_distance"].to(device),
            "turn_index": tf["turn_index"].to(device),
        }

    input_ids_batch = input_ids.unsqueeze(0).to(device)

    with measurer.measure():
        with torch.no_grad():
            model(input_ids_batch, output_attentions=True)

    per_turn_gates = None
    if gate_profile and gate_values_ref:
        per_turn_gates = _extract_per_turn_gates(gate_values_ref, boundaries["turns"])

    turn_features_ref[0] = None

    gar_per_turn = []
    normalized_gar_per_turn = []
    visible_tokens_per_turn = []
    num_goal_tokens = len(goal_positions)

    if gar_variant == "dongre":
        # Dongre: query = all response tokens per turn
        for turn_token_positions in boundaries["assistant_all_token_positions"]:
            result = measurer.compute_gar(goal_positions, turn_token_positions)
            raw_gar = result["mean_gar"]
            gar_per_turn.append(raw_gar)

            last_pos = turn_token_positions[-1]
            num_visible = last_pos + 1
            visible_tokens_per_turn.append(num_visible)

            if num_goal_tokens > 0:
                norm_gar = raw_gar * num_visible / num_goal_tokens
            else:
                norm_gar = 0.0
            normalized_gar_per_turn.append(norm_gar)
    else:
        # Ours: query = last token per assistant turn
        for pos in assistant_positions:
            result = measurer.compute_gar(goal_positions, [pos])
            raw_gar = result["mean_gar"]
            gar_per_turn.append(raw_gar)

            num_visible = pos + 1
            visible_tokens_per_turn.append(num_visible)

            if num_goal_tokens > 0:
                norm_gar = raw_gar * num_visible / num_goal_tokens
            else:
                norm_gar = 0.0
            normalized_gar_per_turn.append(norm_gar)

    result = {
        "gar_per_turn": gar_per_turn,
        "normalized_gar_per_turn": normalized_gar_per_turn,
        "visible_tokens_per_turn": visible_tokens_per_turn,
    }
    if per_turn_gates is not None:
        result["per_turn_gates"] = per_turn_gates
    return result


def compute_conversation_ppl(model, tokenizer, messages, device, turn_features_ref=None, gate_type="none"):
    """Compute NTP perplexity on assistant tokens of a conversation."""
    full_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
    input_ids = tokenizer(full_text, return_tensors="pt", truncation=True, max_length=2048).input_ids

    seq_input = input_ids.squeeze(0)
    boundaries = detect_turn_boundaries(seq_input, tokenizer)

    labels = torch.full_like(input_ids, -100)
    for turn in boundaries["turns"]:
        if turn["role"] == "assistant":
            labels[0, turn["content_start"]:turn["content_end"]] = input_ids[0, turn["content_start"]:turn["content_end"]]

    if (labels != -100).sum() == 0:
        return None, None

    input_ids = input_ids.to(device)
    labels = labels.to(device)

    if gate_type == "threadgate" and turn_features_ref is not None:
        tf = build_turn_features(seq_input, tokenizer)
        turn_features_ref[0] = {
            "turn_distance": tf["turn_distance"].to(device),
            "turn_index": tf["turn_index"].to(device),
        }

    with torch.no_grad():
        outputs = model(input_ids, labels=labels)

    if gate_type == "threadgate" and turn_features_ref is not None:
        turn_features_ref[0] = None

    ppl = torch.exp(outputs.loss).item()
    return ppl, outputs.loss.item()


def plot_gar_comparison(baseline_gar, trained_gar, output_path, gate_type):
    """Plot baseline vs trained GAR curves."""
    min_turns = min(len(baseline_gar), len(trained_gar))
    turns_x = list(range(1, min_turns + 1))
    b = baseline_gar[:min_turns]
    t = trained_gar[:min_turns]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(turns_x, b, "r-s", linewidth=2, markersize=6, label="Baseline (no gate)")
    ax.plot(turns_x, t, "b-o", linewidth=2, markersize=6, label=f"Trained ({gate_type})")

    b_mid = float(np.mean(b[2:8]) if len(b) >= 8 else np.mean(b[2:]))
    t_mid = float(np.mean(t[2:8]) if len(t) >= 8 else np.mean(t[2:]))
    ax.axhline(y=b_mid, color="red", linestyle="--", alpha=0.4, label=f"Baseline mid: {b_mid:.4f}")
    ax.axhline(y=t_mid, color="blue", linestyle="--", alpha=0.4, label=f"Trained mid: {t_mid:.4f}")

    recovery_pp = (t_mid - b_mid) * 100
    ax.set_xlabel("Turn Index", fontsize=12)
    ax.set_ylabel("GAR (Goal Attention Ratio)", fontsize=12)
    ax.set_title(f"GAR Recovery: {gate_type} (mid-turn recovery: {recovery_pp:+.1f}pp)", fontsize=11)
    ax.legend(fontsize=9)
    ax.set_xticks(turns_x)
    ax.grid(True, alpha=0.3)

    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Evaluate trained gated model GAR recovery")
    parser.add_argument("--checkpoint-dir", default=None)
    parser.add_argument("--gate-type", required=True, choices=["threadgate", "uniform", "none"])
    parser.add_argument("--output-dir", default="/root/turn_residual_gating/results/")
    parser.add_argument("--baseline-results", default="/root/turn_residual_gating/results/phase1_gar_results.json")
    parser.add_argument("--model", default=MODEL_NAME)
    parser.add_argument("--conversations-path", default=None, help="Path to standard_conversations.json for fixed conversations")
    parser.add_argument("--gar-variant", default="ours", choices=["ours", "dongre"],
                        help="GAR definition variant: ours (system+first_user goal, last token query) or dongre (system-only goal, all response tokens query)")
    parser.add_argument("--gate-profile", action="store_true",
                        help="Enable per-turn gate value profiling")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    print(f"Gate type: {args.gate_type}")
    print(f"GAR variant: {args.gar_variant}")
    print(f"Checkpoint: {args.checkpoint_dir}")

    # Load base model with eager attention (required for GAR measurement)
    print("Loading base model (eager attention)...")
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    base_model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        attn_implementation="eager",
    )
    base_model.eval()

    # Apply LoRA if present
    if args.checkpoint_dir:
        lora_path = os.path.join(args.checkpoint_dir, "lora")
        if os.path.isdir(lora_path):
            print("Loading LoRA adapter...")
            from peft import PeftModel
            base_model = PeftModel.from_pretrained(base_model, lora_path)
            base_model.eval()
        else:
            print("No LoRA directory found, using base model weights")
    else:
        print("No checkpoint dir specified, using pure base model")

    # Load or generate conversations
    if args.conversations_path and os.path.exists(args.conversations_path):
        print(f"\nLoading fixed conversations from {args.conversations_path}")
        with open(args.conversations_path) as f:
            conv_data = json.load(f)
        conversations = [c["messages"] for c in conv_data]
        conversations_source = "fixed"
        for i, c in enumerate(conv_data):
            num_turns = c.get("num_turns", sum(1 for m in c["messages"] if m["role"] == "assistant"))
            print(f"  Conversation {i+1}/{len(conv_data)}: {num_turns} assistant turns")
    else:
        print("\nGenerating conversations...")
        conversations = []
        for i, (sys_prompt, user_qs) in enumerate(zip(SYSTEM_PROMPTS, CONVERSATIONS_DATA)):
            print(f"  Conversation {i+1}/{len(SYSTEM_PROMPTS)}: {sys_prompt[:50]}...")
            messages = build_conversation(tokenizer, base_model, sys_prompt, user_qs, device)
            num_turns = sum(1 for m in messages if m["role"] == "assistant")
            print(f"    {num_turns} assistant turns")
            conversations.append(messages)
        conversations_source = "generated"

    # Load gates and register hooks
    hf_model = _find_hf_model(base_model)
    hidden_dim = hf_model.config.hidden_size
    num_layers = hf_model.config.num_hidden_layers
    model_device = next(hf_model.model.layers[0].parameters()).device
    print(f"Model device: {model_device}")

    if args.gate_type == "none" or not args.checkpoint_dir:
        print("No gates loaded (base/LoRA-only mode)")
        hooks = []
        turn_features_ref = [None]
        gate_values = {}
    else:
        print("\nLoading gate parameters...")
        gates, turn_embedding = load_gates(args.checkpoint_dir, args.gate_type, hidden_dim, num_layers)
        hooks, turn_features_ref, gate_values = register_gating_hooks(
            base_model, gates, args.gate_type, turn_embedding, device=model_device
        )
    measurer = GARMeasurer(hf_model)

    # Measure GAR with gating active
    print("\nMeasuring GAR...")
    all_gar_curves = []
    all_norm_curves = []
    all_visible_curves = []
    all_gate_profiles = []
    for i, messages in enumerate(conversations):
        result = measure_gar_per_turn(
            base_model, tokenizer, measurer, messages, device,
            turn_features_ref, args.gate_type, gar_variant=args.gar_variant,
            gate_values_ref=gate_values if args.gate_profile else None,
            gate_profile=args.gate_profile,
        )
        if result:
            gar_curve = result["gar_per_turn"]
            norm_curve = result["normalized_gar_per_turn"]
            vis_curve = result["visible_tokens_per_turn"]
            print(f"  Conv {i+1} GAR:  {[f'{g:.4f}' for g in gar_curve]}")
            print(f"  Conv {i+1} nGAR: {[f'{g:.4f}' for g in norm_curve]}")
            all_gar_curves.append(gar_curve)
            all_norm_curves.append(norm_curve)
            all_visible_curves.append(vis_curve)
            if "per_turn_gates" in result:
                all_gate_profiles.append(result["per_turn_gates"])
        else:
            print(f"  Conv {i+1}: WARNING - could not measure GAR")

    # Compute NTP Perplexity (with gates active if applicable)
    print("\nMeasuring NTP Perplexity...")
    all_ppl = []
    all_ntp_loss = []
    for i, messages in enumerate(conversations):
        ppl, ntp_loss = compute_conversation_ppl(
            base_model, tokenizer, messages, device,
            turn_features_ref=turn_features_ref, gate_type=args.gate_type,
        )
        if ppl is not None:
            all_ppl.append(ppl)
            all_ntp_loss.append(ntp_loss)
            print(f"  Conv {i+1} PPL: {ppl:.2f} (NTP loss: {ntp_loss:.4f})")
        else:
            print(f"  Conv {i+1}: WARNING - no assistant tokens for PPL")

    avg_ppl = float(np.mean(all_ppl)) if all_ppl else None
    avg_ntp_loss = float(np.mean(all_ntp_loss)) if all_ntp_loss else None
    if avg_ppl is not None:
        print(f"\nAvg PPL: {avg_ppl:.2f}")
        print(f"Avg NTP Loss: {avg_ntp_loss:.4f}")

    for h in hooks:
        h.remove()

    if not all_gar_curves:
        print("ERROR: No valid GAR measurements")
        sys.exit(1)

    # Statistics
    min_turns = min(len(c) for c in all_gar_curves)
    aligned = [c[:min_turns] for c in all_gar_curves]
    avg_gar = np.mean(aligned, axis=0).tolist()

    aligned_norm = [c[:min_turns] for c in all_norm_curves]
    avg_norm_gar = np.mean(aligned_norm, axis=0).tolist()

    aligned_vis = [c[:min_turns] for c in all_visible_curves]
    avg_visible = [int(x) for x in np.mean(aligned_vis, axis=0).tolist()]

    turn1_gar = avg_gar[0]
    mid_turns_gar = float(np.mean(avg_gar[2:8]) if len(avg_gar) >= 8 else np.mean(avg_gar[2:]))
    mid_turns_norm_gar = float(np.mean(avg_norm_gar[2:8]) if len(avg_norm_gar) >= 8 else np.mean(avg_norm_gar[2:]))

    # Baseline comparison
    baseline_gar = None
    gar_recovery = None
    baseline_mid = None
    if os.path.exists(args.baseline_results):
        with open(args.baseline_results) as f:
            baseline = json.load(f)
        baseline_gar = baseline["avg_gar_per_turn"]
        baseline_mid = baseline["mid_turns_avg_gar"]
        gar_recovery = mid_turns_gar - baseline_mid
        print(f"\nBaseline mid-turn GAR: {baseline_mid:.4f}")
        print(f"Trained mid-turn GAR:  {mid_turns_gar:.4f}")
        print(f"GAR recovery:          {gar_recovery*100:+.2f}pp")
    else:
        print(f"\nWARNING: Baseline not found at {args.baseline_results}")

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
        "num_turns": min_turns,
        "gar_curves": all_gar_curves,
        "avg_gar_per_turn": avg_gar,
        "turn1_avg_gar": turn1_gar,
        "mid_turns_avg_gar": mid_turns_gar,
        "baseline_mid_turns_avg_gar": baseline_mid,
        "gar_recovery_pp": gar_recovery * 100 if gar_recovery is not None else None,
        "normalized_gar_curves": [c[:min_turns] for c in all_norm_curves],
        "avg_normalized_gar_per_turn": avg_norm_gar,
        "mid_turns_avg_normalized_gar": mid_turns_norm_gar,
        "avg_visible_tokens_per_turn": avg_visible,
        "conversations_source": conversations_source,
        "avg_ppl": avg_ppl,
        "avg_ntp_loss": avg_ntp_loss,
        "ppl_per_conversation": all_ppl,
        "ntp_loss_per_conversation": all_ntp_loss,
    }

    if args.gate_profile and all_gate_profiles:
        gate_profile_per_turn = {}
        for i, profile in enumerate(all_gate_profiles):
            gate_profile_per_turn[f"conv_{i}"] = profile
        gate_dr = _compute_gate_dynamic_range(all_gate_profiles, num_layers)
        results["gate_profile_per_turn"] = gate_profile_per_turn
        results["gate_dynamic_range"] = gate_dr

    results_path = os.path.join(args.output_dir, f"{ckpt_name}_gar.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {results_path}")

    if baseline_gar:
        plot_path = os.path.join(args.output_dir, f"{ckpt_name}_gar_comparison.png")
        plot_gar_comparison(baseline_gar, avg_gar, plot_path, args.gate_type)
        print(f"Plot saved to {plot_path}")

    variant_label = f"GAR-{args.gar_variant}" if args.gar_variant == "dongre" else "GAR-ours"
    print(f"\n{'='*50}")
    print(f"Phase 2 GAR Evaluation ({args.gate_type}, {variant_label})")
    print(f"{'='*50}")
    print(f"Turn 1 avg GAR:     {turn1_gar:.4f}")
    print(f"Mid-turns avg GAR:  {mid_turns_gar:.4f}")
    print(f"Mid-turns avg nGAR: {mid_turns_norm_gar:.4f}")
    if gar_recovery is not None:
        print(f"GAR recovery:       {gar_recovery*100:+.2f}pp")
    if avg_ppl is not None:
        print(f"Avg PPL:            {avg_ppl:.2f}")
        print(f"Avg NTP Loss:       {avg_ntp_loss:.4f}")

    if args.gate_profile and "gate_dynamic_range" in results:
        print(f"\nGate Dynamic Range (top layers by |diff|):")
        sorted_layers = sorted(
            results["gate_dynamic_range"].items(),
            key=lambda x: abs(x[1]["diff"]),
            reverse=True,
        )
        for lk, dr in sorted_layers[:10]:
            other_keys = [k for k in dr if k not in ("turn1", "diff")]
            tn_key = other_keys[0] if other_keys else "turn1"
            print(f"  {lk}: turn1={dr['turn1']:.4f}  {tn_key}={dr[tn_key]:.4f}  diff={dr['diff']:+.4f}")


if __name__ == "__main__":
    main()
