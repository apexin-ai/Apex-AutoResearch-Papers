# analysis split consistency check

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_split-consistency-check_20260514T135727_result.json`
- **Structured JSON:** [`378f19009cd4f5d9f4ef.json`](../../sessions/37/378f19009cd4f5d9f4ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：三个 encoder probe 的 test set 完全一致。**

MD5 校验结果：
```
7bfeb5ce8700f8da5010a503737de7b0  checkpoints/split_info.json          (probe_001 / SFR)
7bfeb5ce8700f8da5010a503737de7b0  checkpoints_ablation_e5large/split_info.json  (e5-large)
7bfeb5ce8700f8da5010a503737de7b0  checkpoints_ablation_bgem3/split_info.json    (bge-m3)
```

三个文件字节数相同（201469 bytes）、MD5 哈希完全一致，说明 train/val/test split 是同一份文件的拷贝。当前报告的 test macro_f1 结果（SFR 0.905, e5-large 0.9363, bge-m3 0.9413）可直接用于论文，是 apple-to-apple 对比。

---
