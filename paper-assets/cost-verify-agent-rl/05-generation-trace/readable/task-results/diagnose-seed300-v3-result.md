# diagnose seed300 v3 result

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed300_v3_result_20260522T194231_result.json`
- **Structured JSON:** [`ea137d273889d9e02a4c.json`](../../sessions/ea/ea137d273889d9e02a4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：seed300 step5 checkpoint OOD 能力为零，与 response_mask 无关

| 指标 | 值 |
|------|-----|
| **OOD pass@1** | **0.0%** |
| action_is_valid | 91.78% |
| response_length | 4150.7 |
| success / raw_reward | 0.0 |
| best@134/mean | 0.0 |
| **runtime enable_response_mask** | **False** ✓ |
| eval episodes | 134 |
| 错误 | 仅 atexit BrokenPipeError（清理回调，不影响结果） |

**判定**：v3 用了正确的 `enable_response_mask=False`，OOD 仍然 0.0%。结合之前的证据链：

- v2（mask=True）→ OOD 0.0%
- v3（mask=False）→ OOD 0.0%
- seed7 ablation 证实 mask 确实影响 eval（mask=True: 0% vs mask=False: 8.2%）

**response_mask bug 对 seed300 无影响，因为 checkpoint 本身就没有 OOD 泛化能力。** 134 个 episode 全部失败（包括 best@134 也是 0.0），action_is_valid 91.78% 说明模型在生成合法动作，但无法完成任何 OOD 任务。问题出在 seed300 训练本身，不在 eval 配置。

---
