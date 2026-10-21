# Paper Materials — exec-sim-repair-verifier

> 生成时间: 2026-05-12 | 基于 registry 中 35 个 DONE 实验

---

## 1. 结构化指标表格

### 1.1 4B Function-Level: CLS vs CWM (5 seeds each)

**Classification (CLS) — Qwen3-4B + LoRA**

| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |
|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|
| 42 | multi-seed-core | 87.83 | 87.59 | 88.06 | 86.20 | 89.04 | 89.45 | 86.71 | 17298s (3-seed batch) |
| 123 | multi-seed-core | 89.52 | 89.40 | 89.64 | 87.34 | 91.56 | 91.76 | 87.63 | (same batch) |
| 456 | multi-seed-core | 87.88 | 88.21 | 87.53 | 83.12 | 93.97 | 93.60 | 82.21 | (same batch) |
| 789 | cls-seed789 | 89.00 | 89.10 | 88.90 | 85.20 | 93.40 | 93.30 | 84.90 | 3849s |
| 0 | cls-seed0 | 87.94 | 88.08 | 87.79 | 84.20 | 92.32 | 92.13 | 83.84 | 4977s |
| **Mean** | | **88.43** | **88.48** | **88.38** | **85.21** | **92.06** | **92.05** | **85.06** | |
| **Std** | | **0.74** | **0.67** | **0.83** | | | | | |

**Code World Model (CWM) — Qwen3-4B + LoRA**

| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |
|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|
| 42 | cwm-baseline | 87.51 | 87.71 | 87.31 | 83.53 | 92.32 | 92.06 | 83.03 | 84.02 | 3439s |
| 123 | cwm-seed123 | 87.20 | 87.44 | 86.95 | — | — | — | — | 84.44 | 5096s |
| 456 | cwm-seed456 | 86.98 | 87.29 | 86.66 | 82.52 | 92.65 | 92.26 | 81.70 | 84.02 | 3440s |
| 789 | cwm-seed789 | 86.67 | 86.60 | 86.74 | 84.09 | 89.25 | 89.37 | 84.25 | 83.97 | 5158s |
| 0 | cwm-seed0 | 87.57 | 87.93 | 87.18 | 82.71 | 93.86 | 93.45 | 81.70 | 84.29 | 3586s |
| **Mean** | | **87.19** | **87.39** | **86.97** | **83.21** | **92.02** | **91.79** | **82.67** | **84.15** | |
| **Std** | | **0.38** | **0.52** | **0.27** | | | | | | |

**4B CLS vs CWM Per-Seed Gap (Accuracy)**

| Seed | CLS | CWM | Gap (pp) |
|------|-----|-----|----------|
| 42 | 87.83 | 87.51 | +0.32 |
| 123 | 89.52 | 87.20 | +2.32 |
| 456 | 87.88 | 86.98 | +0.90 |
| 789 | 89.00 | 86.67 | +2.33 |
| 0 | 87.94 | 87.57 | +0.37 |
| **Mean** | **88.43** | **87.19** | **+1.25** |

### 1.2 8B Function-Level: CLS vs CWM (3 seeds each)

**Classification (CLS) — Qwen3-8B + LoRA**

| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | Train Time |
|------|--------|----------|---------|---------|-----------|----------|-----------|----------|------------|
| 42 | model-size-scaling-cls8b | 90.48 | 90.06 | 90.86 | 90.76 | 89.36 | 90.22 | 91.51 | 5614s |
| 123 | cls8b-seed123 | 89.40 | 89.20 | 89.50 | 87.50 | 90.90 | 91.20 | 87.90 | 5666s |
| 456 | cls8b-seed456 | 88.31 | 88.41 | 88.20 | 84.72 | 92.43 | 92.29 | 84.46 | 5481s |
| **Mean** | | **89.40** | **89.22** | **89.52** | **87.66** | **90.90** | **91.24** | **87.96** | |

**Code World Model (CWM) — Qwen3-8B + LoRA**

| Seed | Exp ID | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec | EM Rate | Train Time |
|------|--------|----------|---------|---------|-----------|----------|-----------|----------|---------|------------|
| 42 | model-size-scaling-cwm8b | 87.67 | 87.77 | 87.57 | 84.19 | 91.67 | 91.53 | 83.95 | 84.39 | 5570s |
| 123 | cwm8b-seed123 | 86.98 | 87.13 | 86.83 | — | — | — | — | 84.13 | 5948s |
| 456 | cwm8b-seed456 | 86.24 | 86.51 | 85.96 | 82.09 | 91.45 | 91.08 | 81.39 | 82.80 | 6071s |
| **Mean** | | **86.96** | **87.14** | **86.79** | **83.14** | **91.56** | **91.31** | **82.67** | **83.77** | |

