# analysis math deepseek lomo

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_math_deepseek_lomo_20260522T124027_result.json`
- **Structured JSON:** [`322661fb60b70a08324d.json`](../../sessions/32/322661fb60b70a08324d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MATH DeepSeek LOMO 结果：

| Benchmark | Δitem_id (pp) | ΔG_item |
|-----------|--------------|---------|
| ARC | +3.45 | +0.0022 |
| HellaSwag | +2.57 | −0.0061 |
| GSM8K | +0.45 | −0.0088 |
| **MATH** | **+2.45** | **+0.0009** |

MATH 的 ΔG_item = +0.0009，是 5 个 benchmark 中最小的，远低于 0.01 阈值。移除 DeepSeek 后 item_id% 从 24.03% 升至 26.48%（+2.45pp），符合预期——去掉一个模型后 model 方差减小，item 占比相对升高。

注意：初始计算时发现 LOMO 脚本的 `compute_g_item` 公式与 `math_8model_verified.json` 不一致（LOMO 脚本将 interaction 除以所有非 item 非该 facet 的乘积，而正确的 D-study 公式是除以该 facet 本身的 n_levels）。最终使用了与 verified JSON 一致的 D-study 公式，8-model 数值完全吻合。

---
