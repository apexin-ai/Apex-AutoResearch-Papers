# ops 16980 gpu0 check docred relay

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_16980_gpu0_check_docred_relay_20260520T121442_result.json`
- **Structured JSON:** [`9b0945d4b7649e983256.json`](../../sessions/9b/9b0945d4b7649e983256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型已加载，正在推理。

## 报告

**1. GPU 状态**
| GPU | 进程 | VRAM | 任务 |
|-----|-------|------|------|
| GPU0 | PID 756540 | 18270 MiB | **Llama beam8 s1** (刚启动) |
| GPU1 | PID 755449 | 21122 MiB | Llama beam8 unc (31/200) |

**2. DocRED d066 beam sweep 完成清单**

| 配置 | 状态 |
|------|------|
| Llama beam2 unc | ✅ 200/200 |
| Llama beam2 s1 | ✅ 200/200 |
| Llama beam8 unc | ⏳ 31/200 (GPU1) |
| **Llama beam8 s1** | **⏳ 刚启动 (GPU0, PID 756540)** |
| Llama beam1 unc | ❌ 待跑 |
| Llama beam1 s1 | ❌ 待跑 |
| Llama beam4 unc | ❌ 待跑 |
| Llama beam4 s1 | ❌ 待跑 |
| Qwen beam2 unc | ✅ 200/200 |
| Qwen beam2 s1 | ✅ 200/200 |
| Qwen beam8 unc | ✅ 200/200 |
| Qwen beam8 s1 | ✅ 200/200 |
| Qwen greedy unc | ✅ 200/200 |
| Qwen greedy s1 | ✅ 200/200 |

**3. 新启动**: Llama beam8 s1, PID 756540, GPU0

**4. 磁盘**: /root/autodl-tmp 171G/250G used (80G free, 69%)

---