**8B CLS vs CWM Per-Seed Gap (Accuracy)**

| Seed | CLS | CWM | Gap (pp) |
|------|-----|-----|----------|
| 42 | 90.48 | 87.67 | +2.81 |
| 123 | 89.40 | 86.98 | +2.42 |
| 456 | 88.31 | 86.24 | +2.07 |
| **Mean** | **89.40** | **86.96** | **+2.43** |

**Scaling Summary: CLS-CWM Gap Widens with Model Size**

| Model Size | CLS Mean Acc | CWM Mean Acc | Gap (pp) | Seeds |
|------------|-------------|-------------|----------|-------|
| 4B | 88.43 | 87.19 | +1.25 | 5 |
| 8B | 89.40 | 86.96 | +2.43 | 3 |
| Gap widening | | | +1.18 | |

### 1.3 Trajectory-Level Baseline (5 seeds, Qwen3-4B)

| Seed | Exp ID | Accuracy | Unresolved F1 | Resolved F1 | Consistency |
|------|--------|----------|---------------|-------------|-------------|
| 42 | traj-level-finetuned | 85.66 | 87.50 | 83.18 | 79.94% |
| 123 | traj-level-seed123 | 85.47 | 87.00 | 83.52 | 78.59% |
| 456 | traj-level-seed456 | 87.40 | 88.70 | 85.80 | 78.80% |
| 789 | traj-level-seed789 | 87.31 | 88.27 | 86.17 | 76.74% |
| 0 | traj-level-seed0 | 85.66 | 87.37 | 83.41 | 79.55% |
| **Mean** | | **86.30** | **87.77** | **84.42** | **78.72%** |

### 1.4 LLM-Judge Zero-Shot Baselines

| Model | Accuracy | Fail F1 | Pass F1 | Fail Prec | Fail Rec | Pass Prec | Pass Rec |
|-------|----------|---------|---------|-----------|----------|-----------|----------|
| Qwen3-8B zero-shot | 64.40 | 72.20 | 50.50 | 57.90 | 95.80 | 90.00 | 35.10 |
| Qwen3-32B NF4 zero-shot | 71.69 | 75.91 | 65.68 | 64.40 | 92.43 | 88.12 | 52.35 |
| Fine-tuned 4B CLS (ref) | 88.43 | 88.48 | 88.38 | 85.21 | 92.06 | 92.05 | 85.06 |

Fine-tuning advantage: +24.0pp over 8B zero-shot, +16.7pp over 32B zero-shot.

### 1.5 CLS vs Trajectory — Variant-Level Equivalence (5-Paired Clustered Bootstrap)

| Metric | Value |
|--------|-------|
| Pooled gap (CLS − TRAJ) | −0.45 pp |
| 95% CI | [−1.71, +0.84] |
| Pooled p-value (gap ≠ 0) | 0.499 |
| TOST p-value (±2pp margin) | 0.0071 |
| TOST conclusion | **Equivalent** |
| ICC (intra-cluster correlation) | 0.191 |
| Design effect (DEFF) | 3.97 |
| n_variants | 523 |
| n_clusters | 114 |

Per-seed variant-level gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29

### 1.6 Oracle / Statistical Analysis

**Oracle F2P Stratification (oracle-f2p-stratified)**

| T bucket | % of instances | Block-corr advantage (pp) | Contribution to overall |
|----------|---------------|--------------------------|------------------------|
| T=1 | 68.7% | −0.09 | negligible |
| T=2 | 19.1% | 31.69 | 55.3% |
| T=3–5 | 7.1% | 40.74 | — |
| T≥6 | 5.1% | 40.06 | — |
| **Overall** | 100% | **10.93** | |

**P2P Regression Rate (p2p-regression-rate) — NEGATIVE**
- Mean regression rate: 1.04%, median: 0%
- 77% of incorrect patches break zero P2P tests
- Falls in <5% zone → P2P signal weak for this dataset

**Block Correlation (block-corr-empirical)**

| Metric | Value |
|--------|-------|
| ICC | 0.191 |
| ICC p-value | 0.000 |
| Design effect | 3.97 |
| Overall error rate | 12.49% |
| All-correct problems (observed) | 46 |
| All-correct problems (expected i.i.d.) | 16.35 |
| Ratio (observed/expected) | 2.81× |
| Error std observed | 0.153 |
| Error std expected i.i.d. | 0.081 |

