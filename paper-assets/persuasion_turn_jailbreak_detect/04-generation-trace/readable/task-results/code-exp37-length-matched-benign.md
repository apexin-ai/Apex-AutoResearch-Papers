# code exp37 length matched benign

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp37-length-matched-benign_20260521T004210_result.json`
- **Structured JSON:** [`fc9ee91590b14664901f.json`](../../sessions/fc/fc9ee91590b14664901f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp37 完成，conclusion=**negative**。结果摘要：

**Part 1 — WildChat 分层 FPR**
| Bucket | FPR (mean±std) | n |
|--------|---------------|---|
| Short (3-10) | 0.770±0.105 | 196 |
| Medium (11-15) | 0.942±0.054 | 23 |
| Long (16+) | 0.857±0.117 | 7 |

Short bucket FPR 反而**低于** Medium，说明 WildChat 高 FPR 不是 length 驱动的。

**Part 2 — Benign 截断测试**
FPR 在所有截断水平（K=3/5/8/10）均为 **0.000**，3 seeds 全一致。模型不依赖 turn count 判别 benign。

**Part 3 — Jailbreak padding 测试**
| Attack | Original | Padded (→15 turns) | Delta |
|--------|----------|-------------------|-------|
| DD | 0.996±0.006 | 0.971±0.012 | -2.5pp |
| **AA** | **0.963±0.035** | **0.383±0.261** | **-57.9pp** |

DD 几乎不受影响。但 AA 在追加 benign turns 后检测率从 96.3% 暴跌到 38.3%（seed123 最差仅 5%）。这是 BiGRU attention dilution 漏洞——大量 benign 尾部内容稀释了 AA 微妙的 jailbreak 信号。

---
