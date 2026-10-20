Error analysis on old model set (Qwen-0.5B, 1.5B, 3B, 7B, Llama-3.2-3B).
NOTE: NOT the current 5-family taxonomy. Methodology (error_analysis.py) is reusable.

Key findings (old models):
- Qwen-0.5B catastrophic: forgot 25.2% MMLU items at d100
- Persistent errors: MMLU 7.8%, HumanEval 43.9%, GSM8K 8.1%, ARC 2.0%
- Cross-model unanimous forgetting only 21 MMLU items — forgetting is model-specific
- Forgetting domain distribution proportional to domain size (no domain-specific vulnerability)

TODO: Re-run on 5-family data (Phi-4, Qwen-14B, Qwen-7B, Gemma-2, OLMo-2)