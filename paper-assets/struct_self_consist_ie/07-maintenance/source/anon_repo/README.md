# When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap

Code and data for our EMNLP 2026 ARR submission.

## Abstract

Test-time compute scaling via repeated sampling yields large gains on discrete-answer reasoning, but whether these gains transfer to named entity recognition (NER) remains open. Across four NER datasets with fine-tuned 7--14B models, we find that quality estimation signals predict output quality well (AUROC up to 0.82), yet selecting among candidates produces no detectable improvement over greedy decoding, even with 64 samples. We term this disconnect the **correlation-selection gap** and trace it to two co-occurring conditions: *degeneracy*, where multiple samples collapse to identical predictions, and *signal alignment collapse*, where per-sample scores fail to discriminate quality within an instance. Entity-level construction offers conditional gains (+1.40 pp on Few-NERD) where the framework identifies favorable conditions, but exhibits inverse scaling in most configurations. Cross-task pilots on relation extraction (RE) and SQL parsing confirm task-specific failure modes. The framework is primarily diagnostic, informing when repeated sampling helps for structured prediction and when greedy decoding remains the better default.

## Repository Structure

```
code/               # Core experiment code (training, inference, analysis)
scripts/            # Analysis and visualization scripts
experiments/        # Cross-task extension experiments (RE, SQL)
figures/            # Generated figures
results/            # Experiment outputs and intermediate results
artifacts/          # Aggregated analysis artifacts
```

## Key Components

- **Training**: LoRA fine-tuning configs for Qwen3-8B and LLaMA-3.1-8B on NER datasets (SciERC, CoNLL-2003, Few-NERD, WNUT-17)
- **Inference**: Multi-sample generation with vLLM constrained decoding (`code/run_*.py`)
- **Diagnostic Framework**: Five quality estimation signals (LP, SJ, VC, EM, FK) with instance-level decomposition (`code/analyze_*.py`)
- **Entity Construction**: MBR-based entity-level aggregation with threshold sweep (`scripts/epsilon_sweep.py`, `scripts/entity_independence_*.py`)
- **Cross-task Extensions**: Relation extraction and SQL parsing pilots (`experiments/`)

## Requirements

- Python 3.10+
- PyTorch 2.x with CUDA
- vLLM (for constrained decoding)
- LLaMA Factory (for LoRA fine-tuning)
- Standard scientific stack: numpy, scipy, scikit-learn, matplotlib
