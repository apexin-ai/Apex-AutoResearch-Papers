# writing related work draft

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-draft_20260515T042021_result.json`
- **Structured JSON:** [`6968c75d184ea8d4a475.json`](../../sessions/69/6968c75d184ea8d4a475.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Related Work 草稿已生成，保存在 `artifacts/paper_drafts/related_work_draft.md`。

结构与内容概要：

- **2.1 World-Model RL**: DreamerV1/V2/V3/V4 系列 + MBPO/MOPO model exploitation + TD-MPC2 对比，定位我们在 DreamerV3 imagination 范式内诊断特定失败模式
- **2.2 Temporal Abstraction**: Options → FiGAR/TempoRL（model-free）→ Director/THICK/Hieros/LS-Imagine（hierarchical）→ **TAWM 重点对比**（MPC 下 Δt conditioning 有效 vs 我们发现 imagination-based AC 中有害）→ 时间离散化理论（Tallec, SAR, MTS3）
- **2.3 Value Overestimation & Delusional Bias**: Thrun/Double-Q/TD3/SUNRISE → **Lu & Schuurmans 精确区分**（他们：policy-class constraints 下 Q-backup inconsistency；我们：temporal conditioning + model imprecision 下的 systematic overestimation）→ 近期 MBRL value dynamics 工作
- **2.4 Multi-Step Prediction & Compounding Error**: Venkatraman/Asadi/Ke/Lambert 经典 + Frauenknecht rollout quality → 我们的发现：compounding error 不是 root cause，trained dt_embedding 才是

所有引用均来自 `literature_map.yaml`，格式为 `\citet{}`/`\citep{}`。末尾 overall positioning 段总结文献 gap 并引出贡献。

`register_artifact` 工具不可用，文件已直接写入产出目录。

---
