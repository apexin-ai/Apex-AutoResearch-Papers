# diagnose plan 002 dryrun exit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-002-dryrun-exit_20260514T050606_result.json`
- **Structured JSON:** [`dca84e5edc0b984aecf6.json`](../../sessions/dc/dca84e5edc0b984aecf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练**仍在进行中**，尚未完成。

## 结果

| 项目 | 状态 |
|------|------|
| **日志** | `/root/autodl-tmp/simgate-modular-routing/logs/plan002_dryrun.log` — 进度 **310/1163 steps (27%)**，速度 ~1.37 it/s |
| **Checkpoint** | 目录 `/checkpoints/plan-002-dryrun/` 存在但**为空**（尚未保存） |
| **GPU0** | PID 182475 占用 **29824 MiB**，正在运行 |

### 训练配置摘要（从日志提取）
- 模型: Qwen3-1.7B + LoRA r=16 (0.37% trainable)
- 数据: 5880 samples, 124 episodes train / 33 val
- 类别权重: internal=11.07, deterministic=0.52 (少数类上采样)
- 总步数: 1163, 预计剩余 ~10 分钟

**结论: 训练进行中（running），无报错。** 预计 ~10 分钟后完成，届时再检查 checkpoint 和最终结果。

---
