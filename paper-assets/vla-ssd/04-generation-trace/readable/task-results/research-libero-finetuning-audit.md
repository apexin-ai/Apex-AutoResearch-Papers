# research libero finetuning audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero-finetuning-audit_20260516T023809_result.json`
- **Structured JSON:** [`e63ec21eb37758699a55.json`](../../sessions/e6/e63ec21eb37758699a55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `/root/autodl-tmp/vla-ssd/results/architecture_audit/libero_finetuning_audit.md`。

核心结论：

**两个 checkpoint 都是 base OpenVLA-7B，仅在 Open-X-Embodiment 上预训练，未经任何 LIBERO fine-tuning。**

关键证据：
1. 两个 config.json 的 `norm_stats` 只有 25 个 Open-X-Embodiment 数据集，`grep -i "libero"` 均为空
2. README.md 明确标注来源为 `openvla/openvla-7b`（Open-X 970K episodes）
3. 服务器上无 fine-tuning 脚本、训练日志、trainer_state 等产物
4. "Trained" vs "Untrained" 的区别是 LLM backbone 是否被随机重初始化，不涉及 LIBERO 训练

这对论文其实是**正面的**——分析的是从未见过 LIBERO 数据的模型，发现的结构化表征来自预训练泛化能力。论文应明确写 "without any LIBERO-specific fine-tuning"。

---
