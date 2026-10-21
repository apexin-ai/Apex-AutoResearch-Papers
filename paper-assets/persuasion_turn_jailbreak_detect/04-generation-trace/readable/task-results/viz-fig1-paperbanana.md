# viz fig1 paperbanana

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig1_paperbanana_20260524T092626_result.json`
- **Structured JSON:** [`bb0902c87c209a000f0d.json`](../../sessions/bb/bb0902c87c209a000f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。经过 5 轮迭代，最终 v5 通过了所有检查：

- 4 个 User 对话气泡（User₁–User₃ + Userₖ）
- ×7 Objectives 名称全部正确（9-Class, Binary, Scrambled, MLM, Wiki-MLM, Topic, Vanilla）
- frozen [CLS] ❄ 标注清晰
- BiGRU ← → + MLP → Jailbreak/Benign 流程完整
- 顶会级别视觉质量

产出文件：
- `docs/paper/figures/paper/fig1_architecture.png`
- `docs/paper/figures/paper/fig1_architecture.pdf`

---
