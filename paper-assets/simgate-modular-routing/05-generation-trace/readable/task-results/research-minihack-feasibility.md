# research minihack feasibility

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_minihack-feasibility_20260519T110859_result.json`
- **Structured JSON:** [`75eb6cc54bb98cde203b.json`](../../sessions/75/75eb6cc54bb98cde203b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report saved to `artifacts/minihack_feasibility_report.md`.

**核心结论**:

1. **首选 MiniHack Navigation Tasks (via BALROG)**
   - 有现成的 text wrapper (`nle-language-wrapper`)，LLM 可直接用文本交互
   - Roguelike 是 permadeath 的经典范例，审稿人无需解释
   - BALROG 框架支持 vLLM 本地推理，可复用 Qwen2.5-7B
   - 预估 LLM death rate 30-60%，与 ScienceWorld 的 42% 可比

2. **备选 Crafter**（如果 MiniHack 导航任务 death rate 不在合理区间）
   - 已在服务器验证过：100% random death, 17 actions, semantic map 可建 heuristic
   - 缺点：无原生 text obs，需 image-to-text wrapper

3. **排除 ALFWorld**（无 death 机制）和 **BabyAI**（death 仅限 lava，太窄）

4. **排除 MiniHack Skill/Quest tasks**（所有 LLM 0% 成功率，无诊断价值）

**关键风险**: Day 2 结束时需决策——如果 MiniHack 导航任务 LLM death rate <20% 或 >90%，立即切 Crafter。

**时间线**: 5 天可完成 100 episode pilot（Day 1 环境搭建 → Day 4 full run → Day 5 分析写入论文）。

---
