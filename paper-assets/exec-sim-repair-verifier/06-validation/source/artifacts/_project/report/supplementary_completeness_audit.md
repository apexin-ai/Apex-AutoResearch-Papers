# Supplementary Completeness Audit

## Summary

| Category | Count |
|----------|-------|
| Total success experiments | 132 |
| Referenced in paper (Tables/Sections/Appendix) | 88 |
| Potentially valuable omissions | 28 |
| Not applicable (training runs / intermediate / superseded) | 16 |

---

## Referenced Experiments

### Table 1 — Function-Level Per-Test Accuracy (n=1,890)

| exp_id | metric | where cited |
|--------|--------|-------------|
| multi-seed-core | CLS 4B 3-seed (s42/123/456) | Table 1 (5-seed mean 88.43±0.78) |
| cls-seed789 | acc=89.00 | Table 1 (contributes to 5-seed mean) |
| cls-seed0 | acc=87.94 | Table 1 (contributes to 5-seed mean) |
| per-test-precision-recall | CWM 4B s42=87.51 | Table 1 (5-seed mean 87.19±0.37) |
| cwm-seed123 | acc=87.20 | Table 1 |
| cwm-seed456 | acc=86.98 | Table 1 |
| cwm-seed789 | acc=86.67 | Table 1 |
| cwm-seed0 | acc=87.57 | Table 1 |
| traj-level-finetuned | acc=85.66 | Table 1 (TRAJ 4B 5-seed mean 86.30±0.97) |
| traj-level-seed123 | acc=85.47 | Table 1 |
| traj-level-seed456 | acc=87.40 | Table 1 |
| traj-level-seed789 | acc=87.31 | Table 1 |
| traj-level-seed0 | acc=85.66 | Table 1 |
| deepseek-cls-func | CLS DeepSeek s42 | Table 1 (2-seed mean 86.85±0.11) |
| deepseek-cls-func-s123 | CLS DeepSeek s123 | Table 1 |
| deepseek-cwm-func | CWM DeepSeek s42 | Table 1 (2-seed mean 86.83±1.49) |
| deepseek-cwm-func-s123 | CWM DeepSeek s123 | Table 1 |
| deepseek-traj-func-v2 | TRAJ DeepSeek s42 | Table 1 (2-seed mean 84.16±1.30) |
| deepseek-traj-func-v2-s123 | TRAJ DeepSeek s123 | Table 1 |
| qwen3-0shot-func-baseline | acc=68.70 | Table 1 (0-shot Qwen3-8B) |
| deepseek-0shot-func-baseline | acc=63.00 | Table 1 (0-shot DeepSeek) |
| llm-judge-8b-zeroshot | acc=64.40 | Table 1 (ZS LLM-as-judge 8B) |
| llm-judge-32b-zeroshot | acc=71.69 | Table 1 (ZS LLM-as-judge 32B NF4) |
| exp-e-qwen3-3shot-baseline | 3-shot Qwen3 | Table 1 (3-shot ICL 68.78) |

### Table 2 — Model-Size Scaling (Qwen3, seeds 42/123, bf16)

| exp_id | metric | where cited |
|--------|--------|-------------|
| model-size-scaling-cls8b | CLS 8B s42=90.48 | Table 2 |
| cls8b-seed123 | CLS 8B s123=89.40 | Table 2 |
| model-size-scaling-cwm8b | CWM 8B s42=87.67 | Table 2 |
| cwm8b-seed123 | CWM 8B s123=86.98 | Table 2 |
| qwen3-8b-traj-func-s42 | TRAJ 8B s42 | Table 2 (TRAJ 8B s42=87.60) |
| qwen3-8b-traj-func-s123 | TRAJ 8B s123 | Table 2 (TRAJ 8B s123=87.79) |
| cls8b-seed456 | CLS 8B s456=88.31 | §5.2 (3-seed clustered bootstrap p=0.0066) |
| cwm8b-seed456 | CWM 8B s456=86.24 | §5.2 (3-seed clustered bootstrap) |

### Table 3 — Repo-Level Cross-Formulation

