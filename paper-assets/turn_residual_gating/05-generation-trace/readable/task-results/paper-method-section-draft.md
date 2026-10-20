# paper method section draft

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method_section_draft_20260518T201248_result.json`
- **Structured JSON:** [`6d7ff93e4737ae6e6e2a.json`](../../sessions/6d/6d7ff93e4737ae6e6e2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

草稿已保存到 `artifacts/paper/method_section_draft.md`。

内容覆盖四个小节：
- **3.1** 形式化定义了多轮对话序列、goal token set、GAR 指标，并衔接 Dongre et al. 的诊断结论作为动机
- **3.2** 描述了 ThreadGate 的残差门控公式 $x_l = x_{l-1} + g_l \cdot f_l(x_{l-1})$、GateNetwork 结构（down-proj + TurnEmbedding + 2-layer MLP + sigmoid）、与 frozen LLM + LoRA 的集成方式、参数量分析（~1.67M, 0.02%）
- **3.3** 三部分 loss 的完整公式和设计理由：NTP（assistant-only masking）、MSE-target GAR loss（$\tau=0.5$，解释了为什么不用 maximize）、gate diversity loss（$\sigma_{\min}=0.05$，ReLU 触发机制）、可微 GAR 的 hook 实现
- **3.4** Uniform Gate baseline 的设计（常量向量替换 TurnEmbedding）及其消融目的

注意：paper_framing 中声称的 "<0.01% 参数" 与实际计算不符（实际约 0.02%），草稿中已按真实数据报告。

---
