# analysis gemma4 exit check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma4_exit_check_20260522T154445_result.json`
- **Structured JSON:** [`696105205595c373f725.json`](../../sessions/69/696105205595c373f725.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：**成功 (SUCCESS)**

### 结果摘要

| 项目 | 状态 |
|------|------|
| **Phase 1** (trace 生成) | 完成，520/520 prompts 全部处理 |
| **Phase 2** (layer selection bias) | 完成，168/168 layer×window 组合扫完 |
| **结果文件** | `/root/autodl-tmp/contrastive_trace_safety/artifacts/advbench_layer_bias_gemma4_results.json` (35KB, 23:42 写入) |
| **错误** | 0 Traceback, 0 OOM |

### Phase 2 关键 Metrics

```
CR-composite 最优层:  L0  (0.0%)
Precision 最优层:     L14 (34.1%)
Bal. accuracy 最优层: L7  (17.1%)
Inv. FPR 最优层:      L3  (7.3%)
Divergence:           34.1pp — REPLICATED
```

Layer selection bias 在 Gemma-4 上复现成功，不同指标选出的最优层高度分散（L0/L3/L7/L14），最大分歧 34.1 个百分点。

### 注意

Trace 文件没有保留在独立目录 `advbench_gemma4_traces/` 中（该目录不存在），可能是脚本直接在内存中处理后只输出了聚合结果 JSON。

---
