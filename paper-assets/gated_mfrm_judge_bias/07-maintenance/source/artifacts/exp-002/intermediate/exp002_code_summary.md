exp-002 code framework at /root/gated_mfrm_judge_bias/exp002/

Files:
- run_exp002.py (main CLI)
- sources/performance_gap.py (Source 1: original vs rephrased gap + spline)
- sources/temporal_signal.py (Source 2: pre/post cutoff)
- sources/logprober.py (Source 3: Min-K% memorization)
- composite.py (weighted combiner + tuning)
- validation.py (ConStat delta correlation)
- mock_data.py (test data generator)

Dry-run: 30 items, 4 models, 2 judges → composite e_i mean=0.483, ConStat ρ=1.000