# fix unified id fix patch

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_unified-id-fix-patch_20260522T222457_result.json`
- **Structured JSON:** [`fb870b0c718ebed0d030.json`](../../sessions/fb/fb870b0c718ebed0d030.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clear. No residual old values remain. Here's the complete report:

## 修改汇总

| # | 文件:行 | 旧值 | 新值 | 类别 |
|---|---------|------|------|------|
| 1 | appendix.tex:875 | SC only & 39.17% | SC only & 39.33% | D |
| 2 | appendix.tex:892 | SC $= 39.17\%$ | SC $= 39.33\%$ | D |
| 3 | appendix.tex:898 | $+$1.17 | $+$0.83 | E |
| 4 | appendix.tex:899 | $+$7.00 | $+$6.67 | E |
| 5 | appendix.tex:900 | $+$11.17 | $+$11.00 | E |
| 6 | appendix.tex:948 | SC 39.17% | SC 39.33% | D |
| 7 | appendix.tex:948 | adj. p = 3.00×10⁻⁵ | adj. p = 6.78×10⁻⁵ | BH |
| 8 | appendix.tex:948 | adj. p = 7.44×10⁻⁶ | adj. p = 7.42×10⁻⁶ | BH |
| 9 | appendix.tex:965 | SC 39.17%, gap +15.83 | SC 39.33%, gap +15.67 | D/E |
| 10 | appendix.tex:966 | 40.33 & +1.17 & .189 & .630 | 40.17 & +0.83 & .359 & .720 | E/BH |
| 11 | appendix.tex:967 | 46.17 & +7.00 & 5.0×10⁻⁶ & 3.00×10⁻⁵ | 46.00 & +6.67 & 1.13×10⁻⁵ & 6.78×10⁻⁵ | E/BH |
| 12 | appendix.tex:968 | +11.17 & 6.2×10⁻⁷ & 7.44×10⁻⁶ | +11.00 & 6.18×10⁻⁷ & 7.42×10⁻⁶ | E/BH |
| 13 | appendix.tex:983 | .630 (Qwen3 w5 p_BH) | .720 | BH cascade |
| 14 | appendix.tex:1001 | SC 39.17% | SC 39.33% | D |
| 15 | appendix.tex:1002 | +3.17 | +3.00 | FT |
| 16 | appendix.tex:1003 | +13.00 | +12.83 | FT |
| 17 | appendix.tex:1004 | +26.33 | +26.17 | FT |
| 18 | solutions.tex:9 | SC's 39.17%, +7.00 pp | SC's 39.33%, +6.67 pp | D/E-narr |
| 19 | solutions.tex:12 | SC 39.17%, +7.00 pp | SC 39.33%, +6.67 pp | D/E-narr |
| 20 | solutions.tex:23 | 39.17% & +15.83 & +7.00 pp | 39.33% & +15.67 & +6.67 pp | D/E |
| 21 | solutions.tex:32 | +13.00 pp | +12.83 pp | FT |
| 22 | abstract.tex:8 | +7.00 pp | +6.67 pp | E-narr |
| 23 | introduction.tex:28 | +7.00 pp | +6.67 pp | E-narr |
| 24 | scatter.py:35 | (15.83, 7.00) | (15.67, 6.67) | G |
| 25 | scatter.py:43 | (-1.50, 4.17) | (-1.66, 4.17) | G |
| 26 | scatter.py:44 | (7.00, 5.17) | (6.84, 5.17) | G |
| 27 | scatter.py:50 | (60.50, 13.00) | (60.34, 12.83) | G |
| 28 | scatter.py:134 | (15.83, 7.00) | (15.67, 6.67) | G |

### Canonical 数据读取结果

| Verifier | w | Combo % | Δ (pp) | p_raw | p_BH (m=12) |
|----------|---|---------|--------|-------|-------------|
| **SC baseline** | — | **39.33** (236/600) | — | — | — |
| DeBERTa w1 | 1 | 40.17 | +0.83 | 0.359 | .720 |
| DeBERTa w3 | 3 | 46.00 | +6.67 | 1.13×10⁻⁵ | 6.78×10⁻⁵*** |
| DeBERTa w5 | 5 | 50.33 | +11.00 | 6.18×10⁻⁷ | 7.42×10⁻⁶*** |
| RoBERTa w1 | 1 | 39.17 | −0.17 | 1.0 | 1.0 |
| RoBERTa w3 | 3 | 43.50 | +4.17 | 0.00263 | .755 |
| RoBERTa w5 | 5 | 43.67 | +4.33 | 0.0369 | .720 |
| BART w1 | 1 | 39.33 | 0.00 | 1.0 | 1.0 |
| BART w3 | 3 | 44.50 | +5.17 | 0.000244 | .755 |
| BART w5 | 5 | 45.67 | +6.33 | 0.00275 | .720 |

FT DeBERTa (Mistral-7B): w1=42.33 (Δ+3.00), w3=52.17 (Δ+12.83), w5=65.50 (Δ+26.17)

### BH 重算过程 (m=12 cross-generator)

12 条件排序后 step-up + step-down monotonicity 修正。Mistral w1 从 rank 3→4 (raw .189→.359)，导致 Qwen3 w5 BH 也从 .630→.720（rank cascade）。两个显著条件不变（Mistral w3/w5, p_BH < 0.001）。

### 编译状态
**成功**，27 页，652,500 bytes，0 errors。

### 残留检查
- `39.17` in *.tex: **0 matches**
- `+7.00` in *.tex: **0 matches**
- `15.83` in *.tex: **0 matches**
- `39.17` in *.py: **0 matches**
- `7.00` in scatter plot: **0 matches**

### 未修改项（确认不需要变化）
- RoBERTa/BART Δ 在 multi-NLI 表 (L902-908): canonical 值与当前显示值一致
- `$+$13--26\,pp` (abstract/intro): 12.83→13, 26.17→26 四舍五入后范围不变
- `$14\times$ amplification` (solutions L32): LLaMA 的 $+0.83→+11.67$，不受影响
- DRC τ=0.7 accuracy (L876): 无更新后的 Mistral-7B/PW-D5 DRC 数据，45.33% 保留
- DRC full combo (L877): 46.00% 与 canonical DeBERTa w3 一致
- 3-verifier BH 表 (L928-933): 只显示 checkmarks，显著性结论不变

---
