# d064 Violation & F1 Evaluation — Batch 2 (greedy)

**Date**: 2026-05-19  
**Dataset**: DocRED 998-doc dev set  
**Eval script**: `scripts/eval_d064.py`  
**Server**: westd-16980

## Main Results

| Model | Decoding | Mode | ET% | RV% | DR% | CF% | E-F1 | R-F1 | PF% |
|-------|----------|------|-----|-----|-----|-----|------|------|-----|
| Llama | greedy   | unc  | 0.00 | 0.11 | 0.30 | 0.07 | 83.45 | 44.70 | 4.8 |
| Llama | greedy   | con  | — | — | — | — | — | — | — |
| Qwen  | greedy   | unc  | — | — | — | — | — | — | — |
| Qwen  | greedy   | con  | — | — | — | — | — | — | — |

**PF% = Parse Failure rate**  
**—** = not yet completed

## Cascade Script Status

- **Cascade PID**: 677484 (running, waiting for Llama con PID 665503)
- **Script**: `scripts/d064_cascade_qwen_con.sh`
- **Log**: `/root/autodl-tmp/schema_outputs/d064_cascade_qwen_con.log`
- When Llama greedy con (PID 665503) finishes → auto-starts Qwen greedy con on GPU1

## Llama Greedy Constrained Progress

- **Current**: 882/998 (~88%), PID 665503 still running
- **ETA**: ~60 min (rate ~2 lines/min)
- Eval pending completion

## Detailed Per-File Stats

### Llama greedy unconstrained (westd-16980)
- File: `d064_llama_docred_greedy_unconstrained_w5.jsonl`
- Samples: 998, Parse Fail: 48 (4.8%)
- Entities pred: 18443, Relations pred: 14794
- ET=0, RV=17, DR=45, CF=12
- E: P=85.94 R=81.10 F1=83.45
- R: P=40.94 R=49.23 F1=44.70

## Comparison with Batch 1 (beam-4)

| Model | Decoding | Mode | ET% | RV% | DR% | CF% | E-F1 | R-F1 | PF% |
|-------|----------|------|-----|-----|-----|-----|------|------|-----|
| Llama | beam-4   | unc  | 0.00 | 0.04 | 0.10 | 0.06 | 85.16 | 47.17 | 1.4 |
| Llama | beam-4   | con  | 0.00 | 0.00 | 0.00 | 0.00 | 85.23 | 47.17 | 1.3 |
| Llama | greedy   | unc  | 0.00 | 0.11 | 0.30 | 0.07 | 83.45 | 44.70 | 4.8 |

### Greedy vs Beam-4 (Llama unc)
- **E-F1**: 83.45 vs 85.16 (−1.71) — beam-4 better
- **R-F1**: 44.70 vs 47.17 (−2.47) — beam-4 better
- **PF%**: 4.8% vs 1.4% — greedy 3× more parse failures
- **Violations**: greedy has higher RV (0.11 vs 0.04), DR (0.30 vs 0.10) — beam search reduces violations even without constraints
