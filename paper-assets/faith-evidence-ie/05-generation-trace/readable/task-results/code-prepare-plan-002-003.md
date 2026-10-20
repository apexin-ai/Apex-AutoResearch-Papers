# code prepare plan 002 003

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_plan_002_003_20260515T195611_result.json`
- **Structured JSON:** [`feff43b2e16a2fc35337.json`](../../sessions/fe/feff43b2e16a2fc35337.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### plan_002: `scripts/eval_test_set.sh`
- 使用 RSFT best config: **rsft_s43** (dev rel_f1=0.4683, 三 seed 中最佳)
- 调用 `freige.eval.test_inference`，生成 `predictions.json` + `codalab_submission.json`
- bf16 推理（`--no-quantize`），batch_size=16, max_new_tokens=1024
- 输出到 `/root/autodl-tmp/eval_results/test_set/`

### plan_003: `scripts/edcr_diagnostic.sh`
- 调用已有 `freige.eval.cross_method_table`，覆盖 11 种方法配置
- Dry-run 验证通过，当前结果：

| Method | rel_f1 | evi_f1 | EDCR | ΔEDCR |
|--------|--------|--------|------|-------|
| SFT baseline (quant) | 0.4057 | 0.7979 | 0.7118 | +0.00p |
| CED-reranker (N=8) | 0.4864 | 0.8188 | 0.6156 | -9.62p |
| RSFT-CED 3-seed mean | 0.4596±0.013 | 0.8144±0.005 | 0.6434±0.011 | -6.83p |
| GRPO bf16 (ckpt100) | 0.4549 | 0.8086 | 0.6318 | -8.00p |
| DPO-CED | MISSING | — | — | — |

DPO 的 eval 结果尚未生成（`dpo_ced/metrics.json` 不存在），脚本会自动跳过并打印 MISSING。

---
