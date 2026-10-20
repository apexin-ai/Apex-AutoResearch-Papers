# code supplementary anonymize — Part 2 of 2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-supplementary-anonymize.md) · [Structured JSON](../../../sessions/c4/c4e8aeaa9928d40403d2.json)

## Round 3

### Tool call

_source line 286_

<details open><summary>🔧 Tool call — Write · `toolu_01NTBf6Cq2djarw6aYTpJ8jV`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/supplement/code/README.md",
  "content": "# Generation Depth Fingerprinting: Code Supplement\n\nCode for reproducing the experiments in \"Generation Depth Fingerprinting.\"\n\n## Requirements\n\n- Python 3.10+\n- CUDA-capable GPU (for generation, feature extraction, and end-to-end classifier)\n- A reference language model (e.g., EleutherAI/pythia-410m) available locally or via HuggingFace Hub\n\nInstall dependencies:\n\n```bash\npip install -r requirements.txt\n```\n\n## Directory Structure\n\n`code/` and `data/` are sibling directories under the supplement root. All scripts assume they are run from the `code/` directory and access data via `../data/`.\n\n```\nsupplement/\n├── code/          # Scripts (this directory)\n│   ├── README.md\n│   ├── generate_chain.py\n│   ├── scripts/\n│   └── experiments/\n└── data/          # Data files (not included due to size; see data/README.md for format)\n    ├── README.md\n    ├── features_all_models.csv\n    └── ...\n```\n\n## Data Format\n\n**Features CSV** (`features_all_models.csv`): One row per text sample with columns:\n\n| Column | Description |\n|--------|-------------|\n| `model_name` | Generator model identifier (e.g., `pythia-2.8b`) |\n| `seed_id` | Wikipedia seed text identifier |\n| `depth` | Generation depth (0 = human, 1 = first-gen, 2+ = deeper) |\n| `entropy_mean` | Mean token-level entropy from reference model |\n| `entropy_std` | Std dev of token-level entropy |\n| `entropy_min` | Minimum token-level entropy |\n| `entropy_max` | Maximum token-level entropy |\n| `tail_decay` | Slope of sorted log-prob distribution (ranks 100-1000) |\n| `ttr` | Type-token ratio |\n| `hapax_ratio` | Proportion of words appearing exactly once |\n\n**Generations JSONL**: One JSON object per line with fields `{\"seed_id\", \"depth\", \"text\", \"model_name\"}`.\n\n## Reproduction Steps\n\n### 1. Generate continuation chains (depth 0 to 4)\n\n```bash\npython generate_chain.py \\\n    --input ../data/wiki_seed_1000.jsonl \\\n    --model-path /path/to/generator-model \\\n    --model-name pythia-2.8b \\\n    --output-dir ../data/ \\\n    --device cuda:0\n```\n\nRepeat for each generator model. Multi-GPU sharding is supported via `--shard-id` and `--num-shards`.\n\n### 2. Extract features\n\nExtract 7 features (5 reference-model entropy features + 2 surface features) per text:\n\n```bash\npython extract_features.py \\\n    --input ../data/generations.jsonl \\\n    --output ../data/features.csv \\\n    --ref-model /path/to/pythia-410m \\\n    --device cuda:0\n```\n\nAlternative JSONL output: use `extract_features_jsonl.py` with the same arguments.\n\n### 3. Train classifier and evaluate\n\nSingle-generator 3-class evaluation with Kruskal-Wallis tests:\n\n```bash\npython classify_and_eval.py --input ../data/features.csv --output results/mvp_results.json\n```\n\n### 4. LOGO evaluation (main results)\n\n8-generator Leave-One-Generator-Out evaluation (3-class and binary):\n\n```bash\npython eval_8gen_logo.py\n```\n\n## Script Reference\n\n### Core Pipeline\n\n| Script | Description |\n|--------|-------------|\n| `generate_chain.py` | Generate depth-0 to depth-4 continuation chains |\n| `extract_features.py` | Extract 7 features from text (CSV output) |\n| `extract_features_jsonl.py` | Extract 7 features from text (JSONL output) |\n| `classify_and_eval.py` | XGBoost 3-class classification with statistical tests |\n| `eval_8gen_logo.py` | 8-generator LOGO evaluation (main paper results) |\n\n### Ablation and Analysis\n\n| Script | Description |\n|--------|-------------|\n| `eval_8gen_finer_depth.py` | 5-class vs 3-class depth granularity (Appendix D) |\n| `eval_8gen_sampling_ablation.py` | Training sample size ablation at 25/50/75/100% (Appendix H) |\n| `eval_8gen_cross_model_chains.py` | Cross-model chain extension evaluation (Appendix M) |\n| `eval_8gen_baselines_pooled.py` | Pooled LOGO with detector baselines (main paper) |\n| `cross_temp_transfer.py` | Cross-temperature transfer evaluation (Appendix O) |\n| `end_to_end_classifier.py` | QLoRA end-to-end depth classification (Appendix E) |\n| `distributional_tests.py` | KS + Levene distributional tests on features (Appendix N) |\n| `scripts/lofo_ablation.py` | Leave-one-feature-out ablation (Appendix F) |\n| `scripts/alt_classifier_eval.py` | XGBoost vs LogisticRegression vs RandomForest (Appendix H) |\n| `scripts/bootstrap_ci_v2.py` | Bootstrap 95% confidence intervals |\n| `scripts/tost_equivalence.py` | TOST equivalence testing for downstream results (Appendix L) |\n\n### Robustness and Controls\n\n| Script | Description |\n|--------|-------------|\n| `experiments/human_edit_robustness/run_robustness.py` | Word replacement robustness at 0/5/10/20% (Appendix I) |\n| `8gen_length_confound.py` | Length-matched confound control (Appendix B) |\n| `benchmark_efficiency.py` | Inference efficiency comparison |\n\n### Downstream Utility (Appendix L)\n\n| Script | Description |\n|--------|-------------|\n| `prepare_downstream_data.py` | Build depth-stratified training data variants |\n| `finetune_downstream.py` | Fine-tune causal LM on each variant, measure perplexity |\n| `bootstrap_downstream_ci.py` | Bootstrap CI and effect sizes for downstream results |\n\n### Dataset Statistics and Figures\n\n| Script | Description |\n|--------|-------------|\n| `compute_dataset_stats.py` | Per-generator dataset statistics (Appendix A) |\n| `scripts/plot_fig1_strip.py` | Figure 1: per-generator Spearman rho strip plot |\n| `scripts/plot_fig2.py` | Figure 2: LOGO grouped bar chart |\n| `scripts/plot_fig3.py` | Figure 3: baseline comparison forest plot |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "fab204c3-8db3-40de-acbb-840f821793a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7FJqPiKB36sbqqGzcjrps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 84840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1716
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-17T21:23:36.279Z_

