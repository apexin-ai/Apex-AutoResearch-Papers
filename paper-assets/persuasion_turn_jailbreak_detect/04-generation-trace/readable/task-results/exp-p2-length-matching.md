# exp p2 length matching

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_p2-length-matching_20260523T115114_result.json`
- **Structured JSON:** [`1e20b5577c2a3dd7c24d.json`](../../sessions/1e/1e20b5577c2a3dd7c24d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果

**正面证据：长度匹配后 F1 基本不变，模型不依赖 turn count shortcut。**

| 设置 | Full-set F1 | Range-matched F1 | Δ | Bucket-matched F1 | Δ |
|------|-------------|-------------------|------|---------------------|------|
| **DD OOD** | 0.887 ± 0.086 | 0.880 ± 0.094 | -0.008 | 0.913 ± 0.079 | +0.025 |
| **AA OOD** | 0.883 ± 0.091 | 0.898 ± 0.077 | +0.015 | 0.892 ± 0.074 | +0.009 |

关键发现：
- **DD OOD**: jailbreak turns [6,10], benign turns [6,14]，重叠区间 [6,10]。Range-matched F1 仅下降 0.8%，bucket-matched F1 反而上升 2.5%
- **AA OOD**: jailbreak turns [3,8], benign turns [6,14]，重叠区间 [6,8]（仅 34/80 jailbreak 保留）。Range-matched F1 反而上升 1.5%
- 两种匹配方式的 delta 均 < 3%，确认 OOD 检测不依赖长度差异

结果保存在 `results/exp67_length_matching.json`，脚本在 `scripts/exp67_length_matching.py`。

---
