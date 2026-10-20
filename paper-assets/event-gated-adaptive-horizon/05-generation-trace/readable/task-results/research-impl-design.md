# research impl design

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_impl-design_20260513T010822_result.json`
- **Structured JSON:** [`eb4d4001a2043dbbd75c.json`](../../sessions/eb/eb4d4001a2043dbbd75c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入 `artifacts/implementation_design.md`，覆盖全部六个模块：

- **Module A**: RSSM 修改方案 — `img_step` 增加 Dt embedding 输入（`networks.py:208-233`），`inp_dim` 扩展，config 新增 `gate_*` 超参数
- **Module B**: EventGate 类 — 2层 MLP + Gumbel-Softmax over {1,...,8}，温度从 1.0 线性退火到 0.5，在 `_imagine` 循环中每步调用
- **Module C**: Gate 监督 — 基于 `||feat_t - feat_{t-1}||_2` 生成软标签，cross-entropy loss，stop-gradient 隔离 RSSM
- **Module D**: 适配 λ-return — `r_cum = r * Dt`，`γ^Dt` 折扣调整，新增 `lambda_return_variable_dt` 函数（`tools.py`）
- **Module E**: Collapse 防护 — entropy bonus + 三阶段 curriculum（0-50K 冻结 / 50K-150K ramp / 150K+ 自由）+ 5 个监控指标
- **Module F**: Replay 策略 — 推荐不修改 buffer，RSSM 通过 embedding 学习 Dt 语义；备选 post-sampling temporal skip

文档包含精确的文件/函数/行号引用、完整伪代码、ASCII 架构图、超参数搜索范围表，以及 6 项风险分析。

---
