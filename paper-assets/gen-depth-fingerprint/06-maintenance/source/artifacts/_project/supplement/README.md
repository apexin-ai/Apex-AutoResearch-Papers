# Supplementary Materials

Code and data for reproducing the experiments in "Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains."

## Structure

```
supplement/
├── README.md           (this file)
├── code/               Scripts for generation, feature extraction, and evaluation
│   ├── README.md       Detailed script reference and reproduction steps
│   ├── requirements.txt
│   ├── scripts/        Analysis and plotting scripts
│   └── experiments/    Robustness experiments
└── data/               Feature datasets and evaluation results
    ├── README.md       Data format documentation and column descriptions
    ├── seeds/          Seed passages (Wikipedia, news, creative, scientific)
    └── cross-model-chains/
```

## Quick Start

```bash
cd code/
pip install -r requirements.txt

# Generate chains, extract features, train classifier
python generate_chain.py --input ../data/wiki_seed_1000.jsonl --model-path <model> --output-dir ../data/
python extract_features.py --input ../data/generations.jsonl --output ../data/features.csv --ref-model <ref-model>
python classify_and_eval.py --input ../data/features.csv

# Main result: 9-generator LOGO evaluation
python eval_9gen_logo.py
```

See `code/README.md` for full reproduction instructions and script reference.
See `data/README.md` for dataset descriptions and column definitions.
