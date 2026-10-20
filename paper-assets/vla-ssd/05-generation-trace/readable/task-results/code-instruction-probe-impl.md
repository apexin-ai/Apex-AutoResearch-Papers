# code instruction probe impl

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_instruction-probe-impl_20260515T162204_result.json`
- **Structured JSON:** [`0a850c22dc5f5ab3cb6d.json`](../../sessions/0a/0a850c22dc5f5ab3cb6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码已创建并验证通过。

**文件**: `/root/vla-ssd/scripts/train_instruction_probes.py`

**验证结果** (用现有 LIBERO-10 特征中 LIVING_ROOM_SCENE2 的 2 个 task 测试)：
- Scene grouping 自动发现正确 — `LIVING_ROOM_SCENE2` 包含 2 tasks
- Visual gate: t=0 DINO cos_sim = 0.9981 [PASS]
- Goal classification (trained VLA): Layer 0 = 96.9%, Layer 16 = 97.1%, Layer 32 = 94.1%
- DINO baseline: 96.6% (注意：这是全轨迹数据，视觉会在执行中分化，所以 DINO 也能区分。LIBERO-Goal 中共享 scene 的 task 初始状态完全相同，才是真正的 negative control 条件)
- 输出 `results.json` + `visual_gate.json` 格式正确

---
