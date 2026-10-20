# code fewnerd analysis script

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fewnerd_analysis_script_20260516T171529_result.json`
- **Structured JSON:** [`73e22579fc1aedee12ca.json`](../../sessions/73/73e22579fc1aedee12ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪：`/root/autodl-tmp/struct_self_consist_ie/code/analyze_fewnerd_results.py`

Pilot dry-run 通过，所有 6 个模块正常输出。LP 信号在 pilot 数据中为 N/A 是预期的（pilot 没有 logprob 字段），exp-021 inference 完成后直接运行：

```bash
python code/analyze_fewnerd_results.py --input_dir output/exp_021_inference/
```

---
