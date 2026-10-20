N-gram PPL Scoring Results (Line A Step A2)

Remote path: /root/autodl-tmp/provenance_weight_training/data/scored_data_ngram.jsonl
Script: /root/autodl-tmp/provenance_weight_training/scoring/score_ngram_ppl.py

Stats:
- Samples: 371,499
- Model: Trigram, add-k=0.01, trained on 164,889 real samples
- Real (depth=0): n=164,889, mean=1516.11, median=1135.11
- Synth (depth=1): n=206,387, mean=1506.49, median=473.32
- AUC: 0.7319 (lower PPL = synthetic)
- Spearman r with q_score: -0.3555 (complementary signal)
- Best threshold accuracy: 69.1% (threshold=720.20)