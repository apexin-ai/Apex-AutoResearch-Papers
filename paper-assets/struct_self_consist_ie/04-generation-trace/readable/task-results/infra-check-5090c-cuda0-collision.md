# infra check 5090c cuda0 collision

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_5090c_cuda0_collision_20260521T113110_result.json`
- **Structured JSON:** [`92949619993d463dcd0d.json`](../../sessions/92/92949619993d463dcd0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 进程状态

| 实验 | PID | 状态 |
|------|-----|------|
| exp_fewnerd_n16_s456_v2 | 293438 | **已完成** (EXIT_CODE=0)，19:02 UTC 正常退出 |
| exp_fewnerd_n16_s123 | 311981 | **运行中**，已运行 ~7 分钟 |

### s456_v2 产出
- `output/fewnerd_n16_seed456_v2/report.json` (1.6KB)
- `output/fewnerd_n16_seed456_v2/samples.jsonl` (1.28GB)
- 日志确认 `EXIT_CODE=0`，引擎正常 shutdown

### s123 进度
- 正在处理 prompts: 2992/602368 (~0.5%)，运行约 5 分钟
- 预估速度: input ~1455 toks/s, output ~677 toks/s
- 预估剩余时间: ~3 小时

### GPU 0 状态
- 显存: 30131 / 32607 MiB (92%)
- 利用率: 80%
- s123 独占 GPU 0，无碰撞

### 建议操作
1. **更新 registry**: 将 exp_fewnerd_n16_s456_v2 标记为 COMPLETED
2. **无需干预 s123**: 正常运行中，GPU 独占，无碰撞

---
