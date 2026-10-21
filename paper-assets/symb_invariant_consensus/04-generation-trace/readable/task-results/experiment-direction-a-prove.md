# experiment direction a prove

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_direction-a-prove_20260520T074330_result.json`
- **Structured JSON:** [`6a73308220647cbf55b3.json`](../../sessions/6a/6a73308220647cbf55b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Direction A PROVE 实验完成。结果总结：

| Metric | Value |
|---|---|
| Code gen success rate | 15.2% (31/204) |
| Verification conclusive rate | 7.8% (16/204) |
| Accuracy (conclusive only) | 50.0% (8/16) |
| **Accuracy (PROVE + SC fallback)** | **71.6% (146/204)** |
| **SC baseline (this run)** | **73.5% (150/204)** |
| SC baseline (exp035 ref) | 77.0% |
| SICA baseline (exp035 ref) | 76.5% |
| Total time | 1707s (~28min) |

**结论：负面结果。** PROVE 方向在 Qwen2.5-7B 上不 work：
1. **代码生成率极低**（15.2%）— 7B 模型难以为自然语言逻辑问题生成有效的 `verify()` 函数
2. **结论性验证更低**（7.8%）— 即使代码成功生成，多数情况下不是恰好 1 个候选通过
3. **结论性准确率仅 50%** — 当 PROVE 给出确定答案时，正确率跟随机猜没区别
4. **PROVE+fallback 反而比纯 SC 低 2 个点**（71.6% vs 73.5%）— 因为 conclusive-but-wrong 的 case 覆盖了原本正确的 SC 投票

Server 完整结果（含 verify_code）：`/root/symb_invariant_consensus/results/direction_a_prove/results.json`
本地摘要：`artifacts/direction_a_prove_results.json`（已注册 `art_20260520_3762cb`）

---
