# exp llama cross model v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama-cross-model-v2_20260516T061948_result.json`
- **Structured JSON:** [`c93e8631d2b51970ec9f.json`](../../sessions/c9/c93e8631d2b51970ec9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，环境兼容。

---

## 评估结果

### 上次 `llama-cross-model-expanded` 被 kill 原因
- 启动于 2026-05-15 19:48:50，被 kill 于 20:10:06（运行约 21 分钟）
- 日志显示第一个 task (identify-life-stages-1) 的 episode 0 仍在跑时被外部 kill（vLLM EngineCore 收到 shutdown 信号，abort 1 request）
- 无结果保存，无部分数据可复用

### 新脚本已就绪

**路径**: `/root/autodl-tmp/simgate-modular-routing/scripts/run_llama_cross_model_v2.sh`

**配置**:
| 项目 | 值 |
|------|-----|
| 模型 | Llama-3.1-8B-Instruct (本地已有) |
| GPU | 0 (RTX 5090 32GB, 空闲) |
| Tasks | 7: freeze, identify-life-stages-1, lifespan-longest-lived, inclined-plane-determine-angle, measure-melting-point-unknown-substance, chemistry-mix, grow-fruit |
| Episodes | 10/task |
| 输出 | `data/llama-cross-model-v2/` |
| 预计耗时 | **~5.5 小时** (70 pairs × ~4.7 min/pair) |

**Task 选择依据**: Plan_c (Qwen) 中 internal death rate 50-60% 的 7 个 tasks，排除了 find-non-living-thing (0% death)。

**注意**: GPU 是 RTX 5090 32GB（非任务描述中的 A6000 48GB），Llama-3.1-8B bf16 约 16GB，gpu_memory_utilization=0.85 可用 ~27GB，足够。

---

需要通过 `submit_training_job` 提交此脚本。提交命令：
```
bash /root/autodl-tmp/simgate-modular-routing/scripts/run_llama_cross_model_v2.sh
```

---
