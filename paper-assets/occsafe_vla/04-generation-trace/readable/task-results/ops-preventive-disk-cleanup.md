# ops preventive disk cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_preventive-disk-cleanup_20260522T133632_result.json`
- **Structured JSON:** [`71e2fcd4a6a2ce2aeec6.json`](../../sessions/71/71e2fcd4a6a2ce2aeec6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### westd-10894
- 删除 4 个 10000_chkpt（每个 ~15G，共 ~60G）：
  - `ablation_occ_detach_s2/...--10000_chkpt`
  - `ablation_random_occ_s2/...--10000_chkpt`
  - `depth_s2/...--10000_chkpt`
  - `depth_s3/...--10000_chkpt`
- 释放 ~59G（156G → 97G used）
- **最终可用：154G / 250G（39% used）**，30K checkpoint 写入空间充足

### westd-34685
- 删除 2 个 checkpoint + 整个 occ_s1_fresh 目录：
  - `occ_s1_fresh/...--47500_chkpt`（15G）
  - `occ_s1_fresh/...--50000_chkpt`（15G）
  - `occ_s1_fresh/` 残留目录（仅含 dataset_statistics.json，3KB）
- 释放 ~30G（111G → 81G used）
- **最终可用：270G / 350G（24% used）**

---
