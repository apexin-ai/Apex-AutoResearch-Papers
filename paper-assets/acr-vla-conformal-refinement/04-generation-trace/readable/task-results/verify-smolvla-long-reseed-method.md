# verify smolvla long reseed method

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_smolvla-long-reseed-method_20260522T143706_result.json`
- **Structured JSON:** [`6fd2f2eb07fc20b1e417.json`](../../sessions/6f/6fd2f2eb07fc20b1e417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认：用的是我们的 wrapper，不是 lerobot 官方 eval。**

三个进程的核心命令都是：
```bash
python src/evaluate.py --mode vla_only --benchmark long --seed {0,1,2} --n_rollouts 10 --output_file logs/eval_long_vla_only_seed{0,1,2}.json
```

具体信息：
| PID | GPU | seed | 输出文件 |
|-----|-----|------|---------|
| 232609 | cuda:0 | 0 | `logs/eval_long_vla_only_seed0.json` |
| 232884 | cuda:1 | 1 | `logs/eval_long_vla_only_seed1.json` |
| 233564 | cuda:2 | 2 | `logs/eval_long_vla_only_seed2.json` |

**建议：先不要 kill。** 需要确认两点再决定是否重跑：
1. `src/evaluate.py --mode vla_only` 和 lerobot 官方 eval 的结果差异有多大——如果我们 wrapper 内部就是调的 lerobot eval pipeline，结果可能等价
2. 这三个 seed 跑了多久了——如果快完成了，可以先拿到结果，再补跑 lerobot 官方 eval 做对比

---
