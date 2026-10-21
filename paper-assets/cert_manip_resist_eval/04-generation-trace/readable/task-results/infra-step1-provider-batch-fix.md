# infra step1 provider batch fix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_step1-provider-batch-fix_20260522T115926_result.json`
- **Structured JSON:** [`7488ee84c390398b24e7.json`](../../sessions/74/7488ee84c390398b24e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行 8 分钟，0 个 503 警告——1 worker / 1 rps 策略有效。

## 当前状态汇总

| 项目 | 状态 |
|------|------|
| **v3 进程** | 已 kill (PID 97561, force killed) |
| **Checkpoint 进度** | 23/126 完成 (claude-3-haiku 14/14, gpt-4o 9/14) |
| **OpenAI 测试** | 3/3 成功（gpt-4o-mini, 3-14s/请求），503 已恢复 |
| **新脚本** | `run_plan001_step1_batched.py` 已部署，PID 101904 运行中 |
| **并发配置** | Claude 1w/1rps, Gemini 1w/1rps, OpenAI 1w/0.3rps |
| **503 情况** | v1 (3w/5rps) 连续 503; v2 (1w/1rps) 0 个 503 至今 |
| **预估耗时** | ~5-8 min/condition × 103 conditions ≈ 9-14 小时 |

执行顺序：Claude (28 条件) → Gemini (14 条件) → OpenAI (61 条件，含 gpt-4o 剩余 5 条件)。

日志：`tail -f ~/runs/cert_manip_resist_eval/plan001_step1_batched_v2.log`

---
