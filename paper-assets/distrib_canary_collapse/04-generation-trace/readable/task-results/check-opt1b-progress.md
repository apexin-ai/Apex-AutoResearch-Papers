# check opt1b progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_opt1b_progress_20260517T124537_result.json`
- **Structured JSON:** [`b5c6710bdc0a99cbfd52.json`](../../sessions/b5/b5c6710bdc0a99cbfd52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**OPT-1.3B 实验已完成。**

```
OPT-1.3B Progress:
- Status: COMPLETED (EXIT_CODE=0)
- Generations: 11/11 (gen_0 ~ gen_10, 即 10 轮迭代 + 初始)
- Started: ~15:32 UTC (May 17)
- Finished: ~20:39 UTC (May 17)
- Total time: ~5h 7min
- Per-gen time: ~28 min

Key metrics (collapse trajectory):
  gen_0: ppl=24.9, entropy=3.05, ECE=0.02
  gen_5: ppl=356.6, entropy=1.16, ECE=0.39
  gen_10: ppl=647.4, entropy=1.16, ECE=0.42

Files completed: gen_0 through gen_10 + all_metrics.json
```

collapse 模式清晰：perplexity 从 24.9 飙升至 647.4（26x），token entropy 从 3.05 降至 1.16，ECE 从 0.02 升至 0.42。与 Pythia 系列一致，确认了泛化性。

注：当前 `iterative_train` 进程仅剩 Pythia-410M 实验在 cuda:0 运行中。

---
