# Experiment Setup

## 4.1 Datasets

**Human data.**
We sample a subset of FineWeb (Penedo et al., 2024), a large-scale deduplicated web corpus, as the source of human-authored text. The subset is used both for language model pretraining and as the seed corpus for synthetic data generation.

**Synthetic data.**
We generate synthetic continuations using Qwen3-0.6B (depth-1), producing approximately 132M tokens. Generation is parallelized across 4 GPUs with distinct random seeds (42, 1042, 2042, 3042) to ensure diversity while maintaining reproducibility. Each generation instance performs greedy continuation from FineWeb prompts, simulating the single-depth contamination scenario where LLM-generated text enters web corpora through a single pass of model output.

**Mixed training corpus.**
We construct a contaminated training set of 371,499 documents by mixing human and synthetic text at a contamination ratio $\rho = 0.4$ (40% synthetic). This ratio reflects empirical estimates of synthetic content prevalence in contemporary web crawls (Drayson et al., 2025). Each document is annotated with a binary provenance label (human/synthetic) used exclusively for oracle evaluation; the training pipeline operates without access to these labels.

**Held-out evaluation set.**
We reserve a held-out evaluation split (`eval_holdout.jsonl`) consisting of pure FineWeb human-authored text totaling approximately 4.08M tokens. This set is disjoint from the training corpus and contains no synthetic text, enabling unbiased evaluation of language modeling quality on the target distribution.

**Detector training data.**
A separate balanced split of 67,960 documents (human and synthetic) is used to train the contamination detector (Section 4.2), with no overlap with the language model training or evaluation data.

## 4.2 Contamination Detector

We train a lightweight contamination detector to produce per-document synthetic probability scores $q(x) = \hat{P}(\text{synthetic} \mid x)$.

**Architecture.**
We use a TF-IDF feature extractor with bigram features followed by logistic regression. This deliberately simple architecture is motivated by our finding that high-capacity detectors (e.g., ModernBERT, AUC = 0.9998) produce near-binary $q$-scores concentrated at 0 and 1, which collapse the weighting function $w = (1-q)^b$ to a binary filter regardless of $b$ (Section 5, Claim 2). In contrast, the TF-IDF + logistic regression detector produces a continuous $q$-score distribution (mean = 0.60, std = 0.374, median = 0.707, mid-range ratio = 0.463) that enables meaningful differentiation across the weighting exponent $b$.

**Calibration.**
We apply temperature scaling with $T = 0.204$ to calibrate the detector's output probabilities, achieving an expected calibration error (ECE) of 0.048 post-calibration.

**Performance.**
The detector achieves AUC = 0.939 on held-out evaluation. While substantially below state-of-the-art neural detectors, this performance level is sufficient—and arguably preferable—for our adaptive reweighting framework, as we demonstrate in the results.

## 4.3 Language Model Configuration

**Base model.**
We use Qwen3-0.6B (Yang et al., 2025) as the base language model, performing continued pretraining from the publicly released checkpoint rather than training from scratch. This setup mirrors the practical scenario where a pretrained model is further trained on web-crawled data of uncertain provenance.

**Training hyperparameters.**
We train for 200M tokens (6,103 optimization steps) with the following configuration:

| Parameter | Value |
|---|---|
| Micro batch size | 4 |
| Gradient accumulation steps | 4 |
| Effective batch size | 16 |
| Sequence length | 2,048 |
| Learning rate | 5e-5 |
| Precision | bfloat16 |
| Checkpoint save interval | 500 steps |
| Evaluation interval | 500 steps |
| Maximum saved checkpoints | 2--3 |

All experimental conditions share identical hyperparameters except for the sample weighting scheme.

## 4.4 Weighting Methods

We compare three approaches to handling synthetic contamination during training, all operating on per-sample weights applied to the cross-entropy loss.

**Uniform baseline.**
All training samples receive unit weight $w_i = 1$, regardless of provenance. This represents standard training without contamination mitigation.

