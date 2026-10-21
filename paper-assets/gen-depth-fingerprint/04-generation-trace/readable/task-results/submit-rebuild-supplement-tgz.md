# submit rebuild supplement tgz

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_rebuild-supplement-tgz_20260520T064518_result.json`
- **Structured JSON:** [`b4f2e0b030fd306dd988.json`](../../sessions/b4/b4f2e0b030fd306dd988.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

False positive on the earlier grep (likely matched the `-r` traversal before the old tgz was removed). No actual path leaks found.

Anonymity check passed. Here's the summary:

**File**: `artifacts/_project/anonymous_supplement.tgz`  
**Size**: 19 MB

**Complete file list (68 files)**:

```
supplement/
├── verification_report.md
├── data/                          (30 CSV/JSONL files)
│   ├── README.md
│   ├── cross-model-chains/features.csv
│   ├── detector_scores_8gen.csv
│   ├── features_all_models.csv
│   ├── features_indep_olmo-2-1b.csv
│   ├── features_indep_pythia-2.8b.csv
│   ├── features_llama-3.2-3b-instruct.csv
│   ├── features_olmo-2-0425-1b-instruct.csv
│   ├── features_olmo-2-1b-t05.csv
│   ├── features_olmo-2-1b-t09.csv
│   ├── features_pythia-2.8b-{creative,news,scientific,t05,t09}.csv
│   ├── features_qwen3-0.6b-{instruct,t05,t09}.csv
│   ├── features_qwen3-1.7b-{high-temp,low-temp,instruct,t09}.csv
│   ├── features_qwen8b_ref_{olmo,qwen}.csv
│   ├── features_ref_{olmo,qwen}.csv
│   ├── paraphrase_features.csv
│   ├── transfer_matrix.csv
│   ├── wiki_seed_1000.jsonl
│   └── seeds/{creative,news,scientific}_seed_500.jsonl
└── code/                          (34 .py files + README + requirements.txt)
    ├── README.md, requirements.txt
    ├── 8gen_length_confound.py
    ├── analyze_instruct.py, analyze_prompt_types.py
    ├── benchmark_efficiency.py, bootstrap_downstream_ci.py
    ├── classify_and_eval.py, compute_dataset_stats.py
    ├── cross_model_logo.py, cross_ref_analysis.py, cross_temp_transfer.py
    ├── ddr_temp_analysis.py, distributional_tests.py
    ├── end_to_end_classifier.py
    ├── eval_8gen_{baselines_pooled,finer_depth,logo,sampling_ablation}.py
    ├── eval_exp052_instruct.py, eval_independent_seed.py
    ├── extract_features.py, extract_features_jsonl.py
    ├── finetune_downstream.py, generate_chain.py
    ├── prepare_downstream_data.py, seed_demeaning_logo.py
    ├── transfer_ablation.py
    ├── scripts/{alt_classifier_eval,bootstrap_ci_v2,lofo_ablation,plot_fig1_strip,plot_fig2,plot_fig3,tost_equivalence}.py
    └── experiments/human_edit_robustness/run_robustness.py
```

No anonymity issues detected — no author names, institution names, or server paths in the packaged files.

---
