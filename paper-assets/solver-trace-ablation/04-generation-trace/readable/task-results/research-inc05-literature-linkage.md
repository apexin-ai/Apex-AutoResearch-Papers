# research inc05 literature linkage

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_inc05-literature-linkage_20260515T140825_result.json`
- **Structured JSON:** [`98e67ab2056e810e1b35.json`](../../sessions/98/98e67ab2056e810e1b35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已注册。核心结论：

**4 篇论文映射到 INC-05 发现**：
1. **Laidlaw et al. (2025) "Correlated Proxies"** — **新，需加入 literature_map**。ICLR 2025 Spotlight，提供 reward hacking 的 correlation-breakdown 形式化定义，直接框架化"ISR 优化后 genuine rate 低于 random baseline"。
2. **Yang et al. (2025) "Spurious Rewards"** — 已在 lit map。我们的发现是其强化版：不是 random ≈ truth，而是 structured < random。
3. **Manheim & Garrabrant (2019)** — 已在 lit map，但当前标注为 extremal Goodhart；INC-05 更准确映射到 **regressional Goodhart**（noise exploitation, 无需 distributional shift）。
4. **Pan et al. (2022)** — 已在 lit map。"more capable agents exploit misspecifications more" 直接解释为何 ISR-optimized model 比 random baseline 的 genuine rate 更低。

产出文件含 4 条可直接用于论文的 suggested claims。

---
