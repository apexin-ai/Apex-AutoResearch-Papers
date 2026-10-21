# code plan001 parallel v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-parallel-v2_20260522T094736_result.json`
- **Structured JSON:** [`22f187a5382cb1f92757.json`](../../sessions/22/22f187a5382cb1f92757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动正常。9 个模型全部同时开跑，无 stagger。已完成的 23 个 checkpoint 全部正确 SKIP。

当前状态：
- **已完成**: 23/126 (claude-3-haiku 全部 14 条 + gpt-4o 9 条)
- **剩余**: 103 conditions 正在并发执行
- **配置**: 25 workers/model, max_rps=50 (实质无限制), 无全局信号量
- **tmux session**: `plan001_step1_v2`, PID 94836
- **日志**: `~/runs/cert_manip_resist_eval/plan001_step1_v2.log`

vs 旧版：3 workers/model + 全局 15 并发 + 3 RPS → 12 分钟 0 新 checkpoint。新版理论上快 8x+。

---
