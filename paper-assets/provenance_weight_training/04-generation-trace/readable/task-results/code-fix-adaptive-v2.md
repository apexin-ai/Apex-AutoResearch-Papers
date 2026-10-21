# code fix adaptive v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_adaptive_v2_20260514T132705_result.json`
- **Structured JSON:** [`6387aa845aae52469a68.json`](../../sessions/63/6387aa845aae52469a68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

step_metrics.jsonl 中 `b_star_raw` 和 `b_star_ema` 字段完整存在。

---

## 总结

### 1. 代码修改 diff（8 处）

| 位置 | 修改 |
|------|------|
| `WeightedTrainer.__init__` | 新增 `ema_alpha` 参数、`_b_star_ema` 状态 |
| `compute_loss` adaptive 分支 | `b_val` → `b_star_raw` + EMA 平滑后赋值给 `b_val` |
| `step_info` | adaptive 时追加 `b_star_raw`、`b_star_ema` |
| `training_step` | wandb 日志增加 `weighting/b_star_raw`、`weighting/b_star_ema` |
| `parse_args` | `--n_min` help 文本更新；新增 `--ema_alpha` |
| `main()` n_min 默认值 | `max(1, int(batch_size*0.75))` → `max(1, batch_size//4)` |
| `WeightedTrainer` 实例化 | 传入 `ema_alpha` |
| `config_summary` | 新增 `ema_alpha` 字段 |

### 2. dry-run 验证结果

5 step GPU 训练通过，EMA 平滑效果显著（raw CV 大幅高于 ema CV），`step_metrics.jsonl` 格式正确。

### 3. 提交脚本

路径：`/root/provenance_weight_training/scripts/submit_adaptive_v2.sh`

```bash
bash submit_adaptive_v2.sh 1 42     # GPU 1 跑 seed42
bash submit_adaptive_v2.sh 1 all    # GPU 1 串行跑 3 个 seed
```

### 4. 新增/修改命令行参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--n_min` | int | `max(1, batch_size//4)` (原为 `batch_size*0.75`) | batch_size=4 时 1→释放 weighting 空间 |
| `--ema_alpha` | float | 0.1 | **新增**，EMA 平滑因子（0=不平滑，1=无记忆） |

---
