## H7 Convergence Timing Analysis

Data: reward_log.jsonl isr_mean as H7 proxy (no per-checkpoint taxonomy available)

| 条件 | ISR首次持续>0.5 的 step | 最终 H7% |
|------|------------------------|----------|
| ISR s43 | ~Step 200 | 100% @500 |
| ISR s42 | ~Step 450-500 | 16%→97% (500→1000) |
| Exec-only s43 | ~Step 450-500 | 100% @1000 |
| Random s42/s43 | Never | 0% / 38.3% |
| Exec-only s42/s44 | Never | 0% (H1 mode) |

Key: ISR reward creates H7 self-amplifying positive feedback — ISR s43 onset→saturation ~250 steps (150→400), exec-only s43 ~350 steps (150→500+). Random ISR trajectory shows no upward trend even when H7 exists.

Support for Narrative A: medium-strong. ISR accelerates H7 convergence but onset is seed-dependent.

Remote: /root/solver-trace-ablation/analysis/h7_convergence_timing.md