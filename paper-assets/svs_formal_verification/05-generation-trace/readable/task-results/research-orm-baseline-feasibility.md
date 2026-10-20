# research orm baseline feasibility

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_orm-baseline-feasibility_20260514T105103_result.json`
- **Structured JSON:** [`eb70cdae9c2350282af3.json`](../../sessions/eb/eb70cdae9c2350282af3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心结论：

**推荐方案 A+B 组合（2-3 天）**：

1. **LogicReward-Qwen3-8B**（ICLR 2026）——逻辑推理专用 reward model，用 theorem prover 做 step-level 监督训练，8B 可单卡 5090 运行，**最直接相关的 baseline**
2. **FoVer-PRM**（ACL 2026 Findings）——用 Z3 形式验证生成训练数据的 PRM，与 SVS 方法论（Z3 验证）天然对应，对比价值高
3. **GenRM prompt-based**（Qwen3-8B / DeepSeek V3.2 API）——零训练方案，用 CoT 生成 verification rationale

不推荐从头训练轻量 ORM（方案 C），因为已有 LogicReward 和 FoVer 这两个逻辑推理专用模型，再训的边际收益不高。

---
