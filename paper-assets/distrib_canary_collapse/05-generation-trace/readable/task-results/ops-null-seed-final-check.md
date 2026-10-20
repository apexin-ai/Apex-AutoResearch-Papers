# ops null seed final check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_null_seed_final_check_20260524T044957_result.json`
- **Structured JSON:** [`b92be372958297b3eebd.json`](../../sessions/b9/b92be372958297b3eebd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Null Seed 实验状态

| exp_id | Server | 状态 | Gen 进度 | PermG FPR |
|--------|--------|------|----------|-----------|
| null_s45 (T=10) | 17855 | **done** (EC=0) | 11/11 | 2/6 (33.3%) |
| null_s46 (T=10) | 17855 | running | 8/11 | - |
| null_s47 (T=10) | 17855 | **done** (EC=0) | 11/11 | 0/6 (0.0%) |
| null_s48 (T=10) | 17855 | running | 8/11 | - |
| null_s49 (T=10) | 17855 | running | 8/11 | - |
| null_s50 (T=10) | 17855 | running | 8/11 | - |
| null_gpt2m_s42 | 17855 | running | 4/11 | - |
| null_gpt2m_s43 | 17855 | running | 4/11 | - |
| null_t15_s42 | 19828 | running | 4/16 | - |
| null_t15_s43 | 19828 | running | 4/16 | - |

D102 analyses for s45 and s47 already existed (6-pair). No new completed experiments to analyze.

**False positives in s45:** token_entropy→distinct_2, token_entropy→distinct_3

## Pooled FPR（已完成 seeds）
- **Pythia-410M T=10:** 2/12 (16.7%) — 2 seeds done
- **Pythia-410M T=15:** pending (4/16 gens)
- **GPT-2m T=10:** pending (4/11 gens)
- **Total:** 2/12 (16.7%)

## GPU 状态
- **17855:** 6 GPUs all ~95% util, 14-15GB VRAM — running 6 experiments
- **19828:** 2 GPUs both ~96% util, 14GB VRAM — running 2 experiments

s46/48/49/50 at 8/11 gens should finish in a few hours. GPT-2m and T=15 at ~36% progress, likely 6-8h remaining.

---
