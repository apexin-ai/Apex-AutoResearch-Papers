# research vla probing beyond vision

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vla-probing-beyond-vision_20260515T135955_result.json`
- **Structured JSON:** [`f7d4882a16b378e56599.json`](../../sessions/f7/f7d4882a16b378e56599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注册工具不可用，文件已写入 artifacts 目录。

调研完成。文件位于 `artifacts/literature_map_probing.md`，覆盖 14 篇论文，5 个方向。

**核心发现**：

多篇论文（Grant 2026, VLM4VLA 2025, LIBERO-Plus 2025）独立验证了你遇到的 "vision encoder dominates" 问题。关键突破口来自 Grant et al. 的发现：**在 LIBERO-Goal suite 中（多个 goal 共享同一 scene），language 编码变得关键**（94%→10% under wrong prompts）。

**Top-3 推荐 probing task**：

1. **Instruction-Conditioned Probing on LIBERO-Goal**（2-3天）— 同一视觉场景、不同 instruction，probe 预测 instruction identity。最快验证 LLM 的独特贡献
2. **Counterfactual Activation Injection**（3-5天）— 注入 wrong-prompt activations，测量 probing accuracy 下降幅度作为 language contribution 度量
3. **Cross-modal Causal Tracing**（5-7天）— 扰动 visual tokens 后逐层恢复，追踪 LLM 层中非视觉来源的 task structure 信息

建议先做 Task 1，在 LIBERO-Goal（而非 Spatial/Object）上做 instruction identity probing，2-3天可出结果。

---
