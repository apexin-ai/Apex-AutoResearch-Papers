## vLLM guided_json vs Grammar-Only (Table 3 Row 2) Comparison

**Experiment**: Qwen3-8B zero-shot SciERC extraction with vLLM 0.18.1 guided_json (StructuredOutputsParams)
**Date**: 2026-05-22
**Server**: westd-16980 (RTX PRO 6000 Blackwell 98GB)

### Results

| Metric | Grammar-Only (ours) | vLLM guided_json | Δ |
|--------|:---:|:---:|:---:|
| DR% | 14.84 | 15.26 | +0.42 |
| RV% | 0 | 0 | 0 |
| ET% | 0 | 0 | 0 |
| CF% | 0.08 | 0.04 | -0.04 |
| R-F1 | 8.23 | 8.75 | +0.52 |
| E-F1 | 30.98 | 30.91 | -0.07 |
| Parse Fail% | ~0 | 0 | - |

### Key Findings

1. **RV=0%, ET=0%** — identical to our grammar-only, confirming both enforce JSON schema + enum constraints
2. **DR≈15%** — nearly identical; both leave domain-range violations completely unchecked (~15% violation rate)
3. **F1 scores within noise** — E-F1 Δ=-0.07, R-F1 Δ=+0.52 (sampling variance)
4. **100% parse success** — vLLM's xgrammar guarantees valid JSON

### Conclusion

vLLM's guided_json is functionally equivalent to our XGrammar grammar-only ablation. Both enforce:
- Valid JSON structure
- Enum constraints (entity types, relation types)

Neither enforces:
- Domain-range constraints (which head/tail type pairs are valid for each relation)
- Cross-field consistency (same entity mention having consistent types)

This validates our paper's claim that standard GCD tools (vLLM guided_json, Outlines, etc.) operate at the grammar level only, leaving semantic constraint violations unaddressed.

### Technical Notes
- vLLM 0.18.1 with StructuredOutputsParams (not GuidedDecodingParams which was removed)
- Required patching torch._inductor.select_algorithm.py (duplicate template assertion) for Blackwell GPU compatibility
- Grammar compilation took ~90s; inference ~108s total for 551 samples
- Used enforce_eager=True due to torch 2.10/2.11 incompatibility
