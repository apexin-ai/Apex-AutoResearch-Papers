# code plan 004 step2 gsm8k semi synthetic

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157_result.json`
- **Structured JSON:** [`d35987c353060adf4dbd.json`](../../sessions/d3/d35987c353060adf4dbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。核心结果：

### GSM8K vs MMLU 对比

| 指标 | MMLU plan_011 (external) | GSM8K (external) | GSM8K (standard) |
|------|--------------------------|------------------|-------------------|
| Baseline FPR | 0.314 | **0.471** | 0.191 |
| ΔTPR p=0.5 | +0.508 | **+0.514** | **+0.749** |
| ΔTPR p=1.0 | +0.674 | +0.517 | **+0.818** |

### 关键发现

1. **Standard matching 表现优于预期**：baseline FPR 仅 19.1%，ΔTPR 在 p=0.5 就达到 +0.749，p=0.7 时 TPR 已饱和至 1.000。比 MMLU 的 external matching 更强。

2. **External matching 灵敏度极高但 FPR 太高**：p=0.3 时 TPR 已达 0.970，但 baseline FPR 高达 47.1%（与 Step 1 的 47.4% C-rate 一致）。FPR 不随 p 变化（预期行为——外部分数不受 GSM8K 注入影响），但这意味着 external matching 在 GSM8K 上无法区分真实 temporal DIF 和注入污染。

3. **Standard matching 的 FPR 膨胀**：从 p=0 的 0.191 升至 p=1.0 的 0.645，符合预期——20% items 被注入时 matching variable 被污染。

4. **方法论在 GSM8K 上验证成功**：standard matching 展现清晰的 dose-response，ΔTPR 单调递增，Fisher exact test 显著。

---
