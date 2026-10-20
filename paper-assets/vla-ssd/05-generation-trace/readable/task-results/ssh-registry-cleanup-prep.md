# ssh registry cleanup prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_registry-cleanup-prep_20260515T171117_result.json`
- **Structured JSON:** [`df2d2064b526e56188c5.json`](../../sessions/df/df2d2064b526e56188c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Report.md (Handover 2026-05-15)

**运行中**: `lg_extract_untrained`, `lg_extract_trained`, `lg_extract_untrained_r2` — 均无状态/指标信息

**待处理**: `mvp2_action_probe` — VLA trained model hidden states encode action prediction knowledge

**近期结论**: MVP-2 action-delta 系列三个实验均 success，但 gate 判定整体 FAIL（DINO ≈ trained VLA）

**趋势**: 成功 12 / 负向 2 / 失败 0 / 共 14 次实验。overall_R² = 0.0604 ↑

**下一步**: 无活跃 idea，需通过 ideas.md 添加

---

## ROADMAP.md 摘要

**核心结论**: LIBERO-10 上 VLA 训练表征贡献不显著（vision encoder 主导），项目已 pivot 到 **LIBERO-Goal**（D015 决策），期望在 vision-ambiguous 场景中，VLA 的 language grounding 能体现差异。

**当前阶段**: MVP-2 完成 → Pivot to LIBERO-Goal
- MVP-1 Temporal Distance: G2 FAIL
- MVP-2 Action Prediction: G2/G3 FAIL
- MVP-2 Action-Delta: G3-delta FAIL（DINO ≈ trained）
- 跨 MVP 一致发现: layer stability（trained 31/33 层有效 vs untrained ~15/33）

**近期任务（LIBERO-Goal pivot）**:
1. 确认 LIBERO-Goal 数据可获取 + scene overlap
2. 确认 OpenVLA checkpoint zero-shot 能力
3. 特征提取（trained + untrained + DINO，双卡并行）
4. Instruction-conditioned probing（same-scene/different-goal）
5. 分析 + 可视化 + 论文初稿

**时间线**: CoRL 2026 — Abstract DDL **May 26**（剩 11 天），Paper DDL **May 29**（剩 14 天）

**关键风险**: OpenVLA 未训练过 LIBERO-Goal，需检查 scene overlap，必要时 fine-tune

**GPU**: westd-19183, 2×RTX PRO 6000, 当前 0/2 占用

---