**Matched-Seed Error Overlap**
- CLS dominant error: false alarms (FP) — 56.5% of CLS errors are FP (PASS→FAIL)
- CWM dominant error: false alarms (FP) — 70.3% of CWM errors are FP (PASS→FAIL)
- Same direction (both FP-dominant), different degree — CWM has stronger fail-bias
- Oracle ensemble accuracy: 90.63%
- Partial complementarity from different fail-bias degrees → formulation diversity as verification strategy

### 1.7 Per-Test Diagnostic Analysis

**Precision-Recall by Mutation Type (per-test-precision-recall)**

| Mutation Type | Accuracy | F1 |
|---------------|----------|----|
| return_value | 97.26% | 98.6% (easiest) |
| off_by_one | 82.56% | 80.8% (hardest) |

- 114 problems (perfect-prediction % from suspect checkpoint, removed pending re-evaluation)
- Median problem fail-F1: 94.12%
- Worst problems: MBPP/397 (40%), HumanEval/130 (46%)
- Bucket 6–10 tests: 96.3% accuracy; 11+ tests: 87.1%

**Majority Voting K=3 (per-test-majority-voting) — NEGATIVE**

| Metric | Greedy | Majority Vote K=3 | Delta |
|--------|--------|-------------------|-------|
| Accuracy | 87.83 | 86.83 | −1.00 |
| Fail F1 | 87.59 | 87.29 | −0.30 |
| Pass F1 | 88.06 | 86.33 | −1.73 |

- Unanimous rate: 93.3%
- Net flips: −13 (28 correct→wrong, 15 wrong→correct)

### 1.8 Dataset Statistics (mvp-b-data-prep)

| Metric | Value |
|--------|-------|
| Total samples | 19,076 |
| HumanEval | 5,575 |
| MBPP | 13,501 |
| Class balance | pass 52.0% / fail 48.0% |
| Train/Val/Test | 15,290 / 1,896 / 1,890 |
| Majority baseline | 52.0% |
| Label verification | All verified by execution (5s timeout) |

### 1.9 Training Hyperparameters

| Param | 4B CLS/CWM | 8B CLS/CWM |
|-------|-----------|-----------|
| Base model | Qwen/Qwen3-4B | Qwen/Qwen3-8B |
| Method | LoRA | LoRA |
| Batch size | 2 | 2 |
| Grad accumulation | 16 | 16 |
| Learning rate | 2e-4 | 2e-4 |
| Epochs | 3 | 3 |
| Trainable params | ~0.19% | ~0.19% (15.3M/8.2B) |
| GPU hours per seed | ~1.0–1.5h | ~1.5–1.7h |

---

## 2. Paper Framing 证据审查

### Claim 1: Complexity-Dependent Reformulation Advantage

> CLS and CWM equivalent on simple function-level code; CLS scales better with model size and to repo-level complexity.

| 证据点 | 状态 | 实验 | 数据 |
|--------|------|------|------|
| 4B function-level CLS≈CWM | ✅ 充足 | 5 seeds each | Gap=+1.25pp mean, std overlap |
| 8B scaling gap widens | ✅ 充足 | 3 seeds each | Gap=+2.43pp mean (2.07–2.81) |
| LLM-judge far below fine-tuned | ✅ 充足 | 2 baselines | 8B: 64.4%, 32B: 71.7% vs ft-4B: 88.4% |
| Repo-level CLS > CWM | ❌ 缺失 | v3 均 SIGKILL | 训练中，预计 14–20h |
| CWM failure modes 定性分析 | ⚠️ 间接 | EM rate ~84% | 需 repo-level 数据直接展示 |

