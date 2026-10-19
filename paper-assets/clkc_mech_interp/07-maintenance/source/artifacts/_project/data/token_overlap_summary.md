# Token Overlap Enhanced Analysis

## RC2 Conclusion: EXCLUDED

### Evidence
1. Per-sample Jaccard (3-4%) far below type-level (10-15%) - type-level inflates overlap
2. Qwen EN→ZH: r=0.059, p=0.45 (not significant)
3. Llama EN→ZH: r=-0.15, p=0.012; Spearman r=-0.21, p=0.0004 (significant NEGATIVE)
4. Tercile: Llama low-overlap group 71% acc vs high-overlap 47% acc (Δ=-24pp)

### Files
- Script: /root/clkc_mech_interp/src/token_overlap_enhanced.py
- Results JSON: /root/clkc_mech_interp/data/token_overlap_analysis.json
