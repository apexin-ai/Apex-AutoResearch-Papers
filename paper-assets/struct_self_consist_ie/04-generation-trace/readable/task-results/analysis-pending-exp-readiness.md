# analysis pending exp readiness

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pending_exp_readiness_20260515T103205_result.json`
- **Structured JSON:** [`0ea3aed2cd19df8a9720.json`](../../sessions/0e/0ea3aed2cd19df8a9720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册。结论：

**需要运行的实验（2个）:**
- `exp_017_llama_conll_n16_r1024` (seed=42) — 无输出，可立即跑
- `exp_017_llama_conll_n16_s456_r1024` (seed=456) — 空目录，可立即跑

模型（llama3.1-8b-conll2003-merged, 15GB）、数据（conll2003）、代码（run_mvp_pilot.py）均已到位。GPU 1-3 空闲，可并行跑两个。预计各 2-4 小时。

**已完成的实验（4个）:**
- exp_017 seed=123 r1024 ✅
- exp008_re_n16 ✅（registry 状态过期，实际结果已有）
- exp_007_ner_llama ✅（以 exp_007_llama_n16 命名完成）
- exp_002_merge_conll2003 ✅（以 exp_002_conll_n16 命名完成）

---