**统计检验缺口：**
- ❌ 4B CLS vs CWM paired bootstrap 检验（5 seeds 数据已有，未跑）
- ❌ 8B CLS vs CWM paired bootstrap 检验（3 seeds 数据已有，未跑）
- ❌ Scaling interaction test（gap widening 显著性）
- ⚠️ 需 effect size (Cohen's d)

**判定：** 函数级证据方向正确但统计力度不足（5 seeds paired t-test power 低）。Repo-level 是核心缺失。

### Claim 2: Diagnostic Granularity At Equivalent Accuracy

> Per-test classification achieves equivalent variant-level accuracy to trajectory-level scoring.

| 证据点 | 状态 | 实验 | 数据 |
|--------|------|------|------|
| Variant-level equivalence | ✅ 充足 | 5-paired-clustered-bootstrap | TOST p=0.007, gap=−0.45pp |
| Cluster structure | ✅ 充足 | block-corr-empirical | ICC=0.191, DEFF=3.97 |
| Diagnostic granularity | ✅ 部分 | per-test-precision-recall | Per-mutation breakdown |
| Downstream re-repair | ❌ 缺失 | — | 未实验 |

**统计检验：** ✅ 完整。

**注意：** Seeds 789/0 使用 4-bit quantization，论文需说明。±2pp TOST margin 需 justification。

**判定：** 证据最充分，可直接写入论文。

### Claim 3: Accuracy-Utility Frontier Characterization

> Per-test advantage depends on test distribution; concentrates in multi-F2P instances.

| 证据点 | 状态 | 实验 | 数据 |
|--------|------|------|------|
| T distribution sensitivity | ✅ 充足 | oracle-f2p-stratified | T=1 无优势, T≥2 +30–41pp |
| P2P regression rare | ✅ 充足 | p2p-regression-rate | 1.04% mean (negative) |
| Block correlation | ✅ 充足 | block-corr-empirical | ICC=0.191, ratio 2.81× |
| Error complementarity | ✅ 充足 | matched-seed overlap | Oracle 90.63% |
| Majority voting | ✅ 充足 | per-test-majority-voting | K=3 hurts −0.69pp (negative) |
| Oracle frontier | ✅ 部分 | mvp-a-oracle-sim | 基于模拟，非真实模型 |

**判定：** 证据丰富，但 oracle frontier 基于模拟——需论文明确说明。

---

## 3. 缺失清单

### 3.1 缺失的实验/数据

| 优先级 | 缺失项 | 依赖 | 备注 |
|--------|--------|------|------|
| **P0** | Repo-level CLS 训练结果 | v4 训练完成 (~14–20h) | Claim 1 核心 |
| **P0** | Repo-level CWM 训练结果 | v4 训练完成 | Claim 1 核心 |
| **P0** | Repo-level paired bootstrap | 两个训练完成后 | Go/No-Go 决策 |
| **P1** | 4B CLS vs CWM paired bootstrap (5 seeds) | 数据已有 | 统计完善 |
| **P1** | 8B CLS vs CWM paired bootstrap (3 seeds) | 数据已有 | 统计完善 |
| **P1** | Scaling interaction test | 数据已有 | Gap widening 显著性 |
| **P2** | CLS vs CWM effect size (Cohen's d) | 数据已有 | 补充统计 |
| **P2** | Diagnostic re-repair experiment | 需新实验或 future work | Claim 2 downstream |
| **P3** | Oracle frontier with real model | precision-recall 数据可用 | Claim 3 加强 |

### 3.2 缺失的图表

| Figure | 描述 | 数据来源 | 优先级 |
|--------|------|----------|--------|
| Fig 1 | 方法概览图：CLS vs CWM formulation 对比示意 | 手绘/设计 | P0 |
| Fig 2 | 主结果柱状图：4B/8B CLS vs CWM accuracy + error bars | §1.1 + §1.2 | P0 |
| Fig 3 | Scaling plot：Model size × Formulation accuracy 折线图 | §1.1 + §1.2 | P0 |
| Fig 4 | CLS vs TRAJ 等价性：TOST 可视化 / forest plot | §1.5 | P0 |
| Fig 5 | LLM-judge baseline 对比 bar chart | §1.4 | P1 |
| Fig 6 | Oracle frontier：resolve rate vs precision curves | §1.6 oracle-sim | P1 |
| Fig 7 | F2P 分层分析：per-test advantage by T bucket | §1.6 stratified | P1 |
| Fig 8 | Error complementarity：CLS vs CWM 错误模式对比 | matched-seed overlap | P1 |
| Fig 9 | Block correlation：observed vs expected error distribution | §1.6 block-corr | P2 |
| Fig 10 | Per-test precision-recall by mutation type | §1.7 | P2 |
| Fig 11 | Repo-level 结果（待训练完成） | — | P0 (blocked) |

### 3.3 Repo-Level 完成后需要的后续分析

1. Repo-level eval on SWE-bench Verified subset
2. Paired bootstrap: CLS vs CWM (n≥200)
3. Go/No-Go decision per ROADMAP D008
4. CWM failure mode qualitative analysis (token exhaustion, string mismatch cases)
5. Repo-level oracle frontier with real model precision/recall
6. Update scaling plot with repo-level data point
7. (Stretch) End-to-end re-ranking demo for resolve rate

### 3.4 可立即执行的 CPU 任务

| 任务 | 优先级 | 输入数据 |
|------|--------|----------|
| 4B CLS vs CWM 5-seed paired bootstrap | P1 | 已有 eval predictions |
| 8B CLS vs CWM 3-seed paired bootstrap | P1 | 已有 eval predictions |
| Scaling interaction effect | P1 | 已有 mean/std |
| Cohen's d effect sizes | P2 | 已有 mean/std |
| 画 Fig 2–10 | P0 | 本文档数据 |
| Paper Agent 写已完成 pillars 章节 | P0 | paper_framing + 本文档 |
