# code verify adaptive fix

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_adaptive_fix_20260514T141417_result.json`
- **Structured JSON:** [`0f7a12db3e6e46b812f4.json`](../../sessions/0f/0f7a12db3e6e46b812f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码**已支持** `--n_min` 参数，无需修改。关键信息：

| 项目 | 状态 |
|------|------|
| CLI 参数 | `--n_min`，第 237 行，`type=int, default=None` |
| 默认逻辑 | 第 279-280 行：`args.n_min = max(2, args.batch_size // 2)` |
| 使用位置 | 第 146 行：`find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)` |
| 日志记录 | 第 366 行：`"n_min": args.n_min` 会打印到日志 |

默认值取决于 batch_size：batch_size=4 时默认 n_min=2，batch_size=8 时默认 n_min=4。显式传 `--n_min 2` 可覆盖任何默认值。

**adaptive_fix 实验提交命令模板**：

```bash
python training/pretrain_weighted.py \
  --data_path data/scored_data.jsonl \
  --output_dir outputs/adaptive_fix_seed42 \
  --weighting_method adaptive \
  --model_name models/Qwen/Qwen3-0.6B \
  --n_min 2 \
  --seed 42 \
  --use_wandb \
  --wandb_run_name adaptive_fix_seed42 \
  [其他参数...]
```

无需改代码，直接加 `--n_min 2` 即可。

---
