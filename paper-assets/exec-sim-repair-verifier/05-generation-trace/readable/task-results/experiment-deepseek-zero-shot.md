# experiment deepseek zero shot

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_deepseek-zero-shot_20260517T124706_result.json`
- **Structured JSON:** [`daea59f69c6541d4d172.json`](../../sessions/da/daea59f69c6541d4d172.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

pass/fail
```

**数据集**: 用与 Qwen3 零样本实验 (`llm_judge_zeroshot.py`) 相同的测试集和数据加载方式。

**运行参数**:
- `temperature=0`（确定性推理）
- batch inference 自动分批
- 输出预测结果到 `artifacts/deepseek_coder_6b_zeroshot_results.json`

**评估**:
- 计算：accuracy, precision, recall, F1（per-class + macro）
- 与已有实验对比（如果有 Qwen3 零样本结果）
- 输出 metrics 到 `artifacts/deepseek_coder_6b_zeroshot_metrics.json`

**执行**:
1. SSH 到 home-1x5090
2. 找到已有 zeroshot 脚本或创建新的推理脚本
3. 用 DeepSeek-coder-6.7B-instruct 跑推理
4. 计算指标并保存结果

先 SSH 连上服务器探索已有脚本，然后执行。

---
