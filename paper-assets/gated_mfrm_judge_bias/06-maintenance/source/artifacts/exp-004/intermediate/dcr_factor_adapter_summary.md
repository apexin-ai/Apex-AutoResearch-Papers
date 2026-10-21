DCR Factor Baseline Adapter - Summary

Files:
- /root/gated_mfrm_judge_bias/baselines/dcr_adapter.py — unified baseline interface
- /root/gated_mfrm_judge_bias/baselines/dcr_baseline.py — core DCR logic

4-layer contamination scores:
- s1 (Semantic): Score Elevation
- s2 (Information): Easy-Item Advantage  
- s3 (Data): Perfect-Score Rate
- s4 (Label): Judge Unanimity

Key finding: s2 inflated for pairwise data (0.69-0.77) due to inherent win-rate/difficulty correlation.
This is a DCR limitation useful for paper argumentation.

Integration: run_all_baselines_on_exp001() provides unified interface for exp-004.
Tests: 11/11 passed.