| exp_id | metric | where cited |
|--------|--------|-------------|
| cls4b-v5-ckpt4600-test-eval | CLS 4B s42=83.63 | Table 3 |
| cls8b-s42-resume-ckpt3600-test-v2 | CLS 8B s42=84.48 | Table 3 |
| cls8b-seed123-ckpt3000-test8192-eval | CLS 8B s123=85.60 | Table 3 |
| cls8b-repo-s456-eval-v2 | CLS 8B s456=84.40 | Table 3 (mean 84.83±0.67) |
| deepseek-cls-repo-v5-ckpt2105-eval | DeepSeek CLS s42 e1=82.61 | Table 3 |
| deepseek-cls-repo-v5-ckpt6315-eval | DeepSeek CLS s42 e3=82.51 | App: variant-level table |
| deepseek-cls-repo-s123 | DeepSeek CLS s123=74.93 | Table 3 |
| deepseek-cls-repo-s456-eval-v2 | DeepSeek CLS s456=86.15 | Table 3 (2-seed mean 84.38±2.50) |
| cwm4b-s42-mutation-breakdown | CWM 4B=58.04 | Table 3 |
| qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval | CWM 8B seq4096=64.36 | App: threats/seq-length |
| deepseek-cwm-repo-s42-seq4096-eval | DeepSeek CWM=61.49 | Table 3 |
| qwen3-4b-traj-repo-s42-eval | TRAJ 4B=72.92 | Table 3 |
| qwen3-8b-traj-repo-s42-ckpt98-eval | TRAJ 8B epoch 2=72.92 | Table 3 / App: threats |
| qwen3-8b-traj-repo-s42-best-eval | TRAJ 8B epoch 3=70.83 | App: threats (TRAJ epoch comparison) |
| qwen3-8b-traj-repo-s123 | TRAJ 8B s123=77.08 | Table 3 (3-seed mean 72.91±3.61) |
| qwen3-8b-traj-repo-s456 | TRAJ 8B s456=70.83 | Table 3 |
| deepseek-traj-repo | DeepSeek TRAJ s42 | Table 3 |
| deepseek-traj-repo-8k | DeepSeek TRAJ 8k s42=81.25 | Table 3 |
| deepseek-traj-repo-8k-s123 | variant=75.00 | Table 3 (3-seed mean 77.08±3.61) |
| deepseek-traj-repo-8k-s456 | variant=75.00 | Table 3 |
| deepseek-traj-repo-s123 | variant=77.08 | Table 3 |
| deepseek-traj-repo-8k-s0 | variant=75.00 | App: 6-seed TRAJ (mean 75.35±5.00) |
| deepseek-traj-repo-8k-s789 | variant=66.67 | App: 6-seed TRAJ |
| deepseek-traj-repo-8k-s999 | variant=79.17 | App: 6-seed TRAJ |
| repo-level-0shot-baseline | 0-shot Qwen=49.90 | Table 3 |
| deepseek-0shot-repo-baseline | 0-shot DeepSeek=48.50 | Table 3 |

### Statistical Analysis (§5.2, §5.3, Appendix)

| exp_id | metric | where cited |
|--------|--------|-------------|
| 5-paired-clustered-bootstrap | gap=-0.45pp, TOST p=0.007 | §5.2 equivalence, App: TOST/Holm |
| block-corr-empirical | ICC=0.191, DEFF=3.97 | §5.3, App (f) |
| oracle-f2p-stratified | block_adv=10.93pp | §5.3, App oracle table + Figure 3 |
| mvp-a-oracle-sim | oracle routing | §5.3 (oracle concept) |
| exp-a-routing | oracle routing=100% | §5.3 (oracle CLS-CWM routing) |
| exp-b-complexity-bin | complexity analysis | §5 analysis (T-based binning) |

### Appendix — Ablation / Control Experiments

