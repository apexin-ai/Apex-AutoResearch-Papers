# analysis c9 gsm8k power analysis

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c9_gsm8k_power_analysis_20260516T024927_result.json`
- **Structured JSON:** [`4da1af8bc7afd3356e8c.json`](../../sessions/4d/4da1af8bc7afd3356e8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

### Within-condition 检验力（median ≠ 0）
| 条件 | 回溯 Power | MDES |
|------|-----------|------|
| QW Random s025 high | 1.00 | 0.242 |
| QW Random s025 low | 1.00 | 0.667 |
| QW Random s030 high | 1.00 | 0.836 |
| QW Random s030 low | 1.00 | 2.351 |
| DS Imp s025 | 0.99 | 1.349 |
| DS Imp s030 | **0.59** | 6.029 ← 欠功效 |

### Random vs Importance 对比
| 对比 | 观测差 | MDES | Power | 可检测? |
|------|--------|------|-------|---------|
| s025 random_low vs imp | +0.359 | 0.943 | 0.19 | NO |
| s030 random_low vs imp | +3.108 | 3.325 | 0.74 | NO (差一点) |
| s025 random_high vs imp | −0.382 | 0.343 | 0.88 | **YES** |
| s030 random_high vs imp | +0.218 | 1.183 | 0.07 | NO |

### Required n
CI 宽度缩小 50% → n=200；缩小到 33% → n=460。

### 建议
1. **Within-condition 效应充分有 power**（除 ds_imp_s030），n=50 足够检测 II gradient ≠ 0
2. **Between-condition 对比 3/4 欠功效**——random vs importance 差异太小，n=50 无法区分
3. **EMNLP deadline 9 天**，扩大 n 不现实。论文中报告 MDES + CI 并明确说明检验力限制即可
4. s030 random_low vs imp (diff=3.108, power=0.74) 接近显著，如果只扩展一个条件到 n≈80 可能达到 power=0.80

---
