# analysis exp029 seed100 resume step10

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp029_seed100_resume_step10_20260523T001411_result.json`
- **Structured JSON:** [`ca60a31b65b5e4fb4021.json`](../../sessions/ca/ca60a31b65b5e4fb4021.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## exp029_seed100_resume_step10 结果总结

**训练状态**: ✅ 成功完成 (EXIT_CODE=0, 2.12h)

### 关键指标

| 指标 | Step 5 (resume) | Step 10 (final) |
|------|----------------|-----------------|
| ID eval success (32-ep) | 31.25% | **37.5%** (+6.25pp) |
| reward mean@32 | 3.125 | **3.75** |
| response length | 3502 | **2717** (更高效) |

### 训练健康度: HEALTHY
- **Reward**: 波动上升 (3.91 → 4.77 → 2.81 → 4.53)，step9 有单步回落但 step10 立即恢复
- **KL**: 极低 (0.002-0.007)，未偏离 reference
- **Entropy**: 0.121 → 0.081，策略稳步收敛无 collapse
- **Collapse 检测**: first_turn_valid_rate = 98.4%，MI 健康

### Checkpoint
`/root/autodl-tmp/checkpoints/exp029-seed100/global_step_10/actor/` — FSDP shards 完整 (~20GB)

### 下一步
需要用此 checkpoint 跑 **OOD eval** (AlfworldSG_OOD) 验证 hypothesis：seed100 step10 OOD 是否从 step5 的 11.2% 提升到 20-25%。

---
