# computation raw kappa recompute

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_computation_raw-kappa-recompute_20260519T045812_result.json`
- **Structured JSON:** [`4a493f63a5a9a03fa659.json`](../../sessions/4a/4a493f63a5a9a03fa659.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果表：

| Exp | Model | Dataset | Condition | raw_κ | Eff-K | Valid% | N | Notes |
|-----|-------|---------|-----------|-------|-------|--------|---|-------|
| **Mistral 3-seed (FOLIO-204, K=12)** |
| exp-033 | Mistral-7B | FOLIO-204 | seed=42, T=0.7 | 0.5006 | 1.84 | 83.4% | 204 | Baseline |
| exp-052 | Mistral-7B | FOLIO-204 | seed=123, T=0.7 | 0.4908 | 1.88 | 82.6% | 204 | |
| exp-053 | Mistral-7B | FOLIO-204 | seed=456, T=0.7 | 0.5074 | 1.82 | 81.5% | 204 | |
| **Temperature sensitivity (Mistral-7B, FOLIO-204, K=12)** |
| exp-057 | Mistral-7B | FOLIO-204 | T=0.3 | 0.5267 | 1.77 | 85.9% | 204 | |
| exp-033 | Mistral-7B | FOLIO-204 | T=0.7 | 0.5006 | 1.84 | 83.4% | 204 | |
| exp-054 | Mistral-7B | FOLIO-204 | T=1.0 | 0.4788 | 1.91 | 75.9% | 204 | |
| exp-055 | Mistral-7B | FOLIO-204 | multi-temp | 0.4792 | 1.91 | 79.1% | 204 | |
| **K sensitivity (Mistral-7B, FOLIO-204, T=0.7)** |
| exp-051 | Mistral-7B | FOLIO-204 | K=4 | 0.4576 | 1.69 | 78.9% | 204 | |
| exp-051 | Mistral-7B | FOLIO-204 | K=8 | 0.4906 | 1.80 | 83.3% | 204 | |
| exp-051 | Mistral-7B | FOLIO-204 | K=16 | 0.4907 | 1.91 | 81.8% | 204 | |
| exp-051 | Mistral-7B | FOLIO-204 | K=20 | 0.4909 | 1.94 | 81.3% | 204 | |
| **Qwen models** |
| exp-027 | Qwen3-14B | FOLIO-204 | K=12 | 0.7732 | 1.26 | 99.9% | 204 | raw≈unified |
| exp-035 | Qwen2.5-7B | FOLIO-204 | K=12 | 0.6586 | 1.46 | 99.9% | 204 | raw≈unified |
| exp-036 | Qwen2.5-14B | FOLIO-204 | K=12 | 0.7452 | 1.30 | 99.9% | 204 | raw≈unified |
| exp-038 | Qwen2.5-14B | LogiQA-200 | K=12 | 0.8210 | 1.20 | 100% | 200 | raw=unified |
| **ProofWriter** |
| exp-046 | Mistral-7B | PW-600 | K=12 | 0.2102 | 3.62 | 79.0% | 600 | |

关键发现：
- Qwen 模型 raw 与 unified κ 几乎相同（valid rate ≈100%，无非标准答案），符合预期
- Mistral raw κ 系统性高于 unified κ（如 exp-033: 0.5006 vs 0.4598），因为非标准答案在 unified 中被映射为 Unknown 降低了一致性
- 脚本已添加 `--raw` flag，默认行为不变，向后兼容

JSON 已保存并注册为 artifact `fleiss_kappa_raw_all`。

---
