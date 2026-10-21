# research vla codebase survey

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vla_codebase_survey_20260519T160639_result.json`
- **Structured JSON:** [`d64d1c2f8038dfcacc0b.json`](../../sessions/d6/d64d1c2f8038dfcacc0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/report_vla_codebase.md`。核心结论：

**推荐 OpenVLA-OFT 作为 MVP 基座**，主要理由：
- Action Head 已是独立 `nn.Module`，添加 SDF decoder 遵循现有 pattern，改动最小
- Hidden states 访问开箱即用（`output_hidden_states=True`），32 层 × 4096 维全序列可提取
- 单次前向 + L1 回归，梯度可直接回传——不像 openpi 需要处理 10 步 ODE solver 的梯度
- 纯 PyTorch 生态

**openpi 作为备选**——模型更小 (2.5B vs 7B)、社区更活跃、预训练数据量更大，但 JAX 为主框架 + flow matching ODE 梯度处理增加集成复杂度。

---
