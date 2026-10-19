#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

TASKS = [
    "llm_c_fineweb10b", "torch_conv_kan_cifar10", "open_r1_math500",
    "agent_lightning_room_selector", "uni2ts_lsf_etth1", "timesfm_etth1_long_horizon",
    "modernbert_mnli_accuracy", "cifar10_airbench94", "noisygl_cora_uniform30_gcn",
    "tabmini_molecular_biology_promoters_auc", "binary_diffusion_adult_rf", "xlstm_parity",
    "vbll_yacht_rmse", "tabm_california_rmse", "timexer_pjm_168_24_mse",
    "ablkit_hwf_reasoning_accuracy", "tunedgnn_cora_gcn_accuracy", "verl_grpo_gsm8k",
    "forest_diffusion_iris_f1fake", "var_imagenet256", "align_anything_ragen_bandit",
    "chronos_t5_tiny_monash_weather_wql", "hyperboliccv_cifar100_accuracy",
    "itransformer_ettm2_96_mse", "timemixer_ettm2_96_mse", "art_2048_win_rate",
    "open_r1_multimodal_mathvista_accuracy", "rankup_utkface_mae",
    "sparsetsf_ettm1_96_mse", "simple_rl_reason_qwen25_05b_math500",
]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("result_root", type=Path)
    parser.add_argument("--expected", type=int, default=30)
    args = parser.parse_args()
    rows = []
    for task in TASKS:
        files = sorted((args.result_root / task).glob("*_results.json"))
        if not files:
            rows.append({"task": task, "ok": False, "error": "missing_json"})
            continue
        data = json.load(files[0].open())
        field = "chunk_summaries" if isinstance(data.get("chunk_summaries"), list) else "history"
        seq = data.get(field)
        decisions = data.get("decision_history") if isinstance(data.get("decision_history"), list) else data.get("decisions")
        decision_count = len(decisions) if isinstance(decisions, list) else int(data.get("strict_decision_count", data.get("agent_decisions_made", data.get("decisions_made", 0))))
        ok = isinstance(seq, list) and len(seq) == 6 and decision_count == 5
        rows.append({"task": task, "ok": ok, "field": field, "observations": len(seq) if isinstance(seq, list) else 0, "decisions": decision_count, "json": str(files[0])})
    present = [x for x in rows if x.get("error") != "missing_json"]
    complete = [x for x in rows if x.get("ok")]
    output = {"result_root": str(args.result_root), "present": len(present), "complete": len(complete), "expected": args.expected, "rows": rows}
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if len(complete) == args.expected else 1

if __name__ == "__main__":
    raise SystemExit(main())
