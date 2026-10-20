# paper final rw coverage

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-rw-coverage_20260522T184708_result.json`
- **Structured JSON:** [`ba35d39741bcbf4e6a77.json`](../../sessions/ba/ba35d39741bcbf4e6a77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个目录完全同步，无需修改。以下是覆盖度检查结果。

---

## 覆盖度检查结果

### 1. Reward Hacking 核心引用

| 引用 | bib | related_work.tex | 状态 |
|------|-----|-------------------|------|
| Manheim & Garrabrant taxonomy | ✅ `manheim-goodhart-taxonomy` | ✅ L17, L25 | OK |
| Skalse et al. (formal definition) | ✅ `skalse-reward-hacking` | ✅ L17 | OK |
| METR reward hacking | ✅ `metr-reward-hacking` | ✅ L21 | OK |
| Gao et al. overoptimization scaling laws | ✅ `gao-reward-overoptimization` | ✅ L17 | OK |
| Goodhart 1975 原始论文 | ❌ | ❌ | **可选** — ML 顶会惯例引 Manheim taxonomy 即可 |
| Strathern 1997 | ❌ | ❌ | **可选** — 同上 |

### 2. Neurosymbolic Reasoning + RL

| 引用 | 状态 |
|------|------|
| FOLIO 原始论文 | ✅ L7 |
| LLM-solver pipelines (SatLM, Logic-LM, LINC, FoVer, LoRP) | ✅ L5 |
| RL+solver (mellgren-prolog-grpo, logic-rl, DeepSeek-Prover-V1.5, DeepSeek-R1) | ✅ L5 |
| AlphaProof, DeepSeek-Prover-V2 | ✅ L6 |

覆盖完整，无遗漏。

### 3. 2025-2026 Concurrent Work

已引用的（共 10 篇 concurrent work）：
- spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking (L21)
- tarek2025reward, pronesti2026beyond (L21)
- yue2025rl-reasoning (L21)
- helff2026gaming (L22-23)
- khalifa2026countdown (L24)
- wilhelm2026monitoring (L26)

**WebSearch 发现的未引用论文（供 Director 判断是否添加）：**

| 论文 | arXiv | 一句话 | 建议 |
|------|-------|--------|------|
| Wang et al. "Detecting and Suppressing Reward Hacking with Gradient Fingerprints" (GRIFT) | 2604.16242 | 梯度指纹检测隐式 reward hacking，文本 CoT 监控无法捕获 | 低优先 — 方法层面不同（gradient vs. LOO），且已有 IPT/Wilhelm 两种对比方法 |
| Wang et al. "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort" (TRACE) | 2510.01367 | 截断 CoT 测量推理 effort 以检测隐式 hacking | 低优先 — truncation-based，与 STA 的 LOO 方法正交 |
| Wu & Tang "When Reward Hacking Rebounds" | 2604.01476 | 发现 RLVR 三阶段 rebound pattern（尝试→撤退→反弹成功 hack） | 中等 — rebound 动态与论文的 training curve collapse 有呼应，但在 coding tasks 上 |
| Wang & Huang "Reward Hacking as Equilibrium under Finite Evaluation" | 2603.28063 | 证明 reward hacking 是结构性均衡而非 bug | 低优先 — 纯理论，与实证工作距离远 |

**结论：无关键缺失。** 已有引用密度对 EMNLP 8 页论文已经很高（related work 段落内引用 30+ 篇），添加更多可能导致臃肿。上述 4 篇均为 nice-to-have。

### 4. Wilhelm et al. (2026) 互补性讨论

L26: `"Complementarily, \citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic."`

清晰区分了：
- **Wilhelm**: generation-time detection via internal activations
- **STA**: post-training structural diagnostic (LOO)
- 互补关系明确

**无需修改。**

---

## 总结

- **实际修改：0 处** — 覆盖度检查通过，无关键缺失
- **两个目录同步状态：** `related_work.tex` 和 `references.bib` 完全一致
- **Director 决策项：** 上述 4 篇 2025-2026 论文是否需要添加（建议不添加，当前密度已足够）

---
