# code exp docred bcs expanded

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_docred_bcs_expanded_20260519T114253_result.json`
- **Structured JSON:** [`2f05c6edb389ff4d511d.json`](../../sessions/2f/2f05c6edb389ff4d511d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交运行 (PID=604284)。

**状态汇总**:
- 脚本: `/root/schema-dag-extraction/src/run_docred_bcs_expanded.py`
- 输出: `/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/`
- 日志: `artifacts/exp_docred_bcs_expanded/run.log`
- Registry: `exp_docred_bcs_expanded` → RUNNING

**实验设计**:
- 110 total batches: 2 counts (16,32) x (25 random + 15 low-BCS + 15 high-BCS)
- 70 batches 复用已有推理结果 (25 random + 5 old extreme per count)
- 40 new batches 需要新推理 (10 new extreme per BCS group per count)
- 分析包含: bootstrap regression, 2x2 factorial interaction CI, TOST equivalence (2pp/3pp/5pp)

预计 2-3 小时完成。可以用 `tail -20 artifacts/exp_docred_bcs_expanded/run.log` 查看进度。

---
