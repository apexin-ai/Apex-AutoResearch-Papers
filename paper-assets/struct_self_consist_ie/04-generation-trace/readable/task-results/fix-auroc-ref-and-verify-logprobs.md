# fix auroc ref and verify logprobs

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_auroc_ref_and_verify_logprobs_20260516T174529_result.json`
- **Structured JSON:** [`c9cec8f241e95da154b8.json`](../../sessions/c9/c9cec8f241e95da154b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成：

1. **SCIERC_REF `lp_auroc`** — 已从 `0.5035` 更新为 `0.578`，附注释 `# instance-level AUROC`。脚本内部 sample-level 计算逻辑未动（第 277 行仍计算 `qe_results["LP"]["auroc"]`）。

2. **推理命令** — 已追加到 `train_config_fewnerd_exp021.yaml` 末尾注释块，包含 `--collect_logprobs`。

---