| exp_id | metric | where cited |
|--------|--------|-------------|
| cwm-rank32-ablation-v2 | acc=87.00 | App: LoRA rank ablation table |
| cwm-rank32-alpha64-ablation | acc=87.04 | App: LoRA rank ablation table |
| cls8b-s42-ckpt3600-seq2048-ablation | acc=83.04 | App: seq-length ablation |
| cls8b-s42-ckpt-ablation | ckpt-2200=85.34, ckpt-6633=85.29 | App: threats (checkpoint selection <1pp) |
| exp-downsample-cls-func-v3-eval | acc=80.74 | App: downsample control |
| exp-downsample-cls-func-v3 | training run | App: downsample (produces model) |
| exp-d-constrained-decoding | CWM constrained | App (b) unparseable analysis |
| repo-level-3shot-baseline | per_test=46.28 | App: few-shot table |
| cls4b-ckpt4600-test-mutation-pr | CLS 4B mutation data | App: per-mutation table |
| cls8b-s42-resume-ckpt3600-mutation | CLS 8B s42 mutation data | App: per-mutation table |
| cls8b-seed123-ckpt3000-mutation | CLS 8B s123 mutation data | App: per-mutation table |

---

## Potentially Valuable Omissions

### Priority 1: Checkpoint Val/Test Sweep Curves (28 experiments)

**These ~28 experiments form complete val+test training curves for CLS 4B and 8B across seeds 42/123. The paper mentions "checkpoint selection: <1pp" and references 3 specific checkpoints in Threats, but does NOT include a supplementary figure showing the full training dynamics.**

A checkpoint sweep figure would:
- Visually demonstrate the <1pp checkpoint selection claim
- Show val-test correlation (or lack thereof)
- Strengthen the "no cherry-picking" argument
- Provide diagnostic value for reproducibility

**Suggested: Appendix supplementary figure with val/test curves**

#### 4B Seed 42 Val Sweep (6 experiments)
| exp_id | checkpoint | val acc (%) |
|--------|-----------|-------------|
| cls4b-v5-ckpt600-val5120-eval | ckpt-600 | 82.82 |
| cls4b-v5-ckpt4000-val5120-eval | ckpt-4000 | 89.84 |
| cls4b-v5-val-sweep-ckpt4200 | ckpt-4200 | 89.06 |
| cls4b-v5-val-sweep-ckpt4400-v3 | ckpt-4400 | 89.96 |
| cls4b-v5-val-sweep-ckpt4600 | ckpt-4600 | 90.07 |
| cls4b-seed123-ckpt800-val5120-eval | s123 ckpt-800 | 87.92 |

#### 4B Seed 42 Test Sweep (2 experiments)
| exp_id | checkpoint | test acc (%) |
|--------|-----------|-------------|
| cls4b-v5-ckpt600-test5120-eval | ckpt-600 | 77.74 |
| cls4b-v5-ckpt4400-test5120-eval | ckpt-4400 | 83.24 |

#### 8B Seed 42 Val Sweep (7 experiments)
| exp_id | checkpoint | val acc (%) |
|--------|-----------|-------------|
| cls8b-s42-ckpt200-val8192-eval-v2 | ckpt-200 | 63.52 |
| cls8b-s42-ckpt800-val8192-eval | ckpt-800 | 84.50 |
| cls8b-s42-ckpt1000-val8192-eval | ckpt-1000 | 88.23 |
| cls8b-s42-ckpt1200-val8192-v3 | ckpt-1200 | 87.76 |
| cls8b-s42-ckpt1400-val8192-eval | ckpt-1400 | 85.97 |
| cls8b-s42-ckpt1600-val8192-v2 | ckpt-1600 | 86.75 |
| cls8b-s42-resume-val-sweep-seq8192-v2 | 21 ckpts (1800-5800) | sweep data |

#### 8B Seed 42 Test Sweep (8 experiments)
| exp_id | checkpoint | test acc (%) |
|--------|-----------|-------------|
| cls8b-s42-ckpt200-test8192-eval | ckpt-200 | 70.07 |
| cls8b-s42-ckpt400-test8192-eval | ckpt-400 | 84.79 |
| cls8b-s42-ckpt600-test8192-eval | ckpt-600 | 79.05 |
| cls8b-s42-ckpt800-test8192-eval | ckpt-800 | 83.53 |
| cls8b-s42-ckpt1000-test8192-eval | ckpt-1000 | 83.52 |
| cls8b-s42-ckpt1200-test8192-eval | ckpt-1200 | 83.84 |
| cls8b-s42-ckpt1400-test8192-eval | ckpt-1400 | 85.47 |
| cls8b-s42-ckpt1600-test8192-eval | ckpt-1600 | 84.99 |

