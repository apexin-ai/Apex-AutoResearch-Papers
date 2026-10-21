"""MVP pilot experiment: N=8 stochastic sampling + greedy baseline on SciERC test set."""

import json
import os
import sys
import time

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')

import numpy as np

from data_utils import load_uie_jsonl
from sampling import (
    VLLMSampler, build_uie_prompt, parse_extraction_output,
    realign_spans, SCIERC_SCHEMA_HINT, UIE_JSON_SCHEMA,
)
from consistency import compute_all_consistency_scores
from evaluation import (
    compute_ner_f1, compute_re_f1, per_instance_f1,
    spearman_correlation, compute_sample_f1_distribution,
)

MODEL = "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged"
TEST_DATA = "/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Loading test data from {TEST_DATA}")
    instances = load_uie_jsonl(TEST_DATA)
    print(f"Loaded {len(instances)} instances")

    print(f"Initializing VLLMSampler with model {MODEL}")
    sampler = VLLMSampler(MODEL, tensor_parallel_size=1, max_model_len=2048, gpu_memory_utilization=0.9)

    # Build prompts
    prompts = [build_uie_prompt(inst["text"], subtask="full", schema_hint=SCIERC_SCHEMA_HINT, use_train_format=True) for inst in instances]
    chat_prompts = [sampler.format_chat_prompt(p) for p in prompts]
    print(f"Built {len(chat_prompts)} chat prompts")

    from vllm import SamplingParams
    from vllm.sampling_params import StructuredOutputsParams
    guided = StructuredOutputsParams(json=UIE_JSON_SCHEMA)

    # N=8 stochastic sampling at T=1.0
    print("Starting N=8 stochastic sampling at T=1.0 ...")
    t0 = time.time()
    stoch_params = SamplingParams(n=8, temperature=1.0, max_tokens=512, structured_outputs=guided)
    stoch_outputs = sampler.llm.generate(chat_prompts, stoch_params)
    t_stoch = time.time() - t0
    print(f"Stochastic sampling done in {t_stoch:.1f}s")

    # N=1 greedy at T=0
    print("Starting N=1 greedy decoding at T=0 ...")
    t0 = time.time()
    greedy_params = SamplingParams(n=1, temperature=0.0, max_tokens=512, structured_outputs=guided)
    greedy_outputs = sampler.llm.generate(chat_prompts, greedy_params)
    t_greedy = time.time() - t0
    print(f"Greedy decoding done in {t_greedy:.1f}s")

    # Parse + realign all outputs
    print("Parsing and realigning outputs ...")
    n_parse_fail_stoch = 0
    n_parse_fail_greedy = 0
    sampled_instances = []

    for i, inst in enumerate(instances):
        gold = {"entities": inst.get("entities", []), "relations": inst.get("relations", []), "events": []}

        samples = []
        for out in stoch_outputs[i].outputs:
            parsed = parse_extraction_output(out.text)
            if not parsed.get("entities") and not parsed.get("relations") and out.text.strip():
                raw = out.text.strip()
                try:
                    json.loads(raw)
                except json.JSONDecodeError:
                    n_parse_fail_stoch += 1
            samples.append(realign_spans(parsed, inst["text"]))

        greedy_raw = greedy_outputs[i].outputs[0].text
        greedy_parsed = parse_extraction_output(greedy_raw)
        if not greedy_parsed.get("entities") and not greedy_parsed.get("relations") and greedy_raw.strip():
            try:
                json.loads(greedy_raw.strip())
            except json.JSONDecodeError:
                n_parse_fail_greedy += 1
                print(f"  Greedy parse fail [{i}]: {greedy_raw[:200]}")
        greedy = realign_spans(greedy_parsed, inst["text"])

        sampled_instances.append({
            "id": inst.get("id", str(i)),
            "text": inst["text"],
            "gold": gold,
            "samples": samples,
            "greedy": greedy,
        })

    print(f"Parse failures: stochastic={n_parse_fail_stoch}/{len(instances)*8}, greedy={n_parse_fail_greedy}/{len(instances)}")

    # Save samples
    samples_path = f"{OUTPUT_DIR}/samples.jsonl"
    with open(samples_path, "w") as f:
        for si in sampled_instances:
            f.write(json.dumps(si, ensure_ascii=False) + "\n")
    print(f"Saved samples to {samples_path}")

    # Per subtask evaluation
    report = {
        "exp_id": "mvp_pilot_001",
        "model": MODEL,
        "test_data": TEST_DATA,
        "num_instances": len(sampled_instances),
        "n_samples": 8,
        "temperature": 1.0,
        "n_parse_fail_stoch": n_parse_fail_stoch,
        "n_parse_fail_greedy": n_parse_fail_greedy,
        "time_stoch_s": round(t_stoch, 1),
        "time_greedy_s": round(t_greedy, 1),
    }

    for subtask in ["ner", "re"]:
        print(f"\n{'='*60}")
        print(f"  Subtask: {subtask}")
        print(f"{'='*60}")

        # Filter gold-nonempty
        if subtask == "ner":
            nonempty = [(i, si) for i, si in enumerate(sampled_instances) if len(si["gold"].get("entities", [])) > 0]
        else:
            nonempty = [(i, si) for i, si in enumerate(sampled_instances) if len(si["gold"].get("relations", [])) > 0]

        n_gold_empty = len(sampled_instances) - len(nonempty)
        print(f"  Gold-nonempty instances: {len(nonempty)} / {len(sampled_instances)} (filtered {n_gold_empty})")

        nonempty_instances = [si for _, si in nonempty]

        # Consistency scores (on nonempty only)
        consistency = compute_all_consistency_scores(nonempty_instances, subtask=subtask)

        # Per-instance greedy F1 (on nonempty only)
        greedy_f1s = [per_instance_f1(si["greedy"], si["gold"], subtask=subtask) for si in nonempty_instances]

        # Full ρ
        rho_fk_full, p_fk_full = spearman_correlation(consistency["fleiss_kappa"], greedy_f1s)
        rho_sj_full, p_sj_full = spearman_correlation(consistency["soft_jaccard"], greedy_f1s)

        # Conditional ρ: exclude instances where ALL 8 samples have F1=0
        conditional_mask = []
        for si in nonempty_instances:
            sample_f1s = [per_instance_f1(s, si["gold"], subtask=subtask) for s in si["samples"]]
            conditional_mask.append(any(f > 0 for f in sample_f1s))

        cond_consistency_fk = [s for s, m in zip(consistency["fleiss_kappa"], conditional_mask) if m]
        cond_consistency_sj = [s for s, m in zip(consistency["soft_jaccard"], conditional_mask) if m]
        cond_f1s = [f for f, m in zip(greedy_f1s, conditional_mask) if m]
        n_all_zero = sum(1 for m in conditional_mask if not m)
        n_cond = len(cond_f1s)

        rho_fk_cond, p_fk_cond = spearman_correlation(cond_consistency_fk, cond_f1s) if n_cond >= 3 else (0.0, 1.0)
        rho_sj_cond, p_sj_cond = spearman_correlation(cond_consistency_sj, cond_f1s) if n_cond >= 3 else (0.0, 1.0)

        # Overall metrics
        greedy_preds = [si["greedy"] for si in nonempty_instances]
        golds_ne = [si["gold"] for si in nonempty_instances]
        oracle_preds = [max(si["samples"], key=lambda s, g=si["gold"]: per_instance_f1(s, g, subtask)) for si in nonempty_instances]

        if subtask == "ner":
            greedy_metrics = compute_ner_f1(greedy_preds, golds_ne)
            oracle_metrics = compute_ner_f1(oracle_preds, golds_ne)
        else:
            greedy_metrics = compute_re_f1(greedy_preds, golds_ne)
            oracle_metrics = compute_re_f1(oracle_preds, golds_ne)

        headroom = oracle_metrics["f1"] - greedy_metrics["f1"]

        # Sample F1 distribution
        sample_dist = compute_sample_f1_distribution(nonempty_instances, subtask=subtask)

        # Print
        print(f"  Greedy F1:    {greedy_metrics['f1']*100:.1f}%")
        print(f"  Oracle F1:    {oracle_metrics['f1']*100:.1f}%")
        print(f"  Headroom:     {headroom*100:+.1f}pp")
        print(f"  Sample F1=0:  {sample_dist['pct_f1_zero']:.1f}%")
        print(f"  Fleiss κ (mean): {sum(consistency['fleiss_kappa'])/len(consistency['fleiss_kappa']):.4f}")
        print(f"  Soft Jaccard (mean): {sum(consistency['soft_jaccard'])/len(consistency['soft_jaccard']):.4f}")
        print(f"  Full ρ(κ,F1):  {rho_fk_full:+.4f} (n={len(greedy_f1s)})")
        print(f"  Full ρ(SJ,F1): {rho_sj_full:+.4f} (n={len(greedy_f1s)})")
        print(f"  Cond ρ(κ,F1):  {rho_fk_cond:+.4f} (n={n_cond})")
        print(f"  Cond ρ(SJ,F1): {rho_sj_cond:+.4f} (n={n_cond})")
        if n_cond < 30:
            print(f"  ⚠️ Conditional n={n_cond} < 30, ρ may be unreliable")
        print(f"  All-samples-F1=0 filtered: {n_all_zero}")
        print(f"  SJ > κ: {'YES' if rho_sj_full > rho_fk_full else 'NO'} (delta={rho_sj_full - rho_fk_full:+.4f})")

        # Store in report
        prefix = f"{subtask}_"
        report[f"{prefix}greedy_f1"] = greedy_metrics["f1"]
        report[f"{prefix}greedy_p"] = greedy_metrics["precision"]
        report[f"{prefix}greedy_r"] = greedy_metrics["recall"]
        report[f"{prefix}oracle_f1"] = oracle_metrics["f1"]
        report[f"{prefix}oracle_headroom"] = headroom
        report[f"{prefix}fleiss_kappa_mean"] = float(np.mean(consistency["fleiss_kappa"]))
        report[f"{prefix}soft_jaccard_mean"] = float(np.mean(consistency["soft_jaccard"]))
        report[f"{prefix}sample_f1_mean"] = sample_dist["mean"]
        report[f"{prefix}sample_f1_std"] = sample_dist["std"]
        report[f"{prefix}sample_f1_pct_zero"] = sample_dist["pct_f1_zero"]
        report[f"{prefix}n_gold_empty_filtered"] = n_gold_empty
        report[f"{prefix}n_all_samples_f1_zero_filtered"] = n_all_zero
        report[f"{prefix}correlation_softjaccard_vs_f1_full"] = {"rho": rho_sj_full, "p_value": p_sj_full, "n": len(greedy_f1s)}
        report[f"{prefix}correlation_fleiss_vs_f1_full"] = {"rho": rho_fk_full, "p_value": p_fk_full, "n": len(greedy_f1s)}
        report[f"{prefix}correlation_softjaccard_vs_f1_conditional"] = {"rho": rho_sj_cond, "p_value": p_sj_cond, "n": n_cond}
        report[f"{prefix}correlation_fleiss_vs_f1_conditional"] = {"rho": rho_fk_cond, "p_value": p_fk_cond, "n": n_cond}
        report[f"{prefix}structural_beats_surface"] = rho_sj_full > rho_fk_full
        report[f"{prefix}rho_advantage"] = rho_sj_full - rho_fk_full

    # Verdict
    re_rho_sj = report["re_correlation_softjaccard_vs_f1_full"]["rho"]
    re_beats = report["re_structural_beats_surface"]
    any_headroom = report.get("ner_oracle_headroom", 0) >= 0.02 or report.get("re_oracle_headroom", 0) >= 0.02

    if re_rho_sj >= 0.40 and re_beats and any_headroom:
        verdict = "PASS"
    elif re_rho_sj >= 0.30:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    report["verdict"] = verdict
    report["verdict_note"] = "RE ρ_sj ≥ 0.40 AND ρ_sj > ρ_fk AND any headroom ≥ 2pp"

    print(f"\n{'='*60}")
    print(f"  VERDICT: {verdict}")
    print(f"  RE ρ(SJ,F1) full = {re_rho_sj:+.4f}")
    print(f"{'='*60}")

    # Save report
    report_path = f"{OUTPUT_DIR}/report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved to {report_path}")

if __name__ == "__main__":
    main()
