# code plan 003 eval prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-003-eval-prep_20260514T084744_result.json`
- **Structured JSON:** [`b1369ac6032f724be13c.json`](../../sessions/b1/b1369ac6032f724be13c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。结果总结：

## 调研结果

**方案 A（离线 eval）确认可行。** `eval_end_to_end.py` 基于预收集的 counterfactual 数据（每个 episode 同时有 internal 和 deterministic 轨迹分数），路由决策只选用哪个分数。

## 关键差异：classification head vs implicit router

| | 原 trained-router (v6) | ablation-b implicit router |
|---|---|---|
| 模型类型 | `AutoModelForSequenceClassification` | `AutoModelForCausalLM` |
| 输出 | 2-class logits | 生成文本 |
| 路由判断 | argmax(logits) | `[SIMULATE]` 前缀 → deterministic |
| adapter task_type | SEQUENCE_CLASSIFICATION | CAUSAL_LM |

## 脚本 `eval_implicit_router.py` 已部署并验证

- **Dry-run (3 episodes, 30 steps)**: 9.6s, ~3.1 steps/s
- **全量估时**: 2040 steps ÷ 3.1 steps/s ≈ **11 分钟**
- 路由解析正确（`[SIMULATE]` prefix detection）
- Metrics 计算与 `eval_end_to_end.py` 一致（bootstrap CI, death rate, sim ratio）
- 额外输出 step-level 和 episode-level routing accuracy vs oracle

## 运行命令

```bash
cd /root/autodl-tmp/simgate-modular-routing && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && \
python src/eval_implicit_router.py
```

需要我现在启动全量 eval 吗？

---