#### 8B Seed 123 Val Sweep (5 experiments)
| exp_id | checkpoint | val acc (%) |
|--------|-----------|-------------|
| cls8b-seed123-ckpt3000-val8192-eval | ckpt-3000 | 88.69 |
| cls8b-seed123-ckpt6200-val8192-eval | ckpt-6200 | 87.52 |
| cls8b-seed123-ckpt6400-val8192-eval | ckpt-6400 | 87.48 |
| cls8b-seed123-ckpt6600-val8192-eval | ckpt-6600 | 87.23 |
| cls8b-seed123-ckpt6633-val8192-eval | ckpt-6633 | 87.10 |

#### 8B Seed 123 Test Sweep (5 experiments)
| exp_id | checkpoint | test acc (%) |
|--------|-----------|-------------|
| cls8b-seed123-ckpt200-test-eval | ckpt-200 | 72.55 |
| cls8b-seed123-ckpt6200-test-eval-v2 | ckpt-6200 | 84.70 |
| cls8b-seed123-ckpt6400-test-eval-v2 | ckpt-6400 | 85.08 |
| cls8b-seed123-ckpt6600-test-eval | ckpt-6600 | 84.90 |
| cls8b-seed123-ckpt6633-test-eval | ckpt-6633 | 84.89 |

### Priority 2: Additional Seq-Length Ablation Data Point

| exp_id | metric | why valuable | suggested location |
|--------|--------|--------------|--------------------|
| cls8b-s42-ckpt1000-test-seq2048-ablation | acc=82.83 | Second data point for seq-length ablation (ckpt-1000@2048 vs ckpt-3600@2048=83.04). Shows <1pp consistency across checkpoints at short context. | App: threats, alongside existing 83.04% |

### Priority 3: DeepSeek CWM s123 1-Epoch

| exp_id | metric | why valuable | suggested location |
|--------|--------|--------------|--------------------|
| deepseek-cwm-repo-s123-eval-1epoch | acc=75.45 | DeepSeek CWM s123 at 1-epoch checkpoint. Paper cites DeepSeek CWM val-selected (56.70%) and epoch-3 (61.49%) for s42, but s123 1-epoch data (75.45) is unreported. Could strengthen or complicate the CWM epoch analysis. | App: threats (epoch selection) |

---

## Not Applicable (Training Runs / Intermediate / Superseded)

These experiments don't require paper citation — they are infrastructure (model training), intermediate artifacts (prediction JSONs), superseded versions, or partial evaluations.

| exp_id | reason |
|--------|--------|
| deepseek-cls-repo-v5 | Training run — produces model evaluated in Table 3 |
| deepseek-cwm-repo | Training run |
| deepseek-traj-func | v1, superseded by v2 |
| exp-downsample-cls-func-v3 | Training run (eval in exp-downsample-cls-func-v3-eval) |
| qwen3-4b-traj-repo-s42 | Training run |
| qwen3-8b-traj-repo-s42-v2 | Training run |
| repo-level-cls-8b-conda | Training run |
| repo-level-cls-8b-s42-resume | Training run (resume continuation) |
| repo-level-cls-8b-seed123-conda-v3 | Training run |
| repo-level-cls-seed123-home | Training run |
| repo-level-cls-v4 | Early iteration, superseded by v5 |
| repo-level-cls-v5 | Training run (produces CLS 4B model) |
| repo-level-cls-v5-conda | Training variant (conda env replication) |
| repo-level-cwm-v10 | Training run |
| cls8b-eval-seed42 | Intermediate — generates prediction JSONs for error analysis |
| cls8b-eval-seed123 | Intermediate — generates prediction JSONs |
| matched-seed-8b-predictions | Intermediate — generates prediction JSONs for overlap analysis |
| cls8b-s42-resume-ckpt3600-test | Superseded by v2 (data issue) |
| cwm8b-ckpt400-test-eval-shard2 | Shard of CWM 8B eval (partial) |
| cwm8b-ckpt400-test-eval-shard4 | Shard of CWM 8B eval (partial) |
| mvp-b-data-prep | Data preparation — foundational, no results |
| mvp-b-train | Initial pilot training — foundational |

---

## Negative Results Worth Discussing

