# research webshop sciworld survey

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_webshop-sciworld-survey_20260512T105740_result.json`
- **Structured JSON:** [`6e0b69b581d8ad1b39a4.json`](../../sessions/6e/6e0b69b581d8ad1b39a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心发现：

**三分类 taxonomy 可跨环境通用**，但有几个关键适配点：

1. **WebShop** — episode 只有 10 步，Action/Verification/Planning 边界更模糊；reward 是连续值（属性匹配分数），preference pair 构建逻辑需改；环境搭建最复杂（需 web server + 搜索索引）

2. **ScienceWorld** — episode 长度按任务类型从 10 到 120 步不等，三分类的纠正跨度区分反而更清晰；reward 取 episode 内最高值；有 unseen task 泛化测试（task-8/9 训练集中不存在）；安装只需 Java + pip

3. **建议 ScienceWorld 优先扩展**（安装简单、代码改动小、有 unseen 泛化测试做论文亮点），WebShop 其次

4. **γ_e 映射需要跨环境调整** — WebShop 短 episode 需要更激进的 discount，ScienceWorld 变长 episode 可能需要按 T 做归一化

---
