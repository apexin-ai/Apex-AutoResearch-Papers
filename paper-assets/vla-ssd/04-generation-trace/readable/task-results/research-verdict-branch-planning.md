# research verdict branch planning

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verdict-branch-planning_20260515T132740_result.json`
- **Structured JSON:** [`37f783917e0bc0ccd099.json`](../../sessions/37/37f783917e0bc0ccd099.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

paper_framing.md 和 ideas.md 不存在。基于 ROADMAP 和 memory 制定计划。

---

## 分支 A: PASS / CONDITIONAL

### 即刻（verdict 后 1 小时内）

1. **Effect size 评估** — 计算 VLA vs DINO Δρ(per-task mean)。若 < 0.05，contribution 强度不足（ROADMAP 已标注），需立即调整 framing 为 mechanistic finding 而非 performance improvement
2. **Layer-wise ρ profile 可视化** — 绘制 trained vs untrained vs DINO 三条曲线（33 layers），这是论文必展图（ROADMAP 明确要求）。不占 GPU，纯 CPU 分析
3. **空闲 GPU 启动 cross-trajectory 补充分析** — VLA cross-traj ρ vs DINO cross-traj ρ(0.65)。若 VLA 显著更高 → "VLA learns transferable progress representations beyond visual similarity"，强化 story

### 短期（1-3 天内，deadline: abstract May 26）

1. **创建 paper_framing.md** — 根据 verdict 数值确定 story arc：
   - PASS + Δρ ≥ 0.05: "VLA representations encode task progress → zero-external-model quality scoring"
   - CONDITIONAL (VLA < DINO): "Mechanistic finding: VLA training restructures but doesn't amplify temporal distance signal → DINO-based pipeline"
2. **Hierarchical quality scoring 原型**（占一卡）— 这是 pipeline 第二阶段，用 probe score 对 demo 分层。需要设计 scoring function 并在 LIBERO-Long 上验证区分度
3. **Related work 文献收集** — temporal representation in robotics, demo quality scoring (IW-SFT, DAgger variants), VLA probing (concurrent work survey)
4. **Figure 规划** — 至少需要：(1) pipeline overview, (2) layer-wise ρ profile, (3) trained vs untrained Δρ per task, (4) quality scoring 示例。前三个 MVP 数据即可画

### Control B 完成后

- 合并 Control B 结果到 verdict report（预期 ρ≈0，确认 probe 非随机拟合）
- 释放该卡给 curriculum-weighted LoRA 预实验（pipeline 第三阶段）

---

## 分支 B: FAIL

### 即刻（verdict 后 1 小时内）

1. **Layer-wise ρ 逐层诊断**（最高优先级，不额外占 GPU）— 检查是否存在局部信号：
   - 如果某些层 ρ > 0.5 但 best layer 的 Δρ(trained-untrained) ≤ 0.1 → 信号来自 vision encoder 而非 LLM 训练，VLA 假设失败但 representation 仍可用
   - 如果所有层 ρ < 0.5 → 信号本身不存在，token aggregation 或 probe 架构可能是瓶颈
2. **Token aggregation 变体**（空闲 GPU）— 当前仅用 last_preaction token。features 已包含 `image_mean`，无需重新提取：
   - 切换到 image token mean-pooling（memory 中已标注为对比方案）
   - 如果 image_mean 显著优于 last_preaction → 信号在视觉 token 而非 LLM 决策点，重要 mechanistic finding

### 中期诊断（如果上述未解救，1-2 天内）

1. **Probe 架构升级** — 当前是线性 probe。换 2-layer MLP（hidden=256, ReLU）。如果 MLP 大幅优于 linear → 信号存在但非线性编码，需要更强 probe
2. **Layer 组合** — concatenate top-3 层 hidden states 后训练 probe，测试跨层信息互补
3. **Per-task 拆分分析** — 某些 task 可能天然更难/更容易（DINO per-task range 0.41-0.68），找出哪些 task 失败最严重，是否有系统性模式

### Pivot 方向（诊断全部失败时）

1. **DINO-V2 pipeline**（最小代价 pivot）— DINO 已有 per-task mean ρ=0.554, cross-traj ρ=0.65, subtask AUC=0.9717。放弃 "VLA self-scoring" 改为 "frozen vision encoder scoring"，pipeline 后两阶段不变。论文 story 变为 "Can pretrained vision features score robot demos without task-specific training?"
2. **VLA + DINO 融合** — concatenate VLA hidden state + DINO features 作为 probe 输入。如果融合 > 单独 DINO → VLA 仍有互补信息，story 可以保住
3. **终止条件** — 如果 DINO pipeline 也无法做出有区分度的 hierarchical scoring（阶段二失败），项目 pivot 到完全不同的方向或放弃 CoRL

---

**关键时间约束**: abstract May 26（11 天），paper May 29（14 天）。Branch B 的诊断窗口最多 2 天，之后必须决定 pivot 还是终止。

---