72 experiments have conclusion=failed or negative. Of these, ~67 are infrastructure failures (OOM, SSH timeout, argparse errors, GPU conflicts). 5-6 are genuine negative results:

### Already Referenced in Paper

| exp_id | conclusion | finding | where cited |
|--------|-----------|---------|-------------|
| p2p-regression-rate | negative | P2P rate 1.04% mean, 0% median | App (a): P2P regression rate |
| cwm-baseline | negative | CWM tied CLS at 87.51% (hypothesis: CWM < CLS) | Table 1 (CWM 4B s42=87.51) |
| per-test-majority-voting | negative | K=3 hurt accuracy by -0.68pp | App (g): failed interventions |
| re-repair-phase0 | negative | Oracle diagnostics no effect | §5.3 re-repair pilot |
| re-repair-docker-eval | negative | A1=52.3%, p=0.42, effect ~0 | §5.3 re-repair pilot |
| cls4b-seed123-ckpt800-test5120-eval-v2 | negative | 4B s123 test=75.33%, far below s42=83.63 | App: limitations (seed instability caveat) |

### Not Referenced But Worth Considering

| exp_id | conclusion | finding | assessment |
|--------|-----------|---------|------------|
| repo-level-cwm-8b-conda-v5 | negative | 8B CWM training killed at 93.4% (step 6198/6633) | Infrastructure failure, not a scientific negative. Irrelevant for paper. |

**Verdict: All scientifically meaningful negative results are already covered in the paper.** The remaining failed experiments are infrastructure issues that don't warrant paper discussion.

---

## Recommendations (Priority-Ordered)

### 1. [HIGH] Add Checkpoint Sweep Figure to Appendix

**28 experiments** of val/test sweep data are unreferenced. A dual-panel figure (4B + 8B, val + test curves) would:
- Visually confirm the "<1pp checkpoint selection noise" claim (currently text-only)
- Demonstrate val-test monotonicity (or lack thereof)
- Show training dynamics differ across seeds
- Use existing data — no new experiments needed

**Suggested: App Figure "Checkpoint Selection Sensitivity" with 4 subplots (4B-val, 4B-test, 8B-val, 8B-test), each showing training step vs accuracy.**

Data available: 6 val + 2 test checkpoints for 4B-s42; 7 val + 8 test for 8B-s42; 5 val + 5 test for 8B-s123.

### 2. [LOW] Mention Seq-Length Consistency Across Checkpoints

cls8b-s42-ckpt1000-test-seq2048-ablation (82.83%) is within <1pp of cls8b-s42-ckpt3600-seq2048-ablation (83.04%). A one-sentence note in the seq-length ablation paragraph would strengthen the robustness claim.

### 3. [LOW] DeepSeek CWM s123 Epoch Comparison

deepseek-cwm-repo-s123-eval-1epoch (75.45%) provides a cross-seed data point for CWM epoch selection. The paper discusses CWM epoch selection for s42 only (val-selected 56.70% vs epoch-3 61.49%). Adding the s123 1-epoch data could either corroborate or complicate this analysis. Evaluate before including.

---

## Coverage Statistics

| Paper Section | Experiments Referenced | % of Total |
|--------------|----------------------|------------|
| Table 1 (func-level) | 24 | 18.2% |
| Table 2 (scaling) | 8 | 6.1% |
| Table 3 (repo-level) | 26 | 19.7% |
| Table 4 (taxonomy) | (derived from above) | — |
| §5.2 equivalence | 3 | 2.3% |
| §5.3 analysis | 4 | 3.0% |
| App: ablation/control | 11 | 8.3% |
| App: per-mutation | 3 | 2.3% |
| App: TRAJ DeepSeek 6-seed | 3 | 2.3% |
| App: threats | 3 | 2.3% |
| App: few-shot | 1 | 0.8% |
| **Subtotal referenced** | **88** | **66.7%** |
| Val/test sweep (unused) | 28 | 21.2% |
| Training/intermediate | 16 | 12.1% |

**Conclusion: The paper already references 88/132 (67%) of success experiments. The remaining 33% are split between val/test sweep data (useful for a supplementary figure) and training infrastructure (not citable). All negative results with scientific value are already discussed.**
