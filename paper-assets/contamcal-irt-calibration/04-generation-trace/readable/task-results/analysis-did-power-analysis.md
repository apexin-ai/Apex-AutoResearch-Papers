# analysis did power analysis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_did-power-analysis_20260521T075327_result.json`
- **Structured JSON:** [`2dc5ec002a736f4ed7ae.json`](../../sessions/2d/2dc5ec002a736f4ed7ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### MMLU (n_treated=3,540, n_untreated=10,502)

| Model | DiD (pp) | SE (pp) | MDES (pp) |
|-------|---------|---------|-----------|
| Gemma-2-9B | +0.55 | 0.621 | 1.74 |
| OLMo-2-7B | -1.07 | 0.567 | 1.59 |
| Phi-4 | -0.27 | 0.448 | **1.25** |
| Qwen2.5-14B | +0.69 | 0.733 | 2.05 |
| Qwen2.5-7B | -0.84 | 0.720 | **2.02** |

### ARC-Challenge (n_treated=257, n_untreated=915)

| Model | DiD (pp) | SE (pp) | MDES (pp) |
|-------|---------|---------|-----------|
| Gemma-2-9B | -0.25 | 1.663 | 4.66 |
| OLMo-2-7B | -1.13 | 1.494 | 4.19 |
| Phi-4 | -0.83 | 0.815 | 2.28 |
| Qwen2.5-14B | -0.26 | 1.240 | 3.47 |
| Qwen2.5-7B | +2.43 | 1.987 | 5.57 |

### 解读

- **MMLU**: MDES 1.25–2.05pp。所有 |DiD| < MDES，无法区分 true null 和 <2pp 的 item-specific 效应。但能排除 >2pp 的大效应（先行研究中 memorization 通常 >5pp）。
- **ARC**: MDES 更大（2.28–5.57pp），因 n_treated 仅 257，power 明显不足。
- 检测 0.5pp 效应需 ~33k–89k items per group（MMLU），实际不可行。
- **结论**: Power 确实有限，但 MDES 上界足以排除 memorization 级别的 item-specific 效应。这是 "absence of large effects" 而非 "absence of any effect"。

论文可用文字已生成在 JSON 的 `paper_text.limitations_or_appendix` 字段中。产出路径：`artifacts/did_power_analysis/did_power_analysis.json`

---
