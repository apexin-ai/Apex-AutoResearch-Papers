# code merge script

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_merge_script_20260512T105712_result.json`
- **Structured JSON:** [`92717a50ce31cc545b82.json`](../../sessions/92/92717a50ce31cc545b82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证可用。`/root/carc/merge_results.py` 功能：

- 加载多个 npz 文件，concatenate 所有 raw arrays
- 从合并数据重新计算 (b)(c)(d)(e) 所有统计量和 per-layer breakdown
- Near-zero fractions 和 lag-1 autocorrelation 从 JSON 加权平均/取均值
- 调用 `judge()` 得出 verdict
- 输出 `results_merged.json` + 与 `carc_mvp.py` 一致的 summary

运行命令：
```bash
cd /root/carc && python3 merge_results.py \
    --input results_seed42 results_seed1337 \
    --tau 0.7 \
    --output results_merged.json
```

---
