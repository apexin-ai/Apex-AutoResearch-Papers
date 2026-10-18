# debug pi05 random k09 bug

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_pi05-random-k09-bug_20260521T172606_result.json`
- **Structured JSON:** [`439367ca569e0d2fbf93.json`](../../sessions/43/439367ca569e0d2fbf93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I've completed a thorough investigation. Let me compile the diagnosis report.

---

## Diagnosis Report: π0.5 random k=0.9 = 12.0% SR

### 1. Code Analysis — No `1-k` Bug Found

Both pruning functions use identical `n_keep` computation:

```python
# Line 57 (random)
n_keep = max(1, int(n_tokens * keep_ratio))
indices = torch.randperm(n_tokens, device=img_emb.device)[:n_keep].sort().values

# Line 64 (l2norm)
n_keep = max(1, int(n_tokens * keep_ratio))
_, topk_idx = torch.topk(norms, n_keep)
```

Both are called with the same `args.keep_ratio` at line 126. The JSON config confirms `n_keep_per_image: 230`, which is `int(256 * 0.9)`. **No reversal bug exists.**

`embed_prefix` is called **once** per `sample_actions()` (line 806), then cached as KV values for all 10 denoising steps. So random pruning does NOT create per-denoising-step inconsistency.

### 2. Results Summary

| k | Random SR | L2norm SR | Random seed |
|---|-----------|-----------|-------------|
| 0.3 | 36.4% | 51.0% | 42 |
| 0.5 | 68.4% | 33.4% | 43 |
| 0.7 | 77.2% | 55.0% | 42 |
| 0.9 | **12.0%** | **98.2%** | 42 |
| 1.0 (baseline) | 98.2% | 98.2% | 42 |

Both methods violate monotonicity. L2norm at k=0.5 (33.4%) < k=0.3 (51.0%). Random k=0.9 (12%) << k=0.7 (77.2%).

### 3. Token Importance Analysis

π0.5 post-projector L2 norms: **CV = 0.0547**, normalized entropy = **0.9997**. Token norms are nearly perfectly uniform. L2norm pruning is essentially arbitrary selection — functionally close to random. Yet L2norm k=0.9 = 98.2% vs random k=0.9 = 12.0%. This is physically contradictory.

### 4. Key Observations

- **No dedicated π0.5 log for k=0.9**: The log file `eval_random_k09_seed42.log` is from an **OpenVLA** run (line 1: "Loading OpenVLA from..."), not π0.5. The actual π0.5 k=0.9 run has no preserved log.
- **Script modified at 19:26 on May 21**: Filename format changed to include seed. k=0.9 run (finished May 22 01:18) used the post-modification script. Without version control, we can't diff what else changed.
- **Timing consistent with 12% SR**: 111.4 min for 500 episodes = most episodes running to max_steps, consistent with real failures.
- **Missing `torch.manual_seed`**: Only `np.random.seed(42)` is set. `torch.randperm` uses uncontrolled PyTorch CUDA RNG. Not a bug per se, but means the exact random state is unreproducible.
- **Missing embed_image scaling**: The pruning script omits `features * hidden_size**0.5` that the old script includes. But this affects ALL runs equally (L2norm k=0.9 works fine with same script).

### 5. Root Cause Assessment

**No code bug found.** The pruning functions are correct, the monkey-patching is correct, and the `embed_prefix` caching is correct.

The 12% result **violates information-theoretic monotonicity** (keeping 90% of tokens cannot be worse than keeping 70% with the same method). This points to one of:

1. **Transient runtime issue** during the specific k=0.9 run (most likely) — e.g., GPU numerical error, model loading issue, or a race condition. The absence of a log file makes this impossible to diagnose.
2. **Script had a different version** when k=0.9 ran. Without version control, we can't verify.
3. **Uncontrolled torch RNG** interacting with flow matching noise — unlikely but untestable without reproducing.

### 6. Recommended Actions

1. **Rerun random k=0.9** with explicit `torch.manual_seed(42)` and verbose logging:
   ```python
   # Add at script start, after np.random.seed
   torch.manual_seed(args.seed)
   torch.cuda.manual_seed_all(args.seed)
   ```
   Also add a per-step print: `log.info(f"[Pruning] n_keep={n_keep}, indices_sample={indices[:5].tolist()}")` in `prune_tokens_random` for the first replan of each episode.

2. **Run k=0.9 and k=0.1 back-to-back** in the same process to confirm monotonicity.

3. **Put the script under git** to track future modifications.

### 7. Affected Experiments

Only `pi05_random_k0.90_libero_object_seed42.json` is suspect. All other results show plausible (if noisy) patterns. The L2norm non-monotonicity (k=0.5 < k=0.3) is a separate issue worth investigating but less extreme.

---
