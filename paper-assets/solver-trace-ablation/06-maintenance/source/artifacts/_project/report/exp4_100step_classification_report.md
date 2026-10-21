## EXP-4: 100-Step Checkpoint Hacking Classification

**Source**: `/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json` (Prover9, `grpo_exec_only/` @ 100 steps, seed 42)
**Output JSON**: `/root/autodl-tmp/outputs/exp4_100step_h1h7_classification.json`

| Metric | Value |
|---|---|
| PR @ 100 steps | **32.0%** (32/100) |
| Mean ISR (proved-only) | 0.642 |
| H7 (single premise == conclusion) | **9/32 = 28.1%** of proved |
| H1 (concl appears among ≥2 premises) | 1/32 = 3.1% of proved |
| Total hacking (H1+H7) | **10/32 = 31.2%** of proved |
| Genuine | 22/32 = 68.8% of proved |

### Key Finding
Hacking is NOT low at PR=32%. H7 already 28.1% after only 100 RL steps.
- SFT @ PR=14%: ~0% H7
- RL @ 100 steps, PR=32%: 28.1% H7

The qualitative jump between SFT and early RL supports "RL-specific hacking" claim.
H7 examples: folio_304, folio_669, folio_215 (ISR 0.5–0.75 each).