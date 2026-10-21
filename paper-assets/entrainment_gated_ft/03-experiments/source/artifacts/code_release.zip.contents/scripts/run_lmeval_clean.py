#!/usr/bin/env python
"""Clean lm-eval script for fla models. No monkeypatch."""
import argparse, json, os, torch

from fla.models.gated_deltanet import GatedDeltaNetConfig, GatedDeltaNetForCausalLM
from fla.models.retnet import RetNetConfig, RetNetForCausalLM
from fla.models.transformer import TransformerConfig, TransformerForCausalLM
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

AutoConfig.register("gated_deltanet", GatedDeltaNetConfig)
AutoModelForCausalLM.register(GatedDeltaNetConfig, GatedDeltaNetForCausalLM)
AutoConfig.register("retnet", RetNetConfig)
AutoModelForCausalLM.register(RetNetConfig, RetNetForCausalLM)
AutoConfig.register("transformer", TransformerConfig)
AutoModelForCausalLM.register(TransformerConfig, TransformerForCausalLM)


def patch_config(model_path):
    """Patch config.json in-place: add allow_neg_eigval for GDN models."""
    config_path = os.path.join(model_path, "config.json")
    with open(config_path) as f:
        c = json.load(f)
    if c.get("use_beta") and not c.get("allow_neg_eigval"):
        c["allow_neg_eigval"] = True
        with open(config_path, "w") as f:
            json.dump(c, f, indent=2)
        print(f"[FIX] Patched config.json: allow_neg_eigval=True")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", required=True)
    parser.add_argument("--tasks", required=True, help="comma-separated task names")
    parser.add_argument("--output_dir", default="./lm_eval_clean")
    parser.add_argument("--batch_size", default="16")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    
    patch_config(args.model_path)

    import lm_eval
    tasks_list = args.tasks.split(",")
    
    results = lm_eval.simple_evaluate(
        model="hf",
        model_args=f"pretrained={args.model_path},dtype=bfloat16,trust_remote_code=True,device_map=cuda:0",
        tasks=tasks_list,
        batch_size=args.batch_size,
    )

    model_name = os.path.basename(args.model_path.rstrip("/"))
    output_path = os.path.join(args.output_dir, f"{model_name}_results.json")
    with open(output_path, "w") as f:
        json.dump(results["results"], f, indent=2, default=str)

    print(f"\nResults saved to {output_path}")
    print(json.dumps(results["results"], indent=2, default=str))


if __name__ == "__main__":
    main()
