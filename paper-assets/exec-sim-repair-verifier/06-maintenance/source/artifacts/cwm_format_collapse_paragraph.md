# CWM Format Collapse — Draft Paragraph

## Context
Insert into §5.5 Analysis, expanding the "Why does generation degrade at repo level?" paragraph (currently line 174 of experiments.tex). The existing paragraph states format collapse occurs but does not explain the mechanism; this text supplies the causal diagnosis. Alternative placement: after the "Default assignment artifact" paragraph in §5.4 (line 160).

## Draft (English)

Manual inspection of \cwm{} repo-level outputs reveals the format collapse mechanism: given long repository contexts, the model faithfully generates pytest execution trace fragments (progress indicators such as \texttt{[1\%], [3\%], \ldots}) but exhausts its generation budget before reaching a PASS/FAIL verdict (\tbd{}\% of \tbd{} samples unparseable; mean generation length \tbd{} tokens). This budget-exhaustion failure, not reasoning-mode interference ($<$\tbd{}\% of outputs contain thinking tokens), is the primary cause of \cwm{} accuracy falling below the majority baseline at repo level.

## Notes
- Four \tbd{} placeholders, pending multi-seed confirmation:
  - unparseable rate: single-seed s42 value is 63.7% (6236/9784), but paper already reports 51–74% range across configs
  - sample count: 9784 for single seed
  - mean gen length: 149.8 tokens (median 125) from s42. Note: main text §5.3 reports "mean ~477 tokens" — the 477 figure is from the inference benchmark (100-sample throughput test, Appendix ¶(i)); 149.8 is from the full s42 eval (9784 samples). Use 149.8 for this paragraph since it covers the full eval set; reconcile or footnote the discrepancy if both appear in nearby text.
  - thinking-token rate: 0.3% (30/9784) from s42
- If multi-seed data confirms s42 numbers, replace \tbd{} with exact values
- The "progress indicators" detail is new evidence not in the current draft; may want a brief appendix example (e.g., one truncated output sample)
