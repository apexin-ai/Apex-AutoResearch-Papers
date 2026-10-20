# plan phase1 schedule

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_plan_phase1_schedule_20260517T031006_result.json`
- **Structured JSON:** [`285577a0ff65d303f0c2.json`](../../sessions/28/285577a0ff65d303f0c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存到 `/root/spectral_collapse_ews/phase1_schedule.md`。

调度方案要点：
- **Batch 1-3**：优先跑 pure_collapse vs adaptive 核心对比对，seed=42 最先出结果
- **Batch 4-6**：fixed_mix vs linear_increasing baseline 对
- GPU 交叉排列，同一 GPU 无连续相同 condition
- tau 留占位符，Phase 0 校准后替换（脚本默认 0.02）
- 所有 launch commands 使用 `CUDA_VISIBLE_DEVICES` + `--gpu 0` 模式，tmux session 命名清晰

Phase 0 Go/No-go PASS 后直接按 Batch 顺序复制执行即可。

---
