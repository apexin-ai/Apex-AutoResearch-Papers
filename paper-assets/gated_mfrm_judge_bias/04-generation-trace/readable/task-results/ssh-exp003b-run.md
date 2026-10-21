# ssh exp003b run

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003b_run_20260522T173806_result.json`
- **Structured JSON:** [`46d9de82676ac97e6302.json`](../../sessions/46/46d9de82676ac97e6302.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，MCMC warmup 已开始采样。

**models.py 修改 diff:**
```diff
- from lib.priors import reg_horseshoe_prior_cn
  (removed)

-     # Regularized Horseshoe prior for c_n (Piironen & Vehtari, 2017)
-     c = reg_horseshoe_prior_cn(N)
+     # Hierarchical half-normal prior for contamination susceptibility
+     sigma_c = numpyro.sample("sigma_c", dist.HalfNormal(1.0))
+     c_raw = numpyro.sample("c_raw", dist.HalfNormal(jnp.ones(N) * 1.0))
+     c = numpyro.deterministic("c", c_raw * sigma_c)

-     c_hat = _to_numpy(samples_dict["c_n"].mean(axis=0))
+     c_hat = _to_numpy(samples_dict["c"].mean(axis=0))
```

**run_exp003.py:** 无需修改，`--methods` 参数已存在。

**运行状态:**
- tmux session: `exp003b`
- GPU 0: 667 MiB, 74% utilization
- MCMC chain 1/4 warmup 进行中 (4000 warmup + 4000 samples × 4 chains sequential)
- 日志: `/tmp/exp003b.log`
- 输出目录: `/root/gated_mfrm_judge_bias/exp003/output_003b`

---
