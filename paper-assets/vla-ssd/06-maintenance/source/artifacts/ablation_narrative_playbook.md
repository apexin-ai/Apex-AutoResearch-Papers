# L1 Head Ablation — Narrative Playbook (Updated)

> Updated after ablate_all32 classification = 1.0 for all conditions.
> Classification is not sensitive to L1 attention ablation. Action probe R² pending.

## Known facts (confirmed)
- All classification conditions (baseline, all-24, top-5, control-8, all-32) = 1.0 at all layers
- Diagnostic confirmed: monkey-patch works (attention → 0.000, hidden state cosine sim = 0.973)
- L0 probe = 10% (chance): instruction identity linearly inseparable at L0
- L1 MLP transforms L0 residual into decodable form (regardless of L1 attention)
- Threshold sensitivity: three-condition gradient robust across 30%-70%

## Scenario B1: R² DROPS under ablation (most interesting — novel dissociation)

### Narrative
"L1 attention heads are not necessary for instruction identity classification (trivially maintained via residual stream), but contribute to fine-grained action-relevant information integration. This dissociation reveals that the observed attention redistribution carries functional significance beyond coarse instruction routing."

### Changes:
1. **§4.3 new paragraph** "Attention ablation reveals functional dissociation":
   - Classification 1.0 for all conditions including all-32 → instruction identity via residual stream
   - BUT R² drops: baseline X vs ablate_all32 Y (Δ = Z, p < W)
   - "The 25/32 instruction-dominant head pattern contributes to action-relevant information integration beyond instruction identity"
   - Small ablation table (3 conditions × classification + R² at L1)
2. **Abstract**: no change to C2 wording (already observational)
3. **Discussion**: "Attention ablation reveals a dissociation: instruction identity is trivially maintained via the residual stream, but action-relevant information integration relies partially on the attention-mediated pathway. This suggests that the observed routing reorganization serves fine-grained multimodal integration rather than coarse instruction identification."
4. **Discussion pruning implication**: soften — "pruning instruction-dominant heads may preserve instruction identification but degrade action prediction quality"

### Red lines:
- Never claim attention is "necessary for routing" — classification says otherwise
- The dissociation IS the finding; don't oversell either direction

## Scenario B2: R² UNCHANGED under ablation (attention is training correlate)

### Narrative
"L1 attention redistribution is a robust training signature (absent in pretrained and untrained models) but is not causally necessary for either instruction classification or action prediction. Instruction information enters the readout position via L0 attention and is transformed by L1 feed-forward layers."

### Changes:
1. **§4.3 new paragraph** "Attention ablation reveals mechanistic redundancy":
   - Classification 1.0, R² unchanged for all conditions
   - "The 25/32 pattern is a robust training signature but not a functional bottleneck"
   - Cite Reviewer's analogy: "indicator, not mechanism" (rephrase for paper)
2. **Abstract/Intro/Conclusion**: NO CHANGES (already observational)
3. **Discussion**: add nuance — "The entry-exit attention pattern is robust to threshold choice (Appendix) but is not causally necessary for either instruction decodability or action prediction quality, cautioning against interpreting attention patterns as causal indicators of information flow."
4. **Discussion pruning**: downgrade — "the lack of causal necessity suggests that the entry-exit pattern reflects optimization dynamics rather than an indispensable routing mechanism"
5. **Appendix**: ablation table (5 conditions × 4 layers × 2 metrics)

### Framing:
- "Training signature, not causal mechanism"
- "Indicator of training-induced reorganization"
- "L0 attention + L1 MLP pathway sufficient"

## Both scenarios:
- Always report ALL data (classification + R² + diagnostic)
- Ablation table in main text (small) or appendix depending on space
- Never suppress negative results — transparency builds trust
- The L0→L1 MLP mechanism insight is novel regardless of R² outcome
