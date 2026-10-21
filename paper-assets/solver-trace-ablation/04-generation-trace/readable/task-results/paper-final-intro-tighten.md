# paper final intro tighten

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-intro-tighten_20260522T184655_result.json`
- **Structured JSON:** [`74349f7f28db62590261.json`](../../sessions/74/74349f7f28db62590261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 修改清单

### Edit 1: 开篇 hook（L4-6）
**目的**：以反直觉发现开场，而非程序性定义

| | 内容 |
|---|---|
| **Before** | `Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.` / `This treats all proofs as equal: ...` / `Under RL, this indifference becomes an active vulnerability. The optimizer exploits...` |
| **After** | `A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.` / `The root cause is evaluation by a single criterion---...---which treats all proofs as equal: ...` / `Under RL, this indifference becomes an active vulnerability; the optimizer exploits...` |

变更点：(a) 新增 hook 句直述悖论；(b) 原两句合并为一句用 em-dash 嵌入；(c) 句号改分号连接更紧凑。

### Edit 2: 去冗余——L18 与 L29 重复陈述 Goodhart 发现
**目的**：L18 原文预述了"diagnostic → gameable"，与 ¶4 L29 完全重复。改为 forward reference，让 ¶4 首次揭示该发现。

| | 内容 |
|---|---|
| **Before** | `...our contribution is the empirical finding that the same structure making ISR informative as a diagnostic also makes it gameable as a reward.` |
| **After** | `...our contribution is its systematic application to neurosymbolic outputs, where it reveals a diagnostic--optimization asymmetry (§3--§4).` |

### Edit 3: 压缩 L28——删除冗长括注和三重同义
**目的**：原句有嵌套括注 + "structural collapse"/"component necessity collapses"/"near-complete structural degeneration" 三次说同一件事。

| | 内容 |
|---|---|
| **Before** | `Applied post-hoc, ISR exposes a structural collapse hidden from prove rate (Figure 1): as execution scores climb, component necessity collapses (per-sample mode classification, rather than the aggregate ISR scalar, provides the primary diagnostic evidence; §3), revealing that high prove rate coexists with near-complete structural degeneration.` |
| **After** | `Applied post-hoc, ISR exposes a collapse hidden from prove rate: as execution scores climb, component necessity drops to near zero (Figure 1; §3).` |

### Edit 4: Case study scoping——L30 泛化声明加限定
**目的**：原文 "In this setting" 模糊，末尾断言 "are easier to observe than to optimize" 读起来像普遍定律。

| | 内容 |
|---|---|
| **Before** | `In this setting, the asymmetry persists across logic types, dataset families, reward doses, and random seeds: structural proxies for reasoning quality are easier to observe than to optimize.` |
| **After** | `In our Qwen3-4B experiments, the asymmetry persists across logic types, dataset families, reward doses, and random seeds, suggesting that structural proxies for reasoning quality are easier to observe than to optimize.` |

---

## 未修改的可选改进建议（供 Director 判断）

1. **L11 "complementary problem" 措辞**：`addresses a complementary problem but offers no training-time diagnostic` 中 "complementary problem" 含义模糊（互补的什么 problem？），可改为 `detects gaming at inference time but offers no training-time diagnostic`，更直接。未改是因为现有措辞不影响理解。

2. **Figure caption 密度**：L23-24 的 caption 信息量很大（4 个观察点 + 2 个 section 引用），在 intro 首图中可能让读者 overwhelm。可考虑只保留核心信息（exec-only collapse + ISR gaming），细节留给正文。未改是因为 caption 不在本次任务的 4 项检查范围内。

3. **L4 hook 的 scope 问题**：新 hook "A neurosymbolic reasoner can achieve rising prove rate while..." 是泛指，理论上应说 "In our experiments, a neurosymbolic reasoner..."。但开篇第一句加 scoping 会杀死 hook 效果，且该现象的逻辑基础（execution-only reward 不区分 shortcut）确实是通用的，不只限于 Qwen3-4B。保留为通用表述，让后文（L30, L33）做具体 scoping。

---
