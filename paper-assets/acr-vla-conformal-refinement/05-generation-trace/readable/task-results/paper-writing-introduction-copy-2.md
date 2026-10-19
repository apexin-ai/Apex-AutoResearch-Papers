# paper writing introduction

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260513T214507_result.json`
- **Structured JSON:** [`a1533288e9efca49b7da.json`](../../sessions/a1/a1533288e9efca49b7da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入 `artifacts/_project/paper/introduction.tex`。

结构概要：
- **Para 1**: LIBERO 97-99% → LIBERO-Plus 50-60% 的鲁棒性缺口
- **Para 2**: Training-time (SRPO/RobustVLA/DiG-Flow) vs inference-time (ReconVLA/SAFE/UPS/CP-in-the-Loop/A2C2) 的分类和各自局限，收束到 "no method uses structured per-DOF uncertainty for correction"
- **Para 3**: Core insight — 40D CGS features 保留跨维度协方差结构，MVP 实验数据（6.7%/16.7%/22-24%）作为 evidence
- **Para 4**: ACR-VLA 三组件概述 + 明确声明 CP 用作 feature extractor 而非输出覆盖保证（应对 Reviewer Concern #7）
- **Para 5**: 3 条 contributions，enumerate 格式，主实验结果用 `XX.X pp` / `YY.Y%` 占位

约 720 words，符合 ICLR ~1.5 column 标准。所有引用均来自指定 bibtex_key 列表，无编造。术语与 method section 一致（CGS/ACI+COC/CRM/SmolVLA/K=10/40D/250K params）。

---
