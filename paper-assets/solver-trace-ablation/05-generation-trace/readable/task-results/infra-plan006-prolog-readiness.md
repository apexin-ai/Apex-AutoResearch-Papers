# infra plan006 prolog readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan006-prolog-readiness_20260514T090023_result.json`
- **Structured JSON:** [`ab2ca73b7de0a322bcfd.json`](../../sessions/ab/ab2ca73b7de0a322bcfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**7/7 全部 PASS，Prolog 训练 pipeline 完全就绪。**

Report 已写入 `artifacts/plan006/readiness_report.md`。关键发现：

- **代码层**：`train_grpo.py`、`eval_sta.py`、`src/sta/prolog_reward.py`、`src/solvers/prolog.py` 全部已实现 Prolog 支持
- **配置层**：3 个 Prolog YAML 配置可直接使用（exec_only / exec_only_k16_warmup / exec_sta）
- **数据层**：复用 `train_500_seed42.jsonl`，不需要 Prolog ground truth（GRPO 流程由模型生成 Prolog → swipl 验证）
- **环境层**：swipl 8.4.2 可执行，Qwen3-4B 已下载，磁盘剩余 112GB
- **唯一注意项**：启动时需手动 `export CUDA_VISIBLE_DEVICES=N`（C002/C005），建议先跑 `sta_prolog.py --test` 做 smoke test

---
