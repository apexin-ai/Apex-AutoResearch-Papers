# Internal Numerical Consistency Audit

**Date**: 2026-05-25
**Scope**: All tex files in `docs/paper/sections/` + `main.tex`

---

## 不一致发现

| 位置A | 数字A | 位置B | 数字B | 严重度 |
|-------|-------|-------|-------|--------|
| Table 1 (experiments.tex:37) & Analysis §5.1 (experiments.tex:75) | BT = .675 / 67.5% at n=355 (Qwen3 formality scaled) | Appendix K bootstrap (appendix.tex:328) | "same data yield BT = 66.5%" | critical |
| Table 1 (experiments.tex:37) & Analysis §5.1 (experiments.tex:75) | Likert d = −0.025 at n=355 | Appendix K bootstrap table (appendix.tex:346) | d = −0.017 at n=355 | critical |
| Table 1 caption (experiments.tex:26) | verbosity n=86 | Table 2 GEE footnote (appendix.tex:136) | "other rows: n=88" (applies to verbosity rows too) | critical |
| Table 1 caption (experiments.tex:26) | verbosity n=86 | Abstract (abstract.tex:7) | "Style OR 8–13 at n=88" (verbosity context) | warning |
| Table 1 caption (experiments.tex:26) | verbosity n=86 | Analysis §5.2 (experiments.tex:140) | "style-dominated at n=88: Style OR 8.2–13.1" (verbosity) | warning |
| Analysis §5.1 (experiments.tex:92) | "8/11 bias-positive cells" (8+3=11) | Cross-bench Table T has 6 BT-sig cells + 8 LLMBar BT-sig = 14 total | 11 ≠ 14; denominator unclear | warning |
| Conclusion (conclusion.tex:3) | "divergent pairwise/Likert verdicts in … 6/24 cross-benchmark cells" | Cross-bench Table T (appendix.tex:700-713) | Only 2/6 cross-bench cells are Blindspot (†); 4 are ‡ (both sig). "Divergent verdicts" overstates. | warning |
| Analysis §5.1 (experiments.tex:73) | Cohen's d = −0.04, p = 0.91 (GPT-4o formality) | Table 1 (experiments.tex:32) | d = −.041, p = .905 | info |
| Analysis §5.4 (experiments.tex:182) | Gwet's AC₁ = 0.96 | Appendix S (appendix.tex:665) | Gwet's AC₁ = 0.958 | info |

### 详细说明

**[Critical-1] BT at n=355: 67.5% vs 66.5%**
- Table 1 row "Qwen3 Form.^b" shows .675, and Analysis §5.1 writes "BT remains stable at 67.5%."
- Appendix K (Bootstrap Attenuation) writes "The same data yield BT = 66.5%."
- One of these values is wrong. Most likely the appendix should read 67.5% to match Table 1.

**[Critical-2] Likert d at n=355: −0.025 vs −0.017**
- Table 1 and Analysis §5.1 both report d = −0.025 for the n=355 scaled replication.
- Appendix K bootstrap table row n=355 shows d = −0.017.
- These should be the same value at full sample size. The bootstrap table may have been generated from a different code path or an earlier data version.

**[Critical-3] Table 2 GEE footnote claims all non-scaled rows are n=88**
- Table 1 explicitly distinguishes n=88 (formality) vs n=86 (verbosity).
- Table 2 footnote "$^a$ n=355; other rows: n=88" is incorrect for the four verbosity rows, which should be n=86.

**[Warning-1] Abstract/Analysis say n=88 for verbosity Style OR range**
- The abstract writes "Style OR 8–13 at n=88" in the verbosity context, and Analysis §5.2 says "style-dominated at n=88" for verbosity.
- The correct verbosity sample size is n=86 (Table 1 caption).

**[Warning-2] "8/11 bias-positive cells" count**
- The text says 8 Blindspot + 3 exceptions (‡) = 11 bias-positive cells.
- But LLMBar has 8 BT-significant primary cells (all Blindspot), and cross-benchmark has 6 BT-significant cells (2† + 4‡), totaling 14 bias-positive cells, not 11.
- If register/exploratory cells are excluded, the count might work under some interpretation, but this is not stated.

