# analysis v4 taxei fixed inject25 s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915_result.json`
- **Structured JSON:** [`0cf3fad4f6b752531bf9.json`](../../sessions/0c/0cf3fad4f6b752531bf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验分析结果：v4-taxei-fixed-inject25-s1

### 提取指标

| 指标 | 值 |
|------|-----|
| train_loss | **0.4243** |
| train_steps | 1635 |
| train_duration | 57.5 min |
| epochs | 3.0 |
| final step loss | 0.2337 |
| memory | 18.0 GiB |
| EXIT_CODE | 0 (正常完成) |

### Checkpoint 路径

```
/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635
```

### 异常检查

无异常。训练正常完成，无 OOM/error，exit code=0。无 W&B 记录（wandb 目录不存在）。

### Seed 对比（inject25% 系列）

| Seed | train_loss | duration |
|------|-----------|----------|
| 42 (r2) | 0.285 | 58 min |
| 0 | 0.4258 | 56.1 min |
| 123 | 0.4253 | 55.9 min |
| **1** | **0.4243** | **57.5 min** |

seed=1 的 train_loss=0.4243 与 seed=0 (0.4258) 和 seed=123 (0.4253) 高度一致，三者差异 <0.002，属正常随机波动。seed=42(r2) 的 0.285 明显偏低，可能是该 run 报告的是 final step loss 而非 average train_loss（本次 seed=1 的 final step loss 也是 0.2337）。

**结论**：seed=1 训练成功，loss 水平与同系列其他 seed 一致，无异常。Registry 已更新为 DONE。

---
