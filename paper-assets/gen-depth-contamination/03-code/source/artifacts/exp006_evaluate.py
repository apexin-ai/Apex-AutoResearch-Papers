"""exp006 Evaluation — lm-eval-harness (MMLU + HellaSwag) on LoRA-adapted model.

Input:  base model name + LoRA adapter path (or --base-only for unadapted model)
Output: JSON with task scores in --output path

Dependencies: lm_eval>=0.4, torch, transformers, peft
"""

import argparse
import json
import os
import torch


def run_eval(model_name, adapter_path, tasks, batch_size, cache_dir, output_path):
    import lm_eval

    model_args = f"pretrained={model_name},dtype=bfloat16,trust_remote_code=True"
    if cache_dir:
        model_args += f",cache_dir={cache_dir}"
    if adapter_path:
        model_args += f",peft={adapter_path}"

    print(f"Evaluating: {model_args}")
    print(f"Tasks: {tasks}")

    results = lm_eval.simple_evaluate(
        model="hf",
        model_args=model_args,
        tasks=tasks,
        batch_size=batch_size,
        device="cuda:0",
    )

    # Extract scores
    scores = {}
    for task_name, task_results in results["results"].items():
        task_scores = {}
        for metric, value in task_results.items():
            if isinstance(value, (int, float)):
                task_scores[metric] = value
        scores[task_name] = task_scores

    output = {
        "model": model_name,
        "adapter": adapter_path,
        "tasks": tasks,
        "scores": scores,
    }

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"Results saved to {output_path}")

    # Print summary
    for task, s in scores.items():
        main_metric = s.get("acc_norm,none", s.get("acc,none", "N/A"))
        print(f"  {task}: {main_metric}")

    torch.cuda.empty_cache()
    return output


def main():
    parser = argparse.ArgumentParser(description="exp006 evaluation")
    parser.add_argument("--model-name", type=str, default="Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--adapter-path", type=str, default=None,
                        help="Path to LoRA adapter (omit for base model eval)")
    parser.add_argument("--tasks", type=str, nargs="+", default=["mmlu", "hellaswag"])
    parser.add_argument("--batch-size", type=str, default="auto")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    run_eval(args.model_name, args.adapter_path, args.tasks,
             args.batch_size, args.cache_dir, args.output)


if __name__ == "__main__":
    main()
