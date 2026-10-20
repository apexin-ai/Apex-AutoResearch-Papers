Experiment: D051 Batch 2 — 25+ Count Curve Batches + 3-Seed Variance

Status: RUNNING on cqa1-38874 (tmux session: d051_batch2)
Started: 2026-05-17 03:03 CST

Scripts:
- /root/schema-dag-extraction/scripts/run_d051_count_curves_25.py
- /root/schema-dag-extraction/run_d051_batch2.sh

Execution order:
1. Part A: RE count curves - 25 batches, seed=42, counts=[4,8,16,32,40,64,80]
2. Part A: NER count curves - 25 batches, seed=42, counts=[2,6,12,22,44,66]
3. Part B: RE seeds 123, 456 - full count levels
4. Part B: NER seeds 123, 456 - key levels [6,12,22]

Output directories:
- artifacts/d051_fewrel_n25_s42/
- artifacts/d051_fewnerd_n25_s42/
- artifacts/d051_fewrel_n25_s123/
- artifacts/d051_fewrel_n25_s456/
- artifacts/d051_fewnerd_n25_s123/
- artifacts/d051_fewnerd_n25_s456/

Model: Qwen3-32B-FP8 (/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/)
GPU: NVIDIA RTX PRO 6000 Blackwell (98GB)
Estimated runtime: 8-12 hours

Log: artifacts/d051_batch2.log
Monitor: tail -f artifacts/d051_batch2.log | grep "Saved\|Done\|Error"