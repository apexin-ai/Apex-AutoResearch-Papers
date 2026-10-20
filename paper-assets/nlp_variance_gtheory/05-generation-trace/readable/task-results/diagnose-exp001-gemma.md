# diagnose exp001 gemma

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp001_gemma_20260521T024215_result.json`
- **Structured JSON:** [`f615d7eddffe42bffb04.json`](../../sessions/f6/f615d7eddffe42bffb04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是完整诊断报告。

---

## 诊断结果

### 1. 已产出数据 (exp001_gemma/)

| Shard | 行数 | 条件数 | 精度 |
|-------|------|--------|------|
| shard_0 | 23,200 | 116 | 全部 bfloat16 |
| shard_1 | 20,400 | 102 | 全部 bfloat16 |
| shard_2 | 21,400 | 107 | 全部 bfloat16 |
| shard_3 | 21,400 | 107 | 全部 bfloat16 |
| **合计** | **86,400** | **432** | **bfloat16 only** |

每条件 200 items，数据完整。float32 和 float16 记录数均为 0。

### 2. 崩溃原因

4 个 GPU 日志完全一致：
```
pydantic_core.ValidationError: The model type 'gemma2' does not support float16.
Reason: Numerical instability. Please use bfloat16 or float32 instead.
```
崩溃点：`vllm_runner.py:71` → `LLM()` 构造函数 → vLLM ModelConfig pydantic 校验拒绝 float16。

### 3. 设计矩阵分析

每 shard 324 条件 (含 header 325 行)，总计 1,296 条件：

| Shard | bfloat16 | float16 | float32 |
|-------|----------|---------|---------|
| 0 | 116 | 100 | 108 |
| 1 | 102 | 106 | 116 |
| 2 | 107 | 104 | 113 |
| 3 | 107 | 122 | 95 |
| **合计** | **432** | **432** | **432** |

### 4. float32 未跑到的原因

`run_experiment.py` 用 `df.groupby(["model", "precision"])` 分组执行，字母序为 **bfloat16 → float16 → float32**。bfloat16 全部完成后，首次尝试 float16 即崩溃，float32 **从未执行**。

### 5. fp32 补跑状态 — 已在进行中

`exp001_gemma_fp32/` 目录已创建独立 shard（每 shard 108 个 float32 条件），4 GPU 进程正在运行：

| Shard | 已完成 | 总计 | 进度 |
|-------|--------|------|------|
| 0 | 23 | 108 | 21% |
| 1 | 23 | 108 | 21% |
| 2 | 23 | 108 | 21% |
| 3 | 23 | 108 | 21% |
| **合计** | **92** | **432** | **~21%** |

速度 ~46 秒/条件/GPU，剩余 ~85 条件/shard，预计 **~65 分钟后完成**。

### 6. 数据质量评估

- bfloat16 数据完整且健康（432/432 条件，86,400 records）
- float16 永久排除（Gemma-2 架构限制，非配置错误）
- float32 补跑正常推进，无需额外干预

### 7. 最终预期

| 精度 | 条件 | Records | 状态 |
|------|------|---------|------|
| bfloat16 | 432 | 86,400 | DONE |
| float32 | 432 | 86,400 | RUNNING (21%) |
| float16 | 432 | — | EXCLUDED |
| **有效合计** | **864** | **172,800** | |

```json
{"completed_records": 104800, "expected_total_bf16_fp32": 172800, "missing_conditions": 340, "error_type": "model_incompatibility_float16", "fix_steps": ["fp32补跑已自动启动(exp001_gemma_fp32/), 4 GPU并行, 预计~65分钟完成", "完成后合并: cat exp001_gemma/shard_*.jsonl exp001_gemma_fp32/shard_*.jsonl > exp001_gemma/all_results.jsonl", "从设计矩阵中永久移除float16条件(Gemma-2不支持)"], "can_auto_fix": true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "completed_records": 104800,
    "expected_total_bf16_fp32": 172800,
    "missing_conditions": 340,
    "error_type": "model_incompatibility_float16",
    "fix_steps": [
      "fp32补跑已自动启动(exp001_gemma_fp32/), 4 GPU并行, 预计~65分钟完成",
      "完成后合并: cat exp001_gemma/shard_*.jsonl exp001_gemma_fp32/shard_*.jsonl > exp001_gemma/all_results.jsonl",
      "从设计矩阵中永久移除float16条件(Gemma-2不支持)"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
