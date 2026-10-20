# research v2 rescore check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_v2_rescore_check_20260515T225229_result.json`
- **Structured JSON:** [`57c3da14e547353669bb.json`](../../sessions/57/57c3da14e547353669bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已经很清楚了。总结如下：

---

## 结论

### v2 rescore 改了什么

`rescore_accuracy.py` 是一个**纯离线重评分脚本**，改动内容：

1. **增强 answer matcher**：增加了对 radical 简化（`\sqrt{117}` → `3\sqrt{13}`）、度数符号（`72^\circ` = `72`）、分数与小数互转（`\frac{1}{2}` = `0.5`）的匹配支持
2. **新增 truncation 诊断指标**：`output_truncated_count/rate`、`extraction_failure_count/rate`
3. 对已有 JSON 中的每个 item 重新执行 `answers_match(pred, ref)`，覆写 `match` 字段和 accuracy

### 是否需要 GPU

**不需要。** rescore 只读已有 generation JSON 中的 `pred_answer` 和 `ref_answer` 字段，重新做字符串匹配，完全是 CPU 离线操作。不需要加载模型，不需要重新推理。

### batch1 需要 rescore 的文件

脚本 `main()` 中硬编码的 target_files：

| 文件 | 对应条件 |
|------|----------|
| `accuracy_eval_qw_s015.json` | Qwen s015 |
| `accuracy_eval_qw_s020.json` | Qwen s020 |
| `accuracy_eval_qw_s025.json` | Qwen s025 |
| `accuracy_eval_qw_s030.json` | Qwen s030 |
| `accuracy_eval_ds_s015.json` | DeepSeek s015 |
| `accuracy_eval_ds_s030.json` | DeepSeek s030 |
| `accuracy_eval_ds_dense_n50.json` | DeepSeek dense |

这些文件全部存在于 `/root/autodl-tmp/pacs/analysis_output/`。

### rescore 命令

```bash
cd /root/autodl-tmp/pacs && python rescore_accuracy.py
```

脚本会先跑 unit test 验证 matcher 正确性，然后逐文件 rescore 并 in-place 覆写 JSON，打印 accuracy 变化对比表。

---
