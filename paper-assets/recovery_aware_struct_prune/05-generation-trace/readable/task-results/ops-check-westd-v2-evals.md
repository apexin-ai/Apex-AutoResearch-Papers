# ops check westd v2 evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd_v2_evals_20260515T201003_result.json`
- **Structured JSON:** [`cac3fac351672f847622.json`](../../sessions/ca/cac3fac351672f847622.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，registry 已更新为 DONE。

**结果总结：**

| 实验 | Accuracy | N_correct/N_total | EOS Rate | Avg Len |
|------|----------|-------------------|----------|---------|
| Standard SFT (westd) | **63%** | 63/100 | 0.97 | 260.57 |
| RASP SFT (westd) | **67%** | 67/100 | 0.99 | 182.39 |

与预期对比：
- **Standard 63%** — 接近预期 64%，跨服务器可复现 ✓
- **RASP 67%** — 超出预期 57%，比 Standard 高 4 个点。RASP 在 westd 上的 SFT 恢复效果优于 westb，且 eos_rate 更高（0.99）、生成更简洁（avg_len 182 vs 261）

---
