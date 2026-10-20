# DebugBench VOTA + ae_only Formatted Data

## Files
- /root/autodl-tmp/trace-verdict-study-data/debugbench_vota_train.jsonl (1622 samples)
- /root/autodl-tmp/trace-verdict-study-data/debugbench_vota_test.jsonl (426 samples)
- /root/autodl-tmp/trace-verdict-study-data/debugbench_ae_only_train.jsonl (1622 samples)
- /root/autodl-tmp/trace-verdict-study-data/debugbench_ae_only_test.jsonl (426 samples)

## Token Length Stats (Qwen tokenizer, train split)

### VOTA
- Mean: 1465, Median: 2015
- P95: 2016, Max: 2016
- >2048: 0/1622 (0.0%)
- Truncated: 66.0% (trace truncated to fit 2048 budget)
- Empty trace: 30.5%

### ae_only
- Mean: 723, Median: 700
- P95: 1554, Max: 2016
- >2048: 0/1622 (0.0%)
- Truncated: 0.7%
- Empty trace: 31.5%

## Labels
- pass=1042 (50.9%), fail=1006 (49.1%)

## Format
{input, output, problem_id} — compatible with train_sft.py
