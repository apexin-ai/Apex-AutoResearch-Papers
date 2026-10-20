# research openvla libero goal compat

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openvla-libero-goal-compat_20260515T160816_result.json`
- **Structured JSON:** [`21298365632fd7dcbdac.json`](../../sessions/21/21298365632fd7dcbdac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/openvla_libero_goal_compat.md`。以下是核心结论摘要：

---

### 五个问题的明确结论

**Q1: OpenVLA-7B 训练数据**
- 训练于 OXE 的 25 个**真实世界**数据集（~970K trajectories）
- **不含任何 LIBERO 数据**（代码级、论文级、数据性质三重确认）

**Q2: LIBERO-Goal vs LIBERO-10 场景重叠**
- **无重叠。** LIBERO-Goal 10 个 task 共享一个 kitchen tabletop scene；LIBERO-10 跨 7 个不同 scene（KITCHEN/LIVING_ROOM/STUDY）
- Action space (7-DoF)、image resolution (128×128)、HDF5 格式完全一致，`extract_features.py` 无需修改

**Q3: Zero-shot 特征提取可行性**
- **可行。** 我们做的是 probing hidden states，不需要 action 输出正确
- 不需要 fine-tune，且**不应该** fine-tune（会引入 memorization confound）

**Q4: Grant et al. 2026**
- 用 **fine-tuned** models 做 behavioral evaluation（394K rollouts）
- LIBERO-Goal 效应量极大：OFT 100%→10%，GR00T 97%→0%，X-VLA 94%→10%
- π0.5 是例外（83.3%→76.7%，不显著）
- 他们的 linear probe paradox（99.3% prompt classification but no behavioral effect）是我们的切入点
- **我们的差异**：pretrained vs fine-tuned, representational vs behavioral, trained vs untrained comparison

**Q5: Reviewer 数据污染风险**
- **无风险。** OpenVLA-7B 预训练不含 LIBERO → probe 结果反映 true representational structure，非记忆
- 这使我们的 story 比 Grant et al. 更 clean：测试的是 VLA 训练的**泛化** instruction encoding

---
