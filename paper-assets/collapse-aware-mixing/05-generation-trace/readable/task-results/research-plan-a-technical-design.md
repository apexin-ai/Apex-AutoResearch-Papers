# research plan a technical design

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_a_technical_design_20260514T020152_result.json`
- **Structured JSON:** [`98915bc327b089ad0e8a.json`](../../sessions/98/98915bc327b089ad0e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。

核心结论：

1. **信号选择**：Unigram entropy 作为控制信号，在 generated text 上计算，每 5M tokens 一次。计算本身 <0.1s（CPU），瓶颈是生成 sample tokens（~1.7 min for 100K tokens）。

2. **PI 控制器**：Kp=0.15, Ki=0.02, setpoint=6.24（G0 baseline × 0.9），带 conditional integration anti-windup。参数基于 v7 数据的过程增益分析（K_process ≈ 1.5）得出。

3. **代码改动量极小（~9h）**：`controlled_pipeline.py` 已实现完整 PI 控制循环，核心改动仅需将 spectral rank 信号替换为 n-gram entropy。

4. **实验周期 ~12 天**（1× RTX PRO 6000）：两阶段策略——Phase 1 单 seed 筛选 5 策略（5.4 天），Phase 2 三 seed 验证 top 2-3（6.5 天）。生成占 74% 时间。

5. **待 Director 决策**：GPU 预算确认、是否集成 vLLM 加速、seed=0 复现实验是否为前置依赖。

---
