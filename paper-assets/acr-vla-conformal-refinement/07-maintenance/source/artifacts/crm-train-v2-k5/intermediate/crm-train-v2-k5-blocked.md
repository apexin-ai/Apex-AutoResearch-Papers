blocked: K=10 cache incompatible with K=5 training.

Root cause: train_crm.py uses manifest["K"] (=10) for CGS initialization, ignores args.K during training phase. k_samples tensor shape (N, 10, H, D) is not sliced when --K 5 is passed. Result: --K 5 silently trains with K=10 data.

Fix needed: Add k_samples slicing (k_samples[:, :args.K]) and use args.K for CGS init when args.K < manifest_K.