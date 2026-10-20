# debug closedloop diagnosis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_closedloop_diagnosis_20260519T162132_result.json`
- **Structured JSON:** [`e269c64fe428e684d7c2.json`](../../sessions/e2/e269c64fe428e684d7c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/closedloop_diagnosis.md`。

核心结论：

1. **6 个管线 Bug 已全部定位并修复**（180°旋转、JPEG roundtrip、gripper normalize+invert、center crop、10步等待、env.seed），修复后动作输出从退化（dim0 恒定 0.236）变为合理的变化模式。

2. **修复后 SR 仍为 0/9**（3 tasks × 3 eps），说明问题不仅是管线 Bug，模型本身的动作质量不足——demo 图像 L1 error 0.26–0.43，动作偏差约 30%，远超操作任务所需精度。

3. **扩大到 10–20 trials 极不可能看到非零 SR**：当前 env.seed(0) + do_sample=False 导致同一任务所有 episode 完全相同，本质上只测了 1 次；即使换不同 seed，系统性偏差不会消失。

4. **建议优先排查训练质量**（loss 是否收敛、checkpoint 是否为最优），或直接对比官方预训练好的 LIBERO-Goal checkpoint。

---
