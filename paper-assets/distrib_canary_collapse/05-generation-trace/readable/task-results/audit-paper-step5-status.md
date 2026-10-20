# audit paper step5 status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_step5_status_20260516T031303_result.json`
- **Structured JSON:** [`2852df2bc3915bb8243a.json`](../../sessions/28/2852df2bc3915bb8243a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是逐项审计结果：

---

## Paper Step 5 审计报告

### 文件概况
论文在**本地** `docs/paper/` 目录（不在服务器上）。最近修改：
- `experiments.tex` — May 16 02:39 (最新)
- `discussion.tex` — May 16 02:27
- `method.tex` — May 16 00:08
- 其余文件 — May 15

### GPT-2m cross-arch 结果整合：**已写入，但标注为 preliminary**

| 位置 | 状态 |
|------|------|
| `experiments.tex:72` | 提到 GPT-2-medium 12 pairs, Fleiss κ=0.091 |
| `discussion.tex:15` | "Preliminary cross-architecture validation on GPT-2-medium (single seed, α=1.0)" — Tier 3 共识, 6/6 canary→diversity pairs 显著 |
| `discussion.tex:41` | batch size 差异 (32 vs 4) 已讨论 |
| `discussion.tex:51` | 标注需要 multi-seed 验证 |

**无 Table 行包含 GPT-2m 数值**（没有独立的 GPT-2m 结果表格）。

### W1 — T notation 修复：**已完成**

论文统一使用 `$T{=}10$ generation cycles`，`experiments.tex:13` 明确定义 "T=10 generations (11 time points including the generation-0 baseline)"。T+1 约定在各文件中一致。

### W2 — batch_size 差异注释：**已完成**

`discussion.tex:41` — "GPT-2-medium uses batch size 32 (versus 4 for Pythia) for GPU efficiency, exposing 8× more data per training step, which may accelerate collapse dynamics without altering the qualitative pattern"

### W3 — claim 措辞天花板（避免 architecture-agnostic / scale-independent 过度声称）：**已完成**

- abstract、conclusion 中**无** "architecture-agnostic"、"scale-independent"、"universal"、"generalizable" 等过度声称
- abstract: 仅说 "Applied to Pythia-410M"，GPT-2m 标注为 "preliminary single-seed evidence"
- conclusion:11 — "This result is deliberately scoped to lexical diversity, not model collapse broadly"
- conclusion:14 — 方法论迁移性声称限于框架本身，而非实验结论
- discussion:12 — 明确说 "Generalization to other model architectures...requires independent validation"
- discussion:51 — "Cross-architecture validation beyond our preliminary single-seed GPT-2-medium result requires multi-seed replication"

### W4 — FNR=0 独立证据：**已完成**

- `experiments.tex:176` — 6 ground-truth pairs "validated independently by the first-differencing diagnostic"
- `experiments.tex:186` (Table caption) — 明确标注 FNR 基于独立验证的 ground truth
- `method.tex:111-113` — 专门段落 "Independent validation of ground truth"，解释 first-differencing 检验的独立性
- FNR=0 声称限定于 Tier 3 (K≥4/5, S≥3/4)，Tier 4 明确标注 FNR=50%

### α=0.25 GPT-2m 结果：**无占位符**（正确）

α=0.25 的所有提及都是 Pythia-410M 的结果（3-seed 均值±std），未发现 GPT-2m + α=0.25 的占位符或未完成内容。

---

### 总结

| 项目 | 状态 |
|------|------|
| GPT-2m 整合 | ✅ 已写入（narrative 形式，无独立 Table） |
| W1 T notation | ✅ 已修复 |
| W2 batch_size 注释 | ✅ 已修复 |
| W3 claim 天花板 | ✅ 措辞已收敛，无过度声称 |
| W4 FNR=0 独立证据 | ✅ 已修复 |
| α=0.25 GPT-2m 占位符 | ✅ 无（正确行为） |

**Step 5 的 W1-W4 修复 + GPT-2m 整合均已完成。** 论文当前将 GPT-2m 结果定位为 "preliminary single-seed" 证据，写在 discussion 中而非主实验表格——这与只有 single-seed α=1.0 数据的现状一致。

---
