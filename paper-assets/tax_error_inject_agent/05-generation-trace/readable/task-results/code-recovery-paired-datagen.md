# code recovery paired datagen

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recovery-paired-datagen_20260515T134851_result.json`
- **Structured JSON:** [`d2199d482776471b68f5.json`](../../sessions/d2/d2199d482776471b68f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认运行中。让我在这里做一个当前状态总结：

---

**Recovery-Paired Injection 数据生成 — 执行状态**

**Step 1 Dry-run:** 通过
- 760 injected variants → 711 可处理（49 无 source match）
- P1=170, P2=184, C1=182, C4=175
- 5,408 次 API 调用，平均 7.6 步/trajectory

**Step 2 质量抽查:** 通过
- 3 条真实 API 测试全部成功
- P1 recovery: 正确识别步序错乱，高效恢复（3-5 步）
- P2 recovery: 正确识别子目标缺失，推理链合理（21 步较长但合理）
- Recovery 从 error state 正确接续，非重新开始

**Step 3 成本确认:** $15.31（2,878,433 input + 811,200 output tokens）

**Step 4 全量执行:** 已启动
- PID: 158010 (python), 158004 (bash)
- 输出文件: `data/recovery_paired/recovery_paired.jsonl`
- 日志: `logs/recovery_paired_gen.log`
- 预估时间: ~10 小时（串行 API 调用）

进度可通过日志中 `Processed X/760` 监控（每 100 条打印一次）。需要我定期检查进度吗？

---
