# code cross domain v2 prep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_domain_v2_prep_20260514T101514_result.json`
- **Structured JSON:** [`792d1da8da4cb5eed86b.json`](../../sessions/79/792d1da8da4cb5eed86b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。脚本 `/root/ratekv/run_cross_domain_v2.py` 已就绪：

- 所有 import 正常，所有依赖文件存在
- `C4_PROFILES_CACHE` 不存在（首次运行会自动 profile 并缓存）
- 逻辑：C4 profiling（带缓存）→ 加载 WT2 profiles → 双向 MCKP + cross-domain eval + same-domain baseline + agreement rate
- 输出：`/root/ratekv/cross_domain_v2_results.json`
- c4_rerun 完成后可直接 submit_training_job 提交

---
