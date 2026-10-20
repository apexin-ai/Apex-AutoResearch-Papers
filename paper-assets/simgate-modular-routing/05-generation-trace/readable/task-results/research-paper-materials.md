# research paper materials

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-materials_20260513T084621_result.json`
- **Structured JSON:** [`5da57ebd880d1a8b9221.json`](../../sessions/5d/5da57ebd880d1a8b9221.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入 `notes/` 目录。

## 关键发现

**ScienceWorld 环境**:
- 30 种 task，7,329 个 variations，涵盖物态变化、化学、生物分类、遗传学、电路等 10 个类别
- Action space: 26 种动作模板，每步约 417 个有效组合（动态变化）
- Text-based observation + score 0-100 百分制
- 不支持原生 state fork，需 action replay 实现

**Baselines（ScienceWorld 上有分数的）**:
| Method | Best Score | Model |
|--------|-----------|-------|
| STEP-HRL | 81.57 seen / 77.81 unseen | Llama-3-8B |
| EMPO² | 75.9 avg | Qwen2.5-7B |
| GLIDER | 77.43 seen / 68.34 unseen | Llama-3-8B |
| ETO | 58.17 seen | Mistral-7B |
| GPT-4 (ReAct) | 44.29 seen / 38.05 unseen | — |

**未找到的方法**: CogRouter 和 ITP-R 均未找到对应论文，已在文件中标注。

**未在 ScienceWorld 评测的**: ReTool、AgentMath、Select-then-Solve 三个方法均专注数学/通用 benchmark，无 ScienceWorld 结果。

注意：`autodl-simgate` 服务器 SSH 认证失败，文件写在了 `westb-13313` 上。

---
