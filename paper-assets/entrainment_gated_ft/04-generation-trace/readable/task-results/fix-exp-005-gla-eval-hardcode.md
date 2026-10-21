# fix exp 005 gla eval hardcode

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp-005-gla-eval-hardcode_20260522T154045_result.json`
- **Structured JSON:** [`7526c27ece84e32a4ce0.json`](../../sessions/75/7526c27ece84e32a4ce0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前下载状态：

| 模型 | 进度 | 速度 | 预计剩余 |
|------|------|------|----------|
| **DeltaNet** | 80% | ~30-65 MB/s | ~9 分钟 |
| **HGRN** | 20% | ~54-96 KB/s | **~2 小时 22 分** |

DeltaNet 接近完成，HGRN 下载极慢（从 HuggingFace 直接下载被限速到 ~80 KB/s）。

总结：
- **GLA 评估已完成** — lambada_openai acc=0.3819, ppl=23.96; arc_easy acc=0.5673
- **DeltaNet** — 还需 ~10 分钟下载完成，之后可立即评估
- **HGRN** — 按当前速度还要 2+ 小时。建议杀掉当前 wget，改用 ModelScope 下载（跟 GLA 一样的方式，国内 CDN 快得多）

是否要我把 HGRN 切换成 ModelScope 下载？

---