**Grid-$b$ weighting (Drayson et al., 2025).**
Each sample receives weight $w_i = (1 - q(x_i))^b$ where $q(x_i)$ is the calibrated detector score and $b$ is a fixed exponent selected from a grid: $b \in \{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$. The best $b$ is selected post hoc based on held-out perplexity, following the validation-based tuning protocol of Drayson et al. (2025).

**Adaptive $b^*$ (ours).**
We derive the weighting exponent dynamically per batch from the effective real fraction:
$$\alpha_{\text{eff}}(b) = \frac{\sum_i (1 - q_i)^{b+1}}{\sum_i (1 - q_i)^b}$$

The optimal exponent $b^*$ is computed as:
$$b^* = \inf\{b \geq 0 : \alpha_{\text{eff}}(b) \geq \tau\} \quad \text{s.t.} \quad \text{ESS}(b^*) \geq n_{\min}$$

where the effective sample size is $\text{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$, $\tau = 0.8$ is the target effective real fraction (derived from contamination ratio $\rho = 0.4$ as $\tau = 1 - \rho/2$), and $n_{\min} = 2$ is the minimum ESS constraint for stable gradient estimates. When $\alpha_{\text{eff}}(0) \geq \tau$ (low-contamination batch), uniform weights are used ($b^* = 0$). $b^*$ is computed independently for each mini-batch based on the current batch's score distribution; no cross-batch smoothing or state is maintained. The resulting $b^*$ values typically range from 0.2 to 0.8, with occasional excursions up to 3.8 for heavily contaminated batches.

## 4.5 Evaluation Protocol

**Primary metric.**
We report held-out perplexity computed on the pure-human evaluation set (Section 4.1) using unweighted cross-entropy loss. Critically, evaluation uses standard (unweighted) cross-entropy regardless of the training weighting scheme, ensuring fair comparison across methods—the weighted training loss used by grid-$b$ and adaptive methods is not directly comparable to the uniform baseline's unweighted training loss.

**Statistical reliability.**
All experiments are conducted with 3 random seeds (42, 123, 456). We report mean and standard deviation of held-out perplexity across seeds. [*Note: seed 456 grid-$b$ results and adaptive\_v2 (n\_min=2) results for all seeds are pending completion.*]

**Evaluation schedule.**
Held-out perplexity is computed every 500 training steps via an automated evaluation watcher that scans for new checkpoints at 60-second intervals, ensuring complete evaluation coverage without manual intervention.

## 4.6 Hardware and Compute

**GPU configuration.**
All experiments are conducted on a single node equipped with 4$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96 GB VRAM each). Training runs are assigned to individual GPUs to avoid memory contention; diagnostic and evaluation tasks are scheduled on GPUs with available headroom.

**Training time.**
Each training run (200M tokens, 6,103 steps) takes 3.3–4.2 hours per run depending on the weighting method. The complete MVP experiment matrix (1 uniform + 6 grid-$b$ + 1 adaptive per seed, 3 seeds) requires approximately 70 GPU-hours. Synthetic data generation (132M tokens, 4 GPU-parallel) requires approximately 4 GPU-hours.

**Budget.**
The MVP phase consumes approximately 70–85 GPU-hours across all experiments (baselines, grid search, and adaptive runs with three seeds). The full experimental plan (multiple contamination ratios, larger models, cross-generator evaluation) is budgeted at approximately 180 GPU-hours total, well within the 200 H100-hour-equivalent constraint.

---

## Preliminary Results (Seed 123, n_min=3, legacy version)

For reference, we include the complete seed 123 results that motivate the adaptive approach:

| Method | Eval PPL | $\Delta$ vs. Uniform |
|---|---|---|
| Uniform | 17.690 | — |
| Grid $b=0.5$ (best) | 17.638 | $-$0.052 |
| Grid $b=1.0$ | 17.674 | $-$0.016 |
| Grid $b=1.5$ | 17.701 | +0.011 |
| Grid $b=2.0$ | 17.725 | +0.035 |
| Grid $b=3.0$ | 17.760 | +0.070 |
| Grid $b=5.0$ | 17.804 | +0.114 |
| Adaptive ($n_{\min}=3$) | 17.630 | $-$0.060 |

Perplexity increases monotonically with $b$, with only $b \leq 1.0$ improving over uniform. The adaptive method achieves the lowest perplexity (17.630), outperforming even the best grid-searched $b=0.5$ (17.638) without requiring any validation-based tuning.

[*Pending: adaptive\_v2 ($n_{\min}=2$) results across all seeds; seed 456 grid-$b$ sweep; full 3-seed statistical summary.*]
