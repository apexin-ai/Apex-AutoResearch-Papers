# ops d018 kill exp005

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d018-kill-exp005_20260517T211331_result.json`
- **Structured JSON:** [`b95cd73144b010337962.json`](../../sessions/b9/b95cd73144b010337962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇报如下：

## 结果

| 项目 | 状态 |
|------|------|
| kill exp_005 (PID 116947) | ✓ 成功，进程已终止 |
| 备份 results | ✓ 已保存至 `phase1_adaptive_k20_seed42_results_gen0-4_backup.json` |
| cuda:1 残留检查 | ✓ 无 exp_005 残留 |
| exp_004 独占 cuda:1 | ✓ 正常运行 |

## nvidia-smi 输出

```
GPU 0: RTX PRO 6000 Black | 25017MiB/97887MiB | 74% util | PID 134918 (python)
GPU 1: RTX PRO 6000 Black | 25017MiB/97887MiB | 86% util | PID 135411 (python)
```

cuda:1 上仅有 exp_004 (PID 135411) 在跑，GPU 利用率 86%，状态正常。

exp_004 进程详情：`python run_phase1.py --condition fixed_mix --seed 42 --generations 10 --signal log_det --tau 0.002 --k 0 --signal_mode per_gen --gpu 0`（已运行约 3.3 小时）。

---
