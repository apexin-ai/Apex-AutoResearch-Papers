# D070+D071 Paper Revision Summary (Round 7)

## Files Modified
- docs/paper/sections/abstract.tex — SF-5: simplified to problem-finding-significance, removed ρ/AUROC numbers, bottleneck framing
- docs/paper/sections/introduction.tex — MF-2: 3 contributions (bottleneck/framework/complexity), no "first" claims
- docs/paper/sections/experiments.tex — SF-2: thinking confound with confirmed data, Minor-9: N=8 seed note
- docs/paper/sections/discussion.tex — D071: free-form ablation placeholder, SF-1/SF-6 fixes
- docs/paper/sections/conclusion.tex — D071: free-form ablation mention, bottleneck framing
- docs/paper/sections/method.tex — SF-7: VC ρ diff in footnote, Minor-3: FK significance test
- docs/paper/sections/related_work.tex — Minor-5: he2024uncertainty context
- docs/paper/sections/appendix.tex — MF-3: TOST δ* data, SF-4: cross-model heading, SF-2: thinking footnote

## Computation Artifacts Integrated
1. tost_breakpoint_delta_star.md — NER δ* ∈ [1.28, 3.38]pp, RE δ* ∈ [2.86, 6.53]pp
2. qwen3_thinking_confirmation.md — enable_thinking=True for SciERC, loss participation confirmed
3. vc_implementation_rho_diff.md — Eq.6 vs majority: NER Δρ=+0.127, RE Δρ=+0.019

## D071 Narrative Spine (verified across all sections)
1. Problem: TTS for structured IE under constrained decoding ✓
2. Conceptual: 4/5 instance-level by construction → noted, not discovered ✓
3. Core empirical: LP compression 60% tied ✓
4. Control: free-form ablation [PLANNED] ✓
5. Practical: non-tied +2.9pp + relaxed decoding ✓
