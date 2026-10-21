# deploy bjb1 18228 smolvla backfill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-smolvla-backfill_20260528T063719_result.json`
- **Structured JSON:** [`2c40872b804771d812ce.json`](../../sessions/2c/2c40872b804771d812ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部在跑。

| GPU | 实验 | PID | 显存 | 状态 |
|-----|------|-----|------|------|
| cuda:0 | Pi05 CRM always-on (已有) | 982389 | 12738MiB | 运行中 |
| cuda:1 | eval-supp-long-vla-only-s44 (SmolVLA) | 34426 | 6264MiB | 运行中 |
| cuda:2 | Pi05 CRM always-on (已有) | 983106 | 12738MiB | 运行中 |
| cuda:3 | eval-supp-long-vla-only-s42 (SmolVLA) | 35030 | 5870MiB | 运行中 |

**评估脚本**: `src/evaluate.py`，命令格式：
```
python -u src/evaluate.py --model smolvla --mode vla_only --benchmark long --seed &lt;SEED> --n_rollouts 20 --output_file logs/eval_long_vla_only_smolvla_seed&lt;SEED>.json
```

输出文件分别为 `logs/eval_long_vla_only_smolvla_seed44.json` 和 `logs/eval_long_vla_only_smolvla_seed42.json`，timeout 8h。

---
