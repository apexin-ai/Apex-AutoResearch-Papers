# verify lr hyperparams

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_lr-hyperparams_20260517T132209_result.json`
- **Structured JSON:** [`cf3b189630403e5441d7.json`](../../sessions/cf/cf3b189630403e5441d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总:

| 实验类型 | 脚本默认 LR | 实际使用 LR (checkpoint 确认) |
|----------|------------|-------------------------------|
| CLS (Qwen3-4B) | 2e-4 | **5e-5** |
| CLS (Qwen3-8B) | 2e-4 | **5e-5** |
| CWM (Qwen3-4B) | 2e-4 | **5e-5** (v11+; 早期 v9 用过 2e-4 已废弃) |
| CWM (Qwen3-8B) | 2e-4 | **5e-5** |
| DeepSeek CLS (6.7B) | 2e-4 | **2e-4** |
| DeepSeek CWM (6.7B) | 2e-4 | **2e-4** |
| DeepSeek TRAJ (6.7B) | 2e-4 | **2e-4** |

**关键发现:**

1. **Appendix 表格没有 typo** — Qwen CLS/CWM 四列都写 5e-5，checkpoint 确认一致
2. **所有 DeepSeek 实验用 lr=2e-4**（CLS、CWM、TRAJ 全部），但 appendix 超参表完全没有 DeepSeek 列
3. **没有 Qwen TRAJ checkpoint** — seetacloud 上只有 DeepSeek TRAJ
4. Reviewer 看到 TRAJ 用 2e-4 与表中 5e-5 不一致，原因是它们是不同模型族（DeepSeek vs Qwen），appendix 表只覆盖了 Qwen

**建议**: 在超参表中加 DeepSeek 列（或脚注），注明 DeepSeek 用 lr=2e-4，其余 LoRA 配置相同。

---
