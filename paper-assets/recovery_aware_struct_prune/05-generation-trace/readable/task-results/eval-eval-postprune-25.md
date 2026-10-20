# eval eval postprune 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_eval_postprune_25_20260516T200920_result.json`
- **Structured JSON:** [`6a3d7d8d63ee76cf984e.json`](../../sessions/6a/6a3d7d8d63ee76cf984e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已经完成，结果已在 registry 中。

## 25% Sparsity Post-Prune GSM8K 结果

| Method | Accuracy | N |
|--------|----------|---|
| RASP 25% | **21%** | 100 |
| Standard 25% | **16%** | 100 |

对比 20% sparsity：
- RASP: 31% → 21% (−10 pp)
- Standard: 27% → 16% (−11 pp)

RASP 在 25% sparsity 仍然领先 Standard 5 个百分点，差距与 20% 时 (4 pp) 基本一致。两个实验均已标记 DONE，结果 JSON 在 `/root/autodl-tmp/recovery_aware_struct_prune/results/` 下。

---
