# exp j16 gamma deploy watcher

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_j16-gamma-deploy-watcher_20260518T022838_result.json`
- **Structured JSON:** [`f2f0a121548a77711c2b.json`](../../sessions/f2/f2f0a121548a77711c2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Watcher 已部署（PID 64415）。

当前进度汇总：

**MCMC J=16 状态：3/8 domains 完成，Medical 进行中**

已完成的 3 个 domain 结果：

| Domain | n_items | J=16 γ_mean | J=16 γ_median | 95% CI | P(γ<0) | PPP | Rhat | Converged |
|--------|---------|-------------|---------------|--------|--------|-----|------|-----------|
| STEM_Math | 1190 | 0.5955 | 0.6018 | [-0.076, 1.247] | 0.038 | 0.305 | 1.007 | Yes |
| STEM_Science | 1397 | 0.5661 | 0.5672 | [-0.071, 1.203] | 0.043 | 0.197 | 1.007 | Yes |
| STEM_CS_Eng | 557 | 0.3202 | 0.3218 | [-0.556, 1.206] | 0.240 | 0.503 | 1.006 | Yes |

**待完成：** Medical (进行中), Other, Business_Law, Humanities, Social_Sciences + pooled

**Watcher 行为：** PID 61916 结束后自动写入 `DONE_MARKER.txt` 和 `collected_results.json`。下次检查时 `cat /root/autodl-tmp/exp006/mmlu_domain_irt_j16_qwen/DONE_MARKER.txt` 即可判断是否完成。

---
