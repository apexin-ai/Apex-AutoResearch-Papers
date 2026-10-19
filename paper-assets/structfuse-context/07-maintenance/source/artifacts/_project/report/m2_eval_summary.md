# M2 Full Eval Summary — All Strategies

> Generated: 2026-05-15
> Purpose: 论文写作 + plan_005 分层分析统一数据源

---

## Table 1: Qwen Full M2 — Strategy × Seed Best R@1

| Strategy | s42 | s43 | s44 | Mean | Std |
|----------|-----|-----|-----|------|-----|
| random | 0.5527 | 0.5554 | 0.6009 | **0.5697** | 0.0271 |
| embedding | *missing* | 0.5606 | 0.5942 | 0.5774† | 0.0238† |
| dataflow | *pending* | 0.5495‡ | *pending* | — | — |

- † mean/std computed from 2 seeds only (s42 missing)
- ‡ dataflow_s43 still running; 0.5495 is best R@1 at step 500, eval@1000 showed R@1=0.5174 (early_stop patience 1/2)

---

## Table 2: StarCoder Full M2 — Strategy × Seed Best R@1

| Strategy | s42 | s43 | s44 | Mean | Std |
|----------|-----|-----|-----|------|-----|
| random | 0.4604 | 0.4912 | 0.4871 | **0.4796** | 0.0167 |
| embedding | 0.4372‡ | *pending* | *pending* | — | — |
| dataflow | *pending* | *pending* | *pending* | — | — |

- ‡ embed_s42 still running

---

## Table 3: Strategy Δ vs Random Baseline

### Qwen

| Seed | embed R@1 | random R@1 | Δ (embed−random) |
|------|-----------|------------|-------------------|
| s42 | *missing* | 0.5527 | — |
| s43 | 0.5606 | 0.5554 | **+0.0052** |
| s44 | 0.5942 | 0.6009 | **−0.0067** |
| **Mean Δ** | | | **−0.0008** (n=2) |

| Seed | dataflow R@1 | random R@1 | Δ (dataflow−random) |
|------|--------------|------------|----------------------|
| s43 | 0.5495‡ | 0.5554 | **−0.0059** |

### StarCoder

| Seed | embed R@1 | random R@1 | Δ (embed−random) |
|------|-----------|------------|-------------------|
| s42 | 0.4372‡ | 0.4604 | **−0.0232** |

**Preliminary observation:** On full data, embedding/dataflow do NOT show consistent improvement over random. This contrasts with pilot results (Table 5).

---

## Table 4: SWE-bench BM25 Baseline (300 instances)

| Metric | Value |
|--------|-------|
| R@1 | 0.2733 |
| R@5 | 0.4667 |
| R@10 | 0.5500 |
| R@20 | 0.6467 |

100-instance subset: R@1=0.2800, R@5=0.5100, R@10=0.5800, R@20=0.6300, MRR=0.3768

---

## Table 5: Pilot (24 repos) vs Full — Qwen R@1

| Strategy | Pilot R@1 | Full Mean R@1 | Δ (full−pilot) |
|----------|-----------|---------------|-----------------|
| random | 0.5357 | 0.5697 (n=3) | +0.0340 |
| embedding | 0.5557 | 0.5774 (n=2) | +0.0217 |
| dataflow | 0.5436 | 0.5495 (n=1)‡ | +0.0059 |

### StarCoder Pilot vs Full

| Strategy | Pilot R@1 | Full Mean R@1 | Δ (full−pilot) |
|----------|-----------|---------------|-----------------|
| random | 0.4922 | 0.4796 (n=3) | −0.0126 |
| embedding | 0.5078 | 0.4372 (n=1)‡ | −0.0706 |
| dataflow | 0.4869 | — | — |

**Pilot embed advantage disappeared at full scale** — key finding worth investigating.

---

## Table 6: Training Dynamics

### Qwen

| Subrun | Best R@1 | Best Step | Early Stop Step | Total Steps | Overfitting? |
|--------|----------|-----------|-----------------|-------------|-------------|
| random_s42 | 0.5527 | 1000 | — (ran full) | 4000 | Yes — peaked at 1000, ran 3000 more steps |
| random_s43 | 0.5554 | 1500 | 1500 | 1500 | No — stopped at peak |
| random_s44 | 0.6009 | 500 | 1500 | 1500 | Mild — best at 500, stopped at 1500 |
| embed_s43 | 0.5606 | 1500 | 1500 | 1500 | No — stopped at peak |
| embed_s44 | 0.5942 | 500 | 2000 | 2000 | Mild — best at 500, continued to 2000 |
| dataflow_s43 | 0.5495 | 500 | *running* | ≥1000 | TBD — R@1 dropped to 0.5174 at step 1000 |

### StarCoder

| Subrun | Best R@1 | Best Step | Early Stop Step | Total Steps | Overfitting? |
|--------|----------|-----------|-----------------|-------------|-------------|
| random_s42 | 0.4604 | 2500 | — (ran full) | 4000 | Mild — peaked at 2500 |
| random_s43 | 0.4912 | 1500 | 2500 | 2500 | Mild — best at 1500, stopped at 2500 |
| random_s44 | 0.4871 | 1500 | 1500 | 1500 | No — stopped at peak |
| embed_s42 | 0.4372 | 500 | *running* | ≥500 | TBD |

### Best val_loss Reference

| Subrun | Model | Best val_loss | Step |
|--------|-------|---------------|------|
| random_s42 | Qwen | 0.4651 | 1000 |
| random_s43 | Qwen | 0.4476 | 500 |
| random_s44 | Qwen | 0.4252 | 500 |
| embed_s43 | Qwen | 0.4541 | 500 |
| embed_s44 | Qwen | 0.4341 | 1000 |
| dataflow_s43 | Qwen | 0.4617 | 500 |
| random_s42 | StarCoder | 0.6134 | 1000 |
| random_s43 | StarCoder | 0.5239 | 1500 |
| random_s44 | StarCoder | 0.5913 | 500 |
| embed_s42 | StarCoder | 0.6154 | 500 |

---

## Coverage Summary

| Model | Strategy | Seeds Done | Seeds Running | Seeds Pending |
|-------|----------|------------|---------------|---------------|
| Qwen | random | 3/3 ✓ | 0 | 0 |
| Qwen | embedding | 2/3 | 0 | 1 (s42) |
| Qwen | dataflow | 0/3 | 1 (s43) | 2 (s42, s44) |
| StarCoder | random | 3/3 ✓ | 0 | 0 |
| StarCoder | embedding | 0/3 | 1 (s42) | 2 (s43, s44) |
| StarCoder | dataflow | 0/3 | 0 | 3 |

**Completion: 8/18 done, 2/18 running, 8/18 pending**
