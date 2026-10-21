# code exp58 truncated single turn

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp58_truncated_single_turn_20260522T132513_result.json`
- **Structured JSON:** [`fb97708133ef9927a8ff.json`](../../sessions/fb/fb97708133ef9927a8ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

### exp58 结果：9-class DAPT vs MLM DAPT (3-seed 均值 F1)

| Dataset | Mode | 9-class | MLM | Delta |
|---------|------|---------|-----|-------|
| IID | full | 1.000 | 0.983 | +0.018 |
| IID | last_turn | **0.991** | 0.894 | **+0.097** |
| DD OOD | full | 0.997 | 0.993 | +0.003 |
| DD OOD | last_turn | **0.942** | 0.924 | +0.018 |
| AA OOD | full | 0.972 | 0.941 | +0.031 |
| AA OOD | last_turn | **0.978** | 0.927 | **+0.051** |
| FITD OOD | full | 1.000 | 0.987 | +0.013 |
| FITD OOD | last_turn | **1.000** | 0.927 | **+0.073** |

### 分析

**假设得到支持。** 9-class DAPT 在所有数据集、所有条件下均优于 MLM。关键发现：

1. **截断后差距扩大**：full 模式下平均 delta=+0.016，last_turn 模式下平均 delta=+0.060。9-class 的单轮表征质量远优于 MLM。

2. **AA OOD 特殊现象**：9-class 在截断后 F1 反而从 0.972 升至 0.978（最后一轮包含更直接的恶意请求，去掉前面的伪装轮次反而更好分类）。

3. **对 R15 的解释**：既然 9-class 在单轮截断后仍大幅领先 MLM，说明 ToxicChat 上的逆转（MLM > classification）并非因为 MLM 的单轮语义更好，而是因为 ToxicChat 数据的多轮结构与合成数据差异大，9-class 的多轮结构建模反而成为负担。但需注意合成 vs 人类写作风格差异仍然是混淆因子，无法完全解耦。

---
