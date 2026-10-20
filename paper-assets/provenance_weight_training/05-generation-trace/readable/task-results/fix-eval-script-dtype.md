# fix eval script dtype

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_script_dtype_20260522T143115_result.json`
- **Structured JSON:** [`368d53fe2cafadd449a8.json`](../../sessions/36/368d53fe2cafadd449a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

**报告：**

- 文件：`/root/provenance_weight_training/eval_perplexity.py`（即任务中提到的 `eval_ppl.py`）
- 修改处数：**1 处**（第 92 行）
- 修改前：`ckpt_path, torch_dtype=torch.float16, trust_remote_code=True`
- 修改后：`ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True`
- 文件中已无残留的 `torch.float16`。

---
