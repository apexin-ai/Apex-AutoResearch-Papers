# code a050 prep v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_a050-prep-v2_20260515T002552_result.json`
- **Structured JSON:** [`b0e889f8784ca1e6c029.json`](../../sessions/b0/b0e889f8784ca1e6c029.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，汇总结果：

### 验证结果

| 检查项 | 状态 |
|--------|------|
| 输出目录 `results/alpha_sweep/a050_s42/` | **干净** — 目录不存在，无冲突 |
| 数据目录 `data/wikitext103_5k/` | **存在** — 含 `train/`、`eval/`、`prompts/` 三个子目录 |
| 已有 sweep 点 | `a000_s42`、`a025_s42` 已完成 |
| 参数支持 | 全部匹配 ✓ — `--seed`、`--data_dir`、`--steps_per_gen`、`--num_generations`、`--synthetic_ratio`、`--output_dir` 均为有效参数 |

### 确认的训练命令

```bash
cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py \
  --seed 42 \
  --data_dir data/wikitext103_5k \
  --steps_per_gen 5000 \
  --num_generations 10 \
  --synthetic_ratio 0.50 \
  --output_dir results/alpha_sweep/a050_s42
```

参数全部可用，可以提交。

---
