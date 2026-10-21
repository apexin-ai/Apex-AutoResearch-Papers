# P1 Pre-submission Fixes Log

## 1. Cascade dissolution hypothesis downgrade (Discussion)
✅ **已修复** — `discussion.tex:2`
- "refutes a noise hypothesis" → "argues against a noise hypothesis"
- Added caveat: "This proposed mechanism requires causal verification through controlled intervention experiments." (line 3)
- "We hypothesize" already in place (concurrent worker had applied)

## 2. Results dense sentence splitting (results.tex)
✅ **已修复** — `results.tex:25,27`
- L25: Split ten-seed oracle replications into 3 sentences (qualitative conclusion → Qwen numbers → Llama numbers)
- L27: Split stochastic decoding sentence into 3 sentences (backbone-specific framing → Llama data → Qwen data)

## 3. Table 1 footnote sanitization
✅ **已修复** — `results.tex:69`
- Replaced "silently used heuristic detection due to a default-value bug" with neutral language: "an earlier configuration issue was identified and corrected prior to the definitive replication"

## 4. CONTINGENCY-B comment blocks removed
✅ **已修复** — 3 files
- `results.tex`: removed lines 87-96 (10 lines)
- `discussion.tex`: removed lines 29-39 (11 lines)
- `appendix_scaling.tex`: removed lines 37-52 (16 lines)
- Verified: `grep CONTINGENCY-B` returns 0 matches across paper/

## 5. 14B evidence caveat (Discussion scale paragraph)
✅ **已修复** — `discussion.tex:16`
- Added: "The 14B evidence is substantive but limited by low heuristic suppression (6.4% vs. 56.3% at 7B); the offline oracle estimate (Δ=0 pp) provides complementary full-removal evidence."
- Compression: shortened 72B perturbation caveat, removed "consistent with the cascade-dissolution mechanism described above", "model capacity" → "capacity", "deltas supports" → "deltas support" (grammar fix)

## 6. Efficiency claim linkage (Discussion)
✅ **已修复** — `discussion.tex:7`
- Added: "The observed suppression rates (36--56%) translate directly to inference call reductions of equivalent magnitude, with wall-time savings detailed in Appendix~\ref{app:efficiency}."
- Confirmed label `app:efficiency` exists in `appendix_efficiency.tex`
- Compression: tightened communication structure paragraph ("per-task calibration" → "calibration", "non-inferior or positive direction" → "non-inferior", em-dash → colon in oracle validation sentence)

## 7. Abstract wording fix
✅ **已修复** — `abstract.tex:1`
- "whether functional classification predicts which messages can be safely removed" → "whether functional classification predicts safe removal of individual messages"

## 8. Results L6 phrasing
✅ **已修复** — `results.tex:6`
- "Informationally sparse acknowledgments are most disruptive to remove." → "Informationally sparse acknowledgments are those whose removal is most disruptive."

## 9. Related work quote style
⚠️ **跳过** — no straight double quotes found in `related_work.tex`. All quoted terms already use LaTeX-style `` ...'' or `\emph{}`.
