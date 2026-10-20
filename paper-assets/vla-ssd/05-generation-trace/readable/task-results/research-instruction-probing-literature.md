# research instruction probing literature

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_instruction-probing-literature_20260515T171543_result.json`
- **Structured JSON:** [`68abefa51d355c0a7261.json`](../../sessions/68/68abefa51d355c0a7261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。产出已保存到 `artifacts/literature_survey_instruction_probing.md`。

## 核心发现

**14 篇论文覆盖 4 个方向**，关键结论：

### "Vision dominates" 已是共识
Grant 2026、VLM4VLA 2026、LangForce 2026 都独立验证了 VLA 在标准 benchmark 上几乎忽略 language。LangForce 将此命名为 **Information Collapse**——当 vision 足以预测 action 时，language 信号被 shortcut 掉。

### LIBERO-Goal 是突破口
Grant et al. 2026 是最直接的相关工作：在 LIBERO-Goal 上，正确 prompt 97-100% vs 错误 prompt 0-10%，同时发现 **"encoded but not used" paradox**（π0.5 L17 有 99.3% prompt accuracy 但行为不变）。

### 我们的 novelty 空白

| 维度 | 已有工作 | 我们的差异 |
|------|---------|-----------|
| 分析方法 | Grant: behavioral intervention | **Diagnostic probing (trained vs untrained)** |
| 粒度 | Grant: 单层 prompt accuracy | **Layer × timestep heatmap** |
| 对比 | 各论文只看单 regime | **Vision-sufficient → vision-ambiguous 系统对比** |
| 训练效果 | 无人做 | **Trained vs untrained 回答 "VLA 训练改变了什么"** |

### 最直接竞争者

1. **Grant et al. 2026** — 高威胁但方法正交（intervention vs probing）
2. **LangForce 2026** — 互补（他们提理论+修复，我们提 representation 证据）
3. **Häon et al. 2025** — 互补（causal steering vs diagnostic probing）

**底线：representation probing × vision-ambiguous scenarios × trained vs untrained comparison 这个交叉点目前是空白，这是我们的位置。**

---
