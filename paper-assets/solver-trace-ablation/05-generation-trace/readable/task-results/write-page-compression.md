# write page compression

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_page-compression_20260514T233121_result.json`
- **Structured JSON:** [`8cc1efc86985de4252ed.json`](../../sessions/8c/8cc1efc86985de4252ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

精简完成。各文件变化：

| 文件 | 原行数 | 新行数 | 减少 |
|------|--------|--------|------|
| related_work.tex | 29 | 22 | -7 (24%) |
| method.tex | 64 | 52 | -12 (19%) |
| experiments.tex | 111 | 94 | -17 (15%) |
| conclusion.tex | 21 | 17 | -4 (19%) |
| introduction.tex | 33 | 32 | 未改 |
| **合计** | **258** | **217** | **-41 (16%)** |

主要改动：

**Related Work** — 4 段各压缩至 3-4 句 / 2 句。保留所有直接对比 citation，删除次要引用（pan-reward-misspecification, kwa-catastrophic-goodhart, macdiarmid-emergent-misalignment 等）。去掉详细方法描述，只留 "X does Y; we differ in Z" 格式。

**Method** — sec:task 从 7 行压缩到 3 行（intro 已有铺垫）；sec:sta 尾部删除与 related work 重复的 mutation testing 对比；ISR limitations 从 3 句压到 2 句；sec:rewards 去掉 Random 的详细 justification 和 SFT 的长描述。

**Experiments** — Setup 从 9 行压到 4 行（删 Prover9/SWI-Prolog 重复说明、6 条件列举、分类方法描述）；collapse trajectory 合并步骤数据到一句；SFT baseline 从 4 句压到 2 句；low-dose ISR 合并 H7 描述；premise-count confound 删最后一句；high-dose 从 4 句压到 1 句；cross-logic 精简详细数值。

**Conclusion** — 合并两段 future work 为一句；Interpreting ISR 和 Meta-Level Goodhart 各删 1 句。

所有 \label、\ref、\cite、%% registry 注释均完整保留。三条 Claim 的证据链未受影响。

---
