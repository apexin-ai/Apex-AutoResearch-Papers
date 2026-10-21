# D157 Shuffled-ISR: Eval & Analysis Commands

## Config

- Model: Qwen3-4B, 500 steps, reward_mode=shuffled_isr, β=0.1
- Seeds: s42, s43, s44
- Test data: `data/proofwriter_fol_100.jsonl` (C008)

## 1. Eval Commands (eval_sta.py)

```bash
# s42
export CUDA_VISIBLE_DEVICES=0
python scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path /root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/eval_sta_results.json

# s43
export CUDA_VISIBLE_DEVICES=0
python scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/d157_shuffled_isr_s43_r3/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path /root/autodl-tmp/outputs/d157_shuffled_isr_s43_r3/eval_sta_results.json

# s44
export CUDA_VISIBLE_DEVICES=0
python scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/d157_shuffled_isr_s44_r3/checkpoint-500 \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path /root/autodl-tmp/outputs/d157_shuffled_isr_s44_r3/eval_sta_results.json
```

## 2. Classify Commands (classify_h7.py)

```bash
# s42
python scripts/classify_h7.py \
  --eval_path /root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/eval_sta_results.json \
  --json_out /root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/classify_h7_results.json

# s43
python scripts/classify_h7.py \
  --eval_path /root/autodl-tmp/outputs/d157_shuffled_isr_s43_r3/eval_sta_results.json \
  --json_out /root/autodl-tmp/outputs/d157_shuffled_isr_s43_r3/classify_h7_results.json

# s44
python scripts/classify_h7.py \
  --eval_path /root/autodl-tmp/outputs/d157_shuffled_isr_s44_r3/eval_sta_results.json \
  --json_out /root/autodl-tmp/outputs/d157_shuffled_isr_s44_r3/classify_h7_results.json
```

## 3. Analysis Script

```bash
python scripts/analyze_d157.py \
  --inputs \
    /root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/classify_h7_results.json \
    /root/autodl-tmp/outputs/d157_shuffled_isr_s43_r3/classify_h7_results.json \
    /root/autodl-tmp/outputs/d157_shuffled_isr_s44_r3/classify_h7_results.json \
  --seed_labels s42 s43 s44 \
  --output artifacts/d157_shuffled_isr_analysis.md
```

Path: `scripts/analyze_d157.py`

## 4. Baseline Data (from registry)

### ISR β=0.1 (d134-4b-isr-b01, 5 seeds)

| Seed | PR | Proved | TS(H7) | CE(H1) | PG(H8) | CI | Genuine | Genuine% |
|------|------|--------|--------|--------|--------|-----|---------|----------|
| s47  | 0.97 | 97     | 83     | 1      | 10     | 8   | 3       | 3.1%     |
| s48  | 0.66 | 66     | 66     | 0      | 0      | 0   | 0       | 0.0%     |
| s49  | 0.86 | 86     | 73     | 6      | 6      | 0   | 1       | 1.2%     |
| s50  | 0.98 | 98     | 84     | 0      | 0      | 0   | 6       | 6.1%     |
| s51  | 0.98 | 98     | 96     | 0      | 1      | 0   | 1       | 1.0%     |
| **Mean** | **0.89** | — | — | — | — | — | — | **2.3%** |

### Random β=0.1 (d134-4b-random-b01, 5 seeds)

| Seed | PR | Proved | TS(H7) | CE(H1) | PG(H8) | CI | Genuine | Genuine% |
|------|------|--------|--------|--------|--------|-----|---------|----------|
| s47  | 0.89 | 89     | 0      | 79     | 4      | 0   | 6       | 6.7%     |
| s48  | 0.93 | 93     | 3      | 75     | 14     | 0   | 4       | 4.3%     |
| s49  | 0.05 | 5      | 1      | 4      | 0      | 0   | 0       | 0.0%     |
| s50  | 0.45 | 45     | 4      | 39     | 0      | 0   | 2       | 4.4%     |
| s51  | 0.65 | 65     | 1      | 36     | 19     | 0   | 9       | 13.9%   |
| **Mean** | **0.59** | — | — | — | — | — | — | **5.9%** |

### Exec-only (plan001/sweep, 3 seeds)

| Seed | PR | Proved | TS(H7) | CE(H1) | PG(H8) | CI | Genuine | Genuine% |
|------|------|--------|--------|--------|--------|-----|---------|----------|
| s42  | 0.93 | 93     | 0      | 81     | 6      | 0   | 7       | 7.5%     |
| s45  | 0.99 | 99     | 93     | 5      | 1      | 0   | 1       | 1.0%     |
| s46  | 0.93 | 93     | 0      | 83     | 4      | 0   | 9       | 9.7%     |
| **Mean** | **0.95** | — | — | — | — | — | — | **6.1%** |

## 5. Notes

- s42 training in progress (checkpoint-300 as of 2026-05-20). s43/s44 not yet started.
- D157 output dirs for s43/s44 will be created when training launches.
- All eval must use `--data_path data/proofwriter_fol_100.jsonl` per C008.
- Set `CUDA_VISIBLE_DEVICES` before eval per C005.
- ISR β=0.1 baselines use seeds s47-s51 (no s42/s43/s44 available for this condition).
