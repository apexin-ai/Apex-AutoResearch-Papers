# paper 018 prewrite two versions

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_018-prewrite-two-versions_20260516T110727_result.json`
- **Structured JSON:** [`57ec16186a075470a40d.json`](../../sessions/57/57ec16186a075470a40d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已产出并注册 `artifacts/018/paper/018_prewrite_two_versions.md`。

两版核心差异：

- **Version A**（CIVO 消失）：obs decoder gradient pathway 是 CIVO 的充要条件；KL 7% 梯度仅约束 dynamics consistency，不编码 obs-level temporal patterns → 因果链闭合：obs decoder grad → dt_emb temporal features → biased RSSM → critic overestimation → CIVO。强调 0%/92.7%/100% 三级递进实验。
- **Version B**（CIVO 存续）：vulnerability 在 representation level 而非 gradient pathway；transition model 为满足 KL objective 必须学 Δt-conditioned dynamics → 即使只有 7.3% 信号也足以产生 scale-dependent bias。指向架构级干预（orthogonality / information bottleneck / temporal factorization），并讨论对 THICK/Hieros 的 implication。

结果出来后替换 `[EVAL]`/`[NVE]`/`[STEP]` 占位符，选对应版本插入即可。

---
