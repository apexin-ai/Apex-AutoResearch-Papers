# diagnose exp 006 mmlu domain gamma n24

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_006_mmlu_domain_gamma_n24_20260516T120739_result.json`
- **Structured JSON:** [`7c581027f2481bdfcb57.json`](../../sessions/7c/7c581027f2481bdfcb57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验实际已成功完成，cron 误判为 failed。**

### 证据

1. **无 fitting.log 文件**，但有 3 个完整的结果子目录（STEM_Math, STEM_Science, STEM_CS_Eng）
2. **每个域都有完整的 `irt_results.json`**，包含：
   - 收敛诊断全部通过（`all_ok: true`，无 divergence，Rhat < 1.01，ESS > 900）
   - 后验预测检验结果正常（PPP 0.44–0.89）
   - gamma 估计完整

3. **无进程在运行**（实验已完成）

### 结果摘要

| Domain | N_models | N_items | Fit time | PPP | γ mean | γ CI excludes 0 |
|--------|----------|---------|----------|-----|--------|-----------------|
| STEM_Math | 23 | 1190 | 527s | 0.438 | 0.969 | Yes |
| STEM_Science | 23 | 1397 | 618s | 0.807 | 0.838 | Yes |
| STEM_CS_Eng | 23 | 557 | 153s | 0.892 | 0.197 | No |

### 根因

实验注册时 server 字段填了 "A6000"（不存在），cron 无法 SSH 验证进程状态，自动标记 failed。实际上实验在 cqa1-21977 上正常运行并成功完成了全部 3 个域的 IRT fitting。

**结论：假阳性 failure，实验成功。需要将实验注册的 server 字段更正为 "cqa1-21977"。**

---
