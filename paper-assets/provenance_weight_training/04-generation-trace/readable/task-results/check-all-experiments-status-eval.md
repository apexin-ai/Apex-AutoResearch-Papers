# check all experiments status eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_experiments_status_eval_20260521T071730_result.json`
- **Structured JSON:** [`11ef23e8fea335c4ed57.json`](../../sessions/11/11ef23e8fea335c4ed57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部仍在训练中，无 final checkpoint，暂无法跑 eval。

```
实验状态:
- adaptive_tau08_v3: 训练中 step 4160/6103 (68%), ETA ~1h15m
- gpt2_seed123_v3:   训练中 step 4059/6103 (67%), ETA ~1h20m
- ngram_seed456_v2:  训练中 step 3562/6103 (58%), ETA ~1h38m
- gpt2_seed456_v2:   训练中 step 3546/6103 (58%), ETA ~1h39m

最新 checkpoint:
- adaptive_tau08_v2: checkpoint-4000
- gpt2_seed123_v2:   checkpoint-4000
- ngram_seed456_v2:  checkpoint-3500
- gpt2_seed456_v2:   checkpoint-3500

GPU 使用: 全部 4 卡活跃 (41%~100%, 各占 ~43-46GB)
```

前两个预计 ~1h15-20m 完成，后两个 ~1h38-40m。需要我定时轮询，完成后自动跑 eval 吗？

---
