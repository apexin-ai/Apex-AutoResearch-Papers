# analysis lagrangian code verify

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lagrangian-code-verify_20260516T220051_result.json`
- **Structured JSON:** [`67a4c1152721715a0b24.json`](../../sessions/67/67a4c1152721715a0b24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Here's the complete report.

---

## Part 1: Code Implementation Confirmation

The relevant function is `train_kl_normalized` (all 4 runs used `loss_type: kl_normalized`).

### 4 Questions Answered:

**Q1. λ 更新规则: MULTIPLICATIVE ×2.0/×0.5**

```python
# train.py lines 280-286 (train_kl_normalized)
old_lambda = lambda_sparse
if avg_sparsity < target_sparsity - margin:
    lambda_sparse *= 2.0
elif avg_sparsity > target_sparsity + margin:
    lambda_sparse *= 0.5
lambda_sparse = max(0.01, min(lambda_sparse, args.lambda_max))
```

Update frequency: **every step** (not batched).

**Q2. lambda_max cap: CONFIGURABLE (default=1000)**

```python
# train.py line 72
p.add_argument("--lambda_max", type=float, default=1000.0, ...)
```

Actual runs:
- kl_30pct_s42, kl_40pct_s42: ran with `--lambda_max 5000`
- kl_50pct_s42, kl_70pct_s42: ran with `--lambda_max 1000`

**Q3. Constraint loss: SQUARED with margin (deadzone)**

```python
# train.py line 259
sparsity_error = torch.abs(actual_sparsity - target_sparsity)
constraint_loss = lambda_sparse * torch.clamp(sparsity_error - margin, min=0.0) ** 2
```

Two-sided (uses abs), squared, with deadzone.

**Q4. Margin: 0.02**

```python
# train.py line 223
margin = 0.02
```

Floor: `max(0.01, ...)` (lambda never goes below 0.01).

---

## Part 2: λ Data Table

| Run | Target | Final λ | Final Sparsity | λ 模式 | λ_max used |
|-----|--------|---------|---------------|--------|------------|
| kl_30pct_s42 | 0.3 | **5000** (cap) | **0.285** | multiplicative ×2/×0.5 | 5000 |
| kl_40pct_s42 | 0.4 | **625** | **0.398** | multiplicative ×2/×0.5 | 5000 |
| kl_50pct_s42 | 0.5 | **8** | **0.504** | multiplicative ×2/×0.5 | 1000 |
| kl_70pct_s42 | 0.7 | **1000** (cap) | **0.688** | multiplicative ×2/×0.5 | 1000 |

λ 变化模式（from data）:
- **kl_30pct**: 1→0.5→0.25→...→0.01 (decay), then explosive ×2 jumps to 5000 cap at step ~260
- **kl_40pct**: stays 1 for ~160 steps, jumps to 64→5000 (cap), later decays to 625
- **kl_50pct**: 1→2→4→8, stabilizes at 8 (constraint satisfied quickly)
- **kl_70pct**: 2→4→8→...→512→1000 (geometric doubling to cap within 10 steps)

---

## Part 3: 代码 vs 论文差异（严重）

### Paper Eq.4 (method.tex L96-108) claims:

```
L = L_KL + λ · (s̄ - (1-ρ))          [linear penalty]
λ ← λ + η_λ · (s̄ - (1-ρ))           [additive gradient ascent]
η_λ = 0.1,  λ_max = 5000
```

### Code actually does:

```
L = L_KL + λ · clamp(|s - target| - 0.02, 0)²   [squared + deadzone]
λ ← λ × 2.0  or  λ × 0.5                         [multiplicative]
No η_λ parameter. λ_max varies (1000 or 5000).
```

### Specific mismatches:

| Aspect | Paper | Code | Severity |
|--------|-------|------|----------|
| Update rule | additive `λ + η·v` | multiplicative `λ×2` / `λ×0.5` | **Critical** |
| Penalty form | linear `λ·v` | squared `λ·clamp(v-m,0)²` | **Critical** |
| η_λ | 0.1 | N/A (multiplicative) | **Critical** |
| Deadzone/margin | not mentioned | 0.02 | Medium |
| λ_max | 5000 (uniform) | 5000 (30%/40%), 1000 (50%/70%) | Medium |

### Appendix Table data mismatches:

| Run | Paper claims | Actual from logs |
|-----|-------------|-----------------|
| kl_40pct Final λ | ~2100 | **625** |
| kl_70pct Final λ | ~3800 | **1000** (capped) |
| Table caption λ_max | 5000 | 1000 for 50%/70% runs |

kl_30pct (5000) and kl_50pct (8) match. kl_40pct and kl_70pct are **fabricated/wrong**.

---

**Summary**: The paper's Eq.4 describes a standard additive dual gradient ascent that was **never implemented**. The actual code uses a heuristic multiplicative controller. The appendix table has 2 of 4 λ values that don't match the logged data.

---
