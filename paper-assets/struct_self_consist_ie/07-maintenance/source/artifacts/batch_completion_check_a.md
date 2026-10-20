# Batch Completion Check — 2026-05-16

## 1. exp_022_seed789 (SciERC 3rd seed, N=8)

**Status: SUCCESS**

| Item | Value |
|------|-------|
| Output dir | `output/exp_022_seed789/` |
| samples.jsonl | 551 lines, 19.2 MB |
| report.json | present |

### Key Metrics

| Metric | NER | RE |
|--------|-----|-----|
| Greedy F1 | 0.6665 | 0.4193 |
| Oracle F1 | 0.7856 | 0.5885 |
| Headroom | 0.1192 | 0.1692 |
| ρ(soft_jaccard, F1) full | 0.384 | 0.224 |
| ρ(soft_jaccard, F1) cond | 0.337 | 0.348 |
| ρ(fleiss, F1) full | 0.234 | 0.234 |
| Structural beats surface | YES (+0.150) | NO (-0.010) |
| Logprob ρ (full) | 0.207 | 0.296 |

- **Verdict**: FAIL (RE ρ_sj < 0.40 threshold)
- **Warning**: >30% RE samples F1=0 (44.6%)

---

## 2. exp_025_n32 (SciERC N=32)

**Status: SUCCESS**

| Item | Value |
|------|-------|
| Output dir | `output/exp_025_n32/` |
| samples.jsonl | 551 lines, 69.0 MB |
| report.json | present |

### Key Metrics

| Metric | NER | RE |
|--------|-----|-----|
| Greedy F1 | 0.6581 | 0.4225 |
| Oracle F1 | 0.8379 | 0.6727 |
| Headroom | 0.1798 | 0.2502 |
| ρ(soft_jaccard, F1) full | 0.440 | 0.300 |
| ρ(soft_jaccard, F1) cond | 0.395 | 0.348 |
| ρ(fleiss, F1) full | 0.310 | 0.353 |
| Structural beats surface | YES (+0.129) | NO (-0.053) |
| Logprob ρ (full) | 0.211 | 0.315 |

- **Verdict**: FAIL (RE ρ_sj < 0.40 threshold)
- **Warning**: >30% RE samples F1=0 (43.8%)

### N=32 vs N=8 comparison (NER)

| Metric | N=8 (seed789) | N=32 |
|--------|---------------|------|
| Oracle headroom | 0.119 | 0.180 (+51%) |
| ρ_sj (full) | 0.384 | 0.440 (+15%) |
| ρ_sj (cond) | 0.337 | 0.395 (+17%) |
| Fleiss κ mean | 0.387 | 0.499 (+29%) |

N=32 substantially improves correlation quality and headroom for NER but RE remains weak.

---

## 3. exp_020_fewnerd_smoke (Few-NERD LoRA training)

**Status: INCOMPLETE — interrupted at ~60%**

| Item | Value |
|------|-------|
| Checkpoint dir | `checkpoints/ft_fewnerd_smoke/` |
| Total steps | 8236 (1 epoch) |
| Completed steps | ~5000 (60.7%) |
| Last logged step | 5000, loss=0.041 |
| Saved checkpoints | 2000, 3000, 4000 |
| Best checkpoint | checkpoint-4000 |
| Best eval_loss | 0.0513 |
| Adapter size | 167 MB (safetensors) |

### Training curve (selected points)

| Step | Train Loss | Eval Loss | LR |
|------|-----------|-----------|-----|
| 50 | 0.960 | — | 1.19e-5 |
| 500 | 0.109 | — | 1.21e-4 |
| 1000 | 0.085 | 0.0961 | 2.00e-4 |
| 2000 | 0.065 | 0.0660 | 1.90e-4 |
| 3000 | 0.057 | 0.0542 | 1.66e-4 |
| 4000 | 0.052 | 0.0513 | 1.22e-4 |
| 5000 | 0.041 | — | 8.03e-5 |

- Loss was decreasing steadily; training was interrupted externally (tmux killed / instance restarted)
- Remaining time estimate at interruption: ~2h13m
- checkpoint-4000 is usable for inference if needed, though training incomplete

### Error info
- No error in logs; clean progress bar at step 2711 in `fewnerd_train.log` (older nohup log), trainer_log.jsonl goes to step 5000
- Likely cause: instance shutdown or manual kill
