EXP-2: plan001-exec-only-s43-r4 — greedy (T=0) vs sampling (T=0.7) eval
========================================================================
Checkpoint: /root/autodl-tmp/outputs/plan001_exec_only_s43_r4/checkpoint-500
            (DELETED after eval; greedy JSON dated May 14 11:45, sampling JSON May 14 12:13)
Eval data:  data/proofwriter_fol_100.jsonl  (100 held-out problems)
Decoding:   eval_sta.py defaults to do_sample=False (greedy). Sampling run used --do_sample at T=0.7.

GREEDY (T=0, do_sample=False) — outputs/eval_sta_plan001_exec_only_s43_r4.json
  PR              0.130   (13/100)
  mean ISR        0.0000
  ISR* (proved)   0.0000
  By answer PR    true=0.118, false=0.200, unknown=0.098
  n_premises (proved 13)  mean=17.92  median=16  range=14..30
  mean components (proved)  18.92
  H7 strict          0/13 = 0.0%
  H1 strict          13/13 = 100.0%
  Non-hacking        0/13 = 0.0%

SAMPLING (T=0.7, do_sample=True) — outputs/eval_sta_plan001_s43_r4_do_sample.json
  PR              0.140   (14/100)
  mean ISR        0.0000
  ISR* (proved)   0.0000
  By answer PR    true=0.176, false=0.080, unknown=0.146
  n_premises (proved 14)  mean=17.50  median=16.5  range=12..30
  mean components (proved)  18.50
  H7 strict          0/14 = 0.0%
  H1 strict          14/14 = 100.0%
  Non-hacking        0/14 = 0.0%

Conclusion
  Greedy and T=0.7 sampling agree to within 1 percentage point on PR (Δ=-0.01) and are
  identical on ISR* (both 0.0), H1 rate (both 100%), and mean component count
  (~18.5-18.9). s43 is a decoding-invariant collapse: ~85% of inputs hit max_new_tokens
  producing long repeated-clause outputs; the ~15% that do parse embed the conclusion
  verbatim among 14-30 ground-fact premises so per-clause ablation never reduces
  n_necessary below baseline (ISR=0). The cross-seed gap vs s42 (eval PR=0.93) is real,
  not a sampling artifact.