# eval arc easy per example setup

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_arc-easy-per-example-setup_20260520T060613_result.json`
- **Structured JSON:** [`6b4d900ae4a34b3cbfd3.json`](../../sessions/6b/6b4d900ae4a34b3cbfd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功启动，第一个模型 (GatedDeltaNet-pure) 正在加载权重，`allow_neg_eigval=True` 已注入。

**汇总：**
- 15 个模型全部位于 `/root/autodl-tmp/models_1.3b/`，完整无缺
- 无现有 ARC-Easy per-example 数据，需全部重跑
- Batch 脚本 `run_arc_easy_all.sh` 已部署，每个模型输出到独立目录 `arc_easy/{model_name}/`，包含 `samples/arc_easy.jsonl`
- 实验 `exp-arc-easy-eval` 已提交（PID 620603，tmux session），parent=exp-001，timeout 8h
- Cron 系统自动监控，完成后回调

---
