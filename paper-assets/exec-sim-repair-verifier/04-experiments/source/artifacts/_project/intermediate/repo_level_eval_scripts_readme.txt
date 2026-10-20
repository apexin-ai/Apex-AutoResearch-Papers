Scripts on home-1x5090:/home/sonny/exec-sim-repair-verifier/

1. eval_repo_cls.py - CLS verifier inference (max_seq_length=4096, max_new_tokens=8, batch_size=16)
2. eval_repo_cwm.py - CWM execution simulator inference (max_seq_length=4096, max_new_tokens=64, batch_size=8)
3. paired_bootstrap_repo.py - Clustered paired bootstrap by problem_id (10000 resamples, TOST ±2pp, D008 Go/No-Go)

Test set: 9784 instances (pass=7138, fail=2646)
Output: predictions JSONL {index, problem_id, label, pred, correct, truncated, gen_text}

Usage:
  python eval_repo_cls.py --checkpoint_dir <ckpt> --device cuda:X
  python eval_repo_cwm.py --checkpoint_dir <ckpt> --device cuda:X
  python paired_bootstrap_repo.py --cls_preds <cls.jsonl> --cwm_preds <cwm.jsonl>