<details><summary>↩ Tool result · `toolu_01NTBf6Cq2djarw6aYTpJ8jV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/supplement/code/README.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "b3e4ae1a-d8c5-4dda-86ca-828c9ff3b34b",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/supplement/code/README.md",
    "content": "# Generation Depth Fingerprinting: Code Supplement\n\nCode for reproducing the experiments in \"Generation Depth Fingerprinting.\"\n\n## Requirements\n\n- Python 3.10+\n- CUDA-capable GPU (for generation, feature extraction, and end-to-end classifier)\n- A reference language model (e.g., EleutherAI/pythia-410m) available locally or via HuggingFace Hub\n\nInstall dependencies:\n\n```bash\npip install -r requirements.txt\n```\n\n## Directory Structure\n\n`code/` and `data/` are sibling directories under the supplement root. All scripts assume they are run from the `code/` directory and access data via `../data/`.\n\n```\nsupplement/\n├── code/          # Scripts (this directory)\n│   ├── README.md\n│   ├── generate_chain.py\n│   ├── scripts/\n│   └── experiments/\n└── data/          # Data files (not included due to size; see data/README.md for format)\n    ├── README.md\n    ├── features_all_models.csv\n    └── ...\n```\n\n## Data Format\n\n**Features CSV** (`features_all_models.csv`): One row per text sample with columns:\n\n| Column | Description |\n|--------|-------------|\n| `model_name` | Generator model identifier (e.g., `pythia-2.8b`) |\n| `seed_id` | Wikipedia seed text identifier |\n| `depth` | Generation depth (0 = human, 1 = first-gen, 2+ = deeper) |\n| `entropy_mean` | Mean token-level entropy from reference model |\n| `entropy_std` | Std dev of token-level entropy |\n| `entropy_min` | Minimum token-level entropy |\n| `entropy_max` | Maximum token-level entropy |\n| `tail_decay` | Slope of sorted log-prob distribution (ranks 100-1000) |\n| `ttr` | Type-token ratio |\n| `hapax_ratio` | Proportion of words appearing exactly once |\n\n**Generations JSONL**: One JSON object per line with fields `{\"seed_id\", \"depth\", \"text\", \"model_name\"}`.\n\n## Reproduction Steps\n\n### 1. Generate continuation chains (depth 0 to 4)\n\n```bash\npython generate_chain.py \\\n    --input ../data/wiki_seed_1000.jsonl \\\n    --model-path /path/to/generator-model \\\n    --model-name pythia-2.8b \\\n    --output-dir ../data/ \\\n    --device cuda:0\n```\n\nRepeat for each generator model. Multi-GPU sharding is supported via `--shard-id` and `--num-shards`.\n\n### 2. Extract features\n\nExtract 7 features (5 reference-model entropy features + 2 surface features) per text:\n\n```bash\npython extract_features.py \\\n    --input ../data/generations.jsonl \\\n    --output ../data/features.csv \\\n    --ref-model /path/to/pythia-410m \\\n    --device cuda:0\n```\n\nAlternative JSONL output: use `extract_features_jsonl.py` with the same arguments.\n\n### 3. Train classifier and evaluate\n\nSingle-generator 3-class evaluation with Kruskal-Wallis tests:\n\n```bash\npython classify_and_eval.py --input ../data/features.csv --output results/mvp_results.json\n```\n\n### 4. LOGO evaluation (main results)\n\n8-generator Leave-One-Generator-Out evaluation (3-class and binary):\n\n```bash\npython eval_8gen_logo.py\n```\n\n## Script Reference\n\n### Core Pipeline\n\n| Script | Description |\n|--------|-------------|\n| `generate_chain.py` | Generate depth-0 to depth-4 continuation chains |\n| `extract_features.py` | Extract 7 features from text (CSV output) |\n| `extract_features_jsonl.py` | Extract 7 features from text (JSONL output) |\n| `classify_and_eval.py` | XGBoost 3-class classification with statistical tests |\n| `eval_8gen_logo.py` | 8-generator LOGO evaluation (main paper results) |\n\n### Ablation and Analysis\n\n| Script | Description |\n|--------|-------------|\n| `eval_8gen_finer_depth.py` | 5-class vs 3-class depth granularity (Appendix D) |\n| `eval_8gen_sampling_ablation.py` | Training sample size ablation at 25/50/75/100% (Appendix H) |\n| `eval_8gen_cross_model_chains.py` | Cross-model chain extension evaluation (Appendix M) |\n| `eval_8gen_baselines_pooled.py` | Pooled LOGO with detector baselines (main paper) |\n| `cross_temp_transfer.py` | Cross-temperature transfer evaluation (Appendix O) |\n| `end_to_end_classifier.py` | QLoRA end-to-end depth classification (Appendix E) |\n| `distributional_tests.py` | KS + Levene distributional tests on features (Appendix N) |\n| `scripts/lofo_ablation.py` | Leave-one-feature-out ablation (Appendix F) |\n| `scripts/alt_classifier_eval.py` | XGBoost vs LogisticRegression vs RandomForest (Appendix H) |\n| `scripts/bootstrap_ci_v2.py` | Bootstrap 95% confidence intervals |\n| `scripts/tost_equivalence.py` | TOST equivalence testing for downstream results (Appendix L) |\n\n### Robustness and Controls\n\n| Script | Description |\n|--------|-------------|\n| `experiments/human_edit_robustness/run_robustness.py` | Word replacement robustness at 0/5/10/20% (Appendix I) |\n| `8gen_length_confound.py` | Length-matched confound control (Appendix B) |\n| `benchmark_efficiency.py` | Inference efficiency comparison |\n\n### Downstream Utility (Appendix L)\n\n| Script | Description |\n|--------|-------------|\n| `prepare_downstream_data.py` | Build depth-stratified training data variants |\n| `finetune_downstream.py` | Fine-tune causal LM on each variant, measure perplexity |\n| `bootstrap_downstream_ci.py` | Bootstrap CI and effect sizes for downstream results |\n\n### Dataset Statistics and Figures\n\n| Script | Description |\n|--------|-------------|\n| `compute_dataset_stats.py` | Per-generator dataset statistics (Appendix A) |\n| `scripts/plot_fig1_strip.py` | Figure 1: per-generator Spearman rho strip plot |\n| `scripts/plot_fig2.py` | Figure 2: LOGO grouped bar chart |\n| `scripts/plot_fig3.py` | Figure 3: baseline comparison forest plot |\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 6,
        "newStart": 2,
        "newLines": 18,
        "lines": [
          " ",
          " Code for reproducing the experiments in \"Generation Depth Fingerprinting.\"",
          " ",
          "+## Requirements",
          "+",
          "+- Python 3.10+",
          "+- CUDA-capable GPU (for generation, feature extraction, and end-to-end classifier)",
          "+- A reference language model (e.g., EleutherAI/pythia-410m) available locally or via HuggingFace Hub",
          "+",
          "+Install dependencies:",
          "+",
          "+```bash",
          "+pip install -r requirements.txt",
          "+```",
          "+",
          " ## Directory Structure",
          " ",
          " `code/` and `data/` are sibling directories under the supplement root. All scripts assume they are run from the `code/` directory and access data via `../data/`."
        ]
      },
      {
        "oldStart": 11,
        "oldLines": 30,
        "newStart": 23,
        "newLines": 37,
        "lines": [
          " ├── code/          # Scripts (this directory)",
          " │   ├── README.md",
          " │   ├── generate_chain.py",
          "-│   └── ...",
          "-└── data/          # Data files",
          "+│   ├── scripts/",
          "+│   └── experiments/",
          "+└── data/          # Data files (not included due to size; see data/README.md for format)",
          "     ├── README.md",
          "-    ├── features_8gen.csv",
          "+    ├── features_all_models.csv",
          "     └── ...",
          " ```",
          " ",
          "-## Setup",
          "+## Data Format",
          " ",
          "-```bash",
          "-pip install -r requirements.txt",
          "-```",
          "+**Features CSV** (`features_all_models.csv`): One row per text sample with columns:",
          " ",
          "-A CUDA-capable GPU is required for feature extraction and generation steps.",
          "-A reference language model (e.g., Pythia-410M) must be available locally.",
          "+| Column | Description |",
          "+|--------|-------------|",
          "+| `model_name` | Generator model identifier (e.g., `pythia-2.8b`) |",
          "+| `seed_id` | Wikipedia seed text identifier |",
          "+| `depth` | Generation depth (0 = human, 1 = first-gen, 2+ = deeper) |",
          "+| `entropy_mean` | Mean token-level entropy from reference model |",
          "+| `entropy_std` | Std dev of token-level entropy |",
          "+| `entropy_min` | Minimum token-level entropy |",
          "+| `entropy_max` | Maximum token-level entropy |",
          "+| `tail_decay` | Slope of sorted log-prob distribution (ranks 100-1000) |",
          "+| `ttr` | Type-token ratio |",
          "+| `hapax_ratio` | Proportion of words appearing exactly once |",
          " ",
          "-## Data Pipeline",
          "+**Generations JSONL**: One JSON object per line with fields `{\"seed_id\", \"depth\", \"text\", \"model_name\"}`.",
          " ",
          "-### 1. Seed Preparation",
          "+## Reproduction Steps",
          " ",
          "-Place Wikipedia seed texts in `../data/wiki_seed_1000.jsonl` (each line: `{\"id\", \"title\", \"text\"}`).",
          "+### 1. Generate continuation chains (depth 0 to 4)",
          " ",
          "-### 2. Generation (depth-0 to depth-4 continuations)",
          "-",
          " ```bash",
          " python generate_chain.py \\",
          "     --input ../data/wiki_seed_1000.jsonl \\"
        ]
      },
      {
        "oldStart": 46,
        "oldLines": 7,
        "newStart": 65,
        "newLines": 7,
        "lines": [
          " ",
          " Repeat for each generator model. Multi-GPU sharding is supported via `--shard-id` and `--num-shards`.",
          " ",
          "-### 3. Feature Extraction",
          "+### 2. Extract features",
          " ",
          " Extract 7 features (5 reference-model entropy features + 2 surface features) per text:",
          " "
        ]
      },
      {
        "oldStart": 58,
        "oldLines": 70,
        "newStart": 77,
        "newLines": 73,
        "lines": [
          "     --device cuda:0",
          " ```",
          " ",
          "-Alternative JSONL output format:",
          "+Alternative JSONL output: use `extract_features_jsonl.py` with the same arguments.",
          " ",
          "-```bash",
          "-python extract_features_jsonl.py \\",
          "-    --input ../data/generations.jsonl \\",
          "-    --output ../data/features.jsonl \\",
          "-    --ref-model /path/to/pythia-410m",
          "-```",
          "+### 3. Train classifier and evaluate",
          " ",
          "-### 4. Classification and Evaluation",
          "-",
          " Single-generator 3-class evaluation with Kruskal-Wallis tests:",
          " ",
          " ```bash",
          " python classify_and_eval.py --input ../data/features.csv --output results/mvp_results.json",
          " ```",
          " ",
          "-## Evaluation Scripts",
          "+### 4. LOGO evaluation (main results)",
          " ",
          "-### Core LOGO Evaluation",
          "+8-generator Leave-One-Generator-Out evaluation (3-class and binary):",
          " ",
          "-8-generator Leave-One-Generator-Out (3-class and binary):",
          "-",
          " ```bash",
          " python eval_8gen_logo.py",
          " ```",
          " ",
          "-### Ablation Studies",
          "+## Script Reference",
          " ",
          "+### Core Pipeline",
          "+",
          " | Script | Description |",
          " |--------|-------------|",
          "-| `eval_8gen_finer_depth.py` | 5-class vs 3-class depth granularity |",
          "-| `eval_8gen_sampling_ablation.py` | Training sample size ablation (25/50/75/100%) |",
          "-| `eval_8gen_cross_model_chains.py` | Cross-model chain extension evaluation |",
          "-| `scripts/lofo_ablation.py` | Leave-one-feature-out ablation |",
          "-| `scripts/alt_classifier_eval.py` | XGBoost vs LogisticRegression vs RandomForest |",
          "+| `generate_chain.py` | Generate depth-0 to depth-4 continuation chains |",
          "+| `extract_features.py` | Extract 7 features from text (CSV output) |",
          "+| `extract_features_jsonl.py` | Extract 7 features from text (JSONL output) |",
          "+| `classify_and_eval.py` | XGBoost 3-class classification with statistical tests |",
          "+| `eval_8gen_logo.py` | 8-generator LOGO evaluation (main paper results) |",
          "+",
          "+### Ablation and Analysis",
          "+",
          "+| Script | Description |",
          "+|--------|-------------|",
          "+| `eval_8gen_finer_depth.py` | 5-class vs 3-class depth granularity (Appendix D) |",
          "+| `eval_8gen_sampling_ablation.py` | Training sample size ablation at 25/50/75/100% (Appendix H) |",
          "+| `eval_8gen_cross_model_chains.py` | Cross-model chain extension evaluation (Appendix M) |",
          "+| `eval_8gen_baselines_pooled.py` | Pooled LOGO with detector baselines (main paper) |",
          "+| `cross_temp_transfer.py` | Cross-temperature transfer evaluation (Appendix O) |",
          "+| `end_to_end_classifier.py` | QLoRA end-to-end depth classification (Appendix E) |",
          "+| `distributional_tests.py` | KS + Levene distributional tests on features (Appendix N) |",
          "+| `scripts/lofo_ablation.py` | Leave-one-feature-out ablation (Appendix F) |",
          "+| `scripts/alt_classifier_eval.py` | XGBoost vs LogisticRegression vs RandomForest (Appendix H) |",
          " | `scripts/bootstrap_ci_v2.py` | Bootstrap 95% confidence intervals |",
          "+| `scripts/tost_equivalence.py` | TOST equivalence testing for downstream results (Appendix L) |",
          " ",
          " ### Robustness and Controls",
          " ",
          " | Script | Description |",
          " |--------|-------------|",
          "-| `experiments/human_edit_robustness/run_robustness.py` | Word replacement robustness (0/5/10/20%) |",
          "-| `8gen_length_confound.py` | Length-matched confound control |",
          "-| `eval_8gen_baselines_pooled.py` | Pooled LOGO with detector baselines |",
          "+| `experiments/human_edit_robustness/run_robustness.py` | Word replacement robustness at 0/5/10/20% (Appendix I) |",
          "+| `8gen_length_confound.py` | Length-matched confound control (Appendix B) |",
          " | `benchmark_efficiency.py` | Inference efficiency comparison |",
          " ",
          "-### Dataset and Figures",
          "+### Downstream Utility (Appendix L)",
          " ",
          " | Script | Description |",
          " |--------|-------------|",
          "-| `compute_dataset_stats.py` | Per-generator dataset statistics |",
          "+| `prepare_downstream_data.py` | Build depth-stratified training data variants |",
          "+| `finetune_downstream.py` | Fine-tune causal LM on each variant, measure perplexity |",
          "+| `bootstrap_downstream_ci.py` | Bootstrap CI and effect sizes for downstream results |",
          "+",
          "+### Dataset Statistics and Figures",
          "+",
          "+| Script | Description |",
          "+|--------|-------------|",
          "+| `compute_dataset_stats.py` | Per-generator dataset statistics (Appendix A) |",
          " | `scripts/plot_fig1_strip.py` | Figure 1: per-generator Spearman rho strip plot |",
          " | `scripts/plot_fig2.py` | Figure 2: LOGO grouped bar chart |",
          " | `scripts/plot_fig3.py` | Figure 3: baseline comparison forest plot |",
          "-",
          "-## Feature Descriptions",
          "-",
          "-| Feature | Type | Description |",
          "-|---------|------|-------------|",
          "-| `entropy_mean` | Reference | Mean token-level entropy from reference model |",
          "-| `entropy_std` | Reference | Standard deviation of token-level entropy |",
          "-| `entropy_min` | Reference | Minimum token-level entropy |",
          "-| `entropy_max` | Reference | Maximum token-level entropy |",
          "-| `tail_decay` | Reference | Slope of sorted log-prob distribution (ranks 100-1000) |",
          "-| `ttr` | Surface | Type-token ratio |",
          "-| `hapax_ratio` | Surface | Proportion of words appearing exactly once |"
        ]
      }
    ],
    "originalFile": "# Generation Depth Fingerprinting: Code Supplement\n\nCode for reproducing the experiments in \"Generation Depth Fingerprinting.\"\n\n## Directory Structure\n\n`code/` and `data/` are sibling directories under the supplement root. All scripts assume they are run from the `code/` directory and access data via `../data/`.\n\n```\nsupplement/\n├── code/          # Scripts (this directory)\n│   ├── README.md\n│   ├── generate_chain.py\n│   └── ...\n└── data/          # Data files\n    ├── README.md\n    ├── features_8gen.csv\n    └── ...\n```\n\n## Setup\n\n```bash\npip install -r requirements.txt\n```\n\nA CUDA-capable GPU is required for feature extraction and generation steps.\nA reference language model (e.g., Pythia-410M) must be available locally.\n\n## Data Pipeline\n\n### 1. Seed Preparation\n\nPlace Wikipedia seed texts in `../data/wiki_seed_1000.jsonl` (each line: `{\"id\", \"title\", \"text\"}`).\n\n### 2. Generation (depth-0 to depth-4 continuations)\n\n```bash\npython generate_chain.py \\\n    --input ../data/wiki_seed_1000.jsonl \\\n    --model-path /path/to/generator-model \\\n    --model-name pythia-2.8b \\\n    --output-dir ../data/ \\\n    --device cuda:0\n```\n\nRepeat for each generator model. Multi-GPU sharding is supported via `--shard-id` and `--num-shards`.\n\n### 3. Feature Extraction\n\nExtract 7 features (5 reference-model entropy features + 2 surface features) per text:\n\n```bash\npython extract_features.py \\\n    --input ../data/generations.jsonl \\\n    --output ../data/features.csv \\\n    --ref-model /path/to/pythia-410m \\\n    --device cuda:0\n```\n\nAlternative JSONL output format:\n\n```bash\npython extract_features_jsonl.py \\\n    --input ../data/generations.jsonl \\\n    --output ../data/features.jsonl \\\n    --ref-model /path/to/pythia-410m\n```\n\n### 4. Classification and Evaluation\n\nSingle-generator 3-class evaluation with Kruskal-Wallis tests:\n\n```bash\npython classify_and_eval.py --input ../data/features.csv --output results/mvp_results.json\n```\n\n## Evaluation Scripts\n\n### Core LOGO Evaluation\n\n8-generator Leave-One-Generator-Out (3-class and binary):\n\n```bash\npython eval_8gen_logo.py\n```\n\n### Ablation Studies\n\n| Script | Description |\n|--------|-------------|\n| `eval_8gen_finer_depth.py` | 5-class vs 3-class depth granularity |\n| `eval_8gen_sampling_ablation.py` | Training sample size ablation (25/50/75/100%) |\n| `eval_8gen_cross_model_chains.py` | Cross-model chain extension evaluation |\n| `scripts/lofo_ablation.py` | Leave-one-feature-out ablation |\n| `scripts/alt_classifier_eval.py` | XGBoost vs LogisticRegression vs RandomForest |\n| `scripts/bootstrap_ci_v2.py` | Bootstrap 95% confidence intervals |\n\n### Robustness and Controls\n\n| Script | Description |\n|--------|-------------|\n| `experiments/human_edit_robustness/run_robustness.py` | Word replacement robustness (0/5/10/20%) |\n| `8gen_length_confound.py` | Length-matched confound control |\n| `eval_8gen_baselines_pooled.py` | Pooled LOGO with detector baselines |\n| `benchmark_efficiency.py` | Inference efficiency comparison |\n\n### Dataset and Figures\n\n| Script | Description |\n|--------|-------------|\n| `compute_dataset_stats.py` | Per-generator dataset statistics |\n| `scripts/plot_fig1_strip.py` | Figure 1: per-generator Spearman rho strip plot |\n| `scripts/plot_fig2.py` | Figure 2: LOGO grouped bar chart |\n| `scripts/plot_fig3.py` | Figure 3: baseline comparison forest plot |\n\n## Feature Descriptions\n\n| Feature | Type | Description |\n|---------|------|-------------|\n| `entropy_mean` | Reference | Mean token-level entropy from reference model |\n| `entropy_std` | Reference | Standard deviation of token-level entropy |\n| `entropy_min` | Reference | Minimum token-level entropy |\n| `entropy_max` | Reference | Maximum token-level entropy |\n| `tail_decay` | Reference | Slope of sorted log-prob distribution (ranks 100-1000) |\n| `ttr` | Surface | Type-token ratio |\n| `hapax_ratio` | Surface | Proportion of words appearing exactly once |\n",
    "userModified": false
  }
}
````

