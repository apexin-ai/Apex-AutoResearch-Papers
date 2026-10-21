# ops urgent gpu fill and status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-gpu-fill-and-status_20260518T153037_result.json`
- **Structured JSON:** [`bb2f9e472d434f86be4a.json`](../../sessions/bb/bb2f9e472d434f86be4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认。汇报如下：

---

## GPU 状态汇报

| GPU | 完成/运行 | 详情 |
|-----|----------|------|
| **cuda:0** | d025_s42 **完成** → 已启动 d100_s42 | 完成 loss=0.9429, adapter 154MB, 耗时 1h34m. 新任务 PID 36665, 已加载模型(559MiB) |
| **cuda:1** | d050_s42 **运行中** | 46% (1695/3642), loss~0.93, ETA ~45min |
| **cuda:2** | 14B d000_s42 **运行中** | 89% (2771/3125), loss~0.90, ETA ~18min |
| **cuda:3** | d000_s123 **完成** → 已启动 d005_s123 | 完成 loss=0.9249, adapter 154MB, 耗时 1h47m. 新任务 PID 36943, 已加载模型(559MiB) |

## 模型下载进度

| 模型 | safetensors | 大小 | incomplete | 状态 |
|------|------------|------|-----------|------|
| **Phi-4** | 3 files | 23G | 3 | 下载中 (PID 19608, 运行 5h+) |
| **OLMo-2-7B** | 4 files | 19G | 1 | 下载中 (PID 35305) |
| **Gemma-2-9B** | 6 files | 26G | 1 | 下载中 (PID 35312) |

14B d000_s42 约 18min 后完成，届时 cuda:2 可启动 14B d005_s42。

---
