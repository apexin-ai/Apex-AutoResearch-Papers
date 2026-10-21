# ops detailed progress check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_detailed-progress-check_20260521T205356_result.json`
- **Structured JSON:** [`70a199ad45896fd15f23.json`](../../sessions/70/70a199ad45896fd15f23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

---

```
[westd-41074] GPU0 | random k=0.95 v2        | PID 627788 | 170/500 eps (T4 ep20) | ~50 min left
[westd-41074] GPU1 | fixed-mask k=0.9 v2     | PID 629619 | 160/500 eps (T3 ep10) | ~78 min left
[westd-41074] GPU2 | VTC M96 train            | PID 68539  | 72450/100K steps      | ~15.3h left (0.5 sps)
[westd-41074] GPU3 | VTC M64 v6 train         | PID 59671  | 23650/100K steps      | ~35.4h left (0.6 sps)

[westd-38929] GPU0 | Baseline Spatial          |           | ✅ DONE  SR=97.2%
[westd-38929] GPU1 | L2norm k=0.5 Spatial     | PID 590423 | 470/500 eps (T9 ep20) | ~9 min left
[westd-38929] GPU2 | Random k=0.5 Spatial      |           | ✅ DONE  SR=71.6%
[westd-38929] GPU3 | L2norm k=0.3 Spatial     | PID 590816 | 470/500 eps (T9 ep20) | ~9 min left

[westd-27271] GPU0 | OpenVLA L2norm k=0.9 obj | PID 306593 | 380/500 eps (T7 ep30) | ~57 min left (2.1 eps/min)
[westd-27271] GPU1 | VTC M32 train            | PID 921279 | 74050/100K steps      | ~14.4h left (0.5 sps)

[cqa1-33015] GPU0  | SmolVLA random k=0.3 obj | PID 579179 | running ~54 min       | 进度不可见(无日志文件)
[cqa1-33015] GPU1  | SmolVLA sweep (GPU1脚本)  | PID 74648  | 第4/4实验 random k=0.3, T8 ep3/50 (403/500) | ~21 min left
[cqa1-33015] GPU1  | SmolVLA baseline obj      |           | ✅ DONE  SR=55.2% avg
```

关键发现：
- **即将完成**（<1h）：westd-38929 的两个 Spatial eval，westd-41074 的两个 Object eval，westd-27271 的 OpenVLA eval，cqa1 sweep
- **长训练**：M96 剩~15h，M64v6 剩~35h，M32 剩~14h
- **已完成**：Baseline Spatial 97.2%，Random k=0.5 Spatial 71.6%，SmolVLA baseline object ~55%

---
