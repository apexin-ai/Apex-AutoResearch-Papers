# analysis phi3v r2 seed expansion

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phi3v_r2_seed_expansion_20260520T093900_result.json`
- **Structured JSON:** [`a328dd4a473d026b6d59.json`](../../sessions/a3/a328dd4a473d026b6d59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

**状态**: SUCCESS — 实验正常完成，无错误。

### 核心数据（15-seed 合并）

| 指标 | 数值 |
|------|------|
| Peak layer | **L11** |
| Peak R² | **0.634 ± 0.009** (95% CI: [0.629, 0.639]) |
| Plateau (L10-L17) | 0.631 ± 0.003 |
| L0 (baseline) | -0.330 |
| L32 (exit) | 0.551 |
| CI 收窄 | **47.5%**（±0.010 → ±0.005） |

### 跨架构对比（15-seed vs 15-seed）

| | OpenVLA (Llama-2) | Phi3V (Phi-3-mini) |
|--|---|---|
| Peak layer | L9 | L11 |
| Peak R² | 0.637 | 0.634 |
| **Δ** | **0.003** | |
| Inverted-U | ✓ | ✓ |

两个架构 peak R² 几乎一致（Δ=0.003），都在中间层 peak，都呈 inverted-U shape。

### 判断

- Inverted-U 确认 ✓
- CI 收窄 48% ✓（额外 positive 证据）
- 跨架构 peak 收敛 ✓

Registry 已更新为 DONE/success，分析报告已注册为 artifact。

---
