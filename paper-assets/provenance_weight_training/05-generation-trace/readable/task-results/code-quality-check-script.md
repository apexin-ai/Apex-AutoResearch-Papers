# code quality check script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_quality-check-script_20260513T190524_result.json`
- **Structured JSON:** [`d66b23c015df32518910.json`](../../sessions/d6/d66b23c015df32518910.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/root/provenance_weight_training/check_synthetic_quality.py` 并验证通过，`--help` 正常输出。数据就绪后运行：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python check_synthetic_quality.py --input data/synthetic/depth_1_merged.jsonl
```

---
