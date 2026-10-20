# ops d066 docred batch eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_docred_batch_eval_20260520T135653_result.json`
- **Structured JSON:** [`e7d3985872daabab1af8.json`](../../sessions/e7/e7d3985872daabab1af8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

10 个 DocRED beam sweep 文件全部 eval 完成。汇总：

## 结果总表

| Config | Model | Beam | Mode | E-F1 | R-F1 | ET% | RV% | DR% | CF% | PF% |
|--------|-------|------|------|------|------|-----|-----|-----|-----|-----|
| qwen_greedy_s1 | Qwen | greedy | constrained | 80.54 | 43.64 | 0.00 | 0.00 | 0.00 | 0.12 | 7.5 |
| qwen_greedy_unc | Qwen | greedy | unconstrained | 81.34 | 44.56 | 0.00 | 0.24 | 0.20 | 0.03 | 6.5 |
| qwen_beam2_s1 | Qwen | 2 | constrained | 84.46 | 47.30 | 0.00 | 0.00 | 0.00 | 0.08 | 1.0 |
| qwen_beam2_unc | Qwen | 2 | unconstrained | 84.25 | 47.39 | 0.00 | 0.11 | 0.43 | 0.00 | 1.5 |
| qwen_beam8_s1 | Qwen | 8 | constrained | **84.54** | **48.43** | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 |
| qwen_beam8_unc | Qwen | 8 | unconstrained | 83.95 | 47.84 | 0.00 | 0.11 | 0.33 | 0.00 | 2.0 |
| llama_beam2_s1 | Llama | 2 | constrained | 85.60 | 51.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 |
| llama_beam2_unc | Llama | 2 | unconstrained | 85.34 | 51.31 | 0.00 | 0.07 | 0.11 | 0.05 | 1.0 |
| llama_beam8_s1 | Llama | 8 | constrained | 85.76 | 51.74 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 |
| llama_beam8_unc | Llama | 8 | unconstrained | **85.77** | **51.97** | 0.00 | 0.07 | 0.00 | 0.05 | 0.5 |

## 关键发现

1. **Llama 全面优于 Qwen**：R-F1 差距 ~3-8 个点（51.2-52.0 vs 43.6-48.4）
2. **Beam search 对 Qwen 提升大**：greedy→beam8 R-F1 +4.79；Llama beam2→beam8 仅 +0.57
3. **Constrained vs Unconstrained F1 差异极小**（Δ < 1 点），但 constrained 将 RV%/DR% 降至 0.00
4. **Beam search 大幅降低 Qwen 的 parse failure**：7.5%→1.0%；Llama 本身就低（0.5%）
5. **beam8 + constrained 对 Qwen 是最优配置**（R-F1=48.43, 所有违规=0）；Llama 在 beam8 下 constrained/unconstrained 几乎无差别

结果已写入 `artifacts/d066_beam_sweep/docred_eval_results.md`。

---
