# diagnose repo level cls 8b conda

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_repo-level-cls-8b-conda_20260514T010856_result.json`
- **Structured JSON:** [`eda1c1b25f9f66f11d01.json`](../../sessions/ed/eda1c1b25f9f66f11d01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告: repo-level-cls-8b-conda

### 实际失败原因
**预期的 early stop，非真正失败。** 训练被人工 kill（符合 D056 决策），cron 检测到进程死亡 5 次后自动标记为 failed。原始 PID 185438 已不存在。

训练运行到 step 662/6633 (10%)，最后记录的 loss=0.9534 (step 650)。train.log 最后更新时间 08:58，之后无新写入。

### Checkpoint 状态
三个 checkpoint 全部完好：

| Checkpoint | 时间 | eval_loss | 状态 |
|---|---|---|---|
| checkpoint-200 | 07:27 | **0.0796** (best) | 完整（adapter_model.safetensors 58MB + optimizer + trainer_state） |
| checkpoint-400 | 08:08 | - | 存在 |
| checkpoint-600 | 08:50 | - | 存在 |

trainer_state.json 确认 `best_global_step=200, best_metric=0.0796`。

### Eval 状态
**Eval 正在运行。** GPU 3 上有进程 PID 194821：
- 命令: `python3 eval_repo_cls.py --checkpoint_dir checkpoint-200 --model_name Qwen3-8B --batch_size 8`
- GPU 占用: 21634MiB, 利用率 88%
- 输出目录 `/root/autodl-tmp/results/repo_cls_8b_conda_eval/` 已创建（09:00）但尚无输出文件，eval 仍在进行中

### 建议下一步
1. 将实验状态从 "failed" 改为 "early-stopped (expected)"
2. 等待 eval 完成——监控输出文件 `eval_repo_cls.json` 和 `eval_repo_cls_predictions.jsonl` 是否生成
3. Eval 完成后收集结果，与其他实验对比

---