</details>

---


### Assistant

_source line 288_

Now let me package and verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "130e6156-1a56-4a17-b4c9-aa5c75279b14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvpdDk9yifSMomisqVe9qQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 86556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1854
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 289_

<details open><summary>🔧 Tool call — Bash · `toolu_01LzsPNR325d1x11netGEfzn`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/supplement && zip -r /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/supplementary.zip code/ -x \"code/__pycache__/*\" \"code/.git/*\" \"*.pyc\"",
  "description": "Package supplement code into zip"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "8a67f0ba-2571-4e2d-ba88-72d360e50379",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvpdDk9yifSMomisqVe9qQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 86556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1854
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-17T21:23:41.324Z_

<details><summary>↩ Tool result · `toolu_01LzsPNR325d1x11netGEfzn`</summary>

```text
  adding: code/ (stored 0%)
  adding: code/end_to_end_classifier.py (deflated 69%)
  adding: code/scripts/ (stored 0%)
  adding: code/scripts/plot_fig3.py (deflated 62%)
  adding: code/scripts/tost_equivalence.py (deflated 62%)
  adding: code/scripts/plot_fig1_strip.py (deflated 60%)
  adding: code/scripts/plot_fig2.py (deflated 64%)
  adding: code/scripts/alt_classifier_eval.py (deflated 61%)
  adding: code/scripts/bootstrap_ci_v2.py (deflated 60%)
  adding: code/scripts/lofo_ablation.py (deflated 55%)
  adding: code/8gen_length_confound.py (deflated 67%)
  adding: code/eval_8gen_logo.py (deflated 68%)
  adding: code/eval_8gen_cross_model_chains.py (deflated 71%)
  adding: code/compute_dataset_stats.py (deflated 66%)
  adding: code/README.md (deflated 60%)
  adding: code/extract_features.py (deflated 65%)
  adding: code/prepare_downstream_data.py (deflated 68%)
  adding: code/requirements.txt (deflated 26%)
  adding: code/bootstrap_downstream_ci.py (deflated 61%)
  adding: code/distributional_tests.py (deflated 65%)
  adding: code/extract_features_jsonl.py (deflated 65%)
  adding: code/classify_and_eval.py (deflated 65%)
  adding: code/benchmark_efficiency.py (deflated 73%)
  adding: code/generate_chain.py (deflated 68%)
  adding: code/experiments/ (stored 0%)
  adding: code/experiments/human_edit_robustness/ (stored 0%)
  adding: code/experiments/human_edit_robustness/run_robustness.py (deflated 69%)
  adding: code/eval_8gen_sampling_ablation.py (deflated 71%)
  adding: code/eval_8gen_finer_depth.py (deflated 67%)
  adding: code/eval_8gen_baselines_pooled.py (deflated 69%)
  adding: code/cross_temp_transfer.py (deflated 66%)
  adding: code/finetune_downstream.py (deflated 68%)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "4a2e8bd1-dc2a-492f-ac98-7d4afb9368b1",
  "tool_use_result": {
    "stdout": "  adding: code/ (stored 0%)\n  adding: code/end_to_end_classifier.py (deflated 69%)\n  adding: code/scripts/ (stored 0%)\n  adding: code/scripts/plot_fig3.py (deflated 62%)\n  adding: code/scripts/tost_equivalence.py (deflated 62%)\n  adding: code/scripts/plot_fig1_strip.py (deflated 60%)\n  adding: code/scripts/plot_fig2.py (deflated 64%)\n  adding: code/scripts/alt_classifier_eval.py (deflated 61%)\n  adding: code/scripts/bootstrap_ci_v2.py (deflated 60%)\n  adding: code/scripts/lofo_ablation.py (deflated 55%)\n  adding: code/8gen_length_confound.py (deflated 67%)\n  adding: code/eval_8gen_logo.py (deflated 68%)\n  adding: code/eval_8gen_cross_model_chains.py (deflated 71%)\n  adding: code/compute_dataset_stats.py (deflated 66%)\n  adding: code/README.md (deflated 60%)\n  adding: code/extract_features.py (deflated 65%)\n  adding: code/prepare_downstream_data.py (deflated 68%)\n  adding: code/requirements.txt (deflated 26%)\n  adding: code/bootstrap_downstream_ci.py (deflated 61%)\n  adding: code/distributional_tests.py (deflated 65%)\n  adding: code/extract_features_jsonl.py (deflated 65%)\n  adding: code/classify_and_eval.py (deflated 65%)\n  adding: code/benchmark_efficiency.py (deflated 73%)\n  adding: code/generate_chain.py (deflated 68%)\n  adding: code/experiments/ (stored 0%)\n  adding: code/experiments/human_edit_robustness/ (stored 0%)\n  adding: code/experiments/human_edit_robustness/run_robustness.py (deflated 69%)\n  adding: code/eval_8gen_sampling_ablation.py (deflated 71%)\n  adding: code/eval_8gen_finer_depth.py (deflated 67%)\n  adding: code/eval_8gen_baselines_pooled.py (deflated 69%)\n  adding: code/cross_temp_transfer.py (deflated 66%)\n  adding: code/finetune_downstream.py (deflated 68%)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 291_

<details open><summary>🔧 Tool call — Bash · `toolu_01E3DrYcWH3jZ8ypkpRPDtYe`</summary>

```json
{
  "command": "unzip -p /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/supplementary.zip | grep -iEn '/root/|/home/ubuntu/|wandb|autodl|api.key|sk-|hf_|OPENAI_API_KEY' || echo \"NO LEAKS FOUND\"",
  "description": "Verify no sensitive info in zip"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "dbde68d7-5498-413d-9459-a1486435ee75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWwZ6oyGPnTPy68HneyG1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 88410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 812
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 292 · 2026-05-17T21:23:45.808Z_

<details><summary>↩ Tool result · `toolu_01E3DrYcWH3jZ8ypkpRPDtYe`</summary>

```text
NO LEAKS FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "f332e7ab-49c5-4d50-83c2-224aa496a83f",
  "tool_use_result": {
    "stdout": "NO LEAKS FOUND",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 293_

<details open><summary>🔧 Tool call — Bash · `toolu_01EaozfYbYKr3iEtSeErA1cY`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/supplementary.zip",
  "description": "Check zip file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "f8456d96-5922-4615-9e8a-a009e413f24a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWwZ6oyGPnTPy68HneyG1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 88410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 812
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 294 · 2026-05-17T21:23:46.717Z_

<details><summary>↩ Tool result · `toolu_01EaozfYbYKr3iEtSeErA1cY`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 76K May 17 21:23 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/supplementary.zip
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "67590110-5f9f-4e3c-a349-1daa7c24682a",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 76K May 17 21:23 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/supplementary.zip",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 295_

<details open><summary>🔧 Tool call — Bash · `toolu_01W9CqQRpBwgr67MrRvmyqjN`</summary>

```json
{
  "command": "unzip -l /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/supplementary.zip",
  "description": "List zip contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "bc12b9d3-34b5-4494-ab43-ccb4dbcdc564",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWwZ6oyGPnTPy68HneyG1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 88410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 812
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 296 · 2026-05-17T21:23:47.083Z_

<details><summary>↩ Tool result · `toolu_01W9CqQRpBwgr67MrRvmyqjN`</summary>

```text
Archive:  /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/supplementary.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-05-17 21:23   code/
    11068  2026-05-17 21:21   code/end_to_end_classifier.py
        0  2026-05-17 21:23   code/scripts/
     4506  2026-05-17 13:28   code/scripts/plot_fig3.py
     3644  2026-05-17 21:23   code/scripts/tost_equivalence.py
     4754  2026-05-17 13:01   code/scripts/plot_fig1_strip.py
     4401  2026-05-17 13:28   code/scripts/plot_fig2.py
     4187  2026-05-17 13:28   code/scripts/alt_classifier_eval.py
     4848  2026-05-17 13:28   code/scripts/bootstrap_ci_v2.py
     2812  2026-05-17 13:28   code/scripts/lofo_ablation.py
     9089  2026-05-17 13:28   code/8gen_length_confound.py
     7812  2026-05-17 13:31   code/eval_8gen_logo.py
    25679  2026-05-17 13:28   code/eval_8gen_cross_model_chains.py
     2280  2026-05-17 13:28   code/compute_dataset_stats.py
     5468  2026-05-17 21:23   code/README.md
     7828  2026-05-17 13:29   code/extract_features.py
     8106  2026-05-17 21:20   code/prepare_downstream_data.py
      142  2026-05-17 13:07   code/requirements.txt
     4425  2026-05-17 21:20   code/bootstrap_downstream_ci.py
     3538  2026-05-17 21:22   code/distributional_tests.py
     4552  2026-05-17 12:55   code/extract_features_jsonl.py
     9548  2026-05-17 13:29   code/classify_and_eval.py
    14948  2026-05-17 13:28   code/benchmark_efficiency.py
     8198  2026-05-17 13:29   code/generate_chain.py
        0  2026-05-17 12:52   code/experiments/
        0  2026-05-17 13:28   code/experiments/human_edit_robustness/
    13854  2026-05-17 13:28   code/experiments/human_edit_robustness/run_robustness.py
    18384  2026-05-17 13:28   code/eval_8gen_sampling_ablation.py
     7216  2026-05-17 13:28   code/eval_8gen_finer_depth.py
    11565  2026-05-17 13:28   code/eval_8gen_baselines_pooled.py
     8191  2026-05-17 21:22   code/cross_temp_transfer.py
     5853  2026-05-17 21:20   code/finetune_downstream.py
---------                     -------
   216896                     32 files
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "72445423-b095-4012-961b-0fc5a464a759",
  "tool_use_result": {
    "stdout": "Archive:  /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/supplementary.zip\n  Length      Date    Time    Name\n---------  ---------- -----   ----\n        0  2026-05-17 21:23   code/\n    11068  2026-05-17 21:21   code/end_to_end_classifier.py\n        0  2026-05-17 21:23   code/scripts/\n     4506  2026-05-17 13:28   code/scripts/plot_fig3.py\n     3644  2026-05-17 21:23   code/scripts/tost_equivalence.py\n     4754  2026-05-17 13:01   code/scripts/plot_fig1_strip.py\n     4401  2026-05-17 13:28   code/scripts/plot_fig2.py\n     4187  2026-05-17 13:28   code/scripts/alt_classifier_eval.py\n     4848  2026-05-17 13:28   code/scripts/bootstrap_ci_v2.py\n     2812  2026-05-17 13:28   code/scripts/lofo_ablation.py\n     9089  2026-05-17 13:28   code/8gen_length_confound.py\n     7812  2026-05-17 13:31   code/eval_8gen_logo.py\n    25679  2026-05-17 13:28   code/eval_8gen_cross_model_chains.py\n     2280  2026-05-17 13:28   code/compute_dataset_stats.py\n     5468  2026-05-17 21:23   code/README.md\n     7828  2026-05-17 13:29   code/extract_features.py\n     8106  2026-05-17 21:20   code/prepare_downstream_data.py\n      142  2026-05-17 13:07   code/requirements.txt\n     4425  2026-05-17 21:20   code/bootstrap_downstream_ci.py\n     3538  2026-05-17 21:22   code/distributional_tests.py\n     4552  2026-05-17 12:55   code/extract_features_jsonl.py\n     9548  2026-05-17 13:29   code/classify_and_eval.py\n    14948  2026-05-17 13:28   code/benchmark_efficiency.py\n     8198  2026-05-17 13:29   code/generate_chain.py\n        0  2026-05-17 12:52   code/experiments/\n        0  2026-05-17 13:28   code/experiments/human_edit_robustness/\n    13854  2026-05-17 13:28   code/experiments/human_edit_robustness/run_robustness.py\n    18384  2026-05-17 13:28   code/eval_8gen_sampling_ablation.py\n     7216  2026-05-17 13:28   code/eval_8gen_finer_depth.py\n    11565  2026-05-17 13:28   code/eval_8gen_baselines_pooled.py\n     8191  2026-05-17 21:22   code/cross_temp_transfer.py\n     5853  2026-05-17 21:20   code/finetune_downstream.py\n---------                     -------\n   216896                     32 files",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 297_

Done. Here's a summary:

**Anonymization**: All 26 `.py` files and README are clean. No `/root/`, `/home/ubuntu/`, wandb, autodl, API keys, or author info found in the zip.

**New scripts added** (6 files from server, anonymized):
| File | Anonymization fix |
|------|------------------|
| `prepare_downstream_data.py` | Default paths changed to `../data/`; removed duplicate buggy `save_jsonl` |
| `finetune_downstream.py` | Removed `/root/autodl-tmp/...` from docstring usage example |
| `bootstrap_downstream_ci.py` | `BASE` path changed from `/root/autodl-tmp/...` to `experiments/downstream` |
| `end_to_end_classifier.py` | Removed internal experiment name from output dir; generalized output path |
| `cross_temp_transfer.py` | Already clean (uses `__file__`-relative paths); adjusted DATA_DIR to `../data` |
| `distributional_tests.py` | `DATA_PATH` and `OUT_PATH` changed from `/root/gen-depth-fingerprint/...` to relative |
| `scripts/tost_equivalence.py` | Output path changed from `/root/gen-depth-fingerprint/...` to `results/` |

**README updated**: Added data format docs, full script reference with appendix mappings, downstream utility section, requirements section.

**Package**: `supplementary.zip` = **76 KB**, 32 files (26 `.py` + 1 `.md` + 1 `.txt` + 4 dirs).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "uuid": "1cdd792d-e74f-47c2-89c2-cfbfa48b6a19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oShUk25oSJYydMvjJTJoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1387,
      "cache_read_input_tokens": 89222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1387
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 298_

Done. Here's a summary:

**Anonymization**: All 26 `.py` files and README are clean. No `/root/`, `/home/ubuntu/`, wandb, autodl, API keys, or author info found in the zip.

**New scripts added** (6 files from server, anonymized):
| File | Anonymization fix |
|------|------------------|
| `prepare_downstream_data.py` | Default paths changed to `../data/`; removed duplicate buggy `save_jsonl` |
| `finetune_downstream.py` | Removed `/root/autodl-tmp/...` from docstring usage example |
| `bootstrap_downstream_ci.py` | `BASE` path changed from `/root/autodl-tmp/...` to `experiments/downstream` |
| `end_to_end_classifier.py` | Removed internal experiment name from output dir; generalized output path |
| `cross_temp_transfer.py` | Already clean (uses `__file__`-relative paths); adjusted DATA_DIR to `../data` |
| `distributional_tests.py` | `DATA_PATH` and `OUT_PATH` changed from `/root/gen-depth-fingerprint/...` to relative |
| `scripts/tost_equivalence.py` | Output path changed from `/root/gen-depth-fingerprint/...` to `results/` |

**README updated**: Added data format docs, full script reference with appendix mappings, downstream utility section, requirements section.

**Package**: `supplementary.zip` = **76 KB**, 32 files (26 `.py` + 1 `.md` + 1 `.txt` + 4 dirs).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 493887,
  "duration_api_ms": 553354,
  "num_turns": 32,
  "stop_reason": "end_turn",
  "session_id": "37472f2c-1632-4d9a-9ece-c6bb70529f6d",
  "total_cost_usd": 1.9998144999999998,
  "usage": {
    "input_tokens": 2439,
    "cache_creation_input_tokens": 78768,
    "cache_read_input_tokens": 730478,
    "output_tokens": 25159,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 78768,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 396,
        "cache_read_input_tokens": 89222,
        "cache_creation_input_tokens": 1387,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1387
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2333,
      "outputTokens": 10732,
      "cacheReadInputTokens": 939210,
      "cacheCreationInputTokens": 98647,
      "webSearchRequests": 0,
      "costUSD": 0.27322274999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2447,
      "outputTokens": 27964,
      "cacheReadInputTokens": 783701,
      "cacheCreationInputTokens": 99745,
      "webSearchRequests": 0,
      "costUSD": 1.7265917499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1579a76d-af99-474e-979b-794d5e81ff3b"
}
```

</details>

---