**[Warning-3] Conclusion "6/24 cross-benchmark cells" framing**
- The conclusion groups "6/24 cross-benchmark cells" under "divergent pairwise/Likert verdicts," implying all 6 are Blindspot.
- In reality, 4/6 are ‡ (both BT and Likert significant), meaning Likert also detects those effects. Only 2/6 show the Blindspot pattern.
- Suggested fix: "6/24 cross-benchmark cells tested, of which 2 replicate the Blindspot and 4 show both-significant patterns (‡)."

---

## 占位符

未发现任何占位符。以下模式在所有 tex 文件中均无匹配：
- `XX.X`, `X.XX`, `XX%`, `TBD`, `???`, `PLACEHOLDER`, `TODO`, `FIXME`, `\textcolor{red}`, `\todo`

---

## 图表标签问题

| 问题 | 严重度 |
|------|--------|
| Figure 1 (`fig:pipeline`) 定义于 introduction.tex:32 但全文无 `\ref{fig:pipeline}` 引用 | info |
| Figure 1 标注 "Numbers indicate sample attrition at each stage" — 无法验证图中数字是否与 n=100→n=88/86 一致（需查看 PDF） | info |
| 所有 `\ref{}` 均有对应 `\label{}` 定义，无 undefined reference | — |
| Figure 2 (DAG) 变量 S, Q, Y, R, P 与 method.tex 定义一致 | — |

---

## 已验证一致

以下关键数字组已在多处交叉验证，确认一致：

1. **BT win probabilities (LLMBar, n=88/86)**:
   - GPT-4o Form .630, Verb .760; Qwen3 Form .665, Verb .773; Llama-70B Form .695, Verb .735; Gemini Form .574, Verb .708; Claude Form .562, Verb .541
   - Abstract, Introduction, Table 1, Analysis §5.1/§5.3, Appendix NLI ablation, Appendix BT CI 表 — 全部一致

2. **Style OR 范围 (verbosity, n=88/86)**:
   - Table 2: 13.10, 11.34, 8.21, 8.98 → "8–13" / "8.2–13.1"
   - Abstract, Introduction, Analysis §5.2/§5.3 — 一致

3. **Orig OR 范围 (verbosity)**:
   - Table 2: 0.49, 0.45, 0.38, 0.46 → "0.38–0.49"
   - Analysis §5.2/§5.3 — 一致

4. **Non-tie concordance**:
   - 76.6%, 154/201, p < .001, CI [70.3%, 81.9%]
   - Abstract, Analysis §5.1, Appendix W — 一致

5. **Formality direction asymmetry (GPT-4o, all data)**:
   - formal-origin 78.8% vs casual-origin 54.5%, GEE Style OR = 2.58, p = .002
   - Table 1 footnote, Appendix B — 一致
   - (Note: 88.9%/52.6% in experiments.tex:13 is from consistency-filtered BT stratification, a different subset — correctly distinguished)

6. **Power analysis**:
   - 4–206× range, 336–27,159 pairs
   - Analysis §5.1, Appendix L power table — 一致

7. **Efficiency gap**: 3–4× — Abstract, Analysis §5.2, Conclusion — 一致

8. **GEE shrinkage at n=330/355**:
   - Formality: Qwen3 OR 4.20→2.15 (−49%), Orig OR 4.70→4.99
   - Verbosity: 51–72% shrinkage, Style OR 2.5–4.0
   - Analysis §5.2, Appendix verb_n355 — 一致

9. **Rewriter independence**: 22% Style OR reduction (13.10→10.17)
   - Table 1 footnote, Analysis §5.3, Appendix D — 一致

10. **Gate pass precision**: 98.6% (69/70)
    - Analysis §5.4, Appendix S — 一致

11. **Bootstrap parameters**: 10,000 resamples, seed 42, L2 α=10⁻⁶
    - Experiments §3, Appendix implementation — 一致

12. **NLI threshold**: τ = 0.90; temperature 0.7
    - Method §2.1/§2.2, Appendix implementation — 一致

13. **Likert p-values (LLMBar)**: .905, .461, .395, .534, .284, .403, .309, .370
    - Introduction, Table 1, Analysis §5.3 — 一致

14. **Cross-benchmark BT (Appendix T)**: 6 cells all BT-significant, values match BT CI table

15. **Claude TOST**: BT 56.2%/54.1%, pooled 55.17%
    - Table 1, Appendix G — 一致

16. **All \ref/\label pairs**: 完全匹配，无 undefined reference
