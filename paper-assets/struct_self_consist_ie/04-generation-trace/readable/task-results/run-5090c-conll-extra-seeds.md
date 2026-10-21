# run 5090c conll extra seeds

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_5090c_conll_extra_seeds_20260520T233713_result.json`
- **Structured JSON:** [`d23cf475cd5b4e27301b.json`](../../sessions/d2/d23cf475cd5b4e27301b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部启动并注册完毕。

| exp_id | GPU | T | seed | PID | status |
|--------|-----|---|------|-----|--------|
| exp_conll_t05_s123 | cuda:1 | 0.5 | 123 | 247486 | RUNNING |
| exp_conll_t08_s123 | cuda:2 | 0.8 | 123 | 248190 | RUNNING |
| exp_conll_t12_s123 | cuda:3 | 1.2 | 123 | 248879 | RUNNING |

GPU 验证：cuda:1-3 各占用 ~30GB 显存，cuda:0 (14B inference) 未受影响。命令与 seed=42 完全一致，仅改 `--seed 123` 和 `--output_dir`。预计 30-40 分钟完成。

---
