# status 21461 progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_21461_progress_20260520T010644_result.json`
- **Structured JSON:** [`dad25b6d1e11ea9188d8.json`](../../sessions/da/dad25b6d1e11ea9188d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇报

### d066 beam sweep (GPU 1)
**3/8 configs 完成，当前跑 beam2_full_s1 (465/551 samples)**

| Config | 状态 | 行数 |
|--------|------|------|
| beam1_unconstrained | ✅ | 551/551 |
| beam1_full_s1 | ✅ | 551/551 |
| beam2_unconstrained | ✅ | 551/551 |
| beam2_full_s1 | 🔄 运行中 | 465/551 (84%) |
| beam4_unconstrained | ⏳ | - |
| beam4_full_s1 | ⏳ | - |
| beam8_unconstrained | ⏳ | - |
| beam8_full_s1 | ⏳ | - |

当前 config 约 5 分钟内完成。beam4/beam8 每 sample 推理时间会随 beam width 增长，剩余 4 configs 预计 **3-5 小时**。

### d067 seed variance (GPU 0)
**4/12 configs 完成，当前跑 llama_scierc_seed123_unconstrained (5/551 samples)**

| Config | 状态 | 行数 |
|--------|------|------|
| qwen_scierc seed123 unc | ✅ | 551/551 |
| qwen_scierc seed123 con | ✅ | 551/551 |
| qwen_scierc seed456 unc | ✅ | 551/551 |
| qwen_scierc seed456 con | ✅ | 551/551 |
| llama_scierc seed123 unc | 🔄 刚启动 | 5/551 |
| llama_scierc seed123 con | ⏳ | - |
| llama_scierc seed456 unc | ⏳ | - |
| llama_scierc seed456 con | ⏳ | - |
| qwen_docred seed123 unc | ⏳ | - |
| qwen_docred seed123 con | ⏳ | - |
| qwen_docred seed456 unc | ⏳ | - |
| qwen_docred seed456 con | ⏳ | - |

刚加载完 llama 模型开始推理。每 config ~30 min，剩余 8 configs 预计 **~4 小时**。

### GPU 利用率
| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU 0 (d067) | 77% | 19.0 / 95.6 GB |
| GPU 1 (d066) | 80% | 19.0 / 95.6 GB |

两块 GPU 都在正常工作，显存占用约 20%。

---
