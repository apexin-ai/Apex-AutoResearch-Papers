#!/usr/bin/env python3
"""Test NLI models standalone on ProofWriter D5-600 (CPU only).
Tests: roberta-large-mnli, bart-large-mnli, deberta-v2-xxlarge-mnli (if available).
"""
import json
import time
import sys
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

PW_DATA = "/root/symb_invariant_consensus/data/proofwriter_full.json"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/nli_standalone_cpu_test"
DEVICE = "cpu"

MODELS = {
    "roberta-large-mnli": {
        "path": "/root/autodl-tmp/models/roberta-large-mnli",
        "type": "standard",  # entailment=2, neutral=1, contradiction=0
        "label_map": {2: "True", 1: "Unknown", 0: "False"},
    },
    "bart-large-mnli": {
        "path": "/root/autodl-tmp/models/bart-large-mnli",
        "type": "zero-shot",  # uses zero-shot-classification pipeline
        "label_map": None,  # handled by pipeline
    },
}


def split_problem(problem_text):
    marker = "Determine whether the following statement is true, false, or unknown:"
    idx = problem_text.find(marker)
    if idx == -1:
        marker2 = "Determine whether the following statement is True, False, or Unknown:"
        idx = problem_text.find(marker2)
        if idx == -1:
            return problem_text, ""
        marker = marker2
    premise = problem_text[:idx].strip()
    hypothesis = problem_text[idx + len(marker):].strip()
    return premise, hypothesis


def test_standard_nli(model_name, model_path, label_map, problems, gt, n_sample=50):
    """Test standard NLI model (roberta/deberta style)."""
    print(f"\n{'='*60}")
    print(f"Testing: {model_name}")
    print(f"Path: {model_path}")
    print(f"Device: {DEVICE}")
    print(f"Sample size: {n_sample} (speed test first)")
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()
    
    # Speed test on first sample
    pids = list(problems.keys())[:n_sample]
    
    t0 = time.time()
    correct = 0
    results = {}
    
    for pid in pids:
        premise, hypothesis = split_problem(problems[pid])
        if not hypothesis:
            continue
        
        inputs = tokenizer(premise, hypothesis, return_tensors="pt", 
                          truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        
        probs = torch.softmax(outputs.logits, dim=-1)[0]
        pred_idx = probs.argmax().item()
        pred = label_map[pred_idx]
        
        gold = gt[pid]
        is_correct = (pred == gold)
        correct += int(is_correct)
        results[pid] = {"pred": pred, "gold": gold, "correct": is_correct}
    
    elapsed = time.time() - t0
    n_done = len(results)
    speed = elapsed / n_done if n_done > 0 else 0
    acc = correct / n_done if n_done > 0 else 0
    
    print(f"  Sample accuracy: {acc:.4f} ({correct}/{n_done})")
    print(f"  Speed: {speed:.3f} s/sample")
    print(f"  Estimated full 600: {speed * 600 / 60:.1f} min")
    
    return {
        "model": model_name,
        "n_tested": n_done,
        "accuracy": acc,
        "correct": correct,
        "speed_s_per_sample": round(speed, 4),
        "estimated_full_600_min": round(speed * 600 / 60, 1),
    }


def test_bart_zeroshot(model_path, problems, gt, n_sample=20):
    """Test BART zero-shot classification."""
    print(f"\n{'='*60}")
    print(f"Testing: bart-large-mnli (zero-shot pipeline)")
    print(f"Device: {DEVICE}")
    print(f"Sample size: {n_sample}")
    
    classifier = pipeline("zero-shot-classification", model=model_path, device=-1)
    candidate_labels = ["entailment", "contradiction", "neutral"]
    label_to_answer = {"entailment": "True", "contradiction": "False", "neutral": "Unknown"}
    
    pids = list(problems.keys())[:n_sample]
    
    t0 = time.time()
    correct = 0
    results = {}
    
    for pid in pids:
        premise, hypothesis = split_problem(problems[pid])
        if not hypothesis:
            continue
        
        # For BART zero-shot: classify hypothesis given premise as context
        text = f"{premise}\n\nStatement: {hypothesis}"
        result = classifier(text, candidate_labels, hypothesis_template="This statement is {}.")
        
        top_label = result["labels"][0]
        pred = label_to_answer[top_label]
        
        gold = gt[pid]
        is_correct = (pred == gold)
        correct += int(is_correct)
        results[pid] = {"pred": pred, "gold": gold, "correct": is_correct}
    
    elapsed = time.time() - t0
    n_done = len(results)
    speed = elapsed / n_done if n_done > 0 else 0
    acc = correct / n_done if n_done > 0 else 0
    
    print(f"  Sample accuracy: {acc:.4f} ({correct}/{n_done})")
    print(f"  Speed: {speed:.3f} s/sample")
    print(f"  Estimated full 600: {speed * 600 / 60:.1f} min")
    
    return {
        "model": "bart-large-mnli",
        "n_tested": n_done,
        "accuracy": acc,
        "correct": correct,
        "speed_s_per_sample": round(speed, 4),
        "estimated_full_600_min": round(speed * 600 / 60, 1),
    }


def main():
    import os
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Load data
    with open(PW_DATA) as f:
        pw = json.load(f)
    gt = {p["id"]: p["answer"] for p in pw}
    problems = {p["id"]: p["problem"] for p in pw}
    print(f"Loaded {len(pw)} ProofWriter problems")
    
    all_results = {}
    
    # Test roberta-large-mnli (50 samples for speed)
    r = test_standard_nli(
        "roberta-large-mnli",
        MODELS["roberta-large-mnli"]["path"],
        MODELS["roberta-large-mnli"]["label_map"],
        problems, gt, n_sample=50
    )
    all_results["roberta-large-mnli"] = r
    
    # Test bart-large-mnli (20 samples - slower)
    r = test_bart_zeroshot(
        MODELS["bart-large-mnli"]["path"],
        problems, gt, n_sample=20
    )
    all_results["bart-large-mnli"] = r
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY - NLI Standalone on ProofWriter D5 (CPU sample)")
    print(f"{'='*60}")
    print(f"{'Model':<45} {'Acc':<8} {'Speed':<10} {'Est. Full'}")
    print("-" * 80)
    
    # Include known results
    known = {
        "deberta-base-mnli": 0.3617,
        "deberta-large-mnli": 0.5500,
        "deberta-v3-large-mnli-fever-anli-ling-wanli": 0.4517,
    }
    for name, acc in known.items():
        print(f"  {name:<43} {acc:.4f}   (full 600, from prior exp)")
    
    for name, r in all_results.items():
        print(f"  {name:<43} {r['accuracy']:.4f}   {r['speed_s_per_sample']:.3f}s/q   ~{r['estimated_full_600_min']:.0f}min")
    
    # Save
    output_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(output_path, "w") as f:
        json.dump({"known_results": known, "new_tests": all_results}, f, indent=2)
    print(f"\nSaved to {output_path}")


if __name__ == "__main__":
    main()
