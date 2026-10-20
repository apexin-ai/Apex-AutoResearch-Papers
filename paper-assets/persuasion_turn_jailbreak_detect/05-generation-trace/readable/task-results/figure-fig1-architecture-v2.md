# figure fig1 architecture v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1-architecture-v2_20260518T082453_result.json`
- **Structured JSON:** [`1394fe96d66044861d23.json`](../../sessions/13/1394fe96d66044861d23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。

- **PDF**: 55.6 KB (`fig1_architecture.pdf`)
- **PNG**: 146.9 KB (`fig1_architecture.png`)

布局：Multi-turn Conversation → Extract user turns → Stage 1 (DeBERTa-v3-base + 7 training objectives 列表) → Frozen [CLS] embeddings → Stage 2 (BiGRU → Softmax) → Jailbreak/Benign。Stage 1 浅蓝背景，Stage 2 灰色背景，单条 pipeline 流程，7 variant 以紧凑列表呈现。

DONE

---
