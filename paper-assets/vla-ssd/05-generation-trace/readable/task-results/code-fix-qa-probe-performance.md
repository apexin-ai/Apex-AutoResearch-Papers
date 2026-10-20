# code fix qa probe performance

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_qa_probe_performance_20260516T230439_result.json`
- **Structured JSON:** [`68dc170978f62afec398.json`](../../sessions/68/68dc170978f62afec398.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。以下是完整结果：

---

## Progress 4-class Probe

| Layer | Trained | Untrained |
|-------|---------|-----------|
| L0 | 0.8508 | 0.8508 |
| L4 | 0.8559 | 0.8532 |
| L8 | 0.8560 | 0.8517 |
| L12 | **0.8622** | 0.8487 |
| L16 | 0.8618 | 0.8443 |
| L20 | **0.8632** | 0.8458 |
| L24 | 0.8565 | 0.8443 |
| L28 | 0.8535 | 0.8441 |
| L32 | 0.8454 | 0.8443 |
| **DINOv2** | — | **0.8272** |
| **Projector** | — | **0.8508** |

## Subtask Binary Probe

| Layer | Trained | Untrained |
|-------|---------|-----------|
| L0 | 0.9298 | 0.9298 |
| L4 | 0.9301 | 0.9281 |
| L8 | 0.9347 | 0.9293 |
| L12 | 0.9343 | 0.9306 |
| L16 | **0.9367** | 0.9286 |
| L20 | **0.9367** | 0.9294 |
| L24 | 0.9346 | 0.9292 |
| L28 | 0.9329 | 0.9278 |
| L32 | 0.9254 | 0.9279 |
| **DINOv2** | — | **0.9209** |
| **Projector** | — | **0.9298** |

---

## 关键对比

| 指标 | Best Trained | Best Untrained | DINOv2 |
|------|-------------|---------------|--------|
| Progress best | L20: 0.8632 | L4: 0.8532 | 0.8272 |
| Subtask best | L16/L20: 0.9367 | L12: 0.9306 | 0.9209 |

**观察**（仅记录数字，不下结论，遵守 C001 约束）：
- Trained 在两个任务上 mid-layer (L12-L20) 有一个 inverted-U 峰
- Untrained 在 progress 上从 L0 开始缓慢下降，subtask 上基本平坦
- Trained L0 == Untrained L0 == Projector（符合预期：L0 就是 projector 输出）
- Trained best vs Untrained best 差异：progress +1.0%, subtask +0.6%
- 所有 VLA 条件 >> DINOv2（progress +2-3.6%, subtask +0.7-1.6%）

